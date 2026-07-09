# Topic 05 Documenting & presenting for approval — Slide plan
> **Covers:** Topic 05 — see coverage.md
> **Subtitle:** Assemble and justify the Solution Design, present both deliverables, and get sign-off
> **STATUS: DRAFT** (authored 2026-07-01).

## Depth ceiling
PRODUCE & PRESENT — assemble and justify the Solution Design (Part A) and present the Solution Design + DR Plan to management for approval, obtaining sign-off. No new design and no build — this is the AT1 close-out / design-approval gate.

## Teaching source
Bespoke — technical writing to the YAT templates, and the walkthrough / feedback / lodgement / sign-off discipline; grounded in the scenario.

## AWS pin table
None — bespoke Topic.

## Slides

### Opener
- [BESPOKE] Closing out AT1
  - Topics 1–4 produced the design and the DR plan; Topic 5 turns them into approved deliverables.
  - Two things: document and justify the Solution Design, then present both for approval.
  - Approval is the gate — AT2 implementation only starts once the design is signed off.
  - No new design and no build here — assemble, present, sign off.
  image: gen flat vector hero illustration of a document being presented and stamped approved, blue and gold accents, minimal, no text
  notes:
    Frame Topic 5 as the CLOSE-OUT of AT1 — the design work is done; today it becomes an approved
    deliverable. Set the mode; don't teach documentation technique yet.
    • First bullet: Topics 1–4 produced the web-scale design, the microservice design and the DR plan.
    Today you don't design anything new — you turn that work into finished, signed-off documents.
    • Second bullet: two moves only — DOCUMENT and justify the Solution Design, then PRESENT both
    deliverables for approval. Name them; they're C1 and C2 of today.
    • Third bullet (the gate): approval is a real gate — AT2 implementation does not start until the
    design is signed off. Nothing gets built on an unapproved design.
    • Fourth bullet: no new design, no build here — assemble, present, sign off.
    Misconception to pre-empt: "we're nearly at the build, let's start tweaking the design." No — today
    is producing and presenting the EXISTING design; changing it now reopens work you've already closed.
    Question to pose: "Why would an organisation refuse to let you build before the design is signed off?"
    (accountability + a documented decision to build against — the sign-off is the authority to proceed).
    UoC/AT1 tie: opens the AT1 close-out — ICTCLD503 (document & justify the design) + ICTCLD501 element 5
    (present, lodge, sign off); the output is AT1 Part A documentation + Part C presentation.

### C1 — Documenting & justifying the design
- Teaches: [ICTCLD503 PC 1.7] · [ICTCLD503 PC 2.4]
- Kicker: write it down, and say why
- [PRIMER] Documenting to a template
  - A Solution Design is a professional document, not notes — complete, consistent, and readable by a non-author.
  - Write to the YAT template so structure and quality are predictable.
  - Plain professional English: precise, no jargon for its own sake.
  image: none
  notes:
    A vendor-neutral primer — what it means to write a professional design DOCUMENT, not working notes.
    Keep it short; it sets the standard before the two bespoke slides apply it.
    • First bullet: a Solution Design is a professional document — complete, consistent, and readable by
    someone who wasn't in the room. The test is: could a non-author act on it?
    • Second bullet: writing TO the YAT template makes structure and quality predictable — the reader
    knows where to find each thing, and you can't forget a section.
    • Third bullet: plain professional English — precise, no jargon for its own sake. Clear beats clever.
    Misconception to pre-empt: "the design work is done, so writing it up is just formatting." No — the
    document IS the deliverable the client approves; a strong design described badly fails the same as a
    weak one.
    Question to pose: "If your reader is a manager who wasn't in your design sessions, what must the
    document do that your notes don't?" (stand alone — explain itself without you there).
    UoC/AT1 tie: sets up ICTCLD503 PC 1.7 / PC 2.4 (document & justify) → AT1 Part A quality (criterion A13).
- [BESPOKE] Assemble the Solution Design
  - Bring together the web-scale architecture (Topic 1) and the microservice design (Topic 2) into one document.
  - Each section maps to a requirement — a reader can trace design back to need.
  - Internal consistency: the diagrams, tables and prose agree.
  image: none
  notes:
    Bespoke — the assembly job: two separate design strands become ONE coherent Solution Design.
    • First bullet: bring together the web-scale architecture (Topic 1) and the microservice design
    (Topic 2) into a single document — one artefact the client reads, not two loose pieces.
    • Second bullet: each section maps to a requirement — a reader can trace a design choice back to the
    need that drove it. Traceability is what makes it a design, not a description.
    • Third bullet: internal consistency — the diagrams, tables and prose must AGREE. A diagram that shows
    three tiers and prose that describes two is an instant credibility loss.
    Misconception to pre-empt: "assemble = staple the two designs together." No — you integrate them into
    one narrative with consistent terminology, numbering and diagrams; contradictions between the halves
    are the commonest fault.
    Question to pose: "If a reader picks any design choice in your document, what should they be able to
    find nearby?" (the requirement it satisfies — the trace).
    UoC/AT1 tie: ICTCLD503 PC 2.4 (document the architecture design) → AT1 Part A (criterion A11).
- [BESPOKE] Justify the changes & the design
  - Document and justify the architecture changes (web-scale) and the microservice architecture design.
  - Justification = the requirement met, the option chosen, and why over the alternatives.
  - Unjustified design is an opinion; justified design is defensible under Q&A.
  image: none
  notes:
    Bespoke — the JUSTIFICATION discipline, the heart of C1. Teach that a design without reasons is just
    an assertion.
    • First bullet: document AND justify both the architecture CHANGES (web-scale) and the microservice
    design. Two things get justified, not one.
    • Second bullet: the shape of a justification — the requirement met, the option you chose, and WHY over
    the alternatives. Say all three; a choice with no rejected alternative isn't justified.
    • Third bullet (the line that matters): unjustified design is an opinion; justified design is defensible
    under Q&A — and Q&A is exactly what happens in the walkthrough next.
    Misconception to pre-empt: "justify = describe what I built." No — describing is C1's assembly;
    justifying is arguing why THIS over the options. Students routinely restate the design and call it
    justification.
    Question to pose: "You chose a managed database over self-managed on EC2 — what three things must your
    justification state?" (the requirement, the option chosen, why over the alternative).
    UoC/AT1 tie: ICTCLD503 PC 1.7 (document & justify changes) + PC 2.4 → AT1 Part A criteria A11/A13; the
    justification is what the Part C Q&A tests.
- [EX] Assemble & justify
  - For the practice scenario, assemble the Solution Design in the YAT template.
  - Document and justify the architecture changes and the microservice design.
  timer: ~30 min
  image: none
  notes:
    Facilitation — the C1 practice; students assemble and justify the PRACTICE scenario's Solution Design
    in the YAT template. Mirrors AT1 Part A on a different engagement.
    Tell students, in these words: "For the practice scenario, assemble the Solution Design in the YAT
    template — bring the web-scale and microservice designs into one document — and document and justify
    the architecture changes and the microservice design."
    Steps (put on the board):
    1. Open the YAT Solution Design template and drop the two design strands into their sections.
    2. For each major choice, write the justification: requirement met → option chosen → why over the
    alternatives.
    3. Check internal consistency — diagrams, tables and prose agree; each section traces to a requirement.
    Must produce: an assembled Solution Design (in the template) with each major change/choice justified.
    Timing: ~30 min. Where they get stuck: they DESCRIBE the design instead of JUSTIFYING it — circulate
    and ask "why this over the alternative?" at each choice; also watch for the two strands contradicting.
    Share-back prompt: take one student's justification and ask the room whether it names a rejected option.
    No-leakage note: this is the PRACTICE scenario — AT1 assesses the same assemble-and-justify skill on the
    LMS engagement (comparable, not identical); keep them on the practice design here.

### C2 — Presenting for approval
- Teaches: [ICTCLD501 PC 5.1] · [ICTCLD501 PC 5.2]
- Kicker: walk them through it, and listen
- [PRIMER] The approval walkthrough
  - A walkthrough presents the design + DR plan to the required personnel for a decision.
  - Speak to your choices and their rationale — not every line, the decisions that matter.
  - Approval is a conversation: they will probe, you will respond.
  image: none
  notes:
    A primer on what a design "walkthrough" is — vendor-neutral, before the bespoke how-to.
    • First bullet: a walkthrough presents the design + DR plan to the required personnel for a DECISION —
    its purpose is approval, not information.
    • Second bullet: speak to your CHOICES and their rationale — not every line. Managers approve decisions,
    so present the decisions that matter, not a page-turn.
    • Third bullet: approval is a CONVERSATION — they will probe, you will respond. Expect questions; they
    are the point, not an interruption.
    Misconception to pre-empt: "a walkthrough is reading the document aloud." No — it's a curated pitch of
    the key decisions; reading every line loses the room and hides the decisions under detail.
    Question to pose: "You have 15 minutes with the approvers and a 30-page design — what do you actually
    talk about?" (the decisions and their rationale, not the whole document).
    UoC/AT1 tie: ICTCLD501 PC 5.1 (conduct the walkthrough with required personnel) → AT1 Part C (C1/C6).
- [BESPOKE] Conduct the walkthrough & handle feedback
  - Conduct the verbal walkthrough of the Solution Design and DR Plan with the required personnel.
  - Seek feedback deliberately, and respond to it — accept, adjust, or defend with reasons.
  - Answer contextual Q&A on your own choices — this is where the justification pays off.
  image: none
  notes:
    Bespoke — the two live skills of the walkthrough: presenting your choices and handling feedback in
    real time.
    • First bullet: conduct the VERBAL walkthrough of the Solution Design AND the DR Plan with the required
    personnel — both deliverables, one session.
    • Second bullet: seek feedback DELIBERATELY, then respond to it — accept it, adjust, or defend with
    reasons. All three are valid responses; silence isn't.
    • Third bullet: answer contextual Q&A on your OWN choices — this is where the justification you wrote in
    C1 pays off. If you justified it, you can defend it.
    Misconception to pre-empt: "responding to feedback means agreeing to every change." No — a good
    consultant defends a sound choice with reasons and adjusts where the feedback is right; both are
    professional. Caving to every comment reads as no conviction.
    Question to pose: "An approver says 'why not just use one big server?' — what's your move?" (respond
    with the requirement/justification — defend or adjust, don't freeze).
    UoC/AT1 tie: ICTCLD501 PC 5.1 + PC 5.2 (conduct walkthrough; seek & respond to feedback) → AT1 Part C
    (criteria C1, C2, C5); the Q&A tests the KE behind your choices.
- [EX] Rehearse the walkthrough
  - For the practice scenario, rehearse the walkthrough of the design + DR plan.
  - Seek and respond to feedback; answer Q&A on your choices.
  timer: ~25 min
  image: none
  notes:
    Facilitation — the C2 practice; students rehearse the walkthrough of the practice design + DR plan, in
    pairs (presenter + approver). Mirrors AT1 Part C.
    Tell students, in these words: "For the practice scenario, rehearse the walkthrough of your Solution
    Design and DR plan. Present your key choices, seek feedback, and answer questions on your decisions."
    Run it as pairs (swap roles):
    1. One student presents the design + DR plan to a partner playing the required personnel — decisions,
    not every line, ~5 min.
    2. The "approver" probes: asks why each major choice, offers one piece of feedback.
    3. The presenter responds — accept / adjust / defend with reasons — then swap.
    Must produce: each student has presented their choices aloud and fielded at least two probing questions.
    Timing: ~25 min (both roles). Where they get stuck: they narrate the document line by line instead of
    pitching decisions, and they freeze on pushback — coach them to answer from their C1 justification.
    Share-back prompt: ask one pair to replay the toughest question and how the presenter handled it.
    No-leakage note: practice scenario only — AT1 Part C assesses the same presentation skill on the LMS
    engagement (comparable, not identical).

### C3 — Lodgement & sign-off
- Teaches: [ICTCLD501 PC 5.3] · [ICTCLD501 PC 5.4]
- Kicker: lodge it, get it signed
- [BESPOKE] Lodge & obtain sign-off
  - Lodge the DR plan per the organisational and legislative protocol — the right place, the right record.
  - Obtain final sign-off from the required personnel — the formal acceptance.
  - Sign-off is the gate to AT2: nothing is built until the design is approved.
  image: none
  notes:
    Bespoke — the formal close: lodging per protocol and obtaining sign-off. Teach these as PROCEDURAL
    acts with a paper trail, not a handshake.
    • First bullet: lodge the DR plan per the organisational AND legislative protocol — the right place, the
    right record. Lodgement is where the approved plan is formally stored/registered, not emailed.
    • Second bullet: obtain final SIGN-OFF from the required personnel — the formal acceptance that the
    design is approved.
    • Third bullet (the gate): sign-off is the gate to AT2 — nothing is built until the design is approved.
    Callback to the opener.
    Misconception to pre-empt: "sign-off is just someone saying yes." No — it's a recorded, formal
    acceptance by the required personnel, lodged per protocol; the record is what authorises the build and
    what an auditor looks for.
    Question to pose: "Why does the DR plan have to be lodged 'per organisational and legislative protocol'
    — why not just save it anywhere?" (compliance/retention + it must be findable by the people who'll rely
    on it in a real disaster).
    UoC/AT1 tie: ICTCLD501 PC 5.3 (lodge per protocol) + PC 5.4 (obtain final sign-off) → AT1 Part C
    (criteria C3, C4).
- [EX] Lodgement & sign-off
  - For the practice scenario, lodge the DR plan per protocol.
  - Obtain and record the final sign-off.
  timer: ~15 min
  image: none
  notes:
    Facilitation — the C3 practice; students complete the formal close-out on the practice scenario: lodge
    the DR plan and record the sign-off. Short and procedural.
    Tell students, in these words: "For the practice scenario, lodge the DR plan per protocol, then obtain
    and record the final sign-off."
    Steps (put on the board):
    1. Identify the correct lodgement location/record per the scenario's organisational + legislative
    protocol, and lodge the DR plan there.
    2. Obtain final sign-off from the required personnel (role-play the approver).
    3. RECORD the sign-off — who, what, when — so there's a trail.
    Must produce: the DR plan lodged in the right place + a recorded sign-off entry (approver, date, what
    was approved).
    Timing: ~15 min. Where they get stuck: they treat sign-off as informal ("she said ok") — insist on a
    recorded acceptance; and they're unsure WHERE to lodge — point them at the scenario's protocol.
    Share-back prompt: "What exactly did you record as evidence of sign-off, and who could rely on it later?"
    No-leakage note: practice scenario — AT1 Part C assesses the same lodgement/sign-off on the LMS
    engagement (comparable, not identical).
- [TAKEAWAYS] Topic 5 · Key takeaways
  - Assemble the Solution Design in the YAT template — complete, consistent, professional English.
  - Justify every change and design choice — the requirement, the option, and why.
  - Present the design + DR plan; seek and respond to feedback; answer Q&A on your choices.
  - Lodge per protocol and obtain sign-off — the gate to AT2 implementation.
  image: none

### Close
- [BESPOKE] Next: Topic 6 — AT2 build begins
  - AT1 is closed out: designed, documented, presented, signed off.
  - Next you switch from design to build — implement the web-scale foundation in the lab.
  image: none

## Build notes
~15 slides. Exercises rehearse the close-out on the practice scenario (produce & present; no build). One decorative `gen` image (opener hero).

## Changelog
- 2026-07-01 — authored to full content.
