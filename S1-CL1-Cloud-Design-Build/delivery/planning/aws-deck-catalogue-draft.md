# AWS Academy deck catalogue → CL1 chunk mapping (DRAFT)

> **⚠ Terminology — read first (rename settled 2026-05-31: `AT → Topic → chunk`).** This draft predates the rename. Where it maps decks to our **"topics"** (T1, T2, …), read **chunks**. (AWS deck names like *"ICTCLD502 Topic 1"* are the vendor's own module titles — unrelated to our Topic/chunk levels.) The live planning spine is `cl1-teaching-topics-draft.md`.

**Status:** DRAFT, 2026-05-31. Catalogues the existing AWS Academy / bespoke instructor decks Kangan is licensed to use, and maps each to the AT1/AT2/AT3 topics from the decomposition drafts. Per Tim's steer: **where one deck already covers several of our topics, treat those topics as a candidate group to teach together** (a starting point, not locked).

**Source:** `original-materials/AWS-Instructor Presentations/…` (the `.pptx` decks are the source of truth — agendas extracted from slides 1–8 of each). **Licence note:** the AWS Academy decks are marked *present but do not distribute to students* — instructor-facing only.

**Scope / exclusions:**
- The folder has **nested duplication** — the complete ACA set (incl. M11, M17) is in the deepest copy; ACF + the bespoke 502 decks are in the middle copy. Catalogue below dedupes to the canonical set.
- **`Bespoke-Presentations/` (DR Topics 1–4) and `_Topic – Session plan … ICTCLD501.xlsx` belong to CL2 (Cloud Disaster Recovery), not CL1** — excluded here.
- **ACF M00 (course intro)** = onboarding (S1); **ACA M17 (Bridging to Certification)** = optional SAA enrichment, no CL1 assessment coverage.

---

## Three deck families

| Family | What it is | Best fit |
|---|---|---|
| **ACF** — AWS Academy Cloud Foundations, Modules 00–10 | Breadth-first introduction to AWS services | The cloud-knowledge **foundations** (AT1 T1–T5) + first pass at the AT2 build services |
| **ACA v3** — AWS Academy Cloud Architecting, M01–M11, M16, M17 | Architect-level, "as a cloud architect I need to…" build depth | The AT2 **build** (deeper than ACF) + AT3 **HA** (M10) + CloudFormation (M11) |
| **ICTCLD502 bespoke** — Topics 1–4 | Kangan-authored HA decks, purpose-built for the 502 unit | The AT3 **HA design + implementation** (near 1:1) |

---

## Deck catalogue (deck → our topics)

### ACF — Cloud Foundations

| Deck | Covers | Maps to |
|---|---|---|
| M01 Cloud Concepts Overview | cloud models, advantages, AWS service categories, AWS CAF | **AT1 T1** (cloud fundamentals/deployment models) · AT1 T2 · AT1 T3 |
| M02 Cloud Economics and Billing | pricing fundamentals, RIs, TCO; **AWS Pricing Calculator slide (S20) + hands-on group activity (S22): build a cost estimate from supplied specs and report back** | **AT1 T5** (cost models) · **AT1 T11** (CBA): the calculator activity is **directly reusable** as the AWS-pricing-research scaffold (feeds AT1 Appendix 3); only the CBA *assembly* method (5-yr two-option comparison, avoided-downtime, Year-1 cash-flow, sensitivity) remains bespoke |
| M03 AWS Global Infrastructure | Regions, AZs, edge; **region selection incl. data governance/residency** | AT2 T2 (region discipline) · AT1 T6 (data-residency factor) · AT3 T1 (AZ basis of HA) |
| M04 AWS Cloud Security | **shared responsibility model**, IAM users/groups/roles, securing accounts/data | **AT2 T3** (IAM) · **AT2 T11** (shared responsibility) · AT1 T2 |
| M05 Networking and Content Delivery | **VPC, subnets, security groups**, Route 53, CloudFront | **AT2 T4** (VPC) · **AT2 T5** (security groups) · **AT2 T12** (DNS/Route 53) |
| M06 Compute | **EC2**, EC2 cost optimisation, containers, Lambda, Beanstalk | **AT2 T6** (EC2) · AT1 T2 (IaaS/PaaS/SaaS) · AT1 T5 (EC2 pricing) |
| M07 Storage | **EBS, S3, Glacier**; block vs object | **AT2 T6** (EBS) · **AT2 T9** (S3/Glacier) |
| M08 Databases | **RDS**, DynamoDB, Aurora; managed vs unmanaged | **AT2 T8** (RDS) · AT1 T2/T3 (managed services) |
| M09 Cloud Architecture | **AWS Well-Architected Framework** (6 pillars), reliability & HA, Trusted Advisor | **AT1 T4** (industry standards/WAF) · AT3 T1 (reliability/HA concept) · AT2 T13 (WAF principles) |
| M10 Automatic Scaling and Monitoring | **ELB, CloudWatch, EC2 Auto Scaling** | **AT2 T7** (ALB+ASG) · **AT2 T10** (CloudWatch) · AT3 T4 · AT3 T12 |

### ACA v3 — Cloud Architecting

| Deck | Covers | Maps to |
|---|---|---|
| M01 Welcome | café business case, role of a cloud architect | Onboarding / engagement-role framing (S1; light AT1 context) |
| M02 Introducing Cloud Architecting | cloud architecture, **WAF**, best practices, global infra | AT1 T4 (standards/WAF) · **AT2 T1** (working to a design) · AT2 T13 |
| M03 Securing Access | **IAM** users/groups/roles, IAM policies, shared responsibility | **AT2 T3** (IAM, deeper) · AT2 T11 |
| M04 Adding a Storage Layer with S3 | S3 deep — **lifecycle, versioning**, static site, WAF storage | **AT2 T9** (S3 lifecycle/versioning) |
| M05 Adding a Compute Layer (EC2) | EC2 in architecture, **AMIs, instance-type selection**, EC2 storage, pricing | **AT2 T6** (EC2/EBS) · **AT2 T13** (instance-type decision C1) · AT1 T5 |
| M06 Adding a Database Layer | **RDS** + advanced features, RDS Proxy, migration, **automated backup & read replicas** | **AT2 T8** (RDS) · AT2 T13 (RDS class C2) · AT3 T6 (Multi-AZ readiness) |
| M07 Creating a Networking Environment | **VPC, subnets, IGW, route tables, security groups**, network monitoring | **AT2 T4** (VPC) · **AT2 T5** (security groups) |
| M08 Connecting Networks | Transit Gateway, VPC peering, **Site-to-Site VPN**, Direct Connect | *Partial* — AT2 T1 (understanding the YAT design's campus Site-to-Site VPN); rest beyond CL1 build scope |
| M09 Securing User, Application & Data Access | IAM federation, multi-account, **KMS encryption at rest**, security services | *Partial* — AT2 T5 (encryption at rest); IAM federation/multi-account beyond CL1 scope |
| M10 Implementing Monitoring, Elasticity & **High Availability** | CloudWatch/EventBridge, **EC2 Auto Scaling, scaling databases, load balancers for HA, Route 53 DNS failover** | **AT2 T7/T10** · **AT3 T4** (LB+autoscaling for HA) · **AT3 T6** (HA design) · **AT3 T12** (availability monitoring) — core HA |
| M11 Automating Your Architecture | IaC, **AWS CloudFormation**, Quick Starts, Amazon Q | **AT3 T9** (deploy baseline via CloudFormation) · AT2 (IaC context, optional) |
| M16 Planning for Disaster | **RPO/RTO** strategies, DR patterns, backup | *Partial* — AT3 T1 / AT1 (recovery objectives, RPO/RTO); full DR patterns → CL2 |
| M17 Bridging to Certification | SAA-C03 exam prep | *Optional enrichment* — no CL1 assessment coverage |

### ICTCLD502 bespoke (Kangan-authored HA decks)

| Deck | Covers | Maps to |
|---|---|---|
| Topic 1 — Identify HA requirements | HA definition, reliability, service levels, **SLAs** | **AT3 T1** (HA fundamentals) · **AT3 T5** (HA requirements §2) |
| Topic 2 — Evaluating traditional on-prem availability | multi-tier architecture, **SPoFs**, estimating **RPO/RTO** | **AT3 T1** · **AT3 T5** (baseline review, SPOFs, recovery objectives §3) |
| Topic 3 — Design cloud architecture for HA | HA design principles, WAF reliability pillar, autoscaling, LB, **scaling across AZs** | **AT3 T2** (scaling) · **AT3 T4** (LB+autoscaling) · **AT3 T6** (design HA-equivalent §4) |
| Topic 4 — Implement & finalise HA architecture | implementation approaches (big-bang/incremental/parallel), IaC, **testing tiers, monitoring availability, simulating failures, load/stress testing** | **AT3 T7** (sequencing) · **AT3 T9** (implement) · **AT3 T10** (failure sim) · **AT3 T11** (resize) · **AT3 T12** (availability) · **AT3 T14** (testing) |

---

## Candidate groupings (decks that bundle several of our topics)

Per Tim's steer — where one deck already teaches several topics together, that's a starting-point group:

- **AT2 IAM + shared responsibility** (ACF M04 / ACA M03): T3 + T11.
- **AT2 network + security groups + DNS** (ACF M05 / ACA M07): T4 + T5 (+ T12).
- **AT2 compute + storage** (ACF M06+M07 / ACA M05): T6 (EC2/EBS); S3 (T9) bundled in ACF M07 but split out in ACA M04.
- **AT2 load balancing + autoscaling + monitoring** (ACF M10 / ACA M10): T7 + T10 — strong signal.
- **AT3 HA design cluster** (502 Topic 3 / ACA M10): T2 + T4 + T6.
- **AT3 maintenance-window cluster** (502 Topic 4): T7 + T9 + T10 + T11 + T12 + T14 — strong signal (implement → simulate → measure → test, taught as one block).
- **Cloud foundations cluster** (ACF M01): AT1 T1 + T2 + T3 — the intro knowledge.

---

## Coverage gaps — topics with little/no AWS deck (bespoke teaching needed)

The AWS decks do the heavy lifting for **AT2 (build)** and **AT3 (HA)**. They barely touch **AT1**, which is mostly ICTICT517 consulting/analysis. These topics need **bespoke teaching material**:

- **AT1 consulting/analysis:** T6 strategic alignment (only data-residency touched by ACF M03), T7 current-state synthesis, T8 gap analysis, T9 workload definition, T10 options & evaluation methods, T12 risk/intangibles, T13 recommendation, T14 action plan, T15 change management/governance. *(T5 cost models + the AWS-pricing-research half of T11 are well covered by ACF M02 — incl. a ready build-an-estimate activity; only the CBA-**assembly** method — 5-yr two-option comparison, avoided-downtime, Year-1 cash-flow, sensitivity — is bespoke.)*
- **AT1 communication:** T18 board presentation, T19 Q&A / feedback / sign-off.
- **Cross-AT professional skills (all bespoke):** the documentation topics (AT2 T15 evidence capture, AT2 T16 / AT3 T16 report writing), the contextual-KE integration topics (AT1 T16, AT2 T17, AT3 T17), and the reflection topics (AT2 T18, AT3 T18). AWS decks teach the *services*, not how to evidence/document/reflect on them to a VET assessment standard.
- **AT3 partials:** T8 simulation planning, T13 compare-to-design/adjust, T15 engagement closure — touched by 502 Topic 4 but need bespoke shaping to the YAT engagement.

**Implication for the session plan:** AT2 and most of AT3 can lean on existing decks (teach-time cheap, activity-heavy); AT1 and all the documentation/communication/reflection topics need authoring from scratch. This materially affects how the 27 teaching sessions (S2–S28) get loaded.
