# Topic 05 Leading and planning the team build — Slide plan
> **Covers:** Topic 05 — see coverage.md
> **STATUS: DRAFT** (authored 2026-07-02).

## Depth ceiling
LEADERSHIP / team-planning — plan the team and set it up to build (BSBXTW401 el 1–2): objectives, performance plans, accountability, contingencies, and allocating the four IaC components. Not technical design/build — the CloudFormation write itself is Topic 6 / AT3 and is NOT 504-assessed here.

## Teaching source
Bespoke throughout, drawn from BSBXTW401 leadership content (team planning, task allocation, facilitation) applied to the four-component IaC allocation. In-world team = YAT ICT staff improving Ledgerline.

## AWS pin table
None — leadership (BSBXTW401) topic; bespoke.

## Slides

### Opener
- [BESPOKE] Leading the build team
  - Topic 5 opens AT2: the approved design is written as CloudFormation by a **team of four**, one IaC component each — network, compute, database, storage.
  - Dividing the write is the leadership vehicle: you plan the team, set expectations, and allocate the work — the write itself is a 504 concern, not assessed here.
  - This Topic is the set-up half of AT2 (plan and stand up the team); leading them *through* the write is Topic 6.
  - In-world, the team is YAT ICT staff improving Ledgerline.
  image: gen flat vector hero illustration of a team leader assigning four workstreams to four team members around a table, blue and gold accents, minimal, no text
  notes:
    Frame Topic 5 as the pivot into AT2 — AT1 was the design; AT2 is LEADERSHIP evidence. Set the
    vehicle; don't teach team-planning yet.
    • First bullet: the approved design is written as CloudFormation by a TEAM OF FOUR, one IaC component
    each — network, compute, database, storage. That division is the whole set-up.
    • Second bullet (the key framing): dividing the write is the LEADERSHIP VEHICLE — you plan the team,
    set expectations, allocate the work. The CloudFormation write itself is a 504 concern and is NOT
    assessed here; what's marked is how you lead.
    • Third bullet: this Topic is the SET-UP half of AT2 (plan and stand up the team); leading them
    through the write is Topic 6.
    • Fourth bullet: in-world the team is YAT ICT staff improving Ledgerline — keep it concrete.
    Misconception to pre-empt: "this is a CloudFormation topic." No — the code is the vehicle; the
    assessed evidence is the team plan, allocation and facilitation (BSBXTW401 el 1–2). Nobody is marked
    on their template here.
    Question to pose: "If the four of you each write one component, what's the single biggest risk — and
    whose job is it to manage it?" (the components don't integrate; the team leader's).
    UoC/AT2 tie: opens the AT2 leadership arc — BSBXTW401 el 1–2 (plan + coordinate the team); everything
    today feeds the team plan, allocation records and facilitated set-up evidenced in AT2.

### C1 — Objectives, performance plans & accountability
- Teaches: [BSBXTW401 PC 1.1] · [BSBXTW401 PC 1.2] · [BSBXTW401 PC 1.3] · [BSBXTW401 KE 1] · [BSBXTW401 KE 2]
- Kicker: know the goal, set expectations, hold the line
- [PRIMER] Team objectives, responsibilities & outcomes
  - Start by naming the common objective: deliver the approved Ledgerline design as working, deployed IaC.
  - Break it into responsibilities and required outcomes — what the team must produce, and to what standard.
  - Shared, explicit objectives are what let four separate component-writers pull in one direction.
  image: none
  notes:
    Open Section 1. Teach that a team pulls together only when its common objective is NAMED and shared —
    start there.
    • First bullet: name the common objective out loud — deliver the approved Ledgerline design as
    working, deployed IaC. Everyone should be able to recite it.
    • Second bullet: break the objective into RESPONSIBILITIES and required OUTCOMES — what the team must
    produce and to what standard. Objective → responsibilities → outcomes is the chain.
    • Third bullet: shared, explicit objectives are exactly what let four separate component-writers pull
    in ONE direction — without them you get four disconnected efforts.
    Misconception to pre-empt: "the objective is obvious, we can skip stating it." No — unstated
    objectives drift; making it explicit and shared is the assessable act, not a formality.
    Question to pose: "What's the common objective of this build in one sentence — and could every member
    say it the same way?" (tests whether it's genuinely shared).
    UoC/AT2 tie: BSBXTW401 PC 1.1 (identify common objectives, responsibilities, required outcomes) →
    evidenced in the AT2 team plan.
- [BESPOKE] Performance plans set expectations
  - A performance plan sets each member's expected outcomes, goals and behaviours for their component.
  - Align each plan to the team objective and to relevant policies — a plan is not a wish-list, it is measurable.
  - Example: "network component templates valid, peer-reviewed and deployed to us-east-1 by the milestone; collaborates on shared parameters."
  image: none
  notes:
    The how-to for setting expectations — a PERFORMANCE PLAN per member. Teach it as a measurable
    instrument, not a pep talk.
    • First bullet: a performance plan sets each member's expected outcomes, goals and behaviours for
    THEIR component. One plan per person, tied to their part of the build.
    • Second bullet: align each plan to the team objective AND to relevant policies — and make it
    MEASURABLE. A plan is not a wish-list.
    • Third bullet: read the worked example aloud — note it names an outcome, a standard, a deadline and a
    collaboration behaviour. That's what "measurable" looks like.
    Misconception to pre-empt: "a performance plan is vague encouragement." No — if you can't measure
    whether it was met, it isn't a performance plan; the specificity is what's marked.
    Question to pose: "Take the database owner — what would a good performance plan say their outcome,
    standard and deadline are?" (forces a measurable draft).
    UoC/AT2 tie: BSBXTW401 PC 1.2 (performance plans establishing expected outcomes/goals/behaviours in
    line with the team objective and relevant policies) → the AT2 team plan.
- [BESPOKE] Accountability, grounded in organisational & legislative requirements
  - Choose accountability strategies: clear ownership per component, review checkpoints, a shared definition of done.
  - Ground them in **organisational requirements** — workplace policies, codes of conduct, and YAT's reputation and culture (KE 1).
  - Respect the **legislative requirements** relevant to the workplace (work health & safety, privacy, anti-discrimination) (KE 2) — accountability operates inside those rules.
  image: none
  notes:
    Section 1's third move — accountability, and crucially the two things it must be GROUNDED in. This is
    where KE 1 and KE 2 land.
    • First bullet: choose concrete accountability strategies — clear ownership per component, review
    checkpoints, a shared definition of done. Name mechanisms, not slogans.
    • Second bullet: ground them in ORGANISATIONAL requirements — workplace policies, codes of conduct,
    and YAT's reputation and culture (KE 1). Accountability isn't invented; it sits on the org's rules.
    • Third bullet: respect the LEGISLATIVE requirements relevant to the workplace — WHS, privacy,
    anti-discrimination (KE 2). Accountability operates INSIDE those rules, never outside them.
    Misconception to pre-empt: "accountability = blame when it goes wrong." No — it's the up-front
    structure of ownership and checkpoints so work is owned and visible; it's preventive, not punitive.
    Question to pose: "Name one organisational policy and one law that would shape how you hold this team
    accountable" (draws out KE 1 vs KE 2 — they're different sources).
    UoC/AT2 tie: BSBXTW401 PC 1.3 + KE 1 + KE 2 → the accountability strategies in the AT2 team plan,
    grounded in organisational + legislative requirements.

### C2 — Contingency planning
- Teaches: [BSBXTW401 PC 1.4] · [BSBXTW401 KE 9]
- Kicker: plan for the things that go wrong
- [BESPOKE] Typical team contingencies
  - Plan for contingencies that could impact the team before they happen — don't improvise under pressure.
  - The typical workplace ones: unplanned leave or absence of a component owner; re-allocation of work tasks when load shifts; succession planning for important roles (KE 9).
  - For the build team: if the database-component owner is absent, who picks it up, and how is the handover documented?
  - A contingency is a named trigger plus a pre-agreed response — write it into the team plan.
  image: none
  notes:
    Section 2 — contingency planning. Teach it as naming the failure modes BEFORE they happen, not
    improvising under pressure.
    • First bullet: plan for contingencies that could impact the team ahead of time — the point is you
    decide the response while calm, not mid-crisis.
    • Second bullet: name the TYPICAL workplace ones (KE 9) — unplanned leave or absence of a component
    owner; re-allocation of work when load shifts; succession planning for important roles. These three
    are the examinable list.
    • Third bullet: make it concrete for this build — if the database-component owner is absent, who picks
    it up, and how is the handover documented?
    • Fourth bullet (the definition): a contingency is a NAMED TRIGGER plus a PRE-AGREED RESPONSE — write
    it into the team plan.
    Misconception to pre-empt: "contingency planning is just listing risks." No — a risk without a
    pre-agreed trigger-and-response isn't a contingency; the response is the deliverable.
    Question to pose: "Your compute-component owner goes on unplanned leave the day before the milestone —
    what's your pre-agreed response?" (forces a trigger→response pair).
    UoC/AT2 tie: BSBXTW401 PC 1.4 + KE 9 (plan for the typical workplace contingencies) → the
    contingencies section of the AT2 team plan.

### C3 — Communicating & allocating the component work
- Teaches: [BSBXTW401 PC 2.1] · [BSBXTW401 PC 2.2] · [BSBXTW401 PE 1]
- Kicker: communicate the goal, then hand out the work
- [BESPOKE] Communicate the objectives & responsibilities
  - Communicate the common objectives and each member's responsibilities so everyone shares the same picture of "done".
  - Confirm understanding — a kick-off where the team restates the goal and how the four components integrate.
  - Clear communication up front is what prevents four components that don't fit together.
  image: none
  notes:
    Open Section 3 — coordination begins with COMMUNICATING the goal before any work is handed out.
    • First bullet: communicate the common objectives and each member's responsibilities so everyone
    shares the same picture of "done".
    • Second bullet: CONFIRM understanding — run a kick-off where the team restates the goal and how the
    four components integrate. Communication isn't done until it's been played back.
    • Third bullet: this up-front clarity is precisely what prevents four components that don't fit
    together — the integration failure is a communication failure.
    Misconception to pre-empt: "I emailed the plan, so I've communicated it." No — communication is
    confirmed shared understanding, not a sent message; the kick-off play-back is the evidence.
    Question to pose: "How would you check the team actually shares the same picture of 'done' before they
    start writing?" (draws out confirmation techniques).
    UoC/AT2 tie: BSBXTW401 PC 2.1 (communicate common objectives and responsibilities) → the facilitated
    set-up / kick-off evidenced in AT2.
- [BESPOKE] Allocate the four components
  - Allocate the four IaC components — **network, compute, database, storage** — one per member, by expertise or development potential (PC 2.2).
  - Give appropriate instruction with each allocation: scope of the component, the interfaces it must expose, and any required contingencies (PE 1).
  - The four allocations integrate into one design — allocate the seams (shared parameters, dependencies), not just the boxes.
  image: diagram component-allocation
  notes:
    The core allocation move — hand out the four components. Use the component-allocation diagram to show
    four members mapping to four components that integrate into one design.
    • First bullet: allocate the four IaC components — NETWORK, COMPUTE, DATABASE, STORAGE — one per
    member, by expertise OR development potential (PC 2.2). Note "development potential" — you can
    allocate to stretch someone, not only to their strength.
    • Second bullet: give APPROPRIATE INSTRUCTION with each allocation — scope of the component, the
    interfaces it must expose, and any required contingencies (PE 1). Allocation without instruction
    isn't allocation.
    • Third bullet (the seam point): the four integrate into ONE design — so allocate the SEAMS too
    (shared parameters, dependencies), not just the boxes. That's what the diagram shows.
    Misconception to pre-empt: "allocation = give each person a box and walk away." No — the assessable
    part is the instruction and the seams; unmanaged interfaces are where the build breaks.
    Question to pose: "You give the network component to your least experienced member for development —
    what extra instruction and contingency does that allocation need?" (ties development potential to
    instruction).
    UoC/AT2 tie: BSBXTW401 PC 2.2 + PE 1 (allocate by expertise/development potential, with instruction
    and required contingencies) → the task-allocation records in AT2.
- [EX] Plan & allocate the practice build team
  - For the practice engagement, draft the **team plan**: common objective, per-member performance plans, accountability strategies and contingencies.
  - **Allocate the four components** to four members with clear instruction and any required contingencies.
  - Produce the artefact you'll produce for the assessed Ledgerline team — this is the practice run.
  timer: ~30 min
  image: none
  notes:
    Facilitation — the Section 3 practice; students produce the WHOLE team plan for the PRACTICE
    engagement, the same artefact they'll produce for the assessed Ledgerline team.
    Tell students, in these words: "For the practice engagement, draft the team plan — common objective,
    per-member performance plans, accountability strategies and contingencies — then allocate the four
    components to four members with clear instruction and any contingencies."
    Steps (put on the board):
    1. State the common objective and break it into responsibilities/outcomes.
    2. Write a measurable performance plan per member.
    3. Choose accountability strategies (grounded in policy + law) and name the contingencies.
    4. Allocate network / compute / database / storage — one per member — with instruction AND the seams
    (shared parameters, dependencies).
    Must produce: a team plan (objective, four performance plans, accountability, contingencies) plus an
    allocation of the four components with instruction — the practice run of the assessed artefact.
    Timing: ~30 min. Where they get stuck: they allocate the four boxes but forget the SEAMS and the
    INSTRUCTION — circulate and push "what does the network owner need to expose to the compute owner?";
    and performance plans come out as pep talk, not measurable.
    Share-back prompt: take one team's allocation and ask the room where two components must agree an
    interface — surface a seam.
    No-leakage note: this is the PRACTICE engagement — AT2 assesses the SAME leadership on the Ledgerline
    team (comparable, not identical); keep them on the practice vehicle here.

### C4 — Facilitating collaboration
- Teaches: [BSBXTW401 PC 2.3] · [BSBXTW401 PC 2.4] · [BSBXTW401 KE 3] · [BSBXTW401 KE 6] · [BSBXTW401 KE 7]
- Kicker: keep the team open, respectful and connected
- [PRIMER] Facilitation & communication styles
  - Facilitate open and respectful communication and collaboration between members (PC 2.3).
  - Use facilitation techniques that build cohesion and effectiveness — stand-ups, shared review, ground rules (KE 3).
  - Match the method and style of communication to the message and the person (KE 6) — synchronous for decisions, written for the record.
  image: none
  notes:
    Open Section 4 — facilitation. Teach the techniques that keep a divided team behaving as one.
    • First bullet: facilitate OPEN and RESPECTFUL communication and collaboration between members
    (PC 2.3) — the leader's job is to create the conditions, not to do all the talking.
    • Second bullet: name facilitation techniques that build cohesion and effectiveness (KE 3) —
    stand-ups, shared review, ground rules. These are concrete, nameable routines.
    • Third bullet: match the METHOD and STYLE of communication to the message and the person (KE 6) —
    synchronous for decisions, written for the record. Different messages need different channels.
    Misconception to pre-empt: "good communication = more meetings." No — it's matching the channel to the
    message; a decision needs a conversation, a record needs writing. The wrong channel is the waste.
    Question to pose: "You need the team to agree an integration boundary AND you need a durable record of
    it — what method(s) do you use, and why both?" (draws out KE 6 method-to-message).
    UoC/AT2 tie: BSBXTW401 PC 2.3 + KE 3 + KE 6 (facilitate open/respectful collaboration; techniques;
    methods/styles) → the facilitated collaboration evidenced in AT2.
- [BESPOKE] Diverse teams & cross-collaboration
  - Consider the needs of members from diverse backgrounds: apply cross-cultural communication principles and accommodate special needs or disabilities (KE 7, PC 2.3).
  - Identify opportunities for cross-collaboration with internal and external teams — the DBA team, the security reviewers, an external CloudFormation SME (PC 2.4).
  - Respectful, inclusive facilitation is what makes a four-person split behave as one team.
  image: none
  notes:
    Second half of Section 4 — inclusion and reaching BEYOND the team. This is where KE 7 and PC 2.4 land.
    • First bullet: consider the needs of members from diverse backgrounds — apply cross-cultural
    communication principles and accommodate special needs or disabilities (KE 7, PC 2.3). Facilitation
    has to work for everyone in the room.
    • Second bullet: identify opportunities for CROSS-COLLABORATION with internal and external teams
    (PC 2.4) — the DBA team, the security reviewers, an external CloudFormation SME. The four-person team
    isn't an island.
    • Third bullet: respectful, inclusive facilitation is what makes a four-person split behave as one
    team — it's the enabler, not a nicety.
    Misconception to pre-empt: "cross-collaboration is just delegating outside." No — PC 2.4 is about
    identifying where OTHER teams (internal or external) add value to your build; naming those
    opportunities is the assessed act.
    Question to pose: "Which internal or external team would you pull in for the database component, and
    what would you go to them for?" (draws out a concrete PC 2.4 opportunity).
    UoC/AT2 tie: BSBXTW401 PC 2.3 + PC 2.4 + KE 7 (diverse-background collaboration; cross-collaboration
    with internal/external teams) → the facilitated, inclusive set-up evidenced in AT2.
- [TAKEAWAYS] Topic 5 · Key takeaways
  - Name the common objective, set per-member performance plans, and choose accountability strategies grounded in policy and law.
  - Plan for the typical contingencies — absence, re-allocation, succession — before the build starts.
  - Communicate the objective, then allocate the four components one per member with clear instruction.
  - Facilitate open, respectful, inclusive collaboration and connect with internal/external teams.
  image: none

### Close
- [BESPOKE] Next: Topic 6 — lead the team through the build
  - You've planned the team and allocated the four components; next you lead, support and monitor them as they write the IaC.
  - Bring the team plan and allocations — Topic 6 runs the build against them.
  image: none

## Build notes
~13 slides. Bespoke leadership topic (no AWS pins). Exercise = draft the team/performance plan and allocate the four components for the practice engagement. One generated diagram (`diagram component-allocation` — four members mapped to the four components integrating into one design); one decorative `gen` image (opener hero).

## Changelog
- 2026-07-02 — authored to full content.
