# S1-CL2 Cloud Disaster Recovery — Cluster Assessment Plan

> **STATUS: COMPLETE (authoring + coverage), 2026-06-15.** All instruments, exemplars and `mappings/` are
> built and website-framed; `validate-cluster-coverage` passes **105/105**. What remains before
> institutional sign-off is **external only** — the colleague **Pre-Validation** meeting. Don't reopen for
> authoring. Conforms to the assessment-plan format standard (`docs/assessment-plan-format.md`).
>
> **Scenario binding:** maps to the **Semester-1 YAT** scenario — the offshore-India / GIFT City **website
> global expansion** engagement; scenario sources `scenario/cluster-2-scenario-{assessment,practice}.md` +
> `scenario/scenario-flow.md`.
>
> **What is settled** (approved with Tim, 2026-06-06):
> - The four-topic taxonomy and the **two-AT** division.
> - **AT1 is three parts** — **Part A Solution Design** (ICTCLD503 design), **Part B DR Plan** (ICTCLD501),
>   **Part C presentation** covering both for approval. **AT2** is a single written **Deployment Report**.
> - **DR ≠ regulatory ≠ design — three separate concerns:** the DR plan (501) = "what if the system goes
>   down"; the Solution Design (503) holds the web-scale architecture **and the microservice**; data
>   residency is an **input constraint**, not a deliverable. The microservice lives in the Solution Design
>   (its regulatory purpose is *why* it exists), never in the DR plan.
> - The scenario spine (offshore-India / **website** assessed, **LMS** practised); the **light**
>   India-residency slice; the two approval gates; KE in written appendices + verbal contextual Q&A at AT1's
>   presentation.
>
> **Companion documents:** `consolidated_uoc.md` (every PC/FS/PE/KE/AC verbatim, 13 groups under 4 topics);
> the CL1 plan (the pilot this parallels in shape).

---

## 1. Integration approach

**Goal (same as CL1):** one integrated cluster assessment that reads as a single engagement from design to
hand-over — one scenario, one stakeholder voice, one artefact thread.

**Shape:** one continuous engagement across two delivery phases, each a teach → practise → assess cycle:

```
   Phase 1 — Design & Plan                Phase 2 — Implement
        AT1                                    AT2
   Part A  Solution Design (503 design)   Deployment Report
   Part B  DR Plan         (501)          - microservice build (503) + IaC (505)
   Part C  Presentation    (501 el 5 —    - monitoring + IaC user docs + build sign-off
           the approval gate, covers A+B)
```

**The thread (the design-approval gate):** in AT1 the student **designs** the India-expanded system
(Part A), **plans its recovery** (Part B), and gets **both approved** at the Part C presentation. AT2 then
**builds the design that was signed off** — not a fresh start. UoC-faithful: 501 element 5 = approval before
implementing; 503/505 element 4 = build sign-off. **Part A before Part B** because a DR plan is written *for*
a designed system.

**Knowledge evidence — contextual, not abstract recall** (carried from CL1): students reason about *their
own* design/build choices. **Locations (settled):** a written KE appendix in each document (Part A, Part B,
AT2 — mandatory), plus verbal contextual questions at the AT1 Part C presentation (covering Part A + B KE);
AT2 has no presentation, so its KE is written-only.

---

## 2. Scenario

**Settled** — see `scenario/cluster-2-scenario-assessment.md`. YAT enters an **offshore-India partnership
(GIFT City)** that takes the **public website** global, requiring it to (a) serve a global user base,
(b) be region-recoverable, and (c) be provisioned as code — one event driving all three units. The
**website is the assessment vehicle**; the **LMS is the practice vehicle** (the parallel
`lms-global-expansion` worked example). Baseline: the website arrives **HA-hardened** (Multi-AZ, single-region
cross-AZ).

**Data residency is an input constraint, not a deliverable.** The **light** India slice (a bounded set of
access logs/data in-region; main DB stays in AU) is supplied as the `Data Residency & Sovereignty
Requirements` document. Students **design to it** (it shapes Part A's web-scale design — `503 PC 1.5` — and
is *why* the audit-log microservice exists) and lightly respect it in Part B's DR plan. No compliance plan
is authored; no UoC asks for one. The scenario is **not a topic** and is not itself assessed — it supplies
the inputs + the AWS Academy lab environment.

---

## 3. Assessment structure

| AT | Working title | Mode | Format | Unit focus |
|----|---|---|---|---|
| **AT1** | Cloud Expansion: Design & DR Plan | Individual | **Project Assessment**, three parts — A Solution Design · B DR Plan · C presentation | **ICTCLD503** *design* + **ICTCLD501** |
| **AT2** | Cloud Microservice & IaC Implementation | Individual | Single written **Deployment Report** (+ provided artefacts as appendices) | **ICTCLD503** *build* + **ICTCLD505** + monitoring |

### AT1 — Cloud Expansion: Design & DR Plan
- **Mode / Format / Unit focus:** Individual; **Part A** Solution Design (web-scale architecture for the
  global user base + the audit-log microservice; residency as a design input — `503 PC 1.7/2.4`); **Part B**
  DR Plan (recovery for the Part-A system: risk/impact, RTO/RPO, backup-restore, recovery steps — 501
  el 1–4); **Part C** presentation (walkthrough of A+B, feedback, lodgement, sign-off — 501 el 5, the design
  approval gate). ICTCLD503 *design* + ICTCLD501.
- **UoC coverage:** [ICTCLD501 PC 1.1–1.3, 2.1–2.5, 3.1–3.4, 4.1–4.3, 5.1–5.4] · [ICTCLD501 PE 1–3] · [ICTCLD501 KE 1–6] · [ICTCLD501 FS Oral communication] · [ICTCLD501 FS Planning and organising] · [ICTCLD501 FS Problem solving] · [ICTCLD501 FS Reading] · [ICTCLD501 FS Self-management] · [ICTCLD503 PC 1.1–1.7, 2.1–2.4] · [ICTCLD503 PE 1, 2, 5] · [ICTCLD503 KE 3, 4, 6] · [ICTCLD503 FS Problem solving] · [ICTCLD503 FS Reading] · [ICTCLD503 FS Self-management] · [ICTCLD503 FS Writing]
- **Scenario requirements:** SR-CL2-02 · SR-CL2-03 · SR-CL2-05 · SR-CL2-06

### AT2 — Cloud Microservice & IaC Implementation
- **Mode / Format / Unit focus:** Individual; operate a provided data-store template (505 el 1–2), author
  the microservice template + deploy from the provided code (505 el 3 + 503 el 3), configure monitoring,
  produce the IaC user documentation (`505 PC 4.1`, `PE 4`), obtain build sign-off (`503 PC 4.2/4.3`,
  `505 PC 4.2`). Provided artefacts (data-store template, microservice code, webhook contract) are
  appendices — no separate lab pack. ICTCLD503 *build* + ICTCLD505 + monitoring.
- **UoC coverage:** [ICTCLD503 PC 3.1–3.4, 4.1–4.3] · [ICTCLD503 PE 3, 4] · [ICTCLD503 KE 1, 2, 5] · [ICTCLD503 FS Writing] · [ICTCLD505 PC 1.1–1.4, 2.1–2.6, 3.1–3.7, 4.1, 4.2] · [ICTCLD505 PE 1–4] · [ICTCLD505 KE 1–11] · [ICTCLD505 FS Oral communication] · [ICTCLD505 FS Problem solving] · [ICTCLD505 FS Reading] · [ICTCLD505 FS Self-management] · [ICTCLD505 FS Writing]
- **Scenario requirements:** SR-CL2-01 · SR-CL2-02 · SR-CL2-04

**Two approval moments (UoC-faithful):** end of AT1 Part C = design approval (501 el 5) before any build;
end of AT2 = build sign-off (503 el 4 + 505 el 4).

**Template basis:** AT1 uses the institutional **Project Assessment** template (multi-part, as CL1); the DR
Plan template + AT1 DR-Plan exemplar are built; the Solution Design (Part A) + Part C presentation reuse the
Solution Design / Business-Case-Presentation document types.

---

## 4. Provenance

**CL2 is authored fresh — not a reuse/synthesis exercise like CL1.** ICTCLD505 is greenfield (no source
material exists) and the ICTCLD501 / ICTCLD503 standalone source assessments are not in this repo; every
scenario element worth recovering has been recovered, and the ATs are authored against the consolidated UoC
directly.

**Reused as structure (not provenance):** the CL1 **Solution Design** and **Business-Case-Presentation**
document types (Part A / Part C); the CL1 **AT pattern** (Project Assessment template, multi-part AT,
appendix-bearing AT2 report, contextual reflective KE, bidirectional UoC traceability); and the **scenario
inputs** on the intranet (`website-global-expansion` documents incl. the residency requirements;
`lms-global-expansion` as the parallel practice worked-example).

---

## 5. Coverage verification

The per-AT **UoC coverage** in §3 is the authoritative item→AT mapping; this is the rollup proof that
nothing is unassessed (across `consolidated_uoc.md`, 128 items: 105 PC/FS/PE/KE + 23 AC; no ungrouped items).

- **PC** — 501 (all 19) → AT1; 503 design `1.1–2.4` → AT1, 503 build `3.1–4.3` → AT2; 505 (all 19) → AT2.
- **PE** — 501 `1–3` → AT1; 503 `1/2/5` → AT1, `3/4` → AT2; 505 `1–4` → AT2.
- **KE** — 501 `1–6` → AT1; 503 `3/4/6` → AT1, `1/2/5` → AT2; 505 `1–11` → AT2.
- **FS** — 501 (5) → AT1; 503 (reading/problem-solving/self-management/writing) across AT1+AT2; 505 (5) → AT2.
- **AC** — discharged via the `SR-*` register (§6, AC link); the assessor-requirement ACs are institutional,
  one statement per AT cover sheet.

**Verification:** every consolidated PC / PE / KE / FS is covered by ≥1 AT above. (Confirmed mechanically —
`validate-cluster-coverage` = 105/105.)

---

## 6. Scenario requirements register

The conditions the scenario must enable; the **AC link** names the UoC Assessment Condition each
environmental requirement discharges.

| SR | Condition the scenario must enable | AT(s) | AC link |
|----|---|---|---|
| **SR-CL2-01** | AWS Academy labs (Cloud Foundations + Cloud Architecting) — cloud vendor, managed DB, serverless/IaC services, console/CLI, IDE, browser, SSH/RDP | AT1, AT2 | [ICTCLD503 AC 1] · [ICTCLD503 AC 2] · [ICTCLD503 AC 3] · [ICTCLD503 AC 6] · [ICTCLD503 AC 8] · [ICTCLD505 AC 1] · [ICTCLD505 AC 2] · [ICTCLD505 AC 5] · [ICTCLD505 AC 6] · [ICTCLD505 AC 7] · [ICTCLD505 AC 8] |
| **SR-CL2-02** | The `website-global-expansion` scenario inputs — the offshore-India/GIFT City engagement, the HA-hardened website baseline, the global-user-base driver, requirements + data sources | AT1, AT2 | [ICTCLD503 AC 5] · [ICTCLD503 AC 7] · [ICTCLD503 AC 9] · [ICTCLD505 AC 3] · [ICTCLD505 AC 4] |
| **SR-CL2-03** | The `Data Residency & Sovereignty Requirements` document (the light India slice) — the input constraint driving Part A's web-scale design + the microservice | AT1 | [ICTCLD501 AC 2] |
| **SR-CL2-04** | Provided AT2 artefacts supplied **inline as Deployment-Report appendices (deliberately NOT a lab-pack)**: (a) a data-store CloudFormation template (written in-scenario by another contractor) carrying a **deliberate fault the student must debug and deploy**; (b) the audit-log microservice **application code** (the student authors their own IaC to deploy it); (c) the webhook payload contract. Inline by design — authoring/operating the deployment YAML is the assessed skill (ICTCLD505), so a pre-built/validated lab-pack would remove the assessed work | AT2 | [ICTCLD503 AC 4] |
| **SR-CL2-05** | A required-personnel stakeholder to role-play the AT1 Part C presentation feedback + design sign-off | AT1 | — |
| **SR-CL2-06** | The **data required to assess the website's risk events** — the organisational/business context, IT stack and project requirements (Website Global Expansion engagement brief, requirements, ICT-manager consultation notes, website spec, HA-hardened baseline, data-residency requirements, deprecated on-prem DR plan for context) — **plus** the DR **reporting standard** (the YAT Disaster Recovery Plan template + lodgement protocol). The risk register / impact analysis itself is **student-authored** (the assessed risk assessment), so no pre-built register is provided | AT1 | [ICTCLD501 AC 1] · [ICTCLD501 AC 3] |

*(The LMS `lms-global-expansion` is the **practice** vehicle — teaching context, not an assessment
requirement — so it is not an `SR-*`; see §2.)*

---

## 7. Worklist

**Complete** — all instruments (AT1 Parts A/B/C, AT2), exemplars, templates and `mappings/` are built and
website-framed; coverage validates 105/105. The DR-Plan exemplar's regulatory/microservice material has been
de-weaved into the Part A Solution Design. No authoring remains.

---

## 8. Open questions / TBDs

1. **Pre-validation** — the colleague Pre-Validation meeting (external institutional gate).
2. **Minor labels** — the AT1 working title / website label may broaden (cosmetic).
3. *Residency/legal wording accepted as-is* (LLM-grounded Indian-law framing, fit for an imaginary
   pre-university case study; no legal review engaged); the lab product confirmed (Kangan provisions both
   AWS Academy products); the 503 global-serving practice vehicle is the LMS.

---

## Changelog

- **2026-06-06 → 2026-06-15 (v1–v4 + completion):** initial two-AT plan → the DR≠regulatory≠design
  restructure (AT1 → Parts A Solution Design / B DR Plan / C presentation; microservice + residency moved
  into the Solution Design; residency an input constraint) → re-vehicled assessment LMS→website, practice
  Accounting→LMS (per `scenario-flow.md`) → authoring + coverage complete (105/105). See git history for the
  full evolution.
- **2026-06-22 (reformat to the assessment-plan standard):** restructured to `docs/assessment-plan-format.md`
  — per-AT **UoC coverage** as canonical tags (authoritative item→AT mapping, derived from the AT
  benchmarks; all 105 PC/PE/KE/FS placed), §5 recast as coverage verification, and a new **§6 scenario
  requirements register** (`SR-CL2-01…06`, AC-linked). No assessment-design change — only the plan's
  structure + explicit scenario-requirement capture.
