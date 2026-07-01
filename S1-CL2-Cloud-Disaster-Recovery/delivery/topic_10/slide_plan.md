# Topic 10 Documenting the build, handover & sign-off — Slide plan
> **Covers:** Topic 10 — see coverage.md
> **Subtitle:** User documentation, the Deployment Report, sign-off, and the written knowledge evidence
> **STATUS: DRAFT** (authored 2026-07-01).

## Depth ceiling
SKILL — the technical build is Topics 6–9; this Topic documents it, hands it over and closes it out. Comes last in AT2, ahead of the Deployment Report submission. No new build.

## Teaching source
Bespoke — technical writing to the YAT templates; the user-doc / report / feedback / sign-off discipline; the written KE appendix on the student's own build.

## AWS pin table
None — bespoke Topic.

## Slides

### Opener
- [BESPOKE] Closing out the build
  - Topics 6–9 built and monitored the system; Topic 10 packages and closes it out.
  - Four things: user documentation, the Deployment Report, sign-off, and the written knowledge evidence.
  - The report is assembled from what you captured live during the build — you can't reconstruct it later.
  - No new build here — document, hand over, sign off.
  image: gen flat vector hero illustration of a technical manual and a signed acceptance document, blue and gold accents, minimal, no text

### C1 — IaC user documentation
- Teaches: [ICTCLD505 PC 4.1] · [ICTCLD505 PE 4] · [ICTCLD505 FS Writing]
- Kicker: someone else can run your stacks
- [PRIMER] User documentation for IaC
  - User docs let someone who didn't write the template deploy, update and delete it safely.
  - Include the templates and the parameters — what each does and its allowed values.
  - Clear, logical structure and the required syntax — a reader follows it without you.
  image: none
- [BESPOKE] Document operating the stacks
  - Document how to deploy, update (change set) and delete each stack, with its parameters.
  - Note the Region substitution: the stacks deploy to us-east-1 in the lab; Region is a parameter.
  - Write to the YAT template — logical order, plain professional English.
  image: none
- [EX] Write the IaC user docs
  - For the practice build, write the user documentation for your stacks — deploy/update/delete with parameters.
  timer: ~25 min
  image: none

### C2 — The Deployment Report & build feedback
- Teaches: [ICTCLD503 PC 4.2]
- Kicker: assemble the evidence, seek feedback
- [BESPOKE] Assemble the Deployment Report
  - Assemble the report: the build narrative, the configuration decisions, and the test/troubleshooting evidence.
  - It is built from the screenshots and exports you captured as you went (Topics 6–9).
  - Confirm, seek and respond to feedback with the required personnel — adjust or defend with reasons.
  image: none
- [EX] Assemble the report & handle feedback
  - For the practice build, assemble a short Deployment Report from your captured evidence.
  - Seek feedback and respond to it.
  timer: ~25 min
  image: none

### C3 — Final sign-off
- Teaches: [ICTCLD503 PC 4.3] · [ICTCLD505 PC 4.2] · [ICTCLD505 FS Oral communication]
- Kicker: get the build accepted
- [BESPOKE] Obtain final sign-off
  - Obtain final sign-off from the required personnel — the build closure and approval to proceed.
  - Articulate the build and confirm requirements for the audience — communicate clearly, not in jargon.
  - Sign-off closes AT2: the build is accepted against the approved design.
  image: none
- [EX] Rehearse the build sign-off
  - For the practice build, rehearse the sign-off conversation — walk the report, confirm requirements met, obtain acceptance.
  timer: ~15 min
  image: none

### C4 — Written knowledge evidence
- Teaches: [ICTCLD505 KE 3] · [ICTCLD505 KE 4] · [ICTCLD505 KE 5] · [ICTCLD505 KE 6] · [ICTCLD505 KE 7] · [ICTCLD505 KE 8] · [ICTCLD505 KE 9] · [ICTCLD503 KE 5] · [ICTCLD503 KE 1] · [ICTCLD505 KE 1] · [ICTCLD503 KE 2] · [ICTCLD505 KE 2]
- Kicker: your build, in your words
- [BESPOKE] Write the KE appendix
  - Contextual written responses on your own build — IaC concepts and benefits, testing/debugging, and the shared cloud foundations.
  - Re-evidences the knowledge from Topics 6–9 against what you actually built (not the generic definitions).
  - Assembled into the report's KE appendix — the last piece of the AT2 submission.
  image: none
- [EX] Write the KE responses
  - For the practice build, write the contextual KE responses on your IaC and microservice work.
  timer: ~20 min
  image: none
- [TAKEAWAYS] Topic 10 · Key takeaways
  - User docs let someone else operate your stacks — templates, parameters, deploy/update/delete.
  - The Deployment Report is assembled from live-captured evidence; seek and respond to feedback.
  - Obtain final sign-off — the build accepted against the approved design.
  - The KE appendix re-evidences Topics 6–9 against your own build.
  image: none

### Close
- [BESPOKE] Cluster complete
  - AT2 is documented, handed over and signed off — the build closes out the cluster.
  - You designed it (AT1), built it (AT2), and can defend every choice.
  image: none

## Build notes
~15 slides. Exercises produce the user docs + Deployment Report + KE on the practice build (documentation skill; no new build). One decorative `gen` image (opener hero). C4 Teaches re-evidences Topics 6–9 KEs (advisory EXTRA vs this Topic's coverage — the KE appendix is a re-evidence step by design).

## Changelog
- 2026-07-01 — authored to full content.
