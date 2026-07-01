# Topic 04 DR: strategy & plan — Slide plan
> **Covers:** Topic 04 — see coverage.md
> **Subtitle:** Choose a recovery strategy to the objectives and produce the documented DR plan
> **STATUS: DRAFT** (authored 2026-07-01).

## Depth ceiling
PLAN — develop solution options, choose one to the objectives, and produce the documented recovery plan. Build on Topic 3's requirements + impact analysis. The plan is not executed.

## Teaching source
AWS DR strategies (backup-restore / pilot-light / warm-standby / multi-region active-active) pinned at Step 4 (TBD); bespoke for the choice, the other plan components, and the documented plan.

## AWS pin table
TBD — AWS DR-strategy modules (backup-restore, pilot-light, warm-standby, active-active) to be pinned.

## Slides

### Opener
- [BESPOKE] From analysis to a plan
  - Topic 3 set the requirements, objectives and risks; Topic 4 turns them into a recovery plan.
  - You evaluate the DR strategies, choose one to the objectives, and write the plan.
  - The plan must map to the prioritised risks and meet the RTO/RPO you set.
  - Planning only — recovery is not executed here.
  image: gen flat vector hero illustration of a decision path leading to a document with a checkmark, blue and gold accents, minimal, no text

### C1 — Range of DR solutions
- Teaches: [ICTCLD501 PC 3.1] · [ICTCLD501 PE 1] · [ICTCLD501 KE 3]
- Kicker: four strategies, one choice
- [PRIMER] The four cloud DR strategies
  - Backup & restore: cheapest, slowest — restore from backups after an event.
  - Pilot light: core data live in a second region, minimal standby; scale up on failover.
  - Warm standby: a scaled-down running copy, ready to take load quickly.
  - Multi-region active-active: full running copies, near-zero RTO/RPO, highest cost.
  image: none
- [TABLE] Strategy trade-offs
  | Strategy | RTO | RPO | Cost |
  | Backup & restore | Hours | Hours | Low |
  | Pilot light | ~10s of min | Minutes | Medium |
  | Warm standby | Minutes | Seconds–min | Higher |
  | Active-active | Near-zero | Near-zero | Highest |
  note: DR techniques for the cloud (KE 3); the right choice is the simplest that meets the objectives.
  image: none
- [BESPOKE] Evaluate & choose to the objectives
  - Evaluate each strategy against the Topic 3 RTO/RPO and the budget.
  - Develop a range of solutions, then choose the simplest that meets the requirements (PE 1).
  - Justify the choice — cheaper is right until it fails an objective.
  image: none
- [EX] Evaluate & choose a strategy
  - For the practice scenario, evaluate the four strategies against the objectives.
  - Choose one and justify it against RTO/RPO and cost.
  timer: ~20 min
  image: none

### C2 — Vendor protections, prioritisation & other components
- Teaches: [ICTCLD501 PC 3.2] · [ICTCLD501 PC 3.3] · [ICTCLD501 PC 3.4] · [ICTCLD501 KE 4]
- Kicker: native protections, priorities, and the rest of the plan
- [BESPOKE] Lean on native protections & prioritise
  - Use the vendor's native protections: automated backups, cross-region copy, durable/immutable storage.
  - Prioritise the recovery against the risks — restore the highest-severity, business-critical parts first.
  - Native durability does the heavy lifting; your plan sequences and governs it.
  image: none
- [BESPOKE] Insurance & the other plan components
  - Insurance is a complementary risk-transfer control — it covers residual loss, it does not restore service.
  - Other components: the runbook, declaration/escalation, communications, and DNS failover.
  - A plan is more than a strategy — it is who does what, in what order, and how people are told.
  image: none
- [PRIMER] Continuity standards
  - ISO/IEC 27031 — ICT readiness for business continuity; 27001/27002 — the security management context.
  - Standards give the plan a recognised structure and assurance language.
  - Reference them so the plan is auditable, not ad hoc.
  image: none
- [EX] Prioritise & list the other components
  - For the practice scenario, set the recovery priority against the risks.
  - List the vendor protections leaned on and the other plan components (runbook, escalation, comms, DNS).
  timer: ~20 min
  image: none

### C3 — The disaster recovery plan
- Teaches: [ICTCLD501 PC 4.1] · [ICTCLD501 PC 4.2] · [ICTCLD501 PC 4.3] · [ICTCLD501 PE 1] · [ICTCLD501 PE 3]
- Kicker: aligned, timed, and provably on target
- [BESPOKE] Align actions to the prioritised risks
  - For each prioritised risk, state the recovery action that addresses it.
  - The plan must cover at least the three major risk events from the impact analysis (PE 1).
  - Alignment is the test: every high-severity risk has an owned recovery action.
  image: none
- [BESPOKE] Steps, timelines & meeting RTO/RPO
  - Outline the recovery steps, their timelines, key features and the service providers involved.
  - Show how the sequence meets the RTO/RPO targets — the timing has to add up (PE 3).
  - Name who executes each step and what "recovered" looks like.
  image: diagram dr-runbook-flow
- [BESPOKE] Document the plan
  - Document the DR plan to the business needs, in the YAT template and plain professional English.
  - Complete, internally consistent, and traceable back to the requirements and risks.
  - This documented plan is the Part B deliverable.
  image: none
- [EX] Write the DR plan
  - For the practice scenario, write the recovery plan: aligned actions, steps/timelines/providers, and the RTO/RPO argument.
  - Produce it as a documented runbook.
  timer: ~30 min
  image: none
- [TAKEAWAYS] Topic 4 · Key takeaways
  - Four strategies (backup-restore → active-active) trade RTO/RPO against cost; choose the simplest that fits.
  - Lean on native protections; prioritise recovery against the risks; insurance transfers residual loss only.
  - A plan is strategy + runbook + escalation + comms + DNS failover, to a continuity standard.
  - Align actions to the prioritised risks and show the timing meets RTO/RPO.
  image: none

### Close
- [BESPOKE] Next: Topic 5 — document & present
  - You've produced the Solution Design (Topics 1–2) and the DR plan (Topics 3–4).
  - Next you assemble, justify, present and get sign-off — the AT1 close-out.
  image: none

## Build notes
~18 slides. Exercises run on the practice scenario (planning only). One generated diagram (`diagram dr-runbook-flow`); one decorative `gen` image (opener hero); two TABLEs (strategy trade-offs — one in C1).

## Changelog
- 2026-07-01 — authored to full content.
