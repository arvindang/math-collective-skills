# MATH Founder Stack

[![validate](https://github.com/arvindang/math-collective-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/arvindang/math-collective-skills/actions/workflows/validate.yml)

An open, source-backed founder operating system distilled from the startup
lessons at [startups.henikoff.com](https://startups.henikoff.com).

It turns 80 lessons, essays, and interviews into a portable set of Agent Skills
for Claude and OpenAI/ChatGPT/Codex surfaces that support skills. Each skill has
a focused specialist role, a concrete output artifact, and direct links back to
the primary material.

This project is independent and is not affiliated with or endorsed by Troy
Henikoff, MATH Venture Partners, OpenAI, Anthropic, or gstack.

## Quick start

Clone and install for both Claude Code and Codex:

```bash
git clone https://github.com/arvindang/math-collective-skills.git
cd math-collective-skills
./setup --host all
```

Then start with:

```text
Use $math-founder-office-hours. We are building [product] for [customer].
Our hardest decision right now is [decision].
```

For a broad situation, let the router choose the smallest useful workflow:

```text
Use $math-founder-stack to diagnose our current constraint and choose the
smallest useful workflow.
```

For a focused task, invoke the specialist directly:

```text
Use $math-diagnose-metrics. Audit our retention definition, rebuild the cohort
view, and finish with a handoff for the growth-experiment skill.
```

For a deliberate chain, name both skills and the handoff:

```text
Use $math-validate-startup, then hand its evidence ledger to
$math-model-startup. Do not carry unsupported assumptions forward as facts.
```

Skills do not need to run as one giant workflow. In the same conversation, the
next skill can consume the prior artifact directly. Across conversations or
tools, save or paste the completed artifact from the first skill as input to the
next one.

## The founder loop

This is a process, not a bag of prompts:

**Diagnose → Validate → Model → Measure → Grow → Fund → Pitch → Run → Communicate**

Founder equity, channel partnerships, and operating reviews are cross-cutting
specialists invoked when those decisions appear.

| Skill | Specialist | Produces | Typical handoff |
|---|---|---|---|
| `$math-founder-stack` | Chief of staff | Constraint diagnosis and route | The selected specialist |
| `$math-founder-office-hours` | Founder coach | Reframe, options, and decision brief | Validation, operations, or one narrow specialist |
| `$math-validate-startup` | Customer truth-teller | Evidence ledger and falsifiable validation plan | Model, growth experiment, or pitch |
| `$math-model-startup` | Startup CFO | Driver tree, integrated model design, and scenarios | Metrics, growth experiment, or fundraise plan |
| `$math-diagnose-metrics` | Metrics lead | KPI dictionary, cohorts, unit economics, and diagnosis | Growth experiment, model revision, or investor update |
| `$math-design-growth-experiments` | Growth lead | Bounded test with scale/change/stop thresholds | Metrics diagnosis, model revision, or operating review |
| `$math-build-channel-partnerships` | Partnerships lead | Partner scorecard, deal plan, launch, and measurement | Growth, metrics, or operating review |
| `$math-review-founder-operations` | Operating partner | Focus, leadership, trust, and execution review | Office hours, one specialist, or investor update |
| `$math-plan-fundraise` | Fundraising strategist | Milestone-led amount, timing, structure, and risk cases | Pitch, investor process, and equity preflight |
| `$math-build-investor-pitch` | Pitch coach | Three-pass narrative, evidence gaps, and investor Q&A | Investor process |
| `$math-run-investor-process` | Deal lead | Target map, outreach, CRM cadence, and data-room plan | Pitch iteration and investor updates |
| `$math-write-investor-update` | Investor relations lead | Candid metrics, risks, decisions, and asks | Operating review and the next financing cycle |
| `$math-structure-founder-equity` | Equity preflight coach | Founder facts, scenarios, and professional-review questions | Counsel review and fundraise plan |

Each completed workflow ends with **Watch/read next** and one to three relevant
links to the original lesson—not a generic bibliography.

### The handoff contract

Every specialist keeps four evidence classes separate: **facts** supplied or
verified, **assumptions** still needing proof, **calculations** with visible
logic, and **judgments** or recommendations. A handoff should preserve those
labels and include:

1. the decision made or still open;
2. the completed artifact and evidence used;
3. unresolved questions, risks, and stop conditions;
4. the next skill, why it is next, and the minimum inputs it needs;
5. an owner and review date when execution is involved.

The receiving skill may challenge an upstream judgment. It must not silently
promote an assumption into a fact or reuse a historical source example as a
current benchmark.

### Example end-to-end sequence

```text
$math-founder-stack
  → $math-validate-startup          evidence ledger
  → $math-model-startup             driver model and runway cases
  → $math-diagnose-metrics          KPI contracts and cohort diagnosis
  → $math-design-growth-experiments bounded test and decision gates
  → $math-plan-fundraise            milestone-led financing plan
  → $math-build-investor-pitch      narrative and investor Q&A
  → $math-run-investor-process      target map, CRM, and data room
  → $math-write-investor-update     progress, risks, and asks
```

This is an example, not a mandatory funnel. The router should skip any stage
whose output already exists and is trustworthy.

## Install

The canonical, host-neutral skills live in `skills/` and follow the open
[Agent Skills specification](https://agentskills.io/specification). The same
`SKILL.md` folders work across products; `agents/openai.yaml` adds optional
OpenAI UI metadata and is harmless elsewhere.

### Personal install

```bash
./setup --host claude  # ~/.claude/skills
./setup --host codex   # $CODEX_HOME/skills or ~/.agents/skills
./setup --host all     # both
```

macOS/Linux installs symlinks so a pull updates the skills immediately. Windows
uses copies; rerun setup after pulling changes.

### Repository-scoped install

```bash
./setup --host all --scope project --project /path/to/your-project
```

This installs into `.claude/skills` and `.agents/skills` in the target project.
The installer refuses to overwrite a colliding skill unless the user explicitly
passes `--force`; that flag only replaces exact named skill targets.

### Package for upload

```bash
python3 scripts/package_skills.py
```

This creates deterministic per-skill archives plus a complete filesystem bundle
in `dist/`. Upload the individual skill archive required by the product surface.
Custom skills are managed separately across Claude Code, claude.ai, and Claude
API surfaces. See the current [Claude Agent Skills documentation](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
and [OpenAI skill documentation](https://developers.openai.com/codex/skills/).

There is no single cross-vendor installation registry: portability comes from
keeping `SKILL.md` host-neutral, while the installer and optional metadata adapt
the same source package to each supported host.

## Source rigor

The primary library is [Startup Videos, Lessons & Essays by Troy
Henikoff](https://startups.henikoff.com). Every specialist has a
`references/source-map.md` containing direct lesson links, guidance on when to
use each source, and cautions against overgeneralizing its examples.

The review used the complete public library available on 2026-08-19:

| Coverage | Count |
|---|---:|
| Total pieces | 80 |
| Lessons / essays / interviews | 56 / 16 / 8 |
| Video / text pages | 58 / 22 |
| Pages exposing a timed transcript | 52 |
| Reviewed words in transcript and page prose | 56,935 |

The collector reads visible timed transcript segments because long JSON-LD
metadata can be truncated. Six video pages expose prose or an external embed but
no timed transcript on the page. Low-content listings remain in the coverage
ledger and are explicitly prevented from becoming substantive guidance.

- [`sources/catalog.json`](sources/catalog.json) inventories all 80 pages without
  redistributing source text.
- [`sources/coverage.json`](sources/coverage.json) maps every page to a primary
  skill, evidence status, and supporting skills.
- [`research/`](research/) contains the three complete, item-by-item distilled
  reviews and the gstack packaging benchmark.
- `scripts/collect_source_catalog.py --include-content` can create a temporary
  private review corpus; do not commit that output without permission.

## Safety and editorial policy

The source archive includes financing, securities, equity, option-pool, 83(b),
employment, accounting, and valuation examples. Those examples can be dated,
jurisdiction-specific, simplified, or terminologically imprecise. The skills:

- separate facts, assumptions, calculations, and judgments;
- use scenarios and ranges instead of false precision;
- treat historical numbers as mechanisms, never current benchmarks;
- produce questions for qualified counsel, tax advisers, and accountants;
- do not present educational planning as legal, tax, investment, or securities
  advice.

See [NOTICE.md](NOTICE.md) for attribution and content boundaries.

## Validate and develop

```bash
python3 scripts/build_coverage.py
python3 scripts/validate_package.py
python3 /path/to/skill-creator/scripts/quick_validate.py skills/<skill-name>
python3 scripts/package_skills.py
```

Static activation cases live in `tests/activation-cases.json`. New or changed
skills should also be forward-tested on representative tasks without telling
the test agent the intended answer.

## Repository layout

```text
skills/                  portable specialist skills
  <skill>/SKILL.md       discovery metadata and workflow
  <skill>/references/    source map loaded on demand
  <skill>/assets/        reusable output template
sources/                 public catalog and coverage manifest
research/                evidence reviews and design benchmark
scripts/                 collect, map, validate, install, and package
tests/                   activation fixtures
setup                    cross-host installer
```

The packaging and workflow ergonomics are inspired by
[garrytan/gstack](https://github.com/garrytan/gstack): specialist roles, an
obvious entry point, composable handoffs, fast installation, and testable skill
quality. The implementation and founder guidance here are independent.

## License

Original repository content is MIT-licensed. The linked source material is not
relicensed or redistributed; rights remain with the respective owners.
