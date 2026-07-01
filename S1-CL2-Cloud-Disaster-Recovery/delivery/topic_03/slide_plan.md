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

### C1 — Plan requirements & current recovery position
- Teaches: [ICTCLD501 PC 1.1] · [ICTCLD501 PC 1.2] · [ICTCLD501 PC 1.3]
- Kicker: what must recover, and what's already in place
- [PRIMER] What a DR plan is for
  - A DR plan restores service after a disruptive event, to agreed targets.
  - It is driven by business needs — what the organisation can and cannot tolerate losing.
  - Start by writing down the requirements, not by picking a technology.
  image: none
- [BESPOKE] Identify the DR requirements
  - Read the engagement brief: which systems are business-critical, and to whom.
  - Requirements come from the business — enrolment front-door uptime, financial-record integrity, residency.
  - State each requirement so it can later be tested against a proposed plan.
  image: none
- [BESPOKE] Current recovery position & vendor provisions
  - Determine the existing organisational recovery arrangements — what's already in place, and its gaps.
  - Identify the cloud vendor's DR provisions and SLAs: what the provider guarantees vs what you must add.
  - The plan builds on the vendor's native durability, it doesn't reinvent it.
  image: none
- [EX] Gather requirements & current position
  - For the practice scenario, list the DR plan requirements from the business needs.
  - Record the current recovery arrangements and the relevant vendor DR provisions/SLAs.
  timer: ~20 min
  image: none

### C2 — Recovery objectives & data managed
- Teaches: [ICTCLD501 PC 2.1] · [ICTCLD501 PC 2.3] · [ICTCLD501 KE 5]
- Kicker: how fast, how recent, how much
- [PRIMER] RTO & RPO
  - RTO (Recovery Time Objective): how long you can be down before it hurts too much.
  - RPO (Recovery Point Objective): how much recent data you can afford to lose.
  - They are business decisions expressed as time; every DR choice traces back to them.
  image: diagram rto-rpo-timeline
- [BESPOKE] Set the objectives to business needs
  - Derive RTO/RPO from the requirements — the front door tolerates little downtime; financial records tolerate little data loss.
  - Explain each: what business consequence the target avoids.
  - Tighter targets cost more — set them to the need, not to the maximum.
  image: none
- [BESPOKE] Estimate the data managed
  - Estimate the amount of data the plan must protect and recover.
  - Classify its security level — personal, financial, operational — which drives handling and residency.
  - The volume and sensitivity shape both RPO and the recovery method.
  image: none
- [EX] Determine RTO/RPO & data managed
  - For the practice scenario, determine and explain RTO and RPO to the business needs.
  - Estimate the amount and security level of the data managed.
  timer: ~20 min
  image: none

### C3 — Risk & impact analysis
- Teaches: [ICTCLD501 PC 2.2] · [ICTCLD501 PC 2.4] · [ICTCLD501 PC 2.5] · [ICTCLD501 PE 2] · [ICTCLD501 KE 1] · [ICTCLD501 KE 2]
- Kicker: likelihood times impact equals severity
- [PRIMER] The cloud risk environment & analysis method
  - The cloud risk environment: region/AZ outages, misconfiguration, dependency failure, human error, malicious action.
  - A data-analysis methodology turns those into a comparable picture — likelihood and impact scored consistently.
  - Risk analysis is systematic, not a guess: same scale for every event.
  image: none
- [BESPOKE] Assess the major risk events
  - Assess at least three major risk events: for each, its likelihood and its impact.
  - Severity = likelihood x impact; rank the events so the plan can prioritise.
  - Record plan exclusions — the risks the plan deliberately does not cover, and why.
  image: none
- [BESPOKE] Evaluate impact & document outcomes
  - Evaluate the severity of impact and disruption of each event on the business.
  - Document the impact-analysis outcomes per organisational policies and procedures.
  - The documented analysis is the input the Topic 4 recovery plan is built from.
  image: none
- [EX] Risk & impact analysis
  - For the practice scenario, assess at least three major risk events (likelihood, impact, severity) and note exclusions.
  - Document the impact-analysis outcomes.
  timer: ~30 min
  image: none
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
