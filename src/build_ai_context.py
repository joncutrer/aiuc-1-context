"""
build_ai_context.py — Compile AIUC-1 spec data into a single AI-optimized context document.

Optimized for LLM consumption: dense, minimal redundancy, no decorative formatting.
No nav junk, no marketing sections, no repeated requirement text.

Usage:
    python src/build_ai_context.py

Output: data/ai-context/aiuc-1-context-latest.md  (always overwritten)
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
    "data-and-privacy",
    "security",
    "safety",
    "reliability",
    "accountability",
    "society",
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
    if not os.path.isdir(DIFF_DIR):
        return None
    files = [f for f in os.listdir(DIFF_DIR) if f.endswith(".md")]
    if not files:
        return None
    files.sort(reverse=True)
    return os.path.join(DIFF_DIR, files[0])


# ---------------------------------------------------------------------------
# Content extraction helpers
# ---------------------------------------------------------------------------

def _strip_page_chrome(md: str) -> str:
    """
    Strip nav menus, footers, and marketing sections from a converted webpage.
    Keeps content from the first top-level # heading through the last
    meaningful line before marketing/footer sections begin.
    """
    # Start from the first # heading (skip nav block before it)
    m = re.search(r"^# ", md, re.MULTILINE)
    if m:
        md = md[m.start():]

    # Cut at marketing/footer anchors
    cutoffs = [
        r"^## AIUC-1 is built with industry leaders",
        r"^Stay up to date with AIUC-1",
        r"^\[AIUC-1\.COM\]",
        r"^© 20\d\d",
    ]
    for pat in cutoffs:
        cut = re.search(pat, md, re.MULTILINE)
        if cut:
            md = md[:cut.start()]

    # Remove stray empty image links like [](/) left by the nav
    md = re.sub(r"^\[\]\([^\)]*\)\n?", "", md, flags=re.MULTILINE)

    # Collapse excessive blank lines
    md = re.sub(r"\n{3,}", "\n\n", md)

    return md.strip()


def _extract_keywords(domain_md: str) -> dict[str, list[str]]:
    """
    Extract {req_id: [keyword, ...]} from a domain page markdown.

    Domain pages have requirement blocks structured as:
        ### [Title →A001·Mandatory](url)
        description
        Keywords
        Keyword One
        Keyword Two
        Capabilities
        Universal
    """
    result = {}
    for block in re.split(r"^### ", domain_md, flags=re.MULTILINE):
        id_match = re.search(r"→([A-Z]\d{3})[··]", block)
        if not id_match:
            continue
        req_id = id_match.group(1)
        kw_match = re.search(r"\bKeywords\b\s*\n(.*?)\nCapabilities\b", block, re.DOTALL)
        if kw_match:
            keywords = [kw.strip() for kw in kw_match.group(1).splitlines() if kw.strip()]
            if keywords:
                result[req_id] = keywords
    return result


# ---------------------------------------------------------------------------
# Section builders
# ---------------------------------------------------------------------------

def build_header(latest_version: str, versions: list[str]) -> str:
    """4-line dense header: version, facts, domain index, crosswalk list."""
    versions_str = " ".join(reversed(versions))
    return (
        f"AIUC-1 {latest_version} | {date.today().isoformat()} | https://www.aiuc-1.com\n"
        f"Security/safety/reliability standard for AI agents. 51 requirements across 6 domains. "
        f"Quarterly releases Jan/Apr/Jul/Oct 15. Versions: {versions_str}\n"
        f"Domains: A=Data&Privacy B=Security C=Safety D=Reliability E=Accountability F=Society\n"
        f"Crosswalks: ISO 42001 | MITRE ATLAS | EU AI Act | NIST AI RMF | OWASP Top Ten | CSA AICM | OWASP AIVSS\n\n"
    )


def build_requirements_section(latest_version: str) -> str:
    """
    Requirements table from the spreadsheet snapshot, with a Keywords column
    injected from the domain page markdown files.
    """
    version_dir = os.path.join(SPEC_DIR, latest_version)

    # Collect keywords across all domain pages
    all_keywords: dict[str, list[str]] = {}
    for slug in DOMAIN_SLUGS:
        path = os.path.join(version_dir, f"{slug}.md")
        domain_md = _strip_frontmatter(read_file(path))
        if domain_md:
            all_keywords.update(_extract_keywords(domain_md))

    req_path = os.path.join(version_dir, "evidence-requirements.md")
    req_content = _strip_frontmatter(read_file(req_path))
    if not req_content.strip():
        return "# Requirements\n\n_Not yet fetched._\n\n"

    out = ["# Requirements\n\n"]
    in_table = False

    for line in req_content.splitlines():
        # Skip the H1 and blank line that follows it from the source file
        if line.startswith("# AIUC-1 Requirements") or (not in_table and line == ""):
            continue
        # Table header row — inject Keywords column
        if line.startswith("| Domain |") and not in_table:
            out.append(line.rstrip() + " Keywords |\n")
            in_table = True
            continue
        # Separator row — extend it
        if in_table and line.startswith("|---"):
            out.append(line.rstrip() + "---|\n")
            continue
        # Data rows — look up keywords by req ID (column index 2)
        if in_table and line.startswith("| "):
            parts = [p.strip() for p in line.split("|")]
            req_id = parts[2] if len(parts) > 2 else ""
            keywords = ", ".join(all_keywords.get(req_id, []))
            out.append(line.rstrip() + f" {keywords} |\n")
            continue
        out.append(line + "\n")

    return "".join(out) + "\n"


def build_controls_section(latest_version: str) -> str:
    """Controls & evidence from the spreadsheet snapshot."""
    ev_path = os.path.join(SPEC_DIR, latest_version, "evidence-controls.md")
    content = _strip_frontmatter(read_file(ev_path))
    if not content.strip():
        return "# Controls & Evidence\n\n_Not yet fetched._\n\n"
    # Drop the H1 from the file; we supply our own heading
    content = re.sub(r"^# AIUC-1 Controls.*?\n\n", "", content, count=1)
    return "# Controls & Evidence\n\n" + content.strip() + "\n\n"


def build_domain_descriptions_section(latest_version: str) -> str:
    """
    One heading + one-line description per domain.
    Requirement details are omitted here — they're in the Requirements table.
    """
    version_dir = os.path.join(SPEC_DIR, latest_version)
    lines = ["# Domain Descriptions\n\n"]

    for slug in DOMAIN_SLUGS:
        path = os.path.join(version_dir, f"{slug}.md")
        md = _strip_page_chrome(_strip_frontmatter(read_file(path)))
        if not md:
            continue
        heading = re.search(r"^# (.+)$", md, re.MULTILINE)
        if not heading:
            continue
        title = heading.group(1).strip()
        after = md[heading.end():].lstrip("\n")
        subtitle_m = re.match(r"^(.+)$", after, re.MULTILINE)
        subtitle = subtitle_m.group(1).strip() if subtitle_m else ""
        lines.append(f"## {title}\n{subtitle}\n\n")

    return "".join(lines)


def build_crosswalks_section(latest_version: str) -> str:
    """Crosswalks page stripped of nav and marketing."""
    path = os.path.join(SPEC_DIR, latest_version, "crosswalks.md")
    md = _strip_page_chrome(_strip_frontmatter(read_file(path)))
    if not md:
        return ""
    # Drop the page's own H1 — we supply our own heading
    md = re.sub(r"^# .+\n\n?", "", md, count=1)
    # Remove standalone crosswalk framework links (nav artifacts)
    md = re.sub(r"^\[[^\]]+\]\(/crosswalks/[^\)]+\)\n?", "", md, flags=re.MULTILINE)
    # Remove bare UI label lines like "AIUC-1 is built on" / "AIUC-1 does not duplicate"
    md = re.sub(r"^AIUC-1 (is built on|does not duplicate)\n?", "", md, flags=re.MULTILINE)
    # Remove stray regional/sector legislation lines left by UI labels
    md = re.sub(r"^(Regional AI|Sector-specific|OECD AI Principles)\b.*\n?", "", md, flags=re.MULTILINE)
    # Remove trailing marketing tagline that leaks through chrome strip
    md = re.sub(r"\nThe Security, Safety, and Reliability standard.*$", "", md, flags=re.DOTALL)
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    return "# Framework Crosswalks\n\n" + md + "\n\n"


def build_changelog_section() -> str:
    """All archived changelogs, newest first. Omitted if none exist."""
    files = _sorted_changelogs()
    if not files:
        return ""
    parts = ["# Changelogs\n\n"]
    for fname in reversed(files):
        content = read_file(os.path.join(CHANGELOG_DIR, fname)).strip()
        if content:
            parts.append(content + "\n\n")
    return "".join(parts) if len(parts) > 1 else ""


def build_diff_section() -> str:
    """Latest spec diff. Omitted if none exists. Strips verbose metadata header."""
    diff_path = _latest_diff_file()
    if not diff_path:
        return ""
    content = read_file(diff_path).strip()
    if not content:
        return ""
    # Strip the generated metadata block (Generated/From/To + --- separator)
    content = re.sub(r"\*\*Generated:\*\*.*?\n---\n\n?", "", content, flags=re.DOTALL)
    # Collect no-change sections, then remove them (handle 1–3 trailing newlines)
    no_change_sections = re.findall(r"^## (.+)\n\n_No changes\._", content, re.MULTILINE)
    content = re.sub(r"^## .+\n\n_No changes\._\n*", "", content, flags=re.MULTILINE)
    content = content.strip()
    if not content or content == re.sub(r"^# .+", "", content, count=1).strip() == "":
        # Nothing left but the heading — all unchanged
        title_m = re.match(r"^(# .+)", content)
        title = title_m.group(1) if title_m else "# Diff"
        return f"{title}\nAll sections unchanged.\n\n"
    if no_change_sections:
        content += f"\n\nUnchanged: {', '.join(no_change_sections)}"
    return content.strip() + "\n\n"


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    versions = _sorted_versions()

    if not versions:
        print("WARNING: No spec versions found in data/spec-versions/.")
        print("Run 'python src/fetch_spec.py' first.")
        sys.exit(1)

    latest_version = versions[-1]
    print(f"Latest spec version: {latest_version}")

    parts = [
        build_header(latest_version, versions),
        build_requirements_section(latest_version),
        build_controls_section(latest_version),
        build_domain_descriptions_section(latest_version),
        build_crosswalks_section(latest_version),
    ]

    changelog = build_changelog_section()
    if changelog:
        parts.append(changelog)

    diff = build_diff_section()
    if diff:
        parts.append(diff)

    output = "".join(parts)

    ensure_dir(CONTEXT_DIR)
    write_file(OUT_PATH, output)
    print(f"AI context document written → {OUT_PATH}")
    print(f"  Total size: {len(output):,} characters")


if __name__ == "__main__":
    main()
