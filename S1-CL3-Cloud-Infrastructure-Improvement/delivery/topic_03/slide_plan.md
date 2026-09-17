# Topic 03 Designing the improvements: security, reliability, cost — Slide plan
> **Covers:** Topic 03 — see coverage.md
> **Subtitle:** Design the security, reliability, scalability and cost improvements — and argue the cost-benefit case
> **STATUS: DRAFT — redrafted 2026-09-08 from the AT1 practice workbook, tasks 10–13. Re-cut: carries
> the old Topic 2's reliability design, in the workbook's order (security → reliability → cost).**

## Depth ceiling
DESIGN — the improvement passes of AT1: security, reliability and scalability, cost optimisation and
monitoring, then the cost-benefit justification. On paper, to the goals and metrics from Topics 1–2;
the build is AT3. The DB tier stays design-level (the lab role denies rds:ModifyDBInstance).

**Answer discipline:** everything taught and practised here runs on the practice engagement (the
website); AT1 assesses the same work on the assessed system. The two systems differ by design — the
same reasoning can reach opposite calls, and that is the learning. Teach the method on the practice
vehicle, and never work the assessed system in class — these materials deliberately do not name it,
so they stay correct if it is ever swapped.

## Teaching source
AWS reliability pillar (Multi-AZ, backup/restore, cross-Region DR) + security layers + cost
optimisation, pinned at Step 4 (TBD); bespoke for the single-instance-DB cost-benefit framing and the
residency slice.

## AWS pin table
TBD — AWS reliability/security/cost modules to be pinned.

## Slides

### Opener
- [BESPOKE] The improvement passes
  - The tiers are designed; now you improve them — security, then reliability and scalability, then cost and monitoring.
  - Each pass reviews the same architecture through a different lens, to the goals and metrics you set.
  - It ends with the argument: every improvement justified on cost versus benefit.
  - Design only — the build is AT3.
  image: gen flat vector hero illustration of a resilient cloud architecture spanning two availability zones and a backup region, shields and redundancy arrows, blue and gold accents, minimal, no text
  notes:
    Workbook tasks 10 to 13, in order — three improvement passes then the cost-benefit case.
    The centrepiece lands in this Topic: rejecting an improvement can be the strongest design move in the cluster.

### C1 — The security improvements
- Teaches: [ICTCLD504 PC 2.3] · [ICTCLD504 KE 8]
- Kicker: the improvement stays secure
- [BESPOKE] Security layers, and improving them
  - The layers: network isolation, security groups, least-privilege access, and encryption at rest and in transit as the baseline.
  - Review each layer against the goals and design the improvements — tightening what exists before adding anything new.
  - Every later change must inherit these layers, not bypass them — a DR copy of financial data carries the same protections as the primary.
  image: none
  notes:
    Workbook task 10 — the security pass. Encryption is assumed on by default, including any cross-region copy.
    Misconception: a DR copy is "just a backup" and can be looser. A weaker copy is the breach.
- [EX] Design the security improvements
  - Workbook — task 10.
  - Review the practice engagement's security layers and design the improvements, each tied to a goal.
  timer: ~25 min
  image: none
  notes:
    Activity = practice workbook task 10.
    Push tightening-first: an improvement that adds a service before fixing a loose group has the order wrong.
- [TAKEAWAYS] Section 1 · Security
  - Isolation, groups, least privilege, encryption — the baseline layers.
  - Improvements inherit the layers; copies carry the same protections.
  image: none

### C2 — The reliability and scalability improvements
- Teaches: [ICTCLD504 PC 2.3] · [ICTCLD504 PE 1]
- Kicker: improve reliability to the goal, not beyond it
- [PRIMER] What makes a cloud system reliable
  - Reliability: the system keeps serving through component and zone failures, and recovers from loss.
  - Three building blocks: redundancy across zones, backup and restore, and cross-region disaster recovery.
  - Backup recovers data in place; DR survives losing a whole region — different failures, different tools.
  image: none
  notes:
    The frame before the design. Map each building block to the failure it answers.
- [BESPOKE] The reliability target
  - Review the single-zone baseline against the reliability goals; name where a single failure takes the system down.
  - The shape of the target: a load balancer and a pool of instances across two zones; the database decision still open; a cross-region backup copy, onshore.
  - The database tier is left unresolved on this slide on purpose — the next slide argues it.
  image: diagram reliability-target
  notes:
    Walk the diagram tier by tier. Leave the database tension unresolved for one slide on purpose.
    Redundancy is applied tier by tier, to the goal — not painted across everything.
    The diagram shows the database with a question mark deliberately. Do not resolve it for them.
- [BESPOKE] The centrepiece: spending the money where it buys the most
  - Every tier here is a single point of failure. You cannot fix them all — so which one first, and what do you leave?
  - The compute tier is the cheapest and largest win: one instance with no load balancer means any instance failure is a total outage.
  - The database is the expensive one: a failover standby roughly doubles the database line, for a site whose content changes rarely and restores cleanly from backup.
  - "Reliable means Multi-AZ everywhere" is the reflex to resist. Rank by benefit per dollar against the stated goal, and be able to defend what you left out.
  image: none
  notes:
    The single most assessed piece of reasoning in AT1 — slow down here.
    The assessed skill is arguing the trade-off, not naming the feature. A well-argued rejection outscores a feature added by reflex.
    Press them on availability class: a public marketing site losing an hour overnight is not the same as a system with an externally fixed deadline. Different systems, different answers, same method.
- [TABLE] Database reliability — the options weighed
  | Option | Reliability gain | Cost / risk | Verdict |
  | Backup + tested restore | recovers from loss; recovery measured in hours | low — already largely in place | defensible if the recovery target allows it |
  | Failover (Multi-AZ) database | zero-downtime zone failover | roughly doubles the database line, ongoing | defensible if the recovery target does not |
  | Fix compute first, revisit the database after | removes the largest exposure for the least money | sequencing risk if the database then fails | commonly the strongest argued position |
  note: There is no CHOSEN row. The verdict is the student's and the reasoning is the mark — this table is the shape of the argument, not its answer.
  image: none
- [BESPOKE] The residency slice
  - A scoped constraint: specific regulated data must reside in a named region; the main system stays where it is.
  - The design keeps the regulated data in-region — a slice of the reliability and DR design, not a second architecture.
  - Constraints like this were read precisely in the compliance task; here they get built into the design.
  image: none
  notes:
    Keep it light — one constraint shaping where specific data sits, nothing more.
    Ties back to workbook task 3; the compliance reading becomes a design input here.
- [EX] Design the reliability and scalability improvements
  - Workbook — task 11.
  - Design the reliability and scalability improvements for the practice engagement to your goals, and argue one cost-benefit trade-off explicitly.
  timer: ~35 min
  image: none
  notes:
    Activity = practice workbook task 11.
    The data-tier call is theirs to make and argue. Two students can reach opposite verdicts and both be right, if both are argued against the goal and the cost. That's the learning, not a mistake.
    Watch for a verdict copied off the table rather than argued. The table is the shape of the argument, not its answer.
- [TAKEAWAYS] Section 2 · Reliability
  - Redundancy tier by tier, to the goal.
  - The rejection, argued on cost versus benefit, is the centrepiece.
  - Regulated data placed by the compliance reading.
  image: none

### C3 — Cost optimisation and monitoring
- Teaches: [ICTCLD504 PC 2.3] · [ICTCLD504 KE 9]
- Kicker: pay for what the goals need, and watch it
- [BESPOKE] The cost pass
  - Review the design for cost: right-size every tier, release what elasticity makes releasable, and price the improvements.
  - The techniques that deliver the improvements — redundant deployment, health checks, automated backups and snapshots, cross-region copies — each has a running cost; know it.
  - A design that meets its goals at lower cost beats the same design at higher cost, every time.
  image: none
  notes:
    Workbook task 12, first half. Elasticity's cost payoff is releasing capacity — connect back to Topic 2's definition.
- [BESPOKE] Design the monitoring in
  - Decide now what the improved system reports: the metrics from task 8, watched by alarms with owners.
  - Monitoring designed in is cheap; monitoring bolted on later is a retrofit.
  - This design is what the build's monitoring task implements — the numbers are already set.
  image: none
  notes:
    Task 12, second half. The metrics from Topic 2 come back as the things monitored — the thread is deliberate.
- [EX] Cost and monitoring
  - Workbook — task 12.
  - Design the cost optimisation and the monitoring for the practice engagement — what is right-sized, what is released, what is watched.
  timer: ~25 min
  image: none
  notes:
    Activity = practice workbook task 12.
    Every monitored metric should trace to task 8; every cost claim to a tier.
- [TAKEAWAYS] Section 3 · Cost and monitoring
  - Right-size, release, price the improvements.
  - Monitor the metrics you set, by design not retrofit.
  image: none

### C4 — The cost-benefit justification
- Teaches: [ICTCLD504 PC 1.4] · [ICTCLD504 PC 2.3]
- Kicker: every improvement earns its place
- [BESPOKE] Justify on cost versus benefit
  - Every improvement is justified on cost versus benefit, against the current run cost as the baseline.
  - The shape: what it costs, what it buys, and why that trade is worth it for this business.
  - The rejected options belong in the argument too — what you didn't build, and why, is half the case.
  image: none
  notes:
    Workbook task 13 — the written case. The operational costing document is the baseline; every claim cites it.
    The centrepiece rejection from C2 is the worked example of the form.
- [EX] Write the cost-benefit justification
  - Workbook — task 13.
  - Justify each improvement for the practice engagement on cost versus benefit, citing the current run cost as the baseline.
  timer: ~30 min
  image: none
  notes:
    Activity = practice workbook task 13.
    Push for numbers from the costing document, and for at least one argued rejection.
- [TAKEAWAYS] Topic 3 · Key takeaways
  - Three passes over one architecture: security, reliability, cost.
  - The strongest design move can be a rejection, argued on cost versus benefit.
  - Monitoring designed in against the metrics you set.
  - Every improvement earns its place against the run-cost baseline.
  image: none

### Close
- [BESPOKE] Next: Topic 4 — draw it, document it, present it
  - The design is complete: analysed, targeted, improved and justified.
  - Next you draw the improved architecture, document the proposal, and present it for sign-off.
  image: none

## Build notes
~24 slides. Four activities, mapping to practice workbook tasks 10 · 11 · 12 · 13. One generated
diagram (`diagram reliability-target`, **assets live in the old `topic_02/diagrams/` and must move
here before build**); the opener hero carries the old Topic 2 prompt (cached in old
`topic_02/images/` — move). Re-cut from the old Topic 2 (reliability design, centrepiece, residency,
security layers) in the workbook's order; new teaching: the cost pass, monitoring-by-design, and the
cost-benefit case as its own written task. The old Topic 2's design/migration-principles slides moved
to Topic 1 with tasks 4–5.

## Changelog
- 2026-09-08 — new plan from the AT1 practice workbook (tasks 10–13); re-cut of the old Topics 2/3
  seam; cost and monitoring taught explicitly for the first time.
