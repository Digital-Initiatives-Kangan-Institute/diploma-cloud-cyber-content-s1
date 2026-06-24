# Topic 12 — HA design · Coverage

**Topic 12 of 14** · **AT3 content Topic** (High Availability — the design) · teaching source: **mixed** — bespoke **ICTCLD502 Topics 2–3** (evaluate availability + design HA, incl. the documentation framework) + **ACA M10** (the cross-AZ HA architecture: LB + autoscaling across AZs + Multi-AZ); light bespoke to anchor it to the YAT/Accounting baseline.

The coverage spec — what this Topic must cover, in UoC and AT terms. `slide_plan.md` and the deck are built to satisfy it.

> **Design it (Part A).** Topic 11 gave the concepts; Topic 12 is where students **produce an HA design**. Unlike AT2 (design supplied → students build), **AT3 Part A is the design** (ICTCLD502 element 3) — so here we teach the *method* and students **design the HA upgrade themselves** from the supplied inputs (the Accounting Baseline Design + the HA requirements doc + the scenario). Topic 13 then implements + simulates it. This is **teach + practice**, practice-heavy. AT3 = ICTCLD502 (primary).

---

## Teaching-design note — method, then produce

Each step is taught (the *how*) then practised on the Accounting baseline (the *do*): **teach → practice** throughout (no AWS demos — designing isn't an AWS console task). The deliverable students build toward is a **documented HA design** — the 502 documentation framework: **architecture diagram · service list · SPoF analysis (+ solutions) · RTO/RPO table · scaling plans**. Reuse-first: the design *method* comes from 502 Topics 2–3; the cross-AZ HA *architecture pattern* from ACA M10; the *inputs* are the supplied baseline + HA requirements.

---

## What this Topic must cover

Produce an HA design that hardens the single-AZ baseline, to the supplied inputs, on the practice scenario. Three components:

- **C1 — Review the baseline & find its SPOFs.** Review the deployed single-AZ architecture (the multi-tier shape), **identify single points of failure**, and **estimate its recovery objectives** (RPO/RTO) and which components scale vertically. *(ICTCLD502 element 2 — evaluate availability.)*
- **C2 — Design the HA-equivalent.** Apply the toolkit to **remove each SPOF** — second AZ + mirrored subnets, cross-AZ Auto Scaling, multi-AZ load balancing, Multi-AZ database, redundant egress — and **re-estimate the recovery objectives** (improved). *(ICTCLD502 element 3.1–3.4 — design HA, remove SPOFs.)*
- **C3 — Document the design & plan the work.** Produce the **HA design document** (architecture diagram · service list · SPoF analysis + solutions · RTO/RPO table · scaling plans), and plan the **implementation sequencing** and the **failure/resize simulations** Topic 13 will run. *(ICTCLD502 element 3.5 — document; + AT3 sequencing/simulation planning, sets up Topic 13.)*

---

## 1. UoC mapping

UoC **taught / developed** in this Topic:

| UoC item | Descriptor | Component |
|---|---|---|
| [ICTCLD502 PC 2.1] | Review architecture of a multi-tier application and identify HA requirements | C1 *(the single-AZ baseline is the architecture reviewed)* |
| [ICTCLD502 PC 2.2] | Identify any single points of failure | C1 |
| [ICTCLD502 PC 2.3] | Estimate recovery objectives for components and overall architecture | C1 |
| [ICTCLD502 PC 2.4] | Determine components that must scale vertically and the impact on availability | C1 |
| [ICTCLD502 PC 2.5] | Document architecture review findings | C1 → C3 |
| [ICTCLD502 PC 3.1] | Design equivalent architecture for high availability using cloud services | C2 |
| [ICTCLD502 PC 3.2] | Identify and remove single points of failure as required | C2 |
| [ICTCLD502 PC 3.3] | Estimate recovery objectives for each component and overall architecture | C2 |
| [ICTCLD502 PC 3.4] | Determine components that must scale vertically and the impact on availability | C2 |
| [ICTCLD502 PC 3.5] | Document architecture design | C3 |
| [ICTCLD502 KE 4, 8] | HA design — reliability, redundancy across AZs, LB + autoscaling, Multi-AZ, recovery objectives | C1 · C2 · C3 |

> **AT3 marking home: Part A — the HA Design document.** This Topic develops the skills assessed in AT3 Part A (502 elements 2–3). AT3 build-topic refs **T5–T8** (baseline review & SPOFs · design the HA-equivalent · sequencing · simulation planning).

UoC **applied** here but **taught earlier** (not re-taught):

| What | Where |
|---|---|
| The HA concepts (availability, SPOF, RTO/RPO, the cloud toolkit) | Topic 11 (here: *applied* to produce a design) |
| What the single-AZ baseline contains (VPC, ASG, RDS, etc.) | AT2 / Topics 7–9 (the architecture being hardened) |
| Network-diagram conventions | Topic 7 / the scenario `.drawio` diagrams (used to draw the HA topology) |

---

## 2. AT3 equivalence / alignment

| AT3 element | Where assessed | How Topic 12 aligns |
|---|---|---|
| **Evaluate availability** (502 element 2) | AT3 Part A | C1 — review the baseline, identify SPOFs, estimate recovery objectives + vertical-scaling impact. |
| **Design for HA** (502 element 3) | AT3 Part A | C2 — design the HA-equivalent that removes the SPOFs; re-estimate recovery objectives. |
| **Document the design** (502 PC 2.5 / 3.5) | AT3 Part A | C3 — the HA design document (diagram · service list · SPoF analysis · RTO/RPO table · scaling plans). |
| **Sequencing & simulation planning** | AT3 Part A → B | C3 — plan the implementation order + the failure/resize simulations Topic 13 runs. |

**Practice-activity alignment:** students **design the HA upgrade for the practice baseline** (Accounting / Ledgerline) — review it, find its SPOFs, design them out, document the design — from the supplied inputs (the **Accounting Baseline Solution Design** + the **HA database requirements** doc + the scenario). Mirrors AT3 Part A on the LMS, where students design the LMS HA upgrade from the LMS baseline + the LMS HA requirements.

> **Inputs (supplied), design (student-produced).** We do **not** supply a finished HA design — that's the deliverable. Inputs: the baseline design (predecessor), the HA requirements doc, the scenario docs.

---

## Out of scope for this Topic (covered elsewhere)

- **HA concepts** (what a SPOF / RTO/RPO / the toolkit *are*) → **Topic 11** (applied here, not re-taught).
- **Implementing the HA design + failure/resize simulation + availability measurement** → **Topic 13** (this Topic *plans* them; Topic 13 *does* them).
- **The HA Deployment Report + closure/sign-off** → **Topic 14**.
- **Building the single-AZ baseline** → AT2 / Topics 6–9 (reviewed here, not rebuilt).
- **Multi-Region / full DR** → CL2 (single-Region HA only).

---

## Coverage checklist (for `slide_plan.md` + the deck to satisfy)

- [ ] Each of C1–C3 is **teach → practice** (no AWS demos — designing is analytical).
- [ ] **C1** teaches reviewing an architecture + **identifying SPOFs** + **estimating recovery objectives** (502 Topic 2 method; the "Identify SPoFs in a diagram" slide); practice = do it on the Accounting baseline.
- [ ] **C2** teaches **designing the HA-equivalent** — remove each SPOF with the toolkit (2nd AZ, cross-AZ ASG, multi-AZ LB, Multi-AZ DB, redundant NAT) and **re-estimate recovery objectives**; from 502 Topic 3 + ACA M10's cross-AZ HA architecture (e.g. ACA M10 S41).
- [ ] **C3** teaches the **HA design document** = the 502 framework (architecture diagram · service list · SPoF analysis + solutions · RTO/RPO table · scaling plans) + **sequencing** + **simulation planning**; practice = produce it for the Accounting baseline.
- [ ] The **inputs are supplied, the design is student-produced** — the deck never hands out a finished HA design.
- [ ] The Topic 11 → Topic 12 split is respected: concepts in 11, the *doing* (Identify SPoFs · Removing SPoF · Multi-Tier design) here.
- [ ] Reuse-first: 502 Topics 2–3 (method + doc framework) + ACA M10 (cross-AZ HA architecture); bespoke only to anchor to the Accounting baseline.
- [ ] Student-facing slides in-world; source-deck refs may stay visible (by title), UoC refs off slides; depth ceiling single-Region HA (cross-AZ), DR is CL2.
- [ ] A student leaving this Topic can review a baseline, design its HA-equivalent, and document the design — ready to implement it in Topic 13.
