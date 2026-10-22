#!/usr/bin/env python3
"""Build committed Kelly PDFs and validate original arXiv source provenance."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "papers.json"
MANIFEST = ROOT / "output/pdf/manifest.json"
BUILDDIR = ROOT / ".build"
SOURCE_DATE_EPOCH = "1791504000"


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def safe(relative: str) -> Path:
    candidate = (ROOT / relative).resolve()
    if not candidate.is_relative_to(ROOT.resolve()):
        raise ValueError(f"Path outside checkout: {relative}")
    return candidate


def catalog() -> list[dict]:
    doc = json.loads(CATALOG.read_text(encoding="utf-8"))
    if doc.get("schema_version") != 1 or len(doc.get("documents", [])) != 5:
        raise ValueError("Expected five catalogued arXiv v1 manuscripts")
    return doc["documents"]


def validate_catalog() -> None:
    docs = catalog()
    for field in ("id", "source", "pdf"):
        vals = [d[field] for d in docs]
        if len(vals) != len(set(vals)):
            raise ValueError(f"Duplicate catalog {field}")
    for d in docs:
        if d["status"] != "arxiv-v1" or d["arxiv_version"] != "v1":
            raise ValueError("Unexpected source version: " + d["id"])
        if d["arxiv"] != "https://arxiv.org/abs/" + d["id"]:
            raise ValueError("Inconsistent arXiv link: " + d["id"])
        if "/arxiv-v1/" not in d["source"]:
            raise ValueError("Non-frozen LaTeX source: " + d["source"])
        source = safe(d["source"])
        target = safe(d["pdf"])
        if not source.is_file() or target.suffix != ".pdf":
            raise ValueError("Missing TeX source or improper output location: " + d["id"])
        actual_git_sha = subprocess.check_output(
            ["git", "hash-object", str(source)], cwd=ROOT, text=True
        ).strip()
        if actual_git_sha != d["source_git_blob_sha"]:
            raise ValueError("Original arXiv v1 source changed: " + d["source"])
        if not (source.parent / "SOURCE.md").is_file():
            raise ValueError("Missing source provenance record: " + d["id"])


def verify_pdfs() -> None:
    if not MANIFEST.is_file():
        raise ValueError("Missing PDF manifest; run make pdf")
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    existing = {r["id"]: r for r in data.get("documents", [])}
    if set(existing) != {d["id"] for d in catalog()}:
        raise ValueError("PDF manifest and catalog disagree")
    for doc in catalog():
        entry = existing[doc["id"]]
        source, pdf = safe(doc["source"]), safe(doc["pdf"])
        if not pdf.is_file() or pdf.stat().st_size < 500:
            raise ValueError("Missing or empty PDF: " + str(pdf))
        if pdf.read_bytes()[:5] != b"%PDF-":
            raise ValueError("Not a valid PDF header: " + str(pdf))
        if sha256(pdf) != entry["pdf_sha256"] or sha256(source) != entry["source_sha256"]:
            raise ValueError("Stale PDF or source manifest entry: " + doc["id"])
        pdfinfo = subprocess.check_output(["pdfinfo", str(pdf)], text=True)
        pages = re.search(r"^Pages:\s+(\d+)", pdfinfo, re.MULTILINE)
        if not pages or int(pages.group(1)) != entry["pages"] or entry["pages"] < 1:
            raise ValueError("Page count mismatch: " + doc["id"])
        print(f"Verified {doc['id']}: {entry['pages']} pages", flush=True)


def build() -> None:
    BUILDDIR.mkdir(exist_ok=True)
    results = []
    for d in catalog():
        source = safe(d["source"])
        dest = safe(d["pdf"])
        work = BUILDDIR / d["id"]
        if work.exists():
            shutil.rmtree(work)
        work.mkdir(parents=True)
        env = dict(os.environ, SOURCE_DATE_EPOCH=SOURCE_DATE_EPOCH,
                   FORCE_SOURCE_DATE="1", TZ="UTC")
        cmd = [
            "latexmk", "-pdf", "-interaction=nonstopmode",
            "-halt-on-error", "-file-line-error", "-no-shell-escape",
            "-outdir=" + str(work), source.name
        ]
        print("Compiling " + d["id"], flush=True)
        result = subprocess.run(cmd, cwd=source.parent, env=env,
                                text=True, capture_output=True, timeout=300)
        (work / "build-console.txt").write_text(
            result.stdout + result.stderr, encoding="utf-8")
        built = work / (source.stem + ".pdf")
        if result.returncode or not built.is_file():
            print((result.stdout + result.stderr)[-9000:], file=sys.stderr)
            raise ValueError("LaTeX build failed: " + d["id"])
        log = (work / (source.stem + ".log")).read_text(errors="replace")
        warnings = [
            line for line in log.splitlines()
            if re.search(r"^!|LaTeX Warning:.*undefined|Citation .* undefined|Reference .* undefined|multiply defined", line)
        ]
        if warnings:
            raise ValueError("Unresolved LaTeX diagnostics: " + d["id"] + "\n" + "\n".join(warnings[:15]))
        info = subprocess.check_output(["pdfinfo", str(built)], text=True)
        match = re.search(r"^Pages:\s+(\d+)", info, re.MULTILINE)
        if not match:
            raise ValueError("Missing PDF page count for " + d["id"])
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(built, dest)
        results.append({
            "id": d["id"], "source": d["source"], "source_sha256": sha256(source),
            "pdf": d["pdf"], "pdf_sha256": sha256(dest), "pages": int(match.group(1))
        })
    MANIFEST.write_text(json.dumps({"schema_version": 1, "documents": results}, indent=2) + "\n")
    verify_pdfs()
    print("All five source PDFs built and manifest verified.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    opts = parser.parse_args()
    try:
        validate_catalog()
        if opts.check:
            verify_pdfs()
        else:
            build()
    except (OSError, ValueError, KeyError, subprocess.SubprocessError) as error:
        print(str(error), file=sys.stderr)
        raise SystemExit(1)
