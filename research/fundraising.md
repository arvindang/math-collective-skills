# Fundraising track: source review and skill-design notes

## Corpus audit and method

- Selection rule: every object in `/tmp/henikoff-corpus-v2.json` whose `track` is exactly `Fundraising`.
- Verified count: **19 of 19 items reviewed**. The corpus summary independently reports 19 Fundraising items, and a direct filter also returns 19.
- Coverage: all 19 are video lessons with transcript and prose fields. Publication dates run from November 6, 2018 through October 12, 2023.
- Evidence method: the notes below synthesize the supplied transcript, description, and page prose for each item. They do not reproduce the transcripts. Specific examples and numbers are retained only where they explain the source's reasoning.
- Transcript completeness check: the corrected corpus includes the full visible timed transcript segments for all 19 lessons. In particular, "3 Passes on How to Make a Better Pitch," "The Rule of Two," and "Convertible Debt/SAFE vs. Equity" now continue through their substantive conclusions rather than stopping mid-sentence.
- Interpretation boundary: this is a review of the authors' guidance, not an endorsement of every rule. Legal, tax, accounting, securities, financing, and valuation statements need current professional review before being turned into prescriptive outputs.

## Item-by-item review

### 1. [3 Passes on How to Make a Better Pitch](https://startups.henikoff.com/lesson/3-passes-on-how-to-make-a-better-pitch)

**Distilled principle.** A technically complete pitch becomes memorable only after three editing passes: reduce it to its essential ideas, recast it from the audience's perspective, and design for the emotion that should support the desired action. The source treats the first meeting as a step toward a second meeting rather than a venue for conveying every available fact.

**Actionable framework.** Run the deck through three separate reviews:

1. Essence: inventory all factual claims; rank them; select roughly three or four headlines the audience must remember; move supporting detail to an appendix.
2. Empathy: research the investor's thesis, process, history, portfolio, and likely questions; then evaluate every slide from that investor's decision frame. Portfolio founders can be useful sources about how the investor actually works.
3. Emotion: name the intended audience response for each major section and check whether the evidence earns it. The source uses trust for the team slide and also suggests responses such as excitement, urgency or fear of missing out, desire, and the feeling of recognizing an opportunity early.
4. Remove anything that neither advances a core headline nor answers an audience concern; rehearse a concise path and retain detail for questions.

**Cautions and edge cases.** Compression can hide assumptions or remove evidence that a specialist investor needs. Audience empathy must not become selective disclosure or tailored misrepresentation. Emotional design should clarify stakes and build warranted confidence, not manipulate. The emotions named in the source are illustrations rather than an exhaustive or ethically neutral taxonomy; a skill should ask whether the underlying evidence warrants the intended response.

**Proposed downstream skill tags.** `pitch-review`, `storytelling`, `deck-editing`, `investor-empathy`, `meeting-prep`

### 2. [What are investors REALLY thinking about when they ask about your CAC…?](https://startups.henikoff.com/lesson/what-are-investors-really-thinking-about-when-they-ask-about-your-cac)

**Distilled principle.** Investors use historical unit economics to judge whether future growth is scalable and financeable. A single blended customer-acquisition-cost figure obscures channels with different economics and scaling behavior; trends and components support a more credible forecast.

**Actionable framework.** Build an investor-facing unit-economics bridge:

1. Define CAC and LTV precisely, including time period, included costs, and customer/cohort scope.
2. Split acquisition by channel, such as organic, referral, social, and paid, instead of leading with a blended average.
3. Show each channel's historical volume and CAC trend, then state its plausible scaling constraint.
4. Show LTV by relevant segment or cohort and how it has changed over time.
5. Connect the historical series to an explicit forward model: channel mix, CAC, retention, contribution, and resulting capital need.
6. Identify which assumptions are observed, which are modeled, and which remain unproven.

**Cautions and edge cases.** Early cohorts may be too immature for reliable LTV, attribution may be multi-touch, and paid-channel CAC can rise as spend scales. Definitions vary across companies, so a skill must not compare figures before normalizing them. High LTV/CAC alone does not establish payback speed, cash efficiency, retention quality, or causality. Forecasts should be presented as scenarios rather than facts.

**Proposed downstream skill tags.** `unit-economics`, `kpi-diligence`, `cac-ltv`, `forecast-narrative`, `financial-modeling`

### 3. [Think twice before committing to strategic investors](https://startups.henikoff.com/lesson/think-twice-before-committing-to-strategic-investors)

**Distilled principle.** A corporate or strategic investor can reduce exit optionality if prospective acquirers believe the insider has privileged information or an unbeatable position. The source's simple rule is to prefer no strategic investor or multiple strategics that can constrain one another, rather than a single likely acquirer on the inside.

**Actionable framework.** Before accepting strategic capital:

1. State why the party is investing and what commercial, data, governance, information, or acquisition rights it expects.
2. Map credible future acquirers and ask how each would perceive the strategic's access and influence.
3. Review board seats, observer rights, information rights, rights of first offer/refusal, exclusivity, vetoes, and change-of-control provisions.
4. Compare three cap-table scenarios: financial investor, one strategic, and two or more credible strategics.
5. Quantify near-term commercial value separately from long-term financing and exit constraints.
6. Use counsel to design recusals, information boundaries, standstills, or other protections where appropriate.

**Cautions and edge cases.** The "zero or at least two" rule is a useful prompt, not a universal result. A strategic can add distribution, validation, supply access, regulatory expertise, or a valuable acquisition path; multiple strategics can introduce conflicts rather than solve them. Whether another bidder is deterred depends on rights and process, not merely the investor's label. Board duties, confidentiality, antitrust, and securities issues require counsel.

**Proposed downstream skill tags.** `investor-fit`, `strategic-capital`, `cap-table-risk`, `exit-optionality`, `governance-review`

### 4. [Raise for Outcomes, Not Headlines](https://startups.henikoff.com/lesson/math-101-raise-for-outcomes-not-headlines)

**Distilled principle.** A large round or high valuation is not itself a business outcome. It raises the operating milestones needed to support the next financing and the exit value needed to produce investor returns. Capital and price should therefore be chosen by working backward from achievable outcomes.

**Actionable framework.** For every contemplated raise:

1. Set the proposed pre-money and post-money valuation and calculate ownership sold.
2. Define the operating outcomes the cash must produce before the next financing decision: revenue, usage, retention, margin, regulatory progress, or another stage-appropriate proof point.
3. Build base, upside, and downside runway models through those outcomes.
4. Estimate the next round's plausible valuation range from the resulting metrics; test flat and down-round scenarios.
5. Model an exit range and expected stakeholder proceeds rather than optimizing the current headline valuation.
6. Reduce or re-stage the round if the milestone jump is not credible with the proposed budget and time.

**Cautions and edge cases.** The talk reflects the unusually strong 2021 fundraising market. Down rounds can be painful but may be rational or necessary; "avoid at all costs" should not be encoded literally when the alternative is insolvency or a structurally worse deal. Exit math depends on preferences, dilution, taxes, and future financings. Some businesses appropriately prioritize long-duration strategic value over a near-term next-round mark.

**Proposed downstream skill tags.** `round-sizing`, `valuation`, `milestone-financing`, `down-round-risk`, `exit-scenarios`

### 5. [Don’t Send the Deck](https://startups.henikoff.com/lesson/math-101-dont-send-the-deck)

**Distilled principle.** In a relationship-led early-stage process, the immediate objective of first contact is a meeting, not remote evaluation of a complete deck. The source recommends a one-page teaser that gives enough evidence to create interest while reserving the full narrative for a live conversation.

**Actionable framework.** Create an outreach sequence:

1. Build a one-page teaser that can be scanned quickly: problem, solution, business model, team, salient proof, and a clear visual signal of traction where one exists.
2. Keep it genuinely one page; reveal the strongest reasons to engage without attempting to answer every diligence question.
3. Respond to a deck request with a courteous explanation that the deck is designed to be presented, plus specific meeting times.
4. In the meeting, use the full deck as a discussion scaffold.
5. Send the exact presented PDF after the meeting, along with next steps.
6. Preserve version dates so a later update can demonstrate progress against the prior snapshot.

**Cautions and edge cases.** Many funds now require an asynchronous deck for triage, and refusing can remove a company from the process. A teaser should not manufacture mystery at the expense of basic qualification. Founders should adapt to investor workflow, fundraising stage, geography, and inbound strength. Confidential or competitively sensitive information needs access discipline, but an unsolicited deck is rarely protected merely by a confidentiality legend.

**Proposed downstream skill tags.** `teaser-builder`, `investor-outreach`, `deck-workflow`, `meeting-conversion`, `fundraising-collateral`

### 6. [How to Get Great Investor Meetings](https://startups.henikoff.com/lesson/math-101-how-to-get-great-investor-meetings)

**Distilled principle.** Investors gain conviction from a trajectory, not a single observation. Start relationship-building months before a formal raise, solicit specific advice, document the success criteria, execute against them, and return with visible progress.

**Actionable framework.** Approximately three to six months before fundraising:

1. Identify high-fit investors worth building a relationship with.
2. Ask for advice rather than a commitment: given the company's current position, what proof would make a later financing compelling?
3. Take detailed notes and send a prompt recap that lists the metrics or milestones heard.
4. Convert the advice into an internal plan while retaining founder judgment about which advice to follow.
5. When results arrive, reply in the original email thread with the prior criteria and the new actuals.
6. Ask for a meeting and show a time series that makes the company's trajectory legible.

**Cautions and edge cases.** The source says the investor will effectively have to take the later meeting; that is persuasive rhetoric, not a guarantee. Market conditions, thesis, fund capacity, or portfolio conflicts can change. Founders should not treat an advice meeting as a trick or imply that advice was a commitment. Chasing bespoke investor milestones can distort the product strategy, so criteria should be checked against the company's own plan.

**Proposed downstream skill tags.** `fundraising-timeline`, `investor-relationships`, `milestone-tracking`, `investor-crm`, `traction-narrative`

### 7. [Friction Kills Deals](https://startups.henikoff.com/lesson/math-101-friction-kills-deals)

**Distilled principle.** Familiar, standard financing documents lower delay, legal cost, and surprise. A founder should compare the actual economic benefit of a bespoke term with its transactional cost and closing risk instead of negotiating a headline term in isolation.

**Actionable framework.** For each proposed document change:

1. Establish the current standard form appropriate to stage and jurisdiction; the source cites NVCA forms, Series Seed documents, and YC SAFEs.
2. Describe the requested deviation and the exact scenario in which it changes economics or control.
3. Model founder ownership and investor outcomes across likely next-round valuations, not just the face value of a discount or cap.
4. Estimate additional legal expense, diligence, negotiation time, and risk of losing momentum.
5. Preserve the standard if the deviation is immaterial; negotiate when the modeled benefit or avoided risk is genuinely material.
6. Have qualified counsel confirm the final effect rather than relying on a simplified cap-table example.

The lesson illustrates the test with a $5 million SAFE cap and a discount change from 20% to 10%. Under its particular $5.5 million next-round example, the modeled founder-ownership difference is only 0.4 percentage points, making the author view the added friction as disproportionate.

**Cautions and edge cases.** Standard forms and market conventions change, and a document standard in the United States may be inappropriate elsewhere. Small ownership changes can still be material in aggregate or when coupled with control provisions. Closing a financing is not more important than avoiding an abusive or strategically damaging term. The source's cap, discount, valuation, pool, and ownership figures are illustrative, not a reusable rule.

**Proposed downstream skill tags.** `term-sheet-review`, `deal-friction`, `safe-modeling`, `scenario-analysis`, `legal-process`

### 8. [Our Business is a Relationship Business](https://startups.henikoff.com/lesson/math-101-our-business-is-a-relationship-business)

**Distilled principle.** Durable relationships grow when counterparties feel they retain agency and receive material bad news early. For founders, investor transparency is not merely reporting; it gives investors a chance to help and reduces fear of concealed problems.

**Actionable framework.** Use a disciplined adverse-update format:

1. Report the issue early enough for help to matter.
2. Separate known facts, current interpretation, and unresolved questions.
3. Explain impact on metrics, runway, customers, team, or commitments.
4. Name the response owner, immediate mitigation, and decision date.
5. Make a concrete ask of the investor: introduction, expertise, recruiting, capital planning, or simply awareness.
6. Close the loop with updates until the issue is resolved.

**Cautions and edge cases.** Transparency is not indiscriminate disclosure. Customer data, employee matters, security incidents, litigation, privileged legal advice, and material nonpublic information may require controlled channels and counsel. Different investors have different information rights. Early disclosure should be accurate and scoped; speculation presented as fact can create its own damage.

**Proposed downstream skill tags.** `investor-updates`, `bad-news-communication`, `board-relations`, `trust-building`, `crisis-escalation`

### 9. [Back to Basics: Valuations, Option Pools and What You Need to Know Before Raising Capital](https://startups.henikoff.com/lesson/math-101-back-to-basics-valuations-option-pools-and-what-you-need-to-know-before-raising-capital)

**Distilled principle.** Founders must understand the fully diluted capitalization behind pre-money and post-money labels. When a new or expanded option pool is included in the negotiated pre-money capitalization, its dilution falls primarily on existing holders rather than the incoming investor.

**Actionable framework.** Reconstruct every priced-round term sheet:

1. Define whether valuation is pre-money or post-money and what securities are included in the fully diluted denominator.
2. List issued shares, outstanding options, warrants, converts, and the existing unallocated option pool.
3. Specify the required unallocated pool after closing and whether the top-up occurs pre- or post-money.
4. Solve for pool-top-up shares and new preferred shares together; do not simply add a percentage to the current share count.
5. Produce before-and-after ownership for founders, employees/pool, existing investors, and new investors.
6. Reconcile price per share, proceeds, and post-money value, then stress-test alternative pool sizes.

The lesson's simplified example starts with a $4 million pre-money valuation, $1 million of new capital, and a 10% post-closing option pool. It arrives at approximately 70% founders, 10% pool, and 20% new preferred ownership, demonstrating the pool-top-up effect.

**Cautions and edge cases.** Saying that the option pool is always included in pre-money valuation overstates a negotiable convention. Pool treatment and the fully diluted definition vary. The example omits existing investors, SAFEs/notes, warrants, multiple preferences, secondary sales, and tax consequences. A cap-table skill should show formulas and assumptions and require legal/accounting verification.

**Proposed downstream skill tags.** `cap-table`, `dilution-calculator`, `option-pool`, `priced-round`, `term-sheet-literacy`

### 10. [WAIT – Now Troy Likes Convertible Notes?](https://startups.henikoff.com/lesson/math-101-wait-now-troy-likes-convertible-notes)

**Distilled principle.** Convertible instruments can be well suited to a short bridge or a small, very early rolling raise even if priced equity is preferable for a substantial institutional round. Instrument choice should match the financing's size, duration, and role in reaching the next round.

**Actionable framework.** Consider a convertible bridge when:

1. The company has a reasonably defined next priced round.
2. The bridge funds only a short period and a specific increment of proof.
3. The amount is small relative to the expected new cash in that round.
4. Rolling closes and low legal cost create real execution value.
5. Conversion scenarios, maturity or trigger mechanics, and dilution are modeled before signing.

For a very early financing, compare a simple convertible instrument with a priced round based on total amount, investor coordination, ability to price, and governance needs. The source offers historical heuristics of a note below roughly $500,000, equity above roughly $1 million, and judgment in between; it also explains that a larger bridge may be sensible when small relative to a much larger expected round.

**Cautions and edge cases.** The dollar thresholds and accelerator example date to 2019 and are not universal market standards. A SAFE is not debt; notes add maturity, interest, creditor, and solvency considerations that SAFEs generally do not. A bridge can become a bridge to nowhere if the next round is not credible. Current forms, tax treatment, local law, and investor rights need professional review.

**Proposed downstream skill tags.** `instrument-selection`, `convertible-note`, `safe`, `bridge-financing`, `rolling-close`

### 11. [A Twist on Convertible Notes](https://startups.henikoff.com/lesson/math-101-a-twist-on-convertible-notes)

**Distilled principle.** A fixed cap in a short bridge can create an unintended valuation signal: too high may make later pricing appear like a decline, while too low may anchor later investors. The source proposes a less common midpoint structure whose conversion valuation is determined between the prior round's post-money valuation and the next round's pre-money valuation.

**Actionable framework.** If evaluating this structure:

1. Confirm that the financing is truly a short bridge between identifiable priced rounds.
2. Define the prior post-money and future pre-money bases precisely, including fully diluted capitalization.
3. Write an unambiguous midpoint formula and specify how it interacts with interest, discounts, minimum/maximum prices, maturity, and a sale before conversion.
4. Model up, flat, and down-round cases and the resulting ownership for founders, bridge investors, and new investors.
5. Ask prospective lead investors whether the mechanism creates diligence or closing problems.
6. Compare it with a standard capped instrument, an uncapped discount instrument, and priced equity on total cost and signaling.

**Cautions and edge cases.** A midpoint note is nonstandard and may add exactly the friction warned about elsewhere in the corpus. Down rounds, extension rounds, no qualified financing, or a change in fully diluted definitions can produce surprising results. The structure may also be unfamiliar to counsel and investors, increasing expense and uncertainty. It should be presented as an option for professional evaluation, not a default template.

**Proposed downstream skill tags.** `convertible-structuring`, `midpoint-note`, `valuation-signaling`, `bridge-scenarios`, `nonstandard-terms`

### 12. [The Rule of Two](https://startups.henikoff.com/lesson/math-101-the-rule-of-two)

**Distilled principle.** Accumulated convertible instruments can consume so much of a priced round that little new cash arrives relative to the dilution. The source's planning heuristic is that the next round should bring at least twice as much new capital as the converting balance.

**Actionable framework.** Maintain a conversion-overhang test:

1. Sum principal or purchase amounts plus any note interest expected to convert; separate each cap and discount class.
2. Forecast the next round's realistic new-money range rather than its aspirational target.
3. Flag a warning when converting amounts exceed roughly half of expected new money.
4. Model ownership and effective prices for founders, converting investors, and new investors under multiple round valuations and pool top-ups.
5. Before adding another bridge tranche, recalculate both the new-money need and the metrics required to support it.
6. If overhang is excessive, evaluate a priced round, recapitalization, insider extension, smaller plan, or other counsel-led restructuring.

The example describes an initially planned $1 million convertible raise that grows to $2 million before a $3 million priced round. It uses the resulting founder and new-investor ownership to show why the financing can feel undercapitalized even though a round technically closes: founders perceive substantial dilution without enough new operating cash, while new investors perceive too little ownership for the cash they supplied. The conclusion frames the heuristic as a way to plan two or three financing moves ahead.

**Cautions and edge cases.** Two-to-one is a heuristic, not a legal or financial invariant. Outcome depends on caps, discounts, interest, pre- versus post-money SAFE forms, round valuation, option-pool expansion, and investor rights. The source groups SAFEs with debt for simplicity, but a downstream skill must keep the instruments legally distinct.

**Proposed downstream skill tags.** `conversion-overhang`, `rule-of-two`, `round-planning`, `cap-table-scenarios`, `bridge-risk`

### 13. [Convertible Debt/SAFE vs. Equity](https://startups.henikoff.com/lesson/math-101-convertible-debtsafe-vs-equity)

**Distilled principle.** Convertible instruments reduce immediate pricing, coordination, and legal work, while a priced round gives stakeholders clearer ownership, economics, governance, and control. The easy current transaction can transfer complexity to the next financing. The source also treats completing a priced round and establishing a board and formal rights as an early exercise in organizational rigor that later investors may value.

**Actionable framework.** Compare instruments on a common decision sheet:

1. Capital required and expected number/timing of closes.
2. Ability and willingness to establish a valuation today.
3. Legal cost, closing time, maturity risk, and administrative burden.
4. Ownership certainty across plausible future prices.
5. Governance needs: board, protective provisions, information rights, and preferences.
6. Conversion overhang and effect on the next lead investor.
7. Downside paths if no qualified financing occurs.

Use the sheet to select the structure that keeps both this round and the next one workable, then model the actual documents rather than relying on category labels.

**Cautions and edge cases.** A SAFE is not convertible debt, and current post-money SAFE forms can make ownership effects more explicit than older forms. Priced rounds can sometimes use staged or rolling closings, and financing choices extend beyond the two categories discussed. The talk is from early 2019 and market documents have evolved. Its preference for priced equity should remain a point of view rather than a universal recommendation; formal governance is valuable only when proportionate to the company's stage and financing.

**Proposed downstream skill tags.** `financing-comparison`, `priced-equity`, `convertible-note`, `safe`, `governance-design`

### 14. [Finding the Right Investor](https://startups.henikoff.com/lesson/math-101-finding-the-right-investor)

**Distilled principle.** Fundraising is a targeted sales process: qualify investors, secure a relevant introduction, earn a meeting, let the investor's questions shape the conversation, and follow up precisely.

**Actionable framework.** Build and operate a fundraising funnel:

1. Find investors with relevant stage, sector, business-model, geography, and check-size fit, excluding direct competitive conflicts.
2. Prioritize the list by fit, likelihood, and potential introduction path.
3. Prepare a short, investor-specific forwardable note explaining the fit with concrete portfolio evidence.
4. Attach a one-page teaser; request a live or video conversation for the full deck.
5. In the meeting, answer investor questions directly even if the discussion leaves the slide order.
6. Send individual thanks, the reviewed deck, requested material, and explicit next steps.
7. Track stage, objections, follow-up owner, and date in a CRM-like system.

**Cautions and edge cases.** AngelList's branding and database landscape have changed since 2018, and data sources should be current. Warm introductions often help but cold outreach can work when it is well targeted. Refusing a deck is risky in funds with async screening. A question-led meeting still needs a clear core narrative, and portfolio adjacency must be checked for conflict and information leakage.

**Proposed downstream skill tags.** `investor-targeting`, `fundraising-funnel`, `warm-intro`, `meeting-facilitation`, `follow-up`

### 15. [The Secret of the Ask](https://startups.henikoff.com/lesson/secret-of-the-ask)

**Distilled principle.** If a company has a defensible fundraising range, opening at the lower end can make early commitments look consequential and build momentum. The main pitch should connect the amount raised to dated business milestones; detailed spending belongs in supporting material.

**Actionable framework.** Structure the ask:

1. Derive a minimum and maximum raise from runway, milestones, buffers, and dilution rather than inventing a marketing range.
2. Choose an announced target that is sufficient on its own and can close credibly.
3. Track soft interest, diligence, signed commitments, and funded cash separately; never imply that one is another.
4. If demand exceeds the target, decide deliberately whether extra capital improves risk-adjusted outcomes enough to justify dilution.
5. In the core deck, state amount, measurable outcome, and target date.
6. In the appendix and model, show hiring, product, sales, working-capital, and contingency assumptions that support the milestone.

**Cautions and edge cases.** Momentum must be truthful; false scarcity or inflated commitments can create reputational and legal risk. A low target that cannot fund the plan contradicts the corpus's advice to cross the financing valley. Extending an oversubscribed round affects dilution, governance, and future milestones. Many investors properly require a detailed use-of-funds model even if the top-line pitch emphasizes outcomes. Communications about a securities offering require counsel.

**Proposed downstream skill tags.** `fundraising-ask`, `round-target`, `momentum`, `use-of-funds`, `milestone-plan`

### 16. [Pot of Gold](https://startups.henikoff.com/lesson/math-101-pot-of-gold)

**Distilled principle.** A venture pitch must establish both a sufficiently large possible outcome and a credible sequence of de-risking steps. Investors finance the future, so the presentation should spend more time on how present evidence becomes future value than on repeating the problem and product description.

**Actionable framework.** The source suggests a presentation-time heuristic:

1. Use no more than roughly 20% to establish the problem.
2. Use no more than roughly 20% for the solution and current traction.
3. Use roughly 60% for the forward path: market/value potential, current round, time purchased, measurable next milestone, sales/product mechanics, and likely subsequent stage.
4. Make the immediate stage highly specific; allow later stages to become progressively more uncertain.
5. Link each financing tranche to a time-bound operating outcome, not merely a list of expenses.

**Cautions and edge cases.** The percentages are a rehearsal heuristic, not a required deck structure. No startup path is truly low risk; the credible claim is that identified risks can be retired in a sensible order. Deep-tech, regulated, scientific, or novel-market pitches may need more foundational explanation. Large-outcome claims need bottom-up support and should not be presented as certainty.

**Proposed downstream skill tags.** `venture-case`, `pitch-architecture`, `future-narrative`, `de-risking-roadmap`, `milestone-financing`

### 17. [Impact of Raising Too Much](https://startups.henikoff.com/lesson/impact-of-raising-too-much)

**Distilled principle.** More capital is beneficial only if it creates enough incremental enterprise value to compensate for dilution and financing preferences. Capital efficiency can align founders and early investors because unnecessary rounds reduce both groups' proceeds at a fixed exit value.

**Actionable framework.** Compare capital plans on a common exit model:

1. Set operating scenarios with different financing amounts and probabilities of reaching different outcomes.
2. Build the full round-by-round cap table, including option pools, converts, and dilution.
3. Add liquidation preferences and other waterfall terms rather than using ownership percentages alone.
4. Calculate founder proceeds and each investor cohort's proceeds and multiple across exit values.
5. Compare marginal capital raised with marginal expected enterprise value, survival probability, and time.
6. Choose the least capital that robustly funds the target outcome, including a realistic buffer.

The source holds a $50 million exit constant across examples. Its high-capital scenario raises $29 million and estimates approximately $4.7 million for founders and only 1.2x for the earliest investor; a more modest $9 million total raise estimates approximately $16.2 million for founders and 4.1x for the earliest investor. These figures illustrate sensitivity to financing history, not universal benchmarks.

**Cautions and edge cases.** The supporting spreadsheet referenced by the page is not present in the supplied corpus, so its formulas could not be independently audited here. Holding exit value constant can understate the reason to raise: more capital may increase survival, speed, or ultimate value. The page's reference to a 2017 average exit and the simplified bootstrap proceeds are dated and omit taxes, employees, preferences, and transaction costs. "Raise less" must not be interpreted as undercapitalizing the milestone.

**Proposed downstream skill tags.** `capital-efficiency`, `dilution-model`, `exit-waterfall`, `round-scenarios`, `founder-proceeds`

### 18. [When to Raise Capital](https://startups.henikoff.com/lesson/math-101-when-to-raise-capital)

**Distilled principle.** Size a raise by the time and resources required to approach financial self-sufficiency or another point of real financing leverage. The next fundraise should be planned during the current one, so future capital is an option for acceleration rather than an emergency for survival.

**Actionable framework.** Build a timing model:

1. Forecast monthly cash, expenses, revenue, gross margin, and working capital.
2. Define the leverage milestone: near break-even in the source, or another stage-appropriate proof that reduces dependency on external capital.
3. Calculate time and cash to the milestone in base, delayed, and adverse cases.
4. Add the time needed to run the next financing process plus an operating buffer.
5. Compare the value created by incremental capital with the ownership surrendered.
6. Revisit the model as actual revenue and expense trajectories change.

**Cautions and edge cases.** Near break-even is not the correct immediate target for every venture-backed company. Network businesses, deep tech, biotech, climate infrastructure, or a time-sensitive land grab may rationally prioritize scale or technical proof. "Within spitting distance" must be replaced by measurable thresholds. Market windows, investor appetite, and cash volatility also affect timing, and forecasts should not hide uncertainty.

**Proposed downstream skill tags.** `funding-timing`, `runway-model`, `break-even`, `financing-leverage`, `multi-round-planning`

### 19. [Funding the Valley](https://startups.henikoff.com/lesson/funding-the-valley)

**Distilled principle.** A startup is easiest to finance before execution exposes uncertainty or after it has emerged into demonstrable scale. An idea-stage raise should carry the company through the difficult proof-building period because attempting to refinance in the middle can force punitive terms.

**Actionable framework.** Before an early raise:

1. Draw the stage path from idea through the period of maximum execution uncertainty to a fundable proof point.
2. List the product, market, hiring, regulatory, and sales risks that must be retired along the path.
3. Estimate time and cash for each, then run delay and overrun scenarios.
4. Add enough financing-process lead time that fundraising begins before the cash crisis.
5. Model a flat/down round and the impact of anti-dilution terms on common holders.
6. Set leading indicators that reveal early whether the company is crossing the valley or needs a plan change.

The source grounds the warning in the author's SurePayroll experience: an $8 million Series A was not enough to reach the expected point, and an insider-supported down round with then-common full-ratchet protection heavily diluted common holders and roughly halved the author's personal stake.

**Cautions and edge cases.** "Raise enough" must be reconciled with the separate warning against raising too much. The right amount is scenario-based milestone capital, not the maximum available. Full-ratchet anti-dilution is not a timeless default, and current prevalence depends on market and deal. Existing investors may not support a bridge. Large buffers can increase dilution and spending, while small buffers increase financing risk.

**Proposed downstream skill tags.** `funding-valley`, `runway-stress-test`, `down-round`, `anti-dilution`, `risk-retirement`

## Cross-source themes

### 1. Make the future legible

The strongest connective tissue across the track is that investors finance a future state, not a historical snapshot. CAC/LTV components, milestone-based uses of funds, lines rather than points, and the large-outcome/de-risked-path pitch are all versions of the same reasoning. A reusable skill should translate evidence into a forecast while labeling uncertainty rather than merely polishing a narrative.

### 2. Treat each round as one move in a sequence

The sources repeatedly advise optimizing for the next round or even the round after that. Current valuation affects the next milestone bar; convertible balances affect how much new cash the next round must contain; option-pool treatment affects later ownership; and today's investor rights affect tomorrow's exit competition. Skills should default to multi-round scenarios, not single-transaction answers.

### 3. Raise to a milestone, with a buffer, and preserve optionality

"When to Raise Capital," "Funding the Valley," "The Secret of the Ask," and "Raise for Outcomes" converge on a stage-gated model: capital should buy a specific, dated reduction in risk. "Impact of Raising Too Much" adds the counterweight that extra capital must justify its dilution. The synthesis is neither "raise as much as possible" nor "always raise less"; it is "fund a robust milestone plan and quantify the buffer."

### 4. Fundraising behaves like enterprise sales and relationship management

Investor targeting, warm introductions, teaser collateral, live meetings, advice conversations, follow-up, and transparent bad-news updates form a coherent funnel. The process values fit and trust as much as collateral. A downstream package should therefore include operational artifacts such as a target rubric, forwardable intro, meeting brief, CRM fields, and investor update—not only a pitch-deck generator.

### 5. Reduce unpriced friction, but understand the economics

Standard documents can lower time and legal cost, but simplicity is not a substitute for modeling. Several lessons insist on understanding cap-table math before accepting apparently easy terms. A useful skill should calculate the materiality of a deviation, identify control/legal risks it cannot evaluate, and route those issues to counsel.

### 6. Capital-source fit matters beyond price

The strategic-investor warning, investor-targeting guidance, and relationship lesson treat the investor as a long-lived stakeholder. Check size and valuation are incomplete selection criteria; thesis, behavior, rights, conflict, follow-on capacity, and exit effects belong in the decision.

### 7. Narrative and evidence must reinforce each other

The pitch lessons advocate focus, audience empathy, emotion, future orientation, and a teaser. The metrics lessons require disaggregated, trend-based evidence. Together they imply that storytelling should order and interpret evidence, not replace it.

## Tensions and contradictions to preserve in the skill package

1. **Enough runway versus too much capital.** "Funding the Valley" warns that underfunding creates a punitive mid-valley raise; "Impact of Raising Too Much" warns that excess financing destroys stakeholder economics. Resolve with milestone-based base/downside scenarios and explicit dilution—not a slogan.
2. **Priced equity preference versus judicious convertibles.** "Convertible Debt/SAFE vs. Equity" favors priced equity for a real round, while "WAIT" endorses convertibles for small early raises and short bridges. Route by size, duration, pricing readiness, governance, and conversion overhang.
3. **Standard documents versus a midpoint note.** "Friction Kills Deals" discourages low-value customization; "A Twist on Convertible Notes" proposes a nonstandard midpoint mechanism. Require a material-benefit test and investor/counsel validation before recommending novelty.
4. **Do not send the deck versus investor workflow.** Two lessons advocate reserving the deck for a meeting. That tactic may work in relationship-heavy early-stage contexts but conflict with modern asynchronous screening. Treat it as a selectable strategy, not a universal instruction.
5. **Start with the low-end ask versus fully fund the plan.** A low announced target can create momentum, but it is dangerous if it cannot independently reach the milestone. The minimum must be financially sufficient, not cosmetically attractive.
6. **Near break-even versus venture-scale acceleration.** One lesson identifies near break-even as negotiating leverage; other venture cases focus on scaling and future rounds. Substitute the company's next financing-leverage milestone where break-even is inappropriate.
7. **Avoid a down round versus preserve the company.** Several sources strongly discourage down rounds, while the SurePayroll example shows that a down round can save a business. A survival or strategic reset can outweigh signaling and dilution costs.
8. **No/at least two strategics versus investor-specific diligence.** The strategic-investor rule highlights exit competition but is too categorical to replace rights-level analysis. Contractual access and conflict matter more than the count alone.

## Claims that need disclaimers or freshness checks

### Legal and securities

- SAFEs and convertible notes must not be treated as legally identical; notes involve debt terms while SAFEs generally do not.
- Board, observer, information, veto, strategic-investor, anti-dilution, option-pool, and change-of-control provisions require current counsel and jurisdiction-specific review.
- Public or private statements about fundraising momentum, commitments, oversubscription, or scarcity must be truthful and compliant with offering rules.
- Standard forms named in a source should be fetched fresh from their official publishers; their terms and market acceptance change.

### Financial, tax, and accounting

- Cap-table examples omit material variables and are educational only. Every output should display assumptions and reconcile to actual financing documents.
- LTV and CAC depend on definitions, attribution, cohort maturity, gross margin, churn, and time horizon. A ratio without those inputs is not decision-grade.
- Exit proceeds require a waterfall that includes preferences, participation, seniority, conversion, options, secondaries, fees, and taxes.
- Break-even, valuation, runway, and future financing are scenarios, not forecasts with certainty.

### Dated market claims

- Dollar thresholds for notes versus equity, typical discount rates, valuation caps, legal costs, accelerator terms, and prevalence of full-ratchet protection date mostly to 2018–2021.
- The 2017 exit-average reference and the 2021 "frothy" valuation context should not be reused as present benchmarks.
- Investor-discovery platforms, fund screening workflows, and expectations for asynchronous decks have changed.
- Statements that cold email rarely works, investors will have to take a meeting, or down rounds should be avoided at all costs are rhetorical generalizations, not facts.

### Recommended universal disclaimer behavior

Any skill that touches financing mechanics should: state that it is educational; request jurisdiction, stage, instrument form/version, and actual cap-table inputs; separate source heuristics from calculations; cite the relevant source lesson; identify freshness-sensitive assumptions; and advise review by qualified legal, tax, accounting, or financial professionals without pretending that the disclaimer cures a bad model.

## Proposed skill taxonomy

The package should be modular enough for a founder to call one focused capability, with a router that composes them into a fundraising workflow. Names below are platform-neutral slugs suitable for GPT or Claude skill directories.

### A. Strategy and routing

#### `fundraise-plan`

- Purpose: diagnose stage, target outcome, runway, readiness, and financing sequence; then produce a staged plan.
- Draws from: Raise for Outcomes, When to Raise Capital, Funding the Valley, Impact of Raising Too Much.
- Core outputs: milestone definition, monthly runway cases, amount range, timing, next-round dependency, risk register, and a list of professional-review flags.
- Guardrail: never recommend a dollar amount from a generic benchmark.

#### `financing-instrument-compare`

- Purpose: compare priced equity, convertible note, and SAFE structures for the actual situation.
- Draws from: Convertible Debt/SAFE vs. Equity, WAIT, Rule of Two, Friction Kills Deals, A Twist on Convertible Notes.
- Core outputs: criteria table, conversion-overhang scenarios, present/next-round tradeoffs, and unresolved legal terms.
- Guardrail: keep SAFE and note mechanics distinct and retrieve current form versions when available.

### B. Quantitative readiness

#### `cap-table-model`

- Purpose: calculate fully diluted ownership through priced rounds, pool top-ups, and conversions.
- Draws from: Valuations/Option Pools, Rule of Two, Impact of Raising Too Much.
- Core outputs: assumptions ledger, pre/post cap table, pool math, price per share, dilution bridge, and sensitivity table.
- Guardrail: refuse false precision when documents or inputs are missing.

#### `raise-size-scenarios`

- Purpose: compare minimum, target, and maximum capital plans against milestone probability, runway, dilution, and expected value.
- Draws from: Secret of the Ask, Funding the Valley, Impact of Raising Too Much, Raise for Outcomes.
- Core outputs: base/downside budget, buffer, milestones, financing contingency, and exit/next-round sensitivity.
- Guardrail: the announced minimum must independently fund a coherent plan.

#### `unit-economics-investor-brief`

- Purpose: convert CAC, LTV, retention, and channel history into a defensible forward-investment narrative.
- Draws from: CAC lesson and Pot of Gold.
- Core outputs: metric definitions, channel/cohort tables, trend commentary, forecast assumptions, and diligence questions.
- Guardrail: label immature cohorts and modeled LTV; do not present blended CAC alone.

### C. Investor discovery and process

#### `investor-fit-map`

- Purpose: research and rank investors by thesis, stage, check, portfolio adjacency/conflict, behavior, rights, and strategic effects.
- Draws from: Finding the Right Investor, Three Passes, Strategic Investors.
- Core outputs: scorecard, rationale, conflict flags, reference-check questions, and warm-introduction paths.
- Guardrail: strategic-investor count is a warning signal, not an automatic decision.

#### `investor-outreach-kit`

- Purpose: produce a one-page teaser, forwardable introduction, tailored outreach, and follow-up sequence.
- Draws from: Don't Send the Deck, Finding the Right Investor, Secret of the Ask.
- Core outputs: teaser outline, short email variants, meeting ask, materials policy, and versioning plan.
- Guardrail: adapt the deck policy to the investor's stated screening workflow.

#### `investor-crm-cadence`

- Purpose: establish pre-raise relationship-building, advice recaps, milestone tracking, and re-engagement.
- Draws from: Great Investor Meetings and Relationship Business.
- Core outputs: six-month cadence, CRM schema, recap email, evidence update, and next-action rules.
- Guardrail: never characterize advice as a commitment.

### D. Pitch and meeting execution

#### `venture-pitch-three-pass`

- Purpose: review a deck for essence, investor empathy, emotional intent, and evidence.
- Draws from: Three Passes, Pot of Gold, Secret of the Ask.
- Core outputs: top remembered claims, slide keep/move/delete table, investor-question map, future-path allocation, and rehearsal notes.
- Guardrail: emotional design cannot compensate for missing evidence or authorize misleading claims.

#### `investor-meeting-coach`

- Purpose: prepare and simulate an investor-led conversation rather than a rigid slide recital.
- Draws from: Finding the Right Investor, Great Investor Meetings, Three Passes.
- Core outputs: agenda, likely questions, concise answers, proof appendix map, objection log, and follow-up checklist.
- Guardrail: preserve direct answers and disclose material risks.

### E. Terms, governance, and ongoing relationship

#### `term-friction-materiality-check`

- Purpose: determine whether a proposed departure from a standard document is economically or strategically worth its cost.
- Draws from: Friction Kills Deals, A Twist on Convertible Notes, Strategic Investors.
- Core outputs: deviation inventory, scenario impact, control/exit implications, negotiation priority, and counsel questions.
- Guardrail: no legal conclusions; fetch and identify the governing current document version.

#### `strategic-investor-risk-review`

- Purpose: assess commercial upside against conflict, information, governance, financing, and exit-competition risk.
- Draws from: Strategic Investors and Relationship Business.
- Core outputs: rights matrix, acquirer map, scenario comparison, mitigation questions, and reference-check plan.
- Guardrail: route antitrust, fiduciary, confidentiality, and change-of-control questions to counsel.

#### `investor-update-bad-news`

- Purpose: draft accurate, timely investor updates for adverse developments and specific asks.
- Draws from: Relationship Business.
- Core outputs: facts/interpretation/unknowns, impact, response, owner, ask, and follow-up date.
- Guardrail: identify privileged, regulated, security-sensitive, customer, and personnel information before drafting.

### Suggested composition

A top-level `fundraising` router should ask for stage, jurisdiction, current cash/runway, target milestone, financing history/instruments, current cap table, and desired artifact. It can then route:

- Planning request → `fundraise-plan` + `raise-size-scenarios`
- Instrument request → `financing-instrument-compare` + `cap-table-model`
- Market process request → `investor-fit-map` + `investor-crm-cadence` + `investor-outreach-kit`
- Pitch request → `venture-pitch-three-pass` + `unit-economics-investor-brief` + `investor-meeting-coach`
- Term/governance request → `term-friction-materiality-check` + `strategic-investor-risk-review`
- Portfolio communication request → `investor-update-bad-news`

For portability, each skill should be self-contained Markdown with the same sections: purpose, when to use, required inputs, workflow, output contract, source-derived heuristics, freshness checks, cautions, and example invocation. Avoid platform-specific tool syntax in the core skill; add thin GPT and Claude adapters only where discovery or file conventions differ.

## Coverage ledger

1. 3 Passes on How to Make a Better Pitch
2. What are investors REALLY thinking about when they ask about your CAC…?
3. Think twice before committing to strategic investors
4. Raise for Outcomes, Not Headlines
5. Don’t Send the Deck
6. How to Get Great Investor Meetings
7. Friction Kills Deals
8. Our Business is a Relationship Business
9. Back to Basics: Valuations, Option Pools and What You Need to Know Before Raising Capital
10. WAIT – Now Troy Likes Convertible Notes?
11. A Twist on Convertible Notes
12. The Rule of Two
13. Convertible Debt/SAFE vs. Equity
14. Finding the Right Investor
15. The Secret of the Ask
16. Pot of Gold
17. Impact of Raising Too Much
18. When to Raise Capital
19. Funding the Valley

**Coverage result: 19 listed / 19 selected / 19 reviewed.**
