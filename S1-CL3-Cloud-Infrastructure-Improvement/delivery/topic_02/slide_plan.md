# Topic 02 Metrics, and the four-component design — Slide plan
> **Covers:** Topic 02 — see coverage.md
> **Subtitle:** Confirm the metrics the improvement is measured by, then design the four resource tiers
> **STATUS: DRAFT — redrafted 2026-09-08 from the AT1 practice workbook, tasks 8–9 and the
> assessment's knowledge question Q2. Re-cut: the four-component design moves here from the old
> Topic 3, to match the workbook's order.**

## Depth ceiling
DESIGN — the design work starts: confirm the performance metrics, then select and improve the four
resource tiers to the business needs. Security, reliability and cost improvements are Topic 3; the
build is AT3. Justify each choice; do not over-provision.

**Answer discipline:** activities run on the practice engagement (the website); AT1 assesses the same
work on Ledgerline. Teach the method on the practice vehicle; never supply Ledgerline answers.

## Teaching source
AWS performance/scalability pillar (elastic capacity, auto scaling, resource selection); bespoke for
the metrics discipline, the four-component framing, and the object-storage-in-context contrast.

## AWS pin table
TBD — AWS scalability/architecture modules to be pinned.

## Slides

### Opener
- [BESPOKE] The design starts with a yardstick
  - The analysis is done and the decisions are confirmed; now the design work starts.
  - First the metrics — the numbers the improved system will be measured against — then the four resource tiers.
  - Scalability here means elastic capacity-on-demand, demonstrable by test — not a forecast, and not over-provisioning.
  - Design only, to the business needs — the build is AT3.
  image: gen flat vector hero illustration of four cloud resource tiers network compute database storage scaling elastically, blue and gold accents, minimal, no text
  notes:
    Workbook tasks 8 and 9 today, then the object-storage question. Metrics before design — you can't design to a target you haven't set.
    Misconception: scalable = big enough for the busiest day. That's over-provisioning; scalable means capacity moves with load.

### C1 — Confirm the performance metrics
- Teaches: [ICTCLD504 PC 2.1] · [ICTCLD504 PE 3]
- Kicker: a number with a target, for every goal
- [BESPOKE] From goals to metrics
  - A goal is directional; a metric makes it measurable — a number with a target the improved system can be tested against.
  - Evaluate and confirm the metrics for each goal: availability, recovery times, response time, cost per period.
  - Write them so a later test can pass or fail against them — these numbers come back in the build.
  image: none
  notes:
    Workbook task 8. The goals came from Topic 1; today each one gets its number.
    "Be reliable" is the goal restated — push to availability percentages, recovery-time targets, response times, cost per period.
    These exact metrics are what AT3's monitoring and testing measure against — say so; it motivates the care.
- [EX] Confirm the metrics
  - Workbook — task 8.
  - Evaluate and confirm the performance metrics for the practice engagement — a named metric and a target value for each goal.
  timer: ~25 min
  image: none
  notes:
    Activity = practice workbook task 8.
    The sanity check: could a later test pass or fail against each metric? If not, tighten it.
- [TAKEAWAYS] Section 1 · The yardstick
  - Every goal gets a metric; every metric gets a target.
  - Written to be tested against, later, by the build.
  image: none

### C2 — Design the four resource tiers
- Teaches: [ICTCLD504 PC 2.2] · [ICTCLD504 KE 9]
- Kicker: select and improve each tier to the business needs
- [PRIMER] Scalability is elastic capacity-on-demand
  - Elastic capacity: add resources as load rises, release them as load falls — pay for what you use.
  - The test of a scalable design is a demonstration — it scales on demand, proven later by test — not a load forecast on paper.
  - Over-provisioning fixed spare capacity is not scalability; right-size instead.
  image: none
  notes:
    The definition that governs the Topic. Both directions of elasticity matter — releasing capacity is where the saving lives.
- [BESPOKE] The four resource components
  - Split the design across four tiers: network, compute, database, storage.
  - Compute and storage scale elastically on demand; network and database are selected and configured to support that scale.
  - These are the same four units the build team later divides the IaC work by — a clean seam from design to build.
  image: diagram four-components
  notes:
    The frame the whole design (and the AT2 work-split) is organised by. Not all four tiers scale the same way — that distinction is the teaching.
- [BESPOKE] Selecting and improving each tier
  - Network: right-size the path and load-spreading so the tier below can scale out behind it.
  - Compute: move from fixed capacity to a pool that grows and shrinks on demand.
  - Database: select a managed service that scales reads without a rebuild, keeping the accounting data consistent.
  - Storage: select storage that grows on demand rather than a fixed-size volume.
  image: none
  notes:
    The how-to per tier. The database consistency constraint matters — it's an accounting system; you scale reads, you don't shard the ledger.
- [BESPOKE] Justify against the business needs
  - Tie every resource choice to a stated business need — why this tier, why this size.
  - Choose the simplest option that meets the need; note where capacity scales elastically and how a test would demonstrate it.
  - No tier scaled beyond what a need justifies.
  image: none
  notes:
    The discipline that turns selections into a defensible design. "To be safe" is not a justification.
- [EX] Design the four tiers
  - Workbook — task 9.
  - Select and improve the network, compute, database and storage tiers for the practice engagement, each choice justified against a named need.
  timer: ~35 min
  image: none
  notes:
    Activity = practice workbook task 9 — the biggest design task in AT1.
    Watch for over-provisioning, and for network/database marked elastic when they support scale rather than scale themselves.
- [TAKEAWAYS] Section 2 · The four tiers
  - Network, compute, database, storage — the design's frame and the build's work-split.
  - Compute and storage scale; network and database support.
  - Simplest option that meets the need, elasticity demonstrable by test.
  image: none

### C3 — Object storage in context
- Teaches: [ICTCLD504 KE 6]
- Kicker: the contrast that sharpens the storage choice
- [PRIMER] Object storage, and what it is for
  - Object storage holds whole objects addressed by key — it scales on demand and serves static content directly, no server involved.
  - The natural home for a static website's content: pages, images, downloads.
  - A stateful, transactional, database-backed system is the opposite workload — object storage is not its primary store.
  image: none
  notes:
    Contextual knowledge for the assessment's Q2 — the contrast is the answer: static content suits object storage; a transactional ledger does not.
    Be ready to explain provisioning object storage for a static-site workload — that's the examinable half.
- [EX] Answer the object-storage question
  - The assessment's question Q2, rehearsed in writing.
  - Contrast a stateful accounting workload's storage needs with an object-storage-dependent website workload, and explain how you would provision the latter.
  timer: ~15 min
  image: none
  notes:
    Activity = assessment Q2 rehearsed. The practice workbook carries no questions — use the assessment's.
    Check both halves are present: the contrast, and the provisioning explanation.
- [TAKEAWAYS] Topic 2 · Key takeaways
  - Metrics first: a number with a target for every goal, written to be tested against.
  - Four tiers, each selected and improved to a named need — simplest that fits.
  - Object storage suits static content; a transactional system is the contrast to know.
  image: none

### Close
- [BESPOKE] Next: Topic 3 — security, reliability and cost
  - The metrics are set and the four tiers are designed.
  - Next the improvement designs: security, reliability and scalability, cost and monitoring — and the cost-benefit case that justifies them.
  image: none
  notes:
    The seeded single-instance-DB constraint from Topic 1 becomes the centrepiece next Topic.

## Build notes
~19 slides. Three activities, mapping to practice workbook tasks 8 · 9 + the assessment's Q2
(rehearsed in writing). One generated diagram (`diagram four-components` — **assets live in the old
`topic_03/diagrams/` and must move here before build**); the opener hero carries the old Topic 3
prompt (cached in old `topic_03/images/` — move). Re-cut from the old Topics 1 and 3: metrics arrive
from old Topic 1 with task 8; the four-component design and object-storage contrast arrive from old
Topic 3, matching the workbook's design order (components before the improvement passes).

## Changelog
- 2026-09-08 — new plan from the AT1 practice workbook (tasks 8–9 + Q2); re-cut of the old
  Topics 2/3 seam to workbook order.
