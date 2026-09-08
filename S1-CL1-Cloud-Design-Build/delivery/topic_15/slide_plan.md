# Topic 15 Proving it, and closing the engagement — Slide plan
> **Covers:** Topic 15 — see coverage.md *(new Topic — `coverage.md` not yet authored)*
> **STATUS: DRAFT — new plan 2026-08-28, from the AT3 practice workbook tests T1–T4, closeout tasks
> 25–26, and the assessment's handover, filing, reflection and knowledge questions. Teacher `notes:`
> not yet authored.**

## Depth ceiling
Prove the design under simulated failure, measure what it cost, close the engagement and take the
environment down. Last topic of the cluster.

## Teaching source
Bespoke throughout — simulation discipline, availability measurement, engagement closure and
decommissioning are not covered by the vendor decks.

## AWS pin table
None.

## Slides

### Opener
- [BESPOKE] Break it on purpose
  - You built the design. It has not survived anything yet, so it is still a claim.
  - Today you confirm it is healthy, break it deliberately, measure what that cost, and then say honestly how it compared to what you predicted.
  - Then you close the engagement properly — and take it all down, which costs money if you get it wrong.
  kicker: a claim becomes a fact
  image: none

### C1 — Confirm before you break
- Teaches: [ICTCLD502 PC 4.2]
- Kicker: a baseline to compare against
- [BESPOKE] A simulation against a broken environment tells you nothing
  - Before you deliberately break anything, confirm what you just built is actually working.
  - Otherwise you cannot tell the difference between the failure you caused and one that was already there — and the whole exercise is worthless.
  kicker: know it is healthy first
  image: none
- [BESPOKE] Prove connectivity, and prove isolation
  - Confirm the service is reachable and that capacity is healthy in both locations.
  - Then confirm the data tier is reachable from the application tier — and not from anywhere else.
  - That second test is meant to fail. Its failure is the evidence, and it should be captured alongside the setting that causes it.
  kicker: both halves are evidence
  image: none
- [EX] Confirm every tier, in both locations
  - Workbook — test T1.
  - Confirm the service loads, capacity is healthy in two locations, the application tier reaches the data tier, and nothing outside can.
  timer: ~20 min
  image: none
  notes:
    Activity = practice workbook test T1. The isolation test runs from their own machine, not from the
    server — an easy thing to get backwards. Its expected result is a timeout.
- [TAKEAWAYS] Section 1 · The baseline
  - Confirm healthy before you break anything.
  - Prove what should work and what should not.
  image: none

### C2 — Simulating failure and resize
- Teaches: [ICTCLD502 PC 4.4] · [ICTCLD502 PC 4.5] · [ICTCLD502 PE 3]
- Kicker: watch the service, not the console
- [BESPOKE] Why anyone deliberately breaks a working system
  - An untested recovery plan is not a plan. It is an assumption with a document attached.
  - Organisations have discovered this expensively: a failover nobody had ever exercised, exercised for the first time during a real outage.
  - You simulate so that the first test is not the real one.
  kicker: the first test should not be the real one
  image: none
- [BESPOKE] Watch the service while it happens
  - The evidence is not the console afterwards. It is what the service did while the failure was happening.
  - Keep the service in front of you, reloading, throughout. Note the time you acted, what the service did, and how long until it was normal again.
  - Run one thing at a time. Two simultaneous failures tell you nothing about which caused what.
  kicker: the browser is the instrument
  image: none
- [BESPOKE] Resizing is a different question
  - A failure simulation asks whether you survive losing something. A resize asks what it costs to grow.
  - Adding capacity alongside what is already serving should cost nothing. Replacing something in place usually costs something.
  - Where you can choose, bringing the replacement up before removing the old one is the behaviour worth demonstrating — and it needs headroom above your current capacity to do it.
  kicker: add alongside, or replace in place
  image: none
- [BESPOKE] Record what actually happened, including a failure
  - If the service did go down, capture that. A recorded outage is evidence, and it is the input to a real comparison against what you predicted.
  - Hiding it costs you twice: the finding, and the credibility of everything you did report.
  kicker: an outage recorded is still evidence
  image: none
- [EX] Run your simulations
  - Workbook — tests T2 and T3.
  - Run the failure simulation and the resize simulation you planned, watching the service throughout, and record the times and what happened.
  timer: ~40 min
  image: none
  notes:
    Activity = practice workbook tests T2–T3. Insist the browser is open and refreshing before they
    act; without it there is no measurement.
    Both simulations take real time — a replacement rollout is slow. Budget for it.
- [TAKEAWAYS] Section 2 · Simulating
  - An untested plan is an assumption.
  - Watch the service, one failure at a time, and record times.
  - Adding capacity should cost nothing; replacing in place usually costs something.
  - Record an outage honestly if you cause one.
  image: none

### C3 — Measuring what it cost
- Teaches: [ICTCLD502 PC 4.3] · [ICTCLD502 PE 5]
- Kicker: read the graph honestly
- [BESPOKE] Reading an availability metric
  - A dip in one location is not downtime. It is the design working — the other location kept serving.
  - Downtime is when everything is at zero at the same moment. Measure those periods, not every dip you can see.
  - A resize done well may show a rise rather than a dip. No dip at all is a result worth recording.
  kicker: one location dipping is success
  image: none
- [BESPOKE] What a graph can and cannot tell you
  - A metric graph shows the shape: what was serving, when, and whether anything went fully dark.
  - It cannot give you an availability percentage honestly — its resolution is far coarser than the outages you are measuring, so a short one simply does not appear.
  - The arithmetic comes from your own timings during the simulations: the seconds you measured, over the length of the window. Keep those timings; they are the calculation.
  kicker: the numbers come from your stopwatch
  image: none
- [EX] Measure availability across the window
  - Workbook — test T4.
  - Graph the healthy capacity across your session, identify any real downtime, and state what it shows and how you measured it.
  timer: ~25 min
  image: none
  notes:
    Activity = practice workbook test T4. Two things to press: reading a single-location dip as success
    rather than failure, and doing the arithmetic from their own recorded timings rather than the graph.
- [TAKEAWAYS] Section 3 · Measuring
  - A dip in one location is the design working.
  - A graph shows shape, not percentages.
  - Your own timings are where the number comes from.
  image: none

### C4 — Closing the engagement
- Teaches: [ICTCLD502 PC 4.6] · [ICTCLD502 PC 5.1] · [ICTCLD502 PC 5.2] · [ICTCLD401 PC 4.3]
- Kicker: predicted, actual, difference
- [BESPOKE] What you predicted, against what happened
  - Put your prediction and the measured result side by side, and explain any difference.
  - A match is a finding: say what it confirms, not just that it matched.
  - A difference is a better finding. "Brief" meant something before you measured it and something more precise afterwards — say what.
  - Surprises are the most useful rows in the table.
  kicker: the difference is the learning
  image: none
- [BESPOKE] "Nothing broke" and "I have evidence it works" are different claims
  - Only one of those is supportable, and it depends on what you actually measured.
  - If a recovery took longer than the target you recorded at the start, that is a gap, and it needs an answer rather than a silence.
  - An alarm that never fired during any of this is worth a question: was there nothing to catch, or is the threshold wrong?
  kicker: which claim can you actually make?
  image: none
- [BESPOKE] Handing over and filing
  - Hand over what the receiving team now runs that they did not before — the new behaviour, the new alarms, what to watch.
  - Then file the completed record where the organisation's policy requires, and name the policy.
  - An engagement ends when the client can operate and audit the system without you, not when the build works.
  kicker: they run it now
  image: none
- [BESPOKE] Taking it down
  - Everything you built keeps costing whether anyone is using it or not.
  - Work backwards: the last thing you made is the first thing removed. That is not just tidiness — each thing depends on something built before it, and the wrong order simply fails.
  - Anything created by hand comes out before the environment that was deployed for you, because the deployment cannot remove things it did not create.
  - Two things reliably outlive everything else: a reserved address that is no longer attached to anything, and an orphaned alarm. The address is the one that keeps billing. Check for both.
  kicker: reverse the order you built in
  image: none
- [EX] Compare, respond, hand over and file
  - Workbook — tasks 25 and 26, then the handover and filing tasks.
  - Set your predictions against what happened and explain the differences; say what you changed as a result, or what evidence makes you confident nothing needed changing; then hand over and file.
  - Finally, take the environment down, working backwards.
  timer: ~40 min
  image: none
  notes:
    Activity = practice workbook closeout tasks 25–26 plus the assessment's handover and filing tasks;
    then the cleanup walk. The practice workbook's cleanup section is the reverse walk — use it.
    Do not let anyone leave without checking for an unattached reserved address.
- [TAKEAWAYS] Section 4 · Closing
  - Predicted against actual, with the difference explained.
  - "Nothing broke" is a weaker claim than "I measured it".
  - Hand over the new behaviour, and file to policy.
  - Decommission backwards, and check what outlives it.
  image: none

### C5 — Answering for it
- Teaches: [ICTCLD502 KE 4] · [ICTCLD502 KE 5] · [ICTCLD502 KE 6] · [ICTCLD502 KE 7] · [ICTCLD502 KE 8] · [ICTCLD502 KE 9]
- Kicker: your design, your evidence
- [BESPOKE] Knowledge questions about your own work
  - The questions ask about availability, fault tolerance, recovery and the trade-offs you made — in your design, with your measurements.
  - "Why this change to the data tier?" is answered by what your failure simulation actually showed, not by a definition.
  - You now have something almost nobody has when answering these: measured numbers from your own environment. Use them.
  kicker: you measured it — cite it
  image: none
- [BESPOKE] Reflecting honestly
  - A reflection is a review, not a summary. "I converted the data tier" is a summary; "converting it first would have saved twenty minutes, and here is how I know" is a reflection.
  - The useful material is what you would do differently, what the time pressure changed, and what you would carry into the next engagement.
  kicker: what would you change?
  image: none
- [EX] Answer the questions and write your reflection
  - Answer each knowledge question from your own design and your own simulation results, then write your reflection.
  - Practice note: your practice workbook carries no questions or reflections — use the assessment's, against the environment you just built and measured here.
  timer: ~35 min
  image: none
  notes:
    Activity = the assessment workbook's Q1–Q6 and reflections R1–R3, rehearsed on the practice build.
    The failure mode is definitions — push every answer back to their own timings and their own design.
- [TAKEAWAYS] Topic 15 · Key takeaways
  - Confirm healthy, then break it deliberately and watch the service.
  - One location dipping is the design working; downtime is everything at zero.
  - Compare what happened to what you predicted and explain the difference.
  - Hand over, file, and decommission backwards.
  image: none

### Close
- [BESPOKE] The cluster is done
  - You advised a client, built what was designed, and then made it survive losing a whole location — designed it, built it, broke it, measured it, and closed it out.
  - The assessment is the same work on a different system.
  image: none

## Build notes
~21 slides. Five activities, mapping to practice workbook tests T1 · T2–T3 · T4, closeout tasks 25–26
plus the assessment handover/filing and cleanup, and the assessment's Q1–Q6 + R1–R3.
**New Topic — `topic_15/coverage.md` does not exist and must be authored**, including the
`**AT3 content Topic**` marker `validate-topic-breakdown` requires. No images yet.

## Changelog
- 2026-08-28 — new plan; carries the simulation, measurement, closure and decommissioning work that
  previously sat compressed across Topics 13 and 14. Availability measurement, honest graph reading and
  decommissioning taught for the first time.
