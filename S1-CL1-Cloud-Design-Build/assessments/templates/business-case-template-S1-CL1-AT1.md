# YAT LMS Cloud Migration — Business Case

> **Template for student completion (S1-CL1 AT1).** This is the primary written deliverable for AT1. It contains your analysis of YAT's situation, your evaluation of options including the Cost-Benefit Analysis, your recommendation, the action plan you propose, and a Knowledge Evidence appendix.
>
> Populate every section marked `[FILL IN]`, every cost cell marked `$_____`, and every narrative box marked `[Your response]`. Numbers in *italics* are pre-populated from the YAT cost inputs and are not to be changed unless you can justify why. AWS pricing line items in Appendix 1 are your work — research using the AWS Pricing Calculator and attach the export as Appendix 3.
>
> Final submitted form will be the populated `.docx` equivalent of this document. The CBA detailed line items live in **Appendix 1** of this same document; the Knowledge Evidence responses live in **Appendix 2**.

---

## UoC requirements evidenced by this Business Case

UoC items that map to a specific section are tagged inline under the relevant section heading as *Evidences: [UNIT SECTION numbering]*.

The following UoC requirements are evidenced **generally across the Business Case as a whole**:

- **[ICTICT517 FS Numeracy]** — Interprets numerical data and applies mathematical calculations to assess the financial implications of introducing changes. Evidenced across §7 and Appendix 1.
- **[ICTICT517 FS Writing]** — Uses plain English, terminology, diagrams, numerical information, formatting and structure relevant to the job role and organisation. Evidenced across every narrative section.
- **[ICTICT517 FS Reading]** — Reviews, analyses and evaluates complex online and hard copy documentation. Evidenced through use of the YAT scenario materials and any external research.
- **[ICTICT517 KE 4]** — Current and emerging system and product trends and directions. Evidenced implicitly through researching AWS as a current cloud-vendor option; reinforced in Appendix 2 Knowledge Evidence.

---

## Cover

| | |
|---|---|
| **Student name** | [FILL IN] |
| **Student ID** | [FILL IN] |
| **Submission date** | [FILL IN] |
| **Project** | YAT LMS Cloud Migration |
| **Engagement** | MP Tech Solutions (MTS) — S1-CL1 |
| **Document version** | [FILL IN — e.g. v1.0] |
| **Prepared for (board)** | Sam Walker, YAT ICT Manager (via Pat Lin, MTS) |
| **Analysis period** | 5 years |
| **Currency** | AUD ex GST |

---

## 1. Executive Summary

*Evidences: contributes to [ICTICT517 PC 1.4] Report on proposed changes, gaps and improvement opportunities to superior*

**Write this section last.** A one-page summary the board reads first. Cover, in 4–6 short paragraphs or bullets:

- The problem in one sentence (YAT's LMS situation against the strategic 99.9% availability target)
- The options considered (in-house renewal vs cloud migration to AWS)
- Your recommendation in one sentence
- 5-year cost position (high-level numbers, both options)
- Top 2–3 risks of the recommended option and how you propose to manage them
- The decision you are asking the board to take today

> [Your response]

---

## 2. Engagement Context

*Evidences: [ICTICT517 AC 4] Individual superior in the organisation*

Establish who you are, the engagement, who you report to, and what this Business Case asks the board to decide.

> [Your response — approx. 1 short paragraph]

---

## 3. Strategic Alignment Analysis

*Evidences: [ICTICT517 PC 1.1] Analyse and document current strategic plan of organisation against industry environment and organisational objectives · [ICTICT517 PE 1] interpret a strategic plan and objectives of the organisation*

Analyse YAT's ICT Strategic Plan against the broader ICT industry environment for RTOs and against YAT's documented organisational objectives. Use the YAT material on the intranet as your primary source; cite any external industry sources you use.

Cover:
- The ICT Strategic Plan objectives material to this engagement (cite the specific objectives)
- The current industry environment for RTOs around the items in the plan (cloud adoption, availability expectations, data-residency obligations, etc.)
- Where YAT's plan aligns with industry direction, and where it is more ambitious or more cautious
- Implications for the LMS migration

> [Your response — approx. 250–400 words]

---

## 4. Current State of YAT's ICT

*Evidences: [ICTICT517 PC 1.2] Determine and document current state of ICT systems and practices in organisation · [ICTICT517 PE 2] evaluate the current state of ICT in the organisation*

Synthesise the YAT current-state material on the intranet into a current-state summary suitable for the board. **Do not reproduce the intranet material verbatim.** Your job is synthesis: decide what is material to the migration decision, characterise it in your own words, focus the reader on what drives the gap analysis in §5.

Cover at minimum:
- Network and security topology (zones, redundancy posture)
- The LMS server's current status — what it runs, current availability, recovery objectives, end-of-life situation
- Supporting infrastructure relevant to the migration (backup process, identity directory, storage, integrations)
- Staff capability and external dependencies

> [Your response — approx. 150–250 words]

---

## 5. Gap Analysis

*Evidences: [ICTICT517 PC 1.3] Compare strategic plan objectives and current state of ICT to determine ICT gaps, improvement opportunities, and proposed changes · [ICTICT517 PE 3] identify possible gaps and opportunities in ICT and evaluate organisational impact with reference to the strategic plan and the objectives*

Compare each in-scope ICT Strategic Plan objective against the current state. Identify the gap, the improvement opportunity, and the proposed change. Use the table below; add rows as needed.

| ICT Strategic Plan objective | Current state | Desired future state | Gap | Improvement opportunity | Proposed change |
|---|---|---|---|---|---|
| [FILL IN — e.g. *"Achieve 99.9% availability for critical systems"*] | [Your response] | [Your response] | [Your response] | [Your response] | [Your response] |
| [FILL IN] | [Your response] | [Your response] | [Your response] | [Your response] | [Your response] |
| [FILL IN] | [Your response] | [Your response] | [Your response] | [Your response] | [Your response] |

Narrative summary of the gap analysis:

> [Your response — 100–200 words tying the table together]

---

## 6. Options Considered and Evaluation

*Evidences: [ICTICT517 PC 2.1] Evaluate impact of proposed changes to ICT systems and products against strategic objectives of organisation · [ICTICT517 PC 2.2] Evaluate the difficulty of implementing proposed changes to ICT systems and products · [ICTICT517 KE 3] Methods of evaluation of competing and complementary internal and external ICT systems and products · [ICTCLD401 PC 1.8] Define workload according to business requirements and needs · [ICTCLD502 PC 1.2] Determine cloud infrastructure according to business needs*

### 6.1 Workload definition

Define the LMS workload that the chosen option must support. Include user load, peak patterns, data volumes, integration requirements, availability target. Draw on the LMS application specification on the intranet.

> [Your response]

### 6.2 Options considered

State the options you assessed.

- **Option A — In-house renewal:** [one-line description]
- **Option B — Cloud migration to AWS:** [one-line description]
- *(Add other options here only if you assessed any in addition; state why or why not.)*

### 6.3 Evaluation method

State the evaluation method you applied (the CBA + intangibles assessment + risk register) and any other methods (e.g. weighted decision matrix). Justify why this method is appropriate to the decision.

> [Your response — 1 short paragraph]

### 6.4 Initial impact and difficulty assessment

| | Option A — In-house | Option B — Cloud (AWS) |
|---|---|---|
| **Strategic impact** (PC 2.1) | [Your response — 1–2 sentences] | [Your response] |
| **Implementation difficulty** (PC 2.2) | [Your response] | [Your response] |
| **Headline pros** | [Your response] | [Your response] |
| **Headline cons** | [Your response] | [Your response] |

The deeper financial picture is in §7 (with line-item detail in Appendix 1). The deeper risk picture is in §8.

---

## 7. Cost-Benefit Analysis

*Evidences: [ICTICT517 PC 2.1] Evaluate impact · [ICTICT517 KE 3] Methods of evaluation of competing ICT systems and products · [ICTICT517 FS Numeracy] · [ICTCLD401 KE 4] cost models and cloud economic theories · [ICTCLD502 KE 3] cloud cost models as they relate to scalability of cloud infrastructure · [ICTCLD401 KE 1] industry technology standards (in selecting AWS services)*

A full 5-year CBA comparing Option A (in-house renewal) and Option B (cloud migration to AWS). The detailed line items per option live in **Appendix 1**; the summary tables in this section are the headline view the board reads.

### 7.1 Assumptions

Confirm or adjust the assumptions below. Any change requires a justification note.

| Assumption | Value | Used as-is? |
|---|---|---|
| LMS user population | *800 students + 60 staff* | [ ] yes / [ ] adjusted — see note |
| Annual student growth | *+15% per year* | [ ] yes / [ ] adjusted |
| Current LMS availability | *99.2%* | [ ] yes / [ ] adjusted |
| Target LMS availability | *99.9%* | [ ] yes / [ ] adjusted |
| ICT FTE fully-loaded cost | *$115,000 / year* | [ ] yes / [ ] adjusted |
| Indicative cost of downtime (teaching hours) | *$750 / hour* | [ ] yes / [ ] adjusted |
| Inflation factor applied | [FILL IN — your choice, justify] | n/a |
| AWS pricing region | `ap-southeast-2` (Sydney) — required for data residency | n/a |
| RI / Savings Plan strategy | [FILL IN] | n/a |

### 7.2 Option A — In-house renewal (5-year summary)

| | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 | 5-year |
|---|---:|---:|---:|---:|---:|---:|
| One-off capital | $_____ | — | — | — | — | $_____ |
| Recurring | $_____ | $_____ | $_____ | $_____ | $_____ | $_____ |
| **Annual total** | $_____ | $_____ | $_____ | $_____ | $_____ | **$_____** |

Brief commentary (line-item detail in Appendix 1):

> [Your response]

### 7.3 Option B — Cloud migration to AWS (5-year summary)

| | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 | 5-year |
|---|---:|---:|---:|---:|---:|---:|
| One-off project | $_____ | — | — | — | — | $_____ |
| AWS direct | $_____ | $_____ | $_____ | $_____ | $_____ | $_____ |
| Staff + external (recurring) | (in project) | $_____ | $_____ | $_____ | $_____ | $_____ |
| **Annual total** | $_____ | $_____ | $_____ | $_____ | $_____ | **$_____** |

Brief commentary on AWS sizing assumptions and pricing strategy (line-item detail in Appendix 1):

> [Your response]

### 7.4 Avoided-downtime benefit

*Evidences: [ICTICT517 PC 2.1] (quantifying the impact of moving from 99.2% to 99.9% availability)*

| | Calculation | Value |
|---|---|---:|
| Avoided unavailability per year ((1 − 99.2%) − (1 − 99.9%)) × 8760 hr | $_____ | $_____ hr |
| Proportion during teaching hours | [FILL IN — your assumption] | $_____ % |
| Avoided downtime cost per year (× $750/hr) | $_____ | **$_____** |
| **5-year avoided-downtime benefit** | × 5 | **$_____** |

### 7.5 Comparison summary

| | Option A — In-house | Option B — Cloud (AWS) | Delta (B − A) |
|---|---:|---:|---:|
| One-off (Year 1) | $_____ | $_____ | $_____ |
| Recurring 5-year | $_____ | $_____ | $_____ |
| **5-year direct cost** | **$_____** | **$_____** | **$_____** |
| Avoided-downtime benefit (Option B only) | — | $_____ | $_____ |
| **Net 5-year position** | **$_____** | **$_____** | **$_____** |

#### Year-1 cash-flow comparison

*Evidences: [ICTICT517 PC 2.1] · [ICTICT517 PC 2.2] (Year-1 outlay is a material implementation-difficulty dimension)*

| | Year 1 outlay | Average annual Year 2–5 |
|---|---:|---:|
| Option A | $_____ | $_____ |
| Option B | $_____ | $_____ |

### 7.6 Sensitivity analysis

*Evidences: [ICTICT517 KE 2] Methods of evaluation and planning approaches to technical problems and strategic objectives · [ICTICT517 PC 2.1] (robustness of the impact evaluation under assumption changes)*

Pick at least two assumptions where a reasonable change would materially affect the outcome. Show the recalculation.

**Sensitivity 1:** [name of assumption]

| Original | Alternative | Effect on Option [A/B] 5-year | Effect on the recommendation |
|---|---|---:|---|
| $_____ | $_____ | $_____ | [Your response] |

**Sensitivity 2:** [name of assumption]

| Original | Alternative | Effect on Option [A/B] 5-year | Effect on the recommendation |
|---|---|---:|---|
| $_____ | $_____ | $_____ | [Your response] |

---

## 8. Risk and Impact Assessment

*Evidences: [ICTICT517 PC 2.1] Evaluate impact (non-financial dimensions) · [ICTICT517 PC 2.2] Evaluate difficulty · [ICTICT517 PE 5] evaluate the difficulty of implementing proposed changes*

### 8.1 Intangibles comparison

Provide a 1–2 sentence comparison per factor. **Be honest about trade-offs.**

| Factor | Option A — In-house | Option B — Cloud (AWS) |
|---|---|---|
| Achieving the 99.9% availability target | [Your response] | [Your response] |
| Recovery objectives (RTO ≤ 4h, RPO ≤ 1h) | [Your response] | [Your response] |
| Capacity for 15% annual student growth | [Your response] | [Your response] |
| Capacity for assessment-week peaks | [Your response] | [Your response] |
| YAT ICT staff capability impact | [Your response] | [Your response] |
| Vendor lock-in risk | [Your response] | [Your response] |
| Sustainability | [Your response] | [Your response] |
| Cyber security posture | [Your response] | [Your response] |
| Disaster recovery (whole-campus loss) | [Your response] | [Your response] |

### 8.2 Risk register (recommended option)

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| [FILL IN] | [H/M/L] | [H/M/L] | [Your response] |
| [FILL IN] | [H/M/L] | [H/M/L] | [Your response] |
| [FILL IN] | [H/M/L] | [H/M/L] | [Your response] |

---

## 9. Recommendation

*Evidences: [ICTICT517 PC 2.3] Prioritise proposed changes to refine opportunities and assist in scheduling implementation · [ICTICT517 PE 4] determine and prioritise proposed changes to meet organisational needs · contributes to [ICTICT517 PC 3.1] Develop action plan*

**Recommended option:** [ ] Option A — In-house renewal | [ ] Option B — Cloud migration to AWS

**Headline rationale (3–5 sentences — connect to your CBA findings, the intangibles, and the risk register):**

> [Your response]

This recommendation drives the prioritisation of changes and the action plan in §10.

---

## 10. Action Plan

*Evidences: [ICTICT517 PC 3.1] Develop action plan to implement proposed changes including prioritised schedule and consistency with organisational policy and procedures · [ICTICT517 PC 3.2] Detail standards, targets and implementation methods in action plan · [ICTICT517 PE 6] develop an action plan for implementation · [ICTICT517 KE 1] Key sections of an action plan for ICT implementation projects*

### 10.1 Prioritised changes

List the proposed changes in implementation priority order. Justify the ordering.

| # | Change | Priority rationale |
|---|---|---|
| 1 | [FILL IN] | [Your response] |
| 2 | [FILL IN] | [Your response] |
| 3 | [FILL IN] | [Your response] |
| ... | | |

### 10.2 Implementation schedule

Indicative schedule — durations and dependencies. Phase the work; do not propose a single all-at-once cutover unless the risk register supports it.

| Phase | Activities | Start | Duration | Dependencies | Owner |
|---|---|---|---|---|---|
| 1 | [FILL IN] | [FILL IN] | [FILL IN] | — | [FILL IN] |
| 2 | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| 3 | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

### 10.3 Standards, targets, and success metrics

| Aspect | Standard / target | How measured |
|---|---|---|
| Availability target | 99.9% | [Your response] |
| RPO target | ≤ 1 hour | [Your response] |
| RTO target | ≤ 4 hours | [Your response] |
| Cost envelope (Year 1) | $_____ | [Your response] |
| Cost envelope (Year 5 cumulative) | $_____ | [Your response] |
| Data residency | Australia (`ap-southeast-2`) | [Your response] |
| Other | [FILL IN] | [Your response] |

### 10.4 Implementation methods

For each phase, identify the methods, tools, and standards applied (e.g. AWS Well-Architected review at design milestones, change management procedure for production changes, etc.).

> [Your response]

### 10.5 Alignment with YAT change management procedure

State how the action plan aligns with YAT's documented change-management procedure. Identify which phases require change requests, ICT-manager approval, and senior-management sign-off.

> [Your response]

### 10.6 Action plan risk register (links to §8.2)

Cross-reference the risks identified in §8.2 against the implementation schedule. For each risk, state which phase(s) carry it and which mitigation is in place by the start of that phase.

> [Your response]

---

## 11. Next Steps and Decision Requested

*Evidences: [ICTICT517 PC 3.3] Provide action plan to superior for feedback and approval*

State precisely what you are asking the board to decide today:

- [ ] Approve Option [A / B] as the recommended approach
- [ ] Approve the action plan in §10 as the implementation roadmap
- [ ] Authorise the budget envelope in §10.3
- [ ] [Other — FILL IN]

Items deferred to later sign-off gates (e.g. specific procurement decisions, the high-risk cutover change request at the appropriate phase):

> [Your response]

---

## Sign-off

*Evidences: [ICTICT517 PC 3.3] Provide action plan to superior for feedback and approval*

Completed during / after the board presentation.

| Role | Name | Date | Signature |
|---|---|---|---|
| Prepared by (student) | | | |
| Reviewed by (MTS senior consultant — Pat Lin) | | | |
| Approved by (YAT ICT Manager — Sam Walker) | | | |

---

# Appendix 1 — Cost-Benefit Analysis: Detailed Line Items

*Evidences: [ICTICT517 FS Numeracy] · [ICTICT517 KE 3] · [ICTCLD401 KE 4] · [ICTCLD502 KE 3]*

The detailed line items underpinning the §7 summary tables. The totals from the tables below feed the summary in §7.

## A1.1 Option A — In-house renewal

### A1.1.1 One-off capital (Year 1) — YAT-provided inputs

| Item | Cost |
|---|---:|
| Replacement LMS server | *$25,000* |
| Backup tape library refresh + drive | *$8,000* |
| UPS upgrade | *$3,000* |
| One-off internal migration labour | *$15,000* |
| Other (specify, justify) | $_____ |
| **Total Year-1 capital** | **$_____** |

### A1.1.2 Recurring operational (per year) — YAT-provided inputs

| Category | Item | Annual cost |
|---|---|---:|
| Software licensing | Windows Server Standard | *$1,500* |
| | Antivirus / EDR | *$300* |
| | Monitoring / management tooling | *$2,000* |
| Power and facilities | Electricity + cooling | *$1,200* |
| | Server-room rent allocation | *$5,000* |
| | UPS battery (amortised annually) | *$500* |
| Backup | Tape media | *$1,500* |
| | Offsite tape storage | *$2,400* |
| | Backup software maintenance | *$1,500* |
| Staff time (apply $115k FTE rate) | LMS admin (~0.20 FTE) | $_____ |
| | Incident response (~0.05 FTE) | $_____ |
| External support | MTS application support | *$30,000* |
| Other (specify, justify) | | $_____ |
| **Total recurring per year** | | **$_____** |

### A1.1.3 Year-by-year projection — Option A

| | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 | 5-year |
|---|---:|---:|---:|---:|---:|---:|
| One-off capital | $_____ | — | — | — | — | $_____ |
| Recurring (with inflation if applied) | $_____ | $_____ | $_____ | $_____ | $_____ | $_____ |
| **Annual total** | $_____ | $_____ | $_____ | $_____ | $_____ | **$_____** |

*Carry the totals from this projection up to §7.2.*

## A1.2 Option B — Cloud migration to AWS

### A1.2.1 One-off project costs (Year 1) — your estimates

| Item | Cost | Source / rationale |
|---|---:|---|
| MTS migration labour | $_____ | [FILL IN] |
| YAT ICT staff time during migration | $_____ | [Your estimate, apply $115k FTE rate] |
| Parallel running of on-prem and cloud during cutover | $_____ | [FILL IN] |
| Decommissioning + secure data destruction | $_____ | [FILL IN] |
| Other (specify) | $_____ | [FILL IN] |
| **Total Year-1 project** | **$_____** | |

### A1.2.2 AWS direct recurring (per year) — your sizing + AWS pricing

State your sizing assumptions in the **Sizing notes** column. Attach your AWS Pricing Calculator export as evidence in Appendix 3.

| Category | Service / item | Sizing notes | Annual cost |
|---|---|---|---:|
| Compute | EC2 (baseline HA) | [e.g. 2× m6i.xlarge, RI] | $_____ |
| | EC2 autoscaling (peaks) | [e.g. up to N additional during ~10 weeks/year] | $_____ |
| Database | RDS Multi-AZ | [instance class, RI strategy] | $_____ |
| | RDS storage + backups | [GB] | $_____ |
| Network | Application Load Balancer | | $_____ |
| | NAT Gateway | | $_____ |
| | Data transfer out | [GB/month] | $_____ |
| Storage | EBS volumes (web tier) | [GB, type] | $_____ |
| | S3 (attachments + snapshots) | [GB] | $_____ |
| | AWS Backup (incl. cross-Region copy) | | $_____ |
| Monitoring | CloudWatch (metrics + logs + alarms) | | $_____ |
| Support | AWS Support tier | [Business required for ≤1h sev-1] | $_____ |
| Other (specify) | | | $_____ |
| **AWS direct per year** | | | **$_____** |

### A1.2.3 Staff time + ongoing external support (per year, Years 2–5) — your estimates

| Item | Annual cost | Rationale |
|---|---:|---|
| YAT ICT staff time (admin/monitoring, reduced vs on-prem) | $_____ | [FTE × $115k] |
| YAT ICT staff time (incident response) | $_____ | [FTE × $115k] |
| MTS ongoing support (post-migration) | $_____ | [FILL IN — justify any change from current $30k] |
| Other (specify) | $_____ | |
| **Staff + external per year** | **$_____** | |

### A1.2.4 Year-by-year projection — Option B

| | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 | 5-year |
|---|---:|---:|---:|---:|---:|---:|
| One-off project | $_____ | — | — | — | — | $_____ |
| AWS direct | $_____ | $_____ | $_____ | $_____ | $_____ | $_____ |
| Staff + external (recurring) | (in project) | $_____ | $_____ | $_____ | $_____ | $_____ |
| **Annual total** | $_____ | $_____ | $_____ | $_____ | $_____ | **$_____** |

*Carry the totals from this projection up to §7.3.*

---

# Appendix 2 — Knowledge Evidence

This appendix evidences your underlying knowledge of cloud computing, evaluation methods, and action-planning principles, **as applied to the work you have presented in this Business Case**. Answer concisely; cite specific sections of your own Business Case where relevant.

## A2.1 Selection-style questions

| Question | UoC reference | Your response |
|---|---|---|
| For each component of your proposed AWS solution, identify whether it is IaaS, PaaS or SaaS. Explain why you chose that service type for each. | [ICTCLD401 KE 3] | [Your response] |
| Which cloud deployment model — on-premises/private cloud, hybrid cloud, public cloud — does your solution use? Explain why this model was the right fit for YAT. | [ICTCLD401 KE 11] | [Your response] |
| Which industry technology standards informed your migration approach? Identify at least three and explain how each shaped a specific design or evaluation choice in this Business Case. | [ICTCLD401 KE 1] · [ICTCLD502 KE 1] | [Your response] |
| Which industry-standard hardware or software products does your solution include? For each, identify its general features, capabilities, and the role it plays in the YAT solution. | [ICTCLD401 KE 2] · [ICTCLD502 KE 2] | [Your response] |
| Which cloud cost model(s) did you apply to your CBA's AWS option (e.g. pay-as-you-go, Reserved Instances, Savings Plans, Spot)? Explain why for each AWS service, and how the model relates to scalability. | [ICTCLD401 KE 4] · [ICTCLD502 KE 3] | [Your response] |

## A2.2 Demonstration-style questions

| Question | UoC reference | Your response |
|---|---|---|
| How does your action plan in §10 demonstrate the key sections expected of an ICT implementation action plan? Identify each key section and where it appears. | [ICTICT517 KE 1] | [Your response] |
| Which methods of evaluation and planning approaches did your Business Case apply to YAT's strategic and technical problems? Cite specific sections of the Business Case where each method is applied. | [ICTICT517 KE 2] | [Your response] |
| How did you evaluate competing ICT systems and products in this Business Case? Identify the method and where the evaluation is documented. | [ICTICT517 KE 3] | [Your response] |
| Which current or emerging ICT system / product trends informed your recommendation? Be specific about where in your reasoning the trend was material. | [ICTICT517 KE 4] | [Your response] |

---

# Appendix 3 — Supporting Research

Attach as separate files or include inline links:

- AWS Pricing Calculator export(s) covering the Appendix 1 AWS line items
- Source documents cited in §3 industry-environment research (URLs + access dates)
- Other supporting research

---

# Appendix 4 — Feedback Record

Completed during / after the board presentation event using the `Feedback Record template`. The completed feedback record is attached to this Business Case as part of the AT1 submission bundle.
