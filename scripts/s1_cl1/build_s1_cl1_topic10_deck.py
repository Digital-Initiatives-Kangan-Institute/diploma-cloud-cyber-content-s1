#!/usr/bin/env python3
"""Topic 10 (Evidencing & documenting) — Kangan-branded teaching deck. Final AT2 content Topic.

Turns the Topic 6-9 build into the AT2 deliverable, the Deployment Report. Four components:
C1 evidence into Appendices A/B/C; C2 writing the report (§1-§7); C3 contextual knowledge
evidence; C4 reflection + feedback. ALL BESPOKE, teach -> practice (AWS decks teach services,
not report-writing/KE/reflection to a VET standard) — no AWS slides, no demos, no image
placeholders. Reference: the Deployment Report template (§1-§7 + Appendices A/B/C). Continuity:
§5 <- Topic 9 justifications; §6 <- Topic 9 validation; Appendices <- evidence since Topic 6.
Layouts in kangan_deck.py.

Usage:  python scripts/build_kangan_topic10_deck.py [output.pptx]
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # content-repo scripts/ (brand + registry)  # noqa: E402
sys.path.insert(0, str(next(d / "scripts" for d in Path(__file__).resolve().parents if (d / "scripts" / "helpers" / "__init__.py").exists())))  # umbrella scripts/ (engine)  # noqa: E402
from helpers.kangan_deck import *  # noqa: F401,F403

OUT_DEFAULT = "S1-CL1-Cloud-Design-Build/delivery/topic_10/Topic_10_Slides.pptx"

A1, A2, A3 = MAGENTA, SKY, GREEN


def build(path):
    prs = new_deck()
    n = [0]
    def pg(): n[0] += 1; return n[0]

    title_slide(prs, "10", "Evidencing & documenting",
                "Turn everything you've built into the Deployment Report")

    content_slide(prs, pg(), "The build becomes the deliverable", "no new building — write it up", [
        (0, "Topics 6–9 built, monitored, validated and justified the workload — capturing evidence the whole way."),
        (0, "Topic 10 assembles that into the Deployment Report — the single AT2 deliverable.",
            {"bold": True, "color": A1, "mark_color": A1}),
        (0, "Four moves: organise the evidence, write the report, evidence your knowledge in context, and reflect."),
        (0, "No new resources — everything you need was captured as you built."),
    ])

    # ===== C1 — Evidence into the appendices =====
    divider_slide(prs, "01", "Evidence into the appendices", "make it traceable", A1)
    content_slide(prs, pg(), "What makes evidence count", "traceable, or it proves nothing", [
        (0, "Good evidence is named, dated, and shows the Region and identity it was taken under."),
        (0, "It's organised and referenceable — so a reader can find the exact item the narrative cites.",
            {"bold": True, "color": A1, "mark_color": A1}),
        (0, "A screenshot nobody can place, or an export with no label, proves nothing."),
    ], accent=A1)
    content_slide(prs, pg(), "Appendices A / B / C", "where the evidence lives", [
        (0, "Appendix A — build evidence: the named screenshots taken as you built each tier."),
        (0, "Appendix B — configuration exports: the settings of what you built (e.g. security-group rules, RDS config)."),
        (0, "Appendix C — test and validation evidence: connectivity, scaling and recovery-objective results."),
        (0, "Label and number every item so §4–§6 can cross-reference it.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], accent=A1)
    content_slide(prs, pg(), "Organise what you captured", "since Topic 6", [
        (0, "Gather every screenshot, export and test result you captured across the build."),
        (0, "Sort them into A / B / C; give each a clear label and number."),
        (0, "Note any gaps — and recapture while the lab is still standing.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], accent=A1)
    activity_slide(prs, pg(), "Build your appendices", [
        (0, "Assemble Appendices A, B and C from the evidence you captured since Topic 6:", {"bold": True}),
        (1, "sort into screenshots / config exports / test evidence"),
        (1, "label and number each item"),
        (0, "Flag any gaps and recapture them now.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], "~20 min", accent=A1)
    takeaways_slide(prs, pg(), "Section 1 · Evidence", [
        "Evidence must be traceable — named, dated, Region/identity visible.",
        "Appendix A = screenshots, B = config exports, C = test evidence.",
        "Label and number every item so the narrative can cite it.",
        "Capture as you build; organise here; recapture any gaps now.",
    ], accent=A1)

    # ===== C2 — Writing the Deployment Report =====
    divider_slide(prs, "02", "Writing the Deployment Report", "§1–§7", A2)
    content_slide(prs, pg(), "Technical documentation — who reads it", "write for the reader", [
        (0, "The Deployment Report is written for the people who will run and audit the system — YAT ICT and auditors."),
        (0, "Clear, factual, traceable — every claim backed by an appendix reference.",
            {"bold": True, "color": A2, "mark_color": A2}),
        (0, "It's a record of what was built and why — not a diary of your day."),
    ], accent=A2)
    content_slide(prs, pg(), "The report structure", "the template", [
        (0, "§1 Executive Summary · §2 Engagement Context · §3 Scope of Deployment."),
        (0, "§4 Build / Change Narrative · §5 Configuration Decisions · §6 Testing, Simulation & Validation."),
        (0, "§7 Operational Handover."),
        (0, "Appendices A (screenshots) · B (config exports) · C (test evidence) — referenced throughout.",
            {"bold": True, "color": A2, "mark_color": A2}),
    ], accent=A2)
    content_slide(prs, pg(), "The Build / Change Narrative (§4)", "what you built, tier by tier", [
        (0, "Walk the build in order: foundation → network → compute → elasticity → database → storage → monitoring."),
        (0, "For each, state what you built and what changed from the baseline design."),
        (0, "Cross-reference the Appendix A screenshots and Appendix B exports that prove it.",
            {"bold": True, "color": A2, "mark_color": A2}),
        (0, "Factual and specific — not “I set up the server”, but what, where, and with which settings."),
    ], accent=A2)
    content_slide(prs, pg(), "§5 Configuration Decisions & §6 Testing", "your Topic 9 work lands here", [
        (0, "§5 Configuration Decisions = your Topic 9 C1–C8 justifications — drop in the rationales you wrote."),
        (0, "§6 Testing/Validation = your Topic 9 validation results, each referencing Appendix C.",
            {"bold": True, "color": A2, "mark_color": A2}),
        (0, "This is where the marked judgement (justify) and the evidence of a working build come together."),
    ], accent=A2)
    content_slide(prs, pg(), "§1–§3 and §7", "frame it and hand it over", [
        (0, "§2 Context + §3 Scope — what the engagement was, why, and what's in / out of this build."),
        (0, "§7 Operational Handover — what YAT ICT now owns and how to run it (alarms, backups, access)."),
        (0, "§1 Executive Summary — write it last; a short, plain summary for a busy reader.",
            {"bold": True, "color": A2, "mark_color": A2}),
    ], accent=A2)
    activity_slide(prs, pg(), "Draft the Deployment Report", [
        (0, "Write the report to the template for the practice engagement:", {"bold": True}),
        (1, "§4 narrative cross-referencing your appendices; §5 from your justifications; §6 from your validation"),
        (1, "§2/§3 context + scope; §7 handover; §1 summary last"),
        (0, "Every claim ties back to a labelled appendix item.",
            {"bold": True, "color": A2, "mark_color": A2}),
    ], "~40 min", accent=A2)
    takeaways_slide(prs, pg(), "Section 2 · The report", [
        "Write for the people who run and audit the system; factual and traceable.",
        "Follow the template — §1–§7 + Appendices A/B/C.",
        "§5 carries your justifications; §6 your validation; §4 cross-references the evidence.",
        "Write the Executive Summary last.",
    ], accent=A2)

    # ===== C3 — Contextual knowledge evidence =====
    divider_slide(prs, "03", "Knowledge in context", "evidence what you know", A3)
    content_slide(prs, pg(), "Evidence what you know — in context", "grounded, not abstract", [
        (0, "Some knowledge isn't shown just by building — shared responsibility, managed vs self-hosted, storage/scaling/database options, cost models."),
        (0, "Answer the knowledge questions grounded in your build: cite your actual design and decisions.",
            {"bold": True, "color": A3, "mark_color": A3}),
        (0, "“Why a managed database here?” → because of the Ledgerline workload and these trade-offs — not a textbook definition."),
    ], accent=A3)
    activity_slide(prs, pg(), "Answer the knowledge questions in context", [
        (0, "Answer the AT2 knowledge questions for the practice engagement:", {"bold": True}),
        (1, "reference your own build, decisions and the Ledgerline workload"),
        (1, "shared responsibility · managed vs self-hosted · storage/scaling/db options · cost models"),
        (0, "Specific to your system — not generic best practice.",
            {"bold": True, "color": A3, "mark_color": A3}),
    ], "~20 min", accent=A3)

    # ===== C4 — Reflection & feedback =====
    divider_slide(prs, "04", "Reflection & feedback", "close the loop", A1)
    content_slide(prs, pg(), "Reflect, and respond to feedback", "honest review, then improve", [
        (0, "A reflection is an honest review — what worked, what you'd do differently, what you learned — not a summary of what you did."),
        (0, "Then seek feedback on your report from the required personnel, and respond to it.",
            {"bold": True, "color": A1, "mark_color": A1}),
        (0, "Acting on feedback is part of the job — and it's assessed."),
    ], accent=A1)
    activity_slide(prs, pg(), "Reflect & seek feedback", [
        (0, "Close out the engagement:", {"bold": True}),
        (1, "write a short, honest reflection on the build and the process"),
        (1, "seek feedback on your report, and note what you changed in response"),
    ], "~15 min", accent=A1)

    # ===== Close =====
    takeaways_slide(prs, pg(), "Topic 10 · Key takeaways", [
        "Evidence is traceable and lives in Appendices A / B / C.",
        "Write to the template, cross-referencing the evidence throughout.",
        "§5 carries your C1–C8 justifications; §6 your validation results.",
        "Evidence your knowledge in the context of your build; reflect and respond to feedback.",
        "The Deployment Report is the AT2 deliverable — this is where it all comes together.",
    ], accent=GOLD)
    close_slide(prs, "AT2 complete",
                ["You can now build a cloud workload to a supplied design, evidence it, justify it, and document it.",
                 "Next: the AT2 assessment build — then AT3, where the baseline becomes highly available."], accent=GOLD)

    save(prs, path)


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else OUT_DEFAULT
    build(out)
