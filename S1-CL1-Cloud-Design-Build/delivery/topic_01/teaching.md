# Topic 1 — Cloud literacy · Teaching

**Depth ceiling (read first).** Topic 1 teaches *only* the cloud literacy that AT1 Business Case **Appendix 2, Q1–Q5** tests: **recognise / explain / classify** — enough to write a one-paragraph contextual answer and to reason about options and cost. **No hands-on building.** Configuring IAM, VPC, EC2, RDS, etc. is **AT2** — do not pull the build decks (M4, M6, M7, M8, M10) into this Topic.

Format: each coverage point gives an **[AWS]** deck reference (deck named; slide range to be pinned later) and/or **[BESPOKE]** slide content (each slide split by a `====` rule).

The five points map 1:1 to Appendix 2: **C1→Q2, C2→Q1, C3→Q4, C4→Q3, C5→Q5.**

---

## Opening — framing

**[BESPOKE]**
```
Topic 1 — Cloud literacy
Enough cloud to write the Business Case — not to build anything (yet)

- You're an MTS consultant. Before you can weigh "renew on-prem vs move to cloud",
  you need to speak cloud: the models, the building blocks, the standards, the pricing.
- Goal: answer the five knowledge questions in Business Case Appendix 2, and reason
  about options (§6) and cost (§7). Building these services is AT2.
```

---

## C1 — Cloud fundamentals & deployment models  *(→ Appendix 2 Q2)*

**[AWS] ACF Module 1 — Cloud Concepts Overview** *(slice — slides TBD):* what cloud computing is (on-demand, pay-as-you-go), infrastructure-as-software, advantages.

**[BESPOKE]** deployment models, framed for YAT:
```
Deployment models — where the cloud lives
- Public  — provider-owned, multi-tenant (AWS). Lowest capital, fastest scale.
- Private — single-tenant. More control, more cost.
- Hybrid  — on-prem + cloud (YAT today: on-prem servers + Office 365 SaaS).
- Community — shared by orgs with common needs.
The cluster's decision = an on-prem system → public cloud. Know the rest as context.
```

---

## C2 — Service models: IaaS / PaaS / SaaS  *(→ Appendix 2 Q1)*

**[AWS] ACF Module 1** *(slice):* the AWS service-category introduction.

**[BESPOKE]** the classification lens (decks define the terms; this makes it the decision Q1 asks for):
```
IaaS / PaaS / SaaS — the "who manages what" lens
- IaaS (e.g. EC2)        you manage OS + app. Use to preserve an existing stack.
- PaaS (e.g. RDS, ALB)   provider runs the platform; you manage config + data.
                         Use to offload ops when in-house cloud skills are thin.
- SaaS (e.g. Office 365) provider runs everything; you just use it.
Choosing = control vs operational burden. Classify each part of a solution, and say why.
```

---

## C3 — Core AWS services (name + role)  *(→ Appendix 2 Q4)*

> Q4 asks students to **name a service and its general feature/role** — not to build it. So this is **one overview slide**, not the service decks. The build depth is **AT2 (Topics 9–13)**.

**[AWS] ACF Module 3 — service & service-category overview** *(slice only).*

**[BESPOKE]** the core services + the workload pattern (the connective view the decks don't give):
```
The core services for a web workload — and how they fit
- ALB (Application Load Balancer)  PaaS — distributes traffic, health checks
- EC2 + Auto Scaling Group         IaaS — the app tier; scales with demand
- RDS                              PaaS — the managed database (system of record)
- S3                               object storage — attachments, backups
- EBS                              block storage — disks for EC2
- CloudWatch                       monitoring across all tiers

        Internet → ALB → EC2/ASG → RDS   (+ S3, CloudWatch)

This same shape underlies BOTH the LMS and the Accounting system. You'll BUILD it in AT2;
here you just need to name each piece and its role.
```

---

## C4 — Industry technology standards  *(→ Appendix 2 Q3)*

**[AWS] ACF Module 9 (Cloud Architecture) or ACA Module 2** *(slice):* the **AWS Well-Architected Framework** — six pillars, with Reliability flagged (it underpins AT3).

**[BESPOKE]** the non-AWS standards (no AWS deck covers these) + which decision each informs:
```
Standards that inform a migration — name the right one for the decision
- NIST SP 800-145       defines IaaS/PaaS/SaaS        → §6 service-type choices
- AWS Well-Architected  6 pillars (incl. Reliability)  → design + §10 methods
- ISO/IEC 27017         cloud security controls         → §8 security
- ACSC Essential Eight  AU baseline cyber mitigations   → §10 controls
- ITIL 4                service management              → change-management alignment
You don't memorise them — you name the right one for the decision at hand.
```

---

## C5 — Cloud cost models & economics  *(→ Appendix 2 Q5)*

**[AWS] ACF Module 2 — Cloud Economics and Billing** *(slice):* pay-as-you-go, Reserved Instances vs on-demand, TCO, and the **AWS Pricing Calculator** + its build-an-estimate group activity (reused in the Topic 3 CBA).

**[BESPOKE]** match the model to the workload (turns the concepts into the CBA decision):
```
Matching the pricing model to the workload
- Predictable baseline   → Reserved Instances (discount for commitment)
- Variable / peak load   → On-demand or autoscaling (pay for the spike only)
- Interruptible          → Spot (cheapest; not for production baseline)
- Storage / data         → pay-as-you-go, scales with usage
So total cloud cost grows roughly with demand — the heart of the Topic 3 CBA.
```

---

## Close — bridge to practice & assessment

**[BESPOKE]**
```
From literacy to the job
- Practice (this Topic's exercise): classify a real solution's parts (IaaS/PaaS/SaaS),
  name the services + cost models — on the YAT Accounting System.
- Assessment (AT1): this is tested directly in Business Case Appendix 2 Q1–Q5, and
  underpins your Options (§6), CBA (§7), and Strategic Alignment (§3).
```

---

## Decks — owns vs borrows (for `source_slides/` pruning)

- **Owns (keep in `source_slides/`):** ACF **M1** (Cloud Concepts), ACF **M2** (Economics), ACF **M3** (Global Infra / service overview).
- **Borrows (reference only — do NOT copy; they live in their owning Topic):** WAF-pillars slice from **M9 / ACA M2**.
- **Not in this Topic at all (AT2/AT3 build depth):** **M4** (Security), **M6** (Compute), **M7** (Storage), **M8** (Databases), **M10** (Scaling/Monitoring). → safe to delete from `topic_01/source_slides/`.

## Teaching notes

- Knowledge-heavy, light activity (top tempo band). May span more than one session — it's the foundation, but it's *breadth*, kept to recognise/explain/classify.
- Demos optional (recorded AWS module demos), not required.
- Slice slide-ranges to be pinned in a later pass.
