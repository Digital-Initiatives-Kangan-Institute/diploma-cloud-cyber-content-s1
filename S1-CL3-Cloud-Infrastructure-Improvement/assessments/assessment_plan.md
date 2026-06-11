# S1-CL3 Cloud Infrastructure Improvement — Cluster Assessment Plan

> **STATUS: DRAFT.** Turns the cluster's settled design into the spec the AT instruments are built from, with the coverage proof that every UoC item lands in an assessment.
>
> **What is settled** (discussed and approved with Tim, 2026-06-07):
> - The cluster is one integrated engagement — **lead a team to improve a cloud system's infrastructure** — combining **ICTCLD504** (the technical improve-cycle) and **BSBXTW401** (leading the team that does it).
> - **The driver is YAT's India-campus partnership:** the improvement confirms Ledgerline is stable, reliable, fit for purpose, and **compliant with the applicable Indian regulatory requirements**, then proposes improvements in a **business case** and implements those approved. The engagement framing (MSA, Engagement Role Brief, Improvement Requirements, Consultation Notes, Indian Regulatory Requirements) is **provided** in the *Ledgerline Cloud Infrastructure Improvement* project; the analysis, compliance assessment, design, business case, and implementation are **student-authored**. The improvement is **open** — HA hardening is optional, depending on the team's analysis.
> - **Three ATs in an individual → group → individual rhythm:** **AT1 (individual)** Team Setup (the team plan) · **AT2 (group)** Analyse, Design & Approve (the whole technical analyse→design→business-case workstream, led) · **AT3 (individual)** Implement. **AT1 is 401-led (team/project setup); AT3 is 504-led (implementation); the two units integrate in AT2**, where the team analyses the baseline and designs the improvement together.
> - **Collaboration is assessed where it is real — the analysis-and-design phase (AT2)** — not the point-and-click implementation.
> - **Owned-dimension model:** **teams of four** — each student owns one improvement dimension (security / reliability / scalability / cost) through the AT2 **design** and the AT3 **implementation**, giving individual 504 *depth* evidence inside a group effort. The AT2 **analysis is an individual deliverable** (each student analyses the whole baseline and sets all four goals), so the holistic element-1 evidence (`504 PC 1.1`, `PC 1.6`) is individually valid; the design is owned-dimension, integrated by the team to cover all four.
> - **Team-leadership evidence:** each student **leads at least one team meeting** in AT2, captured by an **assessor observation checklist** (the primary performance evidence, incl. *managed a conflict*) + a **student reflection** appendix (secondary; carries the leadership KE). *How* the assessor stimulates a conflict is the assessor's conduct, out of the instrument's scope.
> - **Heavy reuse:** the improve-loop + lab-pack from **CL1 AT3**; the Solution Design + Deployment Report templates, instrument generators and scenario world from **CL2**.
>
> **What is TBD** (Rule 1/2): none blocking. *(Resolved — see §7: team model (teams of 4, formation at the assessor's discretion, rotating-chair led meetings); vehicle & `[ICTCLD504 KE 6]`; the provided improvement-engagement framing and role names in the `ledgerline-improvement` project; Step-1 UoC transcription; source-reuse accepted author-fresh.)*
>
> **Companion documents:** `consolidated_uoc.md` (every PC/FS/PE/KE/AC in 11 groups under 4 phases); `scenario/cluster-3-scenario-{assessment,practice}.md` + `scenario/scenario-flow.md`; `S1-CL2-.../assessments/assessment_plan.md` (the cluster this most closely parallels).

---

## 1. Integration approach

**Goal (as CL1/CL2):** one integrated cluster assessment that reads as a single engagement, not two units stapled together — a single scenario, a single team-lead voice, a single artefact thread.

**Shape:** the cluster runs as one continuous engagement — *set up the team → analyse, design & approve → implement & finalise*. The two units interweave: **504 is the work** (improve the architecture); **401 is how it is run** (lead the team that does it). It is, in effect, **CL1 AT3's improve-loop widened** (security + reliability + scalability + cost, not only HA), **run by a team**, **on a different existing system**. The units integrate in **AT2** — the team analyses and designs together, led — bookended by the 401 setup (AT1) and the 504 implementation (AT3).

**The thread:**
- **AT1 (individual) — Team Setup.** Each student authors the **Team Plan**: how they will lead the improvement team — objectives, per-member performance expectations, accountability, contingency/risk planning, and the role and task allocation. This is the project/team setup (BSBXTW401); **no technical analysis or design happens here**. The student works from the engagement's *provided* framing (MSA, Engagement Role Brief, Improvement Requirements, Consultation Notes, Indian Regulatory Requirements).
- **AT2 (group) — Analyse, Design & Approve.** The team does the whole technical workstream, led collaboratively across rotating-chair working meetings: each student **individually analyses** the baseline (review, evaluate, the **compliance assessment** against the Indian Regulatory Requirements, options, confirmed decisions, and all four goals + metrics — 504 el 1), then the team **designs** the improvement (each owns one dimension; integrated into one architecture — 504 el 2) and **presents the business case for the deploy sign-off**. The 401 leadership-in-action (coordinate, support, monitor) is evidenced here.
- **AT3 (individual) — Implement.** Each student **implements, tests and finalises their owned dimension** and obtains final sign-off (504 el 3–4).

**Two approval moments (UoC-faithful):** end of AT2 = **deploy sign-off** (`[ICTCLD504 PC 2.5]`); end of AT3 = **final sign-off** (`[ICTCLD504 PC 4.3]`).

**Knowledge evidence — contextual, on the student's own work:** the technical KE rides the analysis/design/deploy documents; the leadership KE (conflict resolution, teamwork challenges) rides the AT2 **reflection** appendix. No abstract recall.

---

## 2. Scenario

**Reuse the YAT world.** By CL3 YAT's systems are in the cloud; **Ledgerline** (the Accounting system) sits at a **single-AZ baseline** (on-prem in CL1 → migrated to single-AZ cloud under the completed *Accounting System Cloud Migration* engagement → improved in CL3). The engagement is **triggered by YAT's India-campus partnership**: MTS is engaged to confirm Ledgerline's cloud infrastructure is **stable, reliable, fit for purpose, and compliant with the applicable Indian regulatory requirements**, and to **improve it** across security, reliability, scalability and cost. The student is promoted to **MTS team lead** of the improvement team; the team **analyses** the baseline, **proposes** improvements in a **business case**, and **implements** those YAT approves. The improvement is **open** — whether it includes HA hardening depends on the team's analysis.

**Provided framing (not the answer).** The *Ledgerline Cloud Infrastructure Improvement* project supplies the engagement framing — Master Services Agreement, Engagement Role Brief, Improvement Requirements (outcome objectives), ICT Manager Consultation Notes, and Indian Regulatory Requirements (the YAT Compliance area's determination of the applicable DPDP / CERT-In / financial-records obligations). These set up the work **without pre-supplying it**: the team's **requirements & architecture analysis, compliance assessment, improvement design, business case, and implementation are all student-authored**. The legal interpretation is owned by YAT Compliance; the team designs the infrastructure to the requirements.

**Vehicle (per `scenario-flow.md`):** CL3 **assesses on Ledgerline** (single-AZ cloud — the "already in the cloud, now improve it" system) and **practises on the website** (students rehearse the improve-loop on the website before being assessed on Ledgerline). *(Forced by the no-leakage invariant: the website is assessed in CL2, so it cannot also be CL3's assessed system.)* **`[ICTCLD504 KE 6]`** (object storage for static web sites) is evidenced as a **contextual knowledge question** in AT2 — e.g. *"How does the accounting system differ from a system that needs to store objects such as images (for example, a website), and how would you provision that storage if it were needed?"* The student reasons by contrast from their own Ledgerline system; KE 6 is *knowledge*, so this evidences it cleanly without Ledgerline itself having to use static-web object storage.

**The team:** a **real student group of four** (the MTS improvement team) — one member per improvement dimension (security / reliability / scalability / cost). AT1 evidences each student's **team planning** individually; in AT2 each student **individually analyses** the baseline and the group **designs** the improvement (each owning a dimension and leading, rotating chair); AT3 is each student's individual implementation of their dimension.

**Baseline:** Ledgerline's **current single-AZ cloud infrastructure** is documented in the `s1-cl3-at1` scenario state — the **Accounting Baseline Solution Design** and the cloud ICT records (application specification, operational costing, infrastructure specifications, single-AZ network topology) — and supplied as a deployable **baseline lab-pack** (the CL1 AT3 pattern, re-pointed at Ledgerline). Students analyse it, improve it, deploy and test the improvements.

---

## 3. Cluster assessment structure

| Component | Working title | Mode | Format | Unit focus |
|---|---|---|---|---|
| **AT1** | Team Setup | **Individual** | Team Plan (objectives, performance expectations, accountability, contingencies, role & task allocation) | **BSBXTW401** el 1 + el 2 (allocate) |
| **AT2** | Analyse, Design & Approve | **Group** | Individual Requirements & Architecture Analysis + owned-dimension Solution Design + business case + led-meeting observation / reflection / performance review + approval presentation | **ICTCLD504** el 1 + el 2; **BSBXTW401** el 2–4 |
| **AT3** | Implementation | **Individual** | As-deployed Deployment Report (the student's dimension) | **ICTCLD504** el 3–4 |

**AT1 — Team Setup (individual).** Each student authors the **Team Plan** — how they will lead the improvement team (distinct from the *provided* Engagement Role Brief, which sets the consulting roles and reporting). No technical analysis or design happens in AT1; that is AT2.
- **Team Plan** — team objectives & responsibilities, per-member performance expectations and behaviours, accountability strategies, contingency/risk planning, and the role and task allocation. → `[BSBXTW401 el 1]` + el 2 (allocate) + `[PE 1]`.

**AT2 — Analyse, Design & Approve (group).** The team does the whole technical workstream — analyse, design, business-case and approve — led collaboratively across a series of rotating-chair working meetings.
- **Requirements & architecture analysis (individual deliverable)** — each student individually reviews the supplied baseline, evaluates it and its business impact (incl. **assessing compliance against the provided Indian Regulatory Requirements**), weighs options, confirms decisions, and sets the security / reliability / scalability / cost goals + performance metrics. Authored individually so the holistic element-1 evidence is valid per student. → `[ICTCLD504 el 1]`, `[PE 1` assess`]`, `[PE 3]`.
- **Owned-dimension design** — each student designs the improvement for their dimension (addressing their analysis goals and any compliance gaps); the team integrates them into one architecture. → `[ICTCLD504 el 2]` (PC 2.1–2.3), `[PE 1` improve`]`.
- **Led meetings** — AT2 runs as **rotating-chair working meetings**; each student leads/facilitates at least one. The assessor records a **team-leadership observation checklist** (communicate objectives, allocate/instruct, facilitate collaboration, coach/support, resolve a task issue, **manage a conflict**). → `[BSBXTW401 el 2–3]`, `[PE 2, PE 5]`. **Primary** leadership evidence.
- **Reflection appendix** — each student reflects on 2 conflicts/challenges (what happened, how handled, learned, improve next time). → `[BSBXTW401 KE 5, KE 10]`, `[FS Interact with others]`. **Secondary/backup** evidence.
- **Performance review** — each student reviews the team's performance on their workstream (measure vs plan, feedback, development opportunities, action plans). → `[BSBXTW401 el 4]`, `[PE 3, PE 4]`.
- **Approval presentation** — the team presents the **improvement business case** for the **deploy sign-off**. → `[ICTCLD504 PC 2.4–2.5]`, `[FS Oral communication]`.

**AT3 — Implementation (individual).** Each student deploys their owned dimension's improvement to the lab, monitors/tests it against the metrics and goals, applies refinements, and documents the **as-deployed** result (changes vs the approved design + test results), describes a **long-term improvement strategy**, and obtains **final sign-off**. → `[ICTCLD504 el 3–4]`, `[PE 2, PE 4, PE 5]`.

**Template basis:** AT2's **Requirements & Architecture Analysis** uses a new **Architecture Analysis** document type — the analysis that *feeds* the design, not a design itself (this is the fix for the earlier "Solution Design in AT1" conflation); AT2's **owned-dimension design** uses the **Solution Design** type (CL2); AT3 reuses the **Deployment Report** type (CL2). The **Team Plan** (AT1), the **Architecture Analysis** template, the **observation checklist**, the **reflection** appendix and the **performance-review** template are new.

---

## 4. Authoring basis / provenance

**CL3 is the lightest cluster with the heaviest reuse.** The engagement workflow (analyse → design → approve → deploy → test → document → sign-off) is structurally CL1 AT3 + CL2, re-pointed at Ledgerline with a team-leadership overlay.

**Reusable / already proven:**
- **CL1 AT3** — the improve-an-existing-baseline shape + the **lab-pack standard** (`documentaion/lab-pack-standard.md`) for the supplied Ledgerline baseline.
- **CL2** — the **Solution Design** + **Deployment Report** templates and their generators; the Kangan **Project Assessment** instrument generators; the **scenario world** + intranet; the validators.

**New authoring (the ~30% that is CL3-specific):**
1. The **BSBXTW401 instruments** — the Team Plan template, the **led-meeting observation checklist**, the **reflection** appendix prompt, the performance-review template.
2. The **Ledgerline baseline lab-pack** (the current single-AZ cloud infra to improve).
3. The **Ledgerline scenario** context (the improvement engagement, the team-lead role).

**Author-fresh (accepted):** no standalone ICTCLD504 / BSBXTW401 source assessments were located; CL3 is authored fresh by design. If one surfaces it may be audited for reusable tasks, but it is not a blocker.

---

## 5. Group coverage map

Every group in `consolidated_uoc.md` (82 items) mapped to where it is covered.

| Group | Phase | Where | Mode | How evidenced |
|---|---|---|---|---|
| **G1** — Analyse cloud architecture (504 el 1) | 2 | **AT2** | individual deliverable | Each student's **individual** Requirements & Architecture Analysis of the supplied baseline, **including the compliance assessment against the provided Indian Regulatory Requirements** (rides on PC 1.2 business-impact + the legislative-requirements input — no new item). Individual so the holistic element-1 evidence (PC 1.1, PC 1.6 — all four goals) is valid per student. `504 PC 1.1–1.6`, `PE 1` (assess), `PE 3` (goals), `KE 1/2/3`. |
| **G2** — Plan team outcomes (401 el 1) | 1 | **AT1** | individual | Team Plan — objectives, performance expectations, accountability, contingencies. `401 PC 1.1–1.4`, `KE 1/2/9`. |
| **G3** — Design & improve architecture (504 el 2) | 2 | **AT2** | group (owned dimension) | Per-dimension improvement design (addressing the AT1 goals, incl. any compliance gaps) + integrated architecture + **business case** presented for sign-off. `504 PC 2.1–2.5`, `PE 1` (improve), `KE 4/5/6/8/9`. |
| **G4** — Coordinate the team (401 el 2) | 1–2 | **AT1 + AT2** | individual / observed | Allocate tasks (AT1 plan, `PE 1`); communicate + facilitate collaboration (AT2 led meetings). `401 PC 2.1–2.4`, `KE 3/6/7`. |
| **G5** — Deploy, monitor & test (504 el 3) | 3 | **AT3** | individual | Deploy/monitor/test/refine the owned dimension. `504 PC 3.1–3.4`, `PE 2/4`, `KE 7/10`. |
| **G6** — Support the team (401 el 3) | 2 | **AT2** | observed + reflection | Led-meeting observation (coach, resolve issues, **manage conflict**) + reflection. `401 PC 3.1–3.4`, `PE 2/5`, `KE 4/5/8/10`. |
| **G7** — Finalise improvements (504 el 4) | 3 | **AT3** | individual | As-deployed report + long-term strategy + final sign-off. `504 PC 4.1–4.3`, `PE 5`. |
| **G8** — Monitor team performance (401 el 4) | 2 | **AT2** | individual | Performance review of the workstream team. `401 PC 4.1–4.4`, `PE 3/4`. |
| **G9** — Foundation skills | — | **all ATs (implicit)** | — | Co-evidenced across the deliverables, meetings and presentation; marking guides note where each is naturally evidenced. |
| **G10** — Assessment conditions: environment & resource access | — | **delivery env** | — | Provided by the scenario website + AWS Academy labs (cloud vendor, managed DB, console/CLI, IDE, SSH/RDP, requirements) + the simulated-environment condition. |
| **G11** — Assessment conditions: assessor requirements | — | **institutional** | — | Satisfied by the institution's assessor-qualification policy; one statement per AT cover sheet. |

**PE distribution check.** AT1: `401 PE 1`. AT2: `504 PE 1` (assess + improve), `504 PE 3`, `401 PE 2/3/4/5`. AT3: `504 PE 2/4/5`. All 10 PE placed.

**KE distribution check.** AT1: `401 KE 1/2/9`. AT2: `504 KE 1/2/3` (analysis) + `504 KE 4/5/6/8/9` (design); `401 KE 3/4/5/6/7/8/10`. AT3: `504 KE 7/10`. All 20 KE placed.

**Verification:** every group G1–G11 has a row; every PC, PE and KE is allocated; FS (G9) cross-cutting; AC is the environment (G10) + the institutional assessor condition (G11). No item is unaddressed.

---

## 6. Required authoring worklist

### AT1 — Team Setup
1. **Team Plan template + exemplar** (NEW — BSBXTW401) — objectives, per-member performance expectations, accountability, contingencies, role & task allocation. *(Distinct from the provided Engagement Role Brief.)* — **done.**
2. **AT1 Student + Assessor instruments** (individual) — the Team Plan deliverable spec; marking guide with bidirectional UoC traceability.

### AT2 — Analyse, Design & Approve
3. **Architecture Analysis template + exemplar** (NEW — 504 el 1) — the **individual** baseline analysis (review, evaluate, compliance assessment, options, confirmed decisions, goals + metrics). The analysis that *feeds* the design — **not** a Solution Design.
4. **Improvement (Solution) Design exemplar** (504 el 2) — reuse the Solution Design type; owned-dimension structure, integrated.
5. **Led-meeting observation checklist** (NEW — BSBXTW401) — the leadership behaviours the assessor records, incl. *managed a conflict*.
6. **Reflection appendix prompt** (NEW) + **performance-review template** (NEW).
7. **Approval presentation** brief + observation/sign-off record (reuse CL2 Part C pattern).
8. **AT2 Student + Assessor instruments** (group) — the individual analysis + the owned-dimension design + business case + the individual observation/reflection/review evidence.

### AT3 — Implementation
9. **As-deployed Deployment Report exemplar** (504 el 3–4) — reuse the Deployment Report type.
10. **AT3 Student + Assessor instruments** (individual).
11. **Assessor operational artefacts** — the **Ledgerline baseline lab-pack** (the current single-AZ cloud infra), provided as appendices / lab artefacts.

### Cluster-level
12. **`assessment_plan.md`** — this document.
13. **`mappings/`** — per-unit Assessment Mapping `.docx` (504, 401).
14. **Realign the scenario** — *done:* the **Ledgerline Cloud Infrastructure Improvement** engagement (provided framing: MSA, Engagement Role Brief, Improvement Requirements, Consultation Notes, Indian Regulatory Requirements) is authored in the website repo's `ledgerline-improvement` project, and the website-repo `s1-cl3-at1` state surfaces the Ledgerline single-AZ baseline (Accounting Baseline Solution Design + cloud ICT records). The website **practice** engagement (`website-improvement`) is the parallel.

---

## 7. Open questions / TBDs

All assessment-design questions are resolved; the items below record the decisions and the one downstream gate.

1. **Team model — resolved (2026-06-11):** **teams of 4**, one student per improvement dimension (security / reliability / scalability / cost), so the team's integrated architecture addresses all four. **Team formation is at the assessor's discretion** — assign, or let students self-form, per the class and circumstances. AT2 runs as **rotating-chair working meetings**: each is chaired by a different member so every student leads at least one, with the assessor completing the leadership observation checklist for the chair.
2. **Vehicle & `[ICTCLD504 KE 6]` — resolved:** assess on Ledgerline (single-AZ cloud), practise on the website (per `scenario-flow.md`, no-leakage); KE 6 evidenced as the contextual object-storage contrast question (see §2).
3. **UoC transcription — resolved (2026-06-11):** Step-1 validation — both `_Complete_` `.md` are an exact word-level match to source.
4. **Source-assessment reuse — accepted author-fresh:** no standalone 504 / 401 source assessments were located; CL3 is authored fresh **by design** (the integrated cross-cluster scenario is the intended approach, not a reuse gap). If a source ever surfaces it may be audited for reusable tasks, but it is not a blocker.
5. **Pre-validation — downstream gate (not a dev-phase task):** the institutional Pre-Validation Tool is run by the validation team after the instruments are authored; it is not part of building the plan or the instruments.

---

## 8. Critical-path next steps (if this plan is approved)

Not committed — natural sequencing only.

1. **Vehicle confirmed + scenario authored** — assess on Ledgerline, practise on the website (per `scenario-flow.md`); the provided improvement-engagement framing and the single-AZ baseline are built in the website repo (`ledgerline-improvement`, `website-improvement`, and the carried-forward Accounting Baseline Design).
2. **Author AT1** — the Team Plan template + exemplar (**done**); derive the individual instruments (the Team Plan deliverable).
3. **Author AT2** — the **Architecture Analysis** template + exemplar (the individual baseline analysis, incl. the compliance assessment) and the **Improvement (Solution) Design** exemplar (owned-dimension); the **observation checklist** + **reflection** + **performance review**; the approval presentation; derive the group instruments.
4. **Author AT3** — the as-deployed Deployment Report exemplar; derive the individual instruments; build the **Ledgerline baseline lab-pack**.
5. **Realign the scenario** + generate the `mappings/` docs; build a UoC-coverage validator; run the Pre-Validation Tool.

---

## Changelog

- **2026-06-07:** Initial draft (v1). Built on the settled integrated design — *lead a team to improve a cloud system's infrastructure* — with the three-AT individual → group → individual rhythm (AT1 setup / AT2 group design / AT3 implement), the owned-dimension technical model, and the team-leadership evidence approach (led-meeting observation checklist + reflection + performance review). Coverage mapped across both units (all 80 items; 10 PE, 20 KE placed). Heavy reuse from CL1 AT3 (improve-loop + lab-pack) and CL2 (Solution Design + Deployment Report). Vehicle (website) and team-model specifics flagged TBD.
- **2026-06-08 (v2 — re-vehicled):** **Vehicle resolved per `scenario-flow.md`: CL3 assesses on Ledgerline (single-AZ cloud), practises on the website.** (v1 had the website as the system to improve; the no-leakage invariant moves *assessment* to Ledgerline since the website is assessed in CL2, and makes the website CL3's *practice* vehicle.) All vehicle context re-pointed website→Ledgerline (engagement, baseline lab-pack, scenario). **Structure, AT rhythm, coverage map and KE/PE distributions unchanged — only the subject system changed.** `[ICTCLD504 KE 6]` resolved — evidenced as a contextual knowledge question contrasting Ledgerline with an object-storage-dependent system (e.g. a website).
- **2026-06-11 (v3 — AC consistency):** Aligned the Assessment Conditions treatment with CL1/CL2. The trailing assessor-requirements clause in each unit is now tagged as that unit's last AC item (`[ICTCLD504 AC 8]`, `[BSBXTW401 AC 2]`) in `consolidated_uoc.md`, collected in a new **G11 — assessment conditions: assessor requirements** (mirroring CL2's G13). Item total **80 → 82** (AC 8 → 10). §5 coverage map splits **G10** (environment & resource access) from **G11** (assessor requirements); the companion-doc group count, the §5 item count, and the verification line are updated to match. **Structure, AT shape, and PE/KE distributions unchanged.** Revalidated: `validate_consolidated.py --assessor-ac` → 82/82 PASS.
- **2026-06-11 (v4 — scenario alignment):** Aligned the plan with the now-built CL3 scenario. Added the **India-campus partnership driver** and the **compliance dimension** (confirm Ledgerline is stable / reliable / fit for purpose / **compliant with the Indian regulatory requirements**, then business-case and implement approved improvements) — woven into §2, §1, §3 and the G1/G3 coverage notes as a driver riding on existing items (no UoC item added; allocation unchanged). Recorded the **provided-vs-student-authored boundary**: the engagement framing (MSA, Engagement Role Brief, Improvement Requirements, Consultation Notes, Indian Regulatory Requirements) is provided in the `ledgerline-improvement` project; the analysis, compliance assessment, design, **business case**, and implementation are student-authored. Renamed the AT1 student deliverable **"team plan / Role Brief" → "Team Plan"** to disambiguate it from the provided Engagement Role Brief. Marked resolved: scenario realign (§6.14, §8.1), Step-1 transcription (§7.4), scenario specifics (header TBD). **UoC coverage, 11-group structure, AT rhythm, and PE/KE distributions unchanged — still 82/82.**
- **2026-06-11 (v5 — team model + TBD cleanup):** Resolved the team-model specifics — **teams of 4** (one student per improvement dimension, so the integrated architecture addresses all four), **formation at the assessor's discretion**, AT2 run as **rotating-chair working meetings** (each student chairs ≥1; assessor observes the chair). Cleaned §7: removed the delivery-sequencing item; reframed source-assessment reuse as **accepted author-fresh** and pre-validation as a **downstream post-dev gate**; the remaining items record resolved decisions. No UoC, coverage, or AT-structure change.
- **2026-06-11 (v6 — AT restructure):** Resolved a real misalignment — the AT1 "Solution Design (analysis scope)" framing implied a *design* in AT1, but the design is AT2. **Restructured the three ATs:** **AT1 = Team Setup** (the Team Plan only — BSBXTW401 el 1 + the allocation slice of el 2; no technical work); **AT2 = Analyse, Design & Approve** (the whole technical workstream — `504 el 1` analysis + `504 el 2` design + business case — plus the 401 leadership-in-action, el 2–4); **AT3 = Implement** (`504 el 3–4`). The only coverage change is **`504 el 1` (G1) moving AT1 → AT2**; to keep the holistic element-1 evidence individually valid, the **AT2 analysis is an individual deliverable** (each student analyses the whole baseline and sets all four goals) while the design stays owned-dimension. The analysis now uses a dedicated **Architecture Analysis** document type (not the Solution Design template — the source of the conflation). §§header/1/2/3/5/6/8 re-pointed; §5 G1 row moved to AT2 and the PE/KE distribution checks re-pointed (`504 PE 1/PE 3` and `504 KE 1/2/3` now AT2). **All 82 items still placed; PE/KE all allocated; individual → group → individual rhythm preserved.** Consequence to note: AT1 is now 401-only and AT3 is 504-only — the two units integrate in AT2 and across the single scenario, rather than in every AT.
