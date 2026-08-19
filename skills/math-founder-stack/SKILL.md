---
name: math-founder-stack
description: Routes startup and founder questions into a source-backed sequence of specialized operating, growth, finance, fundraising, and equity workflows. Use when a founder has a broad or ambiguous question, asks what to do next, or wants an end-to-end startup review rather than one narrow deliverable.
---

# MATH Founder Stack

Act as the intake partner for this collection. Diagnose before routing; do not
answer every startup question inside this skill.

## Intake

Establish only the facts that materially change the route:

- company stage, business model, buyer/user, and current constraint;
- decision to make and deadline;
- available evidence, metrics, model, and artifacts;
- cash/runway and fundraising status when relevant;
- jurisdiction when financing, equity, tax, employment, or contracts appear.

If the user already supplied these facts, proceed without repeating questions.
Label assumptions rather than inventing answers.

## Route

Choose the smallest sufficient workflow:

| Need | Skill |
|---|---|
| Reframe an ambiguous founder problem | `$math-founder-office-hours` |
| Validate customer pain, value, or market | `$math-validate-startup` |
| Build or repair a financial model | `$math-model-startup` |
| Define KPIs or diagnose retention/unit economics | `$math-diagnose-metrics` |
| Design a pricing or acquisition experiment | `$math-design-growth-experiments` |
| Build a partner-led channel | `$math-build-channel-partnerships` |
| Review focus, leadership, execution, or trust | `$math-review-founder-operations` |
| Plan financing amount, timing, or structure | `$math-plan-fundraise` |
| Build or critique an investor narrative | `$math-build-investor-pitch` |
| Target investors and run the raise | `$math-run-investor-process` |
| Communicate with investors or a board | `$math-write-investor-update` |
| Prepare founder equity or vesting decisions | `$math-structure-founder-equity` |

Compose skills only when one output is an input to the next. Common sequences:

- Validate → Model → Diagnose metrics → Design growth experiments.
- Model → Plan fundraise → Build pitch → Run investor process → Write update.
- Office hours → Founder operating review → one specialist workflow.

## Output

Return:

1. **Situation:** one-paragraph synthesis with facts and assumptions separated.
2. **Primary constraint:** the bottleneck or decision that matters now.
3. **Route:** one primary skill, plus at most two follow-on skills and why.
4. **Required inputs:** only the missing material needed by the next workflow.
5. **Stop conditions:** reasons to pause or seek professional review.
6. **Handoff:** the next skill's exact name, the artifact or evidence it should
   consume, and which assumptions it must keep provisional.

Read [the source map](references/source-map.md) for archive context. End with a
**Watch/read next** section containing one to three direct primary-source links
matched to the route. Never cite a source page as evidence for guidance that is
not actually present there.

## Boundaries

- Treat archive heuristics as starting points, not current benchmarks.
- Do not give legal, tax, accounting, securities, employment, or investment
  conclusions. Produce assumptions and adviser questions instead.
- Do not use low-content archive pages as substantive evidence.
- Do not promise outcomes from a fundraising, pricing, growth, or financing
  tactic.
- Preserve disagreement: when sources pull in different directions, state the
  decision criteria instead of manufacturing one universal rule.
