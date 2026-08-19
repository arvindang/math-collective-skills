# Repository guidance

## Purpose

Maintain a portable, source-backed founder skill collection for Claude and
OpenAI/ChatGPT/Codex.

## Invariants

- Keep every skill in the open Agent Skills `SKILL.md` format.
- Use exactly `name` and `description` in SKILL.md frontmatter.
- Keep names lowercase, hyphenated, and equal to their directory names.
- Keep each SKILL.md under 500 lines and move detail to one-level references.
- Keep `agents/openai.yaml` additive; core behavior must remain host-neutral.
- End every specialist output contract with `Watch/read next` and one to three
  relevant direct links from its source map.
- Do not copy, commit, or redistribute source transcripts or essay bodies.
- Preserve all 80 catalog entries and coverage mappings unless the source site
  changes and the catalog is deliberately refreshed.
- Treat legal, tax, securities, accounting, employment, and investment content
  as educational planning with professional-review handoffs.

## Commands

```bash
python3 scripts/collect_source_catalog.py --output sources/catalog.json
python3 scripts/build_coverage.py
python3 scripts/validate_package.py
python3 scripts/package_skills.py
```

When changing a skill, also run the skill-creator `quick_validate.py` against
that skill and forward-test representative prompts from
`tests/activation-cases.json`.

## Source changes

Use `--include-content` only with a temporary output path outside the repository.
Review new or changed source pages, update the relevant research note and source
map, then regenerate the metadata-only public catalog and coverage manifest.
