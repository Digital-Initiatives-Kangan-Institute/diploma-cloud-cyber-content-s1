# Topic 08 Testing, refining and documenting the whole system; final sign-off — Slide plan
> **Covers:** Topic 08 — see coverage.md
> **Subtitle:** Document the as-deployed system against the approved design, describe the long-term strategy, and obtain the final sign-off
> **STATUS: DRAFT** (authored 2026-07-02).

## Depth ceiling
BUILD / FINALISE — the closing AT3 topic. The deploy, monitoring and testing happened in Topic 7; here the deployed-and-tested improvement is written up as-built, the long-term improvement strategy is described, and the final sign-off is obtained. No new build — this closes out AT3 and the cluster.

## Teaching source
Bespoke — as-deployed documentation to the YAT templates, the long-term-improvement narrative, and the final review / sign-off discipline; grounded in the Ledgerline improvement, rehearsed on the website practice vehicle.

## AWS pin table
None — bespoke topic.

## Slides

### Opener
- [BESPOKE] Closing AT3 — document, refine, sign off
  - Topic 7 deployed, monitored and tested the improvement; Topic 8 writes it up and closes the cluster.
  - Three moves: document the as-deployed system against the approved design, describe the long-term improvement strategy, and obtain the final sign-off.
  - The deliverable is the **Deployment Report** — the whole system across all four concerns: security, reliability, scalability, cost.
  - No new build — the report is assembled from what you captured live during the Topic 7 deploy and test.
  image: gen flat vector hero illustration of an engineer finalising a deployment report and obtaining sign-off, checklist and signature, blue and gold accents, minimal, no text
  notes:
    Frame Topic 8 as the CLOSE of AT3 and the cluster — Topic 7 built and tested; Topic 8 writes it up and
    signs it off. No new build.
    • First bullet: Topic 7 deployed, monitored and tested the improvement; Topic 8 writes it up and closes
    the cluster.
    • Second bullet: three moves — document the AS-DEPLOYED system against the approved design, describe
    the LONG-TERM improvement strategy, and obtain the FINAL SIGN-OFF. Those three are C1, C2, C3.
    • Third bullet: the deliverable is the DEPLOYMENT REPORT — the whole system across all four concerns:
    security, reliability, scalability, cost.
    • Fourth bullet: NO new build — the report is assembled from what you captured LIVE during the Topic 7
    deploy and test. That's why live capture mattered.
    Misconception to pre-empt: "documentation is where I finally build the missing bits." No — nothing new
    is built here; if evidence wasn't captured in Topic 7 you can't manufacture it now. The report assembles
    what exists.
    Question to pose: "If you didn't screenshot the SPOF test in Topic 7, can you put it in the report now?"
    (no — capture was live; reinforces why Topic 7 discipline mattered).
    UoC/AT3 tie: opens the AT3 finalisation arc — ICTCLD504 el 4; everything today produces the as-deployed
    report, long-term strategy and sign-off evidenced in AT3.

### C1 — Document as-deployed + test results
- Teaches: [ICTCLD504 PC 4.1] · [ICTCLD504 PE 5]
- Kicker: record what you actually deployed, and prove it works
- [PRIMER] The as-deployed record & the Deployment Report
  - An as-deployed record documents the system as it was actually deployed — not the design on paper, the resources actually running.
  - The Deployment Report assembles it: the as-deployed architecture, the test results, the changes from the approved design, and the deployment/testing steps.
  - It is complete and readable by someone who wasn't in the room — a reviewer can follow it end to end.
  image: none
  notes:
    Open Section 1 — teach what an AS-DEPLOYED record is and what the Deployment Report assembles. PC 4.1
    and PE 5 land across C1.
    • First bullet: an as-deployed record documents the system AS IT WAS ACTUALLY DEPLOYED — not the
    design on paper, the resources actually running. The distinction is the whole idea.
    • Second bullet: the Deployment Report assembles it — the as-deployed architecture, the test results,
    the changes from the approved design, and the deployment/testing steps. Name the four parts.
    • Third bullet: it's COMPLETE and READABLE by someone who wasn't in the room — a reviewer can follow it
    end to end. Write for the absent reader.
    Misconception to pre-empt: "as-deployed = the approved design document." No — the point is documenting
    what ACTUALLY ran (which differs from the design, e.g. DB-tier DR at design level only); copying the
    design defeats it.
    Question to pose: "Name one thing that will differ between the approved design and the as-deployed
    record on this build" (draws out the DB-tier DR / us-east-1 substitution).
    UoC/AT3 tie: ICTCLD504 PC 4.1 + PE 5 → the as-deployed record and step documentation evidenced in AT3.
- [BESPOKE] As-deployed vs the approved design — highlight the changes
  - Document the as-deployed architecture and test results, and **highlight the changes and improvements from the approved design** (PC 4.1).
  - Every difference is named and justified — e.g. the DB-tier DR stayed at design level because the lab couldn't modify the database; the app-tier Multi-AZ was built and evidenced.
  - Test results cover all four concerns — security, reliability, scalability, cost — each against the goals set in Topic 1.
  image: none
  notes:
    The core of C1 — the report must HIGHLIGHT where reality differed from the approved design. PC 4.1
    lands here.
    • First bullet: document the as-deployed architecture and test results, and HIGHLIGHT the changes and
    improvements from the approved design (PC 4.1). Highlighting the deltas is the assessed act.
    • Second bullet: every difference is NAMED and JUSTIFIED — e.g. DB-tier DR stayed at design level
    because the lab couldn't modify the database; app-tier Multi-AZ was built and evidenced. Difference +
    reason, every time.
    • Third bullet: test results cover ALL FOUR concerns — security, reliability, scalability, cost — each
    against the goals set in Topic 1. Close the loop back to the AT1 goals.
    Misconception to pre-empt: "a difference from the design is a failure to hide." No — a named, justified
    difference is good engineering documentation; the unnamed difference is the problem. Surface them.
    Question to pose: "The DB-tier DR is design-level, not deployed — how do you write that up so it reads
    as a justified decision, not a gap?" (rehearses name + justify).
    UoC/AT3 tie: ICTCLD504 PC 4.1 → the as-deployed-vs-design section of the AT3 report.
- [BESPOKE] Document the deployment & testing steps
  - Create the documentation of the deployment and testing steps (PE 5) — the step-by-step record of how the improvement was deployed and tested.
  - Written so a reader could repeat it: the stacks/changes applied, in order, and each test run with its outcome.
  - Assembled from the screenshots, exports and logs you captured as you went in Topic 7 — you can't reconstruct it after the fact.
  image: none
  notes:
    The step-documentation slide — PE 5 lands here. Teach it as a repeatable record.
    • First bullet: create the documentation of the DEPLOYMENT AND TESTING STEPS (PE 5) — the step-by-step
    record of how the improvement was deployed and tested.
    • Second bullet: written so a reader could REPEAT it — the stacks/changes applied, in order, and each
    test run with its outcome. Repeatability is the standard.
    • Third bullet: assembled from the SCREENSHOTS, EXPORTS and LOGS captured as you went in Topic 7 — you
    can't reconstruct it after the fact. Live capture again.
    Misconception to pre-empt: "step documentation is a vague summary." No — the bar is 'a reader could
    repeat it'; a summary that skips the order or the outcomes fails PE 5.
    Question to pose: "Hand your step doc to someone who wasn't here — could they redeploy and re-test from
    it alone? What's missing if not?" (tests the repeatability bar).
    UoC/AT3 tie: ICTCLD504 PE 5 → the deployment/testing-steps documentation evidenced in AT3.
- [TABLE] Deployment Report structure
  | Section | What it contains |
  | As-deployed architecture | The system as actually deployed to us-east-1 — diagrams and resource inventory across all four concerns |
  | Changes from approved design | Where the as-deployed differs from the approved design, and why (e.g. DB-tier DR left at design level) |
  | Test results | The tests run against the deployment and their outcomes — security, reliability, scalability, cost |
  | Deployment & testing steps | The step-by-step record of how it was deployed and tested (PE 5) — repeatable by a reader |
  | Long-term improvement strategy | The next-iteration improvements and their benefits (C2) |
  | Final sign-off record | The approval accepting the deployed system — who, on what, when |
  note: The four concerns run across the as-deployed record and test results; the sign-off record closes the document.
  image: none

### C2 — Long-term improvement strategies
- Teaches: [ICTCLD504 PC 4.2]
- Kicker: what the next iteration would improve, and why
- [BESPOKE] Describe the long-term improvement strategy
  - Describe long-term improvement strategies and their benefits **as applied to the deployed resources** (PC 4.2) — what a next iteration would improve and the benefit it buys.
  - This is where the DB-tier DR lives: built at design level here, it is the headline long-term strategy — cross-Region database resilience and the availability benefit it delivers.
  - Include other future improvements across the four concerns — tighter cost controls, further scalability headroom, security hardening — each tied to a benefit, not a wish-list.
  image: none
  notes:
    Section 2 — LONG-TERM strategy, described (not built). PC 4.2 lands here; contrast with Topic 7's
    short-term refinements.
    • First bullet: describe long-term improvement strategies and their benefits AS APPLIED TO the deployed
    resources (PC 4.2) — what a next iteration would improve and the BENEFIT it buys. Description + benefit,
    tied to the actual deploy.
    • Second bullet (the headline): this is where DB-TIER DR lives — built at design level here, it's the
    headline long-term strategy: cross-Region database resilience and the availability benefit it delivers.
    • Third bullet: include other future improvements across the four concerns — tighter cost controls,
    further scalability headroom, security hardening — each tied to a BENEFIT, not a wish-list.
    Misconception to pre-empt: "long-term strategy is the same as the short-term refinements." No —
    short-term was APPLIED now on the running stack (Topic 7, PC 3.4); long-term is DESCRIBED for a future
    iteration (PC 4.2). Different verb, different topic.
    Question to pose: "DB-tier DR couldn't be deployed in the lab — why does that make it the perfect
    LONG-TERM strategy item, and what benefit do you cite?" (ties the constraint to the long-term narrative).
    UoC/AT3 tie: ICTCLD504 PC 4.2 → the long-term-strategy section of the AT3 report; DB-tier DR is the
    headline item.

### C3 — Final sign-off
- Teaches: [ICTCLD504 PC 4.3]
- Kicker: get the deployed system accepted
- [BESPOKE] Obtain the final sign-off
  - Obtain final sign-off from the required personnel (PC 4.3) — the formal acceptance of the deployed and tested improvement.
  - Walk the Deployment Report: the as-deployed system, the test results against the goals, and the long-term strategy — confirm requirements met for the audience, not in jargon.
  - Record it — who approved, on what, when — as the closing section of the report.
  image: none
  notes:
    Open Section 3 — the FINAL SIGN-OFF, the formal acceptance that closes the cluster. PC 4.3 lands here.
    • First bullet: obtain final sign-off from the REQUIRED PERSONNEL (PC 4.3) — the formal acceptance of
    the deployed and tested improvement.
    • Second bullet: WALK the Deployment Report — the as-deployed system, the test results against the
    goals, and the long-term strategy — confirm requirements met FOR THE AUDIENCE, not in jargon.
    • Third bullet: RECORD it — who approved, on what, when — as the closing section of the report. An
    unrecorded sign-off isn't evidence.
    Misconception to pre-empt: "sign-off is a rubber stamp at the end." No — you have to demonstrate the
    goals were met, in the audience's language; the approver accepts on evidence, not assertion.
    Question to pose: "You're presenting to the YAT sponsor, not an engineer — how do you show 'reliability
    improved' without the jargon?" (draws out audience-appropriate demonstration).
    UoC/AT3 tie: ICTCLD504 PC 4.3 (obtain final sign-off from required personnel) → the sign-off record in
    the AT3 report.
- [BESPOKE] Two approval moments — don't confuse them
  - This is the cluster's **second** approval: the final sign-off at AT3, on the deployed and tested improvement.
  - The **first** was the AT1 deploy sign-off — the approval to proceed to deployment, on the design (Topic 4).
  - The first gate authorised the build; this gate accepts the result and closes the cluster.
  image: none
  notes:
    The clarifier slide — students conflate the cluster's TWO approval moments. Teach the distinction
    explicitly.
    • First bullet: this is the cluster's SECOND approval — the final sign-off at AT3, on the DEPLOYED and
    TESTED improvement.
    • Second bullet: the FIRST was the AT1 deploy sign-off — the approval to PROCEED to deployment, on the
    DESIGN (Topic 4). Different object, different moment.
    • Third bullet: the first gate AUTHORISED the build; this gate ACCEPTS the result and closes the
    cluster. Authorise vs accept — the two verbs.
    Misconception to pre-empt: "there's one sign-off at the end." No — there are two: AT1 approved the
    design to proceed; AT3 accepts the deployed result. Naming which one you're doing is the assessable
    clarity.
    Question to pose: "Which sign-off approved a DESIGN, and which accepts a RUNNING SYSTEM — and what's the
    object of each?" (forces the authorise-vs-accept distinction).
    UoC/AT3 tie: ICTCLD504 PC 4.3 → the final (second) sign-off in AT3; distinct from the AT1 deploy
    sign-off (Topic 4).
- [EX] Write the report section & rehearse the final sign-off
  - For the practice engagement (the website vehicle), write the as-deployed / test-results section of the Deployment Report — highlight the changes from the approved design.
  - Rehearse the final sign-off conversation to a mock panel: walk the report, confirm the goals met, and obtain acceptance.
  - Produce it before finalising the assessed Ledgerline report — this is the practice run.
  timer: ~30 min
  image: none
  notes:
    Facilitation — the Topic 8 practice; students write the as-deployed report section AND rehearse the
    sign-off conversation for the PRACTICE engagement (the website vehicle).
    Tell students, in these words: "For the practice engagement, write the as-deployed / test-results
    section of the Deployment Report — highlight the changes from the approved design. Then rehearse the
    final sign-off conversation to a mock panel: walk the report, confirm the goals met, and obtain
    acceptance."
    Steps (put on the board):
    1. Write the as-deployed architecture + test results section; highlight and justify each change from
    the approved design.
    2. Prepare to present it to a non-technical panel — goals met, in plain language.
    3. Rehearse the sign-off conversation; obtain (mock) acceptance and record who/what/when.
    Must produce: an as-deployed / test-results report section (changes highlighted) plus a rehearsed
    sign-off with a recorded acceptance — the practice run of the AT3 finalisation.
    Timing: ~30 min. Where they get stuck: the report reads as the approved DESIGN rather than what was
    actually deployed — push "what actually ran, and where did it differ?"; and in the sign-off they slip
    into jargon — make them confirm goals for the AUDIENCE.
    Share-back prompt: pick one pair, have them run 60 seconds of the sign-off; ask the room whether the
    goals were shown met in plain language.
    No-leakage note: the website is the PRACTICE vehicle — AT3 assesses the same finalisation on the
    Ledgerline implementation (comparable, not identical); keep them on the practice engagement.
- [TAKEAWAYS] Topic 8 · Key takeaways
  - Document the as-deployed architecture and test results, highlighting the changes and improvements from the approved design.
  - Create the deployment and testing step documentation from your live-captured evidence — repeatable by a reader.
  - Describe the long-term improvement strategy and its benefits — the DB-tier DR and other next-iteration improvements.
  - Obtain and record the final sign-off — the AT3 gate that accepts the deployed system, distinct from the AT1 deploy sign-off.
  image: none

### Close
- [BESPOKE] Cluster complete
  - AT3 is documented, refined and signed off — the deployed improvement is accepted against the approved design.
  - You analysed the baseline (AT1), designed and got the design approved (AT1), led the build (AT2), deployed and tested it (AT3), and closed it with the final sign-off.
  image: none

## Build notes
~11 slides. No new build — documentation, long-term strategy and final sign-off on the Topic 7 deployment. One `[EX]` writes the as-deployed report section and rehearses the final sign-off on the website practice vehicle. One `[TABLE]` gives the Deployment Report structure (as-deployed vs approved design, test results, long-term strategy, sign-off record). One decorative `gen` image (opener hero); no technical diagram. The DB-tier DR (design-level here) is the headline long-term-strategy item.

## Changelog
- 2026-07-02 — authored to full content.
