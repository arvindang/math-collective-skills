# gstack benchmark

Reviewed against [`garrytan/gstack`](https://github.com/garrytan/gstack) at commit
`60e51342b54553cf4347ce7a786cae508125053e` on 2026-08-19.

The goal is to borrow gstack's product qualities and repository ergonomics, not
its implementation or prose.

## Patterns to carry forward

- Present the project as a process, not a loose prompt library.
- Give every skill one recognizable specialist role, trigger, input, and output.
- Include one obvious starting point that diagnoses the user's situation and
  routes to narrower specialists.
- Show the end-to-end sequence in the README and explain what each stage hands
  to the next.
- Make the first useful run possible within a few minutes of installation.
- Support both personal and repository-scoped installation.
- Prefer standard skill folders while generating only small host-specific
  metadata where it adds value.
- Treat source coverage, activation behavior, and output quality as testable
  properties.
- Ship templates for recurring outputs so advice becomes an artifact the next
  skill can consume.
- Make provenance, security boundaries, and update behavior explicit.

## Adaptations for this project

- Use the open Agent Skills `SKILL.md` format as the canonical source so the
  same skill folders work in Claude and OpenAI/Codex products.
- Keep all workflows offline and instruction-first. No telemetry, external
  service, credential, or runtime package is required.
- Prefix skill names with `math-` to keep the collection coherent and avoid
  collisions when installed alongside other skill suites.
- Distill and attribute the Henikoff archive; do not vendor transcripts or
  imply endorsement or affiliation.
- Add legal, tax, and investment boundaries wherever the archive discusses
  securities, equity, SAFEs, notes, 83(b) elections, or valuations.
- Use source maps and a machine-readable coverage manifest to demonstrate that
  every available library item was reviewed.

## Proposed workflow

`Office hours → Validate → Model → Measure → Grow → Fund → Pitch → Run the process → Communicate`

Founder equity is a cross-cutting specialist invoked before incorporation,
grants, hiring, or financing decisions.

## Quality bar

Each skill must have:

1. A precise discovery description.
2. A short, imperative workflow with explicit stop conditions.
3. A concrete output artifact or decision record.
4. A source-backed reference file.
5. At least one representative activation test and one non-activation test.
6. Valid Open Agent Skills frontmatter and OpenAI UI metadata.
