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

### C1 — Reliability improvement design
- Teaches: [ICTCLD504 PC 2.3] · [ICTCLD504 PE 1] · [ICTCLD504 KE 9]
- Kicker: improve reliability to the goal, not beyond it
- [PRIMER] What makes a cloud system reliable
  - Reliability = the system keeps serving through component and zone failures, and recovers from loss.
  - Three building blocks: redundancy across Availability Zones (Multi-AZ), backup/restore, and cross-Region disaster recovery.
  - Reliability is designed jointly with security, scalability and cost — each choice is a trade-off, not a maximum.
  image: none
- [BESPOKE] Review the architecture, set the reliability target
  - Review Ledgerline's single-AZ baseline against the reliability goals; name where a single failure takes the system down.
  - Target: the application tier goes Multi-AZ behind a load balancer; the database gets automated backup/restore; a cross-Region DR copy goes to Melbourne (Australian data stays onshore).
  - The database is deliberately NOT Multi-AZ — the next slide argues why.
  image: diagram reliability-target
- [BESPOKE] The centrepiece — reject the Multi-AZ database
  - Ledgerline is a legacy accounting app, vendor-certified single-instance only — a Multi-AZ (failover) database is simply not available for it.
  - The only route to DB failover is to replace the accounting product: new licence, data migration, change management, and migration risk.
  - That cost is disproportionate to the reliability gained — so the design REJECTS a Multi-AZ database and leaves the DB single-AZ with backup/restore + cross-Region DR. This cost-benefit call is the heart of the Topic.
  - Warn against the reflex: "reliable database = Multi-AZ database" is wrong here — justify against the goal and the cost, not against a checklist.
  image: none
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
- [BESPOKE] The India residency slice
  - A light residency constraint: CERT-In-mandated logs and Companies-Act books-of-account must reside in Mumbai (`ap-south-1`); the main system stays in Sydney.
  - Design keeps the regulated data in-Region — the residency requirement is an input constraint on the design, not a bolt-on.
  - Note it as a scoped slice of the reliability/DR design, not a second architecture.
  image: none
- [EX] Design the reliability improvements
  - For the practice vehicle (the website), design the reliability improvements to the Topic-1 goals across the app, data and DR tiers — you decide what each tier needs, to the goals and no further.
  - Argue ONE cost-benefit trade-off explicitly and show how each change meets a named goal. NB the website runs MySQL with no legacy single-instance constraint, so the data-tier call (e.g. whether to go Multi-AZ) is yours to justify — potentially the OPPOSITE call to Ledgerline's, reached by the same cost-benefit reasoning.
  timer: ~30 min
  image: none

### C2 — Cloud design & migration principles
- Teaches: [ICTCLD504 KE 4] · [ICTCLD504 KE 5]
- Kicker: the principles under the improvement
- [PRIMER] Cloud design principles
  - Design for failure, loose coupling, statelessness, right-sizing, and automation over manual steps (KE 4).
  - Improve the architecture to these principles — they are why Multi-AZ and health checks belong in the design.
  - Simplest design that meets the goal wins; principles justify choices, they don't mandate maximums.
  image: none
- [BESPOKE] Migrating the baseline to the improved architecture
  - Migration principles: move incrementally, keep the system serving, evidence each step, and be able to roll back (KE 5).
  - Sequence the improvement so the single-AZ baseline becomes the Multi-AZ + DR target without a big-bang cutover.
  - This is design-level here — the actual migration/build is AT3.
  image: none
- [EX] Justify the design in principle
  - For your practice design, write the KE-appendix justification: name the cloud design principle behind each reliability choice and the migration approach that reaches it.
  timer: ~20 min
  image: none

### C3 — Security layers underpinning the design
- Teaches: [ICTCLD504 KE 8]
- Kicker: the improvement stays secure
- [BESPOKE] Security layers that keep the design secure
  - The tools and uses of security layers in cloud services: network isolation, security groups, IAM least-privilege, and encryption as the baseline (KE 8).
  - Encryption is assumed on by default (at rest and in transit) — including the cross-Region DR copy and the residency data.
  - Reliability changes must not weaken security — each new tier (Multi-AZ app, DR copy) inherits the security layers, not bypasses them.
  image: none

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
