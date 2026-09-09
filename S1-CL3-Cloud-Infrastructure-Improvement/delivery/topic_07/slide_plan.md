# Topic 07 Deploying and proving the improvement — Slide plan
> **Covers:** Topic 07 — see coverage.md
> **Subtitle:** Deploy the baseline, apply your approved improvement, then monitor, test and refine
> **STATUS: DRAFT — redrafted 2026-09-08 from the AT3 practice workbook, tasks 1–9.**

## Depth ceiling
BUILD — the hands-on heart of AT3 on the practice workbook: deploy the approved baseline, record the
authorised scope, apply the improvement as a change-set, measure against the metrics, test the four
concerns, and refine. Documentation, strategy and sign-off are Topic 8. Every improvement lands
in-place/additive over the deployed baseline — the lab DB tier is create-only.

**Answer discipline:** activities run on the practice engagement (the website) with the student's own
approved design; AT3 assesses the same work on Ledgerline. Teach the method; the improvements applied
are the student's own.

## Teaching source
AWS ACA CloudFormation deploy / change-sets + CloudWatch monitoring decks pinned at Step 4 (TBD);
bespoke for the apply-as-update discipline, the lab DB-tier constraint, and the test-and-refine loop.

## AWS pin table
TBD — AWS CloudFormation/deploy modules to be pinned.

## Slides

### Opener
- [BESPOKE] From approved design to running system
  - The design is approved and the team's IaC is written; now you individually deploy it, prove it, and refine it.
  - Today's arc: baseline up, scope recorded, improvement applied, measured, tested four ways, refined.
  - Region substitution applies to every deploy: the design names its real regions; you build in us-east-1.
  - teach, demo, practice — watch the deploy and change-set, then run your own.
  image: gen flat vector hero illustration of a cloud engineer applying a change-set to upgrade a running system, before and after states, blue and gold accents, minimal, no text
  notes:
    Workbook tasks 1 to 9 today, in order. Not a fresh build — the baseline first, the improvement over it.
    Say the substitution out loud at every deploy.

### C1 — The baseline up, the scope recorded
- Teaches: [ICTCLD504 PE 4]
- Kicker: a known start, an honest boundary
- [PRIMER] Apply-as-update: the change-set discipline
  - Deploy the approved baseline first, then apply the improvement as a change-set over it — not a fresh, replacing stack.
  - A change-set is a reviewable diff: what will be added or modified, seen before it runs.
  - In-place and additive: no resource replacement, no data migration.
  image: none
  notes:
    The conceptual core of AT3. Review-before-execute is the discipline the whole Topic runs on.
    Question to pose: why baseline-then-change-set instead of deploying the improved stack directly?
- [BESPOKE] The lab constraint: the database is create-only
  - The change-set must not modify the database — the lab role denies rds:ModifyDBInstance.
  - Database-tier DR therefore stays design-level, as designed; the live demonstration lands on the app tier.
  - Nothing is dropped, only relocated — the constraint is honest and it is documented.
  image: diagram change-set-flow
  notes:
    The lab reality, on the diagram: baseline, change-set adds app-tier redundancy and scaling, database untouched.
    Misconception: create-only means DB DR isn't assessed. It's evidenced at design level; the built proof moves tiers.
- [BESPOKE] Record what you are authorised to build
  - Before deploying anything else, write down the approved scope — copied from your design sign-off, not remembered.
  - The scope is the boundary for everything that follows: improvements inside it land; ideas outside it wait.
  - An implementer who can show their authorisation is demonstrating governance, not bureaucracy.
  image: none
  notes:
    Workbook task 2 — new discipline, taught with its task. The sign-off from the design exercise is the source.
    If a test later suggests something outside the scope, it goes to the long-term strategy, not the change-set.
- [DEMO] Deploy the baseline
  - Deploy the approved baseline stack in the lab to CREATE_COMPLETE — region set first, substitution said aloud.
  - Confirm the resources, and capture the evidence as you go.
  source: recorded/live demo
  image: none
  notes:
    Live demonstration, educator-led. Narrate the evidence capture — the screenshots taken now are the record later.
    A pre-deployed spare stack saves the session if the live deploy is slow. ~8–10 min.
- [EX] Baseline and scope
  - Workbook — tasks 1 and 2.
  - Deploy the baseline environment and confirm it serves, then record the scope you are authorised to build from your design sign-off.
  timer: ~30 min
  image: none
  notes:
    Activity = practice workbook tasks 1–2.
    The deploy takes time — have them record the scope while the stack builds.
- [TAKEAWAYS] Section 1 · The start
  - Baseline first; the improvement rides over it.
  - The database tier is create-only; its DR is evidenced in the design.
  - Scope copied from the sign-off, before anything else deploys.
  image: none

### C2 — Apply the approved improvement
- Teaches: [ICTCLD504 PC 3.1] · [ICTCLD504 PE 2]
- Kicker: your design, applied as a reviewable diff
- [BESPOKE] The improvement as a change-set
  - Create the change-set for your approved improvement; read the diff before executing — every line is an add or a modify you intended.
  - The database shows no changes in the diff; anything that would replace a resource is a flag to stop and think.
  - Execute, watch to completion, confirm the improved resources are live.
  image: none
  notes:
    Workbook task 3 — their own approved improvement, applied. The diff review is the assessed habit.
    A REPLACE in the diff means data questions — make them notice before executing, not after.
- [DEMO] Apply a change-set
  - Create a change-set over the deployed baseline, read the diff with the class, execute it, confirm the improvement is live.
  source: recorded/live demo
  image: none
  notes:
    Live demonstration, educator-led. Pause on the diff and read it aloud — additions, modifies, and the untouched database.
    Screenshot the diff and the completed update as the evidence pattern students mirror. ~8 min.
- [EX] Apply your improvement
  - Workbook — task 3.
  - Apply your own approved improvement as a change-set: review the diff, execute, and confirm the improvement is live.
  timer: ~30 min
  image: none
  notes:
    Activity = practice workbook task 3, each student applying their own design.
    Stop anyone executing without reading the diff — the review is the point.
- [TAKEAWAYS] Section 2 · The apply
  - Read the diff; know every line.
  - The database stays untouched; replacements are a stop sign.
  - Confirmed live, with the evidence captured.
  image: none

### C3 — Monitor and measure
- Teaches: [ICTCLD504 PC 3.2] · [ICTCLD504 KE 10]
- Kicker: measured against the metrics you set
- [BESPOKE] Monitoring against the metrics and goals
  - Point the monitoring at the deployed resources and measure against the metrics and goals from your design — the deploy has to prove the improvement, not just exist.
  - Industry-standard tooling: metrics, alarms, dashboards — chosen because each maps to a goal, not to collect everything.
  - Record the baseline reading and the post-improvement reading; the before-and-after pair is the proof.
  image: none
  notes:
    Workbook task 4. The metrics were set back in the design — this is where they come due.
    One reading proves nothing; the comparison does.
- [EX] Monitor and measure
  - Workbook — task 4.
  - Set up the monitoring and measure the deployed architecture against your own metrics and business goals, before and after.
  timer: ~25 min
  image: none
  notes:
    Activity = practice workbook task 4.
    Every metric watched should trace to a goal from their design; challenge orphans.
- [TAKEAWAYS] Section 3 · The measure
  - Metrics mapped to goals, alarms on the thresholds.
  - Before and after — the pair is the evidence.
  image: none

### C4 — Test and demonstrate, four ways
- Teaches: [ICTCLD504 PC 3.3] · [ICTCLD504 PE 2] · [ICTCLD504 KE 7]
- Kicker: prove it, don't assert it
- [BESPOKE] Demonstrating each concern
  - Reliability: fail an app-tier instance and show the service stays available — the single-point-of-failure test is the headline.
  - Security: show the layers hold — the isolation that should block, blocks. Scalability: drive load and show capacity move.
  - Cost: show the improvement's running cost against the goal. Four concerns, four demonstrations — a claim is not a demonstration.
  image: none
  notes:
    Workbook tasks 5 to 8, one concern per task. The SPOF test is the marquee — killing an instance and watching the service hold.
    Because the DB tier is create-only, the reliability demonstration lands on the app tier — restate the constraint where it bites.
- [BESPOKE] Testing and debugging technique
  - The loop: reproduce, isolate, read the logs and metrics, confirm the fix.
  - Every test produces a result you can act on — the findings feed the refinements next.
  - Capture as you test: the screenshot taken during the failure is the one you can't take afterwards.
  image: none
  notes:
    The repeatable method — a debugging loop you can evidence, against random poking.
    The capture-during habit matters most in the SPOF test; the recovering state is the evidence.
- [EX] Test and demonstrate
  - Workbook — tasks 5, 6, 7 and 8.
  - Test and demonstrate reliability, security, scalability and cost optimisation on your deployed system, capturing the evidence as each test runs.
  timer: ~45 min
  image: none
  notes:
    Activity = practice workbook tasks 5–8 — the proving session; budget real time.
    Each test states what was done, what was observed, and what it proves — push all three parts.
- [TAKEAWAYS] Section 4 · The proof
  - Four concerns, four demonstrations.
  - The SPOF test is the reliability headline.
  - Reproduce, isolate, read, confirm — and capture during, not after.
  image: none

### C5 — Short-term refinements
- Teaches: [ICTCLD504 PC 3.4]
- Kicker: act on the results, now
- [BESPOKE] Apply what the tests found
  - Your tests will have found something — a threshold too tight, a missing alarm, a slow health check, capacity set wrong.
  - Short-term means applied now, on the running system, as a small follow-up change; the long-term strategy is next Topic.
  - Re-measure after each refinement — a refinement you don't re-measure isn't finished.
  image: none
  notes:
    Workbook task 9 — the workbook says plainly the tests will have found something; finding nothing means look harder.
    Keep the short/long distinction crisp: applied now versus described for later.
- [EX] Refine and re-measure
  - Workbook — task 9.
  - Apply the short-term refinements your test results call for, and re-measure to confirm each one moved the metric the right way.
  timer: ~25 min
  image: none
  notes:
    Activity = practice workbook task 9.
    Every refinement cites the test result that caused it and the re-measurement that confirmed it.
- [TAKEAWAYS] Topic 7 · Key takeaways
  - Baseline, scope, improvement — in that order, as reviewable diffs.
  - Measured before and after against your own metrics.
  - Four demonstrations, evidence captured during.
  - Refined from the results, and re-measured.
  image: none

### Close
- [BESPOKE] Next: Topic 8 — document, strategise, close
  - Deployed, proven, refined — the improvement runs and the evidence exists.
  - Next: the as-deployed record, the long-term strategy, the handover, and taking it all down.
  image: none

## Build notes
~26 slides. Five activities, mapping to practice workbook tasks 1–2 · 3 · 4 · 5–8 · 9. One generated
diagram (`diagram change-set-flow`, already in `diagrams/`); one decorative `gen` opener hero (cached
in `images/`); two DEMOs (deploy baseline; apply change-set — split from the old single demo to match
the task split). Content carried from the 2026-07-02 plan; new teaching: the approved-scope
discipline (task 2), and the four test tasks taught as four demonstrations.

## Changelog
- 2026-09-08 — redrafted from the AT3 practice workbook (tasks 1–9): scope recording taught with its
  task; testing split into the four concerns; every section ends in its workbook tasks.
- 2026-07-02 — authored to full content.
