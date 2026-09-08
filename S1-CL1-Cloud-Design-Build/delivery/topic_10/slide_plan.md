# Topic 10 Proving it works, and handing it over — Slide plan
> **Covers:** Topic 10 — see coverage.md
> **STATUS: DRAFT — redrafted 2026-08-28 from the AT2 practice run sheet + the assessment's knowledge
> questions and handover task. Teacher `notes:` not yet authored. `coverage.md` not yet reconciled.
> Deliberately does NOT teach the concepts behind Q2, Q3 and Q6 — those have no worksheet task and are
> left to surface in the gap review.**

## Depth ceiling
Test every path the build depends on, prove the isolation, drive a scale event, then evidence knowledge
in context and file the completed engagement document. This is the last AT2 topic — after it, students
are ready to attempt AT2.

## Teaching source
Bespoke throughout — testing discipline, contextual knowledge answering, and records handling are not
covered by the vendor decks.

## AWS pin table
None.

## Slides

### Opener
- [BESPOKE] Built is not finished
  - Everything on your run sheet is now built. None of it has been shown to work.
  - Today you prove each path, prove the ones that should be blocked are blocked, and make it scale in front of you.
  - Then you answer for what you built, and file it where it belongs.
  - After this topic you are ready to attempt the assessment.
  kicker: now prove it
  image: none

### C1 — Proving the paths
- Teaches: [ICTCLD401 PC 2.6] · [ICTCLD401 PE 3] · [ICTCLD502 PC 4.2]
- Kicker: test, read, fix, retest
- [BESPOKE] What testing is for
  - Building something is not the same as confirming it does what was asked.
  - Nothing erroring during the build proves only that it deployed.
  - Test → observe → compare against what the run sheet asked for → fix → test again.
  - A test you fixed something to pass is better evidence than one that passed first go — say what you changed.
  kicker: no error is not proof
  image: none
- [BESPOKE] Reaching a server with nothing exposed
  - Your servers sit in a private subnet with no public address and no inbound path. You still need to get onto one.
  - A session service connects through the platform rather than over the network, so it needs no key pair and no open port.
  - That is exactly why the tier can stay closed: administrative access does not require a way in.
  kicker: access without exposure
  image: none
- [BESPOKE] The four paths worth proving
  - Onto a server — confirm you are where you think you are.
  - Out to the internet — the outbound path through the NAT gateway works.
  - Across to the database — the application tier can reach the data tier privately, on its port.
  - In from a browser — a user reaches the application through the load balancer's address.
  - Each one exercises a different piece of what you built. A failure tells you which piece.
  kicker: four paths, four different causes
  image: none
- [BESPOKE] Proving what should not work
  - Connectivity is half of it. The other half is showing the database is unreachable from anywhere it should not be reached from.
  - A test that is supposed to fail is evidence when it fails. Capture it.
  - "It works" and "only the right things can reach it" are two separate claims, and both are assessed.
  kicker: a failure can be the evidence
  image: none
- [BESPOKE] Reading a failure
  - A refused connection and a timeout mean different things. Refused means something answered and said no; a timeout means nothing answered at all.
  - Most of what goes wrong here is a rule pointing at the wrong source, or a subnet with no route — not something broken.
  - Read the error before you change anything.
  kicker: refused ≠ timed out
  image: none
- [EX] Run the connectivity tests
  - Run sheet — tests T1 to T4.
  - Work through each path in order, capture what actually happened, and where one fails, fix it, run it again, and record what you changed.
  timer: ~30 min
  image: none
  notes:
    Activity = practice run sheet tests T1–T4. T4 is the one that catches people: the balancer listens
    on plain HTTP, and a browser left to itself will try the secure port and fail. A 503 usually means
    no healthy target yet rather than a fault — have them check the target group and wait.
- [TAKEAWAYS] Section 1 · Proving the paths
  - Building is not confirming; deploying without error proves very little.
  - Prove the paths that should work and the ones that should not.
  - Read the error before changing anything, then retest and record the fix.
  image: none

### C2 — Proving it scales
- Teaches: [ICTCLD401 PC 3.2]
- Kicker: make it happen on purpose
- [BESPOKE] Watching a scaling policy work
  - A policy that has never been triggered is a claim, not a capability.
  - You make it act by moving the target so the current reading is on the wrong side of it, then putting the target back.
  - Scale out is quick. Scale in is deliberately much slower, so the platform does not thrash.
  - Capture both directions — the group adding and the group removing.
  kicker: out is fast, in is slow
  image: none
- [EX] Drive a scale event
  - Run sheet — test T5.
  - Read the current metric, move the policy target to force the group to add a server, watch it, then reverse it and watch the group come back down.
  timer: ~20 min
  image: none
  notes:
    Activity = practice run sheet test T5. Set expectations on timing — scale-in takes several minutes
    and students assume it has failed. Remind them to put the target value back where it started.
- [TAKEAWAYS] Section 2 · Scaling
  - An untriggered policy is a claim.
  - Move the target to force the event, then restore it.
  - Evidence both directions.
  image: none

### C3 — Answering for what you built, and filing it
- Teaches: [ICTCLD401 KE 5] · [ICTCLD401 KE 6] · [ICTCLD401 KE 7] · [ICTCLD401 KE 8] · [ICTCLD401 KE 9] · [ICTCLD401 KE 10] · [ICTCLD401 PC 4.3]
- Kicker: in context, then on file
- [BESPOKE] Knowledge questions are about your build
  - Some of what you know cannot be shown by a screenshot — why a managed service, what the storage types are for, where the security boundary falls, what happens when a name is resolved.
  - The questions ask about your environment. Name your own resources, your own rules, your own decisions.
  - A textbook definition shows recall. Explaining your own build shows understanding, and that is what is being assessed.
  kicker: name your own resources
  image: none
- [BESPOKE] What a full answer looks like
  - Answer the question that was asked, in the terms it was asked in.
  - Where a question asks for a risk or a consequence, ground it in what the system actually holds and who it belongs to — not in "it would be less secure".
  - Where it asks you to compare, name both options.
  - Where the intranet carries the source, use it. An answer in the client's own terms beats a generic one.
  kicker: specific, sourced, complete
  image: none
- [BESPOKE] Filing the completed document
  - An engagement is not finished when the build works. It is finished when the record of it is somewhere the client can find after you have gone.
  - Where that is, is set by the organisation's records policy — not by preference.
  - Name the location, and name the policy that requires it. "I would file it appropriately" evidences nothing.
  kicker: the record outlives you
  image: none
- [EX] Answer the questions and file the run sheet
  - Answer each knowledge question about your own build, then record where the completed run sheet is filed and which policy required that location.
  - Practice note: your practice run sheet carries no questions — use the assessment's, against the system you have just built here.
  timer: ~40 min
  image: none
  notes:
    Activity = the assessment run sheet's Q1–Q6 and the handover task, rehearsed on the practice build.
    The failure mode is textbook definitions — circulate and ask "but in yours?" every time.
    Some questions have no matching teaching yet; see the gap review before delivering this.
- [TAKEAWAYS] Topic 10 · Key takeaways
  - Prove every path, including the ones that must fail.
  - Trigger the scaling policy rather than asserting it works.
  - Answer knowledge questions from your own build, not from definitions.
  - File the record where policy requires, and name the policy.
  image: none

### Close
- [BESPOKE] AT2 from here
  - You can stand up a working, private, monitored, scaling cloud workload to a run sheet and prove it.
  - The assessment is the same shape of work on a different system.
  - After that: making it survive losing a whole availability zone.
  image: none

## Build notes
~15 slides. Three activities, mapping to practice run sheet tests T1–T4 · T5, then the assessment's
Q1–Q6 + handover task.
**Known incompleteness, deliberate:** Q2 (block vs object storage), Q3 (shared responsibility) and Q6
(DNS) have no practice-worksheet task, so no teaching block was written for them. They are expected to
appear in the gap review. `coverage.md` needs reconciling.

## Changelog
- 2026-08-28 — redrafted from the AT2 practice run sheet; the deployment report, appendices and
  reflection are gone (no longer in the instrument), replaced by testing, contextual knowledge and filing.
