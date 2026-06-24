# Topic 8 — The workload tier · Coverage

**Topic 8 of 14** · **AT2 content Topic** (cloud build — workload tier) · **the largest Topic** (likely spans >1 session) · teaching source: **mostly AWS-sourced** — ACF M06 (Compute), ACF M07 (Storage), ACF M08 (Databases), ACA M05 (Compute layer), ACA M06 (Database layer), ACA M04 (S3), ACA M10 (ELB/Auto Scaling) carry the teaching + the recorded build demos; **bespoke** fills the working-to-design framing, the design's specifics, and the evidence/test discipline.

The coverage spec — what this Topic must cover, in UoC and AT2 terms. `slide_plan.md` and the deck are built to satisfy it.

> **The heart of the build.** Topic 7 laid the network; Topic 8 puts the **workload** inside it — compute, elasticity, the managed database, and object/archive storage. This Topic carries the **core ICTCLD401 Performance Evidence** ("configure compute, storage, database and autoscaling resources within a virtual network"). Students keep building the **supplied design** and capturing **evidence**. AT2 = ICTCLD401 (primary) + ICTCLD502 (partial).

> **Built as two decks (2026-06-03):** **8a** = C1 Compute (EC2+EBS) + C2 Elasticity (ALB+ASG) → `Topic_08a_Slides.pptx`; **8b** = C3 Database (RDS) + C4 Storage (S3+Glacier) → `Topic_08b_Slides.pptx`. Still **one Topic 8** in the spine/numbering — split only for build/review manageability; combinable into one deck later if wanted.

---

## Teaching-design note — primer-first (no assumed baseline)

Per the standing rule, every concept gets a vendor-neutral **primer** before the AWS-context slide: what a **server / virtual machine** is and how it's sized; **block vs object vs archive** storage; **load balancing** and **vertical vs horizontal scaling**; what a **relational database** is and **self-hosted vs managed**. Reuse-first still governs the primer — pin an AWS "basics" slide where one teaches the fundamental; bespoke only for genuine gaps. Per-concept shape: **primer → AWS-context teach → (recorded) demo → practice**.

---

## What this Topic must cover

The **workload tier** built into the Topic 7 network, to the supplied design, evidenced as built. Four components:

- **C1 — Compute (EC2 + EBS).** What a server/VM is + sizing (primer) → EC2 (AMI, instance families/types, launch into `private-app-a`) + EBS (block storage, gp3 volumes, attach/size) → launch the Ledgerline instance with its root + data volumes. *(ICTCLD401 PC 2.3, PC 2.4.)*
- **C2 — Elasticity (ALB + Auto Scaling).** Load balancing + vertical-vs-horizontal scaling (primer) → the internal ALB (target group, listener, health check) + an Auto Scaling Group (launch template, min/desired/max, target-tracking policy) → place the instance behind the ALB in an ASG, and **test scaling**. *(ICTCLD401 PC 3.1, PC 3.2.)*
- **C3 — Managed database (RDS).** Relational-DB basics + self-hosted-vs-managed (primer) → Amazon RDS (engine, instance class, storage, automated backups, encryption; Multi-AZ named but **deferred to AT3**) → provision the (empty) RDS for SQL Server instance in `private-data-a`. *(ICTCLD401 PC 2.5.)*
- **C4 — Object & archive storage (S3 + Glacier).** Object vs block vs archive storage (primer) → Amazon S3 (buckets, block-public-access, versioning, encryption) + **lifecycle to Glacier** (the 7-year financial-records retention) + Object Lock → create the Documents + Backups buckets per the design. *(ICTCLD401 KE — storage options; storage backups and lifecycle.)*

**Connectivity testing (PC 2.6) completes here:** with compute + database now present, test **app → database** reachability (begun in Topic 7) and fix errors.

---

## 1. UoC mapping

UoC **taught / developed** in this Topic:

| UoC item | Descriptor | Component |
|---|---|---|
| [ICTCLD401 PC 2.3] | Create virtual machine according to business processing and operating system requirements | C1 |
| [ICTCLD401 PC 2.4] | Define, add and expand storage on virtual machine | C1 |
| [ICTCLD401 PC 2.5] | Deploy a managed database within virtual network | C3 |
| [ICTCLD401 PC 3.1] | Configure and apply autoscaling to virtual machines to scale by business metrics | C2 |
| [ICTCLD401 PC 3.2] | Test automatic scaling and fix errors as required | C2 |
| [ICTCLD401 PC 2.6] | Test access between resources within virtual network and fix errors (app→db portion) | C1 · C3 *(completes T7)* |
| [ICTCLD401 KE 5] | VM sizing — CPU, memory, storage, network bandwidth | C1 |
| [ICTCLD401 KE 6] | Virtual vs physical machines | C1 *(primer)* |
| [ICTCLD401 KE 5, 6] | Load balancing and autoscaling; vertical vs horizontal scaling | C2 |
| [ICTCLD401 KE 6] | Relational / data-warehouse / NoSQL; self-hosted, managed, cloud-native databases | C3 |
| [ICTCLD401 KE 6] | Storage options — block, object, archive, network filesystems | C1 (block) · C4 (object/archive) |
| [ICTCLD401 KE 5] | Storage backups and lifecycle | C3 (RDS backups) · C4 (S3 lifecycle) |
| [ICTCLD401 PE 2] | **Configure compute, storage, database and autoscaling resources within a virtual network** | C1–C4 *(core PE)* |

> **AT2 marking home: A3 (workload-tier build narrative)** *(confirm — Topic 6 = A2 foundation; this is the workload tier)*. AT2 Deployment Report sections **§4.5 Compute · §4.6 Load balancing · §4.7 Database · §4.8 Storage**. AT2 build-topic refs **T6 (EC2) · T7 (ALB+ASG) · T8 (RDS) · T9 (S3)**.

UoC **applied** here but **taught earlier** (not re-taught):

| What | Where |
|---|---|
| The VPC / subnets / security groups the workload launches into | Topic 7 (built there; the ALB/EC2/RDS now fill the SG shells) |
| Account/Region + evidence-capture discipline | Topic 6 |
| IaaS/PaaS/SaaS framing (EC2 = IaaS, RDS = PaaS) | Topic 1 |

---

## 2. AT2 equivalence / alignment

| AT2 element | Criterion | How Topic 8 aligns |
|---|---|---|
| **§4.5 Compute (EC2 + Auto Scaling)** | A3 | C1 + C2 — EC2 + EBS launched to the design; evidenced in Appendix A/B. |
| **§4.6 Load balancing (ALB)** | A3 | C2 — internal ALB + target group + health check; ASG behind it; scaling tested. |
| **§4.7 Database (RDS)** | A3 | C3 — RDS provisioned to the design (empty instance; schema/data is YAT ICT's job). |
| **§4.8 Storage (EBS + S3)** | A3 | C1 (EBS) + C4 (S3 buckets, versioning, encryption, Glacier lifecycle for 7-yr retention). |
| **Connectivity + scaling testing; fix errors** | A3 · A10 | C2 (scaling test) + C1/C3 (app→db reachability) — captured as evidence. |

**Practice-activity alignment:** students build the **workload tier** (EC2/EBS → ALB+ASG → RDS → S3) of the **practice** engagement (Accounting / Ledgerline) in the AWS Academy lab, to the supplied Solution Design, capturing evidence — mirroring the AT2 workload build on the LMS.

**The design students build to (workload sections):** EC2 Windows Server 2016 (m6i.large*, C1) in `private-app-a` + EBS gp3 root 80 GB & data volume; ASG min 1 / desired 1 / max 2, target-tracking CPU 70%; **internal** ALB HTTPS:443 → the ASG target group; **RDS for SQL Server Standard** (db.m6i.large*, C2; licence model C3), Multi-AZ **off** at baseline, automated backups RPO ≤ 1 h; **S3** Documents bucket (→ Glacier, 7-yr) + Backups bucket, versioning + encryption + block-public-access. *(\*= implementer decision.)*

---

## Out of scope for this Topic (covered elsewhere)

- **CloudWatch monitoring, config-decision justification, full testing/validation discipline** → **Topic 9** (§4.10). *(Scaling is tested here as PC 3.2; the monitoring baseline is Topic 9.)*
- **Writing the Deployment Report** → **Topic 10** (evidence is captured here; the report is written there).
- **HA / Multi-AZ / cross-AZ resilience / read replicas / DNS failover** → **AT3** (explicitly deferred; Multi-AZ is named but disabled at baseline).
- **DynamoDB / NoSQL, EFS, Spot instances, S3 Transfer Acceleration** → out of YAT/Accounting scope (named only to contrast; not built).
- **The network (VPC/subnets/SGs/DNS) the workload sits in** → **Topic 7** (applied here, not re-taught).
- **What these services are conceptually** beyond the primers → applied here, built not re-taught.

---

## Coverage checklist (for `slide_plan.md` + the deck to satisfy)

- [ ] Every UoC item in §1 (taught/developed) is taught in the deck — especially the **core PE** (compute + storage + database + autoscaling in a VPC).
- [ ] Each of C1–C4 has **primer → AWS-context teach → (recorded) demo → practice activity** (hands-on in the lab).
- [ ] A vendor-neutral **primer precedes every concept** — VM/sizing, block-vs-object-vs-archive, load-balancing & scaling, relational/managed DB — reusing AWS "basics" slides where they teach the fundamental.
- [ ] AWS teaching slices pinned (ACF M06/M07/M08 · ACA M04/M05/M06/M10); bespoke covers working-to-design + the design's specifics + evidence/test discipline.
- [ ] **Demos are recorded AWS demos** where one fits (EC2, EBS, ASG, RDS, S3, S3-lifecycle, S3-versioning all have recorded demos — see `planning/aws-recorded-demos-catalogue.md`); live demo only if none fits.
- [ ] **PC 3.2** — scaling is **tested** (trigger a scale event; observe; fix errors) and evidenced (C2).
- [ ] **PC 2.6** — app→database reachability tested and fixed (completes the Topic 7 connectivity test).
- [ ] EBS taught as **block** storage on the VM (C1); S3 taught as **object/archive** storage with **lifecycle to Glacier** for the 7-year retention (C4) — the block-vs-object distinction is explicit.
- [ ] RDS taught as a **managed** database (backups/patching handled) vs self-hosted (C3); MTS provisions an **empty** instance (schema/data = YAT ICT).
- [ ] Depth ceiling respected: build the workload per the supplied design — **single-AZ baseline, Multi-AZ off, ASG min 1/max 2** (elasticity intro, not HA). HA deferred to AT3.
- [ ] AT2 alignment (§2) explicit enough that a student leaving this Topic could build + evidence the full workload tier.
