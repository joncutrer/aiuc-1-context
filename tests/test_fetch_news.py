from pathlib import Path

from conftest import load_src_module


fetch_news = load_src_module("fetch_news")


def test_parse_articles_extracts_research_links_and_dedupes():
    markdown = """
#### [Great New Study on AI Safety. This article explores controls.](/research/great-new-study)
[Read more](/research/great-new-study)

### [Partner Announcement For Certification Program](/research/cert-program-launch)

#### [Ignore this non-research item](/faq)
"""

    articles = fetch_news._parse_articles(markdown)

    assert len(articles) == 2
    assert articles[0]["url"] == "https://www.aiuc-1.com/research/great-new-study"
    assert articles[0]["category"] == "Research"
    assert articles[1]["category"] == "Announcement"


def test_load_existing_urls_reads_digest_format(tmp_path: Path):
    digest = tmp_path / "2026-03.md"
    digest.write_text(
        """
## Item
**URL:** https://www.aiuc-1.com/research/one

## Item 2
**URL:** https://www.aiuc-1.com/research/two
""",
        encoding="utf-8",
    )

    urls = fetch_news._load_existing_urls(str(digest))

    assert urls == {
        "https://www.aiuc-1.com/research/one",
        "https://www.aiuc-1.com/research/two",
    }


def test_format_entry_includes_required_fields():
    entry = fetch_news._format_entry(
        {
            "title": "My Article",
            "url": "https://www.aiuc-1.com/research/my-article",
            "category": "Research",
            "date": None,
        },
        "2026-03-10",
    )

    assert "## My Article" in entry
    assert "**Date:** 2026-03-10" in entry
    assert "**URL:** https://www.aiuc-1.com/research/my-article" in entry
    assert "**Category:** Research" in entry
