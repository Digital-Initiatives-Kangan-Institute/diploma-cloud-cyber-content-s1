# Topic 01 Analysing the baseline architecture — Slide plan
> **Covers:** Topic 01 — see coverage.md
> **Subtitle:** Review and evaluate the existing Ledgerline cloud architecture, then set the improvement goals and metrics
> **STATUS: DRAFT** (authored 2026-07-02).

## Depth ceiling
ANALYSIS — review and evaluate the *existing* Ledgerline architecture and set the improvement goals + metrics. Diagnose and justify; do not design the changes (Topics 2–3) and do not implement (AT3).

## Teaching source
AWS well-architected review (reliability / performance / cost / security pillars) pinned at Step 4 (TBD); bespoke for the Ledgerline single-AZ baseline framing and the goals-and-metrics discipline.

## AWS pin table
TBD — AWS ICTCLD504/architecture modules to be pinned.

## Slides

### Opener
- [BESPOKE] From analysis to improvement
  - Topic 1 opens AT1: before you improve a cloud system you first understand the one you have.
  - This Topic is the analysis half of the Solution Design — review the baseline, evaluate it, set the goals. The design of the fix is Topics 2–4.
  - Vehicle: **Ledgerline**, YAT's Accounting system, runs single-AZ in the cloud — the system you analyse and improve.
  - Stay at analysis: diagnose and justify, don't design the changes yet.
  image: gen flat vector hero illustration of an analyst reviewing a cloud architecture diagram, magnifying glass over a data centre, blue and gold accents, minimal, no text
  notes:
    Frame the whole cluster's opening move — before you improve a cloud system you first understand the
    one you have. This is the ANALYSIS half of AT1's Solution Design; set the posture, don't teach a
    section yet.
    • First two bullets: Topic 1 opens AT1 — review the baseline, evaluate it, set the goals; the design
    of the fix is Topics 2–4. Diagnosis precedes design.
    • Third bullet: name the vehicle — Ledgerline, YAT's Accounting system, running single-AZ in the
    cloud. It is the system they analyse and improve for the assessment.
    • Fourth bullet (the discipline): stay at analysis — diagnose and justify, do NOT design the changes
    yet. Hold that line all Topic.
    Misconception to pre-empt: "we already know the fix is Multi-AZ, let's design it." No — you must first
    review, evaluate business impact and set goals; a fix proposed before the goals exist has nothing to
    be measured against.
    Question to pose: "Why analyse a system you're about to change — why not go straight to the
    improvement?" (you can't justify or measure a change without the baseline + goals it answers).
    UoC/AT1 tie: this Topic develops ICTCLD504 PC 1.1–1.6, PC 2.1 and PE 3; the output is the analysis +
    goals/metrics sections of the AT1 Solution Design.

### C1 — Reviewing the baseline
- Teaches: [ICTCLD504 PC 1.1] · [ICTCLD504 PC 1.2] · [ICTCLD504 KE 1] · [ICTCLD504 KE 2] · [ICTCLD504 KE 3]
- Kicker: understand what you have before you change it
- [PRIMER] How to review a cloud architecture
  - A structured review reads an architecture against pillars: security, reliability, performance, cost.
  - Frame the review with industry technology standards used in cloud solutions (KE 1) and the standard hardware/software products the platform is built on — compute families, managed databases, object/block storage (KE 2).
  - Keep the method vendor-neutral here; you apply it to Ledgerline (a real AWS baseline) next.
  image: none
  notes:
    Open Section 1 with the vendor-neutral METHOD — how you read any cloud architecture — before applying
    it to Ledgerline. This is a technique slide; teach the frame, not the system yet.
    • First bullet: a structured review reads an architecture against pillars — security, reliability,
    performance, cost. Name the four; they recur all cluster.
    • Second bullet: frame the review with the industry technology standards used in cloud solutions
    (KE 1) and the standard hardware/software products the platform is built on — compute families,
    managed databases, object/block storage (KE 2). This is the vocabulary the review is written in.
    • Third bullet: keep it vendor-neutral HERE; they apply it to Ledgerline, a real AWS baseline, on the
    next slide.
    Misconception to pre-empt: "reviewing = listing what's there." No — a review EVALUATES against the
    pillars; an inventory with no judgement isn't a review.
    Question to pose: "Name the four pillars you read an architecture against — and which one a single-AZ
    design most obviously fails." (reliability — sets up the Ledgerline slide).
    UoC/AT1 tie: ICTCLD504 KE 1 / KE 2 (the standards + standard products the review draws on) → AT1
    Solution Design baseline analysis + the Part A KE appendix.
- [BESPOKE] Review the Ledgerline baseline
  - Identify and review Ledgerline's current cloud architecture: a VPC, one Availability Zone, an app tier and a single RDS database.
  - Read the topology top-down — network, compute, database, storage — and note how each resource is deployed today.
  - Cloud adoption changes the IT system: managed services, elasticity and shared responsibility reshape how you run and improve it (KE 3).
  image: diagram ledgerline-baseline
  notes:
    Apply the method to the actual system — walk the Ledgerline baseline off the diagram so students can
    SEE the single-AZ topology they'll evaluate next.
    • First bullet: identify and review the current architecture — a VPC, ONE Availability Zone, an app
    tier and a single RDS database. Point to each on the diagram.
    • Second bullet: read the topology top-down — network → compute → database → storage — noting how each
    resource is deployed today. Model the reading order; it's the same order they'll design in.
    • Third bullet: cloud adoption reshapes the IT system — managed services, elasticity and shared
    responsibility change how you run and improve it (KE 3). This is why "review" here isn't the same as
    reviewing an on-prem box.
    Misconception to pre-empt: "single-AZ just means one server." No — it means every tier shares one
    failure domain; the whole VPC's resources sit in one AZ, so one AZ outage takes it all down.
    Question to pose: "Trace the request path on the diagram — where is the single point of failure?"
    (the one AZ; every tier lives in it).
    UoC/AT1 tie: ICTCLD504 PC 1.1 (identify & review the architecture) + KE 3 → AT1 Solution Design
    baseline section.
- [BESPOKE] Evaluate the design decisions & their business impact
  - Evaluate the baseline and name the business impact of its design decisions: single-AZ means single points of failure — one AZ outage takes Accounting down.
  - A seeded constraint surfaces here: the accounting product is **vendor-certified single-instance only → the database cannot go Multi-AZ**. Record it now — it is the reliability cost-benefit centrepiece in Topic 2.
  - Impact is a business statement, not a technical one: downtime, lost billing, risk to close-of-month — the language the goals in C3 answer.
  image: none
  notes:
    The evaluation slide — teach students to state impact in BUSINESS terms, and plant the constraint that
    drives the whole cluster. This is the analytical heart of Section 1.
    • First bullet: evaluate the baseline and name the business impact of its design decisions — single-AZ
    means single points of failure; one AZ outage takes Accounting down.
    • Second bullet (plant it deliberately): the accounting product is vendor-certified single-instance
    only, so the database CANNOT go Multi-AZ. Have them write it down now — it is the reliability
    cost-benefit centrepiece in Topic 2.
    • Third bullet: impact is a BUSINESS statement, not a technical one — downtime, lost billing, risk to
    close-of-month. That's the language the goals in C3 will answer.
    Misconception to pre-empt: "the impact is 'the server goes down'." No — that's the technical event; the
    business impact is what it COSTS (billing halts, month-end close at risk). Push them from event to cost.
    Question to pose: "If the single AZ fails during end-of-month close, what does that cost YAT — in
    business terms?" (draws out the impact language the goals answer).
    UoC/AT1 tie: ICTCLD504 PC 1.2 (evaluate architecture & identify business impact of design decisions) →
    AT1 Solution Design baseline analysis.
- [EX] Review the practice baseline
  - On the **practice engagement (the website)**, identify and review its current architecture the same way.
  - Evaluate it and name the business impact of its design decisions — where would an outage or a bottleneck hurt the business?
  timer: ~25 min
  image: none
  notes:
    Facilitation — the Section 1 practice; students run the SAME baseline review on the practice
    engagement (the website) before doing it on Ledgerline for the assessment.
    Tell students: "On the practice engagement — the website — identify and review its current
    architecture the same way we just read Ledgerline. Evaluate it and name the business impact of its
    design decisions."
    Steps (put on the board):
    1. Read the practice architecture top-down — network, compute, database, storage.
    2. Note how each tier is deployed today and where a single failure or bottleneck sits.
    3. For each weak point, write the BUSINESS impact — where would an outage or a bottleneck hurt the
    business?
    Must produce: a short written review of the practice baseline with at least two business-impact
    statements (not technical events).
    Timing: ~25 min then discuss. Where they get stuck: they list resources without evaluating them —
    circulate and push "so what does that cost the business?"; also watch for technical-only impacts.
    Share-back prompt: take one student's biggest business impact and ask the room whether it's stated in
    business or technical language.
    No-leakage note: the website is the PRACTICE vehicle — AT1 assesses this same review skill on
    Ledgerline (comparable, not identical); keep them on the practice engagement here.

### C2 — Options & fit against the business model
- Teaches: [ICTCLD504 PC 1.3] · [ICTCLD504 PC 1.4] · [ICTCLD504 PC 1.5]
- Kicker: what could change, and what fits the business
- [PRIMER] Design patterns & architectural options
  - Identify the options available to a cloud architecture: multi-AZ redundancy, horizontal scaling and load balancing, managed vs self-run data tiers, caching, decoupling.
  - Each option is a pattern with a cost and a benefit — there is no single right answer, only a fit.
  - The four improvement concerns to weigh against: security, reliability, scalability, cost.
  image: none
  notes:
    Open Section 2 with the OPTION SPACE — the patterns a cloud architecture can use — kept deliberately
    abstract so the next slide can narrow them to Ledgerline. A menu, not a decision.
    • First bullet: name the options — Multi-AZ redundancy, horizontal scaling + load balancing, managed
    vs self-run data tiers, caching, decoupling. Give each a one-line "what it buys."
    • Second bullet (the framing): each option is a pattern with a COST and a BENEFIT — there is no single
    right answer, only a fit to the business. This is the mindset the whole cluster runs on.
    • Third bullet: the four improvement concerns you weigh options against — security, reliability,
    scalability, cost.
    Misconception to pre-empt: "more redundancy / more scaling is always better." No — every option costs;
    the skill is fit, not maximising. Gold-plating loses marks.
    Question to pose: "Multi-AZ improves reliability — so should every system have it?" (No — only where the
    reliability benefit justifies the cost; sets up the Ledgerline DB call in Topic 2).
    UoC/AT1 tie: ICTCLD504 PC 1.3 (identify design patterns & architectural options) → AT1 Solution Design
    options analysis.
- [BESPOKE] Assess the options against Ledgerline & confirm decisions
  - Determine and assess the benefits and differences of cloud/architectural options **against Ledgerline's current business model and needs** — not in the abstract.
  - Weigh what fits: the single-instance DB constraint rules some reliability options out, which sharpens the ones that remain.
  - Confirm the system design decisions to carry forward according to business needs — the shortlist Topics 2–3 will actually design.
  image: none
  notes:
    Narrow the menu to Ledgerline — teach students to assess options AGAINST a specific business model,
    then commit to a shortlist. This is where analysis becomes decisions.
    • First bullet: determine and assess the benefits and differences of the options against Ledgerline's
    CURRENT business model and needs — not in the abstract. The same option can be right for one business
    and wrong for another.
    • Second bullet: the single-instance-DB constraint (from C1) rules some reliability options out — which
    actually SHARPENS the ones that remain. A constraint is analytical signal, not just a limitation.
    • Third bullet: confirm the system design decisions to carry forward according to business needs — the
    shortlist Topics 2–3 will actually design.
    Misconception to pre-empt: "assess = describe each option." No — assess means judge FIT and pick; they
    must end with confirmed decisions, not a balanced-sounding list.
    Question to pose: "The single-instance DB rules out a Multi-AZ database — does that make the analysis
    harder or easier?" (easier — it removes an option, so you argue the remaining ones).
    UoC/AT1 tie: ICTCLD504 PC 1.4 (assess options against the business model) + PC 1.5 (confirm design
    decisions) → AT1 Solution Design options + decisions.
- [EX] Weigh options on the practice engagement
  - For the practice engagement, list the architectural options open to it and assess each against its business model and needs.
  - Confirm the design decisions worth carrying forward — and note the ones you rule out and why.
  timer: ~25 min
  image: none
  notes:
    Facilitation — the Section 2 practice; students list and assess options for the practice engagement,
    then commit to decisions — mirroring the Ledgerline options work.
    Tell students: "For the practice engagement, list the architectural options open to it and assess each
    against its business model and needs. Then confirm which decisions you'd carry forward — and note what
    you rule out, and why."
    Steps (put on the board):
    1. List the options open to the practice architecture (redundancy, scaling, managed vs self-run,
    caching, decoupling).
    2. Assess each against the practice engagement's business model and needs — cost vs benefit, fit not
    maximum.
    3. Confirm the decisions worth carrying forward; record the ones you RULE OUT and the reason.
    Must produce: a shortlist of confirmed design decisions plus a short "ruled out, because…" list.
    Timing: ~25 min then discuss. Where they get stuck: they keep every option "just in case" — push them
    to commit and to justify a rejection (rejecting an option with a reason is a marked skill).
    Share-back prompt: ask one student for an option they RULED OUT and why — the reasoning is the skill.
    No-leakage note: the website is the practice vehicle; AT1 assesses the same options-and-decisions skill
    on Ledgerline — comparable, not identical.

### C3 — Goals & metrics
- Teaches: [ICTCLD504 PC 1.6] · [ICTCLD504 PC 2.1] · [ICTCLD504 PE 3]
- Kicker: set the target the improvement is measured against
- [PRIMER] Goals across the four concerns
  - Set business goals across the four well-architected concerns: security, reliability, high-performance and cost efficiency (PC 1.6, PE 3).
  - A goal is directional and business-owned ("survive an AZ failure without data loss"); a metric makes it measurable.
  - Goals come from business requirements and needs, not from the technology you happen to like.
  image: none
  notes:
    Open Section 3 by teaching what a GOAL is versus a METRIC — the yardstick discipline the whole
    improvement is later measured against.
    • First bullet: set business goals across the four well-architected concerns — security, reliability,
    high-performance and cost efficiency (PC 1.6, PE 3).
    • Second bullet: a goal is directional and business-owned ("survive an AZ failure without data loss");
    a METRIC makes it measurable (availability %, RTO/RPO). Say both words; students blur them.
    • Third bullet: goals come from business REQUIREMENTS and needs — not from the technology you happen to
    like. Technology-led goals are the classic trap.
    Misconception to pre-empt: "the goal is 'use Multi-AZ'." No — that's a solution masquerading as a goal;
    the goal is the business outcome ("survive an AZ failure"), and the solution is chosen to meet it.
    Question to pose: "'Go Multi-AZ' — is that a goal or a solution? What's the goal underneath it?"
    (survive an AZ failure without data loss — the outcome the solution serves).
    UoC/AT1 tie: ICTCLD504 PC 1.6 + PE 3 (set business goals across the four concerns) → AT1 Solution
    Design goals section.
- [BESPOKE] Set Ledgerline's goals & confirm the metrics
  - Set the security / reliability / high-performance / cost goals for Ledgerline from its business requirements.
  - Evaluate and confirm the performance metrics the improved application is measured against — availability %, RTO/RPO, response time, cost per period (PC 2.1).
  - These goals and metrics are the yardstick for the design (Topics 2–3) and the AT3 build — write them so a later Topic can test against them.
  image: none
  notes:
    Apply the goal/metric discipline to Ledgerline — set concrete goals and confirm the metrics that make
    them testable. This slide produces the yardstick the rest of the cluster measures against.
    • First bullet: set the security / reliability / high-performance / cost goals for Ledgerline FROM its
    business requirements — trace each to a stated need.
    • Second bullet: evaluate and confirm the performance METRICS the improved application is measured
    against — availability %, RTO/RPO, response time, cost per period (PC 2.1). A goal without a metric
    can't be tested.
    • Third bullet (the payoff): write them so a LATER Topic can test against them — these goals and
    metrics are the yardstick for the design (Topics 2–3) and the AT3 build.
    Misconception to pre-empt: "the metric is 'be reliable'." No — that's the goal restated; a metric is a
    number with a target (e.g. availability ≥ 99.5%, RTO ≤ 1 business day). Push them to numbers.
    Question to pose: "Reliability goal: survive an AZ failure. What metric proves it, and what's the
    target?" (availability % / RTO / RPO with a number).
    UoC/AT1 tie: ICTCLD504 PC 1.6 (goals) + PC 2.1 (confirm performance metrics) + PE 3 → AT1 Solution
    Design goals & metrics sections.
- [EX] Draft goals & metrics for the practice engagement
  - For the practice engagement, set the goals across security, reliability, performance and cost.
  - Confirm the metrics each goal is measured by — you will design against them in the practice work that mirrors Topics 2–3.
  timer: ~25 min
  image: none
  notes:
    Facilitation — the Section 3 practice; students set goals + metrics for the practice engagement, the
    yardstick they'll design against in the practice work that mirrors Topics 2–3.
    Tell students: "For the practice engagement, set goals across security, reliability, performance and
    cost. Then confirm the metric each goal is measured by — a number with a target."
    Steps (put on the board):
    1. Write one goal per concern — security, reliability, performance, cost — each traced to a business
    need.
    2. For each goal, confirm the metric that proves it and set a target (availability %, RTO/RPO, response
    time, cost per period).
    3. Sanity-check: could a later Topic TEST against these? If not, tighten them.
    Must produce: four goals, each with a named metric and a target value.
    Timing: ~25 min then discuss. Where they get stuck: goals that are really solutions ("use auto
    scaling"), and metrics with no number — circulate and push outcome-goals + numeric targets.
    Share-back prompt: take one goal/metric pair and ask the room whether the metric actually proves the
    goal.
    No-leakage note: the website is the practice vehicle; AT1 assesses goal/metric setting on Ledgerline —
    comparable, not identical.
- [TAKEAWAYS] Topic 1 · Key takeaways
  - Review the baseline against the four pillars before changing anything; name the business impact of each design decision.
  - Ledgerline is single-AZ with a **vendor-certified single-instance DB that cannot go Multi-AZ** — carry that constraint into Topic 2.
  - Assess options against the business model, then confirm the decisions to carry forward.
  - Set goals across security, reliability, performance and cost, and confirm the metrics — that is the yardstick for the whole improvement.
  image: none

### Close
- [BESPOKE] Next: Topic 2 — designing the reliability improvements
  - You've reviewed the baseline, weighed the options and set the goals; next you design the reliability changes.
  - Bring the single-instance-DB constraint — it is the reliability cost-benefit centrepiece Topic 2 opens on.
  image: none

## Build notes
~13 slides. Depth ceiling ANALYSIS — no design of the fix. Worked examples use Ledgerline; the three `[EX]`s run the same analysis on the practice engagement (the website). One generated technical diagram (`diagram ledgerline-baseline` — single-AZ VPC, one AZ, app tier + single RDS, single points of failure); one decorative `gen` image (opener hero); every other slide `image: none`.

## Changelog
- 2026-07-02 — authored to full content from coverage.md (Step 4 artefact).
