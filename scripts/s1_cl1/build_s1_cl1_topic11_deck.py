#!/usr/bin/env python3
"""Topic 11 (HA concepts) — Kangan-branded teaching deck. First AT3 content Topic.

Concepts layer for High Availability: C1 availability/reliability/service levels, C2 single
points of failure + recovery objectives (RTO/RPO) + vertical-scaling cost, C3 achieving
availability in the cloud (Multi-AZ, load balancing, autoscaling, Multi-AZ databases).

Reuse-first from the bespoke ICTCLD502 Topics 1-3 decks (purpose-built for this unit) + ACA M10
for the AWS HA mechanisms/diagrams. Teach + LIGHT activity (no big build — that's Topic 13; no
demos — concepts). The three light activities (match-target, spot-SPOFs, match-mechanism) run on
the single-AZ Accounting baseline and set up Topic 12, where students DESIGN the HA upgrade
themselves (we supply inputs, not a finished design). Layouts in kangan_deck.py.

Usage:  python scripts/build_kangan_topic11_deck.py [output.pptx]
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kangan_deck import *  # noqa: F401,F403

OUT_DEFAULT = "S1-CL1-Cloud-Design-Build/delivery/topic_11/Topic_11_Slides.pptx"

A1, A2, A3 = MAGENTA, SKY, GREEN


def build(path):
    prs = new_deck()
    n = [0]
    def pg(): n[0] += 1; return n[0]

    title_slide(prs, "11", "HA concepts",
                "What high availability is — and how the cloud achieves it")

    content_slide(prs, pg(), "Making the baseline highly available", "the AT3 arc", [
        (0, "AT2 built a working single-AZ baseline. AT3 makes it highly available — resilient to losing an Availability Zone."),
        (0, "Topic 11 is the concepts; Topic 12 you design the upgrade; Topic 13 you implement + simulate; Topic 14 you close out.",
            {"bold": True, "color": A1, "mark_color": A1}),
        (0, "This Topic builds the vocabulary — availability, fault tolerance, SPOFs, recovery objectives — and the cloud toolkit."),
    ])

    # ===== C1 — Availability, reliability & service levels =====
    divider_slide(prs, "01", "Availability, reliability & service levels", "what 'highly available' means", A1)
    content_slide(prs, pg(), "What is high availability?", "ICTCLD502 · HA requirements", [
        (0, "High availability = a system stays operational and accessible with minimal downtime, even if parts fail."),
        (0, "Availability is a percentage, and it maps to downtime: 99% ≈ 7 hours/month offline; 99.999% ≈ 26 seconds/month."),
        (0, "More nines costs a lot more — often 2–5× — and isn't always achievable.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], accent=A1)
    content_slide(prs, pg(), "Reliability & service levels", "ICTCLD502 · HA requirements", [
        (0, "Reliability = how consistently a service works correctly (availability only means it's online)."),
        (0, "A service level is a performance target (availability, response time)."),
        (0, "A Service Level Agreement (SLA) sets the minimum service level — miss it and credits/penalties apply.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], accent=A1)
    content_slide(prs, pg(), "YAT's availability target", "the design", [
        (0, "Ledgerline needs ≥ 99.5% availability in business hours (Mon–Fri ~07:30–18:00) — there's no 24/7 requirement."),
        (0, "The HA goal is to survive the loss of an Availability Zone — not to chase 99.999%.",
            {"bold": True, "color": A1, "mark_color": A1}),
        (0, "Five-nines would multiply the cost for resilience this business-hours workload doesn't need."),
    ], accent=A1)
    activity_slide(prs, pg(), "Match the target to the business", [
        (0, "Quick discussion:", {"bold": True}),
        (1, "why does 99.5% business-hours fit Ledgerline, and what downtime does it allow?"),
        (1, "when would chasing five-nines be the wrong call — and why?"),
    ], "~5 min", accent=A1)
    takeaways_slide(prs, pg(), "Section 1 · Availability", [
        "HA = stay operational with minimal downtime despite failures.",
        "Availability % maps to real downtime; more nines costs 2–5× more.",
        "Reliability (works correctly) is more than availability (online); SLAs set the minimum.",
        "YAT's target is 99.5% business-hours and AZ resilience — not five-nines.",
    ], accent=A1)

    # ===== C2 — Single points of failure & recovery objectives =====
    divider_slide(prs, "02", "Single points of failure & recovery objectives", "where it breaks, and how fast you recover", A2)
    content_slide(prs, pg(), "What is a single point of failure?", "ICTCLD502 · Evaluating availability", [
        (0, "A single point of failure (SPOF) is any component whose failure stops the whole service."),
        (0, "Like a car's engine — one failure and nothing moves."),
        (0, "In IT: many app servers all on one database; a whole office on one internet link; one server, one Availability Zone.",
            {"bold": True, "color": A2, "mark_color": A2}),
    ], accent=A2)
    content_slide(prs, pg(), "Recovery objectives — RTO & RPO", "ICTCLD502 · Evaluating availability", [
        (0, "RTO (Recovery Time Objective) = the maximum downtime the business will tolerate."),
        (0, "RPO (Recovery Point Objective) = the maximum data loss it will tolerate."),
        (0, "Worked example: backups every 15 min → RPO 15 min; recover 3 layers at 30 min each + 1 h testing → RTO 2.5 h.",
            {"bold": True, "color": A2, "mark_color": A2}),
        (0, "Why not set both to zero? Cost — zero loss / zero downtime is extremely expensive."),
    ], accent=A2)
    content_slide(prs, pg(), "Vertical scaling and its availability cost", "ICTCLD502 · Evaluating availability", [
        (0, "Vertical scaling = a bigger server (more CPU/RAM); horizontal scaling = more servers."),
        (0, "Vertical scaling usually needs a shutdown/restart and hits a ceiling — so it's an availability cost.",
            {"bold": True, "color": A2, "mark_color": A2}),
        (0, "Horizontal scaling is preferred for availability; mitigate vertical changes via an overnight window, a standby switch, or hot-swap."),
    ], accent=A2)
    activity_slide(prs, pg(), "Spot the SPOFs in the baseline", [
        (0, "Look at the single-AZ Accounting baseline you'd be hardening:", {"bold": True}),
        (1, "list its single points of failure (think: AZ, database, the running instance, egress)"),
        (1, "estimate the baseline's recovery objectives (RPO / RTO) and where they fall short"),
        (0, "Keep your list — Topic 12 designs these out.",
            {"bold": True, "color": A2, "mark_color": A2}),
    ], "~10 min", accent=A2)
    takeaways_slide(prs, pg(), "Section 2 · SPOFs & recovery", [
        "A SPOF is any component whose failure stops the whole service.",
        "RTO = tolerable downtime; RPO = tolerable data loss; zero costs the most.",
        "Vertical scaling carries downtime + a ceiling — horizontal scaling aids availability.",
        "The baseline's single AZ and single database are its key SPOFs.",
    ], accent=A2)

    # ===== C3 — Achieving availability in the cloud =====
    divider_slide(prs, "03", "Achieving availability in the cloud", "the HA toolkit", A3)
    content_slide(prs, pg(), "Built-in vs designed fault tolerance", "ICTCLD502 · HA design", [
        (0, "Using the cloud does not make you highly available by itself."),
        (0, "You design redundancy — across compute, storage and network — so no single failure takes the service down.",
            {"bold": True, "color": A3, "mark_color": A3}),
        (0, "A single-AZ cloud design has a SPOF just like an on-prem one."),
    ], accent=A3)
    content_slide(prs, pg(), "The cloud HA toolkit", "ICTCLD502 · HA requirements · ACA M10", [
        (0, "Multi-AZ — run resources across Availability Zones so the loss of one AZ doesn't stop the service."),
        (0, "Load balancing — spread traffic across servers; route only to healthy ones."),
        (0, "Auto Scaling across AZs — keep healthy capacity in each AZ (availability, not just load)."),
        (0, "Managed Multi-AZ databases — a synchronous standby with automatic failover. (Multi-Region / full DR is out of scope — CL2.)",
            {"bold": True, "color": A3, "mark_color": A3}),
    ], accent=A3)
    visual_slide(prs, pg(), "Multi-AZ in action", "ICTCLD502 · HA requirements · ACA M10", [
        (0, "A Multi-AZ database keeps a primary in one AZ and a synchronous standby in another."),
        (0, "If the primary (or its AZ) fails, the standby is promoted automatically — service continues with seconds of downtime."),
        (0, "The application reaches the database by name, so nothing needs reconfiguring.",
            {"bold": True, "color": A3, "mark_color": A3}),
    ], ["Multi-AZ RDS — primary + synchronous standby (ICTCLD502 · HA requirements S13; alt: ACA M10 S44)"], A3)
    activity_slide(prs, pg(), "Match the mechanism to the SPOF", [
        (0, "For each SPOF you found in the baseline, name the cloud mechanism that removes it:", {"bold": True}),
        (1, "single AZ → ?  ·  single database → ?  ·  single running instance → ?  ·  single NAT gateway → ?"),
        (0, "(Answers: a second AZ · Multi-AZ database · an ASG across AZs · a NAT gateway per AZ.)",
            {"bold": True, "color": A3, "mark_color": A3}),
        (0, "This is the shape of the design you'll produce in Topic 12."),
    ], "~10 min", accent=A3)
    takeaways_slide(prs, pg(), "Section 3 · Cloud HA", [
        "The cloud doesn't give you HA — you design redundancy across the tiers.",
        "The toolkit: Multi-AZ, load balancing, auto-scaling across AZs, Multi-AZ databases.",
        "Multi-AZ databases fail over automatically — seconds of downtime, no app change.",
        "Each baseline SPOF maps to a mechanism — that's your HA design.",
    ], accent=A3)

    # ===== Close =====
    takeaways_slide(prs, pg(), "Topic 11 · Key takeaways", [
        "High availability = stay up despite failure; availability % ↔ downtime and cost.",
        "SPOFs and RTO/RPO are how you reason about availability.",
        "Vertical scaling costs availability; horizontal scaling and redundancy buy it.",
        "The cloud HA toolkit (Multi-AZ, LB, autoscaling, Multi-AZ DB) removes SPOFs.",
        "Next you'll use this to DESIGN the HA upgrade yourself.",
    ], accent=GOLD)
    close_slide(prs, "Next: Topic 12 — HA design",
                ["You design the HA upgrade for the Accounting baseline — review it, remove its SPOFs, set recovery objectives, and document the design.",
                 "You produce the design; the requirements and the baseline are your inputs."], accent=GOLD)

    save(prs, path)


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else OUT_DEFAULT
    build(out)
