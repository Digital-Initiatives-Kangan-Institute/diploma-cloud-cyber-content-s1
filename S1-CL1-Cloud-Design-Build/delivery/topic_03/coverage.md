# Topic 3 — Building the evidence · Coverage

**Topic 3 of 22** · **AT1 content Topic** (evaluation) · teaching source: **mixed** — bespoke analysis slides + the **AWS Pricing Calculator** activity (a live-tool activity, not image-heavy AWS slides).

The coverage spec — what this Topic must cover, in UoC and AT1 terms. `slide_plan.md` and the deck are built to satisfy it.

---

## What this Topic must cover

Turning the diagnosed *case for change* (Topic 2) into **evidence a board can act on**: what the realistic options are, what each is worth over time, and what could go wrong. It does **not** make the decision (that's Topic 4) — it builds the comparative evidence the decision rests on. Three components:

- **C1 — Options analysis & evaluation.** Defining the workload/requirements an option must satisfy, identifying the realistic options (renew on-prem vs migrate to cloud), choosing an evaluation method, and assessing each option's **impact against the strategic objectives** and its **implementation difficulty**.
- **C2 — Cost-Benefit Analysis.** Building a multi-year (5-year) cost comparison of the options — assumptions, per-option costs, avoided-downtime benefit, comparison summary and a sensitivity check — **sizing the cloud option with the AWS Pricing Calculator**. Applies Topic 1's cost-model knowledge; evidences numeracy.
- **C3 — Risk & impact assessment.** The qualitative complement to the CBA: an intangibles comparison and a risk register for the recommended direction, so the evidence isn't cost-only.

> Components C1–C3 correspond to chunks **AT1 T9–T12**.

---

## 1. UoC mapping

UoC **taught / developed** in this Topic:

| UoC item | Descriptor | Component |
|---|---|---|
| `[ICTICT517 PC 2.1]` | Evaluate impact of proposed changes to ICT systems and products against strategic objectives of organisation | C1 (impact) · C3 (risk/intangibles) |
| `[ICTICT517 PC 2.2]` | Evaluate the difficulty of implementing proposed changes to ICT systems and products | C1 |
| `[ICTICT517 PE 5]` | Evaluate the difficulty of implementing proposed changes | C1 |
| `[ICTICT517 KE 2]` | Methods of evaluation and planning approaches to technical problems and strategic objectives | C1 |
| `[ICTICT517 KE 3]` | Methods of evaluation of competing and complementary internal and external ICT systems and products | C1 |
| `[ICTICT517 FS Numeracy]` | Interprets and uses numerical information (the multi-year CBA) | C2 |

UoC **applied** here but **taught earlier** (not re-taught):

| UoC item | Descriptor | Taught in |
|---|---|---|
| `[ICTCLD401 KE 4]` | Cost models and cloud economic theories across cloud / non-cloud services, and their benefits | Topic 1 (§5) |
| `[ICTCLD502 KE 3]` | Cloud cost models as they relate to scalability of cloud infrastructure | Topic 1 (§5) |

> The CBA (C2) is where Topic 1's cost-model theory is **applied** to real numbers; Topic 3 teaches the *CBA method and the options/risk evaluation*, not the cost models themselves — the same "apply, don't re-teach" split Topic 2 used for cloud knowledge.

---

## 2. AT1 equivalence / alignment

| AT1 element | Criterion | How Topic 3 aligns |
|---|---|---|
| **§6 — Options Considered and Evaluation** | A4 *(provisional — confirm vs AT1 grid)* | Direct — C1 is exactly this: workload definition, options considered, evaluation method, and the impact + difficulty assessment (exemplar §6.1–§6.4). |
| **§7 — Cost-Benefit Analysis** + **Appendix 1** | A5 *(provisional)* | Direct — C2 is the 5-year CBA: assumptions, Option A vs Option B, avoided-downtime benefit, comparison summary, sensitivity (exemplar §7.1–§7.6); detailed line items go in Appendix 1. |
| **§8 — Risk and Impact Assessment** | A6 *(provisional)* | Direct — C3 is the intangibles comparison + risk register (exemplar §8.1–§8.2). |

**Practice-activity alignment:** students add **§6–§8 (+ Appendix 1)** to the **same practice business case** (YAT Accounting System / Ledgerline) they began in Topic 2 — define the options, build a 5-year CBA sized with the AWS Pricing Calculator, and assess risk/impact — mirroring AT1 Part A §6–§8 against a different system.

> Criterion codes A4–A6 are provisional (Topic 2 used A1–A3 for §3–§5; continuing the pattern). Confirm against the AT1 Business Case marking grid when finalised.

---

## Out of scope for this Topic (covered elsewhere)

- **Prioritisation, recommendation and the action plan** (`PC 2.3`, `PE 4`, `PC 3.1`, `PC 3.2` → BC §9–§11) → **Topic 4**.
- **Communicating / pitching the case** (the board presentation) → **Topic 5**.
- **Cloud cost-model theory + AWS service knowledge** → **Topic 1**; only *applied* here (in the CBA and the options).
- **Appendix note:** the Topic spine lists "App. 1 & 3", but the current BC template has only **Appendix 1 (CBA detailed line items)** — owned here — and Appendix 2 (Supporting Research / Knowledge Evidence). There is no Appendix 3; treat the spine reference as a drafting slip.

---

## Coverage checklist (for `slide_plan.md` + the deck to satisfy)

- [ ] Every UoC item in §1 (taught/developed) is taught in the deck.
- [ ] Each of C1–C3 has teaching content + a practice exercise.
- [ ] The exercise has students add **§6–§8 + Appendix 1** to the practice BC (Accounting System), including a CBA sized with the **AWS Pricing Calculator**.
- [ ] Cost-model knowledge is **applied, not re-taught** (assumes Topic 1 §5).
- [ ] Depth ceiling respected: a 5-year comparative CBA + qualitative risk — the AT1 level, not a full financial model or a quantitative risk simulation.
- [ ] AT1 alignment (§2) is explicit enough that a student leaving this Topic could draft the related AT1 sections.
