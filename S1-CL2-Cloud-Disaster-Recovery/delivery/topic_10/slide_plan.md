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
  notes:
    Frame Topic 10 as the closeout — the technical work is done (Topics 6–9); today packages, hands over
    and signs off. Set the four deliverables; no new build.
    • First bullet: Topics 6–9 built and monitored the system; Topic 10 PACKAGES and closes it out. The
    engineering is behind them; this is the professional wrap.
    • Second bullet: four things — user documentation, the Deployment Report, sign-off, and the written
    knowledge evidence. Preview them as today's map.
    • Third bullet (the recurring truth): the report is assembled from what they captured LIVE during the
    build — you can't reconstruct it later. If evidence is thin, that's a Topics 6–9 habit gap surfacing now.
    • Fourth bullet: no new build here — document, hand over, sign off. Reset expectations from console
    work to writing + communication.
    Misconception to pre-empt: "documentation is the easy bit." No — the report and user docs are assessed
    on quality (D13) and are what a client actually receives; a great build with a poor handover fails the
    professional test.
    Question to pose: "Your build works perfectly but you kept no screenshots — can you write the
    Deployment Report?" (no — it's assembled from live-captured evidence; drives home the Topics 6–9 discipline).
    UoC/AT2 tie: opens the closeout — ICTCLD505 documentation + ICTCLD503 feedback/sign-off — evidenced in
    AT2 §7–8 (D10–D13).

### C1 — IaC user documentation
- Teaches: [ICTCLD505 PC 4.1] · [ICTCLD505 PE 4] · [ICTCLD505 FS Writing]
- Kicker: someone else can run your stacks
- [PRIMER] User documentation for IaC
  - User docs let someone who didn't write the template deploy, update and delete it safely.
  - Include the templates and the parameters — what each does and its allowed values.
  - Clear, logical structure and the required syntax — a reader follows it without you.
  image: none
  notes:
    A primer on what USER documentation for IaC is for — someone who didn't write the template must be
    able to run it. Frame the reader, then the content.
    • First bullet: user docs let someone who did NOT write the template deploy, update and delete it
    safely. The audience is a future operator, not the author.
    • Second bullet: include the templates AND the parameters — what each parameter does and its allowed
    values. Parameters are the knobs; undocumented knobs are traps.
    • Third bullet (FS Writing): clear, logical structure and the required syntax — a reader follows it
    without you in the room. Structure is assessed, not just content.
    Misconception to pre-empt: "the template is self-documenting." No — a stranger under time pressure needs
    the deploy/update/delete steps and the parameter meanings spelled out; readable code isn't a runbook.
    Question to pose: "You hand your stack to YAT's ICT team and leave — what must the doc let them do
    without ringing you?" (deploy, update via change set, delete — safely, with the right parameters).
    UoC/AT2 tie: ICTCLD505 PC 4.1 + PE 4 (create user documentation incl. templates) + FS Writing → AT2
    §7.1 (D10).
- [BESPOKE] Document operating the stacks
  - Document how to deploy, update (change set) and delete each stack, with its parameters.
  - Note the Region substitution: the stacks deploy to us-east-1 in the lab; Region is a parameter.
  - Write to the YAT template — logical order, plain professional English.
  image: none
  notes:
    Make the primer concrete for THEIR stacks — the operating procedures a handover doc must carry.
    • First bullet: document how to DEPLOY, UPDATE (via change set) and DELETE each stack, with its
    parameters. Three operations, each with steps — the change-set path for updates especially.
    • Second bullet: note the Region substitution — the stacks deploy to us-east-1 in the lab, and Region
    is a PARAMETER, so the doc says how to point it elsewhere. Don't bury the substitution.
    • Third bullet: write to the YAT template — logical order, plain professional English. The house style
    is part of the mark (D13).
    Misconception to pre-empt: "update means delete and redeploy." No — teach the CHANGE SET path for
    updates (preview then apply); tearing down to change a parameter loses data and isn't the professional move.
    Question to pose: "What's the safe way to change a running stack's parameter — and how do you know what
    the change will do before it happens?" (a change set — preview, then execute).
    UoC/AT2 tie: ICTCLD505 PC 4.1 + PE 4 + FS Writing → AT2 §7.1 (D10); deploy/update/delete with
    parameters is exactly the user-doc content assessed.
- [EX] Write the IaC user docs
  - For the practice build, write the user documentation for your stacks — deploy/update/delete with parameters.
  timer: ~25 min
  image: none
  notes:
    Facilitation — the C1 practice; students write the user documentation for their practice stacks.
    Tell students, in these words: "For your practice build, write the user documentation for your stacks
    — how to deploy, update and delete each one, with its parameters, in the YAT template."
    Steps (put on the board):
    1. List each stack and its parameters (name, what it does, allowed values).
    2. Write the deploy, update (change set) and delete procedure for each — steps a stranger can follow.
    3. Note the Region substitution (Region is a parameter; deploys to us-east-1 in the lab).
    4. Put it in logical order in the YAT template, plain professional English.
    Must produce: user documentation covering deploy/update/delete with parameters for their stacks —
    the §7.1 deliverable.
    Timing: ~25 min. Where they get stuck: they describe WHAT the template contains instead of HOW to
    operate it — push them to write procedures (numbered steps), and to cover update-via-change-set, not
    just deploy.
    Share-back prompt: swap docs with a neighbour — "could you deploy this stack from their doc alone?"
    No-leakage note: the practice build is comparable-not-identical to the AT2 build; keep them documenting
    the practice stacks here.

### C2 — The Deployment Report & build feedback
- Teaches: [ICTCLD503 PC 4.2]
- Kicker: assemble the evidence, seek feedback
- [BESPOKE] Assemble the Deployment Report
  - Assemble the report: the build narrative, the configuration decisions, and the test/troubleshooting evidence.
  - It is built from the screenshots and exports you captured as you went (Topics 6–9).
  - Confirm, seek and respond to feedback with the required personnel — adjust or defend with reasons.
  image: none
  notes:
    Teach the Deployment Report as an ASSEMBLY of evidence they already have, plus the feedback loop.
    • First bullet: assemble the report — the build narrative, the configuration decisions, and the
    test/troubleshooting evidence. Three strands they generated across Topics 6–9.
    • Second bullet (the recurring truth): it is BUILT from the screenshots and exports captured as they
    went. Assembly is only easy if the capturing was done; surface any gaps now.
    • Third bullet: confirm, seek and RESPOND to feedback with the required personnel — adjust the report,
    or defend a choice WITH REASONS. Feedback is a two-way professional exchange, not just corrections.
    Misconception to pre-empt: "feedback means do whatever I'm told." No — you either incorporate it or
    justify your decision with reasons; a defensible "no, because…" is a valid professional response (PC 4.2).
    Question to pose: "A reviewer says your alarm threshold is too high — what are your two legitimate
    responses?" (adjust it, OR defend it by tracing to the design spec — both are 'responding to feedback').
    UoC/AT2 tie: ICTCLD503 PC 4.2 (confirm/seek/respond to feedback) → AT2 §7.5–7.6 (D11); the report
    assembly also feeds document quality (D13).
- [EX] Assemble the report & handle feedback
  - For the practice build, assemble a short Deployment Report from your captured evidence.
  - Seek feedback and respond to it.
  timer: ~25 min
  image: none
  notes:
    Facilitation — the C2 practice; students assemble a short Deployment Report and run a feedback round.
    Tell students, in these words: "For your practice build, assemble a short Deployment Report from the
    evidence you captured — the build narrative, your configuration decisions, and your
    test/troubleshooting evidence. Then seek feedback on it and respond."
    Steps (put on the board):
    1. Pull your captured screenshots and exports from Topics 6–9 into the report structure.
    2. Write the build narrative + the configuration decisions; attach the test/troubleshooting evidence.
    3. Swap with a peer (or ask the assessor-in-role) for feedback.
    4. Respond: incorporate it, or defend a choice with reasons — and note what you did.
    Must produce: a short assembled Deployment Report plus a recorded feedback exchange (what was raised,
    how you responded) — the §7.5–7.6 evidence.
    Timing: ~25 min. Where they get stuck: thin evidence (nothing captured earlier) — have them note the
    gap rather than fabricate; and treating all feedback as mandatory changes — remind them defending with
    reasons is valid.
    Share-back prompt: "Name one piece of feedback you REJECTED and the reason you gave." (models
    responding, not just complying).
    No-leakage note: the practice build is comparable-not-identical to the AT2 build; keep them on the
    practice report here.

### C3 — Final sign-off
- Teaches: [ICTCLD503 PC 4.3] · [ICTCLD505 PC 4.2] · [ICTCLD505 FS Oral communication]
- Kicker: get the build accepted
- [BESPOKE] Obtain final sign-off
  - Obtain final sign-off from the required personnel — the build closure and approval to proceed.
  - Articulate the build and confirm requirements for the audience — communicate clearly, not in jargon.
  - Sign-off closes AT2: the build is accepted against the approved design.
  image: none
  notes:
    Teach sign-off as the professional close — getting the build formally accepted against the approved
    design, communicated clearly.
    • First bullet: obtain final sign-off from the required personnel — the build closure and approval to
    proceed. Sign-off is a decision by someone with authority, not a self-declaration.
    • Second bullet (FS Oral): articulate the build and confirm requirements FOR THE AUDIENCE — plain
    language, not jargon. The person signing may not be technical; meet them where they are.
    • Third bullet (the point): sign-off closes AT2 — the build is accepted against the APPROVED DESIGN.
    Tie it back to AT1: you're being accepted against the thing you designed and got approved.
    Misconception to pre-empt: "sign-off is a formality once it works." No — it's where you CONFIRM every
    requirement is met, in the client's language; a working build the client doesn't understand or accept
    isn't signed off.
    Question to pose: "You're walking a non-technical manager through the build for sign-off — how do you
    say 'the alarm fires on queue depth' without the jargon?" (rehearses audience-appropriate articulation).
    UoC/AT2 tie: ICTCLD503 PC 4.3 + ICTCLD505 PC 4.2 (obtain final sign-off) + FS Oral communication → AT2
    §7.5–7.6 (D11).
- [EX] Rehearse the build sign-off
  - For the practice build, rehearse the sign-off conversation — walk the report, confirm requirements met, obtain acceptance.
  timer: ~15 min
  image: none
  notes:
    Facilitation — the C3 practice; students REHEARSE the sign-off conversation (oral-communication
    practice, not a document).
    Tell students, in these words: "For your practice build, rehearse the sign-off conversation — walk your
    report, confirm each requirement is met, and obtain acceptance — in plain language for a non-technical
    audience."
    Steps (pair them up):
    1. Pair up — one is the consultant, one is the client/required-personnel signing off (then swap).
    2. Walk the report: what was built, how it meets each requirement, briefly and jargon-free.
    3. Confirm requirements met; the 'client' asks a question or two; obtain acceptance.
    Must produce: a rehearsed sign-off walkthrough where the 'client' can restate what they're accepting —
    practice for the §7.6 sign-off.
    Timing: ~15 min (short — it's a rehearsal). Where they get stuck: slipping into jargon — the 'client'
    should stop them and ask "in plain words?"; and skipping the requirement-by-requirement confirmation.
    Share-back prompt: ask one pair to demo 60 seconds — the room judges whether a non-technical client
    would understand.
    No-leakage note: the practice build is comparable-not-identical to the AT2 build; keep the rehearsal on
    the practice build here.

### C4 — Written knowledge evidence
- Teaches: [ICTCLD505 KE 3] · [ICTCLD505 KE 4] · [ICTCLD505 KE 5] · [ICTCLD505 KE 6] · [ICTCLD505 KE 7] · [ICTCLD505 KE 8] · [ICTCLD505 KE 9] · [ICTCLD503 KE 5] · [ICTCLD503 KE 1] · [ICTCLD505 KE 1] · [ICTCLD503 KE 2] · [ICTCLD505 KE 2]
- Kicker: your build, in your words
- [BESPOKE] Write the KE appendix
  - Contextual written responses on your own build — IaC concepts and benefits, testing/debugging, and the shared cloud foundations.
  - Re-evidences the knowledge from Topics 6–9 against what you actually built (not the generic definitions).
  - Assembled into the report's KE appendix — the last piece of the AT2 submission.
  image: none
  notes:
    Teach the KE appendix as re-evidencing knowledge CONTEXTUALLY — against their own build, not as
    textbook definitions. This is the last piece of the submission.
    • First bullet: contextual written responses on THEIR OWN build — IaC concepts and benefits,
    testing/debugging, and the shared cloud foundations. The prompts ask "on your build," not "define X."
    • Second bullet (the shift): re-evidences the knowledge from Topics 6–9 against what they ACTUALLY
    built — a generic definition scores less than one grounded in their template, their tests, their fixes.
    • Third bullet: assembled into the report's KE APPENDIX — the final component of the AT2 submission.
    Misconception to pre-empt: "I'll paste the definitions from the notes." No — the KE responses are
    marked as CONTEXTUAL (D12); "here's how least-privilege showed up in MY build" beats a dictionary entry.
    Question to pose: "The KE asks about testing techniques — do you answer with the textbook, or with how
    you tested YOUR microservice?" (your build — contextual is the whole point).
    UoC/AT2 tie: ICTCLD505 KE 3–9 + ICTCLD503 KE 5 + the shared foundations (ICTCLD503 KE 1,2 / ICTCLD505
    KE 1,2), re-evidenced against the build → AT2 §8 (D12). This slide deliberately re-evidences the
    Topics 6–9 KEs — the advisory EXTRA is by design.
- [EX] Write the KE responses
  - For the practice build, write the contextual KE responses on your IaC and microservice work.
  timer: ~20 min
  image: none
  notes:
    Facilitation — the C4 practice; students write contextual KE responses on their practice IaC +
    microservice work.
    Tell students, in these words: "For your practice build, write the contextual knowledge-evidence
    responses on your IaC and microservice work — answer each against what YOU built, not a textbook
    definition."
    Steps (put on the board):
    1. Take each KE prompt (IaC concepts/benefits, testing/debugging, the shared foundations).
    2. Answer it CONTEXTUALLY — cite your own template, your own tests, your own fixes from Topics 6–9.
    3. Assemble the responses into the KE appendix of the report.
    Must produce: a set of contextual KE responses grounded in the practice build — the §8 appendix.
    Timing: ~20 min. Where they get stuck: writing generic definitions — push them to name a concrete
    thing from their build in every answer; and thin answers where their build evidence was thin (a Topics
    6–9 gap surfacing).
    Share-back prompt: take one KE and compare a generic answer with a build-grounded one — the room sees
    the difference contextual makes.
    No-leakage note: the practice build is comparable-not-identical to the AT2 build; keep the KE responses
    on the practice build here.
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
