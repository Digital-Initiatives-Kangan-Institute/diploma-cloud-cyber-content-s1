# S1-CL1 AT1 — Business Case Assessor Benchmark

**Audience:** Assessor only — do **not** share with students.

**Purpose:** marking reference for the student's full AT1 Business Case submission. Provides what "Satisfactory" looks like for each Business Case section, expected content cues, a worked CBA example (for §7 and Appendix 1), model answers for the Knowledge Evidence appendix, and common deductions. Use alongside the Presentation Observation Rubric (`presentation-observation-rubric.md`) and the AT1 student brief (`at1-brief-student.md`).

**Status:** DRAFT (Claude v2, 2026-05-23). Expanded from the original CBA-only benchmark to cover the full Business Case. Worked CBA figures are Claude-proposed plausible values matched to the scenario inputs. **TBD** confirm before live delivery.

---

## 1. Marking framework

- The Business Case is marked **Satisfactory / Not Yet Satisfactory** as a whole, with per-section judgements feeding the overall.
- Each Business Case section evidences specific UoC items (see the section-level *Evidences:* tags in `business-case-template-S1-CL1-AT1.md`).
- A section is **Satisfactory** when the UoC items it evidences are demonstrated through the student's content.
- Students may arrive at different reasoning, structure, or numerical totals through different but defensible assumptions — that's acceptable as long as their work is internally consistent and justified.
- **Critical sections** (where NYS forces overall NYS): §7 CBA, §10 Action Plan, Appendix 2 Knowledge Evidence, Sign-off block.
- **Supporting sections** (where NYS may be balanced against evidence elsewhere in the bundle): §1 Executive Summary, §2 Engagement Context, §11 Next Steps.

---

## 2. Marking §1 Executive Summary

**UoC evidenced:** contributes to [ICTICT517 PC 1.4] Report on proposed changes to superior.

**Satisfactory looks like:**
- One page; covers all 6 prompt bullets
- The recommendation is stated (not deferred until later)
- 5-year cost numbers are present and reconcile with §7
- Top 2–3 risks named
- The decision asked of the board is explicit

**Not Yet Satisfactory:**
- Missing or absent
- Reads as background-only with no recommendation
- Numbers do not reconcile with §7

---

## 3. Marking §2 Engagement Context

**UoC evidenced:** [ICTICT517 AC 4] Individual superior in the organisation.

**Satisfactory looks like:**
- Names the student's MTS role + the YAT superior + the engagement scope
- States what the Business Case asks the board to decide

**NYS:** missing or vague about who is engaged and who decides.

---

## 4. Marking §3 Strategic Alignment Analysis

**UoC evidenced:** [ICTICT517 PC 1.1] Analyse and document current strategic plan against industry environment and organisational objectives · [ICTICT517 PE 1] interpret a strategic plan and objectives.

**Satisfactory looks like:**
- Cites the YAT ICT Strategic Plan objectives material to the engagement (verbatim or paraphrased with reference)
- Includes external industry context — RTO sector cloud adoption, availability expectations, data residency obligations — with cited sources
- Identifies where YAT's plan aligns with industry direction and where it is more ambitious / more cautious
- Connects the analysis to the LMS migration

**NYS:**
- No external industry research (analysis is internal-only)
- No citations
- Strategic Plan content reproduced without analysis

---

## 5. Marking §4 Current State of YAT's ICT

**UoC evidenced:** [ICTICT517 PC 1.2] Determine and document current state · [ICTICT517 PE 2] evaluate the current state.

**Satisfactory looks like:**
- Synthesised summary — in the student's own words — covering at minimum the four prompted areas (network/security topology, LMS server status, supporting infrastructure, staff capability + dependencies)
- Material facts are accurate to the YAT scenario
- Focus is on what's relevant to the migration; non-material detail is omitted

**NYS:**
- Verbatim copy-paste of the intranet material
- Material inaccuracies (e.g. wrong OS version, wrong availability baseline)
- Missing one or more of the prompted areas

**Note:** synthesis is the assessable skill here, per the YAT case study tradition (517 AT2 Q2 asks for 100–200 words synthesis). Don't penalise a student for not reproducing the full intranet detail — penalise verbatim reproduction.

---

## 6. Marking §5 Gap Analysis

**UoC evidenced:** [ICTICT517 PC 1.3] Compare strategic plan vs current state · [ICTICT517 PE 3] identify gaps and opportunities.

**Satisfactory looks like:**
- At least 3 rows in the gap table, each covering all 6 columns (Strategic Plan objective, Current state, Desired future state, Gap, Improvement opportunity, Proposed change)
- Gaps are real and supported by §3 + §4
- Narrative summary ties the table together

**Expected gap items the student should identify:**
- Availability gap (99.2% current vs 99.9% target)
- Recovery objectives gap (~24h RPO / 7–11h RTO current vs ≤1h RPO / ≤4h RTO target)
- LMS server end-of-life vs the "Deploy LMS infrastructure in cloud" objective
- Scalability gap for assessment-week peaks
- Optional: cloud-adoption gap aligned to the "Reduce dependency on in-house server infrastructure" objective

**NYS:**
- Fewer than 3 gaps
- Gaps not connected to a stated Strategic Plan objective
- "Proposed change" column missing or generic

---

## 7. Marking §6 Options Considered and Evaluation

**UoC evidenced:** [ICTICT517 PC 2.1] Evaluate impact · [ICTICT517 PC 2.2] Evaluate difficulty · [ICTICT517 KE 3] Methods of evaluation of competing ICT systems and products · [ICTCLD401 PC 1.8] Define workload according to business requirements · [ICTCLD502 PC 1.2] Determine cloud infrastructure according to business needs.

**Satisfactory looks like:**
- §6.1 Workload definition references the LMS application spec
- §6.2 names the two options (Option A in-house renewal, Option B cloud migration to AWS) and explains why these two
- §6.3 names the evaluation method (CBA + intangibles + risk register) and justifies its choice
- §6.4 initial impact + difficulty table populated for both options

**NYS:**
- Only one option assessed
- No evaluation method named
- Workload definition missing

---

## 8. Marking §7 Cost-Benefit Analysis (and Appendix 1)

**UoC evidenced:** [ICTICT517 PC 2.1] Evaluate impact · [ICTICT517 KE 3] · [ICTICT517 FS Numeracy] · [ICTCLD401 KE 4] · [ICTCLD502 KE 3] · [ICTCLD401 KE 1].

This is the most numerical section. Use the worked example below as the benchmark.

### 8.1 Benchmark assumptions

- LMS user population: 800 students + 60 staff
- 5-year analysis period at 2026 price levels (AUD ex GST)
- ICT FTE fully-loaded cost: $115k/year
- Cost of downtime during teaching hours: $750/hour
- Teaching hours per year (indicative): 1,820 hours
- AWS pricing region: `ap-southeast-2` (Sydney)
- AWS compute and database baseline assumed on 1-year Reserved Instance (~30% discount applied)

### 8.2 Option A — In-house renewal (5-year worked example)

**One-off capital (Year 1):**

| Item | Cost |
|---|---:|
| Replacement LMS server | $25,000 |
| Backup tape library refresh + drive | $8,000 |
| UPS upgrade | $3,000 |
| One-off internal migration labour | $15,000 |
| **Year-1 capital** | **$51,000** |

**Recurring operational (per year):**

| Category | Item | Annual cost |
|---|---|---:|
| Software licensing | Windows Server Standard | $1,500 |
| | Antivirus / EDR | $300 |
| | Monitoring / management | $2,000 |
| Power and facilities | Electricity + cooling | $1,200 |
| | Server-room rent allocation | $5,000 |
| | UPS battery (amortised) | $500 |
| Backup | Tape media | $1,500 |
| | Offsite tape storage | $2,400 |
| | Backup software maintenance | $1,500 |
| Staff time | LMS admin (0.20 FTE × $115k) | $23,000 |
| | Incident response (0.05 FTE × $115k) | $5,750 |
| External support | MTS application support | $30,000 |
| **Recurring per year** | | **$74,150** |

**5-year Option A total:**

| Component | 5-year |
|---|---:|
| One-off capital | $51,000 |
| Recurring (5 × $74,150) | $370,750 |
| **Option A — 5 years** | **$421,750** |

### 8.3 Option B — Cloud migration to AWS (5-year worked example)

**One-off project costs (Year 1):**

| Item | Cost |
|---|---:|
| MTS migration labour (architecture → cutover → handover) | $80,000 |
| YAT ICT staff time (~0.30 FTE × 6 months × $115k) | $17,250 |
| Parallel running of on-prem and cloud during cutover (~2 months) | $12,500 |
| Decommissioning on-prem LMS + secure data destruction | $2,500 |
| **Year-1 project** | **$112,250** |

**AWS direct recurring (per year, post-migration):**

Sized for the workload in the LMS application specification. RI discount of ~30% on compute and managed-DB baseline.

| Category | Item | Annual cost |
|---|---|---:|
| Compute | 2× m6i.xlarge EC2 (HA baseline, 1-yr RI) | $6,600 |
| | Auto-scaling peaks (~10 instance-weeks/year) | $1,500 |
| Database | RDS db.m6i.large Multi-AZ MySQL (1-yr RI) | $2,000 |
| | RDS storage + automated backups | $400 |
| Network | Application Load Balancer | $400 |
| | NAT gateway | $400 |
| | Data transfer out (~50 GB/mo) | $50 |
| Storage | EBS gp3 (~500 GB) | $600 |
| | S3 attachments + snapshots (~200 GB) | $50 |
| | AWS Backup cross-Region copy | $300 |
| Monitoring | CloudWatch metrics + logs + alarms | $500 |
| Support | AWS Business Support | $1,800 |
| **AWS direct per year** | | **$14,600** |

**Staff time + ongoing external support (per year, Years 2–5):**

| Category | Item | Annual cost |
|---|---|---:|
| Staff time | LMS admin (0.10 FTE × $115k) | $11,500 |
| | Incident response (0.03 FTE × $115k) | $3,450 |
| External support | MTS ongoing support (reduced — managed services) | $20,000 |
| **Staff + external per year** | | **$34,950** |

**5-year Option B total:**

| Component | 5-year |
|---|---:|
| Year-1 project | $112,250 |
| AWS direct (5 × $14,600) | $73,000 |
| Staff + external (4 × $34,950 — Year 1 covered by MTS migration project) | $139,800 |
| **Option B — 5 years** | **$325,050** |

### 8.4 Avoided-downtime benefit

Current availability: 99.2%. Target: 99.9%. Improvement: 0.7 percentage points = ~61 hours/year avoided unavailability.

Assume ~30% of avoided hours fall during teaching hours:

- 61 hr × 0.30 × $750/hr = ~$13,725/year avoided downtime cost
- Over 5 years: ~$68,625

### 8.5 Comparison summary

| | Option A — In-house | Option B — Cloud (AWS) |
|---|---:|---:|
| One-off (Year 1) | $51,000 | $112,250 |
| Recurring 5-year | $370,750 | $212,800 |
| **5-year total** | **$421,750** | **$325,050** |
| **5-year saving (B − A)** | — | **$96,700** |
| Avoided-downtime benefit (B vs A, 5-year) | — | **~$68,625** |
| **Net 5-year delta in favour of cloud** | — | **~$165,325** |

### 8.6 Year-1 cash-flow profile

Important for sign-off conversation — both options have similar Year-1 cash impact; cloud's savings appear in Years 2–5:

| | Year 1 outlay | Year 2 outlay (recurring) |
|---|---:|---:|
| Option A | $51,000 + $74,150 = **$125,150** | $74,150 |
| Option B | $112,250 + $14,600 = **$126,850** | $14,600 + $34,950 = $49,550 |

### 8.7 Acceptable ranges for student totals

- A student arriving at a 5-year cloud total in the range **$280k–$370k** has done credible AWS sizing and pricing work.
- A student arriving at a 5-year on-prem total in the range **$400k–$450k** has used the inputs correctly and applied reasonable inflation/staff-time treatment.
- Students sharply outside these ranges either have a different sizing rationale (in which case marking checks the rationale) or have miscalculated (in which case flag the specific line items).

### 8.8 Marking checks for §7 + Appendix 1

Award credit for:
- All cost categories present and reasonably populated in both options
- AWS Pricing Calculator (or equivalent) evidence attached as Appendix 3
- 5-year projection per option
- Stated sizing assumption for AWS option
- Sensitivity analysis (§7.6) around at least one key assumption
- Year-1 cash-flow point (§7.5.1) made explicitly
- Quantified avoided-downtime calculation (§7.4)
- Detailed line items in Appendix 1 roll up correctly to §7 summary tables

Common deductions:
- Cloud option missing entire categories (e.g. no Multi-AZ DB pricing, no support tier)
- Pricing values lifted without source — no evidence of AWS Pricing Calculator use
- Missing or absent on-prem option (just doing AWS pricing and skipping the comparison)
- Appendix 1 totals do not reconcile with §7 summary tables

---

## 9. Marking §8 Risk and Impact Assessment

**UoC evidenced:** [ICTICT517 PC 2.1] non-financial impact · [ICTICT517 PC 2.2] difficulty · [ICTICT517 PE 5] evaluate difficulty.

**Satisfactory looks like:**
- §8.1 intangibles table populated for both options across all 9 factors
- Treatment is honest — both options have pros and cons listed; no one-sided cheerleading for the preferred option
- §8.2 risk register has at least 3 risks for the recommended option, each with likelihood / impact / mitigation

**Expected intangibles coverage** (student should address most):
- **Availability** — Option B can achieve 99.9% target; Option A would require significant additional capital for HA (probably out of scope of the renewal cost).
- **Recovery objectives** — Option B meets RTO ≤ 4h / RPO ≤ 1h targets; Option A's current 7–11h RTO and 24h RPO do not.
- **Growth capacity** — Option B autoscales; Option A would require server resizing with downtime.
- **Peak handling** — Option B autoscales for assessment-week spikes; Option A must be statically sized.
- **Staff capability** — Option B exposes YAT ICT to cloud (positive over time; gap during transition).
- **Vendor lock-in** — Option A no lock-in; Option B moderate AWS lock-in via managed services.
- **Sustainability** — Option A 24×7 server-room cooling; Option B leverages AWS sustainability profile.
- **Cyber security** — Option B richer monitoring + threat intelligence; Option A relies on YAT's existing controls.
- **Disaster recovery** — Option B Multi-AZ + cross-Region copy; Option A tape-restore from offsite, ~24h.

**NYS:**
- One-sided intangibles (only positives for cloud)
- Fewer than 4 intangibles addressed substantively
- Risk register absent or has fewer than 3 risks

---

## 10. Marking §9 Recommendation

**UoC evidenced:** [ICTICT517 PC 2.3] Prioritise proposed changes · [ICTICT517 PE 4] determine and prioritise · contributes to [ICTICT517 PC 3.1] Develop action plan.

**Satisfactory looks like:**
- Recommended option clearly stated (Option A or Option B)
- 3–5 sentence rationale connecting back to the CBA findings, intangibles, and risk register
- Recommendation flows logically into §10 Action Plan

**Expected recommendation:** most credible analyses arrive at **Option B (cloud migration to AWS)**. A student recommending Option A is acceptable as long as the recommendation is logically connected to their analysis — e.g. they have identified a particular blocker to cloud that makes in-house renewal the better choice. **Marking does not penalise the choice of option; it marks whether the choice is justified by the work.**

**NYS:**
- Recommendation not connected to the analysis (e.g. dollar comparison shows clear winner but student recommends the other option without justification)
- No rationale given
- Recommendation hedged ("either could work") without committing

---

## 11. Marking §10 Action Plan

**UoC evidenced:** [ICTICT517 PC 3.1] Develop action plan including prioritised schedule and consistency with org policy and procedures · [ICTICT517 PC 3.2] Detail standards, targets and implementation methods · [ICTICT517 PE 6] develop action plan · [ICTICT517 KE 1] Key sections of an action plan.

**This is one of the critical sections — NYS here forces overall NYS.**

**Satisfactory looks like:**
- §10.1 prioritised changes — at least 5 items with priority rationale
- §10.2 implementation schedule — phased; dependencies named; no all-at-once cutover proposed
- §10.3 standards / targets table populated, with measurable targets (99.9% availability, RPO ≤ 1h, RTO ≤ 4h, data residency Australia, cost envelopes)
- §10.4 implementation methods — names specific methods, tools, standards (Well-Architected, AWS managed services, ITIL change management, etc.)
- §10.5 alignment with YAT change-management procedure — explicit
- §10.6 risk register cross-references §8.2

**Common phasing the student should produce (any of):**
- Phase 1: design + foundation build (AWS account setup, IAM, VPC, monitoring baseline)
- Phase 2: application migration (LMS server build, app deployment, parallel running)
- Phase 3: HA hardening (Multi-AZ DB, autoscaling, monitoring + alerting)
- Phase 4: cutover (high-risk change requiring full change-management sign-off)
- Phase 5: stabilisation + handover to YAT ICT operations

**NYS:**
- Single-phase all-at-once cutover with no risk treatment
- Missing standards / targets / success metrics
- No alignment with change-management procedure
- Phases have no dependencies or owners

---

## 12. Marking §11 Next Steps and Decision Requested

**UoC evidenced:** [ICTICT517 PC 3.3] Provide action plan to superior for feedback and approval.

**Satisfactory looks like:**
- States precisely what the board is being asked to approve today
- Names what is deferred to later sign-off gates

**NYS:** vague or missing.

---

## 13. Marking Appendix 2 — Knowledge Evidence

**This is a critical section — NYS here forces overall NYS.**

Below are model answers for each question. Student answers may differ in detail but must demonstrate the underlying knowledge applied to their own Business Case.

### 13.1 Selection-style questions

**Q1 — IaaS / PaaS / SaaS classification of solution components** [ICTCLD401 KE 3]

*Model coverage:* student identifies which AWS services are IaaS (e.g. EC2, EBS — they manage the instances), PaaS (e.g. RDS Multi-AZ, ALB — managed services where AWS runs the platform), SaaS (none in their solution typically — they may note Office 365 as a YAT-existing SaaS but not part of their migration). Rationale: PaaS chosen for DB because YAT ICT lacks DB-admin cloud experience; IaaS chosen for the LMS application tier because the existing Windows Server / DOODLE stack is preserved.

**Q2 — Cloud deployment model** [ICTCLD401 KE 11]

*Model coverage:* Public cloud (AWS). Rationale: YAT's strategic plan explicitly targets cloud migration to reduce in-house infrastructure; private cloud doesn't address the cost reduction objective; hybrid is what they have today (Office 365 SaaS + on-prem LMS) and the migration shifts the on-prem LMS into the public cloud, leaving Office 365 SaaS unchanged.

**Q3 — Industry technology standards** [ICTCLD401 KE 1 · ICTCLD502 KE 1]

*Model coverage:* At least three named, with material role explained. Acceptable: NIST SP 800-145 (definitions of IaaS/PaaS/SaaS) — informs §6 service-type classification; AWS Well-Architected Framework — informs §10 implementation methods; ISO/IEC 27017 — informs §8 security treatment; ACSC Essential Eight — informs §10 security controls; ITIL 4 — informs alignment with YAT change management procedure.

**Q4 — Industry-standard hardware/software products** [ICTCLD401 KE 2 · ICTCLD502 KE 2]

*Model coverage:* Student identifies the specific AWS services in their solution + their general features + role. Example: Amazon EC2 (general-purpose virtual machine; underpins the LMS application tier); Amazon RDS for MySQL Multi-AZ (managed relational database with automatic failover; underpins the LMS data tier); Application Load Balancer (layer-7 load balancer with health checks; distributes traffic across HA EC2 instances); etc.

**Q5 — Cloud cost models and scalability** [ICTCLD401 KE 4 · ICTCLD502 KE 3]

*Model coverage:* Student explains which cost model applies to each AWS service in their CBA. Example: 1-year Reserved Instance for EC2 baseline + RDS baseline (~30% discount — appropriate because demand is predictable); on-demand or autoscaling-spot for EC2 peak capacity (cost scales with assessment-week demand); S3 pay-as-you-go (cost scales with storage growth); Business Support 10% of usage (cost scales with overall AWS spend). Scaling consequence: total AWS cost grows roughly linearly with student-population growth (the 15%/year target).

### 13.2 Demonstration-style questions

**Q6 — Key sections of an action plan** [ICTICT517 KE 1]

*Model coverage:* Student identifies the key sections of an ICT implementation action plan (prioritised list of changes, implementation schedule with dependencies, standards/targets/success metrics, implementation methods, alignment with change-management procedure, risk register, owners) and cites where each appears in their §10. Demonstrates §10 has all key sections.

**Q7 — Methods of evaluation and planning approaches** [ICTICT517 KE 2]

*Model coverage:* Student names the methods applied (CBA, sensitivity analysis, intangibles assessment, risk register) and cites the §7 / §8 sections where each is applied. May also cite their use of structured gap-analysis methodology in §5.

**Q8 — Evaluation of competing ICT systems and products** [ICTICT517 KE 3]

*Model coverage:* Student names the evaluation method — typically the CBA combined with intangibles — and cites §6.3 (where the method is named) + §7 (where the CBA evaluates) + §8.1 (where intangibles compare). May also mention weighted-criteria evaluation if the student used one.

**Q9 — Current and emerging trends** [ICTICT517 KE 4]

*Model coverage:* Student identifies cloud migration itself as the current/emerging trend that informed the recommendation; possibly also Multi-AZ HA design patterns, managed services as a reducing-burden trend, autoscaling-for-cost-optimisation, etc. Cites where in their reasoning each trend was material.

### Marking checks for Appendix 2

Award credit for:
- All 9 questions answered
- Each answer references specific sections of the student's own Business Case
- The cited content is actually present in the student's Business Case (not invented)

Common deductions:
- Generic textbook answers not tied to the student's own work ("IaaS is infrastructure-as-a-service..." without saying which AWS service in their solution is IaaS)
- Citations to Business Case sections that don't contain what the answer claims they do

---

## 14. Marking Appendix 3 — Supporting Research

**Satisfactory looks like:**
- AWS Pricing Calculator export attached (screenshot or shared link)
- Industry-research sources from §3 cited with URLs and access dates
- Any other source documents used for cost figures cited

**NYS:** AWS Pricing Calculator evidence absent — implies the student didn't research their AWS figures and is fabricating.

---

## 15. Marking Appendix 4 — Feedback Record

**Satisfactory looks like:**
- Completed using the Feedback Record template
- Captures actual board feedback received during the presentation event
- Includes student's response or follow-up action where applicable

**NYS:** absent, blank, or evidently not completed at the event.

---

## 16. Marking the Sign-off block

**This is a critical artefact — NYS here forces overall NYS.**

**Satisfactory looks like:**
- Sign-off block populated with names, dates, signatures
- Approval line completed by the role-played YAT ICT Manager (the assessor in role)

**NYS:** sign-off block left blank — implies the student did not seek or obtain approval per [ICTICT517 PC 3.3].

---

## 17. Common deductions across the Business Case

- **Pricing values without source.** Any AWS or non-trivial cost figure without supporting evidence in Appendix 3 is a deduction.
- **Numbers that don't reconcile.** §1 Executive Summary numbers must reconcile with §7 summary tables; §7 summary tables must reconcile with Appendix 1 line items.
- **One-sided intangibles.** §8.1 must be honest about trade-offs of the recommended option.
- **Recommendation not connected to analysis.** §9 must follow logically from §7 and §8.
- **Action plan all-at-once.** A single-phase migration with no phasing or change-management gates fails §10.
- **Verbatim reproduction.** §4 Current State must be synthesised, not copy-pasted from the intranet.
- **Missing KE coverage.** Appendix 2 must have all 9 questions answered with reference to the student's own work.

---

## 18. Overall result calculus

For the AT1 Business Case to be marked **Satisfactory** overall:

- All **critical sections** Satisfactory: §7 (CBA + Appendix 1), §10 (Action Plan), Appendix 2 (Knowledge Evidence), Sign-off block
- All **other sections** Satisfactory **OR** evidence elsewhere in the bundle compensates (e.g. §1 Executive Summary missing but §11 covers the asked-for decision crisply — assessor may issue Satisfactory with a developmental comment)
- Presentation event Satisfactory per the `presentation-observation-rubric.md`
- Submission complete per §3.3 of the student brief

If any critical section is NYS, the overall is NYS and resubmission is required for that section.

---

## Changelog

- **2026-05-23:** Initial benchmark moved from the original `cba-cost-data-pack` draft (which was incorrectly handing the analysis to students) into this assessor-only location. Covered the CBA only.
- **2026-05-23 (later):** Renamed from `cba-assessor-benchmark.md` to `business-case-assessor-benchmark.md`. Expanded scope from CBA-only to the full Business Case — added marking guidance for every section (§1–§11, Sign-off, Appendices 1–4), with the original CBA worked example preserved as §8 (Marking §7 CBA + Appendix 1) and a new §13 added with model answers for the Knowledge Evidence appendix.
