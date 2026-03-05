"""
build_ai_context.py — Compile all AIUC-1 spec data into a single AI-optimized
context document.

Usage:
    python src/build_ai_context.py

Output: data/ai-context/aiuc-1-context-latest.md  (always overwritten)

The output is a dense Markdown document optimized for retrieval by AI assistants.
It should answer any question about AIUC-1 without needing to consult individual files.
"""

import os
import re
import sys
from datetime import date

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPEC_DIR = os.path.join(REPO_ROOT, "data", "spec-versions")
CHANGELOG_DIR = os.path.join(REPO_ROOT, "data", "changelog")
DIFF_DIR = os.path.join(REPO_ROOT, "data", "spec-diffs")
CONTEXT_DIR = os.path.join(REPO_ROOT, "data", "ai-context")
OUT_PATH = os.path.join(CONTEXT_DIR, "aiuc-1-context-latest.md")

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

EVIDENCE_SLUGS = [
    "evidence-requirements",
    "evidence-controls",
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


def _strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            return text[end + 3:].lstrip("\n")
    return text


def _sorted_versions() -> list[str]:
    """Return version folder names sorted chronologically (oldest first)."""
    if not os.path.isdir(SPEC_DIR):
        return []
    pattern = re.compile(r"^\d{4}-Q[1-4]$")
    versions = [d for d in os.listdir(SPEC_DIR) if pattern.match(d)]

    def version_key(v):
        year, q = v.split("-Q")
        return int(year) * 10 + int(q)

    return sorted(versions, key=version_key)


def _sorted_changelogs() -> list[str]:
    if not os.path.isdir(CHANGELOG_DIR):
        return []
    pattern = re.compile(r"^\d{4}-Q[1-4]\.md$")
    files = [f for f in os.listdir(CHANGELOG_DIR) if pattern.match(f)]

    def cl_key(f):
        year, rest = f.split("-Q")
        q = rest.replace(".md", "")
        return int(year) * 10 + int(q)

    return sorted(files, key=cl_key)


def _latest_diff_file() -> str | None:
    """Return the most recently generated diff file path, or None."""
    if not os.path.isdir(DIFF_DIR):
        return None
    files = [f for f in os.listdir(DIFF_DIR) if f.endswith(".md")]
    if not files:
        return None
    # Sort by filename; format is YYYY-QN_vs_YYYY-QN.md
    files.sort(reverse=True)
    return os.path.join(DIFF_DIR, files[0])


# ---------------------------------------------------------------------------
# Build sections
# ---------------------------------------------------------------------------

def build_intro_section() -> str:
    return (
        "# AIUC-1 AI Context — Complete Reference\n\n"
        f"**Generated:** {date.today().isoformat()}  \n"
        "**Source:** https://www.aiuc-1.com/\n\n"
        "This document is an AI-optimized single source of truth for the AIUC-1 standard.\n"
        "It is compiled from archived spec versions, changelogs, and diff reports.\n\n"
        "---\n\n"
        "## What is AIUC-1?\n\n"
        "AIUC-1 (AI Use Case standard 1) is the world's first security and safety standard\n"
        "designed specifically for AI agents. It was developed with 100+ Fortune 500 CISOs\n"
        "to enable enterprise adoption of AI agents.\n\n"
        "**Release cadence:** Quarterly (January 15, April 15, July 15, October 15)\n\n"
        "**Six domains:**\n"
        "- A: Data & Privacy\n"
        "- B: Security\n"
        "- C: Safety\n"
        "- D: Reliability\n"
        "- E: Accountability\n"
        "- F: Society\n\n"
        "**Framework crosswalks:** ISO 42001, MITRE ATLAS, EU AI Act, NIST AI RMF, OWASP Top Ten, CSA AICM\n\n"
        "**Requirement structure per control:**\n"
        "ID & Title | Status (Mandatory/Optional) | Summary | Shoulds | Mays | Keywords | "
        "Metadata | Crosswalks | Evidence Requirements\n\n"
        "---\n\n"
    )


def build_spec_sections(latest_version: str) -> str:
    version_dir = os.path.join(SPEC_DIR, latest_version)
    sections = [f"## Spec Content — {latest_version}\n\n"]

    for slug in DOMAIN_SLUGS:
        path = os.path.join(version_dir, f"{slug}.md")
        content = _strip_frontmatter(read_file(path))
        if content.strip():
            sections.append(f"### Domain: {slug}\n\n{content.strip()}\n\n---\n\n")
        else:
            sections.append(f"### Domain: {slug}\n\n_Not yet fetched._\n\n---\n\n")

    return "".join(sections)


def build_version_history_section(versions: list[str]) -> str:
    if not versions:
        return "## Version History\n\n_No versions archived yet._\n\n---\n\n"

    lines = ["## Version History\n\n"]
    for ver in reversed(versions):  # newest first
        lines.append(f"- **{ver}** — archived in `data/spec-versions/{ver}/`\n")

    lines.append("\n---\n\n")
    return "".join(lines)


def build_changelog_section() -> str:
    files = _sorted_changelogs()
    if not files:
        return "## Changelogs\n\n_No changelogs archived yet._\n\n---\n\n"

    sections = ["## Changelogs\n\n"]
    for fname in reversed(files):  # newest first
        path = os.path.join(CHANGELOG_DIR, fname)
        content = read_file(path).strip()
        if content:
            sections.append(f"{content}\n\n---\n\n")

    return "".join(sections)


def build_evidence_section(latest_version: str) -> str:
    version_dir = os.path.join(SPEC_DIR, latest_version)
    parts = ["## Evidence & Controls\n\n"]
    found_any = False

    for slug in EVIDENCE_SLUGS:
        path = os.path.join(version_dir, f"{slug}.md")
        content = _strip_frontmatter(read_file(path))
        if content.strip():
            parts.append(content.strip() + "\n\n")
            found_any = True

    if not found_any:
        return "## Evidence & Controls\n\n_Not yet fetched. Run fetch_spec to download._\n\n---\n\n"

    parts.append("---\n\n")
    return "".join(parts)


def build_diff_section() -> str:
    diff_path = _latest_diff_file()
    if not diff_path:
        return "## Latest Spec Diff\n\n_No diffs generated yet._\n\n---\n\n"

    content = read_file(diff_path).strip()
    return f"## Latest Spec Diff\n\n{content}\n\n---\n\n"


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    versions = _sorted_versions()

    if not versions:
        print("WARNING: No spec versions found in data/spec-versions/.")
        print("Run 'python src/fetch_spec.py' first to fetch a spec version.")
        latest_version = None
    else:
        latest_version = versions[-1]
        print(f"Latest spec version: {latest_version}")

    parts = [build_intro_section()]
    parts.append(build_version_history_section(versions))

    if latest_version:
        parts.append(build_spec_sections(latest_version))
        parts.append(build_evidence_section(latest_version))

    parts.append(build_changelog_section())
    parts.append(build_diff_section())

    output = "".join(parts)

    ensure_dir(CONTEXT_DIR)
    write_file(OUT_PATH, output)
    print(f"AI context document written → {OUT_PATH}")
    print(f"  Total size: {len(output):,} characters")


if __name__ == "__main__":
    main()
