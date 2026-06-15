#!/usr/bin/env python3
"""Topic 13 (HA implementation & simulation) — Kangan-branded teaching deck. AT3 — Part B skills.

Students implement their own Topic 12 HA design on the running baseline, then simulate failures and
resizes to prove fault tolerance. ICTCLD502 element 4 (+ 5.1). Three components: C1 implement +
demonstrate connectivity at all tiers; C2 monitor + simulate failures/resizes; C3 compare to the
design, improve, document.

Reuse-first from the bespoke ICTCLD502 Topic 4 deck (implement/simulate/finalise method) + ACA M10
S44 (recorded "Creating a Highly Available Application" demo). C1 = teach -> DEMONSTRATE (recorded)
-> practice; C2/C3 = teach -> practice (student-driven simulations; no recorded "simulate a failure"
demo exists). 502 decks labelled by title; no UoC refs on slides. Layouts in kangan_deck.py.

Usage:  python scripts/build_kangan_topic13_deck.py [output.pptx]
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kangan_deck import *  # noqa: F401,F403

OUT_DEFAULT = "S1-CL1-Cloud-Design-Build/delivery/topic_13/Topic_13_Slides.pptx"

A1, A2, A3 = MAGENTA, SKY, GREEN


def build(path):
    prs = new_deck()
    n = [0]
    def pg(): n[0] += 1; return n[0]

    title_slide(prs, "13", "HA implementation & simulation",
                "Build your HA design — then break it on purpose to prove it works")

    content_slide(prs, pg(), "Build it, then break it", "AT3 Part B skills", [
        (0, "In Topic 12 you designed the HA upgrade; now you implement it on the running baseline."),
        (0, "Then you simulate failures and resizes — to prove the design is actually fault tolerant.",
            {"bold": True, "color": A1, "mark_color": A1}),
        (0, "Build → demonstrate connectivity → simulate → compare to your design → improve → document."),
        (0, "For the build: watch the recorded demo, then do it. The simulations you drive yourself."),
    ])

    # ===== C1 — Implement the design =====
    divider_slide(prs, "01", "Implement the design", "harden in place", A1)
    content_slide(prs, pg(), "Implementation approaches", "ICTCLD502 · Implement & finalise", [
        (0, "Big-bang / cutover — switch over all at once: fastest, but high risk."),
        (0, "Incremental — adopt in phases: easier to adapt and troubleshoot; slower."),
        (0, "Parallel — run old and new together: safest fall-back, but highest cost."),
        (0, "In-place HA hardening is incremental — add redundancy without taking the service down.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], accent=A1)
    content_slide(prs, pg(), "Build it well", "ICTCLD502 · Implement & finalise", [
        (0, "Deploy with scripts (infrastructure as code) — repeatable, documented, fewer errors."),
        (0, "Right-size with the Auto Scaling group instead of guessing capacity."),
        (0, "Automate security and monitoring (IAM, CloudWatch, alarms).",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], accent=A1)
    content_slide(prs, pg(), "Demonstrate connectivity at all tiers", "ICTCLD502 · Implement & finalise", [
        (0, "After implementing, confirm each tier works — and only talks to what it should:"),
        (1, "client → application; application → database; database reachable only from the app tier"),
        (0, "Confirm failover works — and that you can fail back to the primary.",
            {"bold": True, "color": A1, "mark_color": A1}),
        (0, "This is the evidence that the build is correct, not just present."),
    ], accent=A1)
    demo_slide(prs, pg(), "Build a highly available application", [
        (0, "Create an Auto Scaling group spread across two Availability Zones, behind a load balancer."),
        (0, "Add a Multi-AZ database with an automatic-failover standby."),
        (0, "Confirm the load balancer routes only to healthy targets across both AZs."),
    ], accent=A1, source="ACA M10 · Creating a Highly Available Application (S44)")
    activity_slide(prs, pg(), "Implement your HA design", [
        (0, "On the running Accounting baseline, implement the hardening from your Topic 12 design:", {"bold": True}),
        (1, "add the second AZ + mirrored subnets; extend the ASG and ALB across both AZs"),
        (1, "convert the database to Multi-AZ; add the second NAT gateway"),
        (0, "Demonstrate connectivity at all tiers and capture evidence.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], "~30 min", accent=A1)
    takeaways_slide(prs, pg(), "Section 1 · Implement", [
        "In-place HA hardening is incremental — no outage.",
        "Deploy with IaC; right-size with the ASG; automate security + monitoring.",
        "Demonstrate connectivity at every tier, including failover and fail-back.",
        "Capture the evidence as you build.",
    ], accent=A1)

    # ===== C2 — Simulate failures & resizes =====
    divider_slide(prs, "02", "Simulate failures & resizes", "break it on purpose", A2)
    content_slide(prs, pg(), "Why simulate?", "ICTCLD502 · Implement & finalise", [
        (0, "An untested backup plan isn't a plan."),
        (0, "In 2016 Delta Air Lines had an outage when failed equipment exposed a backup that had never been tested — about US$100 million.",
            {"bold": True, "color": A2, "mark_color": A2}),
        (0, "You simulate failures to confirm every part of the HA design actually works."),
    ], accent=A2)
    content_slide(prs, pg(), "Monitor & measure availability", "ICTCLD502 · Implement & finalise", [
        (0, "Watch uptime, errors and latency throughout the simulation — you can't prove availability you didn't measure."),
        (0, "Use CloudWatch metrics + alarms and the AWS Health Dashboard."),
        (0, "Record the numbers before, during and after each simulated failure.",
            {"bold": True, "color": A2, "mark_color": A2}),
    ], accent=A2)
    content_slide(prs, pg(), "Simulate failures", "ICTCLD502 · Implement & finalise", [
        (0, "Disable assets — terminate an instance, or take down an Availability Zone's resources."),
        (0, "Network disruption — block traffic to a subnet."),
        (0, "Confirm the system fails over to the redundant assets and keeps serving — that's fault tolerance proven.",
            {"bold": True, "color": A2, "mark_color": A2}),
    ], accent=A2)
    content_slide(prs, pg(), "Simulate resizes & load", "ICTCLD502 · Implement & finalise", [
        (0, "Load testing — does it work under the expected workload (e.g. month-end peak)?"),
        (0, "Stress testing — where's the breaking point, and does it fail gracefully (queued / busy messages, data safe)?"),
        (0, "Resize a component and measure the availability impact — vertical resizes often take a brief outage.",
            {"bold": True, "color": A2, "mark_color": A2}),
    ], accent=A2)
    activity_slide(prs, pg(), "Run the simulations", [
        (0, "Per your simulation plan, with monitoring on:", {"bold": True}),
        (1, "fail an instance / an AZ — confirm the service stays up (fault tolerant)"),
        (1, "trigger a database failover, then fail back"),
        (1, "resize under load and measure the availability impact"),
        (0, "Record the availability impact of each, with evidence.",
            {"bold": True, "color": A2, "mark_color": A2}),
    ], "~30 min", accent=A2)
    takeaways_slide(prs, pg(), "Section 2 · Simulate", [
        "Untested HA isn't HA — simulate to prove it.",
        "Measure availability (CloudWatch) throughout each simulation.",
        "Simulate failures (disable assets / block a subnet) and confirm failover.",
        "Load/stress test and measure the impact of a resize.",
    ], accent=A2)

    # ===== C3 — Compare, improve & document =====
    divider_slide(prs, "03", "Compare, improve & document", "did it meet the design?", A3)
    content_slide(prs, pg(), "Compare findings to the design", "your documented design", [
        (0, "Measure what the simulations showed against your documented recovery objectives."),
        (0, "Did the build meet its RPO/RTO? Did each SPOF's fix actually hold under failure?",
            {"bold": True, "color": A3, "mark_color": A3}),
        (0, "Note any gap between the design's intent and the simulated reality."),
    ], accent=A3)
    content_slide(prs, pg(), "Improve availability if needed", "ICTCLD502 · Implement & finalise", [
        (0, "If a simulation shows a prolonged outage or poor availability, adjust the design:"),
        (1, "more redundancy · Multi-AZ · managed services with built-in HA · monitoring with auto-triggered recovery"),
        (0, "Make the change, then re-test to confirm the improvement.",
            {"bold": True, "color": A3, "mark_color": A3}),
    ], accent=A3)
    activity_slide(prs, pg(), "Compare, adjust & document", [
        (0, "Finalise the implementation:", {"bold": True}),
        (1, "compare your simulation findings against your documented design"),
        (1, "make any improvements the simulations call for, and re-test"),
        (0, "Document the simulation findings against the design — this feeds the HA Deployment Report.",
            {"bold": True, "color": A3, "mark_color": A3}),
    ], "~20 min", accent=A3)
    takeaways_slide(prs, pg(), "Section 3 · Compare & improve", [
        "Compare simulation findings to the documented recovery objectives.",
        "Improve where the simulations show gaps — then re-test.",
        "Document the findings against the design.",
        "What you record here becomes the HA Deployment Report.",
    ], accent=A3)

    # ===== Close =====
    takeaways_slide(prs, pg(), "Topic 13 · Key takeaways", [
        "Implement incrementally — harden in place with no outage.",
        "Demonstrate connectivity at all tiers, including failover.",
        "Simulate failures and resizes to *prove* fault tolerance; measure availability.",
        "Compare to the design, improve where needed, and document the findings.",
        "You implemented and proved your own design.",
    ], accent=GOLD)
    close_slide(prs, "Next: Topic 14 — Closure & documentation",
                ["Write the HA Deployment Report from your evidence and findings, seek and respond to feedback, and obtain final sign-off — closing the engagement.",
                 "Bring your simulation findings."], accent=GOLD)

    save(prs, path)


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else OUT_DEFAULT
    build(out)
