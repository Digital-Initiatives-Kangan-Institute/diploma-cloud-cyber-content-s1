#!/usr/bin/env python3
"""Topic 2 (The case for change) — Kangan-branded teaching deck. All bespoke (BC §3–§5).

Content only; brand + layouts live in kangan_deck.py.
Usage:  python scripts/build_kangan_topic2_deck.py [output.pptx]
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kangan_deck import *  # noqa: F401,F403  (brand palette + layouts)

OUT_DEFAULT = "S1-CL1-Cloud-Design-Build/delivery/topic_02/Topic_02_Slides.pptx"


def build(path):
    prs = new_deck()
    n = [0]
    def pg(): n[0] += 1; return n[0]

    # Title
    title_slide(prs, "02", "The case for change", "Prove the problem before you propose the fix")

    # Opener framing
    content_slide(prs, pg(), "The consultant's first real job", "diagnose before you prescribe", [
        (0, "You can speak cloud now — now you do the diagnosis."),
        (0, "Find out where the organisation is, where it needs to be, and the gap between."),
        (0, "Three moves: align to strategy → describe the current state → expose the gaps.",
            {"bold": True, "color": GOLD_DK}),
        (0, "These three become the opening sections of the business case you'll build."),
    ])
    content_slide(prs, pg(), "A case for change is evidence, not opinion", "", [
        (0, "It answers three questions, in order:"),
        (1, "Where does the organisation want to go?   — strategy"),
        (1, "Where is it now?   — current state"),
        (1, "What's missing to get there?   — gaps"),
        (0, "You're not choosing a solution yet — you're proving the problem is real and worth solving."),
        (0, "Solutions come next. Diagnose before you prescribe.", {"bold": True, "color": MAGENTA, "mark_color": MAGENTA}),
    ])

    # ---- Section 1 ----
    divider_slide(prs, "01", "Strategic alignment", "tie the initiative to the organisation's goals", MAGENTA)
    content_slide(prs, pg(), "Start with strategy", "or the board won't fund it", [
        (0, "A board funds change that moves the organisation toward its own stated goals."),
        (0, "Lead by showing the initiative serves the strategy — not technology for its own sake."),
        (0, "Strategic alignment = “here's what they said they want; here's how this delivers it.”"),
        (0, "It's the “why this, why now” that earns everything that follows.", {"bold": True, "color": GOLD_DK}),
    ], accent=MAGENTA)
    content_slide(prs, pg(), "Read a strategic plan in three layers", "", [
        (0, "Business objectives — where the whole organisation is going", {"bold": True}),
        (1, "e.g. grow students 15%/yr, expand nationally"),
        (0, "ICT goals / objectives — how ICT supports that", {"bold": True}),
        (1, "e.g. reduce in-house dependency; 99.9% for critical systems"),
        (0, "Initiatives — the planned actions", {"bold": True}),
        (1, "e.g. move suitable on-site systems to the cloud"),
        (0, "Trace your initiative up these layers — pull only what's material.",
            {"bold": True, "color": MAGENTA, "mark_color": MAGENTA}),
    ], accent=MAGENTA)
    content_slide(prs, pg(), "Add the outside view", "industry context", [
        (0, "A plan doesn't exist in a vacuum — compare it to where the industry is heading."),
        (0, "Trends that matter: cloud adoption · managed services · OPEX over CAPEX · resilience."),
        (0, "Name both directions:"),
        (1, "Alignment — the plan matches industry direction (strengthens the case)"),
        (1, "Divergence — the plan lags or differs (a risk, or an opportunity to flag)"),
    ], accent=MAGENTA)
    content_slide(prs, pg(), "What good looks like", "", [
        (0, "Every claim cited to the plan (e.g. “ICT Strategic Plan — ICT Goals”)."),
        (0, "Material items only — not the whole plan recited."),
        (0, "Traces the initiative up to a real organisational goal."),
        (0, "Alignment and divergence both named — balanced, not cheerleading.",
            {"bold": True, "color": MAGENTA, "mark_color": MAGENTA}),
    ], accent=MAGENTA)
    activity_slide(prs, pg(), "Write a Strategic Alignment section", [
        (0, "In your working copy of the Business Case, write the Strategic Alignment section for moving the Accounting System (Ledgerline).", {"bold": True}),
        (0, "Remember to:"),
        (1, "Read YAT's ICT Strategic Plan."),
        (1, "Which ICT goals/objectives does this migration serve? Trace up to a business objective — cite them."),
        (1, "Add one or two points of industry context — where's the sector heading?"),
        (1, "Note alignment and divergence."),
        (0, "~½ page."),
        (0, "⚠  Argue alignment through the ICT goals, and name the weaker links honestly. That is the analysis.",
            {"color": MAGENTA, "mark_color": MAGENTA}),
    ], "~20 min, then we discuss", accent=MAGENTA)
    takeaways_slide(prs, pg(), "Section 1 · Strategic alignment", [
        "Open with strategy: tie the initiative to the organisation's own stated goals.",
        "Three layers — business objectives / ICT goals / initiatives; pull only what's material.",
        "Add the outside view; name alignment and divergence.",
        "Cite everything. Strategy is the “why this, why now”.",
    ], accent=MAGENTA)

    # ---- Section 2 ----
    divider_slide(prs, "02", "Current-state synthesis", "synthesis, not transcription", SKY)
    content_slide(prs, pg(), "Current state is synthesis, not transcription", "", [
        (0, "Summarise the current environment in your own words, focused on what's material to this decision."),
        (0, "The board needs the picture that explains why change is needed — not a copy of the IT docs."),
        (0, "Distil it down; don't transcribe it.", {"bold": True, "color": GOLD_DK}),
    ], accent=SKY)
    content_slide(prs, pg(), "The relevance filter", "keep vs drop", [
        (0, "KEEP (if it bears on the decision):", {"bold": True}),
        (1, "platform & stack · age / condition / capacity · availability today · dependencies & integrations · constraints · pain points"),
        (0, "DROP:", {"bold": True}),
        (1, "detail that doesn't move the decision (printer counts, unrelated systems)"),
        (0, "A good current state quietly surfaces the limitations that motivate the change.",
            {"bold": True, "color": SKY, "mark_color": SKY}),
    ], accent=SKY)
    content_slide(prs, pg(), "How to distil", "", [
        (0, "Read the source docs — environment overview, server/app specs, consultation notes.", {"marker": "1.  "}),
        (0, "For each fact ask: “does this affect the renew-vs-migrate decision?” If no, cut it.", {"marker": "2.  "}),
        (0, "Re-state what's left in plain language, grouped: platform · workload · dependencies · condition/risk.", {"marker": "3.  "}),
        (0, "Aim ~½ page. No copy-paste.", {"bold": True, "color": GOLD_DK}),
    ], accent=SKY)
    activity_slide(prs, pg(), "Add the Current State section", [
        (0, "In your working copy of the Business Case, add the Current State section for the Accounting System (Ledgerline).", {"bold": True}),
        (0, "Remember to:"),
        (1, "Use the Accounting application spec, server specs, operational costing, the ICT Environment Overview, and the consultation notes."),
        (1, "Cover: platform & stack · workload (incl. month-end / EOFY peaks) · integrations (AD, O365, LMS fee-status, payroll, banking) · condition & constraints."),
        (0, "~½ page."),
        (0, "⚠  Material only — synthesise in your own words, no verbatim copying.",
            {"color": SKY, "mark_color": SKY}),
    ], "~20 min, then we discuss", accent=SKY)
    takeaways_slide(prs, pg(), "Section 2 · Current state", [
        "Own words, material facts only — synthesis beats transcription.",
        "Filter every fact against “does it affect the decision?”",
        "Surface the limitations that set up the gap analysis.",
    ], accent=SKY)

    # ---- Section 3 ----
    divider_slide(prs, "03", "Gap analysis", "bridges “want” and “have”", GREEN)
    content_slide(prs, pg(), "Gap analysis bridges “want” and “have”", "", [
        (0, "It bridges where we want to be (strategy + requirements) and where we are (current state)."),
        (0, "It makes the problem concrete and measurable."),
        (0, "It hands the next stage a list of changes to evaluate."),
        (0, "No gap → no case.", {"bold": True, "color": GREEN, "mark_color": GREEN}),
    ], accent=GREEN)
    table_slide(prs, pg(), "The gap table", "one row per objective",
                ["Objective", "Current", "Desired", "Gap", "Opportunity", "Proposed change"],
                [["", "", "", "", "", ""]],
                accent=GREEN,
                col_widths=[2.2, 2.0, 1.9, 1.9, 1.9, 2.0],
                note="Objective/Desired ← Strategic Alignment + requirements · Current ← your Current State · Proposed change = the seed of the options you'll weigh next.")
    table_slide(prs, pg(), "Anatomy of a good row", "one objective, traced end to end",
                ["Field", "Example"],
                [["Objective", "“reduce dependency on in-house server infrastructure”"],
                 ["Current", "single ageing on-prem server, owned and maintained in-house"],
                 ["Desired", "no in-house server to own / patch / replace"],
                 ["Gap", "full reliance on end-of-life hardware the organisation must run itself"],
                 ["Opportunity", "move to a managed / cloud platform"],
                 ["Proposed change", "evaluate migrating the workload to the cloud (→ next topic)"]],
                accent=GREEN,
                col_widths=[2.6, 9.3],
                note="Traceable both ways — objective came from the plan, current from your Current State.")
    activity_slide(prs, pg(), "Build the Gap Analysis", [
        (0, "In your working copy of the Business Case, add the Gap Analysis for the Accounting System (Ledgerline) — a table of at least 3 rows.", {"bold": True}),
        (0, "Remember to draw objectives from your Strategic Alignment work + the migration requirements, e.g.:"),
        (1, "reduce in-house infrastructure dependency (ageing server)"),
        (1, "business-hours availability ≥ 99.5% (RPO ≤ 1h / RTO ≤ 1 business day)"),
        (1, "keep financial data onshore + 7-year retention"),
        (1, "size for month-end / EOFY peaks without year-round over-provisioning"),
        (0, "Fill every column: objective → current → desired → gap → opportunity → proposed change."),
        (0, "⚠  Each row must trace back to a real objective and your current-state facts.",
            {"color": GREEN, "mark_color": GREEN}),
    ], "~25 min, then we discuss", accent=GREEN)
    takeaways_slide(prs, pg(), "Section 3 · Gap analysis", [
        "Gap analysis = desired (strategy + requirements) vs current (your synthesis).",
        "One row per objective; fill all six columns; keep it traceable.",
        "The “proposed change” column feeds straight into the options analysis next.",
    ], accent=GREEN)

    # ---- Close ----
    close_slide(prs, "From diagnosis to evaluation", [
        "You've built the case for change: strategy → current state → gaps.",
        "That's the first half of a business case — it proves the problem is real and worth solving.",
        "Your “proposed changes” aren't decisions yet — they're candidates.",
        "Next: weigh the options, cost them, assess the risk — turning the case for change into a recommendation.",
        "You practised on the Accounting System; the same moves carry to whatever engagement lands on your desk.",
    ])

    save(prs, path)


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else OUT_DEFAULT
    build(out)
