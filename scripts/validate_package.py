#!/usr/bin/env python3
"""Run static, cross-host validation for the complete skill package."""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = ROOT / "skills"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
SOURCE_PREFIX = "https://startups.henikoff.com/lesson/"


def error(errors: list[str], path: Path | str, message: str) -> None:
    errors.append(f"{path}: {message}")


def frontmatter(path: Path, errors: list[str]) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        error(errors, path, "missing YAML frontmatter")
        return {}
    try:
        raw, _body = text[4:].split("\n---\n", 1)
    except ValueError:
        error(errors, path, "frontmatter is not closed")
        return {}
    values: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            error(errors, path, f"invalid frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    if set(values) != {"name", "description"}:
        error(errors, path, "frontmatter must contain exactly name and description")
    return values


def validate_links(skill_dir: Path, text: str, errors: list[str]) -> None:
    for raw_target in MARKDOWN_LINK.findall(text):
        target = raw_target.strip().split("#", 1)[0]
        if not target or "://" in target or target.startswith("mailto:"):
            continue
        resolved = (skill_dir / target).resolve()
        try:
            resolved.relative_to(skill_dir.resolve())
        except ValueError:
            error(errors, skill_dir / "SKILL.md", f"link leaves the skill directory: {raw_target}")
            continue
        if not resolved.exists():
            error(errors, skill_dir / "SKILL.md", f"broken local link: {raw_target}")


def validate_skill(skill_dir: Path, catalog_urls: set[str], errors: list[str]) -> str | None:
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        error(errors, skill_dir, "missing SKILL.md")
        return None
    values = frontmatter(skill_file, errors)
    name = values.get("name", "")
    description = values.get("description", "")
    if name != skill_dir.name:
        error(errors, skill_file, "name must match the parent directory")
    if len(name) > 64 or not NAME_PATTERN.fullmatch(name):
        error(errors, skill_file, "name violates Agent Skills naming rules")
    if "anthropic" in name or "claude" in name:
        error(errors, skill_file, "name contains a Claude-reserved word")
    if not 1 <= len(description) <= 1024:
        error(errors, skill_file, "description must contain 1-1024 characters")
    if "use when" not in description.lower():
        error(errors, skill_file, "description must state when to use the skill")

    text = skill_file.read_text(encoding="utf-8")
    if len(text.splitlines()) > 500:
        error(errors, skill_file, "SKILL.md exceeds 500 lines")
    if "references/source-map.md" not in text:
        error(errors, skill_file, "must route relevant tasks to references/source-map.md")
    if "watch/read next" not in text.lower():
        error(errors, skill_file, "must require a Watch/read next recommendation")
    if "handoff" not in text.lower():
        error(errors, skill_file, "must define a handoff to the next workflow")
    validate_links(skill_dir, text, errors)

    source_map = skill_dir / "references/source-map.md"
    if not source_map.is_file():
        error(errors, source_map, "missing source map")
    else:
        source_text = source_map.read_text(encoding="utf-8")
        urls = set(re.findall(r"https://startups\.henikoff\.com/lesson/[a-z0-9-]+", source_text))
        if not urls:
            error(errors, source_map, "must link to at least one primary lesson")
        unknown = sorted(urls - catalog_urls)
        if unknown:
            error(errors, source_map, f"unknown source URL(s): {', '.join(unknown)}")

    openai_yaml = skill_dir / "agents/openai.yaml"
    if not openai_yaml.is_file():
        error(errors, openai_yaml, "missing OpenAI UI metadata")
    else:
        yaml_text = openai_yaml.read_text(encoding="utf-8")
        if f"${name}" not in yaml_text:
            error(errors, openai_yaml, "default prompt must mention the skill explicitly")
    return name or None


def load_json(path: Path, errors: list[str]) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        error(errors, path, f"cannot load JSON: {exc}")
        return None


def main() -> int:
    errors: list[str] = []
    catalog_path = ROOT / "sources/catalog.json"
    catalog = load_json(catalog_path, errors) or {}
    items = catalog.get("items", []) if isinstance(catalog, dict) else []
    catalog_slugs = {item.get("slug") for item in items if isinstance(item, dict)}
    catalog_urls = {item.get("url") for item in items if isinstance(item, dict)}
    if len(catalog_slugs) != 80:
        error(errors, catalog_path, f"expected 80 unique source items, found {len(catalog_slugs)}")
    forbidden_catalog_keys = {"content", "transcript", "prose", "description"}
    for item in items:
        if isinstance(item, dict) and forbidden_catalog_keys.intersection(item):
            error(errors, catalog_path, "public catalog includes source text")
            break

    skill_names: set[str] = set()
    if not SKILLS_ROOT.is_dir():
        error(errors, SKILLS_ROOT, "missing skills directory")
    else:
        for skill_dir in sorted(SKILLS_ROOT.iterdir()):
            if not skill_dir.is_dir():
                continue
            name = validate_skill(skill_dir, catalog_urls, errors)
            if name:
                if name in skill_names:
                    error(errors, skill_dir, f"duplicate skill name: {name}")
                skill_names.add(name)

    coverage_path = ROOT / "sources/coverage.json"
    coverage = load_json(coverage_path, errors) or {}
    mappings = coverage.get("items", []) if isinstance(coverage, dict) else []
    mapped_slugs = {item.get("slug") for item in mappings if isinstance(item, dict)}
    missing = sorted(catalog_slugs - mapped_slugs)
    extra = sorted(mapped_slugs - catalog_slugs)
    if missing:
        error(errors, coverage_path, f"unmapped source slug(s): {', '.join(missing)}")
    if extra:
        error(errors, coverage_path, f"unknown mapped slug(s): {', '.join(extra)}")
    for item in mappings:
        if not isinstance(item, dict):
            continue
        assigned = [item.get("primary_skill"), *item.get("supporting_skills", [])]
        unknown = sorted({name for name in assigned if name and name not in skill_names})
        if unknown:
            error(errors, coverage_path, f"{item.get('slug')}: unknown skill(s): {', '.join(unknown)}")

    cases_path = ROOT / "tests/activation-cases.json"
    cases = load_json(cases_path, errors) or {}
    for name in skill_names:
        entry = cases.get(name, {}) if isinstance(cases, dict) else {}
        if not entry.get("should_trigger") or not entry.get("should_not_trigger"):
            error(errors, cases_path, f"{name}: missing positive or negative activation cases")

    if errors:
        print("Validation failed:")
        for item in errors:
            print(f"- {item}")
        return 1
    print(f"Validated {len(skill_names)} skills and {len(catalog_slugs)} source mappings.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
