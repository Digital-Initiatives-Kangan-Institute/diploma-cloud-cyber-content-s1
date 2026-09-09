# Topic 09 Documenting, teardown & sign-off — Slide plan
> **Covers:** Topic 09 — see coverage.md
> **Subtitle:** User documentation, a clean teardown, the sign-off, and the written questions
> **STATUS: DRAFT — redrafted 2026-09-08 from the AT2 practice workbook, tasks 20–22 and the
> assessment's questions Q1–Q3. Renumbered from the old Topic 10.**

## Depth ceiling
CLOSE — the build is done; this Topic documents it for the people who inherit it, removes it cleanly,
walks the client through it for sign-off, and answers the written questions. Last Topic of the cluster.

**Answer discipline:** activities run on the practice build; the assessment closes out a different
build. Teach the method; the documentation and answers are the student's own.

## Teaching source
Bespoke — technical writing, teardown discipline, the sign-off conversation, and the contextual
written questions.

## AWS pin table
None — bespoke Topic.

## Slides

### Opener
- [BESPOKE] Closing out the build
  - The system is built, tested and observable; now it gets documented, taken down, and signed off.
  - Three tasks and three questions today — the professional wrap on the whole build.
  - Everything you captured during the build is the material — a closeout can't be reconstructed from memory.
  image: gen flat vector hero illustration of a technical manual and a signed acceptance document, blue and gold accents, minimal, no text
  notes:
    Workbook tasks 20 to 22, then the written questions Q1 to Q3.
    The capture-as-you-go habit from Topic 7 pays off here; thin evidence now is a habit gap surfacing.

### C1 — User documentation
- Teaches: [ICTCLD505 PC 4.1] · [ICTCLD505 PE 4] · [ICTCLD505 FS Writing]
- Kicker: someone else can run your stacks
- [PRIMER] What IaC user documentation is for
  - User docs let someone who didn't write the template deploy, update and delete it safely.
  - Include the templates and their parameters — what each does and its allowed values.
  - Clear, logical structure — a reader follows it without you in the room.
  image: none
  notes:
    The audience is a future operator, not the author. Undocumented parameters are traps.
    Readable code is not a runbook — the operations need spelling out.
- [BESPOKE] Document operating the stacks
  - How to deploy, update through a change set, and delete each stack, with its parameters.
  - Note where the region is a parameter and what the lab substitution meant.
  - Procedures, not descriptions — numbered steps a stranger can follow under pressure.
  image: none
  notes:
    Workbook task 20. The common miss is describing what the template contains instead of how to operate it.
    Update-via-change-set is the procedure students forget to document.
- [EX] Write the user documentation
  - Workbook — task 20.
  - Write the user documentation for what you built: deploy, update and delete for each stack, parameters included.
  timer: ~30 min
  image: none
  notes:
    Activity = practice workbook task 20.
    The swap test works: could a neighbour deploy the stack from the doc alone?
- [TAKEAWAYS] Section 1 · The docs
  - Written for the operator who inherits it.
  - Deploy, update, delete — as procedures, with the parameters.
  image: none

### C2 — Taking it down cleanly
- Teaches: [ICTCLD505 PC 2.5] · [ICTCLD505 PC 3.6] · [ICTCLD505 PE 1]
- Kicker: nothing left behind, nothing still billing
- [BESPOKE] Remove what you deployed
  - Tear down through the tooling, not by hand — the stack goes down the way it came up.
  - Confirm the removal: a delete that leaves orphans keeps costing and blocks a rebuild.
  - Multiple stacks come down in reverse dependency order — the one nothing depends on goes first.
  image: none
  notes:
    Workbook task 21. Hand-deleting resources a template owns is the closing form of drift.
    Confirming the teardown is the half students skip — check the console after, not just the delete status.
- [EX] Tear it down
  - Workbook — task 21.
  - Remove everything you deployed using the tooling, in the right order, and confirm nothing is left behind.
  timer: ~20 min
  image: none
  notes:
    Activity = practice workbook task 21.
    Ask what order they chose and why — the dependency reasoning is the teaching.
- [TAKEAWAYS] Section 2 · The teardown
  - Through the tooling, in reverse dependency order.
  - Confirmed gone, not assumed gone.
  image: none

### C3 — Confirming the build, and sign-off
- Teaches: [ICTCLD503 PC 4.2] · [ICTCLD503 PC 4.3] · [ICTCLD505 PC 4.2] · [ICTCLD505 FS Oral communication]
- Kicker: walk them through it, get it accepted
- [BESPOKE] Walk the client through the build
  - Walk the client through what you built, how you know it works, and what you're handing over.
  - Plain language for the audience — the person signing may not be technical.
  - Seek feedback and respond: adjust, or defend with reasons. Both are professional.
  image: none
  notes:
    Workbook task 22, first half. The evidence from the build is the material — the tests, the alarm firing, the docs.
    Rehearse saying "the alarm fires on queue depth" without the jargon.
- [BESPOKE] Obtain the sign-off
  - Ask for the decision and record it — the build accepted against the approved design.
  - Sign-off closes the loop that opened in AT1: designed, approved, built, accepted.
  - The recorded decision is the evidence, conditions and all.
  image: none
  notes:
    Task 22, second half — same discipline as the AT1 sign-off in Topic 5; call back to it.
    Approval with conditions is a normal outcome here too.
- [EX] Confirm the build and get sign-off
  - Workbook — task 22.
  - Walk your client through the build in pairs, respond to their feedback, and record the sign-off decision.
  timer: ~25 min
  image: none
  notes:
    Activity = practice workbook task 22, in pairs, both roles.
    The client asks at least one question and gives at least one piece of feedback — the response is the skill.
- [TAKEAWAYS] Section 3 · The close
  - Plain language, evidence in hand.
  - Feedback answered with reasons; the decision recorded.
  image: none

### C4 — The written questions
- Teaches: [ICTCLD505 KE 1] · [ICTCLD505 KE 2] · [ICTCLD503 KE 1] · [ICTCLD503 KE 2] · [ICTCLD505 KE 7] · [ICTCLD503 KE 5] · [ICTCLD505 KE 10] · [ICTCLD505 KE 11]
- Kicker: your build, in your words
- [BESPOKE] The questions ask about your own build
  - Three questions: the standards and standard products your build relies on, how you tested and debugged, and how you'd manage the templates over time.
  - Every answer cites your own work — your template, your tests, your fixes, your change sets.
  - A definition with nothing of your build in it answers nothing.
  image: none
  notes:
    The assessment workbook carries Q1–Q3; the practice workbook carries none — rehearse with the assessment's questions against the practice build.
    "How you tested" is answered from their task 15–16 record; "manage over time" from their parameterisation and updates.
- [EX] Answer the questions
  - The assessment's questions Q1 to Q3, rehearsed from your practice build.
  - Answer each from what you actually did — the standards you relied on, the testing you ran, the way your templates would be managed.
  timer: ~25 min
  image: none
  notes:
    Activity = assessment Q1–Q3 rehearsed on the practice build.
    Push every generic answer back to a concrete artefact of their own.
- [TAKEAWAYS] Topic 9 · Key takeaways
  - Docs for the inheritor; teardown confirmed; sign-off recorded.
  - The written answers cite your own build, every time.
  image: none

### Close
- [BESPOKE] Cluster complete
  - Designed, planned, presented and approved; then built, proven, documented and signed off.
  - The whole engagement, both sides of the table — that is the cluster.
  image: none

## Build notes
~21 slides. Four activities, mapping to practice workbook tasks 20 · 21 · 22 + the assessment's Q1–Q3
(rehearsed on the practice build). One decorative `gen` opener hero (assets live in the old
`topic_10/images/` — move on renumber). Renumbered from the old Topic 10; the Deployment-Report
framing retired (the workbook is the deliverable), teardown teaching arrives from the old Topic 7 with
task 21.

## Changelog
- 2026-09-08 — redrafted from the AT2 practice workbook (tasks 20–22 + Q1–Q3); renumbered 10 → 09;
  teardown taught here with its task; report-assembly framing retired with the workbook conversion.
- 2026-07-01 — authored to full content (as Topic 10).
