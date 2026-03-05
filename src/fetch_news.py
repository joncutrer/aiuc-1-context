"""
fetch_news.py — Harvest news/research article references from aiuc-1.com
and archive a monthly digest.

Usage:
    python src/fetch_news.py [--since YYYY-MM-DD]

If --since is omitted, defaults to the first day of the current month.
Articles already in the digest file are skipped (idempotent by URL).

Output: data/news/YYYY/YYYY-MM.md
"""

import argparse
import os
import re
import sys
from datetime import date, datetime

import html2text
import requests

BASE_URL = "https://www.aiuc-1.com"
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NEWS_DIR = os.path.join(REPO_ROOT, "data", "news")

# ---------------------------------------------------------------------------
# Shared utilities
# ---------------------------------------------------------------------------

def fetch_url(url: str) -> str:
    headers = {"User-Agent": "aiuc-1-context-bot/1.0 (github.com/joncutrer/aiuc-1-context)"}
    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.text


def html_to_markdown(html: str) -> str:
    converter = html2text.HTML2Text()
    converter.ignore_links = False
    converter.ignore_images = True
    converter.body_width = 0
    return converter.handle(html)


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


# ---------------------------------------------------------------------------
# Article parsing
# ---------------------------------------------------------------------------

def _parse_articles(md: str) -> list[dict]:
    """
    Extract article metadata from the homepage Markdown content.

    The homepage lists research articles as cards. Each card typically contains:
    - A category label (e.g., "Research", "Announcement")
    - A headline
    - A short description
    - A "Read more" link

    Since /research/ returns 404, all article discovery happens from homepage HTML.
    This parser uses heuristics on the converted Markdown.
    """
    articles = []

    # On the homepage, each article card is rendered as an h4 markdown link:
    #   #### [Title text concatenated with excerpt](/research/slug)
    # followed by a separate "Read more" link to the same URL.
    # We match h4 headings that link to /research/ paths.
    link_pattern = re.compile(
        r"^#{1,4}\s*\[(.+?)\]\(((?:https?://(?:www\.)?aiuc-1\.com)?/research/[^\)]+)\)",
        re.MULTILINE,
    )

    seen_urls = set()

    for match in link_pattern.finditer(md):
        raw_text = match.group(1).strip()
        raw_url = match.group(2).strip()

        # Normalise relative URLs to absolute
        url = raw_url if raw_url.startswith("http") else f"{BASE_URL}{raw_url}"

        if url in seen_urls:
            continue

        seen_urls.add(url)

        # The h4 text concatenates title + excerpt without a separator.
        # Derive a clean title from the URL slug as a reliable fallback,
        # but also keep the full text for context.
        slug = url.rstrip("/").split("/")[-1]
        title_from_slug = slug.replace("-", " ").title()
        # Heuristic: take text up to the first sentence boundary (., !, ?)
        # if it's reasonably short; otherwise fall back to the slug-derived title.
        m_sentence = re.match(r"(.{10,120}?[.!?])\s+[A-Z]", raw_text)
        title = m_sentence.group(1).strip() if m_sentence else (
            raw_text[:120] if len(raw_text) <= 120 else title_from_slug
        )

        # Try to infer a category from context (simple heuristic)
        category = "Research"
        title_lower = title.lower()
        if any(w in title_lower for w in ("announce", "partner", "certif", "launch")):
            category = "Announcement"
        elif any(w in title_lower for w in ("whitepaper", "report", "study", "analysis")):
            category = "Research"

        articles.append({
            "title": title,
            "url": url,
            "category": category,
            "date": None,   # date not reliably parseable from link text alone
        })

    return articles


def _load_existing_urls(path: str) -> set[str]:
    """Return the set of URLs already present in a digest file."""
    if not os.path.isfile(path):
        return set()
    with open(path, encoding="utf-8") as f:
        content = f.read()
    return set(re.findall(r"\*\*URL:\*\*\s+(https?://\S+)", content))


def _format_entry(article: dict, today: str) -> str:
    article_date = article.get("date") or today
    return (
        f"## {article['title']}\n"
        f"**Date:** {article_date}  \n"
        f"**URL:** {article['url']}  \n"
        f"**Category:** {article['category']}  \n"
        f"**Summary:** _(fetched {today} — review and edit as needed)_\n\n"
        f"---\n\n"
    )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Fetch AIUC-1 news digest")
    parser.add_argument(
        "--since",
        metavar="YYYY-MM-DD",
        help="Only include articles published on or after this date (default: first of current month)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-add articles even if they are already in the digest",
    )
    args = parser.parse_args()

    today = date.today()
    today_str = today.isoformat()

    if args.since:
        since = datetime.strptime(args.since, "%Y-%m-%d").date()
    else:
        since = today.replace(day=1)

    print(f"Fetching news articles (since {since}) ...")

    html = fetch_url(BASE_URL + "/")
    md = html_to_markdown(html)
    articles = _parse_articles(md)

    if not articles:
        print("No article links found on homepage.")
        return

    print(f"Found {len(articles)} article link(s) on homepage.")

    # Determine output file path
    year_str = today.strftime("%Y")
    month_str = today.strftime("%Y-%m")
    out_dir = os.path.join(NEWS_DIR, year_str)
    out_path = os.path.join(out_dir, f"{month_str}.md")
    ensure_dir(out_dir)

    existing_urls = set() if args.force else _load_existing_urls(out_path)

    new_articles = [a for a in articles if a["url"] not in existing_urls]

    if not new_articles:
        print("No new articles to add.")
        return

    # Write or append to digest file
    if not os.path.isfile(out_path):
        header = f"# News Digest: {month_str}\n\n"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(header)

    with open(out_path, "a", encoding="utf-8") as f:
        for article in new_articles:
            entry = _format_entry(article, today_str)
            f.write(entry)
            print(f"  + Added: {article['title'][:70]}")

    print(f"\n{len(new_articles)} article(s) added → {out_path}")


if __name__ == "__main__":
    main()
