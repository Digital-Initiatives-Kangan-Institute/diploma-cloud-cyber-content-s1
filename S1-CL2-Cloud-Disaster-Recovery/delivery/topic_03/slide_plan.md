# Topic 03 DR: requirements & impact analysis — Slide plan
> **Covers:** Topic 03 — see coverage.md
> **Subtitle:** Establish what recovery must achieve, then analyse the risks and their impact
> **STATUS: DRAFT** (authored 2026-07-01).

## Depth ceiling
ANALYSIS — develop the DR plan requirements and the impact analysis (the front half of the DR-plan lifecycle) for the system designed in Topics 1–2. The recovery strategy and finalised plan are Topic 4; recovery is not executed.

## Teaching source
AWS DR concepts (RTO/RPO, risk in the cloud) pinned at Step 4 (TBD); bespoke for requirements gathering + the impact analysis on the practice scenario.

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
    Frame the pivot — from designing the system (Topics 1–2) to protecting it. This is the front half of the DR lifecycle; set the two moves and the boundary.
    • First bullet: Topics 1–2 built the system; Topic 3 asks what happens when part of it FAILS. The question flips from "how does it run?" to "how does it recover?"
    • Second bullet: locate the Topic — this is the FRONT HALF of the DR plan: the requirements and the impact analysis. The back half (strategy + written plan) is Topic 4.
    • Third bullet: name the two moves — establish what recovery must ACHIEVE (requirements + objectives), then analyse the RISKS that threaten it (impact analysis). In that order; you can't analyse risk against targets you haven't set.
    • Hold the boundary (last bullet): ANALYSIS ONLY — the strategy and the written plan are Topic 4; recovery is never executed here.
    Misconception to pre-empt: "DR is about backups/technology." No — it starts with BUSINESS requirements and risk analysis; the technology choice comes later (Topic 4). Lead with the business, not the tool.
    Question to pose: "Before you can say how to recover a system, what two things must you establish first?" (what recovery must achieve — the requirements/objectives — and what threatens it — the risks).
    UoC/AT1 tie: this Topic develops [ICTCLD501 PC 1.1]–[ICTCLD501 PC 1.3], [ICTCLD501 PC 2.1]–[ICTCLD501 PC 2.5], [ICTCLD501 PE 2] and [ICTCLD501 KE 1]/[ICTCLD501 KE 2]/[ICTCLD501 KE 5], evidenced in AT1 Part B §1–2 and the Part B KE appendix.

### C1 — Plan requirements & current recovery position
- Teaches: [ICTCLD501 PC 1.1] · [ICTCLD501 PC 1.2] · [ICTCLD501 PC 1.3]
- Kicker: what must recover, and what's already in place
- [PRIMER] What a DR plan is for
  - A DR plan restores service after a disruptive event, to agreed targets.
  - It is driven by business needs — what the organisation can and cannot tolerate losing.
  - Start by writing down the requirements, not by picking a technology.
  image: none
  notes:
    Install the purpose of a DR plan — vendor-neutral. Keep it tight; it sets the "requirements before technology" discipline for the whole Topic.
    • First bullet: a DR plan RESTORES service after a disruptive event, to AGREED targets. "Agreed" matters — recovery is measured against targets the business signed off, not best effort.
    • Second bullet: it's driven by BUSINESS NEEDS — what the organisation can and cannot tolerate losing. The business sets the tolerance; the plan serves it.
    • Third bullet (accent it): START by writing down the REQUIREMENTS, not by picking a technology. Leading with "we'll use backups" is the classic mistake — requirements first.
    Misconception to pre-empt: "DR planning = choosing a backup product." No — that's the last step; you first establish what must recover, how fast, and against which risks. Technology is chosen to meet requirements, not the reverse.
    Question to pose: "Two systems both go down — why might one need recovery in minutes and the other can wait a day?" (business tolerance differs; the requirement, not the tech, decides).
    UoC/AT1 tie: [ICTCLD501 PC 1.1] (identify DR requirements per business needs) — the requirements-first mindset AT1 Part B §1 rewards.
- [BESPOKE] Identify the DR requirements
  - Read the engagement brief: which systems are business-critical, and to whom.
  - Requirements come from the business — enrolment front-door uptime, financial-record integrity, residency.
  - State each requirement so it can later be tested against a proposed plan.
  image: none
  notes:
    Teach how to ELICIT the DR requirements from the brief — the first concrete C1 skill. A consultant reads the brief; they don't guess.
    • First bullet: read the engagement brief — which systems are business-CRITICAL, and TO WHOM. Criticality is relative to a stakeholder; name both.
    • Second bullet: requirements come from the BUSINESS — worked examples: enrolment front-door uptime, financial-record integrity, residency. Note the mix of availability, integrity and compliance requirements.
    • Third bullet (accent it): STATE each requirement so it can later be TESTED against a proposed plan. A requirement you can't test is a wish — make it checkable ("front door available 99.5%", not "highly available").
    Misconception to pre-empt: "all systems are equally critical." No — DR is about PRIORITISATION; some systems justify expensive fast recovery, others don't. Naming criticality per stakeholder is the analytical work.
    Question to pose: "'The system should be reliable' — why is that useless as a DR requirement, and how would you fix it?" (untestable; restate as a measurable target the plan can be checked against).
    UoC/AT1 tie: [ICTCLD501 PC 1.1] (identify DR requirements per business needs) — AT1 Part B B1.
- [BESPOKE] Current recovery position & vendor provisions
  - Determine the existing organisational recovery arrangements — what's already in place, and its gaps.
  - Identify the cloud vendor's DR provisions and SLAs: what the provider guarantees vs what you must add.
  - The plan builds on the vendor's native durability, it doesn't reinvent it.
  image: none
  notes:
    Teach the second and third C1 inputs — the CURRENT recovery position and the VENDOR's provisions. You design DR against a baseline, not a blank page.
    • First bullet: determine the EXISTING organisational recovery arrangements — what's already in place, AND its gaps. You can only improve what you've first assessed.
    • Second bullet: identify the cloud vendor's DR provisions and SLAs — what the provider GUARANTEES versus what YOU must add. Draw the line explicitly; it's the shared-responsibility idea applied to recovery.
    • Third bullet (accent it): the plan BUILDS ON the vendor's native durability — it doesn't REINVENT it. Re-implementing what the provider already guarantees is wasted effort and often less reliable.
    Misconception to pre-empt: "we must build all recovery ourselves." No — much durability is native (managed-service backups, cross-region copy); your plan sequences and governs it, filling only the gaps the SLA leaves.
    Question to pose: "The managed database already keeps automated backups — so what's left for YOUR plan to add?" (orchestration, priorities, the parts the SLA doesn't cover, and meeting a tighter RTO/RPO than the default).
    UoC/AT1 tie: [ICTCLD501 PC 1.2] (determine existing recovery plans) + [ICTCLD501 PC 1.3] (identify vendor DR plan and SLAs) — AT1 Part B B2.
- [EX] Gather requirements & current position
  - For the practice scenario, list the DR plan requirements from the business needs.
  - Record the current recovery arrangements and the relevant vendor DR provisions/SLAs.
  timer: ~20 min
  image: none
  notes:
    Facilitation — the C1 practice: gather requirements + the current recovery position on the PRACTICE scenario. Rehearses AT1 Part B B1–B2.
    Tell students: "On the practice scenario, list the DR requirements that come from the business needs — testable ones — then record what recovery is already in place and the relevant vendor DR provisions and SLAs."
    Steps (put on the board):
    1. From the brief, list the DR requirements per business need — each stated so it can be TESTED (a measurable target, a named stakeholder).
    2. Record the current recovery arrangements — what's in place and its gaps.
    3. Note the vendor's DR provisions/SLAs — what's guaranteed vs what you must add.
    Must produce: a testable requirements list plus a short current-position note (existing arrangements + vendor SLAs).
    Timing: ~20 min. Where they get stuck: they write vague requirements ("be reliable") — push measurable, testable statements; and they skip the vendor SLAs (remind them the plan builds on native durability).
    Share-back prompt: "Give me one requirement and how you'd TEST a plan against it" — listen for testability.
    No-leakage note: this runs on the PRACTICE scenario (comparable, not identical); AT1 evidences the same requirements-gathering skill on the assessed system — keep them on the practice brief.
    UoC/AT1 tie: [ICTCLD501 PC 1.1] · [ICTCLD501 PC 1.2] · [ICTCLD501 PC 1.3] — the requirements + current-position pair that opens AT1 Part B.

### C2 — Recovery objectives & data managed
- Teaches: [ICTCLD501 PC 2.1] · [ICTCLD501 PC 2.3] · [ICTCLD501 KE 5]
- Kicker: how fast, how recent, how much
- [PRIMER] RTO & RPO
  - RTO (Recovery Time Objective): how long you can be down before it hurts too much.
  - RPO (Recovery Point Objective): how much recent data you can afford to lose.
  - They are business decisions expressed as time; every DR choice traces back to them.
  image: diagram rto-rpo-timeline
  notes:
    The two most important terms in DR — teach RTO and RPO on the timeline diagram; students routinely confuse them, so nail the distinction with the picture.
    • Use the diagram's timeline: the disaster is the point in the middle. RTO measures FORWARD (how long until service is back); RPO measures BACKWARD (how much recent data is lost between the last good copy and the disaster).
    • RTO (first bullet): how long you can be DOWN before it hurts too much — a TIME target for restoration.
    • RPO (second bullet): how much recent DATA you can afford to lose — a target for the gap back to the last recoverable point.
    • Third bullet (accent it): both are BUSINESS decisions expressed as TIME; every DR choice traces back to them. The strategy in Topic 4 is chosen to hit these numbers.
    Misconception to pre-empt: students swap them constantly. Anchor it: RTO = TIME to recover (forward); RPO = data you can lose (backward). Point at the two arrows on the diagram every time you say the words.
    Question to pose: "A one-hour RPO — what does that actually mean happened to the last hour of data after a failure?" (up to an hour of the most recent data may be lost; backups/replication must be at least that frequent).
    UoC/AT1 tie: [ICTCLD501 KE 5] (RTO/RPO standards and techniques) + [ICTCLD501 PC 2.1] (determine RTO/RPO to business needs) — AT1 Part B B3 and the KE appendix.
- [BESPOKE] Set the objectives to business needs
  - Derive RTO/RPO from the requirements — the front door tolerates little downtime; financial records tolerate little data loss.
  - Explain each: what business consequence the target avoids.
  - Tighter targets cost more — set them to the need, not to the maximum.
  image: none
  notes:
    Apply RTO/RPO to THIS engagement — derive the numbers from the requirements, not from a wish for zero. This is where the concept becomes a design decision.
    • First bullet: DERIVE RTO/RPO from the requirements — worked contrast: the enrolment FRONT DOOR tolerates little DOWNTIME (tight RTO); FINANCIAL RECORDS tolerate little DATA LOSS (tight RPO). Different systems, different pressures — set each independently.
    • Second bullet: EXPLAIN each target by the business CONSEQUENCE it avoids — "RTO one hour because a longer outage loses enrolments during the campaign." The justification is assessable, not just the number.
    • Third bullet (accent it): TIGHTER targets COST MORE — set them to the NEED, not the maximum. Everyone wants near-zero; the skill is matching the target to the tolerance, not gold-plating.
    Misconception to pre-empt: "set RTO/RPO as low as possible to be safe." No — near-zero targets force expensive active-active designs; over-specifying is a marked-down failure to match need to cost.
    Question to pose: "Why might the financial-records system have a TIGHT RPO but a LOOSER RTO than the public front door?" (losing financial data is intolerable; being briefly offline is survivable — the two objectives decouple).
    UoC/AT1 tie: [ICTCLD501 PC 2.1] (determine and explain RTO/RPO to business needs) — AT1 Part B B3; the explanation is what earns the criterion.
- [BESPOKE] Estimate the data managed
  - Estimate the amount of data the plan must protect and recover.
  - Classify its security level — personal, financial, operational — which drives handling and residency.
  - The volume and sensitivity shape both RPO and the recovery method.
  image: none
  notes:
    Teach the DATA-managed estimate — the second C2 output. Recovery is shaped by how much data there is and how sensitive it is.
    • First bullet: ESTIMATE the amount of data the plan must protect and recover. Volume affects how long a restore takes — it feeds directly into whether an RTO is achievable.
    • Second bullet: CLASSIFY its security level — personal, financial, operational — which drives HANDLING and RESIDENCY. India-cohort personal data carries residency obligations; classification isn't academic.
    • Third bullet (accent it): VOLUME and SENSITIVITY shape both the RPO and the recovery METHOD — big/sensitive data changes both how recent your copy must be and where/how you're allowed to keep it.
    Misconception to pre-empt: "the data estimate is just a size in GB." No — it's amount AND security level; the classification drives residency and handling rules that constrain the whole recovery method, not just storage cost.
    Question to pose: "You have 2 TB of India-cohort personal data — name two things that estimate constrains in the plan." (restore time vs RTO, and where copies may legally live — residency).
    UoC/AT1 tie: [ICTCLD501 PC 2.3] (estimate amount and security level of data managed) — AT1 Part B B4.
- [EX] Determine RTO/RPO & data managed
  - For the practice scenario, determine and explain RTO and RPO to the business needs.
  - Estimate the amount and security level of the data managed.
  timer: ~20 min
  image: none
  notes:
    Facilitation — the C2 practice: set and EXPLAIN RTO/RPO and estimate the data on the PRACTICE scenario. Rehearses AT1 Part B B3–B4.
    Tell students: "For the practice scenario, determine RTO and RPO for the critical systems and EXPLAIN each to the business need. Then estimate the amount and security level of the data the plan manages."
    Steps (put on the board):
    1. For each critical system, set an RTO and an RPO — and write the business consequence each target avoids.
    2. Match the target to the need — don't default to near-zero; note the cost trade-off.
    3. Estimate the data managed: amount, and security classification (personal/financial/operational) with its residency implication.
    Must produce: RTO/RPO per critical system WITH explanations, plus a data estimate (amount + classification).
    Timing: ~20 min. Where they get stuck: they give numbers with no justification (the explanation is the mark), and they set everything to near-zero (push them to match target to tolerance and note cost).
    Share-back prompt: "Give me one RTO and the business consequence it's set to avoid" — listen for the justification, not just the number.
    No-leakage note: practice scenario only (comparable, not identical); AT1 evidences the same objectives-and-data skill on the assessed system — keep them on the practice brief.
    UoC/AT1 tie: [ICTCLD501 PC 2.1] · [ICTCLD501 PC 2.3] · [ICTCLD501 KE 5] — recovery objectives + data managed (AT1 Part B B3–B4).

### C3 — Risk & impact analysis
- Teaches: [ICTCLD501 PC 2.2] · [ICTCLD501 PC 2.4] · [ICTCLD501 PC 2.5] · [ICTCLD501 PE 2] · [ICTCLD501 KE 1] · [ICTCLD501 KE 2]
- Kicker: likelihood times impact equals severity
- [PRIMER] The cloud risk environment & analysis method
  - The cloud risk environment: region/AZ outages, misconfiguration, dependency failure, human error, malicious action.
  - A data-analysis methodology turns those into a comparable picture — likelihood and impact scored consistently.
  - Risk analysis is systematic, not a guess: same scale for every event.
  image: none
  notes:
    Open C3 — the risk half. Teach WHAT can go wrong in the cloud and the METHOD for analysing it consistently. Vendor-neutral; sets up the assessment activity.
    • First bullet: name the cloud RISK ENVIRONMENT — region/AZ outages, misconfiguration, dependency failure, human error, malicious action. Note most real incidents are NOT dramatic region outages; misconfiguration and human error dominate.
    • Second bullet: a DATA-ANALYSIS METHODOLOGY turns those into a COMPARABLE picture — likelihood and impact scored CONSISTENTLY, so events can be ranked against each other.
    • Third bullet (accent it): risk analysis is SYSTEMATIC, not a guess — the SAME scale for every event. Consistency is what makes the ranking meaningful.
    Misconception to pre-empt: "the big risk is a data-centre disaster." No — the common risks are misconfiguration and human error; a plan that only guards against region outages misses where incidents actually come from.
    Question to pose: "Two people score the same risk 'high' and 'medium' — what's missing that would make them agree?" (a defined, shared scale — the methodology; without it the scores aren't comparable).
    UoC/AT1 tie: [ICTCLD501 KE 1] (cloud risk environments) + [ICTCLD501 KE 2] (data-analysis methodologies) — the foundation for the risk assessment (PC 2.2/2.4/2.5, PE 2) in AT1 Part B.
- [BESPOKE] Assess the major risk events
  - Assess at least three major risk events: for each, its likelihood and its impact.
  - Severity = likelihood x impact; rank the events so the plan can prioritise.
  - Record plan exclusions — the risks the plan deliberately does not cover, and why.
  image: none
  notes:
    Teach the risk ASSESSMENT itself — the mechanical heart of the impact analysis. This defines exactly what the activity produces.
    • First bullet: assess at least THREE major risk events — for each, its LIKELIHOOD and its IMPACT scored on the shared scale. Three is the assessed minimum (PE 2), not a target to stop at.
    • Second bullet: SEVERITY = likelihood × impact; RANK the events so the plan can PRIORITISE. The ranking is the whole point — it tells Topic 4 what to protect first.
    • Third bullet (accent it): record plan EXCLUSIONS — the risks the plan deliberately does NOT cover, and WHY. Naming what's out of scope, with justification, is a mark of a mature plan, not a gap in it.
    Misconception to pre-empt: "more risks listed = better." No — three well-analysed, ranked risks beat a long unscored list; and a plan with NO stated exclusions is naive, not thorough.
    Question to pose: "A low-likelihood, high-impact event vs a high-likelihood, low-impact one — how does severity = likelihood × impact help you rank them?" (it forces a single comparable score; discuss where they land).
    UoC/AT1 tie: [ICTCLD501 PC 2.2] (assess risks + plan exclusions) + [ICTCLD501 PE 2] (determine likelihood and impact for the DR plan) — AT1 Part B B5.
- [BESPOKE] Evaluate impact & document outcomes
  - Evaluate the severity of impact and disruption of each event on the business.
  - Document the impact-analysis outcomes per organisational policies and procedures.
  - The documented analysis is the input the Topic 4 recovery plan is built from.
  image: none
  notes:
    Teach the last C3 step — evaluate the business impact and DOCUMENT the outcomes properly. This closes the front half and feeds Topic 4.
    • First bullet: EVALUATE the severity of IMPACT and DISRUPTION of each event ON THE BUSINESS — translate the score into business terms (lost enrolments, breached obligation), not just "high".
    • Second bullet: DOCUMENT the impact-analysis outcomes per ORGANISATIONAL POLICIES and procedures — the write-up has a required form; documenting to policy is itself assessed (PC 2.5).
    • Third bullet (accent it): the documented analysis is the INPUT the Topic 4 recovery plan is BUILT FROM — this isn't busywork; the ranked, documented risks directly drive the plan's priorities.
    Misconception to pre-empt: "documenting is just tidying up the notes." No — documenting to organisational policy is an assessed step (PC 2.5), and it's the artefact Topic 4 consumes; sloppy documentation breaks the next stage.
    Question to pose: "Your top risk is documented — how will Topic 4's plan use that exact document?" (it sets the recovery priority order and the targets the plan must meet).
    UoC/AT1 tie: [ICTCLD501 PC 2.4] (evaluate severity of impact/disruption) + [ICTCLD501 PC 2.5] (document outcomes per policies) — AT1 Part B B6–B7.
- [EX] Risk & impact analysis
  - For the practice scenario, assess at least three major risk events (likelihood, impact, severity) and note exclusions.
  - Document the impact-analysis outcomes.
  timer: ~30 min
  image: none
  notes:
    Facilitation — the biggest activity in the Topic: students produce the impact analysis for the practice scenario. The core AT1 Part B §2 rehearsal; the worked risk-register table on the next slide is their shape.
    Tell students: "For the practice scenario, assess at least THREE major risk events — score each for likelihood and impact on one scale, compute severity, rank them, and note what the plan excludes. Then document the outcomes."
    Steps (put on the board):
    1. Pick ≥3 major risk events from the cloud risk environment (don't just list region outages — include misconfiguration/human error).
    2. Score each: likelihood × impact = severity, all on the SAME scale; rank them.
    3. Note plan exclusions — what's deliberately out, and why.
    4. Document the outcomes in business terms (what the impact means for the organisation).
    Must produce: a ranked risk register (≥3 events, likelihood/impact/severity), stated exclusions, and a short documented impact write-up.
    Timing: ~30 min. Where they get stuck: they list risks without scoring on a consistent scale (make them fix one scale first), and they skip exclusions (prompt "what did you decide NOT to cover, and why?").
    Share-back prompt: "Give me your top-ranked risk and the score behind it" — check the scale is applied consistently.
    No-leakage note: practice scenario only (comparable, not identical); AT1 evidences the same risk-and-impact skill on the assessed system — keep them on the practice brief.
    UoC/AT1 tie: [ICTCLD501 PC 2.2] · [ICTCLD501 PC 2.4] · [ICTCLD501 PC 2.5] · [ICTCLD501 PE 2] — the impact-analysis core of AT1 Part B §2.
- [TABLE] Risk register — worked shape
  | Risk event | Likelihood | Impact | Severity |
  | AZ outage in the primary region | Low | High | High |
  | Data corruption / bad deploy | Medium | High | High |
  | Accidental deletion (human error) | Medium | Medium | Medium |
  note: Score every event on the same scale; severity ranks the recovery priority.
  image: none
- [TAKEAWAYS] Topic 3 · Key takeaways
  - DR requirements come from business needs; the plan is tested against them.
  - RTO/RPO express how fast and how recent recovery must be — set to the need.
  - Assess at least three risks by likelihood x impact = severity; record exclusions.
  - Document the impact analysis — it is the input to the Topic 4 plan.
  image: none

### Close
- [BESPOKE] Next: Topic 4 — strategy & plan
  - You've set the requirements, objectives and impact analysis — the front half of the DR lifecycle.
  - Next you choose a recovery strategy and write the documented DR plan.
  image: none

## Build notes
~17 slides. Exercises run on the practice scenario (analysis only). One generated diagram (`diagram rto-rpo-timeline`); one decorative `gen` image (opener hero); one TABLE (risk register).

## Changelog
- 2026-07-01 — authored to full content.
