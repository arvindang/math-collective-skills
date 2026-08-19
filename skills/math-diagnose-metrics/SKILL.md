---
name: math-diagnose-metrics
description: Diagnoses startup KPI, retention, churn, revenue, CAC, LTV, and margin problems using explicit definitions, cohorts, and marginal economics. Use when a founder needs to audit a scorecard, explain a metric change, replace vanity metrics, or determine whether growth is economically healthy.
---

# Diagnose startup metrics

Turn ambiguous dashboard numbers into decision-grade definitions and testable explanations. Pair reconciled aggregate metrics with cohort, channel, segment, and marginal views.

## Load the source guide

Read [references/source-map.md](references/source-map.md) before diagnosing. Apply its source-specific cautions and use it to choose final primary links. Do not quote or recreate transcripts.

Use [assets/metric-diagnostic.md](assets/metric-diagnostic.md) as the default output scaffold.

## Gather inputs

Collect or infer:

- Decision, audience, time range, comparison period, and required cadence.
- Business model, customer/unit, purchase or renewal cadence, lifecycle stages, and revenue model.
- Metric names, formulas, entity/event definitions, inclusion/exclusion rules, windows, denominators, and source systems.
- Raw counts or queries behind numerator and denominator; do not rely only on dashboard percentages.
- Acquisition channel, campaign/offer, cohort, segment, geography, plan, and product-version dimensions.
- Revenue, refunds, discounts, direct/variable costs, acquisition costs, retention/churn, expansion, and cash timing.
- Known instrumentation, identity, attribution, late-arriving data, and cohort-maturity limitations.

## Keep four evidence classes separate

Maintain distinct sections for:

1. **Facts:** observed counts, actual transactions, reconciled financials, definitions in production, and dated source evidence.
2. **Assumptions:** identity rules, attribution choices, expected lifetime, incomplete-cohort projections, and cost allocations.
3. **Calculations:** formulas, units, periods, denominators, cohort logic, and reconciliation bridges.
4. **Judgments:** diagnoses, likely drivers, priorities, and recommended tests.

Never describe a projected LTV, attributed conversion, or causal explanation as an observed fact.

## Diagnose

1. **Frame the decision.** Ask what action changes if the metric rises or falls. Reject a KPI with no owner or decision use.
2. **Write the metric contract.** Define entity, event, numerator, eligible denominator, window, frequency, source, owner, exclusions, and known failure modes.
3. **Reconstruct raw counts.** Calculate the metric from auditable numerator and denominator. Reconcile revenue and customer totals to the authoritative system.
4. **Test the denominator.** Check whether acquisition volume, cohort eligibility, seasonality, or channel mix can improve the ratio without improving behavior.
5. **Build comparison cuts.** Show aggregate context, then cohort, channel, segment, offer, and recent-flow views. Report sample size and maturity.
6. **Decompose movement.** Separate volume, rate, mix, timing, retention, expansion, price, and cost effects. Mark plausible explanations as hypotheses until tested.
7. **Evaluate economics.** Define contribution boundary; calculate CAC, contribution LTV, and payback by relevant cohort/channel. Distinguish blended, paid, average, and marginal CAC.
8. **Look for gaming and abuse.** Ask how the KPI could improve while the business worsens. Inspect promotions, duplicate identities, refunds, low-quality users, and delayed churn.
9. **Prioritize causes.** Rank by evidence strength, economic impact, fixability, and urgency. State what evidence would falsify each leading hypothesis.
10. **Design the next measurement.** Specify query correction, instrumentation repair, customer research, or bounded experiment and its decision threshold.

## Apply metric-specific rules

### Retention and churn

Define the eligible cohort and return/retention event before calculating. Match the window to expected customer behavior. Distinguish logo, revenue, user, and usage retention. Treat return behavior as a satisfaction proxy, not direct proof. Handle reactivation, censoring, seasonality, and identity stitching explicitly.

### CAC and LTV

Include the relevant acquisition spend and document treatment of people, tooling, promotions, and brand. Calculate contribution value after relevant variable delivery costs, not lifetime sales. Show cohort maturity, payback, uncertainty, and marginal response at the next volume. Do not declare viability from LTV/CAC alone.

### Revenue and margin

Define recognized revenue, MRR, ARR, annualized run rate, bookings, backlog, ACV, and TCV separately. Reconcile operating metrics to accounting revenue. Define gross profit and contribution margin by purpose and cost boundary; do not use the labels interchangeably.

### KPI architecture

Select a small causal chain of leading, outcome, and guardrail measures. Prefer sensitive recent-flow metrics for diagnosis and stable aggregate metrics for reconciliation. Add a gaming test and an owner to every KPI.

## Stop or ask

- Ask for the decision, entity, event, time window, and denominator when any is unclear.
- Ask for raw counts or query logic when only a percentage or chart image is available.
- Stop causal claims when evidence is observational; label hypotheses and propose a test.
- Stop precise LTV when cohorts are immature or retention shape is unknown; provide bounded scenarios instead.
- Stop cross-company comparisons until definitions, periods, currencies, cost boundaries, and stages are normalized.
- Stop accounting conclusions when revenue recognition or cost classification is disputed; route to an accountant.
- Refuse to optimize a metric that encourages deception, customer harm, privacy abuse, or concealment of business deterioration.

## Professional-advice and freshness boundaries

Treat the diagnosis as operating analysis, not accounting, audit, investment, legal, tax, or privacy advice. Route external reporting, revenue recognition, cost classification, regulated disclosures, and privacy-sensitive identity tracking to qualified professionals.

Verify freshness for analytics vendor behavior, attribution rules, privacy requirements, accounting standards, market benchmarks, and channel mechanics. State the source and as-of date for any external reference. Prefer company data and explicit definitions over generic benchmarks.

## Output contract

Deliver:

- Decision and metric-health summary.
- Facts, assumptions, calculations, and judgments as separate labeled sections.
- Metric dictionary and numerator/denominator audit.
- Aggregate plus cohort/channel/segment tables with sample-size and maturity notes.
- Movement decomposition and ranked hypotheses with evidence for/against.
- Unit-economics view where relevant, including cost boundary and payback.
- Data-quality issues, gaming risks, unresolved questions, and next measurement/test.
- Owners, decision thresholds, and review date.
- Handoff naming the next skill, the metric diagnostic it should consume, and
  unresolved definitions or causal hypotheses that remain provisional.

End every user-facing deliverable with a heading exactly `Watch/read next` followed by 1–3 task-relevant direct primary-source links selected from [references/source-map.md](references/source-map.md). Link to lesson pages, not copied transcripts or search results.
