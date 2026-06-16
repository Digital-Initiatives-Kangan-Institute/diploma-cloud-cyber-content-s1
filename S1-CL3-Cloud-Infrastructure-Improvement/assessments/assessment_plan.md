# S1-CL3 Cloud Infrastructure Improvement — Cluster Assessment Plan

> **STATUS: DRAFT.** Turns the cluster's settled design into the spec the AT instruments are built from, with the coverage proof that every UoC item lands in an assessment.
>
> **What is settled** (the AT model was reasoned out from the two units' requirements and approved with Tim, 2026-06-16):
> - The cluster is one integrated engagement — **a team improves a cloud system's infrastructure** — combining **ICTCLD504** (the technical improve-cycle, individual) and **BSBXTW401** (leading the team, group).
> - **The seam between individual and group work is the *YAML write*, not the technical deliverable.** Of the three jobs — design / write the IaC / deploy — **design must be individual** (504 el 1–2) and **deploy must be individual** (504 el 3), but **writing the CloudFormation is NOT assessed by 504** (that is ICTCLD505, done in CL2). So the write is the one job free to be divided — and dividing it **by component** is what gives BSBXTW401 its authentic, individually-accountable team work (allocate by expertise, coordinate the integration, monitor each member, manage conflict) **without touching any individual 504 evidence.**
> - **No business case.** Neither UoC requires one, and a business case would precede the design, not follow it. The 504 approval gate is the **AT1 design presentation** (PC 2.4/2.5); the cost-versus-benefit justification rides inside the Solution Design (cost is one of the four design concerns).
> - **Three ATs:** **AT1 (individual) Design** (`504 el 1–2`) · **AT2 (group) Team Implementation** (`401 el 1–4`, the divided write) · **AT3 (individual) Implement** (`504 el 3–4`, deploy + operate the whole system).
> - **Improvement across all four optimisation concerns** — security, reliability, scalability, cost — is required *per candidate* in the **design** (`504 PC 1.6 / 2.3`) and demonstrated *per candidate* on the deployed **whole system** in AT3 (`504 PC 3.3`). **Scalability = the ability to scale on demand (elastic capacity, demonstrable by a controlled test), not a forecast of load growth** — consistent with IR-2 (design to scale = sound engineering; over-provisioning = the gold-plating IR-2 forbids).
> - **Multi-AZ HA** is the reliability improvement (proportionate for a depended-on finance system); the design is provisioned as **parameterised CloudFormation**; a **light India residency slice** (CERT-In logs + Companies-Act books-of-account only) satisfies IR-3 with the main system staying in Sydney (DPDP permits).
> - **The agreed "to be" design is provided.** AT1 each student designs individually (assessed); the engagement then adopts a single **agreed improvement Solution Design** (provided), which is the spec AT2 encodes into IaC and AT3 deploys. A known-good **reference combined template** is held by the assessor so a broken team integration can never block an individual's AT3 deploy/operate evidence.
>
> **What is TBD:** `[TBD — needs discussion: the component breakdown of Ledgerline]` — confirm the ~4 IaC modules (candidate: **network / compute / database / storage**) that are the AT2 write-allocation units (one per team member, teams of four). With the write divided (not the demonstration), each module need only be a sensible, separable IaC unit — it no longer has to independently carry all four concerns, since AT3 demonstrates the whole system.
>
> **Companion documents:** `consolidated_uoc.md` (every PC/FS/PE/KE/AC in 11 groups under 4 phases); `scenario/cluster-3-scenario-{assessment,practice}.md` + `scenario/scenario-flow.md`; `S1-CL2-.../assessments/assessment_plan.md` (the cluster this most closely parallels).

---

## 1. Integration approach

**Goal (as CL1/CL2):** one integrated cluster assessment that reads as a single engagement on one system, not two units stapled together.

**Shape:** *design the improvement (individual) → plan and build it as a team (group) → deploy and operate it (individual)*, all on Ledgerline. The two units meet without colliding because they are evidenced on **different jobs**: 504 owns the **design** (AT1) and the **deploy-and-operate** (AT3), both individual; 401 owns the **team write** (AT2), the only job that divides cleanly and is free to divide (the write is a 505 skill, not a 504 one). It is **CL1 AT3's improve-loop widened** (security + reliability + scalability + cost) and **run by a team**.

**The thread:**
- **AT1 (individual) — Design.** Each student analyses the Ledgerline baseline and designs the whole improvement (all four concerns), then presents it for review and sign-off. Full individual `504 el 1–2`.
- **AT2 (group) — Team Implementation.** The team plans the work, then writes the CloudFormation for the **agreed** design — **divided by component**, integrated into one deployable template — across individually-led working meetings. The full `401` leadership cycle (plan → coordinate → support → monitor) rides on this divided, individually-accountable work. *(The write itself is not 504-assessed.)*
- **AT3 (individual) — Implement.** Each student deploys the combined template in their own lab and demonstrates/tests/refines/documents the **whole** improved system, then obtains final sign-off. Full individual `504 el 3–4`.

**Approval moments (UoC-faithful):** **AT1 Part B** = design sign-off, *obtain sign off to proceed* (`[ICTCLD504 PC 2.5]`, individual); **AT2 Part B** = team validates the combined template (a project/quality gate, not a 504 PC); **AT3** = final sign-off (`[ICTCLD504 PC 4.3]`, individual).

**Knowledge evidence — contextual, on the student's own work:** technical KE rides the AT1 design and the AT3 deployment documents; leadership KE (conflict, teamwork challenges) rides the AT2 reflection. No abstract recall.

---

## 2. Scenario

**Reuse the YAT world.** By CL3 YAT's systems are in the cloud; **Ledgerline** (the Accounting system) sits at a **single-AZ baseline** (on-prem in CL1 → migrated to single-AZ cloud → improved in CL3). The engagement is **triggered by YAT's India-campus partnership**: MTS is engaged to confirm Ledgerline's cloud infrastructure is **stable, reliable, fit for purpose, and compliant with the applicable Indian regulatory requirements**, and to **improve it** across security, reliability, scalability and cost. The student team designs the improvement, builds it as code, and deploys it. The improvement is **open** — its shape follows the analysis, proportionate to an internal business-hours finance system (IR-2).

**Provided framing (not the answer).** The *Ledgerline Cloud Infrastructure Improvement* project supplies the engagement framing — Master Services Agreement, Engagement Role Brief, Improvement Requirements (IR-1…7), ICT Manager Consultation Notes, and Indian Regulatory Requirements. Each student's **analysis, compliance assessment and improvement design** (AT1) are student-authored. The engagement then adopts a single **agreed improvement Solution Design** (provided), which AT2 encodes into IaC and AT3 deploys. The legal interpretation is owned by YAT Compliance; the team designs and builds the infrastructure to the requirements.

**Vehicle (per `scenario-flow.md`):** CL3 **assesses on Ledgerline** (single-AZ cloud) and **practises on the website**. *(No-leakage: the website is assessed in CL2.)* **`[ICTCLD504 KE 6]`** (object storage for static web sites) is evidenced as a **contextual knowledge question** in the AT1 design — contrasting Ledgerline with an object-storage-dependent system.

**The team:** a **student group of four** (the MTS improvement team) — **one IaC component each** for the AT2 write. AT1 is each student's individual design; AT3 is each student's individual deploy-and-operate of the whole.

**Baseline:** Ledgerline's single-AZ cloud infrastructure (`s1-cl3-at1` state — the Accounting Baseline Solution Design + cloud ICT records) — internal-only (Site-to-Site VPN), ~60 users, business-hours, EC2+ASG (single-AZ) / internal ALB / RDS for SQL Server (single-AZ) / S3 / VPC. Supplied as a deployable baseline lab-pack.

---

## 3. Cluster assessment structure

| Component | Working title | Mode | Format | Unit focus |
|---|---|---|---|---|
| **AT1** | Design | **Individual** | **A** Solution Design (analyse + design the whole improvement) · **B** design presentation + sign-off | **ICTCLD504** el 1 + el 2 |
| **AT2** | Team Implementation | **Group** | **A** project/team plan + task allocation · **B** execution — write the agreed design's CloudFormation (divided by component, integrated), individually-led meetings, team sign-off gate | **BSBXTW401** el 1–4 |
| **AT3** | Implement | **Individual** | Deploy the combined template + demonstrate/test/refine/document the **whole system** + final sign-off | **ICTCLD504** el 3 + el 4 |

**AT1 — Design (individual).**
- **Part A — Solution Design.** Analyse the baseline (review, evaluate, business impact, **compliance assessment** against the Indian Regulatory Requirements, options, confirmed decisions, the security/reliability/scalability/cost goals + metrics — `504 el 1`), then design the whole improvement across all four concerns, documented and justified incl. the cost-versus-benefit case (`504 el 2.1–2.3`). Reuses the CL2 **Solution Design** type — its *Review of the Existing Architecture* section carries the analysis.
- **Part B — Design presentation.** Present the proposed architecture for review, field questions, and obtain sign-off to proceed. → `[504 PC 2.4, 2.5]`, `[FS Oral communication]`. An observed individual oral event.

**AT2 — Team Implementation (group).**
- **Part A — Plan.** The team plan (common objectives, per-member performance expectations, accountability, contingencies) and the project/implementation plan, **allocating one IaC component to each member** by expertise. → `[BSBXTW401 el 1]`, `[el 2.2]`, `[PE 1]`.
- **Part B — Execution.** The team writes the CloudFormation for the **agreed** design — each member authors their allocated component, integrated into one deployable template — across **individually-led working meetings**. The lead coordinates, facilitates collaboration, coaches/supports, monitors each member against the plan, and **manages a conflict** (the assessor records the observation checklist for each chair); the team validates the combined template at a sign-off gate. → `[BSBXTW401 el 2–4]`, `[PE 2–5]`, `[FS Interact with others]`. *(The CloudFormation authoring is the team-work vehicle; it is **not** assessed against ICTCLD504 — that is ICTCLD505, evidenced in CL2.)*

**AT3 — Implement (individual).** Each student deploys the combined (agreed, validated) template in their own lab, monitors/measures it against the metrics and goals, **tests and demonstrates security, reliability, scalability and cost** on the deployed whole system, applies short-term refinements from the results, documents the **as-deployed** result + a **long-term improvement strategy**, and obtains **final sign-off**. → `[504 el 3–4]`, `[PE 2/4/5]`. *(A known-good reference combined template is available as a fallback so a team integration failure cannot block this individual evidence.)*

**Template basis:** AT1 reuses the **Solution Design** type (CL2). AT3 reuses the **Deployment Report** type (CL2). **New** = the AT2 **project/team plan** + **CloudFormation write** deliverable spec, the **led-meeting observation checklist**, and the **reflection** prompt. No new "Architecture Analysis" type (the analysis is the Solution Design's review section); no business case.

---

## 4. Authoring basis / provenance

**CL3 is the lightest cluster with the heaviest reuse.** The technical workflow (analyse → design → deploy → test → document → sign-off) is structurally CL1 AT3 + CL2, re-pointed at Ledgerline with a team-leadership overlay on the IaC write.

**Reusable / already proven:**
- **CL1 AT3** — the improve-an-existing-baseline shape + the **lab-pack standard** (docs/lab-pack-standard.md) for the supplied Ledgerline baseline and the deployable improved template.
- **CL2** — the **Solution Design** (AT1) + **Deployment Report** (AT3) templates/generators; the Kangan **Project Assessment** instrument generators; the **scenario world** + intranet; the validators. Students already learned IaC authoring in CL2 (505), so the AT2 write reuses an existing skill (it is not re-assessed).

**New authoring (the CL3-specific part):**
1. The **AT1 Solution Design exemplar** — the agreed "to be" improvement design (also the assessor model). Generated; a stripped, in-world copy is the design **provided** to the AT2 team.
2. The **AT2 instruments** — the project/team-plan deliverable spec, the **CloudFormation write** deliverable (divided by component + integration), the **led-meeting observation checklist**, the **reflection** prompt.
3. The **AT3** as-deployed Deployment Report exemplar + the **deployable improved lab-pack** (the combined template + the assessor reference fallback).

**Author-fresh (accepted):** no standalone ICTCLD504 / BSBXTW401 source assessments located; CL3 is authored fresh by design.

---

## 5. Group coverage map

Every group in `consolidated_uoc.md` (82 items) mapped to where it is covered under the AT model above.

| Group | Phase | Where | Mode | How evidenced |
|---|---|---|---|---|
| **G1** — Analyse cloud architecture (504 el 1) | 1 | **AT1 Part A** | individual | Solution Design *Review of the Existing Architecture* + findings — review, evaluate, business impact, compliance assessment, options, confirmed decisions, all four goals + metrics. `504 PC 1.1–1.6`, `PE 1` (assess), `PE 3`, `KE 1/2/3`. |
| **G2** — Plan team outcomes (401 el 1) | 2 | **AT2 Part A** | group | Team plan — objectives, performance expectations, accountability, contingencies. `401 PC 1.1–1.4`, `KE 1/2/9`. |
| **G3** — Design & improve architecture (504 el 2) | 1 | **AT1 Part A + B** | individual | Whole-improvement design across all four concerns + documented/justified incl. cost-benefit (Part A); presented for review + sign-off (Part B). `504 PC 2.1–2.5`, `PE 1` (improve), `KE 4/5/6/8/9`. |
| **G4** — Coordinate the team (401 el 2) | 2 | **AT2 Part A + B** | group / observed | Allocate components by expertise (Part A); communicate + facilitate collaboration across the write (Part B led meetings). `401 PC 2.1–2.4`, `KE 3/6/7`. |
| **G5** — Deploy, monitor & test (504 el 3) | 3 | **AT3** | individual | Deploy the combined template; monitor/test/demonstrate all four concerns on the whole system; refine. `504 PC 3.1–3.4`, `PE 2/4`, `KE 7/10`. |
| **G6** — Support the team (401 el 3) | 2 | **AT2 Part B** | observed + reflection | Coaching, support, issue-resolution and **conflict management** during the write, observed + the reflection. `401 PC 3.1–3.4`, `PE 2/5`, `KE 4/5/8/10`. |
| **G7** — Finalise improvements (504 el 4) | 3 | **AT3** | individual | As-deployed report + long-term strategy + final sign-off. `504 PC 4.1–4.3`, `PE 5`. |
| **G8** — Monitor team performance (401 el 4) | 2 | **AT2 Part B** | individual | Measure each member's component contribution against the plan, feedback, development opportunities, action plans. `401 PC 4.1–4.4`, `PE 3/4`. |
| **G9** — Foundation skills | — | **all ATs (implicit)** | — | FS Oral → AT1 Part B; FS Interact with others → AT2 Part B; reading/problem-solving/self-management co-evidenced across the deliverables. |
| **G10** — Assessment conditions: environment & resource access | — | **delivery env** | — | Scenario website + AWS Academy labs (cloud vendor, managed DB, console/CLI, IDE, SSH/RDP, requirements) + simulated-environment condition. |
| **G11** — Assessment conditions: assessor requirements | — | **institutional** | — | Institution's assessor-qualification policy; one statement per AT cover sheet. |

**PE distribution check.** AT1: `504 PE 1` (assess + improve), `504 PE 3`. AT2: `401 PE 1/2/3/4/5`. AT3: `504 PE 2/4/5`. All 10 PE placed.

**KE distribution check.** AT1: `504 KE 1/2/3` (analysis) + `504 KE 4/5/6/8/9` (design). AT2: `401 KE 1–10` (team plan + coordinate + support + reflection). AT3: `504 KE 7/10`. All 20 KE placed.

**Verification:** every group G1–G11 has a row; every PC, PE and KE is allocated; FS cross-cutting; AC = environment (G10) + assessor condition (G11). No item is unaddressed. **401 lands entirely in AT2; 504 entirely in AT1 (design) + AT3 (deploy/operate).**

---

## 6. Required authoring worklist

> **Build status note:** the previously-built AT1 "Team Setup" Team-Plan artefacts are **repurposed into AT2 Part A** (the project/team plan). The new **AT1 (Solution Design) and AT3 (Deployment Report) are unbuilt.** The `scripts/s1_cl3/build_s1_cl3_at1_*` files + `assessments/AT1/*` need renaming/relocating to AT2.

### AT1 — Design
1. **Solution Design exemplar** (reuse the CL2 Solution Design type) — the agreed "to be" improvement (all four components, all four concerns, compliance slice, cost-benefit, IaC-partitioned), + the contextual `KE 6` question. *(Generated; a stripped, in-world copy = the design provided to AT2.)*
2. **AT1 Student + Assessor instruments** — the Solution Design deliverable (Part A) + the presentation/sign-off (Part B); marking guide with bidirectional UoC traceability + the FS-Oral observation.

### AT2 — Team Implementation
3. **Project/team-plan + CloudFormation-write deliverable spec** (NEW) — team plan + component allocation (Part A); the divided write + integration + team sign-off gate (Part B). *(Write is 401's vehicle, not 504-assessed.)*
4. **Led-meeting observation checklist** (NEW — BSBXTW401) + **reflection** prompt (NEW).
5. **AT2 Student + Assessor instruments** (group).

### AT3 — Implement
6. **As-deployed Deployment Report exemplar** (reuse the CL2 Deployment Report type) — the whole improved system.
7. **AT3 Student + Assessor instruments** (individual).
8. **AT3 lab artefacts (support — to PRODUCE; the AT3 instruments reference these as provided artefacts and are *draft pending the proving run*).** AT3 follows an **apply-as-update** model: deploy the baseline, then apply the improvement as a CloudFormation **change-set**.
   - **Baseline lab-pack** — the *existing state* as CloudFormation: single-AZ Ledgerline (Windows EC2 + internal ALB + single-AZ RDS for SQL Server + S3 + VPC), **encrypted at rest, empty database** (the system + data are imaginary story; data is out of scope). CL1-AT3 pattern, re-pointed at Ledgerline.
   - **Reference upgrade change-set** — the model implementation of the agreed design *as a CloudFormation update to the baseline stack* (same logical IDs); doubles as the **AT2 model answer** + the **AT3 fallback** if a team's write is unusable. All changes **in-place/additive** — no replacements, since encryption is baseline.
   - **Live proving run** — deploy baseline → apply the change-set → verify (Multi-AZ failover, scale-out) → tear down, in an Academy lab; confirms **SQL-Server-Multi-AZ feasibility** + the change-set mechanics. Required before AT3 is final.
   - Local validation harness (cfn-lint + pytest) + student README, per docs/lab-pack-standard.md.

### Cluster-level
9. **`assessment_plan.md`** — this document.
10. **`mappings/`** — per-unit Assessment Mapping `.docx` (504, 401).
11. **Realign `consolidated_uoc.md`** + the scenario `IR-6` wording (re-point "Improvement Business Case" → the Solution Design's cost-benefit justification, since the business case is dropped).

---

## 7. Open questions / TBDs

1. **Component breakdown — resolved.** The approved Solution Design commits the **four** CloudFormation component stacks (**network / compute / database / storage**); these are the AT2 write-allocation units (one per team member, teams of four).
2. **Team model — resolved:** **teams of 4**, one IaC component each; formation at the assessor's discretion; AT2 run as **rotating-chair working meetings** (each chairs ≥1; assessor observes the chair).
3. **Vehicle & `[ICTCLD504 KE 6]` — resolved:** assess on Ledgerline, practise on the website; KE 6 as the contextual object-storage contrast question in the AT1 design.
4. **Business case — dropped:** not required by either UoC and out of sequence; the 504 approval gate is the AT1 design presentation; cost-benefit rides in the Solution Design.
5. **UoC transcription — resolved (2026-06-11);** **source-assessment reuse — accepted author-fresh;** **Pre-validation — downstream gate** (run by the validation team after authoring).
6. **Encryption / data — resolved (2026-06-16):** the baseline is **encrypted at rest** (RDS/EBS/S3) and the lab database is **empty** — the accounting system and its data are imaginary story justifying the infrastructure choices. **Encryption is not an improvement** and data migration is **out of scope**, so every AT3 change is an **in-place/additive change-set** (no replacement, no IR-4 data-loss exposure). CL3 is an *infrastructure*-improvement exercise, not a data one.

---

## 8. Critical-path next steps

1. **Settle the component breakdown** (§7.1) — AT2 and AT3 both reference it.
2. **Generate the AT1 Solution Design exemplar** (the agreed "to be" design) + derive the stripped in-world copy provided to AT2; build the AT1 instruments + presentation.
3. **Author AT2** — the project/team-plan + CloudFormation-write spec, the observation checklist + reflection; derive the group instruments.
4. **Author AT3** — the as-deployed Deployment Report exemplar; build the deployable improved lab-pack + the reference fallback; derive the individual instruments.
5. **Realign `consolidated_uoc.md`** + the scenario `IR-6` wording; generate `mappings/`; run the coverage validator; hand to Pre-Validation.

---

## Changelog

- **2026-06-07 (v1):** Initial draft — integrated *lead a team to improve cloud infrastructure*; three-AT individual → group → individual; owned-dimension model; team-leadership evidence.
- **2026-06-08 (v2 — re-vehicled):** Assess on Ledgerline, practise on the website; `[KE 6]` as a contextual contrast question.
- **2026-06-11 (v3 — AC consistency):** Assessor-requirements AC tagged; new G11; 80 → 82 items.
- **2026-06-11 (v4 — scenario alignment):** India-campus driver + compliance dimension; provided-vs-student-authored boundary; AT1 deliverable renamed "Team Plan".
- **2026-06-11 (v5 — team model):** Teams of 4, assessor-formed, rotating-chair meetings.
- **2026-06-11 (v6 — AT restructure):** Technical analysis+design moved into a group AT2 with an owned-dimension model + an "Architecture Analysis" document type.
- **2026-06-16 (v7 — units-first restructure):** Retired owned-*dimension* (under-evidenced 504 `PC 3.3`) for owned-*component*; eliminated the Architecture Analysis type (analysis = the Solution Design's review); AT1 individual design, AT2 group plan, AT3 individual component build + hybrid 401.
- **2026-06-16 (v8 — write-is-the-seam):** Resolved the individual/group tension cleanly by locating the **division on the YAML write** (not the technical deliverable): of design / write / deploy, only the write is free to divide (it is ICTCLD505, not 504), so it carries 401's divided, individually-accountable team work while design (AT1) and deploy (AT3) stay individual. Consequences: **AT1** = individual Design — *Part A* Solution Design (`504 el 1–2`), *Part B* presentation + sign-off (`PC 2.4/2.5`, FS Oral); **AT2** = group Team Implementation (`401 el 1–4` entirely) — *Part A* project/team plan + component allocation, *Part B* the divided CloudFormation write + integration + team sign-off (the write **not** 504-assessed); **AT3** = individual Implement — deploy the combined template + demonstrate/test/refine/document the **whole system** (`504 el 3–4`). **Business case dropped** (no UoC requires it; out of sequence; cost-benefit rides in the Solution Design). The agreed "to be" design is **provided** to AT2; an assessor **reference combined template** protects AT3 individual evidence from a team integration failure. Scalability defined as **elastic-capacity-on-demand** (demonstrable, not forecast). All 82 items remain placed; **401 entirely in AT2, 504 entirely in AT1 + AT3.** Component breakdown (the AT2 write-allocation units) is the one open item (§7.1).
