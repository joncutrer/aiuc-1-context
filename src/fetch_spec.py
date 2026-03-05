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
    Release dates are: Jan 15, Apr 15, Jul 15, Oct 15.
    """
    print("Detecting latest version from /changelog ...")
    html = fetch_url(f"{BASE_URL}/changelog")
    md = html_to_markdown(html)

    # Look for YYYY-MM-DD date patterns in the changelog content
    dates = re.findall(r"\b(20\d{2}-(?:01|04|07|10)-15)\b", md)
    if not dates:
        # Fallback: any YYYY-MM-DD date
        dates = re.findall(r"\b(20\d{2}-\d{2}-\d{2})\b", md)

    if not dates:
        raise RuntimeError("Could not detect a release date from /changelog")

    # Sort descending and take the most recent
    latest = sorted(dates, reverse=True)[0]
    version = _date_to_quarter(latest)
    print(f"  → Detected latest version: {version} (release date {latest})")
    return version


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
