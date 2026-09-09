# Topic 01 Analysing the baseline architecture — Slide plan
> **Covers:** Topic 01 — see coverage.md
> **Subtitle:** Review the baseline, check compliance, weigh the options, set the goals
> **STATUS: DRAFT — redrafted 2026-09-08 from the AT1 practice workbook, tasks 1–7.**

## Depth ceiling
ANALYSIS — the front half of AT1 on the practice workbook: review and evaluate the existing
architecture, assess compliance, weigh the options, set the goals and confirm the decisions. The
design of the fix is Topics 2–3; nothing is implemented.

**Answer discipline:** activities run on the practice engagement (the website); AT1 assesses the same
work on Ledgerline. Teach the method on the practice vehicle; never supply Ledgerline answers.

## Teaching source
AWS well-architected review (reliability / performance / cost / security pillars) pinned at Step 4
(TBD); bespoke for the baseline framing, the compliance reading, and the goals-and-metrics discipline.

## AWS pin table
TBD — AWS ICTCLD504/architecture modules to be pinned.

## Slides

### Opener
- [BESPOKE] From analysis to improvement
  - Topic 1 opens AT1: before you improve a cloud system you first understand the one you have.
  - Today runs the analysis half of the design: review the baseline, check compliance, weigh the options, set the goals.
  - Vehicle: Ledgerline, YAT's Accounting system, runs single-AZ in the cloud — the system you analyse and improve.
  - Stay at analysis: diagnose and justify, don't design the changes yet.
  image: gen flat vector hero illustration of an analyst reviewing a cloud architecture diagram, magnifying glass over a data centre, blue and gold accents, minimal, no text
  notes:
    Workbook tasks 1 to 7 today, in order. Diagnosis precedes design — hold that line all Topic.
    Misconception: "we already know the fix, let's design it." A fix proposed before the goals exist has nothing to be measured against.

### C1 — Review the baseline, and evaluate it
- Teaches: [ICTCLD504 PC 1.1] · [ICTCLD504 PC 1.2] · [ICTCLD504 KE 1] · [ICTCLD504 KE 2]
- Kicker: understand what you have before you change it
- [PRIMER] How to review a cloud architecture
  - A structured review reads an architecture against pillars: security, reliability, performance, cost.
  - Frame it with the industry standards used in cloud solutions and the standard products the platform is built on.
  - The method is vendor-neutral; you apply it to a real baseline next.
  image: none
  notes:
    The four pillars recur all cluster. A review evaluates against them — an inventory with no judgement isn't a review.
    Question to pose: which pillar does a single-AZ design most obviously fail?
- [BESPOKE] Review the Ledgerline baseline
  - The current architecture: a VPC, one Availability Zone, an app tier and a single database.
  - Read the topology top-down — network, compute, database, storage — noting how each resource is deployed today.
  - Single-AZ means every tier shares one failure domain; one zone outage takes it all down.
  image: diagram ledgerline-baseline
  notes:
    Walk the diagram; trace the request path and have them find the shared failure domain.
    The workbook's task 1 runs the same reading on the practice engagement.
- [BESPOKE] Evaluate the design decisions and their business impact
  - Evaluate the baseline and state the business impact of its design decisions — downtime, lost billing, risk to close-of-month.
  - A seeded constraint surfaces here: the accounting product is vendor-certified single-instance only, so the database cannot go Multi-AZ. Record it — it drives the reliability design later.
  - Impact is a business statement, not a technical one; the goals you set later answer this language.
  image: none
  notes:
    Push from event to cost: "the server goes down" is technical; "billing halts at month-end" is impact.
    Plant the constraint deliberately — it is the cost-benefit centrepiece of Topic 3.
- [EX] Review and evaluate the practice baseline
  - Workbook — tasks 1 and 2.
  - Review the practice engagement's current architecture top-down, then evaluate it and state the business impact of its design decisions.
  timer: ~30 min
  image: none
  notes:
    Activity = practice workbook tasks 1–2, on the website engagement.
    Watch for resource lists with no judgement, and technical-only impacts.
- [TAKEAWAYS] Section 1 · The review
  - Four pillars: security, reliability, performance, cost.
  - Impact in business language, tied to each design decision.
  - Record the constraints you find — they shape everything after.
  image: none

### C2 — The compliance obligation
- Teaches: [ICTCLD504 AC 5]
- Kicker: read what it obliges, record where you stand
- [BESPOKE] Assess compliance against the regulatory requirements
  - Read the applicable regulatory instruments and record what each actually obliges — no more, no less.
  - Assess the current architecture against each obligation: compliant, non-compliant, or not applicable — with the evidence.
  - An obligation read too broadly costs as much as one ignored; the precise reading is the skill.
  image: none
  notes:
    Workbook task 3 — the regulatory requirements document is on the intranet; the task is careful reading plus an honest assessment.
    The over-read is the common failure; the instruments say precisely what is in scope.
- [EX] Assess compliance
  - Workbook — task 3.
  - Assess the practice engagement's compliance against the applicable regulatory requirements, obligation by obligation.
  timer: ~20 min
  image: none
  notes:
    Activity = practice workbook task 3.
    Press for evidence on every row — "compliant" with nothing behind it is a guess.
- [TAKEAWAYS] Section 2 · Compliance
  - Record what each instrument obliges, precisely.
  - Assess against each obligation with evidence.
  image: none

### C3 — The options, and their fit
- Teaches: [ICTCLD504 PC 1.3] · [ICTCLD504 PC 1.4] · [ICTCLD504 KE 3] · [ICTCLD504 KE 4] · [ICTCLD504 KE 5]
- Kicker: what could change, and what fits the business
- [PRIMER] Design patterns and architectural options
  - The option space: multi-zone redundancy, horizontal scaling and load balancing, managed versus self-run data tiers, caching, decoupling.
  - Each option is a pattern with a cost and a benefit — there is no single right answer, only a fit.
  - Cloud adoption itself changed the option space: managed services, elasticity and shared responsibility reshape what an improvement can be.
  image: none
  notes:
    A menu, not a decision — the next slide narrows it. Give each option a one-line "what it buys".
    Misconception: more redundancy is always better. Every option costs; the skill is fit.
- [BESPOKE] Assess the options against the business model
  - Determine and assess the benefits of each option against the current business model and needs — not in the abstract.
  - Constraints sharpen the choice: an option a constraint rules out narrows the argument to the ones that remain.
  - End with a judgement per option, not a balanced-sounding list.
  image: none
  notes:
    Workbook tasks 4 and 5 — the option list, then the assessment against the business.
    The single-instance-DB constraint from C1 is the worked example of a constraint doing analytical work.
- [BESPOKE] Reaching an improvement is a migration
  - Any option you pick has to be reached from the running baseline: move incrementally, keep the system serving, evidence each step, be able to roll back.
  - The cost of the path is part of the option's cost — a benefit you can only reach through a risky cutover is worth less than it looks.
  - Weigh the journey with the destination when you assess each option.
  image: none
  notes:
    The migration principles, placed where the options are weighed — the path's cost and risk belong in the assessment.
    Question to pose: two options with the same end state, one reachable incrementally and one only by big-bang — which wins, and why?
- [EX] Options and fit
  - Workbook — tasks 4 and 5.
  - Identify the design patterns and options open to the practice engagement, then assess their benefits against its business model and needs.
  timer: ~30 min
  image: none
  notes:
    Activity = practice workbook tasks 4–5.
    Push them to judge each option, and to record what they rule out and why — the rejection reasoning is marked skill.
- [TAKEAWAYS] Section 3 · The options
  - Patterns with costs and benefits; fit over maximum.
  - Assess against this business, not in the abstract.
  - A ruled-out option with a reason is analysis, not failure.
  image: none

### C4 — Goals set, decisions confirmed
- Teaches: [ICTCLD504 PC 1.5] · [ICTCLD504 PC 1.6] · [ICTCLD504 PE 3]
- Kicker: the target the improvement is measured against
- [PRIMER] Goals across the four concerns
  - Set business goals across security, reliability, high performance and cost efficiency.
  - A goal is directional and business-owned — "survive a zone failure without data loss" — and it comes from the business requirements, not from the technology you like.
  - "Use Multi-AZ" is a solution masquerading as a goal; the goal is the outcome underneath it.
  image: none
  notes:
    Workbook task 6. The goal-versus-solution confusion is the one to press — have them find the outcome under a technology statement.
- [BESPOKE] Confirm the design decisions
  - Confirm the decisions to carry forward, each one traced to a business need and consistent with the goals just set.
  - This shortlist is what Topics 2 and 3 design in detail — nothing enters the design that wasn't confirmed here.
  - Record what you confirmed and what you deferred; both are decisions.
  image: none
  notes:
    Workbook task 7 closes the analysis. The workbook order is deliberate: goals first, then decisions confirmed against them.
- [EX] Goals and decisions
  - Workbook — tasks 6 and 7.
  - Set the business goals across the four concerns, then confirm the design decisions you will carry into the design work.
  timer: ~25 min
  image: none
  notes:
    Activity = practice workbook tasks 6–7.
    Watch for goals that are really solutions, and confirmations with no trace to a need.
- [TAKEAWAYS] Topic 1 · Key takeaways
  - Review against the pillars; state impact in business language.
  - Read the obligations precisely; assess with evidence.
  - Options judged for fit; goals owned by the business; decisions confirmed against them.
  image: none

### Close
- [BESPOKE] Next: Topic 2 — metrics, and the four-component design
  - The analysis is done: baseline understood, compliance assessed, options weighed, goals set, decisions confirmed.
  - Next the design starts — the metrics that prove it, and the four resource components.
  image: none
  notes:
    The confirmed decisions and the seeded constraint both come forward — tell them to bring the workbook.

## Build notes
~22 slides. Four activities, mapping to practice workbook tasks 1–2 · 3 · 4–5 · 6–7. One generated
diagram (`diagram ledgerline-baseline`, already in `diagrams/`); one decorative `gen` opener hero
(cached in `images/`). Content carried from the 2026-07-02 plan, regrouped to workbook order; new
teaching: the compliance assessment (task 3) — previously untaught in this Topic. Performance metrics
(PC 2.1) move to Topic 2 with task 8.

## Changelog
- 2026-09-08 — redrafted from the AT1 practice workbook (tasks 1–7): compliance assessment added;
  goals-then-decisions order matched to the workbook; metrics moved out to Topic 2.
- 2026-07-02 — authored to full content from coverage.md (Step 4 artefact).
