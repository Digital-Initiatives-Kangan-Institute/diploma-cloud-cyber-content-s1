#!/usr/bin/env python3
"""Topic 4 (The decision & the plan) — Kangan-branded teaching deck. All bespoke (BC §9–§11).

Content only; brand + layouts live in kangan_deck.py.
Usage:  python scripts/build_kangan_topic4_deck.py [output.pptx]
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kangan_deck import *  # noqa: F401,F403  (brand palette + layouts)

OUT_DEFAULT = "S1-CL1-Cloud-Design-Build/delivery/topic_04/Topic_04_Slides.pptx"

A1, A2, A3 = MAGENTA, SKY, GREEN   # section accents (match Topics 2–3)


def build(path):
    prs = new_deck()
    n = [0]
    def pg(): n[0] += 1; return n[0]

    # Title
    title_slide(prs, "04", "The decision & the plan",
                "From evidence to a recommendation a board can approve")

    # Opener
    content_slide(prs, pg(), "From evidence to decision and plan", "now you make the call", [
        (0, "You've built the evidence (Topic 3). Now you do what a consultant is paid for: make the call."),
        (0, "Three moves: prioritise → recommend → plan it, then ask for the decision.",
            {"bold": True, "color": A1, "mark_color": A1}),
        (0, "These are the last sections of the business case — after this, the written case is complete."),
        (0, "A board approves a clear recommendation, a credible plan, and a specific ask. Give them all three."),
    ])

    # ===== C1 — Recommendation =====
    divider_slide(prs, "01", "Recommendation", "from analysis to advice", A1)
    content_slide(prs, pg(), "From analysis to advice", "", [
        (0, "Evaluation tells you what the options are worth; a recommendation says what to do."),
        (0, "This is the turn from analyst to advisor — you stop weighing and start advising."),
        (0, "The board wants a clear call, backed by the evidence you've already built.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], accent=A1)
    content_slide(prs, pg(), "Prioritise first", "", [
        (0, "Before recommending, rank the proposed changes (from your gap analysis): what matters most, what's urgent, what can wait."),
        (0, "A simple lens: impact (against the objectives) versus effort / urgency."),
        (0, "Prioritisation makes the plan sequenceable — and shows you're not boiling the ocean.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], accent=A1)
    content_slide(prs, pg(), "Make the call", "", [
        (0, "State the recommended option plainly — no hedging."),
        (0, "Justify it straight from the evidence:"),
        (1, "the CBA result (cost over the horizon)"),
        (1, "the risk / impact comparison"),
        (1, "alignment with the strategic objectives"),
        (0, "Name the trade-off you're accepting — a recommendation with no downside isn't trusted.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], accent=A1)
    content_slide(prs, pg(), "What a strong recommendation looks like", "", [
        (0, "Decisive — one clear recommended option."),
        (0, "Evidence-linked — every reason traces to your CBA / risk / strategy work."),
        (0, "Honest — names the trade-off and why it's acceptable."),
        (0, "Actionable — leads naturally into the plan.", {"bold": True, "color": A1, "mark_color": A1}),
    ], accent=A1)
    activity_slide(prs, pg(), "Write the Recommendation", [
        (0, "In your working copy of the Business Case, add the Recommendation section for the Accounting System (Ledgerline).", {"bold": True}),
        (0, "Remember to:"),
        (1, "Prioritise your proposed changes (from your gap analysis)."),
        (1, "State the recommended option plainly."),
        (1, "Justify it from your CBA + risk + strategic alignment — cite your own earlier sections."),
        (1, "Name the trade-off you're accepting."),
        (0, "~½ page."),
        (0, "⚠  Recommend, don't re-argue — point at the evidence you already built.", {"color": A1, "mark_color": A1}),
    ], "~20 min, then we discuss", accent=A1)
    takeaways_slide(prs, pg(), "Section 1 · Recommendation", [
        "Prioritise the changes, then recommend — impact vs effort/urgency.",
        "One clear option; justify it straight from the evidence; name the trade-off.",
        "The recommendation is the hinge between the evidence and the plan.",
    ], accent=A1)

    # ===== C2 — Action plan =====
    divider_slide(prs, "02", "Action plan", "how and when", A2)
    content_slide(prs, pg(), "What the action plan is for", "", [
        (0, "A recommendation says what and why; the action plan says how and when."),
        (0, "It turns a “yes” into execution the organisation can actually run."),
        (0, "And it proves the recommendation is feasible.", {"bold": True, "color": A2, "mark_color": A2}),
    ], accent=A2)
    content_slide(prs, pg(), "The parts of an action plan", "five parts (becomes the Action Plan section)", [
        (0, "Prioritised changes — what gets done, in priority order", {"marker": "1.  "}),
        (0, "Implementation schedule — phases / sequence / timeframe", {"marker": "2.  "}),
        (0, "Standards, targets & success metrics — how you'll know it worked", {"marker": "3.  "}),
        (0, "Implementation methods — how each change is delivered", {"marker": "4.  "}),
        (0, "Alignment with the change-management procedure — routing through governance", {"marker": "5.  "}),
    ], accent=A2)
    content_slide(prs, pg(), "Sequencing & the schedule", "", [
        (0, "Order the work by priority and dependency (you can't migrate data before the target exists)."),
        (0, "Group into phases with a realistic timeframe."),
        (0, "Board-level — phases and milestones, not a day-by-day Gantt. Show the critical path.",
            {"bold": True, "color": A2, "mark_color": A2}),
    ], accent=A2)
    content_slide(prs, pg(), "Standards, targets & success metrics", "", [
        (0, "Hold the work to the industry standards (Well-Architected, ISO 27017, Essential Eight, ITIL)."),
        (0, "Set measurable targets: availability, recovery, cutover with no data loss, budget adherence."),
        (0, "Targets make the plan accountable — they define “done well”.",
            {"bold": True, "color": A2, "mark_color": A2}),
    ], accent=A2)
    content_slide(prs, pg(), "Align to the change-management procedure", "", [
        (0, "Real change runs through governance."),
        (0, "Map the high-risk steps (e.g. cutover) to the change-management procedure:"),
        (1, "change request → risk assessment → approval → change window"),
        (0, "This is what separates a consultant's plan from a wish-list.",
            {"bold": True, "color": A2, "mark_color": A2}),
    ], accent=A2)
    activity_slide(prs, pg(), "Build the Action Plan", [
        (0, "In your working copy of the Business Case, add the Action Plan for the Accounting System.", {"bold": True}),
        (0, "Include all five parts:"),
        (1, "prioritised changes · implementation schedule (phases)"),
        (1, "standards, targets & success metrics · implementation methods"),
        (1, "alignment with the change-management procedure"),
        (0, "~1 page."),
        (0, "⚠  Board-level — phases, milestones and metrics, not a day-by-day task list.", {"color": A2, "mark_color": A2}),
    ], "~30 min, then we compare", accent=A2)
    takeaways_slide(prs, pg(), "Section 2 · Action plan", [
        "The plan turns the recommendation into executable phases.",
        "Five parts: prioritised changes · schedule · standards/targets/metrics · methods · change-mgmt alignment.",
        "Board-level detail; route high-risk steps through governance; make it measurable.",
    ], accent=A2)

    # ===== C3 — The decision requested =====
    divider_slide(prs, "03", "The decision requested", "make the “yes” easy", A3)
    content_slide(prs, pg(), "Close with a clear ask", "", [
        (0, "A business case that doesn't ask for anything gets “noted”, not approved."),
        (0, "The final section makes the decision easy: state exactly what you want approved, today.",
            {"bold": True, "color": A3, "mark_color": A3}),
    ], accent=A3)
    content_slide(prs, pg(), "What to ask for", "be specific", [
        (0, "Approve the recommended option."),
        (0, "Approve the action plan as the roadmap."),
        (0, "Authorise the budget envelope (the figure from your CBA)."),
        (0, "List the next steps; defer the high-risk gates to their change-management approval."),
        (0, "The ask should be answerable with a single “approved”.",
            {"bold": True, "color": A3, "mark_color": A3}),
    ], accent=A3)
    activity_slide(prs, pg(), "Write Next Steps & the Decision Requested", [
        (0, "In your working copy of the Business Case, add the Next Steps and Decision Requested section for the Accounting System — completing the written business case.", {"bold": True}),
        (0, "Remember to:"),
        (1, "State the specific decisions you're asking the board to make (option, plan, budget)."),
        (1, "List the immediate next steps."),
        (1, "Note how the high-risk steps route through the change-management procedure."),
        (0, "~½ page."),
        (0, "⚠  A specific, answerable ask — name the option, the plan, and the budget figure.", {"color": A3, "mark_color": A3}),
    ], "~15 min, then we discuss", accent=A3)
    takeaways_slide(prs, pg(), "Section 3 · The decision requested", [
        "End with a specific, answerable ask: approve option + plan + budget.",
        "Defer high-risk gates to their change-management approval.",
        "Your written business case is now complete — diagnosis, evidence, decision and plan.",
    ], accent=A3)

    # ===== Close =====
    close_slide(prs, "The case is written — now make it", [
        "You've completed the written business case: diagnosis → evidence → decision & plan.",
        "Recommendation, action plan and a clear ask — everything a board needs to say yes.",
        "A written case only persuades if it's also delivered well.",
        "Next: present it — pitch the case to the board and handle the room.",
    ])

    save(prs, path)


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else OUT_DEFAULT
    build(out)
