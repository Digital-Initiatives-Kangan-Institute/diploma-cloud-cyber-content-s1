#!/usr/bin/env python3
"""Build the AccentLoitte LMS Replacement board presentation (.pptx) — student model.

The completed board-presentation deck that accompanied the 2022 AccentLoitte Business
Case (GrayBoard -> DOODLE, on-prem). Student-facing example of a finished board deck;
pairs with the LMS Replacement Business Case PDF on the same project. In-world only.

Usage:  python scripts/build_lms_replacement_deck.py [output.pptx]
Default: ../diploma-cloud-cyber-website/public/documents/YAT-LMS-Replacement-Business-Case-Presentation.pptx
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pptx_brand as b  # noqa: E402


def build(path):
    prs = b.new_deck()

    b.add_title_slide(
        prs, "Business Case", "LMS Replacement — GrayBoard to DOODLE",
        ["AccentLoitte Consulting", "Presented to the YAT Board   ·   May 2022"])

    b.add_content_slide(prs, "Agenda", [
        ("Why now — strategic context", 0),
        ("The GrayBoard LMS today", 0),
        ("The gap", 0),
        ("Options considered", 0),
        ("Recommendation", 0),
        ("Cost summary", 0),
        ("Why DOODLE — the benefits", 0),
        ("Risks and mitigation", 0),
        ("Implementation plan", 0),
        ("The decision we're asking for", 0),
    ])

    b.add_content_slide(prs, "Strategic context & alignment", [
        ("GrayBoard, YAT's in-house LMS, has reached end of supportable life — it needs replacing, not patching.", 0),
        ("Across the RTO sector, institutions have moved off bespoke platforms to supported products.", 0),
        ("Accessibility (WCAG 2.1 AA / DDA) and reliability are now baseline expectations, not extras.", 0),
        ("Replacing GrayBoard serves YAT's goal of reliable, well-supported core systems.", 0),
    ])

    b.add_content_slide(prs, "The GrayBoard LMS today", [
        ("Bespoke, in-house — at end of supportable life.", 0),
        ("Availability and performance are degrading; it struggles at end-of-term assessment peaks.", 0),
        ("No vendor support and no product roadmap — maintenance rests on a few YAT staff.", 0),
        ("Not WCAG 2.1 AA compliant — a Disability Discrimination Act exposure.", 0),
        ("Holds YAT's complete student-record history — which must be preserved through any change.", 0),
    ])

    b.add_content_slide(prs, "The gap", [
        ("Supportability — no vendor support or roadmap.", 0),
        ("Reliability — availability below an acceptable baseline.", 0),
        ("Compliance — accessibility non-conformance.", 0),
        ("Performance — degrades under assessment-week load.", 0),
    ])

    b.add_content_slide(prs, "Options considered", [
        ("Option A — Remediate & retain GrayBoard: accessibility retrofit, hardware refresh, continued in-house maintenance.", 0),
        ("Option B — Replace with a contemporary on-prem LMS (DOODLE), selected via market evaluation.", 0),
        ("A SaaS / cloud LMS was considered but is out of scope for YAT's current on-premises operating model.", 0),
    ])

    b.add_statement_slide(
        prs, "Recommendation",
        "Replace GrayBoard with DOODLE, deployed on-premises.",
        "The only option that is supported, accessible, performant — and future-ready.")

    b.add_table_slide(prs, "Cost summary", ["", "Option A — Remediate", "Option B — Replace"],
                      [["One-off (Year 1)", "$55,000", "$160,000"],
                       ["Recurring (per year)", "$67,000", "$73,400"],
                       ["5-year direct cost", "$390,000", "$453,600"]],
                      col_widths=[4.3, 3.7, 3.7])

    b.add_content_slide(prs, "Why DOODLE — despite the higher cost", [
        ("Option B costs ~$63,600 more over five years — the case for it is not cost, but:", 0),
        ("Vendor support and an active product roadmap.", 1),
        ("WCAG 2.1 AA compliance — closes the DDA exposure.", 1),
        ("Meets the ≥ 99% availability baseline and holds performance at peak load.", 1),
        ("Reduces the concentration risk of bespoke in-house maintenance.", 1),
        ("Option A only defers an unavoidable replacement — and its cost rises as the platform decays.", 0),
    ])

    b.add_content_slide(prs, "Risks & mitigation", [
        ("Data loss in migration → verified ETL with record reconciliation, parallel running, tested backups.", 0),
        ("Cutover disrupts teaching → cutover in the December–January break, with a tested rollback.", 0),
        ("Low user adoption → role-based training before cutover, plus a stabilisation support period.", 0),
        ("Integration gaps (AD / O365 / AVETMISS) → integration testing during the parallel run.", 0),
    ])

    b.add_content_slide(prs, "Implementation plan", [
        ("Phase 1 — Selection & implementation plan  (2022 H1)", 0),
        ("Phase 2 — Deploy, migrate data, parallel run, cutover  (December 2022 – January 2023 break)", 0),
        ("Phase 3 — Stabilise, train, document, knowledge transfer, closure  (January 2023)", 0),
        ("Staff trained before cutover; cutover scheduled into the teaching break to minimise disruption.", 0),
    ])

    b.add_statement_slide(
        prs, "The decision we're asking for",
        "Approve the replacement, the implementation plan, and the Year-1 budget.",
        "Option B — DOODLE on-premises   ·   Year-1 ≈ $160,000")

    b.add_closing_slide(prs, "Questions", "AccentLoitte Consulting  ·  YAT Board, May 2022")

    Path(path).parent.mkdir(parents=True, exist_ok=True)
    prs.save(path)
    print(f"Wrote {path} ({len(prs.slides)} slides)")


if __name__ == "__main__":
    default = "../diploma-cloud-cyber-website/public/documents/YAT-LMS-Replacement-Business-Case-Presentation.pptx"
    out = sys.argv[1] if len(sys.argv) > 1 else default
    build(out)
