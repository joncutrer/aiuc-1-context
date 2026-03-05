"""
fetch_spec.py — Fetch a full AIUC-1 spec version from aiuc-1.com.

Usage:
    python src/fetch_spec.py [YYYY-QN]

If YYYY-QN is omitted, the latest version is auto-detected from /changelog.
Already-fetched versions are skipped (idempotent).
"""

import os
import re
import sys
from datetime import date, datetime

import html2text
import requests

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BASE_URL = "https://www.aiuc-1.com"

EVIDENCE_SHEET_ID = "1jPvVQ8nD2_8hYZVCZE5qFm41p4vKHKukP8eQ13MAMRw"
EVIDENCE_SHEET_URL = (
    f"https://docs.google.com/spreadsheets/d/{EVIDENCE_SHEET_ID}/export?format=xlsx"
)

PAGES = {
    "index":            f"{BASE_URL}/",
    "data-and-privacy": f"{BASE_URL}/data-and-privacy",
    "security":         f"{BASE_URL}/security",
    "safety":           f"{BASE_URL}/safety",
    "reliability":      f"{BASE_URL}/reliability",
    "accountability":   f"{BASE_URL}/accountability",
    "society":          f"{BASE_URL}/society",
    "crosswalks":       f"{BASE_URL}/crosswalks",
}

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPEC_DIR = os.path.join(REPO_ROOT, "data", "spec-versions")

# ---------------------------------------------------------------------------
# Shared utilities
# ---------------------------------------------------------------------------

def fetch_url(url: str) -> str:
    """GET a URL and return the response text. Raises on non-200."""
    headers = {"User-Agent": "aiuc-1-context-bot/1.0 (github.com/joncutrer/aiuc-1-context)"}
    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.text


def html_to_markdown(html: str) -> str:
    """Convert HTML to Markdown using html2text with consistent settings."""
    converter = html2text.HTML2Text()
    converter.ignore_links = False
    converter.ignore_images = True
    converter.body_width = 0  # no line wrapping
    return converter.handle(html)


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def write_file(path: str, content: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


# ---------------------------------------------------------------------------
# Version detection
# ---------------------------------------------------------------------------

def _date_to_quarter(date_str: str) -> str:
    """Convert a release date string (YYYY-MM-DD) to a version label (YYYY-QN)."""
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    quarter = (dt.month - 1) // 3 + 1
    return f"{dt.year}-Q{quarter}"


def detect_latest_version() -> str:
    """
    Fetch /changelog, find the most recent release date, and return YYYY-QN.

    The changelog page states the most recent release in natural language:
      "The most recent version of AIUC-1 was released on **January 15, 2026**."
    It also has section headers like:
      "## January 15, 2026 release"
    We parse these with dateutil since the page does not use ISO date format.
    """
    from dateutil import parser as dateutil_parser

    print("Detecting latest version from /changelog ...")
    html = fetch_url(f"{BASE_URL}/changelog")
    md = html_to_markdown(html)

    # Priority 1: explicit "released on **Month DD, YYYY**" sentence
    m = re.search(r"released on \*?\*?([A-Z][a-z]+ \d{1,2},? \d{4})\*?\*?", md, re.IGNORECASE)
    if m:
        dt = dateutil_parser.parse(m.group(1))
        version = f"{dt.year}-Q{(dt.month - 1) // 3 + 1}"
        print(f"  → Detected latest version: {version} (from '{m.group(0).strip()}')")
        return version

    # Priority 2: section headers "## Month DD, YYYY release"
    headers = re.findall(r"^#{1,3}\s+([A-Z][a-z]+ \d{1,2},? \d{4}) release", md, re.MULTILINE | re.IGNORECASE)
    if headers:
        parsed = sorted([dateutil_parser.parse(h) for h in headers], reverse=True)
        dt = parsed[0]
        version = f"{dt.year}-Q{(dt.month - 1) // 3 + 1}"
        print(f"  → Detected latest version: {version} (from section header '{headers[0]}')")
        return version

    # Fallback: any ISO date in the content, pick the most recent
    dates = re.findall(r"\b(20\d{2}-\d{2}-\d{2})\b", md)
    if dates:
        latest = sorted(dates, reverse=True)[0]
        dt = datetime.strptime(latest, "%Y-%m-%d")
        version = f"{dt.year}-Q{(dt.month - 1) // 3 + 1}"
        print(f"  → Detected latest version: {version} (ISO date fallback: {latest})")
        return version

    raise RuntimeError("Could not detect a release date from /changelog")


# ---------------------------------------------------------------------------
# Evidence spreadsheet helpers
# ---------------------------------------------------------------------------

def _parse_xlsx_sheet(xlsx_bytes: bytes, sheet_index: int) -> list[list[str]]:
    """
    Parse one sheet from raw XLSX bytes using only stdlib (zipfile + ET).
    sheet_index is 0-based (0 = first sheet / sheet1.xml).
    Returns a list of rows, each row a list of cell strings.
    """
    import io
    import zipfile
    import xml.etree.ElementTree as ET

    NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"

    with zipfile.ZipFile(io.BytesIO(xlsx_bytes)) as z:
        with z.open("xl/sharedStrings.xml") as f:
            ss_tree = ET.parse(f)
        shared = []
        for si in ss_tree.findall(f"{{{NS}}}si"):
            parts = [t.text or "" for t in si.findall(f".//{{{NS}}}t")]
            shared.append("".join(parts))

        with z.open(f"xl/worksheets/sheet{sheet_index + 1}.xml") as f:
            ws_tree = ET.parse(f)

    rows = []
    for row in ws_tree.findall(f".//{{{NS}}}row"):
        cells = []
        for c in row.findall(f"{{{NS}}}c"):
            t = c.get("t", "")
            v = c.find(f"{{{NS}}}v")
            if v is None:
                cells.append("")
            elif t == "s":
                cells.append(shared[int(v.text)])
            else:
                cells.append(v.text or "")
        rows.append(cells)
    return rows


def _requirements_to_md(rows: list[list[str]], version: str) -> str:
    """Convert requirements sheet rows to a Markdown table."""
    if len(rows) < 2:
        return "_No requirements data found._\n"

    # rows[0] is the header; rows[1:] are data
    lines = [f"# AIUC-1 Requirements — {version}\n\n"]
    lines.append("| Domain | ID | Title | Full Requirement | Status | Frequency | Capabilities |\n")
    lines.append("|---|---|---|---|---|---|---|\n")

    for row in rows[1:]:
        # Pad short rows
        while len(row) < 6:
            row.append("")
        principle, req_title, full_req, application, frequency, capabilities = row[:6]

        # Split "A001: Title text" into id and title
        m = re.match(r"^([A-Z]\d{3}):\s*(.+)$", req_title)
        req_id = m.group(1) if m else ""
        title = m.group(2) if m else req_title

        # Escape pipes in cell content
        def esc(s):
            return s.replace("|", "\\|").replace("\n", " ")

        lines.append(
            f"| {esc(principle)} | {esc(req_id)} | {esc(title)} "
            f"| {esc(full_req)} | {esc(application)} | {esc(frequency)} | {esc(capabilities)} |\n"
        )

    return "".join(lines)


def _controls_to_md(rows: list[list[str]], version: str) -> str:
    """
    Convert controls & evidence sheet rows to structured Markdown.
    rows[0] is the section-group header, rows[1] is the column header row,
    rows[2:] are data rows.
    """
    if len(rows) < 3:
        return "_No controls data found._\n"

    # Column indices (from rows[1]):
    # 0 Requirement title, 1 Mandatory/Optional, 2 Full requirement,
    # 3 Control application, 4 Control, 5 Evidence title, 6 Typical evidence,
    # 7 Category, 8 Typical Location, 9 Capabilities, 12 Recommended priority
    COL = {name: i for i, name in enumerate(rows[1])}

    def get(row, col_name, default=""):
        idx = COL.get(col_name, -1)
        if idx < 0 or idx >= len(row):
            return default
        return row[idx].strip()

    lines = [f"# AIUC-1 Controls & Evidence — {version}\n\n"]
    current_req = None

    for row in rows[2:]:
        req_title = get(row, "Requirement title")
        if not req_title:
            continue

        if req_title != current_req:
            current_req = req_title
            status = get(row, "Mandatory / Optional")
            capabilities = get(row, "Capabilities")
            lines.append(f"\n## {req_title}\n")
            lines.append(f"*{status} | Capabilities: {capabilities}*\n\n")

        ev_title = get(row, "Evidence title")
        if not ev_title:
            continue

        application = get(row, "Control application")
        control = get(row, "Control")
        typical_ev = get(row, "Typical evidence")
        category = get(row, "Category")
        location = get(row, "Typical Location")
        priority = get(row, "Recommended priority controls")

        lines.append(f"### {ev_title}\n")
        lines.append(f"- **Application:** {application}\n")
        if control:
            lines.append(f"- **Control:** {control}\n")
        lines.append(f"- **Category:** {category}\n")
        if location:
            lines.append(f"- **Typical location:** {location}\n")
        if typical_ev:
            lines.append(f"- **Typical evidence:** {typical_ev}\n")
        if priority:
            lines.append(f"- **Priority guidance:** {priority}\n")
        lines.append("\n")

    return "".join(lines)


def fetch_evidence(version_dir: str, version: str, today: str) -> None:
    """Download the AIUC-1 evidence spreadsheet and save as Markdown files."""
    print(f"  Fetching evidence spreadsheet from Google Sheets ...")
    headers = {"User-Agent": "aiuc-1-context-bot/1.0 (github.com/joncutrer/aiuc-1-context)"}
    try:
        resp = requests.get(EVIDENCE_SHEET_URL, headers=headers, timeout=60)
        resp.raise_for_status()
        xlsx_bytes = resp.content
    except Exception as exc:
        print(f"    WARNING: Could not download evidence spreadsheet: {exc}")
        return

    req_rows = _parse_xlsx_sheet(xlsx_bytes, 1)   # sheet2.xml = AIUC-1 requirements
    ev_rows = _parse_xlsx_sheet(xlsx_bytes, 2)    # sheet3.xml = AIUC-1 Controls & Evidence

    meta = (
        f"---\n"
        f"source: https://docs.google.com/spreadsheets/d/{EVIDENCE_SHEET_ID}\n"
        f"fetched: {today}\n"
        f"version: {version}\n"
    )

    req_path = os.path.join(version_dir, "evidence-requirements.md")
    write_file(req_path, meta + "sheet: AIUC-1 requirements\n---\n\n" + _requirements_to_md(req_rows, version))
    print(f"    Saved → {req_path}")

    ev_path = os.path.join(version_dir, "evidence-controls.md")
    write_file(ev_path, meta + "sheet: AIUC-1 Controls & Evidence\n---\n\n" + _controls_to_md(ev_rows, version))
    print(f"    Saved → {ev_path}")


# ---------------------------------------------------------------------------
# Core fetch logic
# ---------------------------------------------------------------------------

def fetch_spec(version: str, force: bool = False) -> bool:
    """
    Fetch all pages for the given spec version.
    Returns True if pages were fetched, False if skipped (already exists).
    """
    version_dir = os.path.join(SPEC_DIR, version)

    if os.path.isdir(version_dir) and not force:
        print(f"Version {version} already exists at {version_dir} — skipping.")
        return False

    ensure_dir(version_dir)
    today = date.today().isoformat()

    for slug, url in PAGES.items():
        print(f"  Fetching {slug} from {url} ...")
        try:
            html = fetch_url(url)
        except requests.HTTPError as exc:
            print(f"    WARNING: {url} returned {exc.response.status_code} — skipping.")
            continue

        md_body = html_to_markdown(html)
        source_path = url.replace(BASE_URL, "").rstrip("/") or "/"
        header = (
            f"---\n"
            f"source: {url}\n"
            f"fetched: {today}\n"
            f"version: {version}\n"
            f"---\n\n"
        )
        content = header + md_body
        out_path = os.path.join(version_dir, f"{slug}.md")
        write_file(out_path, content)
        print(f"    Saved → {out_path}")

    fetch_evidence(version_dir, version, today)

    print(f"Spec version {version} saved to {version_dir}")
    return True


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    force = "--force" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]

    if args:
        version = args[0].upper()
        if not re.match(r"^\d{4}-Q[1-4]$", version):
            print(f"ERROR: Invalid version format '{version}'. Expected YYYY-QN (e.g. 2026-Q1).")
            sys.exit(1)
    else:
        version = detect_latest_version()

    fetch_spec(version, force=force)


if __name__ == "__main__":
    main()
