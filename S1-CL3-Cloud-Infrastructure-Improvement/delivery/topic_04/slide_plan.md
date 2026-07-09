# Topic 04 Documenting and presenting the Solution Design — Slide plan
> **Covers:** Topic 04 — see coverage.md
> **Subtitle:** Assemble the whole Solution Design, present it for review, and obtain sign-off to proceed
> **STATUS: DRAFT** (authored 2026-07-02).

## Depth ceiling
DESIGN → sign-off — assemble the four design concerns (Topics 2–3) plus the baseline analysis (Topic 1) into one reviewable Solution Design, present it to the required personnel, and obtain the sign-off to proceed to deployment. No build — this Topic closes the AT1 design phase and gates the AT2/AT3 work.

## Teaching source
Bespoke — technical documentation of a proposed architecture and the review / sign-off discipline; grounded in the Ledgerline improvement scenario, rehearsed on the website practice vehicle.

## AWS pin table
None — bespoke topic.

## Slides

### Opener
- [BESPOKE] Closing AT1 — from design to sign-off
  - Topics 1–3 produced the design; Topic 4 turns it into one reviewable Solution Design and gets it approved.
  - Two moves: document and present the proposed architecture, then obtain the sign-off to proceed to deployment.
  - The cost-benefit reasoning rides inside the Solution Design — there is no separate business case.
  - Design only — this is the AT1 deliverable and its approval gate; the build is AT2/AT3.
  image: gen flat vector hero illustration of a presenter showing a cloud architecture proposal to stakeholders for sign-off, blue and gold accents, minimal, no text
  notes:
    Frame the CLOSE of AT1 — Topics 1–3 produced the design; Topic 4 turns it into one reviewable Solution
    Design and gets it approved. Two moves: document/present, then obtain sign-off.
    • First two bullets: Topics 1–3 produced the design; today you assemble it into one reviewable Solution
    Design and get it approved — document and present, then obtain the sign-off to proceed to deployment.
    • Third bullet: the cost-benefit reasoning rides INSIDE the Solution Design — there is no separate
    business case. Say this clearly; students expect a standalone business case.
    • Fourth bullet (the discipline): design only — this is the AT1 deliverable and its approval gate; the
    build is AT2/AT3.
    Misconception to pre-empt: "we write a separate business case for the cost-benefit." No — in this cluster
    the cost-benefit is a SECTION of the Solution Design; one document carries the design, the rationale and
    the trade-offs.
    Question to pose: "Where does the no-Multi-AZ-database argument live in the deliverable?" (inside the
    Solution Design's cost-benefit section — not a separate document).
    UoC/AT1 tie: this Topic develops ICTCLD504 PC 2.4 (document & present) and PC 2.5 (obtain sign-off); the
    output is the assembled AT1 Solution Design + the observed presentation and sign-off record.

### C1 — Documenting & presenting
- Teaches: [ICTCLD504 PC 2.4]
- Kicker: assemble it, then walk them through it
- [PRIMER] What a Solution Design document is
  - A Solution Design is a professional artefact: the proposed architecture, the rationale, and the trade-offs — complete and readable by a reviewer who wasn't in the room.
  - It documents the improved architecture with clear diagrams, decision rationale, and the metrics behind each call.
  - Pitched for a review audience: the required personnel who decide whether to proceed.
  image: none
  notes:
    Open Section 1 — what a Solution Design document IS: a professional artefact a reviewer who wasn't in
    the room can read and decide on. Teach the standard before they assemble theirs.
    • First bullet: a Solution Design is a professional artefact — the proposed architecture, the rationale,
    and the trade-offs — complete and readable by a reviewer who wasn't in the room.
    • Second bullet: it documents the improved architecture with clear DIAGRAMS, decision RATIONALE, and the
    METRICS behind each call. Three things, not just diagrams.
    • Third bullet: it's pitched for a REVIEW audience — the required personnel who decide whether to
    proceed. Write for the decider, not the builder.
    Misconception to pre-empt: "a diagram is the design." No — the diagram is one part; without the rationale
    and the metrics a reviewer can't judge WHY, only WHAT. All three are marked.
    Question to pose: "A reviewer who wasn't in your design sessions opens the document — what must be there
    for them to approve it?" (architecture + rationale + metrics/trade-offs, readable cold).
    UoC/AT1 tie: ICTCLD504 PC 2.4 (document & present proposed architecture for review) → the AT1 Solution
    Design document.
- [BESPOKE] Assemble the whole design
  - Bring together the baseline analysis (Topic 1) and the four design concerns — reliability and scalability (Topics 2–3) — into one document.
  - Each proposed change traces back to a named requirement or gap; the diagrams, tables and prose agree.
  - Fold in the cost-benefit reasoning: what each change costs and the improvement it buys.
  image: none
  notes:
    The assembly slide — bring Topics 1–3 together into one coherent document where every part agrees. This
    is where scattered design work becomes a single deliverable.
    • First bullet: bring together the baseline analysis (Topic 1) and the four design concerns —
    reliability and scalability (Topics 2–3) — into ONE document.
    • Second bullet: each proposed change traces back to a named requirement or gap; the diagrams, tables and
    prose AGREE. Consistency is a marked quality.
    • Third bullet: fold in the cost-benefit reasoning — what each change costs and the improvement it buys
    (including the no-Multi-AZ-database call).
    Misconception to pre-empt: "assemble = staple the topic outputs together." No — assembly means making
    them agree and traceable; contradictions between the diagram and the prose are exactly what a reviewer
    catches.
    Question to pose: "Your reliability diagram shows a single-AZ DB but your prose says 'highly available
    database' — what's wrong, and which is right?" (they must agree; the design is single-AZ DB by the
    cost-benefit call).
    UoC/AT1 tie: ICTCLD504 PC 2.4 → the assembled AT1 Solution Design document.
- [TABLE] Solution Design document structure
  | Section | What it contains |
  | Baseline & gaps | Current Ledgerline architecture and the improvement needs (Topic 1) |
  | Proposed architecture | The improved design + diagrams (reliability + scalability, Topics 2–3) |
  | Decision rationale | Each change: the requirement met, the option chosen, why over alternatives |
  | Cost-benefit | The trade-offs — including why the database is not Multi-AZ |
  | Sign-off record | The approval to proceed to deployment |
  note: The cost-benefit is a section here, not a separate business case; the sign-off record closes the document.
  image: none
- [BESPOKE] Present it for review
  - Present the proposed architecture to the required personnel for review — walk the decisions that matter, not every line.
  - Be ready to defend the reliability cost-benefit call: why the database stays single-AZ rather than Multi-AZ.
  - Seek feedback and respond — accept, adjust, or defend with reasons; this is an observed individual oral in AT1 Part B.
  image: none
  notes:
    Teach the PRESENTATION — walking a reviewer through the design and defending the key call. Note this is
    an observed individual oral (AT1 Part B), so the skill is spoken, not written.
    • First bullet: present the proposed architecture to the required personnel — walk the DECISIONS that
    matter, not every line. Curate for the audience.
    • Second bullet: be ready to DEFEND the reliability cost-benefit call — why the database stays single-AZ
    rather than Multi-AZ. This is the question a reviewer will press.
    • Third bullet: seek feedback and respond — accept, adjust, or defend with reasons. This is an observed
    individual oral in AT1 Part B; responding well is assessed.
    Misconception to pre-empt: "presenting = reading every slide." No — you walk the decisions that matter
    and can defend them under questioning; reading the document aloud isn't presenting it.
    Question to pose: "A reviewer says 'a real accounting system should have a Multi-AZ database' — what's
    your response?" (defend the cost-benefit: vendor single-instance, product-replacement cost
    disproportionate to the goal).
    UoC/AT1 tie: ICTCLD504 PC 2.4 (present for review to required personnel) → AT1 Part B observed
    presentation.
- [EX] Rehearse the design walkthrough
  - For the practice engagement (the website vehicle), present your assembled Solution Design to a mock review panel.
  - Walk the key decisions and defend the cost-benefit trade-offs; seek and respond to feedback.
  timer: ~25 min
  image: none
  notes:
    Facilitation — the Section 1 practice; students present their assembled practice Solution Design to a
    mock review panel — a live rehearsal of the AT1 Part B oral.
    Tell students: "For the practice engagement — the website vehicle — present your assembled Solution
    Design to a mock review panel. Walk the key decisions, defend your cost-benefit trade-offs, and seek and
    respond to feedback."
    Run it (put on the board):
    1. Pair or small-group: one presents, the others are the review panel.
    2. Presenter walks the decisions that matter (not every line) and defends at least one cost-benefit
    trade-off.
    3. Panel gives feedback; presenter responds — accept, adjust, or defend with reasons. Then swap.
    Must produce: each student has presented once and fielded at least one challenge on a trade-off.
    Timing: ~25 min. Where they get stuck: they read the document instead of presenting, and they crumble on
    the first challenge instead of defending with the cost-benefit reasoning — coach both.
    Share-back prompt: ask a panel which defence they found most convincing, and why.
    No-leakage note: the website is the practice vehicle; AT1 assesses the presentation on Ledgerline —
    comparable, not identical.

### C2 — Obtaining sign-off
- Teaches: [ICTCLD504 PC 2.5]
- Kicker: get the deploy authorised
- [BESPOKE] The deploy sign-off — the approval gate
  - Obtain sign-off to proceed to deployment from the required personnel — the formal authorisation to build.
  - Sign-off is the gate: no AT2/AT3 work starts until the design is approved.
  - Record it — who approved, on what, when — as part of the Solution Design.
  image: none
  notes:
    Open Section 2 — the deploy sign-off, the formal authorisation that gates the build. Teach it as a real
    gate with a record, not a formality.
    • First bullet: obtain sign-off to proceed to deployment from the required personnel — the formal
    AUTHORISATION to build.
    • Second bullet: sign-off is the GATE — no AT2/AT3 work starts until the design is approved. It has
    consequences.
    • Third bullet: RECORD it — who approved, on what, when — as part of the Solution Design. An unrecorded
    approval is no approval.
    Misconception to pre-empt: "sign-off is just a signature at the end." No — it's the authorisation that
    lets the build begin, and it must be recorded (who/what/when) to be evidence.
    Question to pose: "What can't happen until this sign-off is obtained and recorded?" (the AT2/AT3 build —
    sign-off gates deployment).
    UoC/AT1 tie: ICTCLD504 PC 2.5 (obtain sign-off to proceed to deployment) → the AT1 sign-off record.
- [BESPOKE] Two approval moments — don't confuse them
  - This is the cluster's first approval: sign-off to proceed to deployment, on the design.
  - The second is the final sign-off at AT3, on the deployed and tested improvement.
  - This gate authorises the build; the AT3 gate accepts the result.
  image: none
  notes:
    Distinguish the cluster's TWO approval moments so students don't conflate them — a common exam error.
    This slide exists purely to separate them cleanly.
    • First bullet: THIS is the cluster's first approval — sign-off to proceed to deployment, on the DESIGN.
    It authorises work that hasn't happened yet.
    • Second bullet: the SECOND is the final sign-off at AT3 — on the deployed and tested improvement. It
    accepts work that has happened.
    • Third bullet: this gate authorises the build; the AT3 gate accepts the result. Different moment,
    different object, different question.
    Misconception to pre-empt: "sign-off is sign-off." No — the AT1 sign-off approves a PLAN to build; the
    AT3 sign-off accepts a BUILT-and-tested result. Confusing them muddles what each is evidence of.
    Question to pose: "The AT1 sign-off and the AT3 sign-off — what does each one approve?" (AT1: proceed to
    deploy, on the design; AT3: accept the deployed & tested improvement).
    UoC/AT1 tie: ICTCLD504 PC 2.5 (obtain sign-off to proceed) — the first of the cluster's two approval
    moments; the second is evidenced at AT3.
- [TAKEAWAYS] Topic 4 · Key takeaways
  - Assemble the baseline analysis and the four design concerns into one reviewable Solution Design.
  - The cost-benefit rides inside the document — no separate business case; be ready to defend the no-Multi-AZ call.
  - Present the proposed architecture to the required personnel and respond to feedback.
  - Obtain and record the sign-off to proceed — the deploy gate, distinct from the AT3 final sign-off.
  image: none

### Close
- [BESPOKE] Next: Topic 5 — leading the AT2 build
  - AT1 is closed out: designed, documented, presented, signed off to proceed.
  - Next you switch from design to build — lead and plan the team that implements the approved design.
  image: none

## Build notes
~10 slides. One `[EX]` rehearses the design walkthrough + sign-off conversation on the website practice vehicle (design only, no build). One `[TABLE]` gives the Solution Design document structure. One decorative `gen` image (opener hero); no technical diagram.

## Changelog
- 2026-07-02 — authored to full content.
