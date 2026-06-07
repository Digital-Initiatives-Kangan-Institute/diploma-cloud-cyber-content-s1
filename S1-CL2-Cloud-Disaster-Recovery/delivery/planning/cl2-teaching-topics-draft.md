# S1-CL2 — teaching Topic sequence (DRAFT)

**Status:** DRAFT, drafted 2026-06-07 (delivery-process Step 1). The cluster's **teaching content** expressed as a linear sequence of **Topics**. A **Topic** is the coherent unit we build teaching + exercise materials for, and the level we schedule into sessions; it is **not** session-bound (one Topic may span sessions). Session allocation is a later step (deferred until each Topic's footprint is known — Step 3).

**Terminology:** `AT → Topic → component`. The authoritative per-Topic coverage (UoC + AT mapping) is worked out in each `topic_NN/coverage.md` (Step 2, derived from the AT assessor `.docx`); this file is the spine. The folders `topic_01/ … topic_10/` already exist.

**Topics vs assessments.** Assessments are **not** Topics. Content Topics are numbered **1–10** (what we build teaching materials for). Assessment events and other non-teaching sessions are listed in delivery order but **lettered**, not numbered.

**Teach / practice / assess rhythm:** content Topics teach + build a *practice* artefact in a **different scenario** than the real YAT engagement; the lettered assessment sessions are where students produce/defend their **real** AT.
- **Practice vehicle — TBD.** CL1 used the YAT Accounting System (Ledgerline). It can carry the DR, IaC, microservice and monitoring Topics, but **not the web-scale Topic (T1)** — bookkeeping isn't a web-scale workload. A **small separate web-scale practice app** is needed behind T1 (and AT1's web-scale design) — see `assessments/assessment_plan.md §7`. **TBD.**

**Planning frame (fixed).** CL2 = **weeks 9–18 (10 weeks), 30 × 3h sessions (3/wk)**, delivered in parallel with CL3. AT1's `.docx` allocates **Part A ≈ 2 weeks, Part B ≈ 3 weeks** → AT1 phase ≈ first 5 weeks (~15 sessions), AT2 phase ≈ last 5 weeks (~15 sessions).

**Depth ceiling.** AT1 Topics are **design / plan** depth (the AT designs and plans — it does not build the web-scale architecture or execute the DR). AT2 Topics are **build** depth. Don't teach deeper than the assessment requires.

**Open inputs (TBD).** (1) the web-scale practice app (above); (2) the **lab-product `[VERIFY]`** — which AWS Academy lab product (Architecting Sandbox vs Learner Lab) — shapes the T6–T9 demos; (3) exact AWS deck pinning per Topic (Step 3, via a CL2 deck catalogue).

---

## Topic 0 — Onboarding *(first session of the block, fixed)*
Orientation, systems/LMS access, scenario introduction (the YAT LMS global-expansion engagement). Not a content Topic.

## AT1 — Cloud Expansion: Design & DR Plan *(content Topics 1–5 · ≈ weeks 9–13)*

| # | Topic | AT anchor | Teaching source | Nature |
|---|---|---|---|---|
| 1 | **Web-scale architecture & design** — web-scaling needs, edge/CDN, read/session caching, compute & storage scaling, global delivery, availability/security maintained | Part A §5 (503 G3) | AWS ACA (CloudFront/edge, ElastiCache, Auto Scaling, Route 53) + bespoke; *deck pinning TBD* | teach + practice **design** |
| 2 | **Microservices & serverless design** — identify the microservice + data transactions, supporting serverless services (API / queue / function / NoSQL), the architecture and the integration contract | Part A §6 (503 G4a) | AWS ACA serverless (Lambda, API Gateway, SQS, DynamoDB) + bespoke; *pinning TBD* | teach + practice **design** |
| 3 | **DR: requirements & impact analysis** — DR plan requirements, current recovery position, RTO/RPO, the risk register, data volume/sensitivity, severity | Part B §2–4 (501 G1) | AWS resilience/DR + bespoke (501 risk/impact discipline) | teach + practice **plan** |
| 4 | **DR: strategy & plan** — the four cloud DR strategies (backup-restore / pilot-light / warm-standby / active-active), choosing one to the objectives, the recovery runbook & steps, continuity standards (ISO 27031) | Part B §5–6 (501 G2) | AWS DR strategies + bespoke | teach + practice **plan** |
| 5 | **Documenting & presenting the design + plan** — justify the architecture; the approval walkthrough, seeking/responding to feedback, lodgement, sign-off, and KE Q&A preparation | Part A docs + Part C (503 PC 1.7/2.4; 501 el 5; FS Writing/Oral) | bespoke | teach + practice **presentation** |

**Non-Topic sessions** *(AT1 — delivery order):*
- **a — AT1 preparation** — students produce their real Solution Design + DR Plan · *assessment*
- **b — AT1 presentation (Part C)** — present design + plan to YAT ICT management, Q&A, feedback, sign-off · *assessment*

*Topics 1–4 build one cumulative practice design + DR plan in the practice scenario; Topic 5 prepares the presentation. The real YAT LMS design is the AT1 assessment.*

## AT2 — Cloud Microservice & IaC Implementation *(content Topics 6–10 · ≈ weeks 14–18)*

| # | Topic | AT anchor | Teaching source | Nature |
|---|---|---|---|---|
| 6 | **IaC: fundamentals & operating provided templates** — what IaC is and why; CloudFormation template anatomy (parameters/resources/outputs); deploy / update / delete / confirm; troubleshoot a broken template | AT2 §4.2 (505 G5) | AWS ACA CloudFormation/IaC + bespoke (the supplied-template discipline) | teach + **demo** + practice build |
| 7 | **Authoring & parameterising your own IaC template** — write a template that provisions a related resource set; parameterise for reuse; update/redeploy; remove; troubleshoot | AT2 §4.3 (505 G6) | AWS ACA CloudFormation + bespoke | teach + **demo** + practice build |
| 8 | **Building & deploying the serverless microservice** — apply T6/T7 to deploy the API + queue + function from the provided code, wire it to the provided data store, test and troubleshoot end-to-end | AT2 §4.4 (503 G4b) | AWS ACA serverless deploy + the provided code/contract | teach + **demo** + practice build |
| 9 | **Monitoring & alarms** — metrics and a scaling-relevant alarm (e.g. queue depth / function errors) on the running microservice; alerting | AT2 §4.5 (503 PC 4.1; 501 KE 6 · G8) | AWS ACA CloudWatch + bespoke | teach + **demo** + practice build |
| 10 | **Documenting the build, handover & sign-off** — IaC user documentation, the Deployment Report, build feedback and final sign-off; contextual KE | AT2 §7 (505 PC 4.1/PE 4; 503/505 el 4 · G9/G10) | bespoke | teach + practice |

*(G7 — shared cloud foundations / industry-standard KE — woven into the AT2 Topics' KE rather than a standalone Topic.)*

**Non-Topic sessions** *(AT2 — delivery order):*
- **c — AT2 build** — operate the provided store + author/deploy the microservice in the lab · *assessment*
- **d — AT2 Deployment Report** — produce the Deployment Report (single deliverable, no presentation) · *assessment*
- **e — catch-up / resit** — end-of-block buffer

*Topics 6–10 build one cumulative practice microservice (the practice scenario) as IaC; the real YAT audit-log microservice is the AT2 assessment.*

---

## Next steps (delivery-process Steps 2–3)
- **Step 2 — `coverage.md` per Topic** (the authoritative UoC + AT mapping, depth ceiling).
- **Step 3 — `slide_plan.md` → Kangan deck** per Topic (primer-first, reuse-first from AWS decks, `teach → demo → practice`), then size each Topic against the tempo bands and lay onto the 30 sessions.
- Resolve the **practice web-scale app** and the **lab-product `[VERIFY]`** before Step 2/3 materials depend on them.
