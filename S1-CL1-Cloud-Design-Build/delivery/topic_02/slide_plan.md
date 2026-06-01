# Topic 2 — The case for change · Slide plan

*The single source for this Topic's teaching + exercise slides, in deck order. (Pairs with `coverage.md`, the UoC/AT spec.)*

**Depth ceiling.** Topic 2 teaches the **analytical setup that justifies change** — to the level needed to write the first half of a Business Case: Strategic Alignment, Current State, and Gap Analysis. It does *not* cover options / cost / risk (Topic 3) or the recommendation & plan (Topic 4). Components map to the Business Case: **C1→Strategic Alignment · C2→Current State · C3→Gap Analysis.**

**Teaching source: all bespoke.** There is no AWS deck for consulting/analysis skills — every teach slide is `[BESPOKE]`. Cloud literacy from Topic 1 is *applied* here (as industry context in C1), not re-taught.

**How to build the single deck:** walk this file top-to-bottom. Each line is one slide, in final order.
- **`[BESPOKE]`** — create the slide from the content block beneath it (the block is a *brief*, not finished copy — write the title + bullets at build time).
- **`[EX]`** — an exercise slide (teach the component, then its exercise, then the next component).

**Exercise spine.** The three component exercises each produce one section of the **practice** Business Case for the **YAT Accounting System (Ledgerline)** — Strategic Alignment, then Current State, then Gap Analysis. Taken together they are the first half of a real case for change, on a different system from the assessment. Inputs students use are all on the YAT intranet (canonical = the **website**): the **ICT Strategic Plan**, the **ICT Environment Overview**, and the Accounting engagement pack (**role brief, migration requirements, consultation notes, application spec, server specs, operational costing**).

**In-world rule.** Slides stay in-world: use the Business Case **section names** (Strategic Alignment / Current State / Gap Analysis), not "§3 / Appendix / AT1", and don't tip which system is the *assessed* one. Keep the UoC / AT / §-mapping in the **speaker notes** only.

---

### Opener

- **`[BESPOKE]`** Topic framing
```
Topic 2 — The case for change
Before you recommend anything, you have to prove change is needed.
- You can now speak cloud (Topic 1). Now you do the consultant's first real job:
  diagnose where the organisation is, where it needs to be, and the gap between.
- Three moves: align to strategy → describe the current state → expose the gaps.
- These three become the opening sections of the Business Case you'll build.
```

- **`[BESPOKE]`** What a "case for change" is (and isn't)
```
A case for change is evidence, not opinion. It answers, in order:
  1. Where does the organisation want to go?   (strategy)
  2. Where is it now?                            (current state)
  3. What's missing to get there?               (gaps)
You are not yet choosing a solution — you're proving the problem is real and worth
solving. Solutions come next (Topic 3). Diagnose before you prescribe.
```

---

### C1 — Strategic alignment analysis  *(→ Business Case: Strategic Alignment)*

- **`[BESPOKE]`** Why a business case opens with strategy
```
A board funds change that moves the organisation toward its own stated goals.
So you start by showing the initiative serves the strategy — not the other way round.
Strategic alignment = "here is what the organisation said it wants; here is how this
initiative delivers it."
```
- **`[BESPOKE]`** How to read a strategic plan — three layers
```
Business objectives = where the whole org is going   (e.g. grow students 15%/yr, expand nationally)
ICT goals/objectives= how ICT supports that          (e.g. reduce in-house dependency; 99.9% for critical systems)
Initiatives         = the planned actions            (e.g. move suitable on-site systems to the cloud)
Your job: trace your initiative UP these layers, and pull only what's MATERIAL to it.
```
- **`[BESPOKE]`** Bring in the outside view — industry context
```
A plan doesn't exist in a vacuum. Compare it to where the industry is heading
(cloud adoption, managed services, OPEX-over-CAPEX, resilience expectations).
Note BOTH:
  - Alignment   — the plan matches industry direction (strengthens the case)
  - Divergence  — the plan lags or differs (a risk, or an opportunity to flag)
```
- **`[BESPOKE]`** What good looks like
```
- Every claim cited to the plan ("ICT Strategic Plan — ICT Goals / Objectives").
- Material items only — not the whole plan recited.
- Traces the initiative up to a real organisational goal.
- Alignment AND divergence both named — balanced, not cheerleading.
```
- **`[EX] [BESPOKE]`** Write the Strategic Alignment section (Accounting engagement)
```
Read YAT's ICT Strategic Plan. Write the Strategic Alignment section of the Business
Case for moving the Accounting System (Ledgerline):
  1. Which ICT goals/objectives does this migration serve? Trace up to a business
     objective where you can. (cite them)
  2. Add one or two points of industry context (where is the sector heading?).
  3. Note alignment AND divergence.
~½ page. Handle the nuances head-on: the plan names the LMS as the FIRST system to move
and sets 99.9% for *critical* systems — Accounting is business-hours and targets 99.5%,
and the headline business objectives (student growth, location-independent learning) are
learning-driven. So argue alignment through the ICT GOALS ("reduce in-house dependency",
"reliable services", "gradually move suitable on-site systems") and name the weaker links
honestly — that IS the analysis.
```
- **`[BESPOKE]`** C1 takeaways
```
- Open with strategy: tie the initiative to the org's own stated goals.
- Three layers — business objectives / ICT goals / initiatives; pull only what's material.
- Add the outside view; name alignment and divergence both.
- Cite everything. Strategy is the "why this, why now".
```

---

### C2 — Current-state synthesis  *(→ Business Case: Current State)*

- **`[BESPOKE]`** What current-state synthesis is
```
Summarise the current environment IN YOUR OWN WORDS, focused on what's material to
THIS decision. Synthesis, not transcription. The reader (the board) needs the picture
that explains why change is needed — not a copy of the IT documentation.
```
- **`[BESPOKE]`** The relevance filter — what to keep, what to drop
```
KEEP (if it bears on the decision):  platform & stack · age / condition / capacity ·
  availability today · dependencies & integrations · constraints · pain points.
DROP:  detail that doesn't move the decision (printer counts, unrelated systems).
A good current state quietly surfaces the LIMITATIONS that motivate the change.
```
- **`[BESPOKE]`** Distil, don't transcribe — technique
```
1. Read the source docs (environment overview, server/app specs, consultation notes).
2. For each fact ask: "does this affect the renew-vs-migrate decision?" If no, cut it.
3. Re-state what's left in plain language, grouped (platform · workload · dependencies
   · condition/risk). Aim ~½ page. No copy-paste.
```
- **`[EX] [BESPOKE]`** Write the Current State section (Accounting engagement)
```
From the Accounting application spec, server specs, operational costing, the ICT
Environment Overview, and the consultation notes, write the Current State section for
the Accounting System in your OWN words:
  platform & stack · workload (incl. month-end/EOFY peaks) · integrations (AD, O365,
  LMS fee-status, payroll bureau, banking) · condition & constraints (server age,
  capacity headroom, availability today).
Material only, ~½ page. No verbatim copying — synthesise.
```
- **`[BESPOKE]`** C2 takeaways
```
- Own words, material facts only — synthesis beats transcription.
- Filter every fact against "does it affect the decision?"
- Surface the limitations that set up the gap analysis.
```

---

### C3 — Gap analysis  *(→ Business Case: Gap Analysis)*

- **`[BESPOKE]`** What gap analysis does
```
Gap analysis is the bridge from "where we want to be" (strategy + requirements) to
"where we are" (current state). It makes the problem concrete and measurable, and it
hands the next stage (options) a list of changes to evaluate. No gap → no case.
```
- **`[BESPOKE]`** The gap table — structure
```
One row per objective/requirement. Columns:
  Objective → Current state → Desired state → Gap → Improvement opportunity → Proposed change
- Objective/Desired come from § Strategic Alignment + the migration requirements.
- Current comes from your Current State section.
- Gap = the honest distance between the two.
- Proposed change = the bridge — and the seed of the options you'll weigh next.
```
- **`[BESPOKE]`** Building a good row — worked shape (neutral)
```
Objective:   "reduce dependency on in-house server infrastructure"
Current:     single ageing on-prem server, owned and maintained by YAT ICT
Desired:     no in-house server to own/patch/replace
Gap:         full reliance on end-of-life hardware YAT must run itself
Opportunity: move to a managed/cloud platform
Proposed:    evaluate migrating the workload to AWS (renew-vs-migrate → Topic 3)
Note: traceable both ways — objective came from the plan, current from your § CurrentState.
```
- **`[EX] [BESPOKE]`** Build the Gap Analysis table (Accounting engagement)
```
Build a gap table of at least 3 rows for the Accounting System. Draw objectives from
the Strategic Alignment work + the migration requirements, e.g.:
  - reduce in-house infrastructure dependency (ageing server)
  - business-hours availability ≥ 99.5% (and recovery: RPO ≤ 1h / RTO ≤ 1 business day)
  - keep financial data onshore + 7-year retention
  - size for month-end / EOFY peaks without year-round over-provisioning
Fill every column: objective → current → desired → gap → opportunity → proposed change.
Each row must trace back to a real objective and your current-state facts.
```
- **`[BESPOKE]`** C3 takeaways
```
- Gap analysis = desired (strategy + requirements) vs current (your synthesis).
- One row per objective; fill all six columns; keep it traceable.
- The "proposed change" column feeds straight into the options analysis next.
```

---

### Close

- **`[BESPOKE]`** From diagnosis to evaluation
```
- You've built the case for change: strategy → current state → gaps. That's the first
  half of a Business Case, and it proves the problem is real and worth solving.
- Your "proposed changes" are not yet decisions — they're candidates.
- Next (Topic 3): weigh the options (renew on-prem vs migrate), cost them, and assess
  the risk — turning the case for change into a recommendation.
```

---

## Build notes

- **All bespoke, ~16 slides** (opener 2 · C1 6 · C2 5 · C3 5 · close 1) — a tight single deck; no AWS source slides, no `source_slides/`.
- **Exercise = build the practice BC's first half.** The three exercises produce Strategic Alignment, Current State, and Gap Analysis for the Accounting System — the same sections AT1 Part A requires (§3–§5), on a different system. Keep the section-name framing on slides; the §/AT mapping lives in speaker notes.
- **Teaching uses neutral/illustrative fragments, not worked Accounting answers** — so the teach slides don't pre-write the exercise. The one worked row in C3 is deliberately generic (the "reduce in-house dependency" objective) and stops short of the full table.
- **Supporting artefact:** none new — all exercise inputs already exist on the YAT website (strategic plan, environment overview, Accounting pack). Confirm the Accounting application spec / server specs / operational costing are published before running C2/C3.
- **Canonical sources = the website** (`diploma-cloud-cyber-website`), not the stale `scenario/MIGRATED/` copies.
- **Speaker-note mapping (trainer):** C1 = ICTICT517 PC 1.1 + PE 1 → BC §3 / A1 · C2 = PC 1.2 + PE 2 → BC §4 / A2 · C3 = PC 1.3 + PE 3 → BC §5 / A3.
