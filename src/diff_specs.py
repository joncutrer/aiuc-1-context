"""
diff_specs.py — Compare two AIUC-1 spec versions and write a structured diff report.

Usage:
    python src/diff_specs.py <version-a> <version-b>

Example:
    python src/diff_specs.py 2026-Q1 2026-Q2

Output: data/spec-diffs/2026-Q1_vs_2026-Q2.md
"""

import difflib
import os
import re
import sys
from datetime import date

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPEC_DIR = os.path.join(REPO_ROOT, "data", "spec-versions")
DIFF_DIR = os.path.join(REPO_ROOT, "data", "spec-diffs")

DOMAIN_SLUGS = [
    "index",
    "data-and-privacy",
    "security",
    "safety",
    "reliability",
    "accountability",
    "society",
    "crosswalks",
]

# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def write_file(path: str, content: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def read_file(path: str) -> str:
    if not os.path.isfile(path):
        return ""
    with open(path, encoding="utf-8") as f:
        return f.read()


# ---------------------------------------------------------------------------
# Diff logic
# ---------------------------------------------------------------------------

def _strip_frontmatter(text: str) -> str:
    """Remove the YAML front-matter block (--- ... ---) from a Markdown file."""
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            return text[end + 3:].lstrip("\n")
    return text


def _count_diff(diff_lines) -> tuple[int, int]:
    """Return (additions, removals) counts from unified diff lines."""
    additions = sum(1 for l in diff_lines if l.startswith("+") and not l.startswith("+++"))
    removals = sum(1 for l in diff_lines if l.startswith("-") and not l.startswith("---"))
    return additions, removals


def diff_domain(slug: str, ver_a: str, ver_b: str) -> str:
    """Produce a Markdown diff section for a single domain slug."""
    path_a = os.path.join(SPEC_DIR, ver_a, f"{slug}.md")
    path_b = os.path.join(SPEC_DIR, ver_b, f"{slug}.md")

    text_a = _strip_frontmatter(read_file(path_a))
    text_b = _strip_frontmatter(read_file(path_b))

    if not text_a and not text_b:
        return f"## {slug}\n\n_Not present in either version._\n\n"

    if not text_a:
        return f"## {slug}\n\n_New in {ver_b} (not present in {ver_a})._\n\n"

    if not text_b:
        return f"## {slug}\n\n_Removed in {ver_b} (present in {ver_a})._\n\n"

    lines_a = text_a.splitlines(keepends=True)
    lines_b = text_b.splitlines(keepends=True)

    diff = list(difflib.unified_diff(
        lines_a, lines_b,
        fromfile=f"{ver_a}/{slug}.md",
        tofile=f"{ver_b}/{slug}.md",
        lineterm="",
    ))

    if not diff:
        return f"## {slug}\n\n_No changes._\n\n"

    additions, removals = _count_diff(diff)
    diff_block = "".join(diff)

    section = (
        f"## {slug}\n\n"
        f"**{additions} additions, {removals} removals**\n\n"
        f"```diff\n{diff_block}\n```\n\n"
    )
    return section


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    if len(sys.argv) < 3:
        print("Usage: python src/diff_specs.py <version-a> <version-b>")
        print("Example: python src/diff_specs.py 2026-Q1 2026-Q2")
        sys.exit(1)

    ver_a = sys.argv[1].upper()
    ver_b = sys.argv[2].upper()

    for ver in (ver_a, ver_b):
        if not re.match(r"^\d{4}-Q[1-4]$", ver):
            print(f"ERROR: Invalid version format '{ver}'. Expected YYYY-QN.")
            sys.exit(1)

    dir_a = os.path.join(SPEC_DIR, ver_a)
    dir_b = os.path.join(SPEC_DIR, ver_b)

    if not os.path.isdir(dir_a):
        print(f"ERROR: Version directory not found: {dir_a}")
        sys.exit(1)
    if not os.path.isdir(dir_b):
        print(f"ERROR: Version directory not found: {dir_b}")
        sys.exit(1)

    print(f"Diffing {ver_a} → {ver_b} ...")

    sections = []
    for slug in DOMAIN_SLUGS:
        print(f"  Comparing {slug} ...")
        sections.append(diff_domain(slug, ver_a, ver_b))

    today = date.today().isoformat()
    header = (
        f"# Diff: {ver_a} → {ver_b}\n\n"
        f"**Generated:** {today}  \n"
        f"**From:** `data/spec-versions/{ver_a}/`  \n"
        f"**To:** `data/spec-versions/{ver_b}/`\n\n"
        f"---\n\n"
    )
    output = header + "\n".join(sections)

    ensure_dir(DIFF_DIR)
    out_path = os.path.join(DIFF_DIR, f"{ver_a}_vs_{ver_b}.md")
    write_file(out_path, output)
    print(f"Diff report saved → {out_path}")


if __name__ == "__main__":
    main()
