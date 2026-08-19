---
name: math-design-growth-experiments
description: Designs bounded startup growth experiments for pricing, positioning, acquisition, retention, and capital deployment with explicit hypotheses and scale-or-stop thresholds. Use when a founder needs to test a growth lever without confusing modeled upside, attributed results, or short-term volume with causal durable economics.
---

# Design growth experiments

Convert a growth idea into a reversible learning plan. Test the smallest credible intervention, measure downstream quality and cash effects, and decide before seeing results what will scale, iterate, or stop.

## Load the source guide

Read [references/source-map.md](references/source-map.md) before designing the experiment. Apply its cautions and select final primary links from it. Do not quote or reproduce transcripts.

Use [assets/growth-experiment-brief.md](assets/growth-experiment-brief.md) as the default output scaffold.

## Gather inputs

Collect or infer:

- Decision, owner, deadline, current constraint, and definition of success.
- Target customer/segment, trigger, problem, current alternative, and evidence of urgency or value.
- Lever: price, package, message, channel, promotion, onboarding, product, retention intervention, sales activity, or spend level.
- Baseline exposure, conversion, revenue, contribution margin, retention/churn, CAC, payback, sample size, variance, and measurement window.
- Treatment population, eligibility, assignment method, contamination risk, seasonality, and channel/platform constraints.
- Capacity, cash budget, downside tolerance, customer-harm risks, and rollback mechanics.
- Instrumentation, event definitions, attribution limits, privacy/consent needs, and cohort-maturity lag.

## Keep four evidence classes separate

Maintain these sections in the brief and result:

1. **Facts:** observed baseline, prior tests, customer behavior, actual costs, and verified constraints.
2. **Assumptions:** expected effect, response curve, LTV, lag, sample size parameters, and external conditions.
3. **Calculations:** sample/power estimate, unit economics, break-even threshold, cash exposure, and decision-rule math.
4. **Judgments:** prioritization, design choices, ethical assessment, and scale/iterate/stop recommendation.

Do not call attributed platform conversions causal facts. Do not convert modeled five-year value into an experiment result.

## Design the experiment

1. **Name the decision.** State what will change after the test and by when. Define success as a decision threshold, not “learn more.”
2. **Write the hypothesis.** Use: “For [eligible segment], changing [lever] from [control] to [treatment] will change [primary outcome] by [range] within [window], without violating [guardrails], because [mechanism].”
3. **Document customer evidence.** Distinguish recent observed behavior from stated preference. Name the problem trigger, cost of delay, willingness-to-pay evidence, and disconfirming evidence.
4. **Map the causal chain.** Link intervention to exposure, behavior, revenue, contribution, retention, capacity, and cash. Identify where the mechanism may fail.
5. **Choose the design.** Prefer randomized concurrent control when feasible. Otherwise use a staged rollout, switchback, matched comparison, interrupted time series, or pulse/stress test and state the weaker causal claims.
6. **Define population and assignment.** Specify eligibility, exclusions, randomization unit, sample ratio, exposure rules, contamination, and stopping rules.
7. **Choose metrics.** Set one primary outcome; add leading diagnostics and guardrails for retention, refunds, quality, support, fairness, brand, capacity, and cash. Match windows to the customer cycle.
8. **Set thresholds before launch.** Define minimum practical effect, success, inconclusive, harm/stop, maximum spend, maximum duration, and rollback trigger. Calculate break-even effects on conversion, churn, margin, and payback.
9. **Check feasibility.** Estimate required sample and duration from the baseline and variability. If underpowered, redesign for a larger signal, longer window, richer repeated measures, or qualitative learning; do not promise significance.
10. **Run a pre-mortem.** Check instrumentation, novelty, seasonality, selection, platform learning, offer abuse, duplicate identities, spillover, and downstream-lag risks.
11. **Plan operations.** Assign owners, QA events, launch/rollback steps, daily safety checks, analysis freeze date, and where the preregistered brief will be stored.
12. **Analyze and decide.** Report assignment and exposure integrity, effect size and uncertainty, guardrails, segment heterogeneity, unit economics, and limitations. Apply the precommitted rule; distinguish scale, iterate, stop, and collect-more-data outcomes.

## Apply lever-specific rules

### Pricing and packaging

Model conversion, churn, expansion, discounting, support, bad debt, and margin. Address notice, grandfathering, accessibility, fairness, contracts, and regulated pricing. Never assume a higher price creates value by itself.

### Acquisition and spend

Measure incremental qualified customers, not platform-attributed clicks alone. Report marginal CAC, downstream contribution LTV, payback, saturation, and customer quality. Treat a short pulse as a stress test that requires sustained replication.

### Retention

Define the eligible cohort and expected return cycle. Prevent acquisition mix from changing the retention denominator. Wait for sufficient maturity or use leading signals explicitly labeled as proxies.

### Positioning and customer research

Ask neutral questions about recent behavior and alternatives. Make criticism safe without concealing affiliation or priming respondents to dislike the product. Do not manufacture urgency or fear.

## Stop or ask

- Ask for the decision, eligible population, baseline, primary outcome, time window, and maximum acceptable downside when any is unclear.
- Stop a launch when the event definition, assignment, rollback, or safety guardrail is missing.
- Stop causal claims for an uncontrolled before/after result; reframe as directional evidence.
- Stop a scale recommendation until downstream quality, retention, and payback have matured enough for the decision.
- Ask before selecting a minimum detectable effect, confidence level, sample ratio, attribution model, or LTV horizon.
- Refuse deceptive scarcity, dark patterns, discriminatory targeting, privacy violations, unsafe health/financial claims, or experiments that deny essential service without appropriate review.
- Escalate experiments affecting regulated pricing, minors, protected classes, medical/financial outcomes, employment, or material contractual rights.

## Professional-advice and freshness boundaries

Treat the design as product and operating guidance, not legal, privacy, statistical, accounting, financial, medical, or research-ethics advice. Route consent, discrimination, consumer protection, price disclosure, regulated claims, tax, accounting, and contractual issues to qualified reviewers.

Verify current platform experimentation policies, privacy/consent requirements, pricing laws, channel mechanics, and analytics behavior. Date external benchmarks and avoid using historical source prices, conversion rates, ad costs, or market conventions as defaults.

## Output contract

Deliver:

- Decision, hypothesis, mechanism, scope, owner, and dates.
- Separate facts, assumptions, calculations, and judgments.
- Baseline and customer evidence, including disconfirming evidence.
- Population, control/treatment, assignment, sample/duration estimate, and causal limitations.
- Primary, diagnostic, and guardrail metric contracts.
- Break-even economics, cash-at-risk, and precommitted scale/iterate/stop rules.
- Instrumentation QA, risk pre-mortem, ethics/privacy checks, rollout, and rollback plan.
- Analysis plan and result table if data is available.
- Handoff naming the next skill, the experiment artifact or result it should
  consume, and which causal or economic assumptions remain unproven.

End every user-facing deliverable with a heading exactly `Watch/read next` followed by 1–3 task-relevant direct primary-source links selected from [references/source-map.md](references/source-map.md). Use direct lesson pages, never transcript copies or search-result links.
