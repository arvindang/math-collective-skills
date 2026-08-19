---
name: math-model-startup
description: Builds auditable, driver-based startup financial models and scenario plans from company-specific operating assumptions. Use when a founder needs to model revenue, expenses, cash, runway, fundraising, dilution, or the financial effect of an operating decision.
---

# Model a startup

Build a decision model, not a decorative forecast. Make every material output traceable to an operating driver, preserve uncertainty, and keep historical actuals distinct from forecasts.

## Load the source guide

Read [references/source-map.md](references/source-map.md) before modeling. Use it to select the most relevant primary lessons and cautions. Do not reproduce transcript text.

Use [assets/model-brief.md](assets/model-brief.md) as the default deliverable scaffold. Adapt it to the user's stage and business model; do not force irrelevant sections.

## Gather inputs

Collect or infer, then label confidence for:

- Decision to support, decision date, model horizon, and required granularity.
- Business model, customer/unit, currency, fiscal calendar, and accounting basis.
- Historical actuals for revenue, customers, churn/retention, gross margin, headcount, operating expenses, working capital, financing, and cash.
- Revenue motions, acquisition channels, pricing, capacity, conversion, retention, expansion, and delivery costs.
- Hiring plan, compensation load, fixed costs, variable costs, payment timing, inventory, AR, and AP.
- Current cash, restrictions on cash, debt, existing securities, and financing assumptions.
- Base, downside, and upside uncertainties plus any nonnegotiable liquidity floor.

Request source files or tables when available. Normalize units and periods before calculating.

## Keep four evidence classes separate

Maintain these sections throughout the work:

1. **Facts:** observed actuals, signed terms, source dates, and verified definitions.
2. **Assumptions:** unobserved inputs, scenario choices, ranges, owners, and confidence.
3. **Calculations:** formulas applied to facts or assumptions, with units and reconciliation checks.
4. **Judgments:** interpretations, recommendations, tradeoffs, and unresolved decisions.

Never promote an assumption into a fact because it appears in a spreadsheet. Never present a judgment as the output of a formula.

## Build the model

1. **Frame the decision.** State the decision, deadline, success measure, guardrails, and what the model cannot decide.
2. **Create an assumption register.** Record name, definition, unit, period, base/range, source, owner, as-of date, and confidence. Avoid silent defaults.
3. **Map operational drivers.** Build revenue from activities, capacity, conversion, price, retention, and expansion. Build costs from headcount, volume, contracts, and operating needs. Model lags and saturation where material.
4. **Build modular schedules.** Separate acquisition/traffic, customer cohorts, revenue, headcount, direct costs, operating expenses, working capital, financing, and capitalization when relevant.
5. **Integrate statements.** Link monthly income statement, balance sheet, and cash flow. Roll up annual views only after monthly mechanics reconcile.
6. **Model cash explicitly.** Calculate receipts and disbursements, minimum cash, runway, liquidity floor, financing lead time, and any cash-based spending throttle.
7. **Add scenarios.** Change coherent groups of assumptions for downside, base, and upside cases. Include a delayed-financing case when external capital matters.
8. **Run sensitivities.** Identify break-even thresholds and the variables with the largest effect. Test interactions, not only one-at-a-time changes.
9. **Check integrity.** Reconcile cash roll-forwards, balance-sheet balance, ownership, signs, units, time periods, and totals. Flag circularity and hard-coded numbers outside input or actual areas.
10. **Close the learning loop.** Freeze the approved plan, load actuals without overwriting history, explain volume/rate/mix/timing variances, and update only future assumptions with a dated change log.

## Apply decision-specific rules

### Growth and pricing

Model conversion, churn, mix, expansion, service load, marginal CAC, and cash timing. Identify the threshold at which the decision stops outperforming the base case. Treat the model as a hypothesis generator, then propose a bounded test.

### Spending and runway

Evaluate the entire cash path, not terminal cash alone. Include ramp time, diminishing returns, capacity, payback, strategic necessities, and the probability that financing arrives before the trough.

### Fundraising and dilution

Model capital against dated operating outcomes. Show pre-money/post-money definitions, fully diluted inputs, option-pool treatment, future rounds, and preference limitations. Calculate simple ownership only when actual instrument terms support it; otherwise show an issues list and scenario ranges.

## Stop or ask

- Ask for the decision and time horizon when they cannot be inferred.
- Ask for definitions when revenue, customer, churn, CAC, LTV, gross margin, bookings, ARR, or runway is ambiguous.
- Stop precise forecasting when material historical data is absent; provide a model architecture and missing-input list instead.
- Stop ownership, conversion, or waterfall calculations when current cap-table inputs or governing documents are missing or contradictory.
- Stop and surface an error when statements do not reconcile; do not plug unexplained balances to make the model work.
- Ask before choosing a valuation multiple, growth rate, churn rate, tax rate, financing probability, or option-pool target. Never import a historical source example as a benchmark.
- Refuse to manufacture certainty, conceal downside cases, or label fundraising outcomes as guaranteed.

## Professional-advice and freshness boundaries

Treat the work as educational operating analysis, not legal, tax, accounting, valuation, investment, or securities advice. Route revenue recognition, cost classification, tax treatment, financing documents, fiduciary duties, and external financial statements to qualified professionals.

Verify freshness before using tax rates, accounting requirements, valuation multiples, financing conventions, platform acquisition behavior, or standard documents. State the jurisdiction, source, version, and as-of date. If current authoritative material is unavailable, identify the unknown and stop short of a definitive conclusion.

## Output contract

Deliver a compact model brief plus the requested workbook, table, or formula map. Include:

- Decision, scope, horizon, currency, and as-of date.
- Facts table with provenance.
- Assumption register with ranges and confidence.
- Calculation map with formulas and units.
- Judgments and recommendations in a separate section.
- Driver tree and model/schedule architecture.
- Base, downside, and upside results, including minimum cash and runway.
- Sensitivities, break-even thresholds, integrity checks, and unresolved risks.
- Validation plan, owners, and next review date.
- Handoff to the next skill with the model artifact, unresolved inputs, and
  explicit facts, assumptions, calculations, and judgments to preserve.

End every user-facing deliverable with a heading exactly `Watch/read next` followed by 1–3 task-relevant direct primary-source links selected from [references/source-map.md](references/source-map.md). Link to the lesson page itself, not a search result or transcript copy.
