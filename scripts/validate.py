#!/usr/bin/env python3
"""Check frozen arXiv sources, local Markdown links, and GitHub-safe math."""
from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote
from build_pdfs import ROOT, catalog, validate_catalog

ALLOWED = {
    "Delta", "Gamma", "Phi", "Rightarrow", "ast", "cdot", "beta", "epsilon", "eta",
    "frac", "ge", "in", "infty", "int", "kappa", "lambda", "le",
    "log", "longrightarrow", "mathbb", "mathcal", "max", "min",
    "mu", "pi", "prod", "qquad", "sigma", "sim", "sqrt", "sum",
    "sup", "text", "theta", "to", "varepsilon", "varphi", "zeta",
    "mathrm", "mathscr", "ell", "lbrace", "rbrace", "left", "right",
}


def inspect_expr(expr: str, name: str, line: int) -> None:
    # GitHub Markdown can consume bare * as emphasis before MathJax sees it.
    # Write ^{\ast} for starred superscripts and \cdot for multiplication.
    if "*" in expr:
        raise ValueError(f"Unprotected asterisk in GitHub math: {name}:{line}")
    if "_+" in expr:
        raise ValueError(f"Use braces for positive-part subscript: {name}:{line}")
    if any(ch in expr for ch in "%#&"):
        raise ValueError(f"Unsafe TeX punctuation: {name}:{line}")
    for matched in re.finditer(r"\\([A-Za-z]+|.)", expr):
        command = matched.group(1)
        if command not in ALLOWED:
            raise ValueError(f"Unsupported GitHub math command \\{command} at {name}:{line}")


def strip_inline_code(s: str) -> str:
    return re.sub(r"(" + chr(96) + r"+)(.*?)\1", "", s)


def check_math(text: str, name: str) -> None:
    lines = text.splitlines()
    fenced = False
    displayed = False
    fence = chr(96) * 3
    for index, raw in enumerate(lines):
        line = raw.strip()
        if line.startswith(fence):
            if line == fence + "math":
                raise ValueError(f"Use separate $$ delimiters instead of fenced math: {name}")
            fenced = not fenced
            continue
        if fenced:
            continue
        plain = strip_inline_code(raw)
        if any(x in plain for x in (r"\(", r"\)", r"\[", r"\]")):
            raise ValueError(f"Legacy math delimiters: {name}:{index+1}")
        if "$$" in plain:
            if plain != "$$":
                raise ValueError(f"Display delimiters must be isolated: {name}:{index+1}")
            if not displayed and index and lines[index-1].strip():
                raise ValueError(f"Missing blank line before display: {name}:{index+1}")
            if displayed and index+1 < len(lines) and lines[index+1].strip():
                raise ValueError(f"Missing blank line after display: {name}:{index+1}")
            displayed = not displayed
            continue
        if displayed:
            # A lone = is interpreted as Markdown/setext syntax, not TeX math.
            # Treat this as a hard error even between valid $ boundaries.
            if line == "=":
                raise ValueError(f"Standalone equality sign in display: {name}:{index+1}")
            if line in {"-", "---", "___"} or re.match(r"^[*+-]\s", line):
                raise ValueError(f"Markdown structure in display: {name}:{index+1}")
            inspect_expr(plain, name, index+1)
        else:
            spans = plain.split("$")
            if len(spans) % 2 == 0:
                raise ValueError(f"Unmatched dollar delimiter: {name}:{index+1}")
            for expr in spans[1::2]:
                inspect_expr(expr, name, index+1)
    if fenced or displayed:
        raise ValueError("Unclosed Markdown fence or display: " + name)


def check_links(p: Path) -> None:
    content = p.read_text(encoding="utf-8")
    for target in re.findall(r"\]\(([^)\s]+)\)", content):
        if target.startswith(("https:", "http:", "mailto:", "#")):
            continue
        dest = (p.parent / unquote(target.split("#")[0])).resolve()
        if not dest.is_relative_to(ROOT):
            raise ValueError("Out-of-repository link " + target)
        if not dest.exists() and dest.suffix != ".pdf" and dest != ROOT / "output/pdf/manifest.json":
            raise ValueError(f"Broken local link in {p.name}: {target}")


def main() -> None:
    validate_catalog()
    for file in (ROOT / "README.md", ROOT / "docs/RESEARCH_STATUS.md"):
        check_math(file.read_text(encoding="utf-8"), str(file.relative_to(ROOT)))
        check_links(file)
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for document in catalog():
        if document["id"] not in readme:
            raise ValueError("Missing paper from README: " + document["id"])
    broken = [
        r"$\operatorname{KL}(P,S)$",
        r"$x_i^*=(p_i-c^*q_i)_+$",
        r"$x_i^{*}=(p_i-c^{*}q_i)_{+}$",
        r"$x_i^{\ast}=(p_i-c^{\ast}q_i)_+$",
        r"$\custommacro x$",
        r"$a\,b$",
        r"$a\!b$",
        r"$\{1,2\}$",
        r"\(x\)",
        r"\[x\]",
        "prose\n$$\nx=y\n$$\n",
        "\n$$\nx=y\n$$\nprose",
        "\n$$\nx\n=\ny\n$$\n",
        "\n$$\nx\n =   \ny\n$$\n",
    ]
    for case in broken:
        try:
            check_math(case, "regression")
        except ValueError:
            pass
        else:
            raise ValueError("Known MathJax regression accepted: " + repr(case))
    # Braced \ast protects the superscript from Markdown emphasis parsing.
    check_math(r"$x_i^{\ast}=(p_i-c^{\ast}q_i)_{+}$", "regression-ok")
    check_math("\n$\n"+r"x_i^{\ast}=(p_i-c^{\ast}q_i)_{+}"+"\n$\n", "regression-ok")
    # Valid display equations keep equality attached to an operand.
    check_math("\n$$\nx=y\n$$\n", "regression-ok")
    check_math("\n$$\nx\n=y\n$$\n", "regression-ok")
    print("Catalog, original sources, Markdown links, and math render rules validated.")


if __name__ == "__main__":
    main()
