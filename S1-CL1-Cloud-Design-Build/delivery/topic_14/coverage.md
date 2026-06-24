# Topic 14 — Closure & documentation · Coverage

**Topic 14 of 14** · **AT3 content Topic** (the final topic — produce the HA deliverable + close the engagement) · teaching source: **bespoke** (writing the HA Deployment Report, evidencing KE, reflecting and closing to a VET standard) + **ICTCLD502 Topic 4** S11–S12 (feedback & sign-off).

The coverage spec — what this Topic must cover, in UoC and AT terms. `slide_plan.md` and the deck are built to satisfy it.

> **Close it out.** Topic 13 implemented + simulated the HA design; Topic 14 turns that into the **HA Deployment Report**, evidences the contextual knowledge, **reflects**, and **closes the engagement with feedback + sign-off** (ICTCLD502 element 5.2–5.3). It's the AT3 analogue of Topic 10 (AT2 documenting), plus the distinct *finalise* element. This closes AT3 — and the course's build arc. AT3 = ICTCLD502 (primary).

---

## Teaching-design note

Bespoke, **teach → practice** throughout (no AWS demos — report-writing/closure isn't an AWS task). The deliverable is the **HA Deployment Report** (the AT3 template), assembled from the Topic 13 evidence + simulation findings. The one reused source is **502 Topic 4 S11–S12** (collecting feedback + obtaining sign-off).

---

## What this Topic must cover

Produce the HA Deployment Report and close the engagement, on the practice scenario. Three components:

- **C1 — Write the HA Deployment Report.** Organise the implementation + simulation evidence into Appendices A/B/C; write the report to the template — §4 the HA changes from baseline, §5 the HA config decisions, **§6 the simulation findings (the heart)**, §7 handover. *(ICTCLD502 PC 3.5 — document the implemented design.)*
- **C2 — Contextual knowledge evidence.** Answer the AT3 knowledge questions (§8) **grounded in the HA work** — availability, fault tolerance, recovery objectives, redundancy — referencing the actual design + simulations. *(ICTCLD502 KE, evidenced contextually.)*
- **C3 — Close the engagement.** **Seek and respond to feedback**, **obtain final sign-off**, and **reflect** (Appendix D) — the finalise step. *(ICTCLD502 PC 5.2, 5.3.)*

---

## 1. UoC mapping

UoC **taught / developed** in this Topic:

| UoC item | Descriptor | Component |
|---|---|---|
| [ICTCLD502 PC 3.5] | Document architecture design (the implemented HA design, as-built) | C1 |
| [ICTCLD502 PC 4.6] | Compare and document simulation findings according to documented design | C1 *(written up in §6; produced in Topic 13)* |
| [ICTCLD502 PC 5.2] | Confirm, seek and respond to feedback with required personnel | C3 |
| [ICTCLD502 PC 5.3] | Obtain final sign off from required personnel | C3 |
| [ICTCLD502 KE 4] | The unit's knowledge evidence — evidenced **contextually** in §8 (availability, fault tolerance, recovery objectives, redundancy) | C2 |
| [ICTCLD502 PE 1] | The fault-tolerant infrastructure — its design, implementation and validation documented here | C1 |

> **AT3 marking home:** the **HA Deployment Report as a whole** (incl. §6 simulation findings, §8 KE, Appendix D reflection) + the closure (feedback + sign-off). AT3 build-topic refs **T15–T18** (evidence capture · deliverable writing · contextual KE · reflection) + element 5 closure.

UoC **applied** here but **taught earlier** (not re-taught):

| What | Where |
|---|---|
| The implementation + simulation findings being written up | Topic 13 (produced there) |
| The HA design | Topic 12 |
| Report-writing + evidence discipline | Topic 10 (AT2) — same skills, the HA report |

---

## 2. AT3 equivalence / alignment

| AT3 element | Where assessed | How Topic 14 aligns |
|---|---|---|
| **Document the implemented HA design** | the HA Deployment Report | C1 — §4 narrative, §5 decisions, §6 simulation findings, §7 handover, Appendices A–C. |
| **Contextual KE** | report §8 | C2 — knowledge questions answered grounded in the HA build. |
| **Finalise** (502 element 5.2–5.3) | §7.5 feedback · §7.6 sign-off | C3 — seek/respond to feedback; obtain final sign-off; reflect (Appendix D). |

**Practice-activity alignment:** students assemble the **HA Deployment Report for the practice** engagement (Accounting / Ledgerline) from their Topic 13 evidence + simulation findings, and close it out — mirroring the AT3 closure on the LMS.

---

## Out of scope for this Topic (covered elsewhere)

- **Implementing / simulating** → Topic 13 (documented + closed here).
- **Designing the HA architecture** → Topic 12.
- **The AT2 Deployment Report** → Topic 10 (same skills, different deliverable).
- **Multi-Region / full DR** → CL2.

---

## Coverage checklist (for `slide_plan.md` + the deck to satisfy)

- [ ] All bespoke, **teach → practice** (no AWS demos).
- [ ] The **HA Deployment Report template** (§1–§8 + Appendices A–D) is taught; students write to it (C1).
- [ ] **§6 simulation findings** is framed as the heart of the report (the proof of fault tolerance) (C1).
- [ ] Evidence is organised + cross-referenced into Appendices A/B/C (C1).
- [ ] **Contextual KE (§8)** answered grounded in the HA work, not abstractly (C2).
- [ ] **Feedback (§7.5)** sought + responded to, **sign-off (§7.6)** obtained, **reflection (Appendix D)** written — the finalise element (C3).
- [ ] In-world; source refs by title may stay; UoC refs off slides.
- [ ] Closes the AT3 arc (and the course's advise → build → harden journey).
