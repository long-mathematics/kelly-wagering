#!/usr/bin/env python3
"""Fetch and preserve the original arXiv v1 sources of the five Kelly papers.

Run from the repository root: python3 scripts/import_arxiv_sources.py
Pre-existing imports are not overwritten.
"""
from pathlib import Path, PurePosixPath
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import gzip
import hashlib
import io
import tarfile
import time

PAPERS = {
    "2603.13581": "implicit-cash",
    "2603.24064": "utility-invariant-support",
    "2603.26620": "parlays-whitrow",
    "2604.11577": "risk-constrained",
    "2604.17577": "quantile-kelly",
}
LIMIT = 100 * 1024 * 1024

def fetch(id_):
    url = f"https://arxiv.org/src/{id_}v1"
    for attempt in range(4):
        try:
            req = Request(url, headers={"User-Agent": "Kelly-Wagering-Arxiv-Source-Archiver/1.0"})
            with urlopen(req, timeout=90) as r:
                payload = r.read(40 * 1024 * 1024 + 1)
            if len(payload) > 40 * 1024 * 1024:
                raise ValueError("Source archive too large")
            return payload
        except (HTTPError, URLError, TimeoutError):
            if attempt == 3:
                raise
            time.sleep(2 ** attempt)

def unpack(payload):
    try:
        arc = tarfile.open(fileobj=io.BytesIO(payload), mode="r:*")
    except tarfile.ReadError:
        if payload[:2] == bytes((31, 139)):
            with gzip.GzipFile(fileobj=io.BytesIO(payload)) as stream:
                data = stream.read(LIMIT + 1)
        else:
            data = payload
        if len(data) > LIMIT or b"\\" not in data:
            raise ValueError("Unexpected source format")
        return {"main.tex": data}
    result = {}
    total = 0
    with arc:
        for entry in arc:
            if entry.isdir():
                continue
            if not entry.isfile():
                raise ValueError(f"Unsafe tar member: {entry.name}")
            p = PurePosixPath(entry.name)
            if p.is_absolute() or ".." in p.parts or any(x in {".git",".github"} for x in p.parts):
                raise ValueError(f"Unsafe tar path: {entry.name}")
            if entry.size < 0 or entry.size > LIMIT:
                raise ValueError(f"Invalid member size: {entry.name}")
            total += entry.size
            if total > LIMIT or len(result) >= 2000 or str(p) in result:
                raise ValueError("Oversized or duplicate source archive content")
            f = arc.extractfile(entry)
            if f is None:
                raise ValueError(f"Unreadable tar member: {entry.name}")
            data = f.read(entry.size + 1)
            if len(data) != entry.size:
                raise ValueError(f"Incorrect member size: {entry.name}")
            result[str(p)] = data
    if not any(name.endswith(".tex") for name in result):
        raise ValueError("No TeX file found")
    return result

def main():
    root = Path(__file__).resolve().parents[1]
    for id_, slug in PAPERS.items():
        folder = root / "papers" / f"{id_}-{slug}" / "arxiv-v1"
        if folder.exists():
            print(f"SKIP {id_}: already imported")
            continue
        raw = fetch(id_)
        files = unpack(raw)
        folder.mkdir(parents=True, exist_ok=False)
        for name, data in files.items():
            path = folder / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        digest = hashlib.sha256(raw).hexdigest()
        manifest = "\n".join("- " + x for x in sorted(files))
        (folder / "SOURCE.md").write_text(
            f"# arXiv:{id_}v1 original submission source\n\n"
            f"Retrieved from https://arxiv.org/src/{id_}v1\n\n"
            f"SHA-256 of downloaded archive: {digest}\n\n"
            "This source snapshot is immutable; later revisions go in separate directories.\n\n"
            f"## Files\n\n{manifest}\n", encoding="utf-8")
        print(f"IMPORTED {id_}v1: {len(files)} file(s), SHA-256 {digest}")

if __name__ == "__main__":
    main()
