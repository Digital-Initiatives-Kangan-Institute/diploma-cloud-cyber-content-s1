# Topic 06 Writing the IaC by component: leading, supporting and monitoring the team — Slide plan
> **Covers:** Topic 06 — see coverage.md
> **STATUS: DRAFT** (authored 2026-07-02).

## Depth ceiling
LEADERSHIP — lead, support and monitor the team (BSBXTW401 el 3–4) *while* it writes the improved-architecture CloudFormation, divided by component. The IaC write is the vehicle; the assessed evidence is the leadership exercised through it — coaching, feedback, conflict handling, development. The technical write is NOT 504-assessed (the individual deploy is AT3, Topics 7–8). No CloudFormation authoring depth here.

## Teaching source
BSBXTW401 leadership content (mentoring/coaching techniques, conflict-resolution/negotiation strategies, professional leadership behaviours, teamwork challenges); bespoke for leading a divided-IaC write in the YAT/Ledgerline scenario.

## AWS pin table
None — leadership (BSBXTW401) topic; bespoke.

## Slides

### Opener
- [BESPOKE] Leading the AT2 build
  - Topic 5 planned the team and allocated the four components; now the team writes the IaC and you lead the build.
  - The team leader runs the build: coaching, supporting, facilitating issue resolution, problem-solving, managing conflict, then monitoring performance and developing others.
  - In-world: you lead the YAT ICT team building Ledgerline's improved infrastructure.
  - Leadership, not code — the CloudFormation write is the vehicle; the assessed evidence (AT2) is how you lead it.
  image: gen flat vector hero illustration of a team leader coaching and giving feedback to developers at work, supportive gesture, blue and gold accents, minimal, no text
  notes:
    Frame Topic 6 as the DELIVERY half of AT2 — Topic 5 planned and allocated; now the team writes the
    IaC and you LEAD the build. Set the mode; don't teach coaching yet.
    • First bullet: Topic 5 planned the team and allocated the four components; now the team writes the
    code and you run the build.
    • Second bullet: name what "leading the build" actually is — coaching, supporting, facilitating issue
    resolution, problem-solving, managing conflict, then measuring performance and developing others. That
    list IS today's four sections.
    • Third bullet: in-world you lead the YAT ICT team building Ledgerline's improved infrastructure —
    keep it concrete.
    • Fourth bullet (the framing to hold all Topic): LEADERSHIP, NOT CODE — the CloudFormation write is
    the vehicle; the assessed evidence (AT2) is how you lead it.
    Misconception to pre-empt: "to lead the build I need to be the best coder." No — you don't write the
    components; you develop the people and run the process. The leadership is what's marked (BSBXTW401
    el 3–4).
    Question to pose: "If you're not writing any of the four components, what exactly are you contributing
    to this build?" (draws out coaching, unblocking, measuring, developing — the leadership).
    UoC/AT2 tie: opens the AT2 delivery arc — BSBXTW401 el 3–4 (support + monitor the team); everything
    today feeds the coaching/issue-resolution/feedback/development evidence in AT2.

### C1 — Coaching & supporting
- Teaches: [BSBXTW401 PC 3.1] · [BSBXTW401 PC 3.2] · [BSBXTW401 KE 4] · [BSBXTW401 KE 8]
- Kicker: coach the people, run the build
- [BESPOKE] The divided-IaC write — your vehicle
  - The team writes four components — network, compute, database, storage — one per member, integrated into one template.
  - The build flows: component drafts → integrate into one template → review and monitor → team sign-off.
  - You don't write the components; you run the build — coaching, supporting and monitoring the team through it.
  image: diagram team-build-flow
  notes:
    Set the vehicle before teaching coaching — use the team-build-flow diagram (component drafts →
    integrate → review/monitor → team sign-off) so students see WHERE leadership acts.
    • First bullet: the team writes four components — network, compute, database, storage — one per
    member, integrated into ONE template.
    • Second bullet: walk the flow off the diagram — component drafts → integrate into one template →
    review and monitor → team sign-off. Point at each stage.
    • Third bullet (the framing): you don't write the components; you RUN the build — coaching, supporting
    and monitoring the team through each of those stages. Your work sits ON the flow, not inside a
    component.
    Misconception to pre-empt: "the integrate step is a technical merge I do." No — you FACILITATE the
    integration (the seams the team agreed in Topic 5); the leadership is getting the four to fit, not
    typing the merge.
    Question to pose: "Point at the flow — at which stage is a conflict between two component owners most
    likely, and what do you do there?" (locates leadership on the diagram; sets up C2).
    UoC/AT2 tie: frames the C1–C4 leadership of the build; the divided write is the vehicle for BSBXTW401
    el 3–4 evidenced in AT2.
- [PRIMER] Mentoring & coaching techniques
  - Coaching develops capability in the moment; mentoring builds it over time — both grow the person, not just the task (KE 4).
  - Techniques: ask before telling, model then hand over, give room to try, check understanding.
  - Coaching is how you enhance the workplace culture — a team that learns from each other, not one that waits to be told.
  image: none
  notes:
    The primer for C1 — distinguish coaching from mentoring and give nameable techniques (KE 4).
    • First bullet: COACHING develops capability in the moment; MENTORING builds it over time — both grow
    the PERSON, not just the task (KE 4). Say the distinction explicitly.
    • Second bullet: name the techniques — ask before telling, model then hand over, give room to try,
    check understanding. These are the moves students are marked on using.
    • Third bullet: coaching is how you ENHANCE the workplace culture — a team that learns from each
    other, not one that waits to be told. Culture is the payoff, not a side-effect.
    Misconception to pre-empt: "coaching = giving the answer faster." No — "ask before telling" is the
    point; if you just supply the fix you've solved the task but developed no one.
    Question to pose: "A member is stuck on their component — what's a COACHING response versus a telling
    response?" (draws out ask-before-telling).
    UoC/AT2 tie: BSBXTW401 KE 4 (mentoring/coaching techniques) → the coaching evidence in AT2; underpins
    PC 3.1 on the next slide.
- [BESPOKE] Coach the culture, support the individuals
  - Provide coaching to staff to enhance workplace culture as the team writes its components (PC 3.1).
  - Support individuals per organisational requirements toward the common team goals — the one integrated, working template (PC 3.2).
  - Role-model professional leadership behaviours: reliability, fairness, openness, following through (KE 8).
  image: none
  notes:
    Apply the coaching primer to the build — this is where PC 3.1, PC 3.2 and KE 8 land.
    • First bullet: provide COACHING to enhance workplace culture as the team writes its components
    (PC 3.1) — coaching in the flow of the build, not a separate training session.
    • Second bullet: SUPPORT individuals per organisational requirements toward the COMMON goal — the one
    integrated, working template (PC 3.2). Support is aimed at the shared outcome, not just individual
    comfort.
    • Third bullet: role-model professional leadership behaviours — reliability, fairness, openness,
    following through (KE 8). The team copies what you DO, not what you say.
    Misconception to pre-empt: "supporting individuals means shielding them from the hard parts." No —
    support moves them toward the common goal; sometimes that's a stretch, not a rescue.
    Question to pose: "Name one professional behaviour you'd role-model in the first stand-up, and what
    the team would take from seeing it" (makes KE 8 concrete).
    UoC/AT2 tie: BSBXTW401 PC 3.1 + PC 3.2 + KE 8 → the coaching/support records and role-modelling
    evidenced in AT2.

### C2 — Facilitating issue resolution & problem-solving
- Teaches: [BSBXTW401 PC 3.3] · [BSBXTW401 PC 3.4] · [BSBXTW401 PE 5] · [BSBXTW401 KE 5] · [BSBXTW401 KE 10]
- Kicker: surface the issue, resolve it together
- [PRIMER] Facilitating issue resolution & problem-solving
  - Facilitate the team to identify, brainstorm, report and resolve task-related issues and inefficiencies — don't solve it for them, run the process (PC 3.3).
  - Use problem-solving skills for team, task or individual challenges: name the problem, options, decide, act (PC 3.4).
  - A stand-up is the routine that surfaces issues early — blockers reported before they stall the build.
  image: none
  notes:
    Open Section 2 — the leader RUNS the problem-solving process, doesn't own the solution. PC 3.3 and
    PC 3.4 land here.
    • First bullet: facilitate the team to IDENTIFY, BRAINSTORM, REPORT and RESOLVE task-related issues
    and inefficiencies — don't solve it for them, run the process (PC 3.3). The verbs are the process.
    • Second bullet: use problem-solving skills for team, task or individual challenges — name the
    problem, options, decide, act (PC 3.4). A repeatable four-step loop.
    • Third bullet: a STAND-UP is the routine that surfaces issues early — blockers reported before they
    stall the build. Routine beats heroics.
    Misconception to pre-empt: "resolving issues = the leader gives the fix." No — PC 3.3 is FACILITATION;
    if you supply every answer the team never learns to surface and solve its own issues.
    Question to pose: "A member reports their component won't integrate — do you fix it, or facilitate?
    What does facilitating look like here?" (draws out the run-the-process stance).
    UoC/AT2 tie: BSBXTW401 PC 3.3 + PC 3.4 → the issue-resolution episodes evidenced in AT2; exercised in
    the next activity.
- [BESPOKE] Conflict, challenges & the teamwork risks
  - Manage conflicts and challenges per organisational requirements using conflict-resolution and negotiation strategies (PE 5, KE 5).
  - Separate the person from the problem; find the shared interest; agree a way forward, not a winner.
  - Watch for the teamwork challenges the evidence expects (KE 10): difficulties performing tasks; conflicts with clients or team members; potential risks or safety hazards; unethical or inappropriate behaviour.
  image: none
  notes:
    The conflict-and-challenges slide — PE 5, KE 5 and the KE 10 checklist land here.
    • First bullet: manage conflicts and challenges per organisational requirements using
    conflict-resolution and negotiation strategies (PE 5, KE 5). Conflict is normal; managing it well is
    the skill.
    • Second bullet: the technique — separate the person from the problem; find the shared interest; agree
    a way forward, not a winner. Say it as a procedure they can run.
    • Third bullet: watch for the teamwork challenges the evidence EXPECTS (KE 10) — difficulties
    performing tasks; conflicts with clients or team members; potential risks or safety hazards;
    unethical or inappropriate behaviour. This is a named list they must be able to recognise.
    Misconception to pre-empt: "good teams don't have conflict, so I should suppress it." No — surfaced,
    well-managed conflict improves the build; suppressed conflict resurfaces at integration. Manage, don't
    bury.
    Question to pose: "Two owners disagree on the network/compute boundary — what's the shared interest
    you'd steer them to?" (models person-vs-problem; previews the seeded conflict in the activity).
    UoC/AT2 tie: BSBXTW401 PE 5 + KE 5 + KE 10 → the conflict-management episode evidenced in AT2
    (exercised next).
- [EX] Run the stand-up & resolve a seeded conflict
  - Lead a stand-up for the practice team: each member reports progress on their component and any blocker.
  - A conflict is injected (two members disagree over an integration boundary) — facilitate it to a resolution and record how you handled it.
  timer: ~25 min
  image: none
  notes:
    Facilitation — the Section 2 practice; students LEAD a stand-up and facilitate an injected conflict to
    resolution, recording how they handled it (the AT2 evidence shape).
    Tell students, in these words: "Lead a stand-up for your practice team — each member reports progress
    on their component and any blocker. Partway through, a conflict is injected: two members disagree over
    an integration boundary. Facilitate it to a resolution and record how you handled it."
    Steps (put on the board):
    1. Run the stand-up — each member: what's done, what's next, any blocker.
    2. When the conflict lands, separate person from problem; surface each side's interest.
    3. Steer to a shared way forward (not a winner); confirm the agreed boundary.
    4. Record the episode — the issue, what you did, the resolution.
    Must produce: a short written record of the facilitated stand-up and the conflict resolution — the
    practice version of the AT2 issue-resolution evidence.
    Timing: ~25 min. Where they get stuck: they ADJUDICATE (pick a winner) instead of facilitating a
    shared way forward — circulate and push "what do both owners actually need?"; and the stand-up drifts
    into solving the whole thing on the spot.
    Share-back prompt: ask one leader how they turned the disagreement into a shared interest — surface the
    person-vs-problem move.
    No-leakage note: this is the PRACTICE team — AT2 assesses the same conflict-management leadership on
    the Ledgerline build (comparable, not identical); keep them on the practice vehicle.

### C3 — Measuring performance & feedback
- Teaches: [BSBXTW401 PC 4.1] · [BSBXTW401 PC 4.2] · [BSBXTW401 PE 2]
- Kicker: measure against the plan, feed it back
- [PRIMER] Measuring performance against the work plans
  - Measure each member's performance against the agreed work plans from Topic 5 — the plan is the yardstick (PC 4.1).
  - Measure the work, not the person: what was due, what was delivered, on what quality.
  - Measurement is the input to feedback — you can't give useful feedback without it.
  image: none
  notes:
    Open Section 3 — measurement is the input to feedback. PC 4.1 lands here.
    • First bullet: measure each member's performance against the AGREED WORK PLANS from Topic 5 — the
    plan is the yardstick (PC 4.1). This is why the performance plans had to be measurable.
    • Second bullet: measure the WORK, not the person — what was due, what was delivered, at what quality.
    Keep it objective and evidence-based.
    • Third bullet: measurement is the INPUT to feedback — you can't give useful feedback without it.
    Section 3 runs measure → feedback in order.
    Misconception to pre-empt: "measuring performance = judging the person." No — you measure the work
    against the plan; the person-level conversation is the feedback that follows, and it's about the gap,
    not character.
    Question to pose: "The compute owner's plan said 'valid, peer-reviewed, deployed by the milestone' —
    how do you measure whether they met it?" (ties measurement back to the Topic 5 plan).
    UoC/AT2 tie: BSBXTW401 PC 4.1 (measure performance against agreed work plans) → the
    performance-measurement evidence in AT2.
- [BESPOKE] Timely, constructive feedback & assistance
  - Provide timely, constructive performance feedback to expected organisational standards — close to the event, specific, actionable (PC 4.2).
  - Balance recognition with the gap; describe the behaviour and its effect, then agree the next step.
  - Provide feedback and assistance to team members — feedback names the gap, assistance helps close it (PE 2).
  image: none
  notes:
    The feedback slide — PC 4.2 and PE 2 land here. Teach feedback as a skill with a shape.
    • First bullet: provide TIMELY, CONSTRUCTIVE feedback to expected organisational standards — close to
    the event, specific, actionable (PC 4.2). Late or vague feedback doesn't change anything.
    • Second bullet: the shape — balance recognition with the gap; describe the BEHAVIOUR and its EFFECT,
    then agree the next step. Behaviour → effect → next step keeps it constructive.
    • Third bullet: provide feedback AND ASSISTANCE (PE 2) — feedback names the gap, assistance helps
    close it. Naming a gap without helping close it is half a job.
    Misconception to pre-empt: "constructive feedback means only positives." No — it means specific and
    actionable, including the gap; a "constructive" that never names the gap develops no one.
    Question to pose: "Give the database owner feedback that they missed the peer-review step — say it as
    behaviour → effect → next step" (rehearses the shape live).
    UoC/AT2 tie: BSBXTW401 PC 4.2 + PE 2 (timely constructive feedback; feedback and assistance) → the
    feedback records in AT2.

### C4 — Development opportunities & action plans
- Teaches: [BSBXTW401 PC 4.3] · [BSBXTW401 PC 4.4] · [BSBXTW401 PE 3] · [BSBXTW401 PE 4]
- Kicker: turn the gaps into growth
- [BESPOKE] Identify learning & development opportunities
  - Identify specific learning and development opportunities to improve team and individual performance and behaviours (PC 4.3).
  - A gap you measured (C3) becomes a development opportunity — a skill to build, a behaviour to shift.
  - Tie each opportunity to an individual and to the team's common goals.
  image: none
  notes:
    Open Section 4 — turn measured gaps into GROWTH. PC 4.3 lands here.
    • First bullet: identify specific learning and development opportunities to improve team and
    individual performance and behaviours (PC 4.3). "Specific" is the word — not "do more training".
    • Second bullet: a gap you MEASURED (Section 3) becomes a development opportunity — a skill to build,
    a behaviour to shift. The measurement feeds this directly.
    • Third bullet: tie each opportunity to an INDIVIDUAL and to the team's common goals — development
    serves the build, not just the person's CV.
    Misconception to pre-empt: "development opportunities are generic courses." No — they're specific,
    drawn from a measured gap, tied to a named person and the team goal; generic = not assessable.
    Question to pose: "The network owner struggled with shared parameters — what specific development
    opportunity does that suggest, for whom?" (turns a measured gap into a specific opportunity).
    UoC/AT2 tie: BSBXTW401 PC 4.3 (identify specific learning/development opportunities) → the development
    plan evidenced in AT2.
- [BESPOKE] Action plans, collated feedback & developing others
  - Implement action plans to address individual and team training needs — who, what, by when (PC 4.4).
  - Collate feedback on individual and team performance so the picture is evidence, not impression (PE 3).
  - Identify and implement development opportunities for others — leadership grows the team, not just the build (PE 4).
  image: none
  notes:
    Close Section 4 — make development ACTIONABLE and evidence-based. PC 4.4, PE 3, PE 4 land here.
    • First bullet: implement ACTION PLANS to address individual and team training needs — who, what, by
    when (PC 4.4). An opportunity without an action plan is just a note.
    • Second bullet: COLLATE feedback on individual and team performance so the picture is EVIDENCE, not
    impression (PE 3). Pulling it together is what makes it defensible.
    • Third bullet: identify and implement development opportunities for OTHERS (PE 4) — leadership grows
    the team, not just the build. This is the leader-develops-people point.
    Misconception to pre-empt: "collating feedback is admin busywork." No — collated feedback is what
    turns scattered impressions into an evidence base for the action plans (and for AT2).
    Question to pose: "You have feedback from three stand-ups on the storage owner — what does 'collating'
    it give you that three separate notes don't?" (draws out the evidence-base point).
    UoC/AT2 tie: BSBXTW401 PC 4.4 + PE 3 + PE 4 (action plans; collate feedback; develop others) → the
    development / action-plan evidence in AT2.
- [TAKEAWAYS] Topic 6 · Key takeaways
  - You lead the build; the divided-IaC write is the vehicle, the leadership is the assessed evidence (AT2).
  - Coach to enhance culture and support individuals toward the common goal; role-model professional behaviours.
  - Facilitate issue resolution and problem-solving; manage conflict and the teamwork risks.
  - Measure against the work plans, give timely constructive feedback, and turn gaps into development action plans.
  image: none

### Close
- [BESPOKE] Next: Topic 7 — the individual deploy
  - You can now lead, support and monitor the team through the build.
  - Next (AT3, Topics 7–8): each member deploys, tests and documents their built infrastructure — the 504-assessed individual work.
  image: none

## Build notes
~14 slides. One `[EX]` — lead a practice-team stand-up and facilitate a seeded conflict to resolution (~25 min). One generated diagram (`diagram team-build-flow`: component drafts → integrate → review/monitor → team sign-off); one decorative `gen` image (opener hero); all other slides `image: none`. Leadership depth only — the technical write is the vehicle, not the assessed object.

## Changelog
- 2026-07-02 — authored to full content.
