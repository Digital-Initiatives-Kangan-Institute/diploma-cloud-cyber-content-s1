#!/usr/bin/env python3
"""Topic 8b (Workload tier — database & storage) — Kangan-branded teaching deck. AT2 build.

Second half of Topic 8 (see coverage.md): 8b = C3 Database (RDS) + C4 Storage (S3 + Glacier).

Reuse-first: RDS authored from ACF M08 (S6-S29, managed vs unmanaged, instance/storage, engines,
recorded RDS demo S22) + ACA M06; storage from ACF M07 (block-vs-object S7, S3 S22-S35, Glacier +
lifecycle S44-S55) + ACA M04 (lifecycle S36, versioning S43). Bespoke fills the design's specifics
and the evidence/test discipline. Primer-first; recorded demos throughout. Layouts in kangan_deck.py.

Usage:  python scripts/build_kangan_topic8b_deck.py [output.pptx]
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kangan_deck import *  # noqa: F401,F403

OUT_DEFAULT = "S1-CL1-Cloud-Design-Build/delivery/topic_08/Topic_08b_Slides.pptx"

A1, A2, A3 = MAGENTA, SKY, GREEN


def build(path):
    prs = new_deck()
    n = [0]
    def pg(): n[0] += 1; return n[0]

    title_slide(prs, "08b", "The workload tier — data & storage",
                "Provision the managed database, and the object & archive storage the application relies on")

    content_slide(prs, pg(), "The data tier", "compute is built — now the data", [
        (0, "8a launched the compute and put it behind a scaling load balancer."),
        (0, "8b adds the data: a managed database (Amazon RDS) and object/archive storage (Amazon S3 + Glacier).",
            {"bold": True, "color": A1, "mark_color": A1}),
        (0, "Still building the supplied design, still capturing evidence."),
        (0, "Watch the recorded demo, then do it yourself."),
    ])

    # ===== C3 — Managed database (RDS) =====
    divider_slide(prs, "01", "The managed database", "Amazon RDS", A1)
    content_slide(prs, pg(), "Databases, and who runs them", "the fundamentals", [
        (0, "A relational database stores structured data in tables, queried with SQL."),
        (0, "Someone must run it: install + patch the OS and database, take backups, secure it, scale it."),
        (0, "Self-hosted = you do all of that (e.g. on an EC2 instance). Managed = the cloud provider does it.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], accent=A1)
    content_slide(prs, pg(), "Self-hosted vs managed — EC2 vs RDS", "AWS · ACF M08 S6–S10 · M06 S44", [
        (0, "Run it yourself on EC2: full control of the engine and OS — but you own all the admin work."),
        (0, "Amazon RDS is a managed service: AWS handles OS/database install + patching, automated backups, scaling and availability.",
            {"bold": True, "color": A1, "mark_color": A1}),
        (0, "You keep responsibility for application optimisation and your data."),
        (0, "Trade-off: control vs effort — choose managed unless you need engine-level control."),
    ], accent=A1)
    content_slide(prs, pg(), "Amazon RDS", "AWS · ACF M08 S8–S29 · ACA M06", [
        (0, "RDS sets up and operates a relational database in the cloud; engines include Microsoft SQL Server."),
        (0, "A DB instance has an instance class (CPU/memory/network) and storage (gp3 SSD / provisioned IOPS)."),
        (0, "It runs in your VPC; automated backups give point-in-time restore; encryption at rest is available."),
        (0, "Multi-AZ gives a standby in another AZ for high availability — named here, but deferred to AT3.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], accent=A1)
    content_slide(prs, pg(), "The database you'll build", "the supplied design", [
        (0, "Amazon RDS for SQL Server, Standard edition (preserves the existing engine + data)."),
        (0, "Instance class db.m6i.large* (C2 decision); gp3 storage ~22 GB + growth; in private-data-a, sg-db, not public."),
        (0, "Multi-AZ off at baseline; KMS encryption on; automated backups + tx-log backups to RPO ≤ 1 hour."),
        (0, "MTS provisions an EMPTY instance — schema and data migration are YAT ICT's responsibility. (*= implementer; licence model = C3.)",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], accent=A1)
    demo_slide(prs, pg(), "Provision an RDS database", [
        (0, "Create a DB subnet group and the database security group."),
        (0, "Launch an RDS DB instance: choose the engine, instance class, storage and backup settings."),
        (0, "Connect to the database from the application tier to confirm it's reachable."),
    ], accent=A1, source="ACF M08 · RDS console (S22) + ACA M06 · backups (S37)")
    activity_slide(prs, pg(), "Provision the Ledgerline database", [
        (0, "In the lab, per the design, provision the database:", {"bold": True}),
        (1, "RDS for SQL Server (class + storage per the design); in private-data-a with sg-db; not public"),
        (1, "enable automated backups + KMS encryption; leave Multi-AZ off (baseline)"),
        (0, "Test app → database connectivity (completes the Topic 7 connectivity test) and fix any errors.",
            {"bold": True, "color": A1, "mark_color": A1}),
        (0, "Capture evidence — the instance, its network/SG, backup + encryption settings."),
    ], "~20 min", accent=A1)
    takeaways_slide(prs, pg(), "Section 1 · Managed database", [
        "A managed database (RDS) offloads OS/engine patching, backups, scaling and availability.",
        "Place it in a private subnet, lock it to the app's security group, encrypt it.",
        "MTS delivers an empty instance — schema and data are the customer's job.",
        "Multi-AZ is the HA option — deferred to AT3; baseline is single-AZ.",
    ], accent=A1)

    # ===== C4 — Object & archive storage (S3 + Glacier) =====
    divider_slide(prs, "02", "Object & archive storage", "Amazon S3 + Glacier", A2)
    content_slide(prs, pg(), "Block vs object vs archive", "primer + AWS · ACF M07 S7", [
        (0, "Block storage = a virtual disk attached to one instance (EBS) — change one block of a file."),
        (0, "Object storage = whole files (objects) + metadata, reached by API, virtually unlimited (S3).",
            {"bold": True, "color": A2, "mark_color": A2}),
        (0, "Archive storage = very cheap, slow to retrieve, for long-term retention (Glacier)."),
        (0, "Match the storage to the job — performance and cost both depend on it."),
    ], accent=A2)
    content_slide(prs, pg(), "Amazon S3", "AWS · ACF M07 S22–S34", [
        (0, "S3 stores objects in buckets; virtually unlimited; designed for 11 9s of durability."),
        (0, "Buckets are Region-scoped and globally-unique-named; access is granular (IAM + bucket settings)."),
        (0, "Block public access, encrypt (SSE), and enable versioning to protect objects.",
            {"bold": True, "color": A2, "mark_color": A2}),
        (0, "Common uses: backups, application assets, document stores."),
    ], accent=A2)
    content_slide(prs, pg(), "Lifecycle to Glacier — retention", "AWS · ACF M07 S44–S50 · ACA M04 S36", [
        (0, "Amazon S3 Glacier is extremely low-cost archive storage; retrieval takes minutes to hours."),
        (0, "A lifecycle rule transitions objects from S3 to Glacier by age — automatic, cheaper over time.",
            {"bold": True, "color": A2, "mark_color": A2}),
        (0, "Object Lock enforces write-once retention — for records that must not be altered or deleted."),
        (0, "This is how the design meets the 7-year financial-records retention."),
    ], accent=A2)
    content_slide(prs, pg(), "The storage you'll build", "the supplied design", [
        (0, "Documents bucket — scanned invoices / POs / supporting docs; lifecycle to Glacier for the 7-year hold."),
        (0, "Backups bucket — off-instance SQL backup exports and file snapshots."),
        (0, "Both buckets: block all public access; SSE(-KMS) encryption; versioning on; access logging.",
            {"bold": True, "color": A2, "mark_color": A2}),
        (0, "Object Lock considered for the financial-records hold."),
    ], accent=A2)
    demo_slide(prs, pg(), "S3 buckets, versioning & lifecycle", [
        (0, "Create a bucket; block public access; enable encryption and versioning."),
        (0, "Add a lifecycle rule to transition objects to Glacier after an age threshold."),
        (0, "(Glacier is the archive tier the lifecycle rule targets.)"),
    ], accent=A2, source="ACA M04 · S3 lifecycle (S36) + versioning (S43) · ACF M07 S35/S55")
    activity_slide(prs, pg(), "Create the buckets per the design", [
        (0, "In the lab, per the design, create the storage:", {"bold": True}),
        (1, "the Documents bucket and the Backups bucket"),
        (1, "block public access; enable SSE encryption + versioning + access logging"),
        (1, "add the lifecycle rule transitioning Documents objects to Glacier (7-year retention)"),
        (0, "Capture evidence — bucket settings, encryption, versioning, the lifecycle rule.",
            {"bold": True, "color": A2, "mark_color": A2}),
    ], "~15 min", accent=A2)
    takeaways_slide(prs, pg(), "Section 2 · Object & archive storage", [
        "S3 is durable object storage in buckets; block public access, encrypt, version.",
        "Lifecycle rules move objects to Glacier to meet long retention cheaply.",
        "Object Lock enforces write-once retention for financial records.",
        "Build the buckets to the design and evidence the settings.",
    ], accent=A2)

    # ===== Close =====
    takeaways_slide(prs, pg(), "Topic 8 · Key takeaways", [
        "The whole workload tier now lives in the Topic 7 network: compute, elasticity, database, storage.",
        "EC2 + EBS run the app; the ALB + ASG make it scale and self-heal.",
        "RDS gives a managed database; S3 + Glacier give durable object & archive storage.",
        "Everything is built to the supplied design, tested, and evidenced.",
        "Single-AZ baseline throughout — high availability is the AT3 story.",
    ], accent=GOLD)
    close_slide(prs, "Next: Topic 9 — operability & justification",
                ["Monitoring the build with CloudWatch, validating it works, and justifying the configuration decisions against the workload.",
                 "Bring your evidence log — Topic 10 turns it into the Deployment Report."], accent=GOLD)

    save(prs, path)


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else OUT_DEFAULT
    build(out)
