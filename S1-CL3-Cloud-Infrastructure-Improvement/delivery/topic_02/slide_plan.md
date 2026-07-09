# Topic 02 Designing for reliability — Slide plan
> **Covers:** Topic 02 — see coverage.md
> **Subtitle:** Design the reliability improvements to the goals — and know when NOT to build them
> **STATUS: DRAFT** (authored 2026-07-02).

## Depth ceiling
DESIGN — design the reliability improvements on paper to the goals set in Topic 1; the build is AT3. No implementation; no over-engineering. The DB tier stays design-level (the lab role denies `rds:ModifyDBInstance`).

## Teaching source
AWS reliability pillar (Multi-AZ, backup/restore, cross-Region DR) pinned at Step 4 (TBD); bespoke for the Ledgerline Multi-AZ-database cost-benefit framing, the parameterised-template design, and the India residency slice.

## AWS pin table
TBD — AWS reliability/architecture modules to be pinned.

## Slides

### Opener
- [BESPOKE] Designing for reliability
  - Topic 2 continues AT1: with the goals set in Topic 1, you now design the changes that make Ledgerline's infrastructure reliable.
  - Reliability, jointly with security, scalability and cost — improve the architecture without over-building it.
  - Target: application-tier Multi-AZ + database backup/restore + cross-Region DR to Melbourne (data stays in Australia).
  - Design only, to the goals — the build is AT3.
  image: gen flat vector hero illustration of a resilient cloud architecture spanning two availability zones and a backup region, shields and redundancy arrows, blue and gold accents, minimal, no text
  notes:
    Frame the pivot from analysis to DESIGN — with Topic 1's goals set, they now design the reliability
    changes. Set the depth ceiling: design on paper, to the goals, not beyond; the build is AT3.
    • First two bullets: Topic 2 continues AT1 — design the changes that make Ledgerline reliable,
    reliability optimised JOINTLY with security, scalability and cost. Improve without over-building.
    • Third bullet: name the target — application-tier Multi-AZ + database backup/restore + cross-Region
    DR to Melbourne (data stays in Australia). Say "Melbourne — onshore" out loud.
    • Fourth bullet (the discipline): design only, to the goals — the build is AT3. Resist drawing console
    steps.
    Misconception to pre-empt: "reliable = make everything Multi-AZ." No — this Topic's centrepiece is
    REJECTING a Multi-AZ database on a cost-benefit call. Reliability is targeted, not maximised.
    Question to pose: "Topic 1 set the reliability goal — what does 'design to the goal, not beyond it' rule
    out?" (gold-plating; any redundancy the goal doesn't justify).
    UoC/AT1 tie: this Topic develops ICTCLD504 PC 2.3, PE 1 and KE 4/5/8/9; the output is the reliability
    sections + KE appendix of the AT1 Solution Design.

### C1 — Reliability improvement design
- Teaches: [ICTCLD504 PC 2.3] · [ICTCLD504 PE 1] · [ICTCLD504 KE 9]
- Kicker: improve reliability to the goal, not beyond it
- [PRIMER] What makes a cloud system reliable
  - Reliability = the system keeps serving through component and zone failures, and recovers from loss.
  - Three building blocks: redundancy across Availability Zones (Multi-AZ), backup/restore, and cross-Region disaster recovery.
  - Reliability is designed jointly with security, scalability and cost — each choice is a trade-off, not a maximum.
  image: none
  notes:
    Open Section 1 with the vendor-neutral definition of reliability and its building blocks — the frame
    before the Ledgerline-specific design.
    • First bullet: reliability = the system keeps serving through component and zone failures, AND recovers
    from loss. Two halves — continuity and recovery.
    • Second bullet: the three building blocks — redundancy across AZs (Multi-AZ), backup/restore, and
    cross-Region DR. Map each to which half it serves.
    • Third bullet: reliability is designed JOINTLY with security, scalability and cost — each choice is a
    trade-off, not a maximum. This is the anti-gold-plating rule again.
    Misconception to pre-empt: "backup and DR are the same thing." No — backup/restore recovers data in
    place; cross-Region DR survives losing a whole Region. Different failures, different tools.
    Question to pose: "Which building block protects against an AZ failure, and which against losing the
    whole Region?" (Multi-AZ vs cross-Region DR — separates the two).
    UoC/AT1 tie: ICTCLD504 KE 9 (features/techniques to improve reliability) → AT1 Solution Design
    reliability design + KE appendix.
- [BESPOKE] Review the architecture, set the reliability target
  - Review Ledgerline's single-AZ baseline against the reliability goals; name where a single failure takes the system down.
  - Target: the application tier goes Multi-AZ behind a load balancer; the database gets automated backup/restore; a cross-Region DR copy goes to Melbourne (Australian data stays onshore).
  - The database is deliberately NOT Multi-AZ — the next slide argues why.
  image: diagram reliability-target
  notes:
    Set the concrete reliability TARGET off the diagram — where the design adds redundancy, and the one
    place it deliberately does NOT. This tees up the centrepiece on the next slide.
    • First bullet: review the single-AZ baseline against the reliability goals; name where a single
    failure takes the system down (from Topic 1's analysis).
    • Second bullet: the target — app tier goes Multi-AZ behind a load balancer; the database gets automated
    backup/restore; a cross-Region DR copy goes to Melbourne (Australian data stays onshore). Point to each
    on the diagram.
    • Third bullet: flag it now — the database is deliberately NOT Multi-AZ; the next slide argues why.
    Leave the tension unresolved for one slide on purpose.
    Misconception to pre-empt: "the whole system goes Multi-AZ." No — only the APP tier does; the DB is
    handled by backup/restore + DR. Redundancy is applied tier by tier, to the goal.
    Question to pose: "The app tier goes Multi-AZ but the database doesn't — what could possibly justify
    treating them differently?" (sets up the cost-benefit centrepiece).
    UoC/AT1 tie: ICTCLD504 PC 2.3 (review & improve architecture for reliability) + PE 1 → AT1 Solution
    Design reliability design.
- [BESPOKE] The centrepiece — reject the Multi-AZ database
  - Ledgerline is a legacy accounting app, vendor-certified single-instance only — a Multi-AZ (failover) database is simply not available for it.
  - The only route to DB failover is to replace the accounting product: new licence, data migration, change management, and migration risk.
  - That cost is disproportionate to the reliability gained — so the design REJECTS a Multi-AZ database and leaves the DB single-AZ with backup/restore + cross-Region DR. This cost-benefit call is the heart of the Topic.
  - Warn against the reflex: "reliable database = Multi-AZ database" is wrong here — justify against the goal and the cost, not against a checklist.
  image: none
  notes:
    THE centrepiece of the whole cluster — teach the cost-benefit REJECTION of a Multi-AZ database. Slow
    down here; this is the single most assessed piece of reasoning in AT1.
    • First bullet: Ledgerline is a legacy accounting app, vendor-certified single-instance only — a
    Multi-AZ (failover) database is simply not available for it.
    • Second bullet: the only route to DB failover is to REPLACE the accounting product — new licence, data
    migration, change management, migration risk. Spell out the true cost.
    • Third bullet (the call): that cost is disproportionate to the reliability gained, so the design REJECTS
    a Multi-AZ database and leaves the DB single-AZ with backup/restore + cross-Region DR. This is the heart
    of the Topic.
    • Fourth bullet: warn against the reflex — "reliable database = Multi-AZ database" is wrong HERE; justify
    against the goal and the cost, not a checklist.
    Misconception to pre-empt: exactly that reflex — students pattern-match "reliability → Multi-AZ" and lose
    the marks. The assessed skill is arguing the trade-off, not naming the feature.
    Question to pose: "You could get DB failover by replacing the product — why is that the WRONG call here?"
    (cost + risk disproportionate to the reliability the goal actually needs).
    UoC/AT1 tie: ICTCLD504 PC 2.3 + PE 1; this is the AT1 cost-benefit centrepiece — the Solution Design
    must ARGUE it, not just state it.
- [TABLE] Database reliability — the options weighed
  | Option | Reliability gain | Cost / risk | Verdict |
  | Single-AZ + backup/restore + cross-Region DR | recover from loss; DR to Melbourne | low — no product change | CHOSEN |
  | Multi-AZ (failover) database | zero-downtime AZ failover | not available — vendor single-instance only | infeasible |
  | Replace the accounting product | enables Multi-AZ | licence + data migration + change mgmt + risk | disproportionate — rejected |
  note: The chosen row is the AT1 cost-benefit centrepiece — the design must argue it, not just state it.
  image: none
- [BESPOKE] Cloud-service features that deliver reliability
  - The techniques the design leans on: Multi-AZ deployment, load-balancer health checks, automated database backups and snapshots, and cross-Region snapshot/DR copy (KE 9).
  - Express the design as a parameterised CloudFormation template — Region and environment as parameters — so the same design deploys repeatably (and to Melbourne for DR).
  - Choose the feature that meets the goal at least cost; each choice cites the goal it serves.
  image: none
  notes:
    The techniques slide — name the concrete cloud-service features the reliability design leans on, and
    introduce the parameterised template that carries the design to AT3.
    • First bullet: the techniques (KE 9) — Multi-AZ deployment, load-balancer health checks, automated
    database backups/snapshots, and cross-Region snapshot/DR copy. Tie each to the target from two slides
    back.
    • Second bullet: express the design as a PARAMETERISED CloudFormation template — Region and environment
    as parameters — so the same design deploys repeatably, and to Melbourne for DR. One template, many
    deploys.
    • Third bullet: choose the feature that meets the goal at LEAST cost; each choice cites the goal it
    serves. Traceability from feature back to goal.
    Misconception to pre-empt: "parameterised = more complex." No — parameters are what stop you writing the
    design twice for two Regions; the DR copy IS the same template with a different Region parameter.
    Question to pose: "Why parameterise Region instead of hard-coding Sydney?" (the Melbourne DR copy is the
    same template, Region-swapped — repeatable, not rewritten).
    UoC/AT1 tie: ICTCLD504 KE 9 (features/techniques to improve reliability) → AT1 Solution Design + KE
    appendix; the parameterised template is the seam to the AT3 build.
- [BESPOKE] The India residency slice
  - A light residency constraint: CERT-In-mandated logs and Companies-Act books-of-account must reside in Mumbai (`ap-south-1`); the main system stays in Sydney.
  - Design keeps the regulated data in-Region — the residency requirement is an input constraint on the design, not a bolt-on.
  - Note it as a scoped slice of the reliability/DR design, not a second architecture.
  image: none
  notes:
    Teach residency as an INPUT CONSTRAINT on the reliability/DR design — a scoped slice, not a second
    architecture. Keep it light; it's one constraint, not a whole new system.
    • First bullet: the constraint — CERT-In-mandated logs and Companies-Act books-of-account must reside in
    Mumbai (ap-south-1); the main system stays in Sydney.
    • Second bullet: the design keeps the regulated data IN-Region — residency is an input constraint the
    design is shaped around, not a bolt-on added at the end.
    • Third bullet: frame it as a scoped slice of the reliability/DR design (where the regulated data lives,
    and its DR), not a second architecture to design in full.
    Misconception to pre-empt: "residency means build a whole separate Indian system." No — it constrains
    WHERE specific regulated data (logs, books-of-account) sits; the rest of the design is unchanged.
    Question to pose: "Which data must stay in Mumbai, and which stays in Sydney — and how does that change
    the DR design?" (only the regulated slice is pinned to ap-south-1).
    UoC/AT1 tie: reinforces ICTCLD504 PC 2.3 (improve architecture jointly for security/reliability) — the
    residency constraint is part of the reliability/DR design in the AT1 Solution Design.
- [EX] Design the reliability improvements
  - For the practice vehicle (the website), design the reliability improvements to the Topic-1 goals across the app, data and DR tiers — you decide what each tier needs, to the goals and no further.
  - Argue ONE cost-benefit trade-off explicitly and show how each change meets a named goal. NB the website runs MySQL with no legacy single-instance constraint, so the data-tier call (e.g. whether to go Multi-AZ) is yours to justify — potentially the OPPOSITE call to Ledgerline's, reached by the same cost-benefit reasoning.
  timer: ~30 min
  image: none
  notes:
    Facilitation — the Section 1 practice; students design the reliability improvements for the practice
    vehicle, arguing one cost-benefit trade-off explicitly. The key teaching move: same REASONING, possibly
    the OPPOSITE call to Ledgerline.
    Tell students: "For the practice vehicle — the website — design the reliability improvements to your
    Topic-1 goals across the app, data and DR tiers. You decide what each tier needs — to the goals and no
    further — and you argue at least one cost-benefit trade-off out loud."
    Steps (put on the board):
    1. Design the app tier, the data tier and DR to your Topic-1 reliability goals.
    2. Pick ONE trade-off and argue it explicitly — cost vs the reliability it buys.
    3. Show how each change meets a NAMED goal.
    Must produce: a reliability design across the three tiers with one written cost-benefit argument, each
    change tied to a goal.
    Timing: ~30 min then discuss. Key point to surface: the website runs MySQL with NO legacy
    single-instance constraint, so the data-tier call (e.g. whether to go Multi-AZ) is theirs to justify —
    potentially the OPPOSITE decision to Ledgerline's, reached by the SAME cost-benefit reasoning. That's
    the learning, not a mistake.
    Where they get stuck: they copy Ledgerline's "reject Multi-AZ DB" verdict — remind them the constraint
    is different here, so re-run the reasoning, don't copy the answer.
    Share-back prompt: ask two students their data-tier call and WHY — expect different verdicts, same
    reasoning shape.
    No-leakage note: the website is the practice vehicle; AT1 assesses the reliability design on Ledgerline
    — comparable, not identical, and the DB constraint differs by design.

### C2 — Cloud design & migration principles
- Teaches: [ICTCLD504 KE 4] · [ICTCLD504 KE 5]
- Kicker: the principles under the improvement
- [PRIMER] Cloud design principles
  - Design for failure, loose coupling, statelessness, right-sizing, and automation over manual steps (KE 4).
  - Improve the architecture to these principles — they are why Multi-AZ and health checks belong in the design.
  - Simplest design that meets the goal wins; principles justify choices, they don't mandate maximums.
  image: none
  notes:
    Open Section 2 — the design PRINCIPLES that justify the reliability choices already made. Teach them as
    the "why" behind Multi-AZ and health checks, not as new features.
    • First bullet: the principles (KE 4) — design for failure, loose coupling, statelessness, right-sizing,
    and automation over manual steps. Give a one-line example of each.
    • Second bullet: improve the architecture TO these principles — they are why Multi-AZ and health checks
    belong in the design. Principles explain the choices.
    • Third bullet: the simplest design that meets the goal wins; principles justify choices, they don't
    mandate maximums. Same anti-gold-plating rule.
    Misconception to pre-empt: "'design for failure' means add every redundancy." No — it means assume
    components WILL fail and design so the system copes at the level the goal needs; it's a mindset, not a
    maximum.
    Question to pose: "'Design for failure' — how does it justify the Multi-AZ app tier but NOT a Multi-AZ
    database here?" (cope with AZ failure at the app tier; the DB copes via backup/restore + DR at
    acceptable cost).
    UoC/AT1 tie: ICTCLD504 KE 4 (design principles for cloud applications) → AT1 Solution Design KE appendix.
- [BESPOKE] Migrating the baseline to the improved architecture
  - Migration principles: move incrementally, keep the system serving, evidence each step, and be able to roll back (KE 5).
  - Sequence the improvement so the single-AZ baseline becomes the Multi-AZ + DR target without a big-bang cutover.
  - This is design-level here — the actual migration/build is AT3.
  image: none
  notes:
    Teach the MIGRATION principles — how you move the single-AZ baseline to the improved target without a
    big-bang cutover. Design-level here; the actual migration is AT3.
    • First bullet: the migration principles (KE 5) — move incrementally, keep the system serving, evidence
    each step, and be able to ROLL BACK. Say each as a rule.
    • Second bullet: sequence the improvement so single-AZ becomes Multi-AZ + DR without a big-bang cutover.
    It's a path, not a switch.
    • Third bullet: this is design-level HERE — the actual migration/build is AT3. Hold the depth ceiling.
    Misconception to pre-empt: "migration = turn off the old, turn on the new." No — you move incrementally
    and keep serving; the ability to roll back is a design requirement, not an afterthought.
    Question to pose: "Why sequence the migration instead of cutting over in one weekend?" (keep serving,
    evidence each step, roll back if a step fails — lower risk to a live accounting system).
    UoC/AT1 tie: ICTCLD504 KE 5 (migrating principles for cloud applications) → AT1 Solution Design KE
    appendix.
- [EX] Justify the design in principle
  - For your practice design, write the KE-appendix justification: name the cloud design principle behind each reliability choice and the migration approach that reaches it.
  timer: ~20 min
  image: none
  notes:
    Facilitation — the Section 2 practice; students write the KE-appendix justification for their practice
    reliability design — naming the principle behind each choice.
    Tell students: "For your practice design, write the KE-appendix justification: for each reliability
    choice, name the cloud design principle behind it, and describe the migration approach that reaches the
    improved architecture."
    Steps (put on the board):
    1. List each reliability choice from your Section-1 practice design.
    2. Against each, name the design principle that justifies it (design for failure, loose coupling,
    right-sizing, automation…).
    3. Describe the migration approach — incremental, keep-serving, roll-back — that reaches the target.
    Must produce: a short KE-appendix passage linking each choice to a principle plus a migration approach.
    Timing: ~20 min then discuss. Where they get stuck: they restate the choice instead of naming the
    PRINCIPLE behind it — circulate and ask "which principle makes that the right move?"
    Share-back prompt: take one choice and ask the room which principle best justifies it.
    No-leakage note: the website is the practice vehicle; the AT1 KE appendix is written for Ledgerline —
    comparable, not identical.

### C3 — Security layers underpinning the design
- Teaches: [ICTCLD504 KE 8]
- Kicker: the improvement stays secure
- [BESPOKE] Security layers that keep the design secure
  - The tools and uses of security layers in cloud services: network isolation, security groups, IAM least-privilege, and encryption as the baseline (KE 8).
  - Encryption is assumed on by default (at rest and in transit) — including the cross-Region DR copy and the residency data.
  - Reliability changes must not weaken security — each new tier (Multi-AZ app, DR copy) inherits the security layers, not bypasses them.
  image: none
  notes:
    Section 3 — the security layers that keep the improved design secure. Short section; the message is that
    reliability changes must INHERIT security, never bypass it.
    • First bullet: the tools/uses of security layers (KE 8) — network isolation, security groups, IAM
    least-privilege, and encryption as the baseline. Name the layers.
    • Second bullet: encryption is assumed ON by default — at rest and in transit — INCLUDING the
    cross-Region DR copy and the residency data. Nothing regulated travels or rests unencrypted.
    • Third bullet: reliability changes must not weaken security — each new tier (Multi-AZ app, DR copy)
    inherits the security layers, not bypasses them.
    Misconception to pre-empt: "the DR copy is just a backup, so it's lower-security." No — a DR copy of
    regulated financial data carries the SAME encryption and access controls as the primary; a weaker copy
    is the breach.
    Question to pose: "You add a cross-Region DR copy — what security must travel with it?" (encryption in
    transit + at rest, IAM controls — the DR copy inherits the primary's security layers).
    UoC/AT1 tie: ICTCLD504 KE 8 (tools & uses of security layers in cloud services) → AT1 Solution Design KE
    appendix; security is optimised jointly with reliability (PC 2.3).

### Close
- [TAKEAWAYS] Topic 2 · Key takeaways
  - Reliability = Multi-AZ app tier + DB backup/restore + cross-Region DR to Melbourne (data onshore).
  - The centrepiece: reject a Multi-AZ database — the DB is single-AZ by a cost-benefit call, argued explicitly.
  - Justify every reliability choice against a goal and against cost; don't over-engineer.
  - Cloud design/migration principles and encryption-baseline security layers underpin the whole improvement.
  image: none
- [BESPOKE] Next: Topic 3 — designing for scalability
  - You've designed the reliability half of the Solution Design; next you design the scalability half and the four resource components.
  - Bring this design — scalability builds on the same reviewed architecture.
  image: none

## Build notes
~14 slides. DESIGN depth — no build (AT3 owns the implementation; the DB tier is design-only). Exercises run on the practice vehicle: design the reliability improvements with one explicit cost-benefit trade-off, then write the KE-appendix justification. One generated architecture diagram (`diagram reliability-target`); one decorative `gen` image (opener hero). The Multi-AZ-database cost-benefit rejection is the centrepiece (C1 + the TABLE).

## Changelog
- 2026-07-02 — authored to full content from coverage.md (Step-4 artefact).
