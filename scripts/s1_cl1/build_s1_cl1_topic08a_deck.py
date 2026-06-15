#!/usr/bin/env python3
"""Topic 8a (Workload tier — compute & elasticity) — Kangan-branded teaching deck. AT2 build.

Topic 8 is split into two decks (see coverage.md): 8a = C1 Compute (EC2+EBS) + C2 Elasticity
(ALB + Auto Scaling); 8b = C3 Database (RDS) + C4 Storage (S3+Glacier). Still one Topic 8.

Reuse-first: EC2/EBS authored from ACF M06 (S9-S35); elasticity/ASG from ACA M10 (S18-S26);
ALB from ACA M07/M10. Recorded demos: EC2 (ACF M06 S35), Auto Scaling policies (ACA M10 S26).
Bespoke fills the working-to-design framing, the design's specifics, and evidence/test discipline.
Primer-first; AWS practicals teach -> DEMONSTRATE (recorded) -> practice. Layouts in kangan_deck.py.

Usage:  python scripts/build_kangan_topic8a_deck.py [output.pptx]
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kangan_deck import *  # noqa: F401,F403

OUT_DEFAULT = "S1-CL1-Cloud-Design-Build/delivery/topic_08/Topic_08a_Slides.pptx"

A1, A2, A3 = MAGENTA, SKY, GREEN


def build(path):
    prs = new_deck()
    n = [0]
    def pg(): n[0] += 1; return n[0]

    title_slide(prs, "08a", "The workload tier — compute & elasticity",
                "Launch the application server, give it storage, and put it behind a load balancer that scales")

    content_slide(prs, pg(), "Filling the network", "the workload moves in", [
        (0, "Topic 7 laid the network; now the workload goes inside it."),
        (0, "8a — compute + elasticity (this deck); 8b — the managed database + storage.",
            {"bold": True, "color": A1, "mark_color": A1}),
        (0, "Still building the supplied design, still capturing evidence as you go."),
        (0, "For every AWS build task: watch the recorded demo, then do it yourself."),
    ])

    # ===== C1 — Compute (EC2 + EBS) =====
    divider_slide(prs, "01", "Compute — the application server", "EC2 + EBS", A1)
    content_slide(prs, pg(), "What a server is — and a virtual one", "the fundamentals", [
        (0, "A server is a computer that runs your application for others to use."),
        (0, "Its size is four dimensions: CPU (processing), memory (RAM), disk (storage), network bandwidth."),
        (0, "A virtual machine (VM) is a software-defined server — you rent one and size it to the workload.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], accent=A1)
    content_slide(prs, pg(), "Amazon EC2", "AWS · ACF M06 S10", [
        (0, "Amazon EC2 provides resizable virtual machines — called instances — in the cloud."),
        (0, "You get full control of the guest OS (Windows or Linux)."),
        (0, "You launch an instance from an Amazon Machine Image (AMI) into a subnet, ready in minutes."),
        (0, "You control traffic to and from it with security groups.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], accent=A1)
    content_slide(prs, pg(), "Launching an instance — the key choices", "AWS · ACF M06 S11–S26", [
        (0, "AMI — the template (OS + any pre-installed software)."),
        (0, "Instance type — family.generation.size (e.g. m6i.large) sets CPU / RAM / storage / network."),
        (0, "Network — which VPC and subnet; IAM role — an instance profile so the app can call AWS services."),
        (0, "User data — a first-boot script; storage — root + data volumes; tags; security group; key pair."),
    ], accent=A1)
    content_slide(prs, pg(), "Storage on the instance — EBS (block)", "primer + AWS · ACF M06 S22", [
        (0, "Block storage = a virtual disk attached to one instance (like a drive in a PC)."),
        (0, "Amazon EBS is durable block storage — stop and start the instance and the data is still there.",
            {"bold": True, "color": A1, "mark_color": A1}),
        (0, "(Instance store is ephemeral — it's lost when the instance stops.)"),
        (0, "gp3 SSD volumes; you can resize or change type without downtime."),
    ], accent=A1)
    content_slide(prs, pg(), "The compute you'll build", "the supplied design", [
        (0, "EC2 Windows Server 2016 (m6i.large*, a C1 implementer decision), in private-app-a, no public IP."),
        (0, "An instance role grants it access to RDS, S3 and CloudWatch — no stored keys."),
        (0, "EBS: gp3 root 80 GB + a gp3 data volume (footprint + 12-month growth + headroom)."),
        (0, "Attach sg-app; tag per the naming standard. (*= implementer decision.)"),
    ], accent=A1)
    demo_slide(prs, pg(), "Launch an EC2 instance", [
        (0, "Use the Launch Instance Wizard: choose the AMI and instance type."),
        (0, "Set the network (VPC/subnet), IAM role, storage volumes, tags and security group."),
        (0, "Launch, then view the instance, its volumes and monitoring."),
        (0, "Resize the instance type / root volume to see how it changes."),
    ], accent=A1, source="ACF M06 · EC2 (S35)")
    activity_slide(prs, pg(), "Launch the Ledgerline server", [
        (0, "In the lab, per the supplied design, launch the application server:", {"bold": True}),
        (1, "AMI Windows Server 2016; instance type per the design; into private-app-a (no public IP)"),
        (1, "attach the instance role + sg-app; add the gp3 data volume; tag it"),
        (0, "Capture named evidence — the instance, its volumes, the Region.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], "~25 min", accent=A1)
    takeaways_slide(prs, pg(), "Section 1 · Compute", [
        "EC2 = a resizable virtual machine, launched from an AMI into your subnet.",
        "The instance type sets CPU / RAM / storage / network — size it to the workload.",
        "EBS = durable block storage attached to the instance (survives stop/start).",
        "Build to the supplied design; no public IP; capture evidence as you go.",
    ], accent=A1)

    # ===== C2 — Elasticity (ALB + Auto Scaling) =====
    divider_slide(prs, "02", "Elasticity — load balancing & scaling", "ALB + Auto Scaling", A2)
    content_slide(prs, pg(), "Load balancing & scaling", "primer + AWS · ACA M10 S19", [
        (0, "A load balancer spreads incoming traffic across several instances and checks their health."),
        (0, "Elasticity = the infrastructure grows and shrinks as demand changes."),
        (0, "Vertical scaling = replace with a bigger instance; horizontal scaling = add more instances.",
            {"bold": True, "color": A2, "mark_color": A2}),
        (0, "Horizontal scaling is the cloud way — and the basis of high availability later."),
    ], accent=A2)
    visual_slide(prs, pg(), "The Application Load Balancer", "AWS · ACA M07 / M10", [
        (0, "An ALB receives requests on a listener (here HTTPS:443)."),
        (0, "It forwards them to a target group and routes only to healthy targets (health checks)."),
        (0, "It can be internet-facing or internal (this design is internal — staff over the VPN).",
            {"bold": True, "color": A2, "mark_color": A2}),
    ], ["AWS — load balancer → target group → instances"], A2)
    visual_slide(prs, pg(), "Auto Scaling groups", "AWS · ACA M10 S20–S24", [
        (0, "An Auto Scaling group (ASG) manages a fleet of instances from a launch template."),
        (0, "Capacity settings: minimum / desired / maximum; it replaces unhealthy instances automatically."),
        (0, "Scaling policies — scheduled, dynamic (target-tracking), or step — adjust capacity."),
        (0, "It integrates with the ALB's health checks across Availability Zones.",
            {"bold": True, "color": A2, "mark_color": A2}),
    ], ["AWS — horizontal scaling with an ASG (ACA M10 S22)"], A2)
    content_slide(prs, pg(), "The elasticity you'll build", "the supplied design", [
        (0, "Internal ALB, HTTPS:443 listener → a target group of the Ledgerline instances."),
        (0, "Auto Scaling Group: min 1 / desired 1 / max 2; target-tracking on CPU at 70%; 300 s cooldown."),
        (0, "Health checks: ELB + EC2 — an unhealthy instance is replaced."),
        (0, "This is baseline elasticity, single-AZ — cross-AZ resilience (HA) comes in AT3.",
            {"bold": True, "color": A2, "mark_color": A2}),
    ], accent=A2)
    demo_slide(prs, pg(), "Create an Auto Scaling policy", [
        (0, "Create a launch template and an Auto Scaling group with min / desired / max."),
        (0, "Attach a target-tracking scaling policy (e.g. keep average CPU near a target)."),
        (0, "Watch the group launch and register instances with the load balancer."),
    ], accent=A2, source="ACA M10 · Scaling policies (S26)")
    activity_slide(prs, pg(), "Behind the ALB + ASG — then test scaling", [
        (0, "In the lab, per the design:", {"bold": True}),
        (1, "create the internal ALB + target group + HTTPS:443 listener"),
        (1, "create the launch template + ASG (min 1 / max 2, target-tracking CPU 70%)"),
        (0, "Test scaling: drive the metric (or change desired capacity), watch it scale out then in; fix any errors.",
            {"bold": True, "color": A2, "mark_color": A2}),
        (0, "Capture evidence — the ALB, target health, the ASG, and the scaling event."),
    ], "~25 min", accent=A2)
    takeaways_slide(prs, pg(), "Section 2 · Elasticity", [
        "A load balancer spreads traffic and routes only to healthy targets.",
        "An Auto Scaling group scales horizontally between min and max on a policy.",
        "Test that it scales and self-heals — that's PC evidence, not an optional extra.",
        "Baseline here is single-AZ; cross-AZ high availability is AT3.",
    ], accent=A2)

    # ===== Close =====
    takeaways_slide(prs, pg(), "Topic 8a · Key takeaways", [
        "EC2 is a virtual machine launched from an AMI; the instance type sizes it.",
        "EBS gives the instance durable block storage.",
        "An Application Load Balancer spreads load and health-checks the targets.",
        "An Auto Scaling group scales horizontally to a policy and replaces failures.",
        "Build to the supplied design, test the scaling, and evidence everything.",
    ], accent=GOLD)
    close_slide(prs, "Next: Topic 8b — the data tier",
                ["The managed database (Amazon RDS) and object / archive storage (Amazon S3 + Glacier) — the data the application relies on.",
                 "Bring your evidence log."], accent=GOLD)

    save(prs, path)


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else OUT_DEFAULT
    build(out)
