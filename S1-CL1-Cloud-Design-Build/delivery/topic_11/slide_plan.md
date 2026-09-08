# Topic 11 Availability, and the state of what you have — Slide plan
> **Covers:** Topic 11 — see coverage.md
> **STATUS: DRAFT — redrafted 2026-08-28 from the AT3 practice workbook, Part A tasks 1–6. Teacher
> `notes:` not yet authored. `coverage.md` not yet reconciled.**

## Depth ceiling
Establish what the design is held to, and evaluate the environment you have against it. Cross-zone
availability only — multi-region and full disaster recovery are CL2.

**Answer discipline:** the workbook's tasks are worked by leading question, never by being told. These
slides teach the *method* for finding a weakness. They must not name the weaknesses.

## Teaching source
Bespoke ICTCLD502 material (availability concepts, evaluating availability), with light AWS support
(ACF M09 reliability).

## AWS pin table
ACF M09 (Well-Architected reliability), light.

## Slides

### Opener
- [BESPOKE] It works. What happens when it doesn't?
  - You built a working platform. Everything serving it runs in one place.
  - Nobody has yet asked what happens if that place goes away — and the client is about to.
  - Across the next topics you establish the targets, review what you have, design the upgrade, build it, and break it on purpose to prove it holds.
  - Today: what the design is held to, and honestly where the current environment stands against it.
  kicker: the question nobody has asked
  image: none

### C1 — What the design is held to
- Teaches: [ICTCLD502 PC 1.1] · [ICTCLD502 KE 4] · [ICTCLD502 KE 7] · [ICTCLD502 KE 8] · [ICTCLD502 FS Reading]
- Kicker: targets, sourced
- [BESPOKE] What high availability means
  - A highly available system stays usable when parts of it fail. Not "never fails" — keeps serving while failing.
  - Availability is expressed as a percentage of time, and every percentage is a quantity of downtime.
  - The step from two nines to five is the difference between hours a month and seconds a month.
  kicker: it assumes failure
  image: none
- [BESPOKE] What the nines cost
  - Each additional nine multiplies cost, and past a point it stops being purchasable at all.
  - So the target is not "as high as possible". It is the level this business actually needs.
  - A service used in business hours by one team does not need what a public, always-on platform needs.
  - Over-buying availability spends real money on downtime nobody would have noticed.
  kicker: buy what the business needs
  image: none
- [BESPOKE] Availability, reliability, and the agreement
  - Availability — is it up?
  - Reliability — is it working correctly? A service can be up and still returning errors.
  - A service level is the measurable target you promise; the agreement makes it contractual and attaches consequences to missing it.
  kicker: up is not the same as working
  image: none
- [BESPOKE] Recovery objectives
  - RTO — recovery time: the longest outage the business will tolerate.
  - RPO — recovery point: the most work it can afford to lose.
  - One is measured in time, the other in data. They are answers to different questions and they are routinely swapped.
  - Neither is set to zero, for the same reason nobody buys five nines by reflex.
  kicker: time, and data
  image: none
- [BESPOKE] A target you cannot source is a target you invented
  - Every figure you record has to come from somewhere — a requirements document, a policy, a specification.
  - Write down where each one came from as you record it. If you cannot, you have assumed it.
  - This matters more than it sounds: the whole design is measured against these numbers, and a number nobody agreed to cannot hold anything to account.
  kicker: name the source
  image: none
- [EX] Establish the targets
  - Workbook — task 1.
  - Record the availability, recovery and service-level targets this design has to meet, and for each one name the document it came from.
  timer: ~20 min
  image: none
  notes:
    Activity = practice workbook task 1. The intranet carries the figures; they have to go and read.
    The failure mode is plausible invented numbers — press every row for its source.
    Do not supply the figures.
- [TAKEAWAYS] Section 1 · The targets
  - Availability is a percentage that maps to real downtime, and nines cost.
  - Up is not the same as working correctly.
  - RTO is time; RPO is data.
  - Every target carries its source.
  image: none

### C2 — Reviewing what you have
- Teaches: [ICTCLD502 PC 2.1] · [ICTCLD401 FS Reading]
- Kicker: evaluate before you change
- [BESPOKE] Review before you improve
  - The instinct is to start adding redundancy. Resist it.
  - A fix aimed at a weakness you have not confirmed is wasted work, and it hides the one that matters.
  - Go tier by tier — network, compute, balancing, data, egress, monitoring — and judge each against the targets you just recorded.
  kicker: one tier at a time
  image: none
- [BESPOKE] Reading an architecture description honestly
  - Two things are easy to conflate: what exists and what is being used.
  - A resource can be provisioned across two places while everything actually serving sits in one.
  - When you read a description of an environment, separate the inventory from the load. They are different questions and only one of them is about availability.
  kicker: provisioned is not the same as used
  image: none
- [BESPOKE] Some tiers will already be fine
  - Not every row of your review is a problem. Saying "this meets the target, and here is why" is a finding.
  - It is also the discipline that stops you redesigning something that did not need it.
  kicker: "no change needed" is an answer
  image: none
- [EX] Review the environment against the targets
  - Workbook — task 2.
  - Work through each tier and record whether it meets the targets from task 1, and where it does not, why not.
  timer: ~25 min
  image: none
  notes:
    Activity = practice workbook task 2. The workbook's considerations do the leading — let them.
    Do not name which tiers pass or fail; the exercise is that they find out.
- [TAKEAWAYS] Section 2 · The review
  - Evaluate before you change anything.
  - Separate what exists from what is carrying load.
  - A tier that already meets the target is a finding worth recording.
  image: none

### C3 — Where it breaks, and how fast it comes back
- Teaches: [ICTCLD502 PC 2.2] · [ICTCLD502 PC 2.3] · [ICTCLD502 PC 2.4]
- Kicker: put numbers on it
- [BESPOKE] Single points of failure
  - A single point of failure is any component whose failure stops or degrades the whole service.
  - Redundancy in one tier does not remove a weakness in another — many servers sharing one database still have one database.
  kicker: one failure, whole service
  image: none
- [BESPOKE] How to hunt them
  - Two passes over the architecture, and they find different things:
    - Count. Go down every row and ask: is there exactly one of these?
    - Zone. Ask what would go dark if one whole location were lost this afternoon.
  - Some failures are quiet. A component can fail without users noticing, while something important stops happening in the background — those still belong on the list.
  - For each, record what the failure looks like and what the business actually loses.
  kicker: count them, then lose a zone
  image: none
- [BESPOKE] Estimating what you achieve today
  - Put numbers on it, per component: how much work would be lost, and how long recovery would take.
  - RPO comes from how often the data is captured. RTO comes from how long it takes to restore, point the application at it, and confirm it works — not from the restore alone.
  - Some components hold no data of their own, and the honest answer is that an RPO does not apply.
  - Compare each number to the target on the same row. The difference is the gap the design has to close.
  kicker: measured against the target
  image: none
- [BESPOKE] What can only be made bigger
  - Some components you add to. Others you can only replace with a larger one.
  - Anything in the second group carries an availability cost whenever it is resized, and eventually a ceiling.
  - Record which components are in that position and what happens to the service while they are resized.
  kicker: add to it, or replace it
  image: none
- [EX] Find the weaknesses and put numbers on them
  - Workbook — tasks 3, 4 and 5.
  - Identify the single points of failure with the failure mode and the consequence; estimate what the current environment achieves against each target; and record what can only scale vertically.
  timer: ~40 min
  image: none
  notes:
    Activity = practice workbook tasks 3–5. Task 3 tells them how many rows to expect and that fewer
    means they have missed something — let the workbook do that, don't pre-empt it.
    Circulate for lists that stop at the obvious tier; prompt with the two passes, not with answers.
- [TAKEAWAYS] Section 3 · Weaknesses and numbers
  - A single point of failure stops the whole service; redundancy elsewhere does not help.
  - Hunt by counting, then by losing a location.
  - RTO includes restoring, re-pointing and confirming — not just the restore.
  - Note what can only be replaced rather than added to.
  image: none

### C4 — Reporting what you found
- Teaches: [ICTCLD502 PC 2.5]
- Kicker: for the person who signs it
- [BESPOKE] Writing for the person who pays for it
  - Your reader approves the work and funds it. They are not going to read your tables.
  - Name the gap in the same terms as the target — a percentage, an amount of lost work, a number of hours. "Not highly available" is not a gap.
  - Say which components drive it. Keep it short enough that it gets read.
  kicker: their terms, not yours
  image: none
- [EX] Summarise the review
  - Workbook — task 6.
  - Write the short summary of what you found: the gap between the environment and the targets, and which components drive it, for a non-engineer.
  timer: ~20 min
  image: none
  notes:
    Activity = practice workbook task 6. Watch for engineer-to-engineer writing and for summaries
    that describe the architecture instead of naming the gap. The "cut it to two sentences" prompt in
    the workbook is a good share-back.
- [TAKEAWAYS] Topic 11 · Key takeaways
  - Availability is a business target with a cost, sourced from a document.
  - Review tier by tier before designing anything.
  - Find weaknesses by counting, and by losing a location.
  - Quantify what you achieve today, and report the gap in the client's terms.
  image: none

### Close
- [BESPOKE] Next — designing the upgrade
  - You know what it has to meet and where it currently falls short.
  - Next you design the change, tier by tier — and check each tier before you assume it needs one.
  image: none

## Build notes
~19 slides. Four activities, mapping to practice workbook tasks 1 · 2 · 3–5 · 6.
No committed images used. `multi-az-rds` diagram (currently in `topic_11/diagrams/`) moves to Topic 12,
where the data-tier design is done. `coverage.md` needs reconciling.
**Leakage guard:** no slide in this plan names a specific single point of failure or a specific fix.

## Changelog
- 2026-08-28 — redrafted from the AT3 practice workbook; the SPOF→mechanism answer table removed
  (it gave away tasks 3 and 13), tasks 2, 5 and 6 given activities for the first time.
