#!/usr/bin/env python3
"""Topic 9 (Operability & justification) — Kangan-branded teaching deck. AT2 build Topic.

Makes the Topic 6-8 build operable + defensible: C1 monitoring (CloudWatch baseline), C2
validation (does it meet the design?), C3 justifying the C1-C8 configuration decisions against
the Ledgerline workload (the marked AT2 judgement).

Reuse-first: C1 CloudWatch authored from ACA M10 monitoring section (S9-S16) / ACF M10. C2 and C3
are bespoke (the validation + justification discipline AWS decks don't teach) and run teach ->
practice. No recorded CloudWatch demo in the catalogue, so C1's demo is the one LIVE instructor
demo; C2/C3 have no demo. Depth ceiling: baseline alarms + baseline recovery objectives; HA-tuned
monitoring / availability / failure-sim are AT3. Layouts in kangan_deck.py.

Usage:  python scripts/build_kangan_topic9_deck.py [output.pptx]
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kangan_deck import *  # noqa: F401,F403

OUT_DEFAULT = "S1-CL1-Cloud-Design-Build/delivery/topic_09/Topic_09_Slides.pptx"

A1, A2, A3 = MAGENTA, SKY, GREEN


def build(path):
    prs = new_deck()
    n = [0]
    def pg(): n[0] += 1; return n[0]

    title_slide(prs, "09", "Operability & justification",
                "Monitor the build, validate it works, and justify every decision against the workload")

    content_slide(prs, pg(), "From built to defensible", "the build needs to stand up", [
        (0, "Topics 6–8 built the workload — foundation, network, compute, data."),
        (0, "Now make it operable and defensible: monitor it, validate it, and justify the open decisions.",
            {"bold": True, "color": A1, "mark_color": A1}),
        (0, "These three things are exactly what the Deployment Report is marked on."),
        (0, "Topic 10 then turns the evidence and justifications into the report itself."),
    ])

    # ===== C1 — Monitoring & logging (CloudWatch) =====
    divider_slide(prs, "01", "Monitoring & logging", "CloudWatch baseline", A1)
    content_slide(prs, pg(), "What monitoring is", "the fundamentals", [
        (0, "A metric is a measurement taken over time — CPU %, free storage, database connections."),
        (0, "An alarm is a threshold on a metric that fires an action or a notification when crossed."),
        (0, "A log is a record of events — what happened, and when."),
        (0, "You monitor so you find out before your users do.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], accent=A1)
    visual_slide(prs, pg(), "Amazon CloudWatch", "AWS · ACA M10 S9–S12", [
        (0, "Collects metrics and logs from AWS services into one place."),
        (0, "Alarms send notifications (e.g. to SNS) or trigger actions (e.g. Auto Scaling)."),
        (0, "Dashboards visualise metrics and alarms; CloudWatch Logs centralises log files.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], ["AWS — CloudWatch metrics / alarms / dashboards (ACA M10 S9–S12)"], A1)
    table_slide(prs, pg(), "The monitoring you'll build", "the design · §4.10",
                ["Baseline alarm", "Threshold"],
                [["EC2 CPU high", "≥ 80% over 10 min"],
                 ["RDS CPU high", "≥ 80% over 10 min"],
                 ["RDS free storage low", "< 15%"],
                 ["ALB target 5XX / unhealthy host", "> 5 / min, or any unhealthy host"],
                 ["RDS connections high", "> 80% of max"]],
                accent=A1, col_widths=[8.5, 7.5],
                note="Logging: VPC flow logs + RDS logs → CloudWatch Logs; ALB access logs → S3; EC2 OS logs via the CloudWatch Agent; audit-relevant logs retained 7 years. HA-tuned alarms come in AT3.")
    demo_slide(prs, pg(), "Create a CloudWatch alarm", [
        (0, "Pick a metric (e.g. EC2 CPU) and set a threshold and period."),
        (0, "Choose the action — a notification (SNS), or an Auto Scaling action."),
        (0, "Confirm the alarm state, and view it on a dashboard."),
    ], accent=A1)  # live — no recorded CloudWatch demo in the catalogue
    activity_slide(prs, pg(), "Stand up the baseline monitoring", [
        (0, "In the lab, per the design's §4.10:", {"bold": True}),
        (1, "create the baseline alarms (EC2/RDS CPU, RDS storage + connections, ALB 5XX/unhealthy)"),
        (1, "enable the logging destinations (CloudWatch Logs, ALB access logs to S3, the CloudWatch Agent)"),
        (0, "Capture evidence — the alarms and the log configuration.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], "~15 min", accent=A1)
    takeaways_slide(prs, pg(), "Section 1 · Monitoring", [
        "A metric is measured over time; an alarm fires on a threshold; a log records events.",
        "CloudWatch collects metrics + logs, alarms, and dashboards in one place.",
        "Build the design's baseline alarms + logging — HA-tuned alarms are AT3.",
        "Monitoring is evidence: capture the alarms and log config.",
    ], accent=A1)

    # ===== C2 — Validation =====
    divider_slide(prs, "02", "Validation", "does it meet the design?", A2)
    content_slide(prs, pg(), "What validation is", "the fundamentals", [
        (0, "Building something is not the same as confirming it does what was asked."),
        (0, "Validation = test → observe → compare to the requirement/design → fix.",
            {"bold": True, "color": A2, "mark_color": A2}),
        (0, "It's how you (and the assessor) know the build actually meets the spec."),
    ], accent=A2)
    content_slide(prs, pg(), "Validate against the design + recovery objectives", "consolidate the tests", [
        (0, "Pull together the tests you've already run: connectivity (Reachability Analyzer), app→database, and scaling."),
        (0, "Check the build meets the design's recovery objectives: RPO ≤ 1 hour, RTO ≤ 1 business day."),
        (0, "Name the known limit honestly: this baseline is single-AZ — the single AZ and single RDS instance are SPOFs.",
            {"bold": True, "color": A2, "mark_color": A2}),
        (0, "That SPOF is tolerable for a business-hours service now, and is the objective of the AT3 HA design."),
    ], accent=A2)
    activity_slide(prs, pg(), "Validate the build", [
        (0, "In the lab, run a validation pass against the design:", {"bold": True}),
        (1, "confirm connectivity (staff→ALB, app→database) and the scaling behaviour"),
        (1, "check the recovery objectives are met; note the single-AZ SPOF"),
        (0, "Record each result and any fix; capture evidence.",
            {"bold": True, "color": A2, "mark_color": A2}),
    ], "~15 min", accent=A2)
    takeaways_slide(prs, pg(), "Section 2 · Validation", [
        "Validation confirms the build meets the requirement — not just that it exists.",
        "Consolidate the connectivity + scaling tests into a check against the design.",
        "Check the recovery objectives; name the single-AZ SPOF honestly.",
        "Record results and fixes — they're report evidence.",
    ], accent=A2)

    # ===== C3 — Justifying the configuration decisions (centrepiece) =====
    divider_slide(prs, "03", "Justifying your decisions", "C1–C8 against the workload", A3)
    content_slide(prs, pg(), "What it means to justify", "the fundamentals", [
        (0, "“I chose X” is not a justification."),
        (0, "“I chose X because the workload needs Y, weighed against cost / security / residency — and the alternative was worse, for these reasons” is.",
            {"bold": True, "color": A3, "mark_color": A3}),
        (0, "A justification is specific to this workload, and names the trade-off."),
    ], accent=A3)
    content_slide(prs, pg(), "The method — justify against the workload", "four steps, every decision", [
        (0, "1. State the decision (what you chose)."),
        (0, "2. The workload facts that bear on it (load, pattern, data sensitivity, residency, cost appetite)."),
        (0, "3. Weigh it — performance vs cost vs security vs residency."),
        (0, "4. Name the alternative and why you rejected it.",
            {"bold": True, "color": A3, "mark_color": A3}),
    ], accent=A3)
    table_slide(prs, pg(), "The decisions you'll justify", "the design · §4.16 (C1–C8)",
                ["#", "Decision", "Justify against…"],
                [["C1", "EC2 instance type", "typical 15–25 / month-end 45–55 users"],
                 ["C2", "RDS instance class", "read-heavy at month-end"],
                 ["C3", "SQL Server licence model", "cost (licence-included vs BYOL)"],
                 ["C4", "EBS data-volume size", "footprint + 12-month growth"],
                 ["C5–C8", "ASG params · backup/RPO · DNS+ACM · bastion/RDP", "the workload + the design's targets"]],
                accent=A3, col_widths=[1.3, 6.7, 8.0],
                note="Each is made and evidenced in the Deployment Report, justified against the Ledgerline workload.")
    content_slide(prs, pg(), "Worked example — SQL Server licensing (C3)", "the method, end to end", [
        (0, "Decision: licence-included (pay hourly, includes the SQL Server licence) vs bring-your-own-licence (BYOL)."),
        (0, "Workload facts: steady business-hours use; YAT may already hold SQL Server licences; cost is a stated concern."),
        (0, "Weigh: licence-included is simpler + better for variable/short use; BYOL is cheaper at steady use if licences are owned.",
            {"bold": True, "color": A3, "mark_color": A3}),
        (0, "Decide + justify: pick the cheaper-over-the-term option for this steady workload, and say why the other was rejected."),
    ], accent=A3)
    activity_slide(prs, pg(), "Justify the C1–C8 decisions", [
        (0, "Using the four-step method, write a justified rationale for each of the design's open decisions:", {"bold": True}),
        (1, "ground each in the Ledgerline workload — 15–25 typical / 45–55 month-end; read-heavy month-end"),
        (1, "financial-records residency; 7-year retention; business-hours, idle overnight"),
        (0, "These rationales go straight into your Deployment Report.",
            {"bold": True, "color": A3, "mark_color": A3}),
    ], "~30 min", accent=A3)
    takeaways_slide(prs, pg(), "Section 3 · Justification", [
        "A justification names the workload need, the trade-off, and the rejected alternative.",
        "Use the four-step method on every open decision.",
        "Ground every choice in the Ledgerline workload — not generic best practice.",
        "These rationales are the heart of what the report is marked on.",
    ], accent=A3)

    # ===== Close =====
    takeaways_slide(prs, pg(), "Topic 9 · Key takeaways", [
        "Monitor the build — baseline alarms + logging (CloudWatch).",
        "Validate it against the design and the recovery objectives; name the SPOF.",
        "Justify every open decision against the workload — performance, cost, security, residency.",
        "Baseline operability only — HA-tuned monitoring and availability are AT3.",
        "Monitoring, validation and justifications all feed the Deployment Report.",
    ], accent=GOLD)
    close_slide(prs, "Next: Topic 10 — Evidencing & documenting",
                ["Assemble the evidence, the validation results and the C1–C8 justifications into the Deployment Report — the AT2 deliverable.",
                 "Everything you've captured since Topic 6 comes together here."], accent=GOLD)

    save(prs, path)


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else OUT_DEFAULT
    build(out)
