# Topic 05 Establishing the build team — Slide plan
> **Covers:** Topic 05 — see coverage.md
> **Subtitle:** Agree the objective, set expectations, plan for trouble, allocate the work
> **STATUS: DRAFT — redrafted 2026-09-08 from the AT2 practice workbook, tasks 1–6.**

## Depth ceiling
LEADERSHIP — the set-up half of AT2 on the practice workbook: the team's objective, expectations,
accountability, contingencies, the allocation of the four IaC components, and the agreement on working
beyond the team. Not technical build — the CloudFormation write is the vehicle, not the assessed
content.

**Answer discipline:** activities run as the practice team on the practice engagement; AT2 assesses
the same leadership on the Ledgerline build team. Teach the method; the plans and agreements are the
team's own.

## Teaching source
Bespoke throughout, drawn from BSBXTW401 leadership content applied to the four-component IaC
allocation. In-world team = YAT ICT staff.

## AWS pin table
None — leadership topic; bespoke.

## Slides

### Opener
- [BESPOKE] Leading the build team
  - AT2 begins: the approved design is written as CloudFormation by a team of four, one component each — network, compute, database, storage.
  - Dividing the write is the leadership vehicle: what is marked is how you plan, allocate and lead — not the code.
  - This Topic stands the team up; leading it through the build is Topic 6.
  image: gen flat vector hero illustration of a team leader assigning four workstreams to four team members around a table, blue and gold accents, minimal, no text
  notes:
    Workbook tasks 1 to 6 today — the whole team set-up, in order.
    Misconception: this is a CloudFormation topic. The code is the vehicle; the leadership evidence is what's assessed.

### C1 — The objective, the expectations, the accountability
- Teaches: [BSBXTW401 PC 1.1] · [BSBXTW401 PC 1.2] · [BSBXTW401 PC 1.3] · [BSBXTW401 KE 1] · [BSBXTW401 KE 2]
- Kicker: know the goal, set expectations, hold the line
- [PRIMER] Agree what the team is here to do
  - Name the common objective out loud — everyone should be able to recite it the same way.
  - Break it into responsibilities and required outcomes: what the team must produce, to what standard.
  - Shared, explicit objectives are what let four separate component-writers pull in one direction.
  image: none
  notes:
    Workbook task 1. Unstated objectives drift — making it explicit and shared is the assessable act.
    Test: could every member say the objective the same way?
- [BESPOKE] Set what is expected of each member
  - A performance plan per member: expected outcomes, goals and behaviours for their component — measurable, not a pep talk.
  - Align each plan to the team objective and to the organisation's policies.
  - The shape: an outcome, a standard, a deadline, and a collaboration behaviour.
  image: none
  notes:
    Workbook task 2. If you can't measure whether it was met, it isn't a performance plan.
    Draft one live for the database owner — outcome, standard, deadline, behaviour.
- [BESPOKE] Agree how you hold each other accountable
  - Concrete mechanisms: clear ownership per component, review checkpoints, a shared definition of done.
  - Grounded in organisational requirements — policies, codes of conduct, the organisation's culture — and inside the legislative ones: health and safety, privacy, anti-discrimination.
  - Accountability is preventive structure, not blame after the fact.
  image: none
  notes:
    Workbook task 3. Mechanisms, not slogans — and the grounding in policy and law is examinable.
    Question to pose: one policy and one law that shape how this team holds the line.
- [EX] Stand the team up
  - Workbook — tasks 1, 2 and 3.
  - As the practice team: agree the objective, set what is expected of each member, and agree the accountability mechanisms.
  timer: ~35 min
  image: none
  notes:
    Activity = practice workbook tasks 1–3, done as a team, recorded individually.
    Watch for pep-talk performance plans and slogan accountability — push mechanisms and measures.
- [TAKEAWAYS] Section 1 · The set-up
  - One objective, recitable by all.
  - Measurable expectations per member.
  - Accountability grounded in policy and law.
  image: none

### C2 — Plan for what could go wrong
- Teaches: [BSBXTW401 PC 1.4] · [BSBXTW401 KE 9]
- Kicker: decide the response while calm
- [BESPOKE] The typical contingencies
  - The workplace classics: unplanned absence of a component owner, re-allocation when load shifts, succession for important roles.
  - A contingency is a named trigger plus a pre-agreed response — written into the team plan, decided before it's needed.
  - For this build: the database owner is out the day before the milestone — who picks it up, and how is the handover recorded?
  image: none
  notes:
    Workbook task 4. A risk without a pre-agreed response isn't a contingency; the response is the deliverable.
    The three named classics are the examinable list.
- [EX] Plan the contingencies
  - Workbook — task 4.
  - Write the team's contingencies: the triggers that could hurt the build, and the response agreed for each.
  timer: ~20 min
  image: none
  notes:
    Activity = practice workbook task 4.
    Every row is trigger plus response — challenge any that are just risks listed.
- [TAKEAWAYS] Section 2 · Contingencies
  - Absence, re-allocation, succession — planned before they happen.
  - Trigger plus pre-agreed response, in writing.
  image: none

### C3 — Allocate the work, and agree the outside connections
- Teaches: [BSBXTW401 PC 2.1] · [BSBXTW401 PC 2.2] · [BSBXTW401 PC 2.4] · [BSBXTW401 PE 1] · [BSBXTW401 KE 3] · [BSBXTW401 KE 6] · [BSBXTW401 KE 7]
- Kicker: hand out the boxes, and the seams
- [BESPOKE] Allocate the four components
  - One component per member — network, compute, database, storage — by expertise or by development potential.
  - Each allocation carries instruction: the component's scope, the interfaces it must expose, and any contingencies that attach to it.
  - Allocate the seams, not just the boxes — shared parameters and dependencies are where four components become one build.
  image: diagram component-allocation
  notes:
    Workbook task 5. "Development potential" matters — you can allocate to stretch someone, with the extra instruction that implies.
    The unmanaged interface is where the build breaks; the diagram shows the seams.
- [BESPOKE] Communicate it, and connect beyond the team
  - Communicate the objectives and responsibilities so everyone shares the same picture of done — confirmed by play-back, not just sent.
  - Agree how the team works with people outside it: the internal teams and external specialists worth pulling in, and for what.
  - Facilitation that works for everyone: match the channel to the message, and communicate across cultures and needs.
  image: none
  notes:
    Workbook task 6 — the outside-team agreement is its own task.
    Communication isn't done until it's played back; a decision needs a conversation, a record needs writing.
- [EX] Allocate and agree
  - Workbook — tasks 5 and 6.
  - Allocate the four components with instruction and seams, then agree how the team will work with people outside it.
  timer: ~30 min
  image: none
  notes:
    Activity = practice workbook tasks 5–6, as the practice team.
    Press the seams: what must the network owner expose to the compute owner? And press a concrete outside connection, named, with a reason.
- [TAKEAWAYS] Topic 5 · Key takeaways
  - Objective, expectations, accountability, contingencies — the team plan.
  - Four components allocated with instruction; the seams allocated too.
  - Outside connections agreed before they're needed.
  image: none

### Close
- [BESPOKE] Next: Topic 6 — leading the build
  - The team is stood up: objective agreed, work allocated, trouble planned for.
  - Next the build runs — and you lead it: the meeting, the coaching, the measuring, the reflecting.
  image: none
  notes:
    The team plan comes back throughout Topic 6 — the build is measured against it.

## Build notes
~19 slides. Three activities, mapping to practice workbook tasks 1–3 · 4 · 5–6. One generated diagram
(`diagram component-allocation`, already in `diagrams/`); one decorative `gen` opener hero (cached in
`images/`). Content carried from the 2026-07-02 plan, regrouped to workbook task order; the
facilitation/diversity teaching folds into the allocation section with task 6.

## Changelog
- 2026-09-08 — redrafted from the AT2 practice workbook (tasks 1–6): every section ends in its
  workbook tasks; outside-team agreement taught with its task.
- 2026-07-02 — authored to full content.
