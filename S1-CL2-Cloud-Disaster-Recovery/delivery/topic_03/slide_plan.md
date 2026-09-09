# Topic 03 DR: requirements & impact analysis — Slide plan
> **Covers:** Topic 03 — see coverage.md
> **Subtitle:** Establish what recovery must achieve, then analyse the risks and their impact
> **STATUS: DRAFT — redrafted 2026-09-08 from the AT1 Part B practice workbook, tasks 20–27 and the
> assessment's knowledge questions Q5–Q6.**

## Depth ceiling
ANALYSIS — the front half of the DR plan on the practice workbook: requirements, current position,
objectives, the data protected, risks, exclusions and impact. The strategy and written plan are
Topic 4; recovery is never executed.

**Answer discipline:** activities run on the practice workbook; the assessment is the same work on the
assessed system. Teach the method on the practice vehicle; never supply assessed-system answers.

## Teaching source
AWS DR concepts (RTO/RPO, risk in the cloud) pinned at Step 4 (TBD); bespoke for requirements
gathering + the impact analysis on the practice scenario.

## AWS pin table
TBD — AWS resilience / DR concept modules (RTO/RPO, risk) to be pinned.

## Slides

### Opener
- [BESPOKE] From design to disaster recovery
  - Topics 1–2 designed the system; Topic 3 asks what happens when part of it fails.
  - This is the front half of the DR plan: the requirements and the impact analysis.
  - You establish what recovery must achieve, then analyse the risks that threaten it.
  - Analysis only — the strategy and the written plan are Topic 4.
  image: gen flat vector hero illustration of a cloud system with a warning shield and a recovery arrow, blue and amber accents, minimal, no text
  notes:
    The pivot from designing the system to protecting it — today runs workbook tasks 20 to 27 in order.
    Misconception: DR starts with backups. It starts with business requirements; technology comes in Topic 4.
    You can't analyse risk against targets you haven't set — that's why the order is fixed.

### C1 — Requirements, and the current recovery position
- Teaches: [ICTCLD501 PC 1.1] · [ICTCLD501 PC 1.2] · [ICTCLD501 PC 1.3]
- Kicker: what must recover, and what's already in place
- [PRIMER] What a DR plan is for
  - A DR plan restores service after a disruptive event, to agreed targets.
  - It is driven by business needs — what the organisation can and cannot tolerate losing.
  - Start by writing down the requirements, not by picking a technology.
  image: none
  notes:
    Requirements-first is the discipline of the whole Topic. "Agreed" matters — recovery is measured against signed-off targets, not best effort.
    Question to pose: two systems go down — why can one wait a day and the other can't? (business tolerance, not technology).
- [BESPOKE] Identify the DR requirements
  - Read the brief: which systems are business-critical, and to whom.
  - Requirements mix availability, integrity and compliance — the business sets each tolerance.
  - State each requirement so it can later be tested against a proposed plan.
  image: none
  notes:
    Workbook task 20's skill. A requirement you can't test is a wish — "highly available" fails, a stated target passes.
    Criticality is relative to a stakeholder; have them name both halves.
- [BESPOKE] Current recovery position and vendor provisions
  - Determine the existing recovery arrangements — what's already in place, and its gaps.
  - Identify the vendor's DR provisions and SLAs: what the provider guarantees versus what you must add.
  - The plan builds on the vendor's native durability; it doesn't reinvent it.
  image: none
  notes:
    Tasks 21 and 22 — you design DR against a baseline, not a blank page.
    Question to pose: the managed database already keeps backups — what's left for your plan to add? (orchestration, priorities, the gaps the SLA leaves).
- [EX] Requirements and current position
  - Workbook — tasks 20, 21 and 22.
  - Record the recovery requirements from the business needs, the existing recovery arrangements, and the vendor provisions and SLAs that apply.
  timer: ~25 min
  image: none
  notes:
    Activity = practice workbook tasks 20–22.
    The common misses: untestable requirements, and skipping the vendor SLAs entirely.
- [TAKEAWAYS] Section 1 · The inputs
  - Requirements before technology, each one testable.
  - Assess what's in place before designing what's missing.
  - The vendor guarantees some of it; your plan covers the rest.
  image: none

### C2 — Recovery objectives, and the data you protect
- Teaches: [ICTCLD501 PC 2.1] · [ICTCLD501 PC 2.3] · [ICTCLD501 KE 5]
- Kicker: how fast back, how much lost, how much data
- [PRIMER] RTO and RPO
  - Recovery Time Objective: how long until service is back.
  - Recovery Point Objective: how much data you can afford to lose.
  - Two different clocks — a system can be back fast yet have lost hours of data, or the reverse.
  image: diagram rto-rpo-timeline
  notes:
    The two numbers everything downstream hangs off. Test the distinction with an example — "back in ten minutes but missing the last hour" is a good RTO and a poor RPO.
    Tighter targets cost more; the trade-off is the teaching point.
- [BESPOKE] Set the objectives to business needs
  - Each objective comes from a business tolerance, not from what the technology happens to offer.
  - Different systems get different objectives — one blanket target over-spends on some and under-protects others.
  - Write the objective next to the requirement that produced it.
  image: none
  notes:
    Workbook task 23. The traceability is the mark: objective beside the business need that set it.
    Push back on round numbers with no source — "why one hour and not four?"
- [BESPOKE] Estimate the data you are protecting
  - What data, how much of it, and how fast it grows — the plan protects a quantity, not an idea.
  - Where it lives, and what state it is in: live, backed up, replicated, or none of these.
  - The estimate sizes the recovery: restoring a gigabyte and a terabyte are different plans.
  image: none
  notes:
    Workbook task 24 — the data inventory. Volume and growth turn an abstract plan into a sized one.
    The "what state is it in" column surfaces the unprotected data — that's the finding.
- [EX] Objectives and data
  - Workbook — tasks 23 and 24.
  - Set the recovery objectives against the business needs, then estimate the data being protected — what, how much, where, and its current state.
  timer: ~25 min
  image: none
  notes:
    Activity = practice workbook tasks 23–24.
    Insist every objective cites the business need that set it.
- [TAKEAWAYS] Section 2 · The targets
  - RTO and RPO are two different clocks.
  - Objectives come from business tolerances, per system.
  - The plan protects a measured quantity of data.
  image: none

### C3 — Risks, exclusions and impact
- Teaches: [ICTCLD501 PC 2.2] · [ICTCLD501 PC 2.4] · [ICTCLD501 PC 2.5] · [ICTCLD501 PE 2] · [ICTCLD501 KE 1] · [ICTCLD501 KE 2]
- Kicker: what threatens it, what's out, what it costs
- [PRIMER] The cloud risk environment, and a method
  - The cloud changes the risks, it doesn't remove them: zone and region outages, misconfiguration, credential compromise, dependency failure.
  - A public, internet-facing system adds its own class: volumetric attack and abuse.
  - Use a method: identify events, rate likelihood and impact, rank — the same way every time, so the ranking is defensible.
  image: none
  notes:
    The examinable pair: what's distinctive about cloud risk, and the method used to rate it — both come back as knowledge questions.
    The method matters more than the ratings; a defensible ranking beats a "right" one.
- [BESPOKE] Assess the major risk events
  - For each event: what happens, how likely, what it hits, and how hard.
  - Rate honestly — a register where everything is high tells the reader nothing.
  - The ranked list is what the strategy in Topic 4 answers, in priority order.
  image: none
  notes:
    Workbook task 25 — the register itself. The rank ordering is the output that drives everything in Topic 4.
    Watch for all-high ratings; force the relative judgement.
- [BESPOKE] Say what the plan does not cover
  - Every plan has edges: events out of scope, systems not covered, decisions deferred.
  - An exclusion stated is a decision; an exclusion discovered during a disaster is a failure.
  - Each exclusion carries a reason — cost, likelihood, or someone else's responsibility.
  image: none
  notes:
    Workbook task 26 — exclusions as deliberate decisions, recorded with reasons.
    This is the slide that stops "the plan covers everything" — nothing does.
- [BESPOKE] Record the outcomes of the impact analysis
  - Bring it together: the events, their ratings, what each would cost the business, and the ranking.
  - The impact is stated in business terms — hours down, data lost, obligations breached — not in technology terms.
  - This record is the evidence the strategy is built on; it must be readable on its own.
  image: none
  notes:
    Workbook task 27 closes the analysis. Business terms are the discipline — "the database is down" is not an impact, "enrolments stop" is.
- [TABLE] Risk register — worked shape
  | Event | Likelihood | Impact | Rank |
  | Zone outage | possible | service degraded, capacity halved | 2 |
  | Region outage | rare | full outage, recovery from backup | 3 |
  | Credential compromise | possible | data exposure, obligation breach | 1 |
  | Volumetric attack | likely | front door degraded for hours | 4 |
  note: A worked shape, not an answer — the practice scenario's events, ratings and ranks are the student's own.
  image: none
- [EX] Risks, exclusions and impact
  - Workbook — tasks 25, 26 and 27.
  - Assess the major risk events, record what the plan excludes and why, then record the outcomes of the impact analysis in business terms.
  - Then rehearse the assessment's Part B questions Q5 and Q6 — the risk environment, and your method — from your own register.
  timer: ~35 min
  image: none
  notes:
    Activity = practice workbook tasks 25–27, then assessment Q5–Q6 rehearsed from their own register.
    The practice workbook carries no questions — use the assessment's, answered from the work just done.
    Press the method question: "how did you rate these, and why that way?"
- [TAKEAWAYS] Topic 3 · Key takeaways
  - Requirements first, each testable; objectives from business tolerances.
  - Two clocks: RTO and RPO. A measured quantity of data.
  - A defensible method, honest ratings, stated exclusions, business-terms impact.
  image: none

### Close
- [BESPOKE] Next: Topic 4 — strategy and plan
  - The analysis is done: targets set, risks ranked, impact recorded.
  - Next you choose the recovery strategy that answers it, and write the plan.
  image: none
  notes:
    Everything in Topic 4 traces back to today's register and objectives — carry them forward.

## Build notes
~23 slides. Three activities, mapping to practice workbook tasks 20–22 · 23–24 · 25–27 + the
assessment's Part B Q5–Q6 (rehearsed from the practice register). One decorative `gen` opener hero
(cached in `images/`). Content carried from the 2026-07-01 plan; new teaching: the exclusions task and
the data-inventory framing.

## Changelog
- 2026-09-08 — redrafted from the AT1 Part B practice workbook (tasks 20–27 + Q5–Q6): exclusions
  taught for the first time; activities point at workbook task numbers.
- 2026-07-01 — authored to full content.
