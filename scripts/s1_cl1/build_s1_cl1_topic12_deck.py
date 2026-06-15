#!/usr/bin/env python3
"""Topic 12 (HA design) — Kangan-branded teaching deck. AT3 content Topic — Part A skills.

Where students DESIGN the HA upgrade (we supply inputs, not a finished design). Three components:
C1 review the baseline & find its SPOFs (502 element 2); C2 design the HA-equivalent that removes
them, re-estimate recovery objectives (502 element 3); C3 document the design (the 502 5-part
framework) + plan implementation sequencing and the failure/resize simulations (sets up Topic 13).

Reuse-first from the bespoke ICTCLD502 Topics 2-3 (the design method + documentation framework) +
ACA M10 S41 (cross-AZ HA architecture: ALB + Multi-AZ RDS). Teach -> practice throughout (no AWS
demos — designing is analytical); the three activities together produce the HA design for the
Accounting baseline. Source-deck refs in kickers by TITLE (not "502 Topic N"); image placeholders
cite the exact slide; no UoC refs on slides. Layouts in kangan_deck.py.

Usage:  python scripts/build_kangan_topic12_deck.py [output.pptx]
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kangan_deck import *  # noqa: F401,F403

OUT_DEFAULT = "S1-CL1-Cloud-Design-Build/delivery/topic_12/Topic_12_Slides.pptx"

A1, A2, A3 = MAGENTA, SKY, GREEN


def build(path):
    prs = new_deck()
    n = [0]
    def pg(): n[0] += 1; return n[0]

    title_slide(prs, "12", "HA design",
                "Design the upgrade — review the baseline, design out its single points of failure, and document it")

    content_slide(prs, pg(), "Now you design it", "AT3 Part A skills", [
        (0, "Topic 11 gave you the concepts; Topic 12 is where you produce an HA design."),
        (0, "You design the upgrade yourself — the baseline and the HA requirements are your inputs, not a finished answer.",
            {"bold": True, "color": A1, "mark_color": A1}),
        (0, "Three moves: review the baseline + find its SPOFs → design them out → document the design and plan the work."),
        (0, "Topic 13 then implements and simulates what you design here."),
    ])

    # ===== C1 — Review the baseline & find its SPOFs =====
    divider_slide(prs, "01", "Review the baseline & find its SPOFs", "evaluate before you change", A1)
    content_slide(prs, pg(), "Review the architecture", "ICTCLD502 · Evaluating availability", [
        (0, "Start by understanding what's there: the multi-tier shape — presentation / logic / data (web / app / database)."),
        (0, "Each tier can be built, scaled and diagnosed separately."),
        (0, "Review the deployed single-AZ baseline before you change anything.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], accent=A1)
    visual_slide(prs, pg(), "Identify the single points of failure", "ICTCLD502 · Design HA S10", [
        (0, "Walk the architecture and mark every component whose failure stops the whole service."),
        (0, "In a single-AZ cloud build that's the AZ itself, the one database, the one running instance, the one NAT.",
            {"bold": True, "color": A1, "mark_color": A1}),
        (0, "A network diagram makes the SPOFs visible — find them before you design the fix."),
    ], ["Identify-SPoFs network diagram (ICTCLD502 · Design HA S10)"], A1)
    content_slide(prs, pg(), "Estimate the recovery objectives", "ICTCLD502 · Evaluating availability S8", [
        (0, "Estimate the baseline's RPO from the backup interval, and its RTO from recovery-per-tier + testing."),
        (0, "Worked example: 15-min backups → RPO 15 min; 30 min × 3 tiers + 1 h test → RTO 2.5 h."),
        (0, "Flag components that scale vertically (they carry downtime) and the availability impact.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], accent=A1)
    activity_slide(prs, pg(), "Review the Accounting baseline", [
        (0, "Take the supplied single-AZ Accounting baseline and evaluate its availability:", {"bold": True}),
        (1, "list its single points of failure (AZ · database · running instance · NAT)"),
        (1, "estimate its RPO and RTO, and where they fall short of the HA requirement"),
        (1, "note the components that scale vertically and the downtime that implies"),
        (0, "Document your findings — they drive the design.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], "~20 min", accent=A1)
    takeaways_slide(prs, pg(), "Section 1 · Review & SPOFs", [
        "Understand the multi-tier baseline before you change it.",
        "Identify every single point of failure — a diagram makes them visible.",
        "Estimate the baseline's RPO/RTO and flag vertical-scaling components.",
        "Your findings are the input to the design.",
    ], accent=A1)

    # ===== C2 — Design the HA-equivalent =====
    divider_slide(prs, "02", "Design the HA-equivalent", "remove every SPOF", A2)
    content_slide(prs, pg(), "Design redundancy — remove the SPoFs", "ICTCLD502 · Design HA S9", [
        (0, "Using the cloud doesn't make you highly available — you design redundancy."),
        (0, "For each SPOF, add redundancy across compute, storage and network so no single failure stops the service.",
            {"bold": True, "color": A2, "mark_color": A2}),
        (0, "The goal: an equivalent architecture that keeps running when one component — or one AZ — fails."),
    ], accent=A2)
    visual_slide(prs, pg(), "The cross-AZ HA architecture", "ACA M10 S41 · ICTCLD502 · Design HA S7–S8", [
        (0, "Spread the workload across two Availability Zones: load balancing across AZs → instances (ASG) across AZs → a Multi-AZ database."),
        (0, "The load balancer routes only to healthy targets; the ASG keeps capacity in each AZ; the database fails over automatically.",
            {"bold": True, "color": A2, "mark_color": A2}),
        (0, "Redundant egress (a NAT per AZ) keeps outbound working if an AZ is lost."),
    ], ["Cross-AZ HA architecture — ALB + ASG + Multi-AZ RDS (ACA M10 S41)"], A2)
    content_slide(prs, pg(), "Remove each SPOF — the mapping", "design method", [
        (0, "Single Availability Zone → a second AZ with mirrored subnets."),
        (0, "Single running instance → an Auto Scaling group spread across both AZs."),
        (0, "Single database → a Multi-AZ database with a synchronous standby + automatic failover."),
        (0, "Single NAT gateway → a NAT gateway per AZ.",
            {"bold": True, "color": A2, "mark_color": A2}),
    ], accent=A2)
    content_slide(prs, pg(), "Re-estimate the recovery objectives", "ICTCLD502 · Design HA S11", [
        (0, "Re-estimate RPO/RTO for the HA design — per component and overall."),
        (0, "RPO is unchanged (backups); RTO drops to minutes for an AZ or instance failure via automatic failover.",
            {"bold": True, "color": A2, "mark_color": A2}),
        (0, "Check the numbers now meet the HA requirement — and note what remains (the single Region)."),
    ], accent=A2)
    activity_slide(prs, pg(), "Design the HA-equivalent for Accounting", [
        (0, "Design the upgrade for the baseline you reviewed:", {"bold": True}),
        (1, "design out each SPOF using the mapping (2 AZs · cross-AZ ASG · Multi-AZ DB · NAT per AZ)"),
        (1, "sketch the cross-AZ topology"),
        (1, "re-estimate the recovery objectives and confirm they meet the requirement"),
    ], "~25 min", accent=A2)
    takeaways_slide(prs, pg(), "Section 2 · Design", [
        "HA isn't automatic — you design redundancy across the tiers.",
        "Spread across two AZs: LB + ASG across AZs, Multi-AZ database, redundant NAT.",
        "Map each SPOF to its fix — that's the HA design.",
        "Re-estimate recovery objectives and check they meet the requirement.",
    ], accent=A2)

    # ===== C3 — Document the design & plan the work =====
    divider_slide(prs, "03", "Document the design & plan the work", "the deliverable", A3)
    content_slide(prs, pg(), "What an HA design documents", "ICTCLD502 · Design HA S14", [
        (0, "Architecture diagram — the components, the redundancy, the connections between tiers."),
        (0, "Service list — the AWS services used and each one's purpose."),
        (0, "SPoF analysis — the SPOFs identified, and the solution implemented for each."),
        (0, "RTO/RPO table — recovery objectives per component and overall; scaling plans — what scales, how, and the trigger.",
            {"bold": True, "color": A3, "mark_color": A3}),
    ], accent=A3)
    content_slide(prs, pg(), "Draw the HA topology", "ICTCLD502 · Evaluating availability S12–S14", [
        (0, "A logical diagram showing the two AZs, the redundancy, the tiers and their connections."),
        (0, "Focus on the key details — boundaries, resource types, connectivity — not every setting."),
        (0, "Use the scenario's network-diagram conventions (the same draw.io style as the baseline diagram).",
            {"bold": True, "color": A3, "mark_color": A3}),
    ], accent=A3)
    content_slide(prs, pg(), "Plan the implementation & simulation", "sets up Topic 13", [
        (0, "Sequencing — the order to harden the running baseline in place, without an outage (add the AZ, extend ASG/ALB, convert the DB to Multi-AZ)."),
        (0, "Simulation plan — the failures and resizes you'll run to prove fault tolerance (AZ/instance failure, database failover, resize under load).",
            {"bold": True, "color": A3, "mark_color": A3}),
        (0, "This plan is what Topic 13 executes."),
    ], accent=A3)
    activity_slide(prs, pg(), "Produce your HA design document", [
        (0, "Assemble the HA design for the Accounting upgrade:", {"bold": True}),
        (1, "architecture diagram · service list · SPoF analysis + solutions · RTO/RPO table · scaling plans"),
        (1, "the implementation sequencing + the simulation plan"),
        (0, "This is the deliverable — the design you'll implement next.",
            {"bold": True, "color": A3, "mark_color": A3}),
    ], "~30 min", accent=A3)
    takeaways_slide(prs, pg(), "Section 3 · Document & plan", [
        "An HA design = diagram · service list · SPoF analysis · RTO/RPO table · scaling plans.",
        "Draw the topology clearly — two AZs, redundancy, tiers, connections.",
        "Plan the sequencing (harden in place, no outage) and the simulations.",
        "The documented design is the Part-A deliverable.",
    ], accent=A3)

    # ===== Close =====
    takeaways_slide(prs, pg(), "Topic 12 · Key takeaways", [
        "Review the baseline and find its single points of failure.",
        "Design them out across two AZs (LB + ASG + Multi-AZ DB + redundant NAT).",
        "Re-estimate recovery objectives against the requirement.",
        "Document the design (five parts) and plan the implementation + simulations.",
        "You produce the design — next you build it.",
    ], accent=GOLD)
    close_slide(prs, "Next: Topic 13 — HA implementation & simulation",
                ["Implement your HA design on the running baseline, then simulate failures and resizes to prove it's fault tolerant.",
                 "Bring your design document and your simulation plan."], accent=GOLD)

    save(prs, path)


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else OUT_DEFAULT
    build(out)
