# Topic 08 Documenting, handover and close — Slide plan
> **Covers:** Topic 08 — see coverage.md
> **Subtitle:** Document the as-deployed system, set the long-term strategy, hand over, and take it down
> **STATUS: DRAFT — redrafted 2026-09-08 from the AT3 practice workbook, tasks 10–13 and the
> assessment's questions Q1–Q2.**

## Depth ceiling
CLOSE — the last Topic of the cluster: document the as-deployed architecture and test results,
describe the long-term strategy, hand over and obtain final sign-off, then remove what was deployed.
No new build; the material is what was captured live in Topic 7.

**Answer discipline:** activities run on the practice engagement; AT3 assesses the same closeout on
Ledgerline. The documentation and answers are the student's own.

## Teaching source
Bespoke — technical documentation, handover and sign-off discipline, teardown, and the contextual
written questions.

## AWS pin table
None — bespoke topic.

## Slides

### Opener
- [BESPOKE] Closing the cluster
  - Deployed, proven, refined — now it gets written up, handed over, signed off, and taken down.
  - The material is what you captured live during the deploy and tests; a closeout can't be reconstructed from memory.
  - Four tasks and two questions, and the cluster is done.
  image: gen flat vector hero illustration of a technical report and a signed acceptance document beside a dismantled cloud stack, blue and gold accents, minimal, no text
  notes:
    Workbook tasks 10 to 13, then the written questions Q1–Q2.
    Thin evidence here is a Topic 7 capture-habit gap surfacing — say so; it's the recurring lesson.

### C1 — Document the as-deployed system
- Teaches: [ICTCLD504 PC 4.1] · [ICTCLD504 PE 5]
- Kicker: the system as it actually runs
- [BESPOKE] As-deployed, against the approved design
  - An as-deployed record documents what is actually running — not the design on paper.
  - Highlight every change from the approved design, named and justified — the DB-tier DR held at design level because the lab is create-only; the app-tier redundancy built and evidenced.
  - Test results across all four concerns, each against the goals set at the start.
  image: none
  notes:
    Workbook task 10, first half. The differences are not failures — a named, justified difference is exactly what the record is for.
- [BESPOKE] Document the steps, repeatably
  - The deployment and testing steps, written so a reader could repeat them: the stacks and changes applied in order, each test and its outcome.
  - Assembled from the screenshots, exports and logs captured as you went.
  - Readable cold by someone who wasn't in the room.
  image: none
  notes:
    Task 10, second half. The repeatability test is the standard: could a stranger re-run the deploy from this record?
- [EX] Write the as-deployed record
  - Workbook — task 10.
  - Document the as-deployed architecture and test results, highlighting the changes from the approved design, with the deployment and testing steps.
  timer: ~35 min
  image: none
  notes:
    Activity = practice workbook task 10.
    Every claimed result points at a captured artefact; gaps get noted honestly, not papered over.
- [TAKEAWAYS] Section 1 · The record
  - What actually runs, differences named and justified.
  - Steps a stranger could repeat, from live-captured evidence.
  image: none

### C2 — The long-term strategy
- Teaches: [ICTCLD504 PC 4.2]
- Kicker: what the next iteration buys
- [BESPOKE] Describe the long-term improvement strategy
  - What a next iteration would improve, and the benefit each item buys — tied to benefits, not a wish-list.
  - The headline lives here: the database-tier DR designed but not lab-buildable — cross-region resilience and the availability it delivers.
  - Ideas the tests surfaced that sat outside your approved scope belong here too — that's what the scope boundary was for.
  image: none
  notes:
    Workbook task 11. The short-term/long-term line drawn in Topic 7 pays off: applied then versus described now.
    The out-of-scope test findings finally get their home.
- [EX] Describe the strategy
  - Workbook — task 11.
  - Describe the long-term improvement strategies for your deployed system and the benefit each delivers.
  timer: ~20 min
  image: none
  notes:
    Activity = practice workbook task 11.
    Each strategy carries a benefit; challenge any that are features without one.
- [TAKEAWAYS] Section 2 · The strategy
  - Next-iteration improvements, each with its benefit.
  - The design-level DR is the headline; out-of-scope findings land here.
  image: none

### C3 — Hand over, sign off, take it down
- Teaches: [ICTCLD504 PC 4.3] · [ICTCLD504 PE 4]
- Kicker: accepted, recorded, removed
- [BESPOKE] The final sign-off
  - Walk the client through the record: the as-deployed system, the results against the goals, the long-term strategy — plain language for the audience.
  - This is the cluster's second approval: it accepts the deployed and tested result. The first approved the design; different moment, different question.
  - Record the decision — who accepted, what, when — conditions and all.
  image: none
  notes:
    Workbook task 12. Call back to the Topic 4 sign-off explicitly — authorise versus accept is the distinction students blur.
    The recorded decision is the evidence, same as every sign-off in the semester.
- [BESPOKE] Remove what you deployed
  - Tear down through the tooling, in reverse dependency order — the stack comes down the way it went up.
  - Confirm the removal; orphans keep billing and block rebuilds.
  - An engagement ends when the environment is gone and the record survives.
  image: none
  notes:
    Workbook task 13. The confirm-after-delete habit from the whole semester closes the loop here.
- [EX] Hand over, sign off, tear down
  - Workbook — tasks 12 and 13.
  - Walk your client through the build in pairs and record the sign-off decision, then remove everything you deployed and confirm nothing remains.
  timer: ~35 min
  image: none
  notes:
    Activity = practice workbook tasks 12–13, sign-off in pairs with roles swapped.
    Nobody leaves with a stack still running — the teardown confirmation is part of the exercise.
- [TAKEAWAYS] Section 3 · The close
  - Plain-language walkthrough, decision recorded.
  - Second approval accepts the result.
  - Removed through the tooling, confirmed gone.
  image: none

### C4 — The written questions
- Teaches: [ICTCLD504 KE 7] · [ICTCLD504 KE 10]
- Kicker: your build, your evidence
- [BESPOKE] The questions ask about your own build
  - Two questions: how you tested this environment and avoid regressions, and what you would monitor to know it stays healthy.
  - Both are answered from your own work — the four demonstrations you ran, the metrics you watched, the refinements you re-measured.
  - A definition with none of your build in it answers nothing.
  image: none
  notes:
    The assessment carries Q1–Q2; the practice workbook carries none — rehearse with the assessment's, from the practice build.
    Their task 5–8 test records and task 4 monitoring are the source material.
- [EX] Answer the questions
  - The assessment's questions Q1 and Q2, rehearsed from your practice build.
  - Answer from what you actually did: the testing and the monitoring, cited from your own records.
  timer: ~20 min
  image: none
  notes:
    Activity = assessment Q1–Q2 rehearsed.
    Push every answer back to a test they ran or a metric they watched.
- [TAKEAWAYS] Topic 8 · Key takeaways
  - The record shows what runs, what changed, and how to repeat it.
  - Strategy with benefits; sign-off recorded; environment removed.
  - Written answers cite your own testing and monitoring.
  image: none

### Close
- [BESPOKE] The cluster is done
  - You analysed a system, designed and justified its improvement, led the team that built it, then deployed, proved, documented and closed it — end to end.
  - The assessment is the same work on a different system.
  image: none

## Build notes
~21 slides. Four activities, mapping to practice workbook tasks 10 · 11 · 12–13 + the assessment's
Q1–Q2 (rehearsed on the practice build). One decorative `gen` opener hero (new prompt — the old hero
lacked the teardown; regenerate). Content carried from the 2026-07-02 plan; new teaching: the
teardown task and the written-question rehearsal. The old Deployment Report TABLE retired — the
workbook is the deliverable.

## Changelog
- 2026-09-08 — redrafted from the AT3 practice workbook (tasks 10–13 + Q1–Q2): teardown taught with
  its task; report framing aligned to the workbook deliverable; question rehearsal added.
- 2026-07-02 — authored to full content.
