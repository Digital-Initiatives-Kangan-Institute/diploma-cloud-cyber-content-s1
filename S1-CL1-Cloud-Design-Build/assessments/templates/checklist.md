# S1-CL1 — Templates Checklist

> **STATUS: DRAFT.** Running list of every template students need access to as downloads from the YAT mock intranet. Some exist in `original_materials/` and can be carried across; some need to be authored. Each item carries a brief description of purpose, which AT(s) use it, and the UoC references it supports.
>
> Status legend:
> - ✅ **Exists** in `original_materials/` — can be carried across to the intranet templates section
> - ❌ **New authoring required**

---

## Templates from `original_materials/` (carry across)

- [ ] **CBA Template (institutional)** — `ICTICT517_Cost Benefit Analysis template.xlsx` ✅
  - **Purpose:** original 517-standalone Excel CBA template (carried across in `original_materials/` for reference only). Superseded by the YAT-aligned Business Case Template below, which embeds the CBA as §7. **Not used directly in live delivery.**
  - **Used in:** reference only
  - **UoC refs:** n/a (superseded)

- [x] **Business Case Template (YAT-aligned, student-fillable)** — `business-case-template-S1-CL1-AT1.md` ❌→✅ Authored 2026-05-23 (expanded from the earlier standalone CBA template, now a single integrated document with the body covering §1–§11 + Sign-off, and four appendices)
  - **Purpose:** primary (and only) written deliverable for AT1. Single document containing: strategic alignment analysis, current-state synthesis, gap analysis, options/evaluation, CBA summary (§7) with detailed line items in Appendix 1, risk and impact assessment, recommendation, action plan, next-steps decision-requested, sign-off block, and four appendices (1: CBA detail, 2: KE evidence, 3: supporting research, 4: feedback record). **No separate CBA workbook** — all CBA detail lives in Appendix 1 of this same document. Built to render as a `.docx`.
  - **Used in:** AT1
  - **UoC refs:** [ICTICT517 PC 1.1] · [ICTICT517 PC 1.2] · [ICTICT517 PC 1.3] · [ICTICT517 PC 1.4] · [ICTICT517 PC 2.1] · [ICTICT517 PC 2.2] · [ICTICT517 PC 2.3] · [ICTICT517 PC 2.4] · [ICTICT517 PC 3.1] · [ICTICT517 PC 3.2] · [ICTICT517 PC 3.3] · [ICTICT517 PE 1–6] (partial) · [ICTICT517 KE 1, 2, 3, 4] · [ICTICT517 FS Numeracy, Writing, Reading] · [ICTICT517 AC 4] · [ICTCLD401 PC 1.8] · [ICTCLD401 KE 1, 2, 3, 4, 11] · [ICTCLD502 PC 1.2] · [ICTCLD502 KE 1, 2, 3]
  - **Companion assessor artefact:** `assessments/AT1/business-case-assessor-benchmark.md` (worked example with all CBA values filled in — for marking the §7 work)

- [ ] **Draft Plan Template (institutional)** — `ICTICT517_Draft Plan template.docx` ✅
  - **Purpose:** original 517-standalone action-plan template (in `original_materials/` for reference only). **Superseded by the Business Case Template §10**, which embeds the action plan as an integral section of the AT1 Business Case deliverable. **Not used directly in live delivery.**
  - **Used in:** reference only
  - **UoC refs:** n/a (superseded)

- [ ] **Feedback Record Template** — `ICTICT517_Feedback Record template.docx` ✅
  - **Purpose:** Document template used to capture feedback from the superior/colleague meeting in AT1, and the closure-meeting feedback in AT3.
  - **Used in:** AT1, AT3
  - **UoC refs:** [ICTICT517 PC 1.4] Report on proposed changes to superior · [ICTICT517 PC 2.4] Document evaluation process and provide to superior for feedback · [ICTICT517 PC 3.3] Provide action plan to superior for feedback and approval · [ICTCLD401 PC 4.2] Seek and respond to feedback · [ICTCLD502 PC 5.2] Confirm, seek and respond to feedback

---

## Templates derived from scenario content (new authoring)

- [ ] **Change Request Form** — referenced in `<repo_root>/scenario/internal-change-management-procedure.md` step 1 ❌
  - **Purpose:** Form the student completes when proposing a change through YAT's change-management procedure. Captures description, justification, affected systems, risks, duration, rollout plan, backout plan, proposed date, responsible person.
  - **Used in:** AT3 (closure submission via change management); referenced in AT1 (action plan must be consistent with the procedure)
  - **UoC refs:** [ICTICT517 AC 3] Organisational policies and procedures for ICT changes · [ICTICT517 PC 3.1] action plan consistency with organisational policy and procedures · [ICTCLD401 PC 4.3] Save and store user documentation according to organisational policies and procedures · [ICTCLD502 PC 5.3] Obtain final sign off from required personnel

- [ ] **Risk and Impact Analysis Template** — referenced in `<repo_root>/scenario/internal-change-management-procedure.md` step 2 ❌
  - **Purpose:** Standalone risk-and-impact analysis attached to high-risk change requests. Risk register format with likelihood/impact rating, mitigation, residual risk.
  - **Used in:** AT3 (closure submission for the high-risk migration cutover); AT1 (could inform action-plan risk analysis)
  - **UoC refs:** [ICTICT517 AC 3] · [ICTICT517 PC 2.1] Evaluate impact of proposed changes · [ICTICT517 PC 2.2] Evaluate the difficulty of implementing proposed changes

---

## Templates for AT-specific deliverables (new authoring)

- [x] **Board Presentation Deck Template** — `board-presentation-deck-template-S1-CL1-AT1.md` ❌→✅ Authored 2026-05-23 · reframed 2026-05-23 (later) to align with the Business Case structure
  - **Purpose:** Slide-by-slide structure for the student's presentation to the YAT board (assessor + peer, role-played). The deck **presents the Business Case** — each slide names the Business Case section it walks the board through. 10 prescribed slides plus speaker notes. Asked-for decision at the end: approval of the action plan in Business Case §10 + the budget envelope in §10.3. Built to render as a `.pptx`.
  - **Used in:** AT1
  - **UoC refs:** [ICTICT517 PC 1.4] Report on proposed changes to superior · [ICTICT517 PC 2.4] Document evaluation process and provide to superior for feedback · [ICTICT517 PC 3.3] Provide action plan to superior for feedback and approval · [ICTICT517 FS Oral Communication] · [ICTCLD502 FS Oral communication] · [ICTICT517 FS Writing]
  - **Companion assessor artefact:** `assessments/AT1/presentation-observation-rubric.md` (observation checklist for the live event)


- [ ] **AT2 Portfolio Template** — ❌
  - **Purpose:** Structured template for the cloud foundation build evidence — sections for each part (IAM, VPC, EC2, RDS, multi-tier), screenshot placeholders, configuration documentation fields, feedback/sign-off block.
  - **Used in:** AT2
  - **UoC refs:** All ICTCLD401 PCs across elements 2, 3, 4 · ICTCLD401 PE 1, 2, 3 · [ICTCLD401 PC 4.1] Document and communicate work

- [ ] **AT3 Portfolio Template** — ❌
  - **Purpose:** Structured template for the HA design and implementation evidence — sections for review of on-prem env, HA design (with network diagram), implementation evidence (screenshots), simulation evidence, monitoring graphs, vertical-resize evidence.
  - **Used in:** AT3
  - **UoC refs:** All ICTCLD502 PCs across elements 2, 3, 4 · ICTCLD502 PE 1, 2, 3, 4, 5 · [ICTCLD502 PC 4.6] Compare and document simulation findings

- [ ] **AT3 Closure Pack Template** — ❌
  - **Purpose:** Cover document for the consolidated cluster closure pack submitted at end of AT3 — covers strategic context (AT1 outputs), foundation build (AT2 outputs), HA implementation (AT3 outputs), and a Security Responsibilities Matrix sub-deliverable. Routed through the change-management procedure.
  - **Used in:** AT3 closure
  - **UoC refs:** [ICTCLD401 PC 4.1] Document and communicate work · [ICTCLD401 PC 4.3] Save and store user documentation · [ICTCLD502 PC 5.1] Adjust and improve availability · [ICTCLD502 PC 5.2] Confirm, seek and respond to feedback · [ICTCLD502 PC 5.3] Obtain final sign off · [ICTICT517 PC 3.3] Provide action plan to superior for feedback and approval

- [ ] **Security Responsibilities Matrix Template** — ❌
  - **Purpose:** One-page matrix template — rows for each component of the YAT cloud architecture, columns for responsibility owner (cloud vendor / YAT / MTS / students-end-users), cells for the specific responsibility (e.g. physical security of data centres, OS patching, application config, user account management, etc.).
  - **Used in:** AT3 closure (sub-deliverable inside the closure pack)
  - **UoC refs:** [ICTCLD401 PC 1.2] Identify impact of shared security responsibility models · [ICTCLD401 PC 1.7] Identify and assign security responsibilities · [ICTCLD401 KE 7] user, business and vendor responsibilities according to shared security responsibility models · [ICTCLD502 PC 1.3] Identify level of shared security responsibility models according to business needs

- [ ] **Network Diagram Standards / Drawing Conventions** — ❌
  - **Purpose:** Brief reference document specifying YAT's diagramming conventions for cloud and network diagrams: standardised icons (e.g. AWS architecture icons), labels on all elements, public vs private subnet labelling, author and version block, page footer. Referenced from AT2 (VPC diagram) and AT3 (HA architecture diagram). Not strictly a fillable "template" but a standards reference for what's expected.
  - **Used in:** AT2, AT3
  - **UoC refs:** [ICTCLD401 PC 2.2] Create virtual multi-tier network · [ICTCLD502 PC 2.5] Document architecture review findings · [ICTCLD502 PC 3.5] Document architecture design

---

## Summary by status

| Status | Count |
|---|---:|
| ✅ Exists in `original_materials/` — kept as reference only | 3 (CBA, Draft Plan — both superseded; Feedback Record — still used) |
| ✅ Authored 2026-05-23 (YAT-aligned student templates) | 2 (Business Case Template, Board Presentation Deck Template) |
| ❌ New authoring required | 7 |
| **Total templates identified** | **12** |

**Strategy change (2026-05-23):** rather than carry over and rebrand the multiple per-unit institutional templates, the cluster authors YAT-aligned templates from scratch for consistency and cluster alignment. The original `ICTICT517_Cost Benefit Analysis template.xlsx` and `ICTICT517_Draft Plan template.docx` are kept in `original_materials/` for reference but **are not used in live delivery** — their content has been absorbed into the Business Case Template (§7 CBA + §10 Action Plan respectively). Only the Feedback Record template is still actively used (in AT1 presentation + AT3 closure).

Assessor-side companions (not student templates) also authored 2026-05-23 and live under `assessments/AT1/` rather than `assessments/templates/`:
- `business-case-assessor-benchmark.md` — worked example for marking the CBA work in Business Case §7
- `presentation-observation-rubric.md` — observation checklist for the board presentation event

This list is appended to whenever a new template need is identified in the course of authoring scenario or AT brief content.

---

## Changelog

- **2026-05-23:** Initial population from existing scenario/assessment-plan analysis. Lists the three ICTICT517 templates in `original_materials/` plus the seven new templates implied by the cluster's AT structure (change request form, risk and impact analysis, AT2 portfolio, AT3 portfolio, AT3 closure pack, Security Responsibilities Matrix, network diagram standards).
- **2026-05-23 (later):** Added the YAT-aligned CBA template and Board Presentation Deck Template for student completion (markdown drafts pending conversion to `.xlsx` and `.pptx`). Companion assessor artefacts (CBA benchmark + presentation observation rubric) authored under `assessments/AT1/`.
- **2026-05-23 (later still):** Expanded the standalone CBA template into a YAT-aligned Business Case Template covering all AT1 narrative + analytical sections (strategic alignment, current state, gap analysis, options/evaluation, CBA as §7, risk/impact, recommendation, action plan as §10, next steps, KE Appendix as §12). Renamed file `cba-template-S1-CL1-AT1.md` → `business-case-template-S1-CL1-AT1.md`. Marked the standalone CBA Template and the standalone Draft Plan Template as **superseded** — their content is absorbed into the Business Case Template. Strategy clarified: author cluster templates from scratch for consistency rather than rebrand the per-unit originals.
- **2026-05-23 (final today):** Restructured the Business Case Template's appendices into a four-appendix structure all within the same document: Appendix 1 (CBA detailed line items, referenced from the §7 summary), Appendix 2 (Knowledge Evidence — moved from former §12), Appendix 3 (supporting research e.g. AWS Pricing Calculator export), Appendix 4 (Feedback Record). **No separate Excel workbook artefact** — confirmed not UoC-mandated; all CBA detail lives in Appendix 1 of the Business Case. Simplifies the AT1 submission to a single Word document plus the deck.
- **2026-05-23 (really final today):** Reframed the Board Presentation Deck Template so each slide explicitly names the Business Case section it walks the board through. The deck is now described as "presents your Business Case", with the asked-for decision at the end being approval of the action plan in BC §10. Added a top-level UoC-evidenced block to the deck template to match the convention used in the Business Case template.
