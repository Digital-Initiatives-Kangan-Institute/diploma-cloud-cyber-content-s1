# Topic 04 DR: strategy & plan — Slide plan
> **Covers:** Topic 04 — see coverage.md
> **Subtitle:** Choose a recovery strategy to the objectives and assemble the documented DR plan
> **STATUS: DRAFT — redrafted 2026-09-08 from the AT1 Part B practice workbook, tasks 28–37 and the
> assessment's knowledge question Q7.**

## Depth ceiling
PLAN — the back half of the DR plan on the practice workbook: evaluate options, recommend an approach,
add the supporting components, write the detection and recovery steps, prove the objectives are met,
and assemble the plan. Built on Topic 3's analysis; the plan is never executed.

**Answer discipline:** activities run on the practice workbook; the assessment is the same work on the
assessed system. Teach the method on the practice vehicle; never supply assessed-system answers.

## Teaching source
AWS DR strategies (backup-restore / pilot-light / warm-standby / active-active) pinned at Step 4
(TBD); bespoke for the choice, the plan components, and the assembled plan.

## AWS pin table
TBD — AWS DR-strategy modules (backup-restore, pilot-light, warm-standby, active-active) to be pinned.

## Slides

### Opener
- [BESPOKE] From analysis to a plan
  - Topic 3 set the objectives and ranked the risks; Topic 4 turns them into a recovery plan.
  - You evaluate the strategies, recommend one, add everything else a plan carries, and assemble it.
  - The plan must map to the prioritised risks and provably meet the objectives you set.
  - Planning only — recovery is not executed here.
  image: gen flat vector hero illustration of a decision path leading to a document with a checkmark, blue and gold accents, minimal, no text
  notes:
    Today consumes Topic 3's output — the register and objectives stay on the desk; workbook tasks 28 to 37 in order.
    Misconception: the plan is just picking a strategy. The strategy is one row; the plan is everything from detection to sign-off.

### C1 — Evaluate the options, recommend an approach
- Teaches: [ICTCLD501 PC 3.1] · [ICTCLD501 PC 4.1] · [ICTCLD501 KE 3]
- Kicker: four strategies, one recommendation
- [PRIMER] The four cloud DR strategies
  - Backup and restore: cheapest, slowest — restore from backups after an event.
  - Pilot light: core data live in a second region, minimal standby; scale up on failover.
  - Warm standby: a scaled-down running copy, ready to take load quickly.
  - Multi-region active-active: full running copies, near-zero recovery targets, highest cost.
  image: none
  notes:
    A spectrum of cost against speed, walked cheapest to priciest — the core examinable content of the Topic.
    Misconception: active-active is "best". The best strategy is the simplest that meets the objectives.
- [TABLE] Strategy trade-offs
  | Strategy | RTO | RPO | Cost |
  | Backup & restore | Hours | Hours | Low |
  | Pilot light | ~10s of min | Minutes | Medium |
  | Warm standby | Minutes | Seconds–min | Higher |
  | Active-active | Near-zero | Near-zero | Highest |
  note: The right choice is the simplest that meets the objectives.
  image: none
- [BESPOKE] Evaluate the options, then recommend
  - Evaluate each strategy against the objectives and budget from your own analysis — a range considered is part of the evidence.
  - Recommend the simplest option that meets the requirements, and say what ruled out the cheaper ones.
  - Cheaper is right until it fails an objective.
  image: none
  notes:
    Workbook tasks 28 and 29 — the evaluation then the recommendation, as separate written steps.
    The step-up reasoning is what markers look for: start cheap, move up only when a target forces it.
- [EX] Evaluate and recommend
  - Workbook — tasks 28 and 29.
  - Evaluate the recovery options against your objectives, then record the recommended approach and what ruled the others out.
  timer: ~25 min
  image: none
  notes:
    Activity = practice workbook tasks 28–29.
    Watch for jumping straight to active-active "to be safe", and choices made with no numbers cited.
- [TAKEAWAYS] Section 1 · The choice
  - Four strategies trade recovery speed against standing cost.
  - Show the range considered; recommend the simplest that fits.
  - Every elimination cites an objective.
  image: none

### C2 — The rest of the plan
- Teaches: [ICTCLD501 PC 3.2] · [ICTCLD501 PC 3.3] · [ICTCLD501 PC 3.4]
- Kicker: native protections, priorities, and the parts everyone forgets
- [BESPOKE] Lean on native protections and prioritise
  - Use the vendor's native protections: automated backups, cross-region copy, durable storage.
  - Prioritise recovery against the ranked risks — the highest-severity, business-critical parts come back first.
  - Native durability does the heavy lifting; your plan sequences and governs it.
  image: none
  notes:
    Workbook task 30. Recovery order is set by the Topic 3 ranking, not by convenience.
    Question to pose: you can't bring everything back at once — what decides the order?
- [BESPOKE] Insurance, and the other components
  - Insurance transfers residual loss — it covers money, it does not restore service.
  - The other components: the runbook, declaration and escalation, communications, failover of the entry point.
  - A plan is who does what, in what order, and how people are told — not just a strategy name.
  image: none
  notes:
    Workbook tasks 31 and 32. Insurance sits alongside recovery, never instead of it — a refund buys back none of your recovery time.
    The human components are the ones students forget; prompt "who declares the disaster?"
- [EX] Priorities, insurance and components
  - Workbook — tasks 30, 31 and 32.
  - Record the vendor protections leaned on and the recovery priorities, the role insurance plays, and the other components your plan carries.
  timer: ~25 min
  image: none
  notes:
    Activity = practice workbook tasks 30–32.
    Push past the technical parts — escalation, communications and ownership are assessed components too.
- [TAKEAWAYS] Section 2 · The components
  - Build on native protections; sequence by severity.
  - Insurance covers residual loss only.
  - Runbook, escalation, communications, failover — the plan's working parts.
  image: none

### C3 — Detection, steps, and proving the targets
- Teaches: [ICTCLD501 PC 4.2] · [ICTCLD501 PE 3] · [ICTCLD501 KE 5] · [ICTCLD501 KE 6]
- Kicker: detect it, recover it, prove the clock fits
- [BESPOKE] Detection and alerting
  - A plan that starts with "when someone notices" has already spent its recovery time.
  - State what detects each event class — monitoring, alarms, health checks — and who gets told, how.
  - Detection time is inside the recovery clock; the objective includes it.
  image: none
  notes:
    Workbook task 33 — detection as part of the plan, not an assumption. The RTO clock starts at the event, not at the discovery.
    Tie back to the alarm work they'll do in AT2 — same machinery, planning-side view.
- [BESPOKE] The recovery steps
  - Ordered steps with timelines, key features, and the service providers involved.
  - Name who executes each step and what recovered looks like — an owner and a definition of done per step.
  - Recover in priority order; the sequence comes from your ranking, not from habit.
  image: diagram dr-runbook-flow
  notes:
    Workbook task 34 — the runbook. Walk the diagram: detect, declare, recover in priority order, verify.
    No anonymous actions; every step carries a who and a done.
- [BESPOKE] Show the plan meets the objectives
  - Add the step timings up and set the total against the recovery time objective — the arithmetic is the proof.
  - Do the same for data: what the plan can lose against what the objective allows.
  - If the numbers don't fit, the plan changes — re-sequence, parallelise, or step the strategy up.
  image: none
  notes:
    Workbook task 35 — the explicit objectives argument. Listing the right steps is not proof; the addition is.
    This is where a cheap strategy honestly fails and gets stepped up — that revision is good evidence.
- [EX] Detection, steps and the proof
  - Workbook — tasks 33, 34 and 35.
  - State the detection and alerting, write the recovery steps with owners and timings, then show the plan meets the recovery objectives.
  timer: ~35 min
  image: none
  notes:
    Activity = practice workbook tasks 33–35.
    Make them add the timings up — the missing arithmetic is the most common gap in the whole Part B.
- [TAKEAWAYS] Section 3 · The proof
  - Detection time is inside the recovery clock.
  - Every step has an owner, a timing, and a definition of done.
  - The arithmetic against the objectives is the proof.
  image: none

### C4 — Standards, and the assembled plan
- Teaches: [ICTCLD501 PC 4.3] · [ICTCLD501 PE 1] · [ICTCLD501 KE 4]
- Kicker: to a standard, in one document
- [PRIMER] Continuity standards
  - ISO/IEC 27031 — ICT readiness for business continuity; 27001/27002 — the security management context around it.
  - Standards give the plan a recognised structure and assurance language.
  - Reference them so the plan is auditable, not ad hoc.
  image: none
  notes:
    Workbook task 36 — which standards the plan reflects, and why referencing them matters.
    Misconception: you must implement the standard. At this level you reference it to structure and justify the plan.
- [BESPOKE] Assemble the Disaster Recovery Plan
  - Bring the parts into one document: requirements, objectives, risks, strategy, components, steps, proof.
  - Complete, internally consistent, and traceable — any action leads back to the risk and requirement that drove it.
  - Written for the business in plain professional English; this is the deliverable of the whole Part B.
  image: none
  notes:
    Workbook task 37 — assembly. The reader test: someone cold can follow any recovery action back to its risk.
    Everything from Topics 3 and 4 exists to produce this one artefact.
- [EX] The standards, and the assembled plan
  - Workbook — tasks 36 and 37, then the assessment's Part B question Q7 from your own plan.
  - Record the standards the plan reflects, assemble the full Disaster Recovery Plan, then explain the recovery techniques available and why yours fits.
  timer: ~35 min
  image: none
  notes:
    Activity = practice workbook tasks 36–37 + assessment Q7 rehearsed from the assembled plan.
    The practice workbook carries no questions — use the assessment's, answered from the plan just written.
- [TAKEAWAYS] Topic 4 · Key takeaways
  - Recommend the simplest strategy the objectives allow, and show your working.
  - A plan is detection, steps, owners, timings, components — with the arithmetic proving the targets.
  - Reference the continuity standards; assemble one traceable document.
  image: none

### Close
- [BESPOKE] Next: Topic 5 — present for approval
  - The Solution Design and the Disaster Recovery Plan are both complete.
  - Next you take them to the client: the walkthrough, the feedback, the lodgement and the sign-off.
  image: none
  notes:
    Part C is the performance — everything written so far is what gets presented.

## Build notes
~26 slides. Four activities, mapping to practice workbook tasks 28–29 · 30–32 · 33–35 · 36–37 + the
assessment's Part B Q7 (rehearsed from the assembled plan). One generated diagram
(`diagram dr-runbook-flow`, already in `diagrams/`); one decorative `gen` opener hero (cached in
`images/`); one TABLE (strategy trade-offs). Content carried from the 2026-07-01 plan; new teaching:
detection and alerting as its own subject, and the objectives arithmetic as a separate proof step.

## Changelog
- 2026-09-08 — redrafted from the AT1 Part B practice workbook (tasks 28–37 + Q7): detection/alerting
  and the meets-objectives proof taught explicitly; activities point at workbook task numbers.
- 2026-07-01 — authored to full content.
