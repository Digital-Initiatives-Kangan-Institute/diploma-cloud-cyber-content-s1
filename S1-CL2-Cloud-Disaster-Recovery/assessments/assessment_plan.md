# S1-CL2 Cloud Disaster Recovery — Cluster Assessment Plan

> **STATUS: DRAFT.** This plan turns the cluster's settled design (topic taxonomy, two-AT division, AT1's three-part shape, the scenario spine) into the spec the AT instruments are built from, and carries the coverage proof that every UoC item lands in an assessment.
>
> **What is settled** (discussed and approved with Tim, 2026-06-06):
> - The four-topic taxonomy and the **two-AT** division.
> - **AT1 is three parts** — **Part A Solution Design** (ICTCLD503 design), **Part B DR Plan** (ICTCLD501), **Part C presentation** covering both for approval. **AT2** is a single written **Deployment Report** (implement).
> - **DR ≠ regulatory ≠ design — three separate concerns:** the *Disaster Recovery* plan (501) answers "what do we do if the system goes down"; the *Solution Design* (503) holds the web-scale architecture **and the microservice**; *data residency* is an **input constraint**, not a student deliverable. The microservice lives in the Solution Design (its regulatory purpose is *why* it exists), **never** in the DR plan.
> - The scenario spine (offshore-India / **website** as the assessment vehicle; **LMS** as the practice vehicle); the **light** India-residency slice; the two approval gates; the KE evidencing approach (written appendices in each document + verbal contextual Q&A at AT1's presentation).
>
> **What is TBD** (my proposals, not yet approved — Rule 1/2): every group-level *assessment idea*; the 503 global-serving practice vehicle; project slugs; `501 KE 6` placement; and the two `[VERIFY]`s. All carry explicit TBD marks below.
>
> **Companion documents:**
> - `consolidated_uoc.md` (cluster root) — every PC/FS/PE/KE/AC verbatim, in 13 groups under the 4 topics.
> - `scenario/cluster-2-scenario-assessment.md` + `cluster-2-scenario-practice.md` — the scenario design (offshore-India spine, residency drivers, microservice, AWS Academy simulation); `scenario/scenario-flow.md` — the cross-cluster assessment/practice matrix.
> - `S1-CL1-Cloud-Design-Build/assessments/assessment_plan.md` — the pilot-cluster plan this one parallels in shape.

---

## 1. Integration approach

**Goal (same as CL1):** one integrated cluster assessment that reads as a single project from design to hand-over, not three units stapled together — a single scenario, a single stakeholder voice, a single artefact thread.

**Shape:** the cluster runs as one continuous engagement across two delivery phases, each a **teach → practice → assess** cycle:

```
   Phase 1 — Design & Plan                       Phase 2 — Implement
   (Topic 1 + design-side Documenting)           (Topics 2, 3 + build-side Documenting)
        ↓                                              ↓
       AT1                                            AT2
   Part A  Solution Design   (ICTCLD503 design)      Deployment Report
   Part B  DR Plan           (ICTCLD501)             - microservice build (503)
   Part C  Presentation      (501 element 5 —        - IaC (505)
           covers A + B,       the approval gate)    - monitoring (Topic 3)
                                                     - IaC user docs + build sign-off

   Each part/AT bundles: the design/build work + its documentation
   + a feedback/sign-off cycle + contextual reflective KE questions
   on the student's own work.
```

**The thread (the design-approval gate):** in AT1 the student **designs** the India-expanded system (Part A), **plans its recovery** (Part B), and gets **both approved** at the Part C presentation. AT2 then **builds** the design that was signed off. AT2 is not a fresh start — it implements the student's own approved design. This is UoC-faithful: 501 element 5 = approval *before* implementing; 503/505 element 4 = build sign-off.

**Why Part A before Part B:** a DR plan is written *for* a designed system — you cannot plan recovery for infrastructure you have not yet designed. So the Solution Design (Part A) is produced first; the DR Plan (Part B) plans recovery for it; the presentation (Part C) approves the pair.

**Knowledge evidence — contextual, not abstract recall** (carried from CL1): KE is assessed by asking students to reason about *their own* design and build choices, not abstract questions divorced from the project. Example: instead of "List web-scale cloud components," ask "For your YAT web-scale design, which components did you choose for SQL vs NoSQL, monolith vs microservice, container vs serverless — and why each?"

**KE evidencing locations (settled):**
- **Written answers in a KE appendix** of each document — Part A (Solution Design), Part B (DR Plan), and AT2 (Deployment Report) each carry one. This is the mandatory location.
- **Verbal contextual questions at the AT1 Part C presentation** — the verbal location, covering the Part A + Part B KE. AT2 has no presentation, so its KE is **written-only**.
- All questions are **contextual to what the student did**, never general theory.

---

## 2. Scenario

**Settled** — see `scenario/cluster-2-scenario-assessment.md` (and `scenario-flow.md`). In brief: YAT enters an **offshore-India partnership (GIFT City)** that takes the **public website** global, requiring it to (a) serve a global user base, (b) be region-recoverable, and (c) be provisioned as code — one event that drives all three units. The **website is the assessment vehicle**; the **LMS is the practice vehicle** (the parallel `lms-global-expansion` engagement, taught as the worked example). Baseline: the website arrives **HA-hardened** (Multi-AZ, single-region cross-AZ) — the provided CL2 starting state.

**Data residency is an *input constraint*, not a deliverable.** The **light** India slice (a bounded set of access logs/data in-region; the main DB stays in AU) is supplied to students as the `Data Residency & Sovereignty Requirements` document in the `website-global-expansion` project. Students **design to it** — it shapes Part A's web-scale design (`503 PC 1.5`, global user base) and is *why* the audit-log microservice exists — and it is lightly respected in Part B's DR plan (recovery must not break residency). Students do **not** author a compliance plan; no UoC asks for one.

**Scenario is not a topic** and is not itself assessed. It supplies the assessment inputs and the environment (AWS Academy labs).

**Open scenario items that touch assessment (TBD):** project slugs; the two `[VERIFY]`s (Kangan's exact AWS Academy lab product; legal wording before student-facing docs). *(The 503 global-serving practice vehicle is resolved — the **LMS** is the web-scale practice system per the scenario-flow re-vehicling.)*

---

## 3. Cluster assessment structure

| Component | Working title | Format | Unit focus | Topics |
|---|---|---|---|---|
| **AT1** | Cloud Expansion: Design & DR Plan | **Project Assessment**, three parts (below) | **ICTCLD503** *design* + **ICTCLD501** | 1 + Documenting (design) |
| **AT2** | Cloud Microservice & IaC Implementation | Single written **Deployment Report** (+ provided artefacts as appendices) | **ICTCLD503** *build* + **ICTCLD505** + monitoring | 2, 3 + Documenting (build) |

**AT1 — three parts:**

| Part | Deliverable | Carries | Document |
|---|---|---|---|
| **A** | **Solution Design** — web-scale architecture for the global user base + the microservice (audit-log service). Residency reflected as a design input. | ICTCLD503 *design* (G3, G4a) + design documentation (`503 PC 1.7/2.4`) | Solution Design `.docx` |
| **B** | **DR Plan** — recovery for the system designed in Part A. Risk/impact, RTO/RPO, backup-restore, recovery steps. Pure DR. | ICTCLD501 elements 1–4 (G1, G2) | DR Plan `.docx` |
| **C** | **Presentation** — walkthrough of Part A + Part B, seeking/responding to feedback, lodgement, obtaining sign-off. The design-approval gate. | ICTCLD501 element 5 (`PC 5.1–5.4`) + FS Oral communication (501) | presentation `.pptx` + observation record |

**AT2 — single Deployment Report:** the student operates a provided data-store template (505 elements 1–2), authors their own template for the microservice and deploys it from the provided code (505 element 3 + 503 element 3), configures the monitoring (Topic 3), produces the IaC user documentation (`505 PC 4.1`, `PE 4`), and obtains the build sign-off (`503 PC 4.2/4.3`, `505 PC 4.2`). The provided artefacts (the data-store template, the microservice code, the webhook contract) are supplied as appendices to the assessment document — there is no separate lab pack.

**Why two ATs (not three):** the cluster splits cleanly into a *design/plan* phase and a *build* phase with a single natural approval gate between them. Folding the DR plan into AT1 as Part B (rather than a third AT) keeps one approval moment, balances the workload (two comparable phases instead of two paper ATs + one overloaded build AT), and stays lean — while preserving the design→plan→build order inside AT1.

**Two approval moments (by design, UoC-faithful):**
- **End of AT1 (Part C) — design approval:** the Solution Design + DR Plan approved at the presentation, before any build. Carries ICTCLD501 element 5.
- **End of AT2 — build sign-off:** the implemented, monitored infrastructure signed off via the Deployment Report. Carries ICTCLD503 element 4 (`PC 4.2/4.3`) + ICTCLD505 element 4 (`PC 4.2`).

**Template basis:** AT1 uses the institutional **Project Assessment** template (multi-part, as CL1 AT1–AT3 did). The **DR Plan template** (Part B) and **AT1 DR-Plan assessor exemplar** are already built (`scripts/build_dr_plan_template.py`, `scripts/build_s1_cl2_at1_dr_plan_exemplar.py`); the exemplar needs the regulatory/microservice material **de-weaved** out (that content moves to the Part A Solution Design). A **Solution Design** exemplar + template (Part A) and the **Part C** presentation are to be authored, reusing the existing Solution Design / Business-Case-Presentation document types.

---

## 4. Authoring basis / provenance

**CL2 is authored fresh — it is not a reuse/synthesis exercise like CL1.** Two reasons:

1. **ICTCLD505 is greenfield** — no source material exists for it at all.
2. **The ICTCLD501 / ICTCLD503 standalone source assessments are not in this repo.** ⚠️ **The Step-3 reuse audit is blocked until they are located.** Until then no reuse provenance can be claimed and the ATs are authored against the consolidated UoC directly.

**What *is* reusable / already built:**
- The **DR Plan template + AT1 DR-Plan assessor exemplar** (Part B) — pending the de-weave.
- The **Solution Design** and **Business-Case-Presentation** document types from CL1 (for Part A and Part C).
- The **CL1 AT pattern** as a structural model (Project Assessment template; multi-part AT; appendix-bearing report for AT2; contextual reflective KE; bidirectional UoC traceability).
- The **scenario inputs** already on the intranet (the `website-global-expansion` project documents, incl. the residency requirements; the `lms-global-expansion` project is the parallel **practice** worked-example).

**TBD:** if/when the 501/503 source assessments surface, re-audit AT1/AT2 for reusable practical tasks (especially 503's microservice/serverless lab steps and 501's risk-register/impact-analysis structure) before finalising.

---

## 5. Group coverage map

Every group in `consolidated_uoc.md` mapped to where it is covered, and how. This is the audit trail proving no UoC item is unaddressed. (There are **no ungrouped items** this cluster — all 128 items sit in G1–G13.)

| Group | Topic | Where | How it is evidenced |
|---|---|---|---|
| **G1** — Cloud DR: requirements & impact analysis | 1 | **AT1 Part B** | DR requirements + impact-analysis sections of the DR plan: risk register, RTO/RPO determination, data volume/sensitivity, severity. `501 PC 1.1–1.3, 2.1–2.5`, `501 PE 2`, `501 KE 1/2/5`, `501 FS Planning & organising`. |
| **G2** — Cloud DR: solutions & plan finalisation | 1 | **AT1 Part B** | The DR plan body: ≥3 major risk events, solution options + prioritisation, plan steps/timelines, RTO/RPO alignment. `501 PC 3.1–3.4, 4.1–4.3`, `501 PE 1/3`, `501 KE 3/4`. |
| **G3** — Web-scale architecture design | 1 | **AT1 Part A** | Solution Design: scalable web-app architecture for the global website — elastic network/compute/storage, global reach (CloudFront), availability/security maintained, residency-driven placement. `503 PC 1.1–1.6`, `503 PE 1/5`, `503 KE 3/6`. |
| **G4a** — Microservices & serverless: design | 1 | **AT1 Part A** | Solution Design: the webhook-driven audit-log microservice — services, data transactions, supporting cloud services. `503 PC 2.1–2.3`, `503 PE 2`, `503 KE 4`. |
| **G4b** — Microservices & serverless: implementation | 2 | **AT2** | Deploy/configure the Part A microservice on serverless services; functional test + troubleshoot. `503 PC 3.1–3.4`, `503 PE 3/4`, `503 KE 5`. |
| **G5** — IaC: deploy & manage with templates | 2 | **AT2** | Deploy/configure/update/remove resources from predefined IaC templates + troubleshoot. `505 PC 1.1–1.4, 2.1–2.6`, `505 PE 1/3`, `505 KE 3/4/5/6/7/10/11`. |
| **G6** — IaC: author & parameterise own templates | 2 | **AT2** | Student-authored template provisioning related resources; update/redeploy; parameterise for reuse. `505 PC 3.1–3.7`, `505 PE 2`, `505 KE 8/9`. |
| **G7** — Shared cloud foundations (standards, hw/sw/storage) | 2 | **AT2** | KE appendix / contextual questions co-evidencing the near-identical `503 KE 1/2` + `505 KE 1/2` once. |
| **G8** — Metrics, monitoring, alerts & scaling alarms | 3 | **AT2** (+ AT1 Part B) | `503 PC 4.1` — configure a metric + a scaling-relevant alarm (CloudWatch, e.g. queue depth) on the microservice during the build (**AT2**). `501 KE 6` (monitor / create alerts) — evidenced as disaster-detection in the **DR Plan KE appendix (AT1 Part B)**. |
| **G9** — Documentation & technical writing | 4 | **split** | `503 PC 1.7, 2.4` + `503 FS Writing` → **AT1 Part A** (architecture documented & justified — i.e. the Solution Design itself). `505 PC 4.1`, `505 PE 4` + `505 FS Writing` → **AT2** (IaC user documentation). |
| **G10** — Finalisation: feedback, sign-off & lodgement | 4 | **split** | `501 PC 5.1–5.4` + `501 FS Oral communication` → **AT1 Part C** (presentation: walkthrough, feedback, lodgement, sign-off of A+B). `503 PC 4.2/4.3`, `505 PC 4.2` + `505 FS Oral communication` → **AT2** (build feedback + final sign-off). |
| **G11** — FS: reading, self-management, problem solving | — | **both (implicit)** | Co-evidenced across both ATs' technical deliverables and troubleshooting; marking guides note where each is naturally evidenced rather than assessing it separately. |
| **G12** — AC: required environment & resource access | — | **delivery env** | Provided by the scenario website + AWS Academy labs (vendor service provider, managed DB, serverless, pre-prepared code, IDE/CLI/SSH, reference data). Captured in the cluster delivery-environment spec, not as marked criteria. |
| **G13** — AC: assessor requirements | — | **institutional** | Satisfied by the institution's assessor-qualification policy; one statement per AT cover sheet. |

**KE distribution check.** AT1 Part A: `503 KE 3/4/6` (web-scale + microservice design). AT1 Part B: `501 KE 1/2/3/4/5/6` (DR — KE appendix; KE 6 = disaster detection/alerting). AT2: `503 KE 1/2/5`; `505 KE 1–11`. All 23 KE placed.

**PE distribution check.** AT1 Part A: `503 PE 1/2/5`. AT1 Part B: `501 PE 1/2/3`. AT2: `503 PE 3/4`, `505 PE 1/2/3/4`. All 12 PE placed.

**Verification:** every group G1–G13 has a row; every PE and KE item is allocated (G11–G13 are cross-cutting by design). No group is unaddressed.

---

## 6. Required authoring worklist

Everything here is **new authoring** unless marked *built* (no reuse provenance available — §4).

### AT1 — Cloud Expansion: Design & DR Plan
1. **Part A — Solution Design exemplar** (NEW) — assessor model: web-scale architecture design + microservice (audit-log) design, residency reflected as input, per-section UoC mapping (`ex.uoc`). Reuse the Solution Design document type.
2. **Part B — DR Plan exemplar** — *built* (`AT1-exemplar-dr-plan.docx`); **de-weave** the regulatory/microservice content (it currently relies on the India-log store) so it is pure ICTCLD501; that content moves to Part A.
3. **Part C — Presentation** (NEW) — the presentation brief + an exemplar deck (Business-Case-Presentation type), plus the observation/feedback/sign-off record covering Part A + Part B.
4. **Student template(s)** — DR Plan template *built*; add a **Solution Design student template** + the Part C presentation template/brief.
5. **AT1 Student task** (`AT1-…-Student.docx`) — task instructions, scenario brief, the Part A/B/C deliverable specs, the contextual KE question set, submission/conditions.
6. **AT1 Assessor guide** (`AT1-…-Assessor.docx`) — marking guide with **bidirectional UoC traceability**, the Part C observation checklist, KE Q&A model answers, sign-off records.

### AT2 — Cloud Microservice & IaC Implementation
7. **AT2 exemplar** (NEW) — model Deployment Report (mirrors CL1 AT2's shape, retargeted to the microservice + IaC + monitoring build).
8. **AT2 Student task** + **Assessor guide** — deployment-report deliverable spec (microservice build evidence, IaC deploy + own-template authoring, monitoring config, IaC user docs, test evidence, KE/reflection), build sign-off step, contextual KE set, bidirectional traceability.
9. **Provided artefacts (Appendices A & B of the AT2 documents)** — the predefined data-store template students operate in G5 (CloudFormation), the pre-prepared microservice code (`503 AC 4`), and the webhook payload contract. Embedded as appendices in the assessor and student instruments — not a separate lab pack.

### Cluster-level
10. **`assessment_plan.md`** — this document.
11. **`mappings/`** — the official per-unit Assessment Mapping `.docx` (501/503/505), generated as CL1's were (`scripts/populate_mapping_docs.py` pattern).
12. **Cluster cover / instructions** — single front document presenting the engagement narrative + the two-AT / three-part structure.
13. **Realign `consolidated_uoc.md`** — update its AT1 description from "Part A DR plan + appendices / Part B presentation" to the three-part shape (Part A Solution Design / Part B DR Plan / Part C presentation).
14. **The 503 web-scale practice on the LMS** (`lms-global-expansion`, the practice vehicle) — delivery, not assessment; deferred.

---

## 7. Open questions / TBDs

1. **503 global-serving practice vehicle** — **resolved:** the **LMS** (web-scale) is the practice vehicle; students practise the web-scale design/build on the `lms-global-expansion` engagement before assessing on the website. *(Resolved by the scenario-flow re-vehicling; no separate practice web app needed.)*
2. **Source-assessment reuse** — if the 501/503 standalone assessments surface, re-audit AT1/AT2 for reusable practical tasks before finalising (§4).
3. **AT1 working title + website label** — working title "Cloud Expansion: Design & DR Plan"; the website `s1-cl2-at1` state label currently reads "Disaster Recovery Plan" and may want broadening to reflect the design+plan scope. TBD.
4. **The two `[VERIFY]`s** — Kangan's exact AWS Academy lab product; legal/residency wording before student-facing docs.
5. **Pre-validation** — run the institutional Pre-Validation Tool over each AT before submission (as CL1 §7).

*Resolved 2026-06-06: (a) DR ≠ regulatory ≠ design — DR Plan is pure 501, the microservice sits in the Solution Design, residency is an input constraint; (b) AT1 is three parts (A Solution Design / B DR Plan / C presentation), AT2 is the Deployment Report; (c) KE — written appendices in each document + verbal contextual Q&A at AT1 Part C; (d) the light India-residency slice. See §1/§3.*

---

## 8. Critical-path next steps (if this plan is approved)

Not committed — natural sequencing only.

1. **Author AT1 Part A** — the Solution Design exemplar (web-scale + microservice), residency-as-input.
2. **De-weave AT1 Part B** — strip the regulatory/microservice material from the DR Plan exemplar so it is pure 501; verify it reads against the Part A design.
3. **Author AT1 Part C** — the presentation brief + exemplar deck + observation/sign-off record covering A+B.
4. **Derive the AT1 Student + Assessor instruments** from the three exemplars (bidirectional traceability + contextual KE set).
5. **Author AT2** (exemplar → Student + Assessor) + the assessor operational artefacts (IaC templates, microservice code, webhook contract).
6. **Realign `consolidated_uoc.md`** to the three-part AT1 shape.
7. Generate the `mappings/` Assessment Mapping docs; build a UoC-coverage validator mapping every item to a specific AT line/sub-task; run the Pre-Validation Tool; stakeholder review.

---

## Changelog

- **2026-06-06:** Initial draft (v1). Built on the settled four-topic / two-AT structure and the offshore-India scenario spine. Coverage map across AT1 (501 + 503-design) and AT2 (503-build + 505 + monitoring). CL2 noted as author-fresh (505 greenfield; 501/503 source assessments not located → Step-3 reuse audit blocked). KE evidencing settled (written appendices + verbal contextual Q&A at AT1 presentation).
- **2026-06-06 (restructure, v2):** Resolved DR ≠ regulatory ≠ design. **AT1 restructured to three parts** — Part A **Solution Design** (ICTCLD503 design, incl. the microservice), Part B **DR Plan** (ICTCLD501, pure), Part C **presentation** covering both (501 element 5, the approval gate). The microservice and its regulatory purpose move out of the DR plan into the Solution Design; **data residency is an input constraint, not a deliverable** (no compliance-plan artefact — no UoC requires one); the light India-residency slice confirmed. §1/§3/§5/§6/§8 rewritten; coverage map re-mapped to Part A/B/C + AT2 (all 23 KE, 12 PE re-checked). DR Plan exemplar flagged for de-weave; Solution Design (Part A) + presentation (Part C) exemplars added to the worklist. `consolidated_uoc.md`'s AT1 description noted for realignment.
- **2026-06-07 (v3):** AT2 recast to **Cloud Microservice & IaC Implementation** — the student operates a provided data-store template and authors the microservice from provided code; the provided artefacts are supplied as assessment appendices (no separate lab pack); the lab environment is chosen per activity (TBA pending the lab-product `[VERIFY]`). `501 KE 6` confirmed in AT2 monitoring.
- **2026-06-08 (v4 — re-vehicled):** **Assessment vehicle changed LMS → website; practice vehicle Accounting → LMS**, per the cross-cluster `scenario-flow.md` no-leakage decision (the website is assessed only in CL2; the LMS is the web-scale practice system). This **supersedes the v1–v3 "LMS as the assessment vehicle" framing** (Rule 4). Scenario/project references re-pointed (`lms-global-expansion` → `website-global-expansion`; `cluster-2-scenario.md` → `cluster-2-scenario-{assessment,practice}.md`); the 503 web-scale-practice TBD resolved (LMS). **Structure, AT shape, coverage map, and KE/PE distributions are unchanged — only the subject system's context changed.** The AT1/AT2 `.docx` instruments remain LMS-framed and are pending regeneration.
