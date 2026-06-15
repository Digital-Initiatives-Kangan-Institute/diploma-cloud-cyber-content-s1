#!/usr/bin/env python3
"""Topic 6 (Build foundations) — Kangan-branded teaching deck. First AT2 build Topic.

Reuse-first: the IAM, shared-responsibility and cloud-architecture teach slides are authored
FROM the AWS decks (ACF M04 Cloud Security; ACA M02 Intro Cloud Architecting) — their actual
teaching points — with image placeholders for the AWS diagrams to transfer. Bespoke is reserved
for the genuine gaps: the AT2 working-to-a-design discipline, Region-for-residency, evidence
discipline, the design's specific IAM groups, applying responsibility to the Accounting build,
and the demos. AWS practicals use teach -> DEMONSTRATE -> practice. Layouts in kangan_deck.py.

AWS source slides (isolate into source_slides/): ACA M02 S08; ACF M04 S05–S08, S11–S12, S18–S20,
S27–S29, S31. See slide_plan.md.

Usage:  python scripts/build_kangan_topic6_deck.py [output.pptx]
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kangan_deck import *  # noqa: F401,F403

OUT_DEFAULT = "S1-CL1-Cloud-Design-Build/delivery/topic_06/Topic_06_Slides.pptx"

A1, A2, A3 = MAGENTA, SKY, GREEN


def build(path):
    prs = new_deck()
    n = [0]
    def pg(): n[0] += 1; return n[0]

    title_slide(prs, "06", "Build foundations",
                "Implement the supplied design in AWS — account, identity, and the shared-responsibility line")

    content_slide(prs, pg(), "From advising to building", "AT1 was advice; now you build", [
        (0, "You implement a supplied design in the AWS lab — and evidence it."),
        (0, "New mode: work to a design you didn't write — read it, build it faithfully.",
            {"bold": True, "color": A1, "mark_color": A1}),
        (0, "New discipline: capture evidence as you go — the Deployment Report is built from it."),
        (0, "This Topic — the foundation tier: account & Region, identity & access, shared responsibility."),
        (0, "For every AWS task: watch the demo, then do it yourself."),
    ])

    # ===== C1 — Working to a supplied design =====
    divider_slide(prs, "01", "Working to a supplied design", "account · Region · evidence", A1)
    # AWS-sourced: ACA M02 S08 — cloud architecture: requirements -> design -> built structure
    visual_slide(prs, pg(), "Cloud architecture: requirements → design → build", "ACA M02", [
        (0, "Cloud architecture turns requirements into a structure:"),
        (1, "the customer sets the requirements · the architect produces the design · the delivery crew builds it"),
        (0, "In AT2 you're the delivery crew — the design is already done.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], ["AWS — cloud architecture: requirements→design→structure (ACA M02 S08)"], A1)
    content_slide(prs, pg(), "Working to a supplied design", "faithful implementation, not redesign", [
        (0, "Read the design end to end before you touch the console."),
        (0, "Build what it specifies; make and justify only the decisions it leaves open (C1–C8)."),
        (0, "“Implementer decision” = where your judgement is assessed.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], accent=A1)
    content_slide(prs, pg(), "Choose your Region — data residency first", "(applied from Topic 1)", [
        (0, "Region is the first build decision — and it's compliance, not preference."),
        (0, "The design mandates ap-southeast-2 (Sydney): financial records + PII stay onshore."),
        (0, "Set the console Region before creating anything — resources are Region-scoped."),
        (0, "Wrong-Region resources are wrong evidence — the assessor checks the Region in every screenshot.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], accent=A1)
    content_slide(prs, pg(), "Evidence discipline — capture as you build", "", [
        (0, "The Deployment Report is evidenced from what you capture live — you can't reconstruct it later."),
        (0, "Capture each named screenshot the template lists, as you build that resource (Region + the named resource visible)."),
        (0, "Export configs (IAM policies, SG rules, VPC) as you go → Appendix B."),
        (0, "Build → capture → move on. Evidence is part of the build, not a write-up afterwards.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], accent=A1)
    demo_slide(prs, pg(), "Set up the build workspace", [
        (0, "Sign in to the AWS Academy lab; set the Region to ap-southeast-2."),
        (0, "Confirm the identity you're building as."),
        (0, "Capture the first named screenshot (the Region selector) into the evidence log."),
        (0, "Show where configuration exports come from."),
    ], accent=A1)
    activity_slide(prs, pg(), "Set up your build workspace", [
        (0, "In the AWS Academy lab, set up to build the Accounting System foundation:", {"bold": True}),
        (1, "set the Region to ap-southeast-2 (confirm it — data residency)"),
        (1, "confirm your build identity"),
        (1, "capture your first named evidence screenshot (Region visible) into your evidence log"),
        (0, "Open the supplied Accounting Baseline Solution Design and skim it end to end."),
    ], "~15 min", accent=A1)
    takeaways_slide(prs, pg(), "Section 1 · Working to a supplied design", [
        "Architecture = requirements → design → build; in AT2 you're the builder, to a supplied design.",
        "Region first — ap-southeast-2 for data residency; visible in all evidence.",
        "Capture evidence live as you build — the report is made from it.",
    ], accent=A1)

    # ===== C2 — IAM (AWS-sourced from ACF M04 S18–S29) =====
    divider_slide(prs, "02", "Identity & access", "who can do what", A2)
    visual_slide(prs, pg(), "IAM — the essential components", "ACF M04", [
        (0, "IAM user — a person or application that authenticates to the account."),
        (0, "IAM group — a collection of users granted identical permissions."),
        (0, "IAM role — temporary permissions, assumable by a person, application or service (e.g. an EC2 instance)."),
        (0, "IAM policy — a JSON document defining which resources can be accessed, and how."),
    ], ["AWS — IAM components: user / group / role / policy (ACF M04 S18)"], A2)
    content_slide(prs, pg(), "Securing access — the best practices", "ACF M04", [
        (0, "Attach policies to groups; assign users to groups (don't attach policies to individuals)."),
        (0, "Least privilege — grant only the permissions the task needs; all access is denied by default."),
        (0, "MFA on human users; protect the root user (use it only when you must)."),
        (0, "Roles, not long-lived keys, for services — an EC2 instance assumes a role to reach RDS / S3.",
            {"bold": True, "color": A2, "mark_color": A2}),
    ], accent=A2)
    content_slide(prs, pg(), "The design's IAM model", "build these groups + role", [
        (0, "YAT-ICT-Admins — read-only infra + console post-handover"),
        (0, "MTS-Consultants — build admin"),
        (0, "Application-Service — EC2 instance role (RDS + S3 + CloudWatch)"),
        (0, "Finance-Auditors — read-only on logs / metrics / configs"),
        (0, "Enforce MFA on the human groups (Essential Eight).",
            {"bold": True, "color": A2, "mark_color": A2}),
    ], accent=A2)
    demo_slide(prs, pg(), "Build an IAM group, user & MFA", [
        (0, "Create a group; attach a least-privilege policy."),
        (0, "Create a user; add to the group; enable MFA."),
        (0, "Create the EC2 instance role (Application-Service) and attach its policy."),
        (0, "Capture the IAM evidence screenshot (groups list + a user with MFA)."),
    ], accent=A2, source="ACF M04 · IAM")
    activity_slide(prs, pg(), "Build the IAM model", [
        (0, "Per the Accounting Baseline Design, build the IAM foundation in the lab:", {"bold": True}),
        (1, "create the groups + the application-service role, with least-privilege policies"),
        (1, "create at least one user per human group; enforce MFA"),
        (1, "capture the IAM evidence (groups, a user with MFA, the role)"),
    ], "~30 min", accent=A2)
    takeaways_slide(prs, pg(), "Section 2 · Identity & access", [
        "IAM = users + groups (people), roles (services, temporary creds), policies (JSON permissions).",
        "Attach policies to groups; least privilege; MFA on humans; roles for services.",
        "Build the design's groups + role, and evidence it as you go.",
    ], accent=A2)

    # ===== C3 — Shared responsibility (AWS-sourced from ACF M04 S05–S12) =====
    divider_slide(prs, "03", "Shared responsibility", "who secures what", A3)
    visual_slide(prs, pg(), "The shared responsibility model", "ACF M04", [
        (0, "AWS — security OF the cloud: physical data centres, hardware, network, virtualization infrastructure."),
        (0, "You — security IN the cloud: the EC2 OS (patching), applications, security-group config, IAM, account management, and your data."),
        (0, "Knowing the line tells you what you must configure — and what you can rely on.",
            {"bold": True, "color": A3, "mark_color": A3}),
    ], ["AWS — shared responsibility model (ACF M04 S05)"], A3)
    content_slide(prs, pg(), "The line shifts with the service", "ACF M04", [
        (0, "IaaS (EC2) — you manage more: the OS, patching, security groups, access controls."),
        (0, "PaaS (RDS) — AWS handles the OS, database patching, firewall, DR; you manage your data + access."),
        (0, "More managed = more on AWS. The service type sets where the line falls.",
            {"bold": True, "color": A3, "mark_color": A3}),
    ], accent=A3)
    content_slide(prs, pg(), "Assigning responsibility on this build", "", [
        (0, "Map each layer of the Accounting build to its owner — AWS · YAT ICT · MTS (build) · end-users."),
        (0, "The supplied design's security section names the split; your job is to apply it:"),
        (1, "AWS patches the RDS host · YAT patches the EC2 OS · MTS sets the IAM + SG config at build"),
    ], accent=A3)
    activity_slide(prs, pg(), "Complete the shared-responsibility assignment", [
        (0, "No console build — an analysis task (in the style of the AWS scenario).", {"italic": True, "color": GREY1}),
        (0, "For each part of the Accounting foundation, name who is responsible — AWS or you (YAT/MTS):", {"bold": True}),
        (1, "EC2 OS patching · security-group settings · application config · IAM / MFA"),
        (1, "SQL Server patching on RDS · physical data-centre security · S3 bucket access config · data"),
        (0, "Per the supplied design + the shared-responsibility model. ~½ page — feeds your Deployment Report's security section."),
    ], "~15 min, then we discuss", accent=A3)
    takeaways_slide(prs, pg(), "Section 3 · Shared responsibility", [
        "AWS secures the cloud; you secure what's in it — OS, apps, IAM, config, data.",
        "The line shifts by service: IaaS = more on you; PaaS = more on AWS.",
        "Map every component to its owner — that's what you configure vs rely on.",
    ], accent=A3)

    # ===== Close =====
    close_slide(prs, "Foundation down — next, the network", [
        "You've set the build mode (work to the design, evidence as you go) and stood up the foundation: account/Region, IAM, shared responsibility.",
        "Everything else sits on this identity + access base.",
        "Next: the network & security base — VPC, subnets, security groups, DNS.",
    ])

    save(prs, path)


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else OUT_DEFAULT
    build(out)
