# Topic 10 — Evidencing & documenting · Coverage

**Topic 10 of 14** · **AT2 content Topic** (the final AT2 topic — produce the deliverable) · teaching source: **bespoke** (AWS decks teach the services; writing a Deployment Report + evidencing KE + reflecting to a VET standard is ours to teach).

The coverage spec — what this Topic must cover, in UoC and AT2 terms. `slide_plan.md` and the deck are built to satisfy it.

> **The build becomes the deliverable.** Topics 6–9 built, monitored, validated and justified the workload — capturing evidence the whole way. Topic 10 turns that into the **Deployment Report**, the single AT2 deliverable: organise the evidence, write the narrative + decisions + testing, evidence the contextual knowledge, and reflect. No new building. AT2 = ICTCLD401 (primary — element 4 lands here) + ICTCLD502 (partial).

---

## Teaching-design note — primer-first (no assumed baseline)

Each concept gets a plain primer before the how-to: what **technical documentation** is and who reads it; what makes evidence **traceable** (named, cross-referenced); what a **reflection** is (honest review, not a summary). This Topic is bespoke, so there's no AWS slide to reuse — but the same "explain the fundamental, then do it on the practice scenario" shape holds: **teach → practice** throughout (no AWS demos).

---

## What this Topic must cover

Assemble the AT2 **Deployment Report** from the evidence and decisions produced in Topics 6–9, to the report template, on the practice scenario. Four components:

- **C1 — Evidence into the appendices.** What traceable evidence is (primer) → organise the named screenshots, configuration exports and test results captured since Topic 6 into **Appendix A (screenshots) / B (config exports) / C (test evidence)**, each labelled and referenceable. *(ICTCLD401 PC 4.3 — save and store documentation per organisational policy.)*
- **C2 — Writing the Deployment Report.** The report structure (§1 Exec Summary · §2 Context · §3 Scope · §4 Build/Change Narrative · §5 Configuration Decisions · §6 Testing/Validation · §7 Operational Handover) → write each section, **cross-referencing the appendices**; §5 carries the C1–C8 justifications (Topic 9), §6 the validation (Topic 9). *(ICTCLD401 PC 4.1 — document and communicate work to required personnel.)*
- **C3 — Contextual knowledge evidence.** Some knowledge isn't shown by building — answer the AT2 knowledge questions **grounded in this build** (e.g. shared responsibility, managed vs self-hosted, storage/scaling options, cost models), in context, not abstractly. *(ICTCLD401 KE — evidenced contextually; confirm the AT2 KE list against the assessor doc.)*
- **C4 — Reflection & feedback.** What a professional reflection is (primer) → reflect on the build and process; **seek and respond to feedback** on the work. *(ICTCLD401 PC 4.2 — seek and respond to feedback as required.)*

---

## 1. UoC mapping

UoC **taught / developed** in this Topic:

| UoC item | Descriptor | Component |
|---|---|---|
| [ICTCLD401 PC 4.1] | Document and communicate work to required personnel | C2 |
| [ICTCLD401 PC 4.2] | Seek and respond to feedback as required | C4 |
| [ICTCLD401 PC 4.3] | Save and store user documentation according to organisational policies and procedures | C1 |
| [ICTCLD401 KE 4, 5, 6, 7] | The unit's knowledge evidence — evidenced **contextually** in the report (shared responsibility, managed/self-hosted, storage/scaling/db options, cost models) | C3 |
| [ICTCLD401 PE 1 · PE 2] | The built artefacts are the evidence — assembled into the report's appendices here | C1 |
| `[ICTCLD502]` | Documentation of the implemented architecture (partial — AT2 portion) | C2 *(confirm)* |

> **AT2 marking home:** the **Deployment Report as a whole** (every criterion is evidenced in it); element 4 (documentation/feedback/storage) is *developed* here. Report sections **§1–§7 + Appendices A/B/C**. AT2 build-topic refs **T15 (evidence capture) · T16 (report writing) · T17 (contextual KE) · T18 (reflection)**.

UoC **applied** here but **taught earlier** (not re-taught):

| What | Where |
|---|---|
| The build itself (foundation, network, workload, monitoring) | Topics 6–9 (documented here, not re-built) |
| The C1–C8 justifications; the validation results | Topic 9 (written into §5 / §6 here) |
| Evidence-capture *discipline* (named screenshots / exports as you build) | Topics 6–9 (the captured evidence is *organised* here) |
| Report-writing conventions (audience, traceability) | AT1 (Business Case) — the same professional-writing skills, new document |

---

## 2. AT2 equivalence / alignment

| AT2 element | Criterion | How Topic 10 aligns |
|---|---|---|
| **Appendices A / B / C** | evidence | C1 — captured evidence organised, labelled, referenceable. |
| **§4 Build/Change Narrative** | A-build | C2 — the build written up, cross-referencing the appendices. |
| **§5 Configuration Decisions** | A4 | C2 — the Topic 9 C1–C8 justifications written into the report. |
| **§6 Testing/Validation** | A-build | C2 — the Topic 9 validation results written up (ref Appendix C). |
| **Contextual KE** | KE | C3 — knowledge questions answered grounded in the build. |
| **Reflection / feedback** | element 4 | C4 — reflect on the work; seek + respond to feedback. |

**Practice-activity alignment:** students assemble a **Deployment Report for the practice** engagement (Accounting / Ledgerline) from their captured evidence and Topic 9 justifications — mirroring the AT2 report on the LMS. The report template + the assessor exemplar set the standard.

---

## Out of scope for this Topic (covered elsewhere)

- **Building / monitoring / validating / justifying** → Topics 6–9 (this Topic *documents* them).
- **The HA design + its deployment report** → AT3 (a separate, later deliverable).
- **The Business Case report** → AT1 (same writing skills, different document).
- **Cost-model construction** → AT1 (referenced in a justification, not rebuilt here).

---

## Coverage checklist (for `slide_plan.md` + the deck to satisfy)

- [ ] Each of C1–C4 is covered, **teach → practice** (no AWS demos — bespoke topic).
- [ ] The **Deployment Report template** structure (§1–§7 + Appendices A/B/C) is taught explicitly, and students write to it (C2).
- [ ] **Evidence traceability** is taught: named, organised into the right appendix, and **cross-referenced** from the narrative (C1 + C2).
- [ ] §5 is the home of the **Topic 9 C1–C8 justifications**; §6 the **Topic 9 validation** — the deck shows how they land in the report (C2).
- [ ] **Contextual KE** is evidenced *in the build's context*, not abstractly (C3) — confirm the AT2 KE question list against the assessor doc.
- [ ] **Reflection** is taught as honest review (what worked, what you'd change), and **feedback** is sought + responded to (C4).
- [ ] Student-facing slides stay in-world; the report is for "YAT/MTS personnel"; AWS source refs n/a (bespoke topic).
- [ ] Depth/scope: documents the **baseline** build; the HA report is AT3.
- [ ] AT2 alignment (§2) explicit enough that a student leaving this Topic could assemble a complete, evidenced, justified Deployment Report.
