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
  notes:
    Frame Topic 7 as the START of AT3 — AT2 wrote the IaC; now you DEPLOY, PROVE and REFINE it in the
    lab. Set the deploy discipline; don't teach change-sets yet.
    • First bullet: AT2 wrote the IaC; AT3 begins — deploy it, prove it, refine it.
    • Second bullet: today's arc — stand up the approved Ledgerline baseline, apply the improvement as a
    CHANGE-SET, then monitor, test and refine.
    • Third bullet (say it explicitly): Region substitution applies to EVERY deploy — the design targets
    Sydney (DR Melbourne) but you build in [scenario: ap-southeast-2 (Sydney) | deploy: us-east-1]. Same
    build; only the console Region differs.
    • Fourth bullet: the rhythm — teach → demo → practice: watch the deploy + change-set demo, then do it
    on the practice engagement.
    Misconception to pre-empt: "AT3 is a fresh build from scratch." No — you deploy the APPROVED baseline
    first, then apply the improvement OVER it as a change-set. That apply-as-update discipline is the whole
    Topic.
    Question to pose: "Why deploy the baseline first and change-set the improvement, instead of just
    deploying the improved stack directly?" (draws out the reviewable-diff, in-place, no-data-migration
    reasoning).
    UoC/AT3 tie: opens the AT3 deploy arc — ICTCLD504 el 3; everything today feeds the AT3 implementation
    record (deploy, monitoring, test results, refinements).

### C1 — Deploy the approved architecture
- Teaches: [ICTCLD504 PC 3.1] · [ICTCLD504 PE 4]
- Kicker: deploy the baseline, then apply the improvement as an update
- [PRIMER] Apply-as-update: the change-set discipline
  - Deploy the approved baseline first, then apply the improvement **as a change-set** over it — not a fresh, replacing stack.
  - A change-set is a reviewable diff: you see exactly what will be added or modified before it runs (in-place/additive — no resource replacement, no data migration).
  - The improvement adds app-tier Multi-AZ and scaling; encryption is already baseline, so it is not part of this change.
  image: none
  notes:
    The primer for C1 — teach what a change-set IS and why the improvement lands as one. This is the
    conceptual core of AT3.
    • First bullet: deploy the approved BASELINE first, then apply the improvement AS A CHANGE-SET over it
    — not a fresh, replacing stack. Two steps, in order.
    • Second bullet: a change-set is a REVIEWABLE DIFF — you see exactly what will be added or modified
    before it runs (in-place/additive — no resource replacement, no data migration). "Review before
    execute" is the discipline.
    • Third bullet: the improvement adds app-tier Multi-AZ and scaling; ENCRYPTION is already baseline, so
    it is NOT part of this change. Scope the change precisely.
    Misconception to pre-empt: "a change-set replaces the old resources with new ones." No — here it's
    in-place/additive; replacement would mean data migration, which we explicitly avoid. Review the diff to
    confirm modifies, not replaces.
    Question to pose: "Before you execute a change-set, what should you check in the diff — and what would
    a REPLACE on the database mean?" (draws out review-before-execute + why replace is dangerous).
    UoC/AT3 tie: ICTCLD504 PC 3.1 (deploy approved architecture) + PE 4 (console/SDK/CLI) → the deploy
    evidence in AT3; sets up the lab DB constraint next.
- [BESPOKE] The lab constraint: the database is create-only
  - The change-set must **not modify the database** — the Learner Lab role denies `rds:ModifyDBInstance`, so the DB tier is create-only.
  - DB-tier DR (backup / cross-region) therefore stays **design-level** (per AT1), demonstrated on the app tier.
  - Deploy with the console, an SDK, or the CLI — whichever the platform exposes (PE 4); the change-set targets the app tier only.
  image: diagram change-set-flow
  notes:
    The lab reality that shapes the whole deploy — use the change-set-flow diagram (baseline → change-set
    adds app-tier Multi-AZ + scaling, DB untouched → improved stack).
    • First bullet: the change-set must NOT modify the database — the Learner Lab role denies
    rds:ModifyDBInstance, so the DB tier is CREATE-ONLY. State the technical constraint plainly.
    • Second bullet: therefore DB-tier DR (backup / cross-region) stays DESIGN-LEVEL (per AT1), and the
    reliability demonstration lands on the APP tier. The constraint is honest, not a gap.
    • Third bullet: deploy with the console, an SDK, or the CLI — whichever the platform exposes (PE 4);
    the change-set targets the APP TIER only.
    Misconception to pre-empt: "create-only means the database DR isn't assessed." No — it's designed and
    evidenced at design level (AT1); the lab just can't apply it live, so the built demonstration moves to
    the app tier. Nothing is dropped, only relocated.
    Question to pose: "The lab denies rds:ModifyDBInstance — so where do you DEMONSTRATE reliability, and
    where does DB-tier DR get evidenced instead?" (app tier live; DB tier at design level).
    UoC/AT3 tie: ICTCLD504 PC 3.1 + PE 4 → the deploy is scoped to what the lab allows; the substitution
    keeps the assessment honest (documented in the AT3 record).
- [DEMO] Deploy the baseline, then apply the change-set
  - Deploy the approved baseline stack in the lab to CREATE_COMPLETE (`[scenario: ap-southeast-2 (Sydney) | deploy: us-east-1]`).
  - Create a change-set for the improvement, review the diff (app-tier Multi-AZ + scaling added; DB untouched), then execute it.
  - Confirm the improved resources in the console/CLI.
  source: recorded demo — deploy + change-set
  image: none
  notes:
    DEMONSTRATION (educator-led, LIVE) — demonstrate the course's OWN deploy on the lab-pack in front of
    the class, then students replicate on the practice engagement next slide. There is no recorded
    substitute; screen your own live console/CLI.

    WHAT TO DEMONSTRATE (step by step, narrating as you go):
    1. Deploy the approved BASELINE stack in the lab to CREATE_COMPLETE — set the console Region to
    us-east-1 first ([scenario: ap-southeast-2 (Sydney) | deploy: us-east-1]); say the substitution out loud.
    2. Create a CHANGE-SET for the improvement; open the diff and read it WITH the class — app-tier
    Multi-AZ + scaling added; database untouched.
    3. Execute the change-set; watch it to UPDATE_COMPLETE.
    4. Confirm the improved resources in the console/CLI (the new app-tier instances, the scaling config).

    WHAT TO EMPHASISE:
    • REVIEW THE DIFF BEFORE EXECUTING — pause on it; this is the discipline, not a formality. Point out
    modifies vs any replaces.
    • The DB tier shows NO changes in the diff — tie it back to the create-only constraint
    (rds:ModifyDBInstance denied).
    • Region visible before anything is created — model setting it first.
    • Narrate the evidence capture — screenshot the diff and the CREATE_COMPLETE / UPDATE_COMPLETE states
    as you go; students must mirror this in AT3.

    PREP: a clean Learner Lab open, the approved baseline template + the improvement change ready to load,
    Region set to us-east-1. ~10–12 min to deploy + change-set + narrate before the activity. If a deploy is
    slow, have a pre-deployed baseline stack ready so the change-set step isn't rushed.
- [EX] Deploy + apply the change-set on the practice engagement
  - On the practice engagement (the website), deploy the single-AZ baseline, then apply YOUR OWN improvement as a change-set in us-east-1.
  - Review the diff before executing; confirm the change-set applies the changes you intended, note which are in-place modifies vs replacements, and check the improvement is live.
  timer: ~35 min
  image: none
  notes:
    Facilitation — the C1 practice; students do what you just demoed, on the PRACTICE engagement (the
    website), in us-east-1.
    Tell students, in these words: "On the practice engagement, deploy the single-AZ baseline, then apply
    YOUR OWN improvement as a change-set in us-east-1. Review the diff before you execute, confirm it
    applies the changes you intended, and check the improvement is live."
    Steps (put on the board):
    1. Deploy the single-AZ baseline to CREATE_COMPLETE (Region us-east-1 — [scenario: ap-southeast-2
    (Sydney) | deploy: us-east-1]).
    2. Create a change-set for your improvement; REVIEW the diff.
    3. Note which changes are in-place MODIFIES vs REPLACEMENTS; confirm the DB isn't being modified.
    4. Execute; confirm the improvement is live.
    Must produce: a deployed baseline, a reviewed change-set, and evidence the improvement applied (diff
    screenshot + the live improved resources) — the practice version of the AT3 deploy.
    Timing: ~35 min. Where they get stuck: the baseline deploy is slow (have them start it, then read the
    diff of a prepared change-set while it runs); they execute WITHOUT reading the diff (stop them —
    reviewing it is the point); and a change that would REPLACE a resource surprises them — make them notice
    it in the diff.
    Share-back prompt: ask one student which line of their diff was a modify and which (if any) was a
    replace, and what that means for data.
    No-leakage note: the website is the PRACTICE vehicle — AT3 assesses the same deploy on the Ledgerline
    system (comparable, not identical); keep them on the practice engagement here.

### C2 — Monitor & measure
- Teaches: [ICTCLD504 PC 3.2] · [ICTCLD504 KE 10]
- Kicker: measure the deploy against the AT1 metrics and business goals
- [PRIMER] Monitoring against metrics & business goals
  - Monitor and measure the architecture against the **performance metrics and business goals set at AT1** — the deploy has to prove the improvement, not just exist.
  - Use industry-standard metrics, methods and monitoring techniques for cloud resources (KE 10): CloudWatch metrics, alarms and dashboards.
  - Pick the metrics that map to each goal — latency/throughput for performance, healthy-host count for reliability.
  image: none
  notes:
    Open Section 2 — a deploy has to PROVE the improvement, not just exist. PC 3.2 and KE 10 land here.
    • First bullet: monitor and measure the architecture against the PERFORMANCE METRICS and BUSINESS
    GOALS set at AT1 — the deploy proves the improvement against the targets you already agreed.
    • Second bullet: use industry-standard metrics, methods and monitoring techniques for cloud resources
    (KE 10) — CloudWatch metrics, alarms and dashboards. Name the tooling.
    • Third bullet: pick the metrics that MAP to each goal — latency/throughput for performance,
    healthy-host count for reliability. A metric with no goal behind it is noise.
    Misconception to pre-empt: "monitoring = turn on CloudWatch and collect everything." No — you measure
    against the AT1 goals; the skill is choosing the metric that evidences a specific goal, not maximising
    data.
    Question to pose: "Your AT1 goal was 'improve availability' — which specific metric proves it, and what
    alarm threshold would you set?" (ties a goal to a metric to a threshold).
    UoC/AT3 tie: ICTCLD504 PC 3.2 + KE 10 (monitor/measure against metrics and business goals) → the
    monitoring evidence in the AT3 record.
- [BESPOKE] Read the numbers on the deployed stack
  - Point CloudWatch at the deployed resources: CPU/latency/request counts on the app tier, alarm on the thresholds the AT1 goals imply.
  - A metric is only useful against a target — record the baseline reading, then the post-improvement reading, and compare.
  - Monitoring is evidence: these readings become part of the AT3 implementation record.
  image: none
  notes:
    The how-to for Section 2 — point monitoring at the ACTUAL deployed resources and read them against
    targets.
    • First bullet: point CloudWatch at the deployed resources — CPU/latency/request counts on the app
    tier; alarm on the thresholds the AT1 goals imply. Concrete metrics on concrete resources.
    • Second bullet (the key discipline): a metric is only useful AGAINST A TARGET — record the BASELINE
    reading, then the POST-IMPROVEMENT reading, and compare. Before/after is what proves the improvement.
    • Third bullet: monitoring is EVIDENCE — these readings become part of the AT3 implementation record.
    Capture them as you go.
    Misconception to pre-empt: "one post-improvement reading proves the improvement." No — without the
    baseline reading you have nothing to compare to; the before/after pair is the proof.
    Question to pose: "You added app-tier scaling — what two readings do you need to show it helped, and
    when do you take each?" (draws out baseline vs post-improvement).
    UoC/AT3 tie: ICTCLD504 PC 3.2 + KE 10 → the baseline / post-improvement readings evidenced in the AT3
    record.

### C3 — Test & demonstrate
- Teaches: [ICTCLD504 PC 3.3] · [ICTCLD504 PE 2] · [ICTCLD504 KE 7]
- Kicker: prove security, reliability, scalability and cost on the running system
- [BESPOKE] Test & demonstrate the improvements
  - Test and demonstrate the **security, reliability, scalability and cost optimisation** of the deployed resources (PC 3.3) — deploy, test and measure the design against its principles, metrics and goals (PE 2).
  - Reliability: fail/remove one app-tier instance and show the Multi-AZ deployment stays available — a **technique to avoid a single point of failure** (KE 7).
  - Scalability: drive load and show the app tier scales; cost: show the improvement's cost against the goal.
  image: none
  notes:
    Open Section 3 — PROVE the four concerns on the running system. PC 3.3, PE 2 and KE 7 land here.
    • First bullet: test and demonstrate the SECURITY, RELIABILITY, SCALABILITY and COST OPTIMISATION of
    the deployed resources (PC 3.3) — deploy, test and measure the design against its principles, metrics
    and goals (PE 2). Four concerns, all demonstrated.
    • Second bullet (the headline): RELIABILITY — fail/remove one app-tier instance and show the Multi-AZ
    deployment stays available — a technique to AVOID A SINGLE POINT OF FAILURE (KE 7). This is the marquee
    test.
    • Third bullet: SCALABILITY — drive load and show the app tier scales; COST — show the improvement's
    cost against the goal. Each concern gets a demonstration.
    Misconception to pre-empt: "demonstrating reliability means saying it's reliable." No — you have to
    SHOW it: kill an instance and show continued availability. A claim isn't a demonstration.
    Question to pose: "How do you PROVE, not assert, that the app tier has no single point of failure?"
    (draws out the fail-an-instance SPOF test).
    UoC/AT3 tie: ICTCLD504 PC 3.3 + PE 2 + KE 7 → the test-and-demonstrate evidence across the four
    concerns in AT3.
- [BESPOKE] Testing & debugging techniques
  - Apply testing/debugging techniques to the deployed system: reproduce, isolate, read the logs/metrics, confirm the fix (KE 7).
  - The SPOF test is the headline — because the DB tier is create-only here, the reliability demonstration lands on the app tier (DB-tier DR stays design-level).
  - Every test produces a result you can act on — that feeds C4.
  image: none
  notes:
    The technique slide for Section 3 — give a repeatable testing/debugging method (KE 7) and place the
    SPOF test.
    • First bullet: apply testing/debugging techniques to the deployed system — reproduce, isolate, read
    the logs/metrics, confirm the fix (KE 7). A four-step debugging loop.
    • Second bullet: the SPOF test is the headline — and because the DB tier is CREATE-ONLY here, the
    reliability demonstration lands on the APP tier (DB-tier DR stays design-level). Same constraint as C1,
    restated where it bites.
    • Third bullet: every test produces a RESULT you can act on — that feeds C4 (short-term refinements).
    Testing isn't the end; it drives the refine loop.
    Misconception to pre-empt: "debugging is random poking until it works." No — reproduce → isolate → read
    logs/metrics → confirm; a method you can evidence, not trial and error.
    Question to pose: "Your SPOF test shows a slow failover — walk the reproduce → isolate → read → confirm
    loop on it" (rehearses the technique; leads into C4).
    UoC/AT3 tie: ICTCLD504 KE 7 + PC 3.3 + PE 2 → the testing/debugging evidence in AT3; feeds the
    refinements in C4.

### C4 — Short-term refinements
- Teaches: [ICTCLD504 PC 3.4]
- Kicker: act on the test results, now
- [BESPOKE] Apply short-term refinements
  - Apply **short-term refinements** to the deployed resources according to the test results (PC 3.4) — a threshold tweak, a scaling adjustment, a security-group tightening.
  - Short-term = what you change now on the running system as a small follow-up change-set; long-term strategy is Topic 8.
  - Re-measure after each refinement to confirm it moved the metric the right way — the test → refine loop.
  image: none
  notes:
    Close the deploy loop — ACT on the test results now. PC 3.4 lands here.
    • First bullet: apply SHORT-TERM refinements to the deployed resources according to the test results
    (PC 3.4) — a threshold tweak, a scaling adjustment, a security-group tightening. Small, immediate
    changes.
    • Second bullet: SHORT-TERM = what you change NOW on the running system as a small follow-up
    change-set; LONG-TERM strategy is Topic 8. Draw the line explicitly.
    • Third bullet: RE-MEASURE after each refinement to confirm it moved the metric the right way — the
    test → refine loop. A refinement you don't re-measure isn't finished.
    Misconception to pre-empt: "short-term and long-term improvements are the same list." No — short-term
    is applied now on the deployed stack (PC 3.4); long-term is described, not applied (Topic 8, PC 4.2).
    Don't mix them.
    Question to pose: "Your SPOF test showed failover was slow — what's a SHORT-TERM refinement you'd apply
    now, and how do you confirm it worked?" (draws out tweak + re-measure).
    UoC/AT3 tie: ICTCLD504 PC 3.4 (short-term refinements from test results) → the refinement evidence in
    AT3; long-term strategy is Topic 8 (PC 4.2).

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
