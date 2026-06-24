# Topic 11 — HA concepts · Coverage

**Topic 11 of 14** · **AT3 content Topic** (the first — High Availability foundations) · teaching source: **mixed** — the bespoke **ICTCLD502 Topics 1–3** decks (Kangan-authored, purpose-built for this unit) + **ACA M10** (HA: load balancing, autoscaling, Multi-AZ, failover) / ACF M09 (Well-Architected reliability); light bespoke to tie it to the YAT/Accounting baseline.

The coverage spec — what this Topic must cover, in UoC and AT terms. `slide_plan.md` and the deck are built to satisfy it.

> **New AT, new shape.** AT3 = ICTCLD502 (primary) — take the **single-AZ baseline** built in AT2 and make it **highly available**. Topic 11 is the **concepts** layer (teach + light activity): what availability, fault tolerance, single points of failure and recovery objectives *are*, and how the cloud achieves availability (redundancy across AZs, load balancing, autoscaling, Multi-AZ). Topic 12 designs the HA architecture, Topic 13 implements + simulates it, Topic 14 closes out. This Topic builds the vocabulary the rest of AT3 uses.

> **Practice model — students design, we supply inputs (settled 2026-06-03).** Unlike AT2 (design supplied → students build), **AT3 Part A is the design** (502 element 3) — students *produce their own HA design*. So we do **not** supply a finished HA design; we supply the **inputs** they design from: the **Accounting Baseline Solution Design** (predecessor), the scenario docs, and a focused **HA requirements** doc (`projects/accounting-cloud-migration/ha-database-requirements.md`, created — the parallel of the LMS `ha-database-requirements.md`). The design **practice space is Topic 12**. *(A full Accounting HA Solution Design was drafted then set aside as instructor-exemplar only — held back so it doesn't pre-empt the design practice.)*

---

## Teaching-design note — primer-first (no assumed baseline)

Each concept gets a plain primer before the cloud-specific treatment: what **availability** means (and how a % maps to downtime), what **fault tolerance** and a **single point of failure** are, what **RPO/RTO** measure. The bespoke 502 decks already pitch at the right level (they're purpose-built, not AWS-generic), so reuse-first here means **drawing from the 502 Topics 1–3 slides**; ACA M10 supplies the AWS HA mechanisms. **Teach + light activity** (concepts — the build/simulate is Topic 13).

---

## What this Topic must cover

The vocabulary and mechanisms of high availability — enough to *review* the baseline (Topic 12) and *design/build* HA (Topics 12–13). Three components:

- **C1 — Availability, reliability & service levels.** What availability *is* (primer; % ↔ downtime) → reliability, recoverability and service levels (SLAs); how a business-hours 99.5% target differs from a 24/7 99.9% one. *(ICTCLD502 PC 1.1; 1.2.)*
- **C2 — Single points of failure & recovery objectives.** What a SPOF *is* (primer) → identify SPOFs in a multi-tier architecture; **RPO** (how much data you can lose) vs **RTO** (how long to recover); which components must **scale vertically** and the availability impact. *(ICTCLD502 PC 2.2; 2.3; 2.4 — concepts.)*
- **C3 — Achieving availability in the cloud.** Built-in vs designed fault tolerance (primer) → redundancy **across Availability Zones**; **load balancing + autoscaling** for availability (not just load); **Multi-AZ** databases; **DNS failover** — the mechanisms AT3 will use. *(Underpins ICTCLD502 element 3; from ACA M10.)*

---

## 1. UoC mapping

UoC **taught / developed** in this Topic:

| UoC item | Descriptor | Component |
|---|---|---|
| [ICTCLD502 PC 1.1] | Determine reliability, recoverability and service levels required for application | C1 |
| [ICTCLD502 PC 1.2] | Determine cloud infrastructure according to business needs | C1 |
| [ICTCLD502 PC 2.2] | Identify any single points of failure | C2 *(concept; applied to the baseline in Topic 12)* |
| [ICTCLD502 PC 2.3] | Estimate recovery objectives for components and overall architecture | C2 *(concept)* |
| [ICTCLD502 PC 2.4] | Determine components that must scale vertically and the impact on availability | C2 *(concept)* |
| [ICTCLD502 KE 4, 7, 8] | HA concepts — fault tolerance, redundancy, availability zones, load balancing, autoscaling, Multi-AZ, failover | C1 · C2 · C3 |
| `[ICTCLD401 PC 1.2 / KE]` | Shared security responsibility (applied at the HA layer) | C1 *(light; taught in Topic 6)* |

> **AT3 marking home:** the concepts here are *examined through* AT3 Part A (the HA Design — Topic 12) and Part B (implement/simulate — Topic 13); Topic 11 itself is **teach + light activity**, not a graded deliverable. AT3 build-topic refs **T1–T4** (HA fundamentals · reliability/SLAs · scaling · LB+autoscaling).

UoC **applied** here but **taught earlier** (not re-taught):

| What | Where |
|---|---|
| The single-AZ baseline (VPC, ASG min1/max2, single RDS) that AT3 hardens | AT2 / Topics 7–9 (the starting point) |
| What ASG / ALB / RDS / AZs *are* | AT2 / Topic 8 (here: used *for availability*, not introduced) |
| Recovery objectives of the baseline (RPO ≤ 1 h, RTO ≤ 1 business day; single-AZ SPOF) | Topic 9 (the design's §4.13) |

---

## 2. AT3 equivalence / alignment

| AT3 element | Where assessed | How Topic 11 aligns |
|---|---|---|
| **Identify HA requirements** (502 element 1) | AT3 Part A | C1 — reliability / recoverability / service levels; the vocabulary for stating HA requirements. |
| **Evaluate availability** (502 element 2 — concepts) | AT3 Part A | C2 — SPOFs, recovery objectives, vertical-scaling impact (concepts; applied to the baseline in Topic 12). |
| **Design for HA** (502 element 3 — underpinning) | AT3 Part A | C3 — the cloud HA mechanisms (cross-AZ redundancy, LB+autoscaling, Multi-AZ, failover) students will design with. |

**Practice-activity alignment:** light activities only — e.g. spot the SPOFs in the baseline, estimate recovery objectives, match a mechanism to an availability problem. The real design/build is Topics 12–13 on the Accounting HA design (pending).

---

## Out of scope for this Topic (covered elsewhere)

- **Reviewing the actual baseline + designing the HA-equivalent** → **Topic 12** (concepts applied).
- **Implementing HA + failure/resize simulation + availability measurement** → **Topic 13**.
- **Closure, sign-off, the HA Deployment Report** → **Topic 14**.
- **Disaster recovery to a second Region / full DR patterns** → CL2 (out of CL1 scope; baseline is single-Region HA).
- **Building EC2/ALB/ASG/RDS** → AT2 / Topic 8 (used here for availability, not re-taught).

---

## Coverage checklist (for `slide_plan.md` + the deck to satisfy)

- [ ] Each of C1–C3 covered, **teach → light activity** (no big build — that's Topic 13).
- [ ] **Availability** taught concretely: % ↔ downtime, and why YAT's 99.5% business-hours target differs from a 24/7 99.9% one (C1).
- [ ] **SPOF** and **RPO/RTO** are defined plainly and tied to the YAT baseline's known single-AZ SPOF (C2).
- [ ] The cloud HA mechanisms (cross-AZ redundancy, LB+autoscaling-for-availability, Multi-AZ, DNS failover) are taught as the toolkit AT3 will use (C3).
- [ ] Reuse-first: drawn from the **502 Topics 1–3** decks + **ACA M10** HA section; light bespoke ties it to the YAT/Accounting baseline.
- [ ] Depth ceiling: single-Region HA (cross-AZ); full DR / second Region is out (CL2).
- [ ] Student-facing slides in-world; AWS/502 source refs may remain visible (per the 2026-06-03 exception).
- [ ] Sets up Topic 12 (design) cleanly — a student leaving Topic 11 has the vocabulary to review the baseline and reason about an HA design.
