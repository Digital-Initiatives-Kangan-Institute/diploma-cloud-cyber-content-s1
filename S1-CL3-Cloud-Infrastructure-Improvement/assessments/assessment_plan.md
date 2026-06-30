# S1-CL3 Cloud Infrastructure Improvement — Cluster Assessment Plan

> **STATUS: DRAFT.** Turns the cluster's settled design into the spec the AT instruments are built from,
> with the coverage proof that every UoC item lands in an assessment. Conforms to the assessment-plan
> format standard (`docs/assessment-plan-format.md`).
>
> **Scenario binding:** maps to the **Semester-1 YAT** scenario — the scenario plan (to be written) is the
> cross-cluster source the `SR-*` below are validated against; current scenario sources are
> `scenario/scenario-flow.md` + `scenario/cluster-3-scenario-{assessment,practice}.md`.
>
> **What is settled** (AT model reasoned from the two units' requirements, approved 2026-06-16):
> - One integrated engagement — **a team improves a cloud system's infrastructure** — combining
>   **ICTCLD504** (the technical improve-cycle, individual) and **BSBXTW401** (leading the team, group).
> - **The seam between individual and group work is the *YAML write*, not the technical deliverable.** Of
>   design / write the IaC / deploy, **design (504 el 1–2) and deploy (504 el 3) are individual**, while
>   **writing the CloudFormation is not 504-assessed** (it is ICTCLD505, done in CL2). So the write is the
>   one job free to divide — dividing it **by component** gives BSBXTW401 its individually-accountable team
>   work without touching any individual 504 evidence.
> - **Three ATs:** **AT1 (individual) Design** (`504 el 1–2`) · **AT2 (group) Team Implementation**
>   (`401 el 1–4`, the divided write) · **AT3 (individual) Implement** (`504 el 3–4`).
> - **No business case** (neither UoC requires one; the 504 approval gate is the AT1 design presentation;
>   cost-benefit rides inside the Solution Design).
> - **Reliability = application-tier Multi-AZ + DB backup/restore + cross-Region DR; the database is NOT
>   Multi-AZ** (Ledgerline is vendor-certified single-instance — the discovered Multi-AZ DB limitation,
>   TF-03). Scalability = elastic-capacity-on-demand (demonstrable, not forecast). Parameterised
>   CloudFormation; a light India residency slice (CERT-In + Companies-Act).

---

## 1. Integration approach

One integrated cluster assessment that reads as a single engagement on one system. **Shape:** *design the
improvement (individual) → plan and build it as a team (group) → deploy and operate it (individual)*, all on
Ledgerline. The units meet without colliding because they are evidenced on **different jobs**: 504 owns the
**design** (AT1) and **deploy-and-operate** (AT3), both individual; 401 owns the **team write** (AT2), the
only job free to divide. It is CL1 AT3's improve-loop widened (security + reliability + scalability + cost)
and run by a team.

**Approval moments (UoC-faithful):** AT1 Part B = design sign-off, *obtain sign off to proceed*
(`[ICTCLD504 PC 2.5]`, individual); AT2 Part B = team validates the combined template (a project gate, not a
504 PC); AT3 = final sign-off (`[ICTCLD504 PC 4.3]`, individual).

**Knowledge evidence — contextual, on the student's own work:** technical KE rides the AT1 design + the AT3
deployment documents; leadership KE rides the AT2 reflection. No abstract recall.

---

## 2. Scenario

**Reuse the YAT world.** By CL3, **Ledgerline** (the Accounting system) sits at a **single-AZ cloud
baseline** (on-prem in CL1 → migrated → improved in CL3). The engagement is triggered by YAT's India-campus
partnership: MTS is engaged to confirm Ledgerline is stable, reliable, fit for purpose and compliant with
the applicable Indian regulatory requirements, and to improve it across the four concerns. The student team
designs the improvement, builds it as code, and deploys it. The improvement is **open** — its shape follows
the analysis, proportionate to an internal business-hours finance system (IR-2).

**Provided framing (not the answer):** the engagement framing (MSA, Role Brief, Improvement Requirements
IR-1…7, ICT Manager Consultation Notes, Indian Regulatory Requirements) is supplied; each student's
analysis, compliance assessment and improvement design (AT1) are student-authored. The engagement then
adopts a single **agreed improvement Solution Design** (provided), which AT2 encodes into IaC and AT3
deploys.

**Vehicle (per `scenario-flow.md`):** assess on **Ledgerline** (single-AZ cloud), practise on the
**website** (no-leakage: the website is assessed in CL2). The testable scenario needs are the `SR-*` in §3 +
the register in §6.

---

## 3. Assessment structure

| AT | Working title | Mode | Format | Unit focus |
|----|---|---|---|---|
| **AT1** | Design | **Individual** | **A** Solution Design (analyse + design the whole improvement) · **B** presentation + sign-off | **ICTCLD504** el 1–2 |
| **AT2** | Team Implementation | **Group** | **A** project/team plan + component allocation · **B** the divided CloudFormation write + integration + team sign-off | **BSBXTW401** el 1–4 |
| **AT3** | Implement | **Individual** | Deploy the combined template + demonstrate/test/refine/document the **whole system** + final sign-off | **ICTCLD504** el 3–4 |

### AT1 — Design
- **Mode / Format / Unit focus:** Individual; Part A Solution Design (analyse the baseline + design the
  whole improvement across all four concerns, incl. the compliance assessment + cost-benefit) + Part B
  observed presentation and sign-off; ICTCLD504 el 1–2.
- **UoC coverage:** [ICTCLD504 PC 1.1–1.6, 2.1–2.5] · [ICTCLD504 PE 1, 3] · [ICTCLD504 KE 1–6, 8, 9] · [ICTCLD504 FS Oral communication] · [ICTCLD504 FS Reading] · [ICTCLD504 FS Writing] · [ICTCLD504 AC 5]
- **Scenario requirements:** SR-CL3-03 · SR-CL3-04 · SR-CL3-05 · SR-CL3-06 · SR-CL3-09 · SR-CL3-10

### AT2 — Team Implementation
- **Mode / Format / Unit focus:** Group; Part A team plan + allocate one IaC component per member; Part B
  the team writes the agreed design's CloudFormation (divided by component, integrated) across
  individually-led meetings + a team sign-off gate; BSBXTW401 el 1–4. *(The write is 401's vehicle — not
  504-assessed.)*
- **UoC coverage:** [BSBXTW401 PC 1.1–1.4, 2.1–2.4, 3.1–3.4, 4.1–4.4] · [BSBXTW401 PE 1–5] · [BSBXTW401 KE 1–10] · [BSBXTW401 FS Get the work done] · [BSBXTW401 FS Interact with others] · [BSBXTW401 FS Navigate the world of work]
- **Scenario requirements:** SR-CL3-01 · SR-CL3-07 · SR-CL3-08

### AT3 — Implement
- **Mode / Format / Unit focus:** Individual; deploy the combined (agreed, validated) template, monitor/test
  /demonstrate all four concerns on the deployed whole system, refine, document the as-deployed result + a
  long-term strategy, obtain final sign-off; ICTCLD504 el 3–4. *(An assessor reference combined template is
  the fallback so a team integration failure can't block this individual evidence.)*
- **UoC coverage:** [ICTCLD504 PC 3.1–3.4, 4.1–4.3] · [ICTCLD504 PE 2, 4, 5] · [ICTCLD504 KE 7, 10] · [ICTCLD504 FS Problem solving] · [ICTCLD504 FS Self-management] · [ICTCLD504 FS Writing]
- **Scenario requirements:** SR-CL3-01 · SR-CL3-02 · SR-CL3-06 · SR-CL3-07 · SR-CL3-09

**Template basis:** AT1 reuses the CL2 **Solution Design** type; AT3 reuses the CL2 **Deployment Report**
type. New = the AT2 project/team-plan + CloudFormation-write deliverable spec, the led-meeting observation
checklist, and the reflection prompt. No business case; no separate "Architecture Analysis" type (the
analysis is the Solution Design's review section).

---

## 4. Provenance

**Lightest cluster, heaviest reuse.** The technical workflow (analyse → design → deploy → test → document →
sign-off) is structurally CL1 AT3 + CL2, re-pointed at Ledgerline with a team-leadership overlay on the
write.

- **Reused / proven:** CL1 AT3's improve-an-existing-baseline shape + the lab-pack standard
  (`docs/lab-pack-standard.md`); CL2's Solution Design (AT1) + Deployment Report (AT3) generators, the
  Kangan Project Assessment instrument generators, the scenario world, and the validators. Students learned
  IaC in CL2 (505), so the AT2 write reuses an existing skill (not re-assessed).
- **New (CL3-specific):** the AT1 Solution Design exemplar (the agreed "to be" design); the AT2 instruments
  (team-plan + write spec, observation checklist, reflection); the AT3 as-deployed Deployment Report
  exemplar + the deployable improved lab-pack + assessor reference fallback.
- **Author-fresh (accepted):** no standalone ICTCLD504 / BSBXTW401 source assessments located — CL3 is
  greenfield by design (step-3 audit not applicable).

---

## 5. Coverage verification

The per-AT **UoC coverage** in §3 is the authoritative item→AT mapping; this section is the rollup proof
that nothing is unassessed (across `consolidated_uoc.md`, 82 items).

- **PC** — 504: AT1 `1.1–2.5`, AT3 `3.1–4.3` (all 18). 401: AT2 `1.1–4.4` (all 16).
- **PE** — 504: AT1 `1, 3`, AT3 `2, 4, 5` (all 5). 401: AT2 `1–5` (all 5).
- **KE** — 504: AT1 `1–6, 8, 9`, AT3 `7, 10` (all 10). 401: AT2 `1–10` (all 10).
- **FS** — 504: AT1 Oral/Reading/Writing, AT3 Problem-solving/Self-management/Writing (all 5). 401: AT2
  Get-the-work-done/Interact-with-others/Navigate-the-world-of-work (all 3).
- **AC** — environment/legislative ACs are discharged via the `SR-*` register (§6, AC link column); the
  assessor-requirement ACs (`[ICTCLD504 AC 8]`, `[BSBXTW401 AC 2]`) are institutional, one statement per AT
  cover sheet.

**Verification:** every consolidated PC / PE / KE / FS is covered by ≥1 AT above; **401 lands entirely in
AT2; 504 entirely in AT1 (design) + AT3 (deploy/operate).** (Confirmed mechanically — `validate-cluster-
coverage` = 72/72.)

---

## 6. Scenario requirements register

The conditions the scenario must enable for these assessments. The scenario plan must satisfy every `SR-*`;
the **AC link** names the UoC Assessment Condition each environmental requirement discharges.

| SR | Condition the scenario must enable | AT(s) | AC link |
|----|---|---|---|
| **SR-CL3-01** | AWS Academy Learner Lab (us-east-1) — cloud vendor services, managed DB, console/SDK/CLI, IDE, browser, SSH/RDP; the team build + individual deploy/operate environment | AT2, AT3 | [ICTCLD504 AC 1] · [ICTCLD504 AC 2] · [ICTCLD504 AC 3] · [ICTCLD504 AC 4] · [ICTCLD504 AC 6] · [ICTCLD504 AC 7] · [BSBXTW401 AC 1] |
| **SR-CL3-02** | Deployable single-AZ Ledgerline **baseline lab-pack** (EC2+ASG / internal ALB / single-AZ RDS for SQL Server / S3 / VPC; encrypted at rest, empty DB) — the as-is system AT3 deploys then improves | AT3 | — |
| **SR-CL3-03** | Engagement framing — Master Services Agreement, Engagement Role Brief, Improvement Requirements (IR-1…7), ICT Manager Consultation Notes | AT1 | — |
| **SR-CL3-04** | Indian Regulatory Requirements (CERT-In logging + Companies-Act books-of-account) driving the compliance assessment + the India residency slice | AT1 | [ICTCLD504 AC 5] |
| **SR-CL3-05** | Current-state ICT records (baseline Solution Design, infrastructure/application specs, operational costing) carrying the Multi-AZ database limitation breadcrumb (TF-03) | AT1 | — |
| **SR-CL3-06** | A required-personnel stakeholder who role-plays the design review + sign-off (AT1 Part B) and the final sign-off (AT3) | AT1, AT3 | — |
| **SR-CL3-07** | The agreed "to be" improvement Solution Design provided to the team (AT2 build input) + an assessor reference combined template (AT3 fallback) | AT2, AT3 | — |
| **SR-CL3-08** | A student team of four (the MTS improvement team) for the group write | AT2 | [BSBXTW401 AC 1] |
| **SR-CL3-09** | YAT Solution Design + Deployment Report templates (intranet Templates section) | AT1, AT3 | — |
| **SR-CL3-10** | The website (an object-storage-dependent system) for the contextual `[ICTCLD504 KE 6]` contrast question + the CL3 practice vehicle | AT1 | — |

---

## 7. Worklist

- **AT1** — Solution Design exemplar (the agreed "to be" design; also the provided AT2 input) + the AT1
  Student/Assessor instruments (Part A deliverable + Part B presentation/sign-off; marking guide with
  bidirectional UoC traceability + FS-Oral observation).
- **AT2** — the project/team-plan + CloudFormation-write deliverable spec (write divided by component +
  integration + team sign-off), the led-meeting observation checklist + reflection prompt; the
  Student/Assessor instruments (group).
- **AT3** — the as-deployed Deployment Report exemplar; the deployable improved lab-pack (combined template +
  assessor reference fallback; **proven live 2026-06-21**, apply-as-update change-set, SQL Server Express
  stand-in, RDS create-only); the Student/Assessor instruments (individual).
- **Cluster** — this plan; `mappings/` per-unit Assessment Mapping docs (built); `consolidated_uoc.md`
  realignment to the write-is-the-seam model (the prose still describes the superseded owned-dimension /
  business-case model).

---

## 8. Open questions / TBDs

1. **Component breakdown — resolved:** four CloudFormation component stacks (**network / compute / database /
   storage**) = the AT2 write-allocation units (one per member, teams of four).
2. **Team model — resolved:** teams of 4; rotating-chair working meetings (each chairs ≥1; assessor observes
   the chair).
3. **Business case — dropped:** out of sequence; cost-benefit rides in the Solution Design.
4. **Encryption / data — resolved:** baseline encrypted at rest, lab DB empty; encryption is not an
   improvement and data migration is out of scope; every AT3 change is an in-place/additive change-set.
5. **`consolidated_uoc.md` prose — `[TBD]`:** still describes the old owned-dimension / business-case model;
   realign to write-is-the-seam (the item inventory is unaffected).
6. **Pre-validation** — downstream institutional gate (run after authoring).

---

## Changelog

- **2026-06-07 → 2026-06-21 (v1–v9):** initial integrated three-AT model through the write-is-the-seam
  restructure (v8) and the database-reliability-via-backup/DR resolution (v9). See git history for the full
  evolution (owned-dimension → owned-component → write-is-the-seam; business case dropped; Multi-AZ DB
  limitation breadcrumb TF-03). All 82 items remained placed throughout.
- **2026-06-22 (v10 — reformat to the assessment-plan standard):** restructured to
  `docs/assessment-plan-format.md` — per-AT **UoC coverage** as canonical tags (now the authoritative
  item→AT mapping, derived from the AT benchmarks), §5 recast as coverage verification, and a new **§6
  scenario requirements register** (`SR-CL3-01…10`, with AC-link discharge of the environmental conditions).
  No assessment-design change — only the plan's structure + the explicit scenario-requirement capture.
