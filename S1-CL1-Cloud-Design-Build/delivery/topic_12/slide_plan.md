# Topic 12 HA design — Slide plan
> **Covers:** Topic 12 — see coverage.md
> **Subtitle:** Design the upgrade — review the baseline, design out its single points of failure, and document it

## Slides

### Opener
- [BESPOKE] Now you design it
  - Topic 11 gave you the concepts; Topic 12 is where you produce an HA design.
  - You design the upgrade yourself — the baseline and the HA requirements are your inputs, not a finished answer.
  - Three moves: review the baseline + find its SPOFs → design them out → document the design and plan the work.
  - Topic 13 then implements and simulates what you design here.
  kicker: AT3 Part A skills
  image: none
  notes:
    Frame this as the map for the whole Topic — set the shift, don't teach method yet.
    • Topic 11 gave the concepts (SPOF, RTO/RPO, the toolkit); Topic 12 is where they PRODUCE an
    HA design. This is the doing, not the knowing.
    • Stress the bolded edge: the baseline and the HA requirements are their INPUTS — the finished
    design is what they build, we don't hand it out.
    • Three moves, map them to the three sections: review the baseline + find its SPOFs → design
    them out → document the design and plan the work.
    • Topic 13 then implements and simulates exactly what they design here — so a sloppy design
    now costs them next week.
    Misconception to pre-empt: "we'll be given an HA design to copy" — that's AT2 (design supplied →
    you build). AT3 flips it: the design IS the deliverable (502 element 3).
    Question to pose: "How is this Topic different from AT2 — who does the designing this time?"
    UoC/AT tie: develops ICTCLD502 elements 2–3, assessed in AT3 Part A (the HA Design document).

### C1 — Review the baseline & find its SPOFs
- Teaches: [ICTCLD502 PC 2.1] · [ICTCLD502 PC 2.2] · [ICTCLD502 PC 2.3] · [ICTCLD502 PC 2.4] · [ICTCLD502 PC 2.5] · [ICTCLD502 KE 4, 8]
- Kicker: evaluate before you change
- [BESPOKE] Review the architecture
  - Start by understanding what's there: the multi-tier shape — presentation / logic / data (web / app / database).
  - Each tier can be built, scaled and diagnosed separately.
  - Review the deployed single-AZ baseline before you change anything.
  kicker: ICTCLD502 · Evaluating availability
  image: none
  notes:
    Open C1 — the rule is evaluate before you change. Keep it to orienting on the shape.
    • Start by understanding what's there: the multi-tier shape — presentation / logic / data
    (web / app / database). Name the tiers on the baseline.
    • Each tier can be built, scaled and diagnosed separately — that's what lets them reason about
    one tier's failure at a time.
    • Bolded line: review the deployed single-AZ baseline BEFORE changing anything — you can't
    design out a weakness you haven't found.
    Misconception to pre-empt: keen students want to jump straight to "add a second AZ." Reviewing
    feels like wasted time — but a fix aimed at the wrong SPOF is wasted design.
    Question to pose: "Why review a system someone else already built before you improve it?"
    UoC/AT tie: ICTCLD502 PC 2.1 — review a multi-tier architecture and identify HA requirements;
    this is the AT3 Part A "evaluate availability" skill.
- [BESPOKE] Identify the single points of failure
  - Walk the architecture and mark every component whose failure stops the whole service.
  - In a single-AZ cloud build that's the AZ itself, the one database, the one running instance, the one NAT.
  - A network diagram makes the SPOFs visible — find them before you design the fix.
  kicker: ICTCLD502 · Design HA S10
  image: diagram identify-spofs
  notes:
    The core C1 skill — make the SPOFs visible on the diagram. Work off the picture, not the prose.
    • Walk the architecture and mark every component whose failure stops the WHOLE service — that's
    the test for a SPOF.
    • In a single-AZ cloud build (bolded), the SPOFs are the AZ itself, the one database, the one
    running instance, the one NAT. Point at each on the diagram.
    • A network diagram makes them visible — find them all before designing any fix.
    Misconception to pre-empt: "we're in the cloud, so it's already redundant." No — a single-AZ
    build is full of SPOFs; the cloud gives you the tools for HA, it doesn't grant HA for free.
    Question to pose: point at a box — "if this one dies, does Ledgerline stay up? Then it's a SPOF."
    UoC/AT tie: ICTCLD502 PC 2.2 — identify single points of failure (AT3 Part A).
    [Diagram-led slide — drive the SPOF hunt off the network diagram.]
- [BESPOKE] Estimate the recovery objectives
  - Estimate the baseline's RPO from the backup interval, and its RTO from recovery-per-tier + testing.
  - Worked example: 15-min backups → RPO 15 min; 30 min × 3 tiers + 1 h test → RTO 2.5 h.
  - Flag components that scale vertically (they carry downtime) and the availability impact.
  kicker: ICTCLD502 · Evaluating availability S8
  image: none
  notes:
    Put numbers on the baseline's resilience — this quantifies how bad the SPOFs are.
    • RPO comes from the backup interval (how much data you could lose); RTO from recovery-per-tier
    plus testing (how long to get back up).
    • Walk the worked example slowly: 15-min backups → RPO 15 min; 30 min × 3 tiers + 1 h test →
    RTO 2.5 h. Make them see where each number comes from.
    • Bolded line: flag components that scale VERTICALLY — they carry downtime (you resize by
    stopping/restarting), which hurts availability.
    Misconception to pre-empt: RPO and RTO get conflated. RPO = data lost; RTO = time to restore —
    different clocks. And RTO is not just "the backup frequency."
    Question to pose: "If Ledgerline backs up hourly, what's the most data YAT could lose in a
    failure?" (that's the RPO).
    UoC/AT tie: ICTCLD502 PC 2.3 / PC 2.4 — estimate recovery objectives + vertical-scaling impact.
- [EX] Review the Accounting baseline
  - Take the supplied single-AZ Accounting baseline and evaluate its availability:
    - list its single points of failure (AZ · database · running instance · NAT)
    - estimate its RPO and RTO, and where they fall short of the HA requirement
    - note the components that scale vertically and the downtime that implies
  - Document your findings — they drive the design.
  timer: ~20 min
  image: none
  notes:
    Facilitation — the first C1 practice. Analytical, no AWS console; they work from the supplied
    baseline design on paper/screen.
    Tell students: "You've been handed the single-AZ Accounting baseline. Before you can improve
    it, evaluate its availability — find where it's fragile and put numbers on it."
    Steps (put on the board):
    1. List its single points of failure (AZ · database · running instance · NAT).
    2. Estimate its RPO and RTO, and note where they fall short of the HA requirement.
    3. Note which components scale vertically and the downtime that implies.
    Must produce: a short written availability review — the SPOF list, the RPO/RTO estimate with
    the shortfall, and the vertical-scaling note. These findings drive the design next section.
    Timing: ~20 min then share. Where they get stuck: they list generic "the server could fail"
    rather than naming the specific single-AZ SPOFs — point them back to the four on the diagram;
    and some skip the RTO reasoning — remind them it's per-tier recovery + testing.
    Share-back prompt: "Which SPOF worried you most, and what's your RTO estimate?"
    No-leakage note: Ledgerline/Accounting is the PRACTICE baseline; AT3 assesses the SAME skill on
    the LMS baseline (design the LMS HA upgrade) — comparable, not identical. Keep them on Accounting.
- [TAKEAWAYS] Section 1 · Review & SPOFs
  - Understand the multi-tier baseline before you change it.
  - Identify every single point of failure — a diagram makes them visible.
  - Estimate the baseline's RPO/RTO and flag vertical-scaling components.
  - Your findings are the input to the design.
  image: none

### C2 — Design the HA-equivalent
- Teaches: [ICTCLD502 PC 3.1] · [ICTCLD502 PC 3.2] · [ICTCLD502 PC 3.3] · [ICTCLD502 PC 3.4] · [ICTCLD502 KE 4, 8]
- Kicker: remove every SPOF
- [BESPOKE] Design redundancy — remove the SPoFs
  - Using the cloud doesn't make you highly available — you design redundancy.
  - For each SPOF, add redundancy across compute, storage and network so no single failure stops the service.
  - The goal: an equivalent architecture that keeps running when one component — or one AZ — fails.
  kicker: ICTCLD502 · Design HA S9
  image: none
  notes:
    Open C2 — the mindset flip: HA is something you DESIGN, not something the cloud gives you.
    • Using the cloud doesn't make you highly available — you design the redundancy in.
    • Bolded line: for each SPOF, add redundancy across compute, storage and network so no single
    failure stops the service.
    • The goal: an EQUIVALENT architecture — same function as the baseline — that keeps running when
    one component, or one whole AZ, fails.
    Misconception to pre-empt: "we moved it to AWS, so it's now highly available." No — a single-AZ
    AWS build is no more available than an on-prem one; availability is a design property.
    Question to pose: "What makes a cloud build highly available — the cloud, or your design?"
    UoC/AT tie: ICTCLD502 PC 3.1 / PC 3.2 — design the HA-equivalent, remove SPOFs (AT3 Part A).
- [BESPOKE] The cross-AZ HA architecture
  - Spread the workload across two Availability Zones: load balancing across AZs → instances (ASG) across AZs → a Multi-AZ database.
  - The load balancer routes only to healthy targets; the ASG keeps capacity in each AZ; the database fails over automatically.
  - Redundant egress (a NAT per AZ) keeps outbound working if an AZ is lost.
  kicker: ACA M10 S41 · ICTCLD502 · Design HA S7–S8
  image: diagram cross-az-ha-architecture
  notes:
    The reference pattern they design toward — from ACA M10. Assemble it off the diagram tier by tier.
    • Spread the workload across TWO Availability Zones: load balancing across AZs → instances (an
    ASG) across AZs → a Multi-AZ database.
    • Bolded line: the LB routes only to HEALTHY targets; the ASG keeps capacity in each AZ; the
    database fails over automatically. Each mechanism removes a specific SPOF.
    • Redundant egress — a NAT per AZ — keeps outbound working if an AZ is lost.
    Misconception to pre-empt: "two AZs means two copies I fail over by hand." No — the managed
    services (ALB health checks, ASG, Multi-AZ RDS) do the failover; that's the point of using them.
    Question to pose: "If one whole AZ vanishes right now, which of these pieces keeps serving?"
    UoC/AT tie: ICTCLD502 KE 4 / KE 8 — redundancy across AZs, LB + autoscaling, Multi-AZ.
    [Diagram-led slide — build the cross-AZ topology visually.]
- [BESPOKE] Remove each SPOF — the mapping
  - Single Availability Zone → a second AZ with mirrored subnets.
  - Single running instance → an Auto Scaling group spread across both AZs.
  - Single database → a Multi-AZ database with a synchronous standby + automatic failover.
  - Single NAT gateway → a NAT gateway per AZ.
  kicker: design method
  image: none
  notes:
    The heart of the design — a systematic SPOF→fix mapping. Every fix must trace to a SPOF they found.
    • Single Availability Zone → a second AZ with mirrored subnets.
    • Single running instance → an Auto Scaling group spread across both AZs.
    • Single database → a Multi-AZ database with a synchronous standby + automatic failover.
    • Single NAT gateway (bolded) → a NAT gateway per AZ.
    • Tie it back: these are exactly the four SPOFs from C1 — the design is disciplined, not creative
    for its own sake.
    Misconception to pre-empt: students add redundancy scattershot ("more of everything"). Stress
    each addition must remove a NAMED SPOF; redundancy with no SPOF behind it is just cost.
    Question to pose: "Take each SPOF you listed this morning — what's the single fix for it?"
    UoC/AT tie: ICTCLD502 PC 3.2 — identify and remove single points of failure as required.
- [BESPOKE] Re-estimate the recovery objectives
  - Re-estimate RPO/RTO for the HA design — per component and overall.
  - RPO is unchanged (backups); RTO drops to minutes for an AZ or instance failure via automatic failover.
  - Check the numbers now meet the HA requirement — and note what remains (the single Region).
  kicker: ICTCLD502 · Design HA S11
  image: none
  notes:
    Prove the design actually improves the numbers — and be honest about what it doesn't fix.
    • Re-estimate RPO/RTO for the HA design, per component and overall.
    • Bolded line: RPO is unchanged (still driven by backups); RTO drops to MINUTES for an AZ or
    instance failure, because failover is now automatic.
    • Check the numbers meet the HA requirement — and note what REMAINS: the single Region.
    Misconception to pre-empt: "HA fixes everything." It doesn't — a single-Region design still
    falls to a Region-wide event; that's DR territory (CL2), explicitly out of scope here.
    Question to pose: "What does the second AZ do to your RTO — and what does it NOT protect against?"
    (the single Region.)
    UoC/AT tie: ICTCLD502 PC 3.3 / PC 3.4 — re-estimate recovery objectives for the HA design.
- [EX] Design the HA-equivalent for Accounting
  - Design the upgrade for the baseline you reviewed:
    - design out each SPOF using the mapping (2 AZs · cross-AZ ASG · Multi-AZ DB · NAT per AZ)
    - sketch the cross-AZ topology
    - re-estimate the recovery objectives and confirm they meet the requirement
  timer: ~25 min
  image: none
  notes:
    Facilitation — the C2 practice. Analytical design work on the baseline they reviewed in C1.
    Tell students: "You've evaluated the Accounting baseline and you have its SPOFs. Now design the
    upgrade — an HA-equivalent that removes every one of them."
    Steps (put on the board):
    1. Design out each SPOF using the mapping (2 AZs · cross-AZ ASG · Multi-AZ DB · NAT per AZ).
    2. Sketch the cross-AZ topology.
    3. Re-estimate the recovery objectives and confirm they meet the requirement.
    Must produce: a cross-AZ topology sketch + a SPOF→fix mapping + the re-estimated RPO/RTO
    against the requirement. This is the design core of the C3 document.
    Timing: ~25 min then share. Where they get stuck: they redesign from scratch or invent new tiers
    — pull them back to hardening the SAME architecture; and some forget the NAT-per-AZ / redundant
    egress — check every SPOF from C1 has a matching fix.
    Share-back prompt: "Show your topology — which SPOF does each new element remove?"
    No-leakage note: this is practice on the Accounting baseline; AT3 assesses the same design skill
    on the LMS baseline — comparable, not identical. Don't let LMS specifics leak in either direction.
- [TAKEAWAYS] Section 2 · Design
  - HA isn't automatic — you design redundancy across the tiers.
  - Spread across two AZs: LB + ASG across AZs, Multi-AZ database, redundant NAT.
  - Map each SPOF to its fix — that's the HA design.
  - Re-estimate recovery objectives and check they meet the requirement.
  image: none

### C3 — Document the design & plan the work
- Teaches: [ICTCLD502 PC 2.5] · [ICTCLD502 PC 3.5] · [ICTCLD502 KE 4, 8]
- Kicker: the deliverable
- [BESPOKE] What an HA design documents
  - Architecture diagram — the components, the redundancy, the connections between tiers.
  - Service list — the AWS services used and each one's purpose.
  - SPoF analysis — the SPOFs identified, and the solution implemented for each.
  - RTO/RPO table — recovery objectives per component and overall; scaling plans — what scales, how, and the trigger.
  kicker: ICTCLD502 · Design HA S14
  image: none
  notes:
    Open C3 — the five-part documentation framework (502). This is the shape of the AT3 deliverable.
    • Architecture diagram — the components, the redundancy, the connections between tiers.
    • Service list — the AWS services used and each one's purpose.
    • SPoF analysis — the SPOFs identified, and the solution implemented for each.
    • Bolded line: RTO/RPO table (recovery objectives per component and overall) + scaling plans
    (what scales, how, and the trigger).
    Misconception to pre-empt: "the diagram IS the design document." No — the diagram is ONE of five
    parts; a diagram alone hides the reasoning, the objectives and the scaling story.
    Question to pose: "If you hand a client only a diagram, what can't they see about your design?"
    (the SPOF reasoning, the recovery numbers, what scales.)
    UoC/AT tie: ICTCLD502 PC 2.5 / PC 3.5 — document the review findings and the design (AT3 Part A).
- [BESPOKE] Draw the HA topology
  - A logical diagram showing the two AZs, the redundancy, the tiers and their connections.
  - Focus on the key details — boundaries, resource types, connectivity — not every setting.
  - Use the scenario's network-diagram conventions (the same draw.io style as the baseline diagram).
  kicker: ICTCLD502 · Evaluating availability S12–S14
  image: none
  notes:
    How to draw the diagram WELL — it's the centrepiece of the document, so pitch the altitude right.
    • A logical diagram showing the two AZs, the redundancy, the tiers and their connections.
    • Focus on the key details — boundaries, resource types, connectivity — NOT every setting.
    • Bolded line: use the scenario's network-diagram conventions — the same draw.io style as the
    baseline diagram (consistency reads as professional).
    Misconception to pre-empt: over-detailing — students try to draw every port, subnet CIDR and
    instance setting. This is a LOGICAL diagram, not a config dump; too much detail hides the design.
    Question to pose: "What's the right level of detail — enough to see the redundancy, not so much
    it becomes a settings list?"
    UoC/AT tie: ICTCLD502 PC 3.5 — document the architecture design; reuses the Topic 7 diagram
    conventions.
- [BESPOKE] Plan the implementation & simulation
  - Sequencing — the order to harden the running baseline in place, without an outage (add the AZ, extend ASG/ALB, convert the DB to Multi-AZ).
  - Simulation plan — the failures and resizes you'll run to prove fault tolerance (AZ/instance failure, database failover, resize under load).
  - This plan is what Topic 13 executes.
  kicker: sets up Topic 13
  image: none
  notes:
    The bridge to Topic 13 — the plan they'll execute next week. Keep the two parts distinct.
    • Sequencing — the ORDER to harden the running baseline in place, without an outage (add the AZ,
    extend the ASG/ALB across it, convert the DB to Multi-AZ). In place, not a rebuild.
    • Bolded line: the simulation plan — the failures and resizes they'll run to PROVE fault
    tolerance (AZ/instance failure, database failover, resize under load).
    • This plan is exactly what Topic 13 executes — so it has to be concrete and ordered.
    Misconception to pre-empt: "we'll rebuild it as HA from scratch." No — you harden the RUNNING
    baseline in place, in an order that never takes Ledgerline down.
    Question to pose: "How do you add a second AZ to a live system without an outage — what goes first?"
    UoC/AT tie: AT3 Part A → B — the sequencing + simulation planning that sets up Topic 13.
- [EX] Produce your HA design document
  - Assemble the HA design for the Accounting upgrade:
    - architecture diagram · service list · SPoF analysis + solutions · RTO/RPO table · scaling plans
    - the implementation sequencing + the simulation plan
  - This is the deliverable — the design you'll implement next.
  timer: ~30 min
  image: none
  notes:
    Facilitation — the C3 practice. This assembles everything from C1–C2 into the deliverable.
    Tell students: "Assemble your HA design for the Accounting upgrade into one document — this is
    the shape of the deliverable you'll produce for real in AT3."
    Steps (put on the board):
    1. Architecture diagram · service list · SPoF analysis + solutions · RTO/RPO table · scaling plans.
    2. Add the implementation sequencing and the simulation plan.
    Must produce: a single HA design document with all five framework parts PLUS the sequencing and
    simulation plan — complete enough that Topic 13 could implement straight from it.
    Timing: ~30 min then share. Where they get stuck: a strong diagram but a thin/absent SPoF
    analysis or RTO/RPO table — remind them all five parts are required, the diagram isn't the whole
    document; and vague sequencing ("just set it up") — push for a concrete, no-outage order.
    Share-back prompt: "Swap documents — could you implement someone else's design from it as written?"
    No-leakage note: practice document on the Accounting baseline; AT3 requires the same document for
    the LMS — comparable, not identical. This is a rehearsal of the AT3 Part A deliverable, not it.
- [TAKEAWAYS] Section 3 · Document & plan
  - An HA design = diagram · service list · SPoF analysis · RTO/RPO table · scaling plans.
  - Draw the topology clearly — two AZs, redundancy, tiers, connections.
  - Plan the sequencing (harden in place, no outage) and the simulations.
  - The documented design is the Part-A deliverable.
  image: none
- [TAKEAWAYS] Topic 12 · Key takeaways
  - Review the baseline and find its single points of failure.
  - Design them out across two AZs (LB + ASG + Multi-AZ DB + redundant NAT).
  - Re-estimate recovery objectives against the requirement.
  - Document the design (five parts) and plan the implementation + simulations.
  - You produce the design — next you build it.
  image: none

### Close
- [BESPOKE] Next: Topic 13 — HA implementation & simulation
  - Implement your HA design on the running baseline, then simulate failures and resizes to prove it's fault tolerant.
  - Bring your design document and your simulation plan.
  image: none
