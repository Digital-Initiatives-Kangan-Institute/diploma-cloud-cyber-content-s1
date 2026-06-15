#!/usr/bin/env python3
"""Topic 14 (Closure & documentation) — Kangan-branded teaching deck. FINAL AT3 content Topic.

Produce the HA Deployment Report and close the engagement. Three components: C1 write the HA
Deployment Report (from the Topic 13 evidence + simulation findings, to the AT3 template); C2
contextual knowledge evidence (report S8, grounded in the HA work); C3 close the engagement —
feedback, sign-off, reflection (ICTCLD502 element 5.2-5.3).

ALL BESPOKE, teach -> practice (report-writing / KE / closure to a VET standard — AWS doesn't teach
it); the one reused source is 502 Topic 4 S11-S12 (feedback + sign-off). No demos, no image
placeholders. Closes AT3 and the course's advise -> build -> harden arc. Layouts in kangan_deck.py.

Usage:  python scripts/build_kangan_topic14_deck.py [output.pptx]
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kangan_deck import *  # noqa: F401,F403

OUT_DEFAULT = "S1-CL1-Cloud-Design-Build/delivery/topic_14/Topic_14_Slides.pptx"

A1, A2, A3 = MAGENTA, SKY, GREEN


def build(path):
    prs = new_deck()
    n = [0]
    def pg(): n[0] += 1; return n[0]

    title_slide(prs, "14", "Closure & documentation",
                "Write the HA report, evidence what you know, and close the engagement")

    content_slide(prs, pg(), "Close it out", "the final step", [
        (0, "Topic 13 implemented the HA design and proved it under simulated failure."),
        (0, "Topic 14 turns that into the HA Deployment Report, evidences your knowledge, and closes the engagement.",
            {"bold": True, "color": A1, "mark_color": A1}),
        (0, "Three moves: write the report (the simulation findings are its heart), evidence knowledge in context, and close out with feedback + sign-off."),
        (0, "This is the end of AT3 — and of the journey from advising to building to hardening."),
    ])

    # ===== C1 — Write the HA Deployment Report =====
    divider_slide(prs, "01", "Write the HA Deployment Report", "from evidence to deliverable", A1)
    content_slide(prs, pg(), "Evidence into the appendices", "the same discipline as AT2", [
        (0, "Organise everything you captured into the appendices: A — build screenshots; B — configuration exports; C — test & simulation evidence."),
        (0, "Label and number each item so the narrative can cite it.",
            {"bold": True, "color": A1, "mark_color": A1}),
        (0, "Traceable evidence is what turns a claim into proof."),
    ], accent=A1)
    content_slide(prs, pg(), "The HA report structure", "the template", [
        (0, "§1 Executive Summary · §2 Engagement Context · §3 Scope (the maintenance window)."),
        (0, "§4 Build/Change Narrative (the HA changes from the baseline) · §5 Configuration Decisions · §6 Testing, Simulation & Validation."),
        (0, "§7 Operational Handover · §8 Knowledge Evidence."),
        (0, "Appendices A–D — A screenshots · B config exports · C test/simulation evidence · D reflections.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], accent=A1)
    content_slide(prs, pg(), "The heart — §6 simulation findings", "your Topic 13 work", [
        (0, "§6 is where you prove fault tolerance: the failure simulation, the resize simulation, and the availability you measured."),
        (0, "Compare the findings to the design's recovery objectives, and record any adjustments you made.",
            {"bold": True, "color": A1, "mark_color": A1}),
        (0, "This section is what AT3 is marked on — the evidence the HA design actually works."),
    ], accent=A1)
    content_slide(prs, pg(), "§4 narrative · §5 decisions · §7 handover", "the rest of the report", [
        (0, "§4 — the HA changes from the baseline (cross-AZ network, cross-AZ ASG + ALB, Multi-AZ database), cross-referencing the appendices."),
        (0, "§5 — the HA configuration decisions, justified."),
        (0, "§7 — operational handover: what YAT ICT now runs (the HA-tuned alarms, the failover behaviour, what to watch)."),
        (0, "§1 Executive Summary — write it last.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], accent=A1)
    activity_slide(prs, pg(), "Draft the HA Deployment Report", [
        (0, "Write the report to the template for the practice engagement:", {"bold": True}),
        (1, "§4 the HA changes; §5 the decisions; §6 your simulation findings (the centrepiece)"),
        (1, "cross-reference Appendices A/B/C; §7 the handover"),
        (0, "Every claim ties back to a labelled appendix item.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], "~40 min", accent=A1)
    takeaways_slide(prs, pg(), "Section 1 · The report", [
        "Organise evidence into Appendices A/B/C; label and cross-reference.",
        "Follow the template — §1–§8 + Appendices A–D.",
        "§6 simulation findings is the heart — the proof of fault tolerance.",
        "Write the Executive Summary last.",
    ], accent=A1)

    # ===== C2 — Contextual knowledge evidence =====
    divider_slide(prs, "02", "Knowledge in context", "evidence what you know", A2)
    content_slide(prs, pg(), "Evidence what you know (§8)", "grounded, not abstract", [
        (0, "Answer the knowledge questions about high availability — fault tolerance, recovery objectives, redundancy, the trade-offs."),
        (0, "Ground every answer in your own HA work: cite your design and your simulation findings.",
            {"bold": True, "color": A2, "mark_color": A2}),
        (0, "“Why Multi-AZ for the database?” → because of this workload and what my failover simulation showed — not a textbook definition."),
    ], accent=A2)
    activity_slide(prs, pg(), "Answer the knowledge questions in context", [
        (0, "Complete §8 for the practice engagement:", {"bold": True}),
        (1, "reference your HA design, your decisions, and your simulation results"),
        (1, "availability · fault tolerance · recovery objectives · redundancy mechanisms"),
        (0, "Specific to your system — not generic best practice.",
            {"bold": True, "color": A2, "mark_color": A2}),
    ], "~20 min", accent=A2)

    # ===== C3 — Close the engagement =====
    divider_slide(prs, "03", "Close the engagement", "feedback · sign-off · reflection", A3)
    content_slide(prs, pg(), "Feedback & sign-off", "ICTCLD502 · Implement & finalise", [
        (0, "At completion, collect unbiased feedback to confirm the design meets requirements — surveys, one-on-one interviews, focus groups."),
        (0, "Confirm, seek and respond to feedback from the required personnel."),
        (0, "Then obtain final sign-off from the project sponsor (or delegated authority) — generally the last step in closing a project.",
            {"bold": True, "color": A3, "mark_color": A3}),
    ], accent=A3)
    content_slide(prs, pg(), "Reflect", "Appendix D", [
        (0, "Write an honest reflection on the HA engagement — what worked, what you'd do differently, what you learned."),
        (0, "A reflection is a review, not a summary of what you did.",
            {"bold": True, "color": A3, "mark_color": A3}),
        (0, "It's how you improve the next engagement — and it's assessed."),
    ], accent=A3)
    activity_slide(prs, pg(), "Close out — feedback, sign-off & reflection", [
        (0, "Finalise the engagement:", {"bold": True}),
        (1, "seek feedback on your report and record your response (§7.5)"),
        (1, "obtain and record final sign-off (§7.6)"),
        (1, "write your reflection (Appendix D)"),
    ], "~20 min", accent=A3)
    takeaways_slide(prs, pg(), "Section 3 · Close", [
        "Collect unbiased feedback; confirm, seek and respond to it.",
        "Obtain final sign-off — the last step in closing the project.",
        "Reflect honestly — what worked, what you'd change.",
        "The engagement is now formally complete.",
    ], accent=A3)

    # ===== Close =====
    takeaways_slide(prs, pg(), "Topic 14 · Key takeaways", [
        "The HA Deployment Report is the deliverable — write it to the template.",
        "§6 simulation findings is the heart: the proof of fault tolerance.",
        "Evidence your knowledge in the context of your own HA work.",
        "Close with feedback, final sign-off, and an honest reflection.",
        "AT3 — and the build journey — is complete.",
    ], accent=GOLD)
    close_slide(prs, "AT3 complete",
                ["You advised the client (AT1), built the solution (AT2), and made it highly available (AT3) — designed, implemented, proven, documented, and signed off.",
                 "The cluster's teaching arc is done."], accent=GOLD)

    save(prs, path)


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else OUT_DEFAULT
    build(out)
