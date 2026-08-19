#!/usr/bin/env python3
"""Build the curated source-to-skill coverage manifest."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

# Values are ordered: primary skill first, then supporting skills.
ASSIGNMENTS: dict[str, list[str]] = {
    "tech-scenes-unplugged-with-troy-henikoff-managing-director-of-math-venture-partners": ["math-review-founder-operations"],
    "3-passes-on-how-to-make-a-better-pitch": ["math-build-investor-pitch"],
    "angel-investing-101": ["math-founder-stack"],
    "math-101-table-of-contents": ["math-founder-stack"],
    "nailing-cold-investor-outreach": ["math-run-investor-process"],
    "what-are-investors-really-thinking-about-when-they-ask-about-your-cac": ["math-diagnose-metrics", "math-build-investor-pitch", "math-plan-fundraise"],
    "channel-partnerships-part-ii-engaging-and-closing-partners": ["math-build-channel-partnerships"],
    "think-twice-before-committing-to-strategic-investors": ["math-plan-fundraise", "math-run-investor-process"],
    "channel-partnerships-part-i-building-an-ideal-profile-and-selecting-the-best": ["math-build-channel-partnerships"],
    "the-easiest-way-to-impress-your-future-investors-the-early-stage-data-room": ["math-run-investor-process"],
    "dont-trust-google-for-your-customer-retention-metrics": ["math-diagnose-metrics"],
    "the-most-effective-way-to-do-investor-updates": ["math-write-investor-update"],
    "stop-selling-yourself-short-your-market-size-is-bigger-than-you-think": ["math-validate-startup", "math-build-investor-pitch"],
    "math-101-how-defining-purpose-yields-results": ["math-founder-office-hours", "math-review-founder-operations"],
    "secrets-to-a-speedy-and-successful-fundraise": ["math-run-investor-process"],
    "math-101-raise-for-outcomes-not-headlines": ["math-plan-fundraise"],
    "chicago-capital-podcast-troy-henikoff-on-ted-lasso-vc-and-building-a-winning-team": ["math-founder-stack"],
    "higher-valuations-are-not-always-better": ["math-plan-fundraise"],
    "math-101-dont-send-the-deck": ["math-run-investor-process", "math-build-investor-pitch"],
    "math-101-how-to-learn-from-churn": ["math-diagnose-metrics"],
    "math-101-the-right-kpis-matter": ["math-diagnose-metrics"],
    "levers-the-framework-for-building-repeatability-into-your-business": ["math-design-growth-experiments", "math-review-founder-operations", "math-diagnose-metrics"],
    "math-101-how-to-get-great-investor-meetings": ["math-run-investor-process"],
    "math-101-friction-kills-deals": ["math-plan-fundraise", "math-run-investor-process"],
    "how-to-get-better-introductions": ["math-run-investor-process", "math-review-founder-operations"],
    "entrepreneurship-fundraising-and-practical-advice-for-startup-founders": ["math-founder-stack"],
    "math-101-reading-between-the-lines": ["math-review-founder-operations"],
    "math-101-our-business-is-a-relationship-business": ["math-write-investor-update", "math-run-investor-process"],
    "math-101-paying-for-services-with-equity": ["math-structure-founder-equity"],
    "math-101-3-things-you-need-to-have-a-successful-business": ["math-founder-office-hours", "math-design-growth-experiments", "math-review-founder-operations"],
    "the-inevitable-economics-of-trust": ["math-review-founder-operations"],
    "math-101-how-to-make-your-annual-budget-twice-as-valuable": ["math-model-startup", "math-review-founder-operations"],
    "math-101-how-to-find-the-right-job-at-the-right-start-up": ["math-review-founder-operations"],
    "math-101-pain-killer-vs-vitamin": ["math-validate-startup"],
    "math-101-do-you-know-the-difference-between-gross-profit-and-contribution-margin": ["math-diagnose-metrics", "math-model-startup"],
    "math-101-the-entrepreneurs-wheel-of-fortune": ["math-founder-office-hours", "math-review-founder-operations"],
    "math-101-back-to-basics-valuations-option-pools-and-what-you-need-to-know-before-raising-capital": ["math-structure-founder-equity", "math-plan-fundraise"],
    "math-101-communicating-to-your-investors-its-more-important-than-you-think": ["math-write-investor-update"],
    "math-101-the-equity-conversation": ["math-structure-founder-equity", "math-review-founder-operations"],
    "math-101-financial-modeling-part-5-modeling-financial-growth": ["math-model-startup", "math-design-growth-experiments"],
    "math-101-financial-modeling-part-4-how-fundraising-and-dilution-impacts-your-equity-as-a-founder": ["math-model-startup", "math-structure-founder-equity", "math-plan-fundraise"],
    "math-101-financial-modeling-part-3-modeling-your-expenses": ["math-model-startup"],
    "math-101-decoding-the-revenue-puzzle": ["math-model-startup", "math-diagnose-metrics"],
    "math-101-financial-modeling-part-2-the-power-of-a-financial-model": ["math-model-startup"],
    "math-101-financial-modeling-part-1-what-is-a-financial-model": ["math-model-startup"],
    "math-101-your-baby-is-ugly": ["math-validate-startup"],
    "not-all-revenue-is-created-equal": ["math-diagnose-metrics", "math-validate-startup", "math-review-founder-operations"],
    "math-101-founder-vesting-rsus-and-83b-elections-making-sense-of-the-mess": ["math-structure-founder-equity"],
    "math-101-founders-allocating-equity-and-avoiding-the-big-mistake": ["math-structure-founder-equity"],
    "math-101-how-to-answer-the-question-what-is-your-cac": ["math-diagnose-metrics"],
    "tech-scenes-chicago-with-troy-henikoff": ["math-founder-stack"],
    "setting-the-record-straight": ["math-review-founder-operations"],
    "math-101-why-is-troy-obsessed-with-cac": ["math-diagnose-metrics"],
    "math-101-what-makes-a-truly-great-entrepreneur": ["math-founder-office-hours", "math-review-founder-operations"],
    "math-101-how-to-optimize-use-of-capital": ["math-design-growth-experiments", "math-model-startup"],
    "math-101-wait-now-troy-likes-convertible-notes": ["math-plan-fundraise"],
    "math-101-mistakes-entrepreneurs-make-setting-prices": ["math-design-growth-experiments", "math-validate-startup"],
    "math-101-a-twist-on-convertible-notes": ["math-plan-fundraise"],
    "math-101-the-rule-of-two": ["math-plan-fundraise"],
    "math-101-convertible-debtsafe-vs-equity": ["math-plan-fundraise"],
    "math-101-finding-the-right-investor": ["math-run-investor-process"],
    "secret-of-the-ask": ["math-build-investor-pitch"],
    "math-101-pot-of-gold": ["math-build-investor-pitch"],
    "impact-of-raising-too-much": ["math-plan-fundraise"],
    "math-101-when-to-raise-capital": ["math-plan-fundraise"],
    "funding-the-valley": ["math-plan-fundraise"],
    "bootstrapping-in-america-with-troy-henikoff": ["math-founder-stack"],
    "which-chicagoans-are-best-at-mentoring-women": ["math-review-founder-operations", "math-founder-office-hours", "math-run-investor-process"],
    "the-new-york-times-test": ["math-review-founder-operations", "math-founder-office-hours"],
    "the-distance-podcast-troy-henikoff": ["math-founder-stack"],
    "qa-with-troy-henikoff-are-entrepreneurs-born-or-made": ["math-founder-office-hours", "math-review-founder-operations"],
    "startup-financial-modeling-part-4-the-balance-sheet-cash-flow-and-unit-economics": ["math-model-startup", "math-diagnose-metrics"],
    "startup-financial-modeling-part-3-the-income-statement-and-custom-detail-tabs": ["math-model-startup"],
    "startup-financial-modeling-part-2-start-with-your-assumptions": ["math-model-startup"],
    "startup-financial-modeling-part-1-what-is-a-financial-model": ["math-model-startup"],
    "startup-stories-nothing-matters-more-than-your-customers": ["math-founder-stack"],
    "techstars-conversation-with-troy-henikoff": ["math-founder-stack"],
    "troy-henikoff-interview-on-growth-hacker": ["math-founder-stack"],
    "troy-henikoff-makes-list-of-top-50-chicagoans-in-tech": ["math-founder-stack"],
    "q-what-are-some-common-questions-asked-by-vcs-during-a-first-pitch-meeting": ["math-build-investor-pitch", "math-run-investor-process", "math-validate-startup"],
}

STATUS = {
    "tech-scenes-unplugged-with-troy-henikoff-managing-director-of-math-venture-partners": "synopsis_only",
    "angel-investing-101": "description_only",
    "math-101-table-of-contents": "index_only",
    "chicago-capital-podcast-troy-henikoff-on-ted-lasso-vc-and-building-a-winning-team": "stub",
    "entrepreneurship-fundraising-and-practical-advice-for-startup-founders": "stub",
    "tech-scenes-chicago-with-troy-henikoff": "stub",
    "bootstrapping-in-america-with-troy-henikoff": "stub",
    "the-distance-podcast-troy-henikoff": "stub",
    "startup-stories-nothing-matters-more-than-your-customers": "stub",
    "techstars-conversation-with-troy-henikoff": "stub",
    "troy-henikoff-interview-on-growth-hacker": "stub",
    "troy-henikoff-makes-list-of-top-50-chicagoans-in-tech": "non_instructional",
}


def main() -> int:
    catalog = json.loads((ROOT / "sources/catalog.json").read_text(encoding="utf-8"))
    items = catalog["items"]
    catalog_slugs = {item["slug"] for item in items}
    if catalog_slugs != set(ASSIGNMENTS):
        missing = sorted(catalog_slugs - set(ASSIGNMENTS))
        extra = sorted(set(ASSIGNMENTS) - catalog_slugs)
        raise SystemExit(f"coverage mismatch; missing={missing}, extra={extra}")

    review_file = {
        "Being A Better Entrepreneur": "research/being-a-better-entrepreneur.md",
        "Fundraising": "research/fundraising.md",
        None: "research/extended-library.md",
    }
    output = {
        "source": catalog["source"],
        "reviewed_on": "2026-08-19",
        "total_items": len(items),
        "items": [
            {
                "slug": item["slug"],
                "evidence_status": STATUS.get(item["slug"], "substantive"),
                "primary_skill": ASSIGNMENTS[item["slug"]][0],
                "supporting_skills": ASSIGNMENTS[item["slug"]][1:],
                "review": review_file[item.get("track")],
            }
            for item in items
        ],
    }
    path = ROOT / "sources/coverage.json"
    path.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(output['items'])} mappings to {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
