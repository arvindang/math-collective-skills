# Contributing

Contributions that improve source fidelity, workflow clarity, portability, or
evaluation quality are welcome.

## Before opening a change

1. Identify the founder decision or artifact the skill should improve.
2. Link each source-derived principle to the original Henikoff page.
3. Keep source wording paraphrased; do not add transcripts or article copies.
4. Distinguish archive guidance from added safety and editorial judgment.
5. Add or update positive and negative activation cases.
6. Run `python3 scripts/validate_package.py`.

For a new skill, use the repository pattern: `SKILL.md`,
`references/source-map.md`, `assets/<output-template>`, and
`agents/openai.yaml`. Prefer a new skill only when its trigger, inputs, and
success criteria are meaningfully different from existing specialists.

Source examples are historical context, not universal current benchmarks. Flag
claims that depend on jurisdiction, document version, accounting policy, market
conditions, platform behavior, or professional advice.
