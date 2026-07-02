# Topic 07 Deploying the baseline and applying the improvement as a change-set — Slide plan
> **Covers:** Topic 07 — see coverage.md
> **Subtitle:** Deploy the approved baseline, apply the improvement as a change-set, then monitor, test and refine
> **STATUS: DRAFT** (authored 2026-07-02).

## Depth ceiling
BUILD — the first hands-on Topic of AT3 (Implement). Deploy the approved architecture to the Learner Lab, measure it against the AT1 metrics/goals, test and demonstrate the improvements, and refine. Every improvement lands as an **in-place/additive change-set** over the deployed baseline — no resource replacement, no data migration; encryption is baseline and data is out of scope. AWS practicals run `teach → demo → practice`. The as-deployed documentation, long-term strategy and final sign-off are Topic 8 (out of scope here).

## Teaching source
AWS ACA CloudFormation deploy / change-sets + CloudWatch monitoring decks pinned at Step 4 (TBD); bespoke for the apply-as-update discipline, the lab DB-tier constraint, and the test-and-refine loop against the AT1 metrics.

## AWS pin table
TBD — AWS CloudFormation/deploy modules to be pinned.

## Slides

### Opener
- [BESPOKE] From approved design to running system
  - AT2 wrote the IaC; AT3 begins — you deploy it, prove it, and refine it in the lab.
  - This Topic: stand up the approved Ledgerline baseline, apply the improvement as a **change-set**, then monitor, test and refine.
  - Region substitution applies to every deploy: the design targets Sydney (DR Melbourne), but you build in `[scenario: ap-southeast-2 (Sydney) | deploy: us-east-1]`. Same build, only the console Region differs.
  - `teach → demo → practice`: watch the deploy + change-set demo, then do it on the practice engagement.
  image: gen flat vector hero illustration of a cloud engineer applying a change-set to upgrade a running system, before and after states, blue and gold accents, minimal, no text

### C1 — Deploy the approved architecture
- Teaches: [ICTCLD504 PC 3.1] · [ICTCLD504 PE 4]
- Kicker: deploy the baseline, then apply the improvement as an update
- [PRIMER] Apply-as-update: the change-set discipline
  - Deploy the approved baseline first, then apply the improvement **as a change-set** over it — not a fresh, replacing stack.
  - A change-set is a reviewable diff: you see exactly what will be added or modified before it runs (in-place/additive — no resource replacement, no data migration).
  - The improvement adds app-tier Multi-AZ and scaling; encryption is already baseline, so it is not part of this change.
  image: none
- [BESPOKE] The lab constraint: the database is create-only
  - The change-set must **not modify the database** — the Learner Lab role denies `rds:ModifyDBInstance`, so the DB tier is create-only.
  - DB-tier DR (backup / cross-region) therefore stays **design-level** (per AT1), demonstrated on the app tier.
  - Deploy with the console, an SDK, or the CLI — whichever the platform exposes (PE 4); the change-set targets the app tier only.
  image: diagram change-set-flow
- [DEMO] Deploy the baseline, then apply the change-set
  - Deploy the approved baseline stack in the lab to CREATE_COMPLETE (`[scenario: ap-southeast-2 (Sydney) | deploy: us-east-1]`).
  - Create a change-set for the improvement, review the diff (app-tier Multi-AZ + scaling added; DB untouched), then execute it.
  - Confirm the improved resources in the console/CLI.
  source: recorded demo — deploy + change-set
  image: none
- [EX] Deploy + apply the change-set on the practice engagement
  - On the practice engagement (the website), deploy the single-AZ baseline, then apply YOUR OWN improvement as a change-set in us-east-1.
  - Review the diff before executing; confirm the change-set applies the changes you intended, note which are in-place modifies vs replacements, and check the improvement is live.
  timer: ~35 min
  image: none

### C2 — Monitor & measure
- Teaches: [ICTCLD504 PC 3.2] · [ICTCLD504 KE 10]
- Kicker: measure the deploy against the AT1 metrics and business goals
- [PRIMER] Monitoring against metrics & business goals
  - Monitor and measure the architecture against the **performance metrics and business goals set at AT1** — the deploy has to prove the improvement, not just exist.
  - Use industry-standard metrics, methods and monitoring techniques for cloud resources (KE 10): CloudWatch metrics, alarms and dashboards.
  - Pick the metrics that map to each goal — latency/throughput for performance, healthy-host count for reliability.
  image: none
- [BESPOKE] Read the numbers on the deployed stack
  - Point CloudWatch at the deployed resources: CPU/latency/request counts on the app tier, alarm on the thresholds the AT1 goals imply.
  - A metric is only useful against a target — record the baseline reading, then the post-improvement reading, and compare.
  - Monitoring is evidence: these readings become part of the AT3 implementation record.
  image: none

### C3 — Test & demonstrate
- Teaches: [ICTCLD504 PC 3.3] · [ICTCLD504 PE 2] · [ICTCLD504 KE 7]
- Kicker: prove security, reliability, scalability and cost on the running system
- [BESPOKE] Test & demonstrate the improvements
  - Test and demonstrate the **security, reliability, scalability and cost optimisation** of the deployed resources (PC 3.3) — deploy, test and measure the design against its principles, metrics and goals (PE 2).
  - Reliability: fail/remove one app-tier instance and show the Multi-AZ deployment stays available — a **technique to avoid a single point of failure** (KE 7).
  - Scalability: drive load and show the app tier scales; cost: show the improvement's cost against the goal.
  image: none
- [BESPOKE] Testing & debugging techniques
  - Apply testing/debugging techniques to the deployed system: reproduce, isolate, read the logs/metrics, confirm the fix (KE 7).
  - The SPOF test is the headline — because the DB tier is create-only here, the reliability demonstration lands on the app tier (DB-tier DR stays design-level).
  - Every test produces a result you can act on — that feeds C4.
  image: none

### C4 — Short-term refinements
- Teaches: [ICTCLD504 PC 3.4]
- Kicker: act on the test results, now
- [BESPOKE] Apply short-term refinements
  - Apply **short-term refinements** to the deployed resources according to the test results (PC 3.4) — a threshold tweak, a scaling adjustment, a security-group tightening.
  - Short-term = what you change now on the running system as a small follow-up change-set; long-term strategy is Topic 8.
  - Re-measure after each refinement to confirm it moved the metric the right way — the test → refine loop.
  image: none

### Close
- [TAKEAWAYS] Topic 7 · Key takeaways
  - Deploy the approved baseline first, then apply the improvement as an in-place/additive **change-set** — review the diff before executing.
  - The lab DB tier is create-only (`rds:ModifyDBInstance` denied) — DB-tier DR stays design-level; the improvement lands on the app tier.
  - Monitor and measure against the AT1 metrics and business goals; test and demonstrate security, reliability, scalability and cost — the SPOF test is the reliability headline.
  - Apply short-term refinements from the test results and re-measure — the test → refine loop.
  image: none
- [BESPOKE] Next: Topic 8 — document, strategise, sign off
  - You have deployed, proven and refined the improvement in the lab.
  - Next you document the as-deployed system, set the long-term strategy, and take it to final sign-off.
  image: none

## Build notes
~13 slides. `teach → demo → practice` on the practice engagement in us-east-1 (substituted). One generated diagram (`diagram change-set-flow`: baseline stack → change-set adds app-tier Multi-AZ + scaling, DB untouched → improved stack); one decorative `gen` image (opener hero); one DEMO (deploy baseline + apply change-set); one EX (deploy + apply the change-set on the practice engagement). Vehicle taught = Ledgerline; the website engagement is the practice vehicle.

## Changelog
- 2026-07-02 — authored to full content.
