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
  notes:
    Frame the finalisation half — turn Topic 3's analysis into a chosen strategy and a documented plan. Set the three moves and the boundary.
    • First bullet: callback — Topic 3 set the requirements, objectives and RISKS; Topic 4 turns them into a PLAN. Today consumes yesterday's output; keep the impact analysis on the desk.
    • Second bullet: name the three moves — EVALUATE the DR strategies, CHOOSE one to the objectives, WRITE the plan. In that order.
    • Third bullet (accent it): the plan must MAP to the prioritised risks AND meet the RTO/RPO you set — those two Topic-3 outputs are the acceptance test for everything today.
    • Hold the boundary (last bullet): PLANNING ONLY — recovery is not executed here. A documented plan is the deliverable, not a failover.
    Misconception to pre-empt: "the plan is just picking a DR strategy." No — a plan is strategy PLUS runbook, escalation, comms and DNS failover, aligned to the risks and provably meeting RTO/RPO. The strategy is one part.
    Question to pose: "Before you choose a DR strategy, what two Topic-3 numbers must you already have in hand?" (the RTO/RPO objectives and the ranked risks — the strategy is chosen to meet them).
    UoC/AT1 tie: this Topic develops [ICTCLD501 PC 3.1]–[ICTCLD501 PC 3.4], [ICTCLD501 PC 4.1]–[ICTCLD501 PC 4.3], [ICTCLD501 PE 1]/[ICTCLD501 PE 3] and [ICTCLD501 KE 3]/[ICTCLD501 KE 4], evidenced in AT1 Part B §5–6 and the KE appendix.

### C1 — Range of DR solutions
- Teaches: [ICTCLD501 PC 3.1] · [ICTCLD501 PE 1] · [ICTCLD501 KE 3]
- Kicker: four strategies, one choice
- [PRIMER] The four cloud DR strategies
  - Backup & restore: cheapest, slowest — restore from backups after an event.
  - Pilot light: core data live in a second region, minimal standby; scale up on failover.
  - Warm standby: a scaled-down running copy, ready to take load quickly.
  - Multi-region active-active: full running copies, near-zero RTO/RPO, highest cost.
  image: none
  notes:
    Teach the four cloud DR strategies as a SPECTRUM of cost vs speed — the core KE of the Topic. Walk them cheapest/slowest to priciest/fastest; the trade-off table on the next slide reinforces this.
    • BACKUP & RESTORE: cheapest, slowest — restore from backups after an event. Nothing runs until you need it; recovery is measured in hours.
    • PILOT LIGHT: core DATA live in a second region, minimal standby; scale UP on failover. The data's already there; you spin up compute when disaster strikes.
    • WARM STANDBY: a scaled-DOWN running copy, ready to take load quickly. It's already running, just small — faster failover, higher standing cost.
    • ACTIVE-ACTIVE: full running copies, NEAR-ZERO RTO/RPO, HIGHEST cost. Both sides live all the time; you pay for a full duplicate.
    Misconception to pre-empt: "active-active is the 'best' one." No — the BEST strategy is the SIMPLEST that meets the objectives; active-active is overkill (and overspend) unless the RTO/RPO genuinely demand it.
    Question to pose: "As you move down the list, what are you buying, and what are you paying for it?" (faster recovery / less data loss, paid for with rising standing cost and complexity).
    UoC/AT1 tie: [ICTCLD501 KE 3] (DR techniques for cloud) + [ICTCLD501 PC 3.1] (develop a range of DR solutions) — AT1 Part B B8 and the KE appendix.
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
  notes:
    Teach the CHOICE discipline — evaluate the four strategies against the Topic-3 objectives and pick deliberately. This is the assessable judgement, not the memorised list.
    • First bullet: EVALUATE each strategy against the Topic-3 RTO/RPO and the BUDGET. You're matching a strategy's capability to your specific targets, not ranking them in the abstract.
    • Second bullet: DEVELOP A RANGE of solutions, THEN choose the SIMPLEST that meets the requirements (PE 1). Showing the range considered is part of the evidence — don't jump straight to one.
    • Third bullet (accent it): JUSTIFY the choice — "cheaper is right UNTIL it fails an objective." Start cheap and step up only when a target forces you to; that's the reasoning assessors look for.
    Misconception to pre-empt: "choose the strongest strategy to be safe." No — choosing beyond the objectives is over-engineering and overspend; the mark is for the SIMPLEST strategy that still meets RTO/RPO and budget.
    Question to pose: "Backup & restore gives a 4-hour recovery but your RTO is 30 minutes — what's the CHEAPEST strategy that still meets it?" (step up the spectrum only as far as the objective forces — likely pilot light/warm standby).
    UoC/AT1 tie: [ICTCLD501 PC 3.1] + [ICTCLD501 PE 1] (develop and evaluate a range, choose one) — AT1 Part B B8; the justification earns the criterion.
- [EX] Evaluate & choose a strategy
  - For the practice scenario, evaluate the four strategies against the objectives.
  - Choose one and justify it against RTO/RPO and cost.
  timer: ~20 min
  image: none
  notes:
    Facilitation — the C1 practice: evaluate the four strategies and choose one for the practice scenario. Rehearses AT1 Part B B8.
    Tell students: "For the practice scenario, evaluate all four DR strategies against the RTO/RPO and budget you set in Topic 3 — then choose ONE and justify it. Show the range you considered, not just the winner."
    Steps (put on the board):
    1. Line up the four strategies against your objectives (use the trade-off table as a lens).
    2. Eliminate the ones that miss RTO/RPO or blow the budget — say why each is out.
    3. Choose the SIMPLEST survivor and justify it against RTO/RPO and cost.
    Must produce: a short evaluation of all four plus a justified choice tied to the objectives.
    Timing: ~20 min. Where they get stuck: they jump straight to active-active "to be safe" (push simplest-that-fits), and they choose with no numbers (make them cite their RTO/RPO).
    Share-back prompt: "Name your choice and the objective that ruled out the cheaper option below it" — surfaces the step-up reasoning.
    No-leakage note: practice scenario only (comparable, not identical); AT1 evidences the same evaluate-and-choose skill on the assessed system — keep them on the practice brief.
    UoC/AT1 tie: [ICTCLD501 PC 3.1] · [ICTCLD501 PE 1] · [ICTCLD501 KE 3] — develop a range, evaluate, choose (AT1 Part B B8).

### C2 — Vendor protections, prioritisation & other components
- Teaches: [ICTCLD501 PC 3.2] · [ICTCLD501 PC 3.3] · [ICTCLD501 PC 3.4] · [ICTCLD501 KE 4]
- Kicker: native protections, priorities, and the rest of the plan
- [BESPOKE] Lean on native protections & prioritise
  - Use the vendor's native protections: automated backups, cross-region copy, durable/immutable storage.
  - Prioritise the recovery against the risks — restore the highest-severity, business-critical parts first.
  - Native durability does the heavy lifting; your plan sequences and governs it.
  image: none
  notes:
    Open C2 — the rest of a plan beyond the strategy. Teach leaning on NATIVE protections and PRIORITISING recovery against the ranked risks.
    • First bullet: use the vendor's NATIVE protections — automated backups, cross-region copy, durable/immutable storage. These are already reliable and cheap; build on them rather than rolling your own.
    • Second bullet: PRIORITISE the recovery against the RISKS — restore the highest-severity, business-critical parts FIRST. This is where Topic 3's ranking pays off; recovery order is set by severity, not convenience.
    • Third bullet (accent it): native durability does the HEAVY LIFTING; your plan SEQUENCES and GOVERNS it. Your value-add is orchestration and priority, not re-implementing storage durability.
    Misconception to pre-empt: "restore everything at once." No — you SEQUENCE recovery by severity/criticality; some systems wait. Priority order, driven by the impact analysis, is the assessable decision.
    Question to pose: "In a real recovery you can't bring everything back simultaneously — what decides the order?" (the risk ranking / business criticality from Topic 3 — restore highest-severity, critical systems first).
    UoC/AT1 tie: [ICTCLD501 PC 3.2] (prioritise recovery against risks) + [ICTCLD501 PC 3.4] (other DR components) + [ICTCLD501 KE 4] — AT1 Part B B11.
- [BESPOKE] Insurance & the other plan components
  - Insurance is a complementary risk-transfer control — it covers residual loss, it does not restore service.
  - Other components: the runbook, declaration/escalation, communications, and DNS failover.
  - A plan is more than a strategy — it is who does what, in what order, and how people are told.
  image: none
  notes:
    Teach the OTHER plan components — insurance as a complement, plus the operational parts that turn a strategy into a usable plan.
    • First bullet: INSURANCE is a COMPLEMENTARY risk-transfer control — it covers RESIDUAL loss, it does NOT restore service. Money back is not uptime; it sits alongside recovery, never replaces it.
    • Second bullet: name the OTHER components — the RUNBOOK, DECLARATION/ESCALATION, COMMUNICATIONS, and DNS FAILOVER. Each is a plan ingredient students forget because they fixate on the strategy.
    • Third bullet (accent it): a plan is MORE than a strategy — it's WHO does WHAT, in WHAT ORDER, and how PEOPLE are TOLD. The human/process side is as assessed as the technical one.
    Misconception to pre-empt: "insurance is an alternative to DR." No — it transfers residual financial risk; it buys none of your RTO back. It's a complementary control, listed alongside the recovery components, not instead of them.
    Question to pose: "Your cloud provider fully refunds the outage — are you recovered?" (No — a refund isn't restored service; insurance covers residual loss, recovery restores the system).
    UoC/AT1 tie: [ICTCLD501 PC 3.3] (insurance as a complementary control) + [ICTCLD501 PC 3.4] (identify other DR components) — AT1 Part B B11.
- [PRIMER] Continuity standards
  - ISO/IEC 27031 — ICT readiness for business continuity; 27001/27002 — the security management context.
  - Standards give the plan a recognised structure and assurance language.
  - Reference them so the plan is auditable, not ad hoc.
  image: none
  notes:
    Teach the CONTINUITY STANDARDS — the recognised frameworks that give the plan structure and assurance. Vendor-neutral; brief but examinable (KE 4).
    • First bullet: ISO/IEC 27031 — ICT READINESS for business continuity (the DR-relevant one); 27001/27002 — the security MANAGEMENT context around it. Know which standard covers what.
    • Second bullet: standards give the plan a RECOGNISED STRUCTURE and assurance LANGUAGE — you're not inventing terms; you're speaking a language auditors and clients already trust.
    • Third bullet (accent it): REFERENCE them so the plan is AUDITABLE, not ad hoc. Citing the standard is what lets an external party assure the plan.
    Misconception to pre-empt: "we have to fully implement ISO 27031." No — at this level you REFERENCE the relevant standards to structure and justify the plan; certification is a separate organisational undertaking.
    Question to pose: "Which of these standards is the one specifically about ICT readiness for continuity?" (27031 — 27001/27002 are the broader security-management context).
    UoC/AT1 tie: [ICTCLD501 KE 4] (ISO/IEC 27001/27002/27031) — AT1 Part B KE appendix (B15).
- [EX] Prioritise & list the other components
  - For the practice scenario, set the recovery priority against the risks.
  - List the vendor protections leaned on and the other plan components (runbook, escalation, comms, DNS).
  timer: ~20 min
  image: none
  notes:
    Facilitation — the C2 practice: set the recovery PRIORITY and list the plan's other components for the practice scenario. Rehearses AT1 Part B B11.
    Tell students: "For the practice scenario, set the recovery PRIORITY order against your ranked risks — then list the vendor native protections you'll lean on and the other plan components: runbook, escalation, comms, DNS failover."
    Steps (put on the board):
    1. Order the recovery by severity/criticality — what comes back first, second, third, and why.
    2. List the native protections you'll build on (backups, cross-region copy, durable storage).
    3. List the other components: runbook, declaration/escalation, communications, DNS failover — note insurance if relevant as a residual-loss control.
    Must produce: a prioritised recovery order plus a components checklist (native protections + operational components).
    Timing: ~20 min. Where they get stuck: they try to recover everything at once (force a priority order tied to the risk ranking), and they list only technical parts (prompt "who declares the disaster? how are people told?").
    Share-back prompt: "What recovers first, and which risk ranking put it there?" — ties priority back to Topic 3.
    No-leakage note: practice scenario only (comparable, not identical); AT1 evidences the same prioritise-and-components skill on the assessed system — keep them on the practice brief.
    UoC/AT1 tie: [ICTCLD501 PC 3.2] · [ICTCLD501 PC 3.3] · [ICTCLD501 PC 3.4] · [ICTCLD501 KE 4] — prioritisation + the other plan components (AT1 Part B B11).

### C3 — The disaster recovery plan
- Teaches: [ICTCLD501 PC 4.1] · [ICTCLD501 PC 4.2] · [ICTCLD501 PC 4.3] · [ICTCLD501 PE 1] · [ICTCLD501 PE 3]
- Kicker: aligned, timed, and provably on target
- [BESPOKE] Align actions to the prioritised risks
  - For each prioritised risk, state the recovery action that addresses it.
  - The plan must cover at least the three major risk events from the impact analysis (PE 1).
  - Alignment is the test: every high-severity risk has an owned recovery action.
  image: none
  notes:
    Open C3 — assembling the actual plan. Teach ALIGNMENT: every prioritised risk maps to a recovery action. This is the plan's core integrity test.
    • First bullet: for EACH prioritised risk, state the recovery ACTION that addresses it — a one-to-one mapping from risk to response, no risk left unanswered.
    • Second bullet: the plan must cover at least the THREE major risk events from the impact analysis (PE 1) — the same three from Topic 3; the analysis and the plan must line up.
    • Third bullet (accent it): ALIGNMENT is the test — every high-severity risk has an OWNED recovery action. "Owned" means a named responsible party, not just an action floating in the plan.
    Misconception to pre-empt: "the plan is a general recovery procedure." No — it must trace RISK → ACTION for each prioritised risk; a generic procedure that doesn't map to the specific analysed risks fails alignment.
    Question to pose: "You have five ranked risks and a plan with four actions — what does that gap tell you?" (a high-severity risk has no owned recovery action — the plan isn't aligned yet).
    UoC/AT1 tie: [ICTCLD501 PC 4.1] (align DR actions to risks per requirements) + [ICTCLD501 PE 1] (plan covers ≥3 major risk events) — AT1 Part B B12.
- [BESPOKE] Steps, timelines & meeting RTO/RPO
  - Outline the recovery steps, their timelines, key features and the service providers involved.
  - Show how the sequence meets the RTO/RPO targets — the timing has to add up (PE 3).
  - Name who executes each step and what "recovered" looks like.
  image: diagram dr-runbook-flow
  notes:
    The keystone C3 slide — the runbook: ordered steps with timings that provably meet RTO/RPO. Use the runbook-flow diagram to walk the sequence and add up the time live.
    • First bullet: outline the recovery STEPS, their TIMELINES, key FEATURES and the SERVICE PROVIDERS involved — a runbook is specific and sequenced, not a paragraph of intent.
    • Second bullet (accent it): SHOW how the sequence MEETS the RTO/RPO targets — the timing has to ADD UP (PE 3). Sum the step timings and compare to the RTO; if the total exceeds it, the plan fails and must be revised.
    • Third bullet: NAME who executes each step and what "RECOVERED" looks like — a definition of done, and an owner per step. No anonymous actions.
    • On the diagram: trace detect → declare → recover-in-priority-order → verify, and point at where the RTO clock starts and stops.
    Misconception to pre-empt: "if I list the right steps, RTO is met." No — you must ARITHMETICALLY show the timeline adds up to within RTO/RPO; PE 3 is explicitly about DOCUMENTING how the targets are reached, not just naming steps.
    Question to pose: "Your steps total 90 minutes but the RTO is 60 — what has to change?" (re-sequence, parallelise, or step up the DR strategy; the timing must fit the target).
    UoC/AT1 tie: [ICTCLD501 PC 4.2] (steps, timelines, features, providers) + [ICTCLD501 PE 3] (document how the plan reaches RTO/RPO) — AT1 Part B B13; this runbook is the PE 3 evidence.
- [BESPOKE] Document the plan
  - Document the DR plan to the business needs, in the YAT template and plain professional English.
  - Complete, internally consistent, and traceable back to the requirements and risks.
  - This documented plan is the Part B deliverable.
  image: none
  notes:
    Teach the DOCUMENTATION step — turning the aligned actions and runbook into the finished, professional DR plan. This is the Part B deliverable itself.
    • First bullet: DOCUMENT the plan to the BUSINESS NEEDS, in the YAT TEMPLATE and PLAIN professional English — a client-ready document, written for the business, not a pile of engineer's notes.
    • Second bullet: COMPLETE, internally CONSISTENT, and TRACEABLE back to the requirements and risks — the reader can follow any action back to the risk and requirement that drove it.
    • Third bullet (accent it): this documented plan IS the Part B deliverable — everything in Topics 3–4 exists to produce this artefact.
    Misconception to pre-empt: "documenting is a formatting pass at the end." No — documenting to business needs, to the template, and traceably is an assessed criterion (PC 4.3); it's the deliverable, not decoration.
    Question to pose: "A marker reads your plan cold — what makes it traceable back to the risks and requirements?" (every recovery action references the prioritised risk and the objective it serves — no orphan actions).
    UoC/AT1 tie: [ICTCLD501 PC 4.3] (document the DR plan to business needs) — AT1 Part B B14; the documented plan is the Part B §6 deliverable.
- [EX] Write the DR plan
  - For the practice scenario, write the recovery plan: aligned actions, steps/timelines/providers, and the RTO/RPO argument.
  - Produce it as a documented runbook.
  timer: ~30 min
  image: none
  notes:
    Facilitation — the biggest activity in the Topic: students write the full DR plan for the practice scenario. The capstone AT1 Part B §6 rehearsal, building on everything from Topics 3–4.
    Tell students: "For the practice scenario, write the recovery plan — align an owned action to each prioritised risk, lay out the steps with timelines and providers, and MAKE THE ARITHMETIC show the sequence meets your RTO/RPO. Produce it as a documented runbook."
    Steps (put on the board):
    1. Map each prioritised risk to an owned recovery action (cover at least your three major risks).
    2. Sequence the steps with timelines and the service providers involved.
    3. Add up the timings and show they meet RTO/RPO — revise the sequence if they don't.
    4. Document it to business needs, in plain professional English (the YAT template shape).
    Must produce: a documented runbook — aligned actions, sequenced steps with timings, an explicit RTO/RPO argument.
    Timing: ~30 min. Where they get stuck: they write steps but never prove the timing meets RTO (make them add it up — PE 3), and they leave actions unowned (every step needs a "who").
    Share-back prompt: "Walk one risk from the register through to its recovery action and show the clock fits RTO" — surfaces alignment AND timing.
    No-leakage note: practice scenario only (comparable, not identical); AT1 evidences the same plan-writing skill on the assessed system — keep them on the practice brief.
    UoC/AT1 tie: [ICTCLD501 PC 4.1] · [ICTCLD501 PC 4.2] · [ICTCLD501 PC 4.3] · [ICTCLD501 PE 1] · [ICTCLD501 PE 3] — the full plan-writing core of AT1 Part B §6.
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
