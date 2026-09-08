# Topic 12 Designing the upgrade — Slide plan
> **Covers:** Topic 12 — see coverage.md
> **STATUS: DRAFT — redrafted 2026-08-28 from the AT3 practice workbook, Part A tasks 7–12. Teacher
> `notes:` not yet authored. `coverage.md` not yet reconciled.**

## Depth ceiling
Design the change tier by tier, across two availability zones. Multi-region and full disaster recovery
are CL2 and stay out.

**Answer discipline:** every task in this topic has a design answer the student must reach themselves.
These slides teach the mechanisms and the questions to ask of each tier. They must not state which
mechanism this environment needs, and in particular must not resolve tasks 9 or 11 — one of which may
correctly be "nothing to do", and the other of which may correctly be "accept the risk and write it down".

## Teaching source
Bespoke ICTCLD502 (designing for high availability) with AWS support for the cross-zone pattern and
standby databases (ACA M10).

## AWS pin table
ACA M10 S19–S24, S41.

## Slides

### Opener
- [BESPOKE] Now you design it
  - You have the targets and you have the gap. Nobody is going to hand you the answer.
  - You design the change tier by tier: the network, the application tier, the balancer, the data tier, the outbound path, the monitoring.
  - Each tier gets the same two questions: what is actually there now, and what does this target require of it?
  - Sometimes the answer is that nothing needs to change. That is a design decision too, and it has to be argued.
  kicker: the design is the deliverable
  image: none

### C1 — Redundancy, and where it goes
- Teaches: [ICTCLD502 PC 3.1] · [ICTCLD502 PE 1] · [ICTCLD502 PE 2]
- Kicker: the network and the servers
- [BESPOKE] Availability is designed, not granted
  - Running on a cloud platform does not make a system highly available.
  - The platform gives you the means to build redundancy. Whether you have any depends on how you used them.
  - Every piece of redundancy you add should remove a weakness you actually named. Redundancy with nothing behind it is just cost.
  kicker: the platform supplies tools, not outcomes
  image: none
- [BESPOKE] The mechanisms available to you
  - Placement across zones — run the same thing in more than one location.
  - Load balancing — spread traffic, and route only to what is healthy.
  - A scaling group across zones — hold healthy capacity in each location, and replace what dies.
  - A standby database — a synchronised copy in another location, promoted automatically.
  - Which of these this environment needs is your call to make, tier by tier.
  kicker: four tools; your judgement
  image: none
- [BESPOKE] Designing network capacity for a second location
  - A server can only run somewhere it has a subnet to run in.
  - Subnets that exist for other purposes are not interchangeable — a subnet belongs to a tier as well as to a location.
  - Follow the addressing and naming already in use. A design that breaks the existing convention reads as a mistake to whoever builds it.
  kicker: a subnet belongs to a tier and a place
  image: none
- [BESPOKE] Designing the application tier
  - A scaling group can only launch into the subnets it is given. That setting is what makes a second location reachable at all; everything else depends on it.
  - Then the capacity numbers. Work them backwards from the failure: a location is lost, and you still need capacity serving. What is the smallest minimum that guarantees it?
  - Minimum is about surviving. Maximum is about load. They answer different questions, and the busiest period is what sets the second one.
  kicker: work the minimum backwards from the failure
  image: none
- [BESPOKE] What your diagram has to show
  - A logical diagram, not a settings dump. Someone should be able to build from it without asking you a question, and should not have to read every value to see the shape.
  - What goes on it:
    - the zone boundaries, so it is obvious what is in which place
    - one box per subnet, labelled with its name, its range and its zone
    - the resources sitting inside the subnet they actually run in
    - lines only where traffic really flows
  - What stays off it: instance types, thresholds, rule-by-rule settings. Those live in your tables.
  kicker: enough to build from, not everything you know
  image: none
- [BESPOKE] A worked example — a different client
  - This is another client's environment, drawn the way yours should be drawn.
  - It is not your system and not your answer. Copy the shapes and the labelling, not the content.
  - Work across it: zone boundary → subnet boxes → what sits in each → the connections between them.
  - Yours should be recognisably the same kind of drawing, with your environment's details in it.
  kicker: same shapes, your details
  image: diagram example-topology-other-client
- [EX] Design the network and the application tier
  - Workbook — tasks 7 and 8. Draw your diagram to match the example's conventions.
  - Record the subnet or subnets you are adding and where, sketch the environment you are aiming for, then design the scaling group's subnets and capacity, with a reason for each number.
  timer: ~35 min
  image: none
  notes:
    Activity = practice workbook tasks 7–8. Task 7's exemplar row describes a subnet that already
    exists — make sure they read it as a pattern, not as their answer.
    Do not confirm or deny their capacity numbers; the workbook's considerations lead them there.
- [TAKEAWAYS] Section 1 · Network and compute
  - The platform gives you tools; the redundancy is yours to design.
  - Every addition should remove a weakness you named.
  - A scaling group reaches only the subnets it is given.
  - Minimum is about survival; maximum is about load.
  image: none

### C2 — Check before you design
- Teaches: [ICTCLD502 PC 3.1]
- Kicker: what is already there
- [BESPOKE] The most expensive design error
  - It is not designing the wrong thing. It is designing something that already exists.
  - It wastes the client's money, and it tells whoever reads your design that you did not look.
  - Before you design any tier, go back to the description of the current environment and read what is already true of it.
  kicker: read it before you draw it
  image: none
- [BESPOKE] "Nothing to do" is a real answer
  - If a tier already meets the requirement, the correct design decision is to leave it alone.
  - But it only counts if you say so and say why. Silence reads as an oversight.
  - Watch for the reflex answer. "Make it highly available" is what everyone writes; whether there is anything left to make is a different question.
  - There is a related question worth asking of every tier: when something new appears, who connects it up — you, or something already running?
  kicker: say it, and say why
  image: none
- [EX] Design the load balancer
  - Workbook — task 9.
  - Decide what your design does about the load balancer, and record why — checking what is already there before you answer.
  timer: ~15 min
  image: none
  notes:
    Activity = practice workbook task 9. This is a deliberate trap and it only works if it is left
    intact — do not hint at the answer, in either direction.
    Students who write a change without checking the current-state table have failed the actual test;
    let the share-back surface that.
- [TAKEAWAYS] Section 2 · Checking first
  - Designing something that already exists is the expensive error.
  - "No change needed, because…" is a complete answer; silence is not.
  image: none

### C3 — The data tier
- Teaches: [ICTCLD502 PC 3.1] · [ICTCLD502 PC 3.3] · [ICTCLD502 PE 1]
- Kicker: the worst numbers you found
- [BESPOKE] A standby is not a backup
  - A standby is a synchronised copy that can take over. It addresses losing the instance or its location, and it acts on its own.
  - A backup is a point-in-time copy. It addresses the data itself being wrong — a bad run, a deletion — which failing over to a synchronised copy of the same bad data does not fix.
  - They solve different problems and answer different numbers. Most designs need both.
  kicker: different problems, different numbers
  image: none
- [BESPOKE] What automatic failover changes
  - A standby that is promoted automatically turns a recovery measured in hours into one measured in minutes or less.
  - It changes your recovery time. It does not change how much data you could lose — that is still the backup question.
  - The application connects to the database by name, so when the standby takes over nothing has to be reconfigured. That is why the recovery is fast.
  kicker: it moves one number, not both
  image: diagram multi-az-rds
- [EX] Design the data tier
  - Workbook — task 10.
  - Design the change to the component with the worst recovery numbers in your review, and state what it gives you that the current configuration does not.
  timer: ~20 min
  image: none
  notes:
    Activity = practice workbook task 10. The exemplar row deliberately covers retention rather than
    the availability setting — the substantive decision is theirs. Watch for students who change the
    backup setting and think they have answered it.
- [TAKEAWAYS] Section 3 · The data tier
  - A standby covers losing the instance; a backup covers the data being wrong.
  - Automatic failover moves your recovery time, not your data loss.
  - Connecting by name is what makes failover invisible.
  image: none

### C4 — The outbound path
- Teaches: [ICTCLD502 PC 3.1] · [ICTCLD502 PC 3.2]
- Kicker: consistency, or a documented risk
- [BESPOKE] The tier people forget
  - Servers in a new location still need whatever they use to reach out — and whatever that is, it lives somewhere.
  - A gateway is only half of it. A subnet with no route table of its own falls back to a default with no path out at all, so the route is what actually sends traffic anywhere.
  kicker: the gateway and the route
  image: none
- [BESPOKE] Accepting a risk is a design position
  - Redundancy costs money, and a client with a budget is entitled to weigh it.
  - Accepting a risk deliberately — naming what breaks, and when — is a legitimate engineering answer.
  - An accepted risk you wrote down is a design position. The same risk unmentioned is an oversight. The difference is only the writing down.
  - Consistency matters too: if you have designed around losing a location everywhere else, leaving one tier depending on it is a choice you have to be able to defend.
  kicker: written down, or an oversight
  image: none
- [EX] Design the outbound path
  - Workbook — task 11.
  - Design what the servers in the new location use to reach out, and be explicit about whether you are removing the risk or accepting it.
  timer: ~20 min
  image: none
  notes:
    Activity = practice workbook task 11. Both answers are creditable. Do not steer.
    What is not creditable is not addressing it, or removing the risk without noticing there was a cost.
- [TAKEAWAYS] Section 4 · The outbound path
  - A new subnet needs a route, not just a gateway.
  - Accepting a documented risk is a design position; an unmentioned one is an oversight.
  image: none

### C5 — Monitoring the thing you designed
- Teaches: [ICTCLD502 PC 3.1] · [ICTCLD502 PE 5]
- Kicker: would anything tell you?
- [BESPOKE] The alarms you have watch the old shape
  - The monitoring built with the original platform answers the questions that mattered then.
  - After your change, a whole location can be lost and the service can keep running. That is the design working — and it means nothing obvious goes wrong.
  - So ask of each existing alarm: if this happened at 2am on a Sunday, would anything tell me?
  kicker: success can be silent
  image: none
- [BESPOKE] What makes an alarm worth having
  - An alarm needs a metric, a threshold, and a failure it would actually catch.
  - Watch out for metrics that aggregate across the thing you are trying to distinguish — a total that stays healthy tells you nothing about where the health is.
  - For each alarm you design, finish this sentence: "this fires when ___, which means ___ has happened." If you cannot, the threshold is a guess.
  kicker: finish the sentence
  image: none
- [EX] Design the monitoring
  - Workbook — task 12.
  - Design the monitoring that would tell you about the failures your new design is meant to survive, and say what each alarm detects.
  timer: ~20 min
  image: none
  notes:
    Activity = practice workbook task 12. The exemplar is the alarm that already exists, written in
    the table's own terms — its last sentence names the opening their alarms have to close.
    Do not name the metrics; the workbook's considerations lead there.
- [TAKEAWAYS] Topic 12 · Key takeaways
  - Redundancy is designed, and each piece should remove a named weakness.
  - Check what exists before designing a change to it.
  - A standby moves recovery time; backups cover the data being wrong.
  - An accepted risk must be written down to count.
  - After a successful design, failures get quieter — design the monitoring for that.
  image: none

### Close
- [BESPOKE] Next — checking your own work
  - You have a design. You do not yet know whether it hangs together, or whether it closes the gap you measured.
  - Next: check it against your own review, then plan how you will actually apply it.
  image: none

## Build notes
~21 slides. Five activities, mapping to practice workbook tasks 7–8 · 9 · 10 · 11 · 12.
`multi-az-rds` diagram moves in from `topic_11/diagrams/`. The `cross-az-ha-architecture` and
`identify-spofs` diagrams currently in `topic_12/diagrams/` are **not used** by this plan — both draw
the finished answer, which is the student's to produce. `coverage.md` needs reconciling.

**Asset to author: `example-topology-other-client`.** A worked network diagram the students copy the
conventions of, per the "same shapes, your details" model. Two constraints on it, or it hands over
Part A:
- it is a **different client's system**, not Ledgerline and not the LMS;
- its component mix must **exclude the pieces the design traps hang on** — no outbound-path/NAT
  arrangement (task 11 is a judgement call about exactly that) and no load-balancer-across-zones
  decision (task 9 tests whether they check what already exists). Show zone boundaries, subnet
  boxes, tiers and connections; leave those two out.
**Leakage guard:** no slide names a specific weakness, a specific fix, or resolves tasks 9 or 11.

## Changelog
- 2026-08-28 — redrafted from the AT3 practice workbook; the SPOF→fix mapping slide and the finished
  cross-zone topology diagram removed (both answered the tasks), one activity per design task added.
