#!/usr/bin/env python3
"""Topic 7 (Network & security base) — Kangan-branded teaching deck. AT2 build Topic.

Reuse-first: ACF M05 (Networking & Content Delivery) + ACA M07 (Creating a Networking
Environment) cover almost everything here — including the primers (ACF M05 S5-S9 networking
basics; ACA M07 S23 firewall analogy; ACF M05 S49-S50 DNS) and the connectivity test
(ACA M07 S45 Reachability Analyzer). Every teach slide is authored FROM those slides; the
AWS provenance is carried in each slide's kicker, and diagrams are labelled image placeholders.
Bespoke is reserved for the genuine gaps: working-to-a-supplied-design framing, the design's
specific topology / SG chain / DNS, and the evidence-capture + test discipline.

Primer-first: every concept gets a vendor-neutral primer before the AWS-context slide.
AWS practicals use teach -> DEMONSTRATE -> practice. The VPC+SG build demo is the RECORDED
ACA M07 S30 demo; the DNS-record step is the one LIVE demo (no recorded Route 53 demo fits a
private hosted zone). Layouts in kangan_deck.py.

AWS source slides: ACF M05 S5-S9, S11-S13, S17, S20-S21, S33-S35, S49-S50; ACA M07 S10-S20,
S23-S24, S30, S41, S45. See slide_plan.md.

Usage:  python scripts/build_kangan_topic7_deck.py [output.pptx]
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kangan_deck import *  # noqa: F401,F403

OUT_DEFAULT = "S1-CL1-Cloud-Design-Build/delivery/topic_07/Topic_07_Slides.pptx"

A1, A2, A3 = MAGENTA, SKY, GREEN


def build(path):
    prs = new_deck()
    n = [0]
    def pg(): n[0] += 1; return n[0]

    title_slide(prs, "07", "Network & security base",
                "Build the network tier — the VPC your workload lives in, the rules around it, and how it's found by name")

    content_slide(prs, pg(), "Continuing the build", "foundation done — now the network", [
        (0, "Topic 6 set the foundation: the account, identity, and the shared-responsibility line."),
        (0, "Now you build the network the workload sits inside.",
            {"bold": True, "color": A1, "mark_color": A1}),
        (0, "Three parts: the virtual network (VPC + subnets), traffic control (security groups), and name resolution (DNS)."),
        (0, "Still working to the supplied design — and still capturing evidence as you go."),
        (0, "For every AWS build task: watch the demo, then do it yourself."),
    ])

    # ===== C1 — Virtual network & subnets =====
    divider_slide(prs, "01", "Virtual network & subnets", "the fabric your workload lives in", A1)
    # PRIMER — authored from ACF M05 S5-S9 (networking basics)
    visual_slide(prs, pg(), "Networking, the essentials", "AWS · ACF M05 S5–S9", [
        (0, "A network connects machines so they can share resources; it can be split into smaller pieces called subnets."),
        (0, "Every machine has an IP address — a unique numeric label (e.g. 10.0.0.17)."),
        (0, "A CIDR block describes a range of addresses: 10.0.0.0/16 — the /number says how many bits are fixed.",
            {"bold": True, "color": A1, "mark_color": A1}),
        (0, "Traffic moves between networks through routers / gateways."),
    ], ["AWS — IP address / CIDR (ACF M05 S6 / S8)"], A1)
    content_slide(prs, pg(), "The VPC — your private network in AWS", "AWS · ACF M05 S11 · ACA M07 S10", [
        (0, "A VPC is a logically isolated section of AWS that you define — your own virtual network."),
        (0, "It belongs to one Region and can span Availability Zones; you size it with a CIDR block (largest /16, smallest /28; you can't change it later)."),
        (0, "You divide the VPC into subnets — each in one AZ, classified public or private.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], accent=A1)
    visual_slide(prs, pg(), "Routing: gateways & route tables", "AWS · ACA M07 S12–S16", [
        (0, "A route table holds rules that direct a subnet's traffic; every table has a built-in local route for inside-the-VPC traffic."),
        (0, "Public subnet → an Internet Gateway (a 0.0.0.0/0 route to the IGW) gives direct internet access."),
        (0, "Private subnet → no direct internet path."),
        (0, "A NAT gateway lets private resources reach OUT (e.g. patching) without being reachable from the internet.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], ["AWS — VPC anatomy: subnets · IGW · NAT · route tables (ACA M07 S16)"], A1)
    activity_slide(prs, pg(), "Public or private?", [
        (0, "For each resource, decide which subnet it belongs in — public or private:", {"bold": True}),
        (1, "the database · a batch-processing job · the web/app server · a NAT gateway"),
        (0, "Rule of thumb: anything that shouldn't be reachable from the internet goes private; only internet-facing entry points and the NAT gateway go public.",
            {"bold": True, "color": A1, "mark_color": A1}),
        (0, "(AWS recommends even web/app tiers sit private, behind a load balancer.)"),
    ], "~10 min", accent=A1)
    content_slide(prs, pg(), "The network you'll build", "work from the Solution Design", [
        (0, "Open the Solution Design for this engagement (on the intranet) and study its network topology (§4.4) — you build to that.",
            {"bold": True, "color": A1, "mark_color": A1}),
        (0, "VPC 10.0.0.0/16 (room to expand); DNS resolution + flow logs on."),
        (0, "Subnets in ap-southeast-2a: public-egress-a (NAT only) · private-app-a (app + internal ALB) · private-data-a (database)."),
        (0, "Internet Gateway is egress-only — patching via NAT; no inbound path from the internet."),
        (0, "Staff reach the service over the campus Site-to-Site VPN; route tables set per tier."),
    ], accent=A1)
    takeaways_slide(prs, pg(), "Section 1 · The virtual network", [
        "A VPC is your logically isolated network in one Region, sized by a CIDR block.",
        "Subnets split the VPC by tier and Availability Zone — public or private.",
        "Route tables + IGW/NAT decide what reaches the internet — this design is egress-only.",
        "Build to the supplied topology; Region first (data residency).",
    ], accent=A1)

    # ===== C2 — Controlling traffic (security groups) =====
    divider_slide(prs, "02", "Controlling traffic", "who may talk to what", A2)
    # PRIMER — authored from ACA M07 S23 (firewall analogy)
    content_slide(prs, pg(), "What a firewall does", "AWS · ACA M07 S23", [
        (0, "A firewall filters network traffic by rule — it decides what's allowed through."),
        (0, "Think of a security group like an apartment door: it only lets in the tenant with the right key — it protects one resource.",
            {"bold": True, "color": A2, "mark_color": A2}),
        (0, "Traffic is identified by address + port: 443 = HTTPS, 1433 = SQL Server, 3389 = RDP."),
        (0, "Least privilege — open only the ports the job needs, only to who needs them."),
    ], accent=A2)
    content_slide(prs, pg(), "Security groups", "AWS · ACF M05 S33–S35 · ACA M07 S24", [
        (0, "A security group is a virtual firewall attached to a resource (an instance or interface)."),
        (0, "Stateful — if you allow traffic in, the return traffic is automatically allowed out."),
        (0, "Allow-rules only (no deny). A new SG blocks all inbound until you add rules."),
        (0, "You can name another security group as the source — that's how you chain tiers (e.g. allow 443 only from the load balancer's SG).",
            {"bold": True, "color": A2, "mark_color": A2}),
    ], accent=A2)
    table_slide(prs, pg(), "The design's security groups", "least-privilege, chained tier-to-tier",
                ["Security group", "Inbound (allow)", "Outbound (allow)"],
                [["sg-alb", "HTTPS 443 from staff CIDR / VPN", "to sg-app"],
                 ["sg-app", "from sg-alb · RDP 3389 from MTS bastion", "SQL 1433 to sg-db · HTTPS via NAT · LDAPS to AD"],
                 ["sg-db", "SQL 1433 from sg-app", "(none needed)"]],
                accent=A2, col_widths=[2.4, 4.9, 4.6],
                note="Source = another security group, not an IP range — the tiers chain. The targets (ALB, EC2, RDS) are launched in Topic 8; here you build the rule shells.")

    # ----- C1+C2 build: demonstrate (recorded) then practice -----
    demo_slide(prs, pg(), "Build a VPC and its security groups", [
        (0, "Create a public and a private subnet, each with its own route table."),
        (0, "Create an Internet Gateway, attach it to the VPC, and configure the internet route."),
        (0, "Create a NAT gateway, assign an Elastic IP, and add the private-subnet route."),
        (0, "Create a web-server security group and a database security group."),
    ], accent=A2, source="ACA M07 · Creating a VPC (S30)")
    activity_slide(prs, pg(), "Build the network fabric", [
        (0, "In the AWS Academy lab, per the supplied Accounting design, build the network tier:", {"bold": True}),
        (1, "VPC 10.0.0.0/16; the three subnets (public-egress / private-app / private-data)"),
        (1, "Internet Gateway + NAT gateway + per-tier route tables (egress-only)"),
        (1, "the sg-alb → sg-app → sg-db security-group chain"),
        (0, "Capture named evidence as you go — VPC, subnets, route tables, SG rules — Region visible.",
            {"bold": True, "color": A2, "mark_color": A2}),
    ], "~25 min", accent=A2)

    # ===== C3 — Name resolution & connectivity =====
    divider_slide(prs, "03", "Found by name & proven to work", "DNS · connectivity testing", A3)
    # PRIMER + teach — authored from ACF M05 S49-S50
    visual_slide(prs, pg(), "How DNS works — and Route 53", "AWS · ACF M05 S49–S50", [
        (0, "DNS translates a name (ledgerline.yat.internal) into the IP address computers actually use."),
        (0, "A resolver asks the DNS hierarchy and gets the address back — we use names, not IPs, because addresses change."),
        (0, "Amazon Route 53 is AWS's highly available DNS service.",
            {"bold": True, "color": A3, "mark_color": A3}),
        (0, "Public hosted zone = internet-facing names; private hosted zone = names that resolve only inside your VPC."),
    ], ["AWS — Route 53 DNS resolution flow (ACF M05 S50)"], A3)
    content_slide(prs, pg(), "The design's name & certificate", "the supplied design · decision C8", [
        (0, "Ledgerline gets an internal hostname in a private hosted zone — staff-only, over the VPN; no public internet name."),
        (0, "An ACM TLS certificate secures HTTPS to that name."),
        (0, "The exact hostname + certificate domain is implementer decision C8 — confirm it with YAT ICT.",
            {"bold": True, "color": A3, "mark_color": A3}),
    ], accent=A3)
    content_slide(prs, pg(), "Prove it works — test connectivity", "AWS · ACA M07 S45, S41", [
        (0, "After building, confirm reachability: external access in (reach the service over the VPN) and access between tiers (app → db)."),
        (0, "Reachability Analyzer traces the path and names the blocking component when something can't connect."),
        (0, "VPC flow logs show ACCEPT / REJECT — a REJECT is usually a security-group rule or a missing route.",
            {"bold": True, "color": A3, "mark_color": A3}),
        (0, "Fix it and retest; capture the test as evidence. (Full app → db testing completes in Topic 8, once compute exists.)"),
    ], accent=A3)
    # LIVE demo — no recorded Route 53 demo fits a private hosted zone (source=None)
    demo_slide(prs, pg(), "Create a DNS record & test reachability", [
        (0, "In Route 53, create / confirm the private hosted zone for the internal domain."),
        (0, "Add the record for the Ledgerline name (and note the ACM certificate)."),
        (0, "From a test point, resolve the name and check reachability."),
        (0, "If it's blocked, read the flow logs / Reachability Analyzer and fix the SG or route."),
    ], accent=A3)
    activity_slide(prs, pg(), "Configure DNS + test connectivity", [
        (0, "In the lab, finish the network tier:", {"bold": True}),
        (1, "create the private hosted zone + record for the internal hostname (note the ACM cert)"),
        (1, "run reachability tests for what exists so far; record the result and any fix you made"),
        (0, "Capture the DNS config and the test result as evidence.",
            {"bold": True, "color": A3, "mark_color": A3}),
    ], "~15 min", accent=A3)
    takeaways_slide(prs, pg(), "Section 3 · Names & connectivity", [
        "DNS maps names → addresses; use a Route 53 private hosted zone for an internal name.",
        "Always test reachability and fix errors — flow logs + Reachability Analyzer show why traffic is blocked.",
        "The network tier is now ready for the workload to move in.",
    ], accent=A3)

    # ===== Close =====
    takeaways_slide(prs, pg(), "Topic 7 · Key takeaways", [
        "A VPC is your isolated network, split into tiered subnets across an AZ.",
        "Routing + IGW/NAT control internet reach — this design is egress-only.",
        "Security groups are stateful, least-privilege firewalls, chained tier-to-tier.",
        "DNS makes resources findable by name — a private hosted zone here.",
        "Build to the supplied design, test it, and evidence everything.",
    ], accent=GOLD)
    close_slide(prs, "Next: Topic 8 — the workload tier",
                ["EC2 + EBS, the load balancer + Auto Scaling group, RDS and S3 — the workload that moves into the network you just built.",
                 "Bring your evidence log."], accent=GOLD)

    save(prs, path)


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else OUT_DEFAULT
    build(out)
