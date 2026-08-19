#!/usr/bin/env python3
"""Collect metadata (and optionally text) from startups.henikoff.com.

The default output is safe for a public source catalog: it records metadata,
coverage counts, and content hashes without reproducing the source text. Pass
--include-content only for temporary review files that will not be committed.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import time
from typing import Any
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET


BASE_URL = "https://startups.henikoff.com"
SITEMAP_URL = f"{BASE_URL}/sitemap.xml"
USER_AGENT = "math-collective-skills-source-indexer/1.0 (+public research)"


class JsonLdParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._in_json_ld = False
        self._chunks: list[str] = []
        self.blocks: list[dict[str, Any]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "script" and values.get("type") == "application/ld+json":
            self._in_json_ld = True
            self._chunks = []

    def handle_data(self, data: str) -> None:
        if self._in_json_ld:
            self._chunks.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag != "script" or not self._in_json_ld:
            return
        self._in_json_ld = False
        raw = "".join(self._chunks).strip()
        try:
            value = json.loads(raw)
        except json.JSONDecodeError:
            return
        if isinstance(value, dict):
            self.blocks.append(value)


class ProseParser(HTMLParser):
    BLOCK_TAGS = {
        "address", "article", "aside", "blockquote", "br", "div", "dl", "dt",
        "dd", "figcaption", "figure", "h1", "h2", "h3", "h4", "h5", "h6",
        "hr", "li", "ol", "p", "pre", "section", "table", "td", "th", "tr", "ul",
    }

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._depth = 0
        self._chunks: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        classes = set((values.get("class") or "").split())
        if tag == "div" and "prose" in classes and self._depth == 0:
            self._depth = 1
            return
        if self._depth:
            self._depth += 1
            if tag in self.BLOCK_TAGS:
                self._chunks.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if not self._depth:
            return
        if tag in self.BLOCK_TAGS:
            self._chunks.append("\n")
        self._depth -= 1

    def handle_data(self, data: str) -> None:
        if self._depth:
            self._chunks.append(data)

    def text(self) -> str:
        value = html.unescape("".join(self._chunks))
        value = re.sub(r"[ \t]+", " ", value)
        value = re.sub(r"\n[ \t]+", "\n", value)
        value = re.sub(r"\n{3,}", "\n\n", value)
        return value.strip()


class TranscriptParser(HTMLParser):
    """Extract the complete visible timed transcript instead of truncated JSON-LD."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._depth = 0
        self._current: list[str] = []
        self._segments: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        classes = set((values.get("class") or "").split())
        if tag == "span" and "stext" in classes and self._depth == 0:
            self._depth = 1
            self._current = []
            return
        if self._depth:
            self._depth += 1

    def handle_endtag(self, tag: str) -> None:
        if not self._depth:
            return
        self._depth -= 1
        if self._depth == 0:
            value = re.sub(r"\s+", " ", "".join(self._current)).strip()
            if value:
                self._segments.append(value)

    def handle_data(self, data: str) -> None:
        if self._depth:
            self._current.append(data)

    def text(self) -> str:
        return " ".join(self._segments)


def fetch(url: str, retries: int = 3) -> str:
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html,*/*"})
    for attempt in range(retries):
        try:
            with urlopen(request, timeout=30) as response:
                return response.read().decode("utf-8")
        except Exception:
            if attempt == retries - 1:
                raise
            time.sleep(0.5 * (attempt + 1))
    raise AssertionError("unreachable")


def lesson_urls() -> list[str]:
    xml = fetch(SITEMAP_URL)
    root = ET.fromstring(xml)
    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = [node.text or "" for node in root.findall("sm:url/sm:loc", namespace)]
    return [url for url in urls if urlparse(url).path.startswith("/lesson/")]


def library_metadata() -> dict[str, dict[str, str]]:
    page = fetch(f"{BASE_URL}/library")
    pattern = re.compile(
        r'<li class="lib" data-kind="(?P<kind>[^"]+)"\s+'
        r'data-year="(?P<year>[^"]+)"\s+data-fmt="(?P<format>[^"]+)">'
        r'.*?<a href="(?P<path>/lesson/[^"]+)"',
        re.DOTALL,
    )
    return {
        urljoin(BASE_URL, match.group("path")): {
            "kind": match.group("kind"),
            "year": match.group("year"),
            "format": match.group("format"),
        }
        for match in pattern.finditer(page)
    }


def get_block(blocks: list[dict[str, Any]], schema_type: str) -> dict[str, Any]:
    return next((block for block in blocks if block.get("@type") == schema_type), {})


def creator_name(value: Any) -> str | None:
    if isinstance(value, dict):
        name = value.get("name")
        return name if isinstance(name, str) else None
    if isinstance(value, list):
        names = [creator_name(item) for item in value]
        return ", ".join(name for name in names if name) or None
    return value if isinstance(value, str) else None


def parse_lesson(url: str, library: dict[str, dict[str, str]], include_content: bool) -> dict[str, Any]:
    page = fetch(url)
    json_parser = JsonLdParser()
    json_parser.feed(page)
    video = get_block(json_parser.blocks, "VideoObject")
    article = get_block(json_parser.blocks, "Article")
    breadcrumb = get_block(json_parser.blocks, "BreadcrumbList")
    primary = video or article

    prose_parser = ProseParser()
    prose_parser.feed(page)
    prose = prose_parser.text()
    transcript_parser = TranscriptParser()
    transcript_parser.feed(page)
    visible_transcript = transcript_parser.text()
    json_transcript = primary.get("transcript", "") if isinstance(primary.get("transcript", ""), str) else ""
    transcript = visible_transcript or json_transcript
    description = primary.get("description", "") if isinstance(primary.get("description", ""), str) else ""
    content_parts = [part.strip() for part in (transcript, prose) if part.strip()]
    if not content_parts and description.strip():
        content_parts = [description.strip()]
    content = "\n\n".join(content_parts)

    crumbs = breadcrumb.get("itemListElement", []) if isinstance(breadcrumb, dict) else []
    track = None
    module = None
    if isinstance(crumbs, list) and len(crumbs) >= 3:
        track = crumbs[1].get("name") if isinstance(crumbs[1], dict) else None
        module = crumbs[2].get("name") if isinstance(crumbs[2], dict) else None

    title = primary.get("name") or primary.get("headline")
    if not title:
        match = re.search(r"<h1>(.*?)</h1>", page, re.DOTALL)
        title = re.sub("<[^>]+>", "", match.group(1)).strip() if match else url.rsplit("/", 1)[-1]

    metadata = library.get(url, {})
    record: dict[str, Any] = {
        "slug": urlparse(url).path.rsplit("/", 1)[-1],
        "title": html.unescape(str(title)),
        "url": url,
        "kind": metadata.get("kind") or ("lesson" if video else "essay"),
        "format": metadata.get("format") or ("video" if video else "text"),
        "published": primary.get("uploadDate") or primary.get("datePublished"),
        "author": creator_name(primary.get("author") or primary.get("creator") or primary.get("publisher")),
        "duration": primary.get("duration"),
        "track": track,
        "module": module,
        "has_transcript": bool(transcript),
        "has_prose": bool(prose),
        "word_count": len(content.split()),
        "content_sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
    }
    if include_content:
        record["description"] = description or None
        record["transcript"] = transcript
        record["prose"] = prose
        record["content"] = content
    return record


def summarize(items: list[dict[str, Any]]) -> dict[str, Any]:
    def counts(field: str) -> dict[str, int]:
        values: dict[str, int] = {}
        for item in items:
            key = str(item.get(field) or "unclassified")
            values[key] = values.get(key, 0) + 1
        return dict(sorted(values.items()))

    return {
        "items": len(items),
        "with_transcript": sum(bool(item["has_transcript"]) for item in items),
        "with_prose": sum(bool(item["has_prose"]) for item in items),
        "total_words": sum(int(item["word_count"]) for item in items),
        "by_kind": counts("kind"),
        "by_format": counts("format"),
        "by_track": counts("track"),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--include-content", action="store_true")
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()

    urls = lesson_urls()
    library = library_metadata()
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = [pool.submit(parse_lesson, url, library, args.include_content) for url in urls]
        items = []
        for index, future in enumerate(futures, 1):
            try:
                items.append(future.result())
            except Exception as exc:
                print(f"failed to fetch item {index}/{len(futures)}: {exc}", file=sys.stderr)
                return 1

    document = {
        "source": BASE_URL,
        "sitemap": SITEMAP_URL,
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "content_included": args.include_content,
        "summary": summarize(items),
        "items": items,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(document["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
