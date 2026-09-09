# Topic 04 Drawing, documenting and presenting the design — Slide plan
> **Covers:** Topic 04 — see coverage.md
> **Subtitle:** Draw the improved architecture, document and justify it, present it, and get sign-off to build
> **STATUS: DRAFT — redrafted 2026-09-08 from the AT1 practice workbook, tasks 14–18 and the
> assessment's knowledge questions Q1 and Q3 (Q2 is rehearsed in Topic 2).**

## Depth ceiling
DESIGN → sign-off — close AT1 on the practice workbook: draw the improved architecture, document and
justify the proposal, prepare and run the review presentation, and obtain the sign-off to proceed to
deployment. No build; this gates the AT2/AT3 work.

**Answer discipline:** activities run on the practice engagement (the website); AT1 assesses the same
work on Ledgerline. Teach the method on the practice vehicle; the drawings and documents are the
student's own.

## Teaching source
Bespoke — technical documentation of a proposed architecture and the review / sign-off discipline.

## AWS pin table
None — bespoke topic.

## Slides

### Opener
- [BESPOKE] Closing AT1 — from design to sign-off
  - The design is complete; now it becomes one reviewable proposal: drawn, documented, presented, approved.
  - The cost-benefit reasoning rides inside the proposal — there is no separate business case.
  - This Topic ends with the sign-off that authorises the build.
  image: gen flat vector hero illustration of a presenter showing a cloud architecture proposal to stakeholders for sign-off, blue and gold accents, minimal, no text
  notes:
    Workbook tasks 14 to 18, then the remaining written questions.
    Students expect a standalone business case — say clearly the cost-benefit is a section of the one document.

### C1 — Draw the improved architecture
- Teaches: [ICTCLD504 PE 1]
- Kicker: one picture of the whole design
- [BESPOKE] Draw what you designed
  - One diagram of the whole improved architecture: every tier, every improvement, and where the users come in.
  - Label what each component is for, not just what product it uses — a reader sees the job of every box.
  - The diagram must agree with the design tables that produced it; a mismatch here is what reviewers catch first.
  image: none
  notes:
    Workbook task 14. Any drawing tool is fine; agreement with the design beats prettiness.
    The single-instance database should be visibly single-instance — the diagram states the design honestly, rejection included.
- [EX] Draw the architecture
  - Workbook — task 14.
  - Draw the full improved architecture for the practice engagement, agreeing with every design decision you recorded.
  timer: ~30 min
  image: none
  notes:
    Activity = practice workbook task 14.
    Pair-swap works: if a partner can't read a box's job, it needs a better label.
- [TAKEAWAYS] Section 1 · The drawing
  - Every tier, every improvement, one picture.
  - Labels say the job; the drawing agrees with the tables.
  image: none

### C2 — Document and justify the proposal
- Teaches: [ICTCLD504 PC 2.4]
- Kicker: readable cold, defensible line by line
- [PRIMER] What the proposal document is
  - A professional artefact: the proposed architecture, the rationale, and the trade-offs — readable by a reviewer who wasn't in the room.
  - Diagrams, decision rationale, and the metrics behind each call — all three, not just the pictures.
  - Written for the decider, not the builder.
  image: none
  notes:
    Without rationale and metrics a reviewer can judge what, but not why — and why is what gets approved.
- [TABLE] Proposal structure
  | Section | What it contains |
  | Baseline & gaps | The current architecture and the improvement needs |
  | Proposed architecture | The improved design and its diagram |
  | Decision rationale | Each change: the requirement met, the option chosen, why over alternatives |
  | Cost-benefit | The trade-offs — including what was rejected and why |
  | Sign-off record | The approval to proceed to deployment |
  note: The cost-benefit is a section here, not a separate business case.
  image: none
- [BESPOKE] Document and justify
  - Bring the analysis, the designs and the drawing into one document where the diagrams, tables and prose agree.
  - Each proposed change traces to a named requirement or gap; each rejection carries its argument.
  - Internal consistency is a marked quality — contradictions between diagram and prose are what reviewers catch.
  image: none
  notes:
    Workbook task 15. Assembly means making the parts agree, not stapling them together.
    The classic catch: a diagram showing one thing and prose claiming another — have them self-check for it.
- [EX] Document the proposal
  - Workbook — task 15.
  - Document and justify the proposed architecture for the practice engagement, to the proposal structure.
  timer: ~35 min
  image: none
  notes:
    Activity = practice workbook task 15.
    Press traceability: any change picked at random leads back to a requirement, or it doesn't belong.
- [TAKEAWAYS] Section 2 · The document
  - Architecture, rationale, metrics — readable cold.
  - Every change traces; every rejection argues.
  image: none

### C3 — Present it, and get the sign-off
- Teaches: [ICTCLD504 PC 2.4] · [ICTCLD504 PC 2.5]
- Kicker: walk the decisions, record the approval
- [BESPOKE] Prepare the presentation
  - Plan the order you take the reviewer through the proposal, and for each part the one point they must take away.
  - Anticipate the questions: the choices someone could challenge are the ones to prepare — your justifications already hold the answers.
  - Time it to the slot; running out of time is the most common way this goes wrong.
  image: none
  notes:
    Workbook task 16 — the preparation is its own task, and the one-point-per-part discipline stops a page-turn.
    The cost-benefit rejection is the challenge to expect; the C2 argument is the prepared answer.
- [BESPOKE] Present for review, then ask for the decision
  - Walk the decisions that matter, not every line; defend or adjust under questioning, with reasons.
  - Then ask for the sign-off to proceed to deployment, and record it — who approved, what, when.
  - This is the cluster's first approval: it authorises the build. The second, at the end of the build, accepts the result. Different moment, different question.
  image: none
  notes:
    Workbook tasks 17 and 18. The presentation is observed; responding to challenge is assessed, not just surviving it.
    The two-approvals distinction matters — this one approves a plan; the final one accepts a result.
- [EX] Present and close
  - Workbook — tasks 16, 17 and 18.
  - Prepare the walkthrough, present the proposal to a mock review panel, respond to the feedback, then ask for sign-off and record the decision.
  timer: ~40 min
  image: none
  notes:
    Activity = practice workbook tasks 16–18, in pairs or small groups, roles swapped.
    The panel challenges at least one trade-off; the presenter answers from their own document.
- [TAKEAWAYS] Section 3 · The close
  - One point per part; prepare the questions your choices invite.
  - Defend with reasons; record the decision.
  - First approval authorises the build; the final one accepts the result.
  image: none

### C4 — The written questions
- Teaches: [ICTCLD504 KE 1] · [ICTCLD504 KE 2] · [ICTCLD504 KE 3] · [ICTCLD504 KE 5]
- Kicker: your design, your answers
- [BESPOKE] The questions ask about your own design
  - Two questions remain: the standards and standard products your design relies on, and what cloud adoption changed — with the migration principles that manage the change.
  - Every answer cites your own analysis and design — the review you ran, the options you weighed, the path you chose.
  - A textbook definition with none of your design in it answers nothing.
  image: none
  notes:
    The assessment carries Q1–Q3; Q2 was rehearsed in Topic 2. The practice workbook carries none — rehearse with the assessment's.
    Push each answer back to their own workbook: the standards their review used, the migration path their options assessment weighed.
- [EX] Answer the questions
  - The assessment's questions Q1 and Q3, rehearsed from your practice design.
  - Answer from your own work: the standards and products your build relies on, and what cloud adoption changed for this system.
  timer: ~20 min
  image: none
  notes:
    Activity = assessment Q1 + Q3 rehearsed on the practice design.
    Listen for citations of their own analysis rather than recited definitions.
- [TAKEAWAYS] Topic 4 · Key takeaways
  - Drawn, documented, presented, approved — one proposal, internally consistent.
  - The rejection argued is the strongest section.
  - Approval recorded; the build is authorised.
  - Written answers cite your own design.
  image: none

### Close
- [BESPOKE] Next: Topic 5 — leading the build team
  - AT1 is closed: designed, justified, presented, signed off to proceed.
  - Next you switch from designing to leading — the team that builds the approved design.
  image: none

## Build notes
~21 slides. Four activities, mapping to practice workbook tasks 14 · 15 · 16–18 + the assessment's
Q1 and Q3 (Q2 rehearsed in Topic 2). One decorative `gen` opener hero (cached in `images/`); one
TABLE (proposal structure). Content carried from the 2026-07-02 plan; new teaching: the drawing task,
the preparation task, and the written-question rehearsal.

## Changelog
- 2026-09-08 — redrafted from the AT1 practice workbook (tasks 14–18 + Q1/Q3): drawing and
  preparation taught as their own tasks; question rehearsal added.
- 2026-07-02 — authored to full content.
