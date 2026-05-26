# YAT LMS HA Deployment Report — Template

**Document type:** Student-fillable template (downloadable from the YAT intranet Templates section)
**Relevant to:** S1-CL1 AT3 Part B
**Status:** DRAFT (Claude v1, 2026-05-25). All section prompts + KE questions + reflection prompts are Claude-drafted — **TBD** confirm wording before issuing to students.

---

> **⚠️ AUTHORING NOTES (out-of-template) — not to be included in the student-facing artefact:**
>
> This template uses the **same shape and major sections** as the AT2 Deployment Report template (`template-deployment-report-S1-CL1-AT2.md`) so the two reports are directly comparable. Section headings sit at the same place; what differs is the *detail of the prompts within each section* — HA-specific build narrative, HA simulation work (failure + resize) in §6, HA-specific KE questions in §8, HA-flavoured screenshots in Appendix A.
>
> **UoC traceability map** (which template section evidences which UoC item — used by assessor benchmark; not visible to students):
>
> | Template section / appendix | UoC items evidenced |
> |---|---|
> | §1 Executive Summary | [ICTCLD401 PC 4.1] — partial *(document + communicate work, written executive-level)* |
> | §2 Engagement Context | *(references AT1, AT2, the student's own HA Design — not direct UoC)* |
> | §3 Scope of Deployment | *(scoping — what's in this HA phase, what stays for a later phase)* |
> | §4 Build Narrative (HA implementation) | [ICTCLD502 PC 4.1] *(implement architecture design)* across all sub-sections; [ICTCLD502 PE 1] *(implement half)*; [ICTCLD502 PE 2] *(deploy half — autoscaling)*; [ICTCLD502 PE 4] *(use cloud management console / SDK / CLI)* |
> | §5 Configuration Decisions | *(rationale for HA implementation choices)* |
> | §6 Testing, Simulation and Validation | [ICTCLD502 PC 4.2] *(connectivity)*; [ICTCLD502 PC 4.3] *(monitor + measure availability)*; [ICTCLD502 PC 4.4] *(simulate failures + confirm fault tolerance)*; [ICTCLD502 PC 4.5] *(simulate resizing + measure availability impact)*; [ICTCLD502 PC 4.6] *(compare + document simulation findings)*; [ICTCLD502 PC 5.1] *(adjust + improve availability per simulations)*; [ICTCLD502 PE 3] *(simulate failures and demonstrate fault tolerance)*; [ICTCLD502 PE 5] *(define, monitor, record availability)* |
> | §7 Operational Handover | [ICTCLD401 PC 4.3] *(save documentation per organisational policies)*; [ICTCLD502 PC 5.2] *(confirm, seek and respond to feedback)*; [ICTCLD502 PC 5.3] *(obtain final sign off)* |
> | §8 Knowledge Evidence Responses | [ICTCLD502 KE 4] *(HA concepts: FT, SPOF, MTTF/MTTR/MTBF, RTO/RPO, SLAs, scalability)*; [ICTCLD502 KE 5] *(testing and debugging)*; [ICTCLD502 KE 6] *(availability measurement)*; [ICTCLD502 KE 7] *(built-in vs designed FT)*; [ICTCLD502 KE 8] *(load balancing + autoscaling for availability)*; [ICTCLD502 KE 9] *(monitoring techniques + metrics)* |
> | Appendix A — Build Evidence | [ICTCLD502 PE 1, PE 2] *(the built HA artefacts)*; [ICTCLD502 PE 4] *(console screenshots)* |
> | Appendix B — Configuration Exports | [ICTCLD502 PE 4] *(deeper config evidence)* |
> | Appendix C — Simulation and Test Evidence | [ICTCLD502 PE 3] *(failure-simulation evidence)*; [ICTCLD502 PE 5] *(availability measurement)*; [ICTCLD502 PC 4.4, 4.5, 4.6]; [ICTCLD502 FS Problem solving] |
> | Appendix D — Reflections | [ICTCLD502 FS Self-management]; [ICTCLD401 FS Learning, Planning and organising, Self-management] |
> | §9 Document quality | [ICTCLD401 FS Writing]; [ICTCLD502 FS Reading] |
>
> Foundation Skills evidenced through the report itself: [ICTCLD401 FS Reading, FS Writing]; [ICTCLD502 FS Reading].

---

## Cover sheet

| | |
|---|---|
| **Engagement** | YAT LMS Cloud Migration — HA Hardening Phase |
| **Engagement reference** | YAT-LMS-MIG-2026 |
| **Report version** | 1.0 |
| **Submitted by (consultant name)** | [Your name] |
| **Consultant role** | MTS Consultant |
| **Student ID** | [Your student ID] |
| **Date submitted** | [DD/MM/YYYY] |
| **Submitted to** | Sam Walker, YAT ICT Manager · Pat Lin, MTS Senior Consultant |
| **Companion document** | YAT LMS Cloud Architecture — HA Design v1.0 (Part A of this AT3 submission — the design this report implements) |

---

## §1 Executive Summary

*Provide a brief (≤ 1 page) summary of the HA hardening phase. Write this section last, after the rest of the report is complete.*

Cover at minimum:
- What HA changes were applied (one or two sentences — Multi-AZ DB, cross-AZ ASG, cross-AZ ALB, HA monitoring, cross-Region backup as applicable)
- Whether the 99.9% availability target is now achievable
- The simulation outcomes in headline form (failure simulation: passed / failed; resize simulation: outcome)
- Any limitations or items deferred to a later phase

*[Your executive summary here — approximately 250–400 words]*

---

## §2 Engagement Context

*Brief context for the reader. References the prior phases. ≤ ½ page.*

Cover:
- The strategic context: the board-approved action plan from AT1 → the AT2 foundation build → this AT3 HA hardening
- The HA Design document (Part A of this AT3 submission) — the specification this report implements
- Your role: MTS consultant returning to harden the AT2 baseline for HA
- The maintenance-window context for this phase (Saturday late-night window — see §3)
- Scope hand-off: confirm that any further work (cross-Region DR, application-layer HA) is deferred to a separate engagement

*[Your engagement context here]*

---

## §3 Scope of Deployment

*What is included in this HA phase, and what is deferred. ≤ ½ page.*

Restate from the HA Design (in your own words):

- **In scope of this report (the implementation work):** Multi-AZ database, cross-AZ compute resilience, cross-AZ ALB targets, HA-tuned monitoring and alarms, cross-Region backup (if in design)
- **Maintenance window context:** the implementation was performed within a single Saturday late-night maintenance window (~3.5 hours simulated), with the requirement that the LMS be back online at the end of the window either with HA hardening complete or with a clean rollback
- **Out of scope (carried into future phases):** cross-Region DR with active-active or hot-standby, application-layer HA (DOODLE clustering — YAT IT scope), end-of-engagement organisational change management activities

*[Your scope statement here]*

---

## §4 Build Narrative

*Layer-by-layer account of the HA changes you applied. For each layer below, write a short narrative paragraph or two about what changed from the AT2 baseline, and cross-reference the relevant Appendix A screenshots and Appendix B configuration exports.*

### 4.1 IAM (changes from AT2 baseline)

*Cover: any IAM changes needed for the HA work (typically minimal — possible additions: AWS Backup service role, cross-Region replication role for S3). State explicitly if no IAM changes were needed. Cross-reference: Appendix A screenshots, Configuration exports.*

*[Your IAM narrative here]*

### 4.2 Network topology (cross-AZ subnets)

*Cover: the new subnets added in the second AZ (`public-web-b`, `private-app-b`, `private-data-b`), route table associations, no change to IGW or NAT (or new NAT in second AZ if you went that way). Cross-reference: Screenshots and config exports.*

*[Your network narrative here]*

### 4.3 Compute layer (cross-AZ ASG)

*Cover: ASG expansion to include the new AZ subnets, capacity changes (typically min raised from 1 to ≥2 across two AZs), scaling-policy tuning if changed, launch template changes if any. Cross-reference: screenshots + config exports.*

*[Your compute narrative here]*

### 4.4 Application Load Balancer (cross-AZ targets)

*Cover: ALB subnet group extended to include both AZs, target group health-check verification across AZs. Cross-reference.*

*[Your ALB narrative here]*

### 4.5 Database layer (Multi-AZ)

*Cover: enabling Multi-AZ on the RDS instance, the standby AZ, the brief failover blip observed during conversion, post-conversion verification. Cross-reference: RDS console screenshot showing Multi-AZ status.*

*[Your database narrative here]*

### 4.6 Storage (cross-Region backup)

*Cover: cross-Region snapshot copies (if in HA design), AWS Backup configuration, S3 cross-Region replication (if applicable). Cross-reference.*

*[Your storage narrative here]*

### 4.7 Security (HA-related adjustments)

*Cover: any security group adjustments needed for cross-AZ traffic, any HA-related security additions. Typically minimal — state explicitly if no changes. Cross-reference.*

*[Your security narrative here]*

### 4.8 Monitoring (HA-tuned alarms)

*Cover: the HA-tuned CloudWatch alarms added (availability metric tracking, per-AZ target counts, RDS failover detection, cross-AZ latency, service-level dashboard). This section is meaningfully bigger than the AT2 baseline monitoring narrative. Cross-reference: CloudWatch screenshots.*

*[Your monitoring narrative here]*

---

## §5 Configuration Decisions

*The HA design left some implementation-time decisions to you. For each decision you made during implementation, state your choice and briefly justify it against the HA requirements and the YAT LMS workload.*

| # | Decision point | Your decision | Rationale |
|---|---|---|---|
| C1 | RDS Multi-AZ apply timing — "apply immediately" vs "during next maintenance window" | *[Your choice]* | *[1–3 sentences — typically apply-immediately is OK during a planned maintenance window]* |
| C2 | ASG capacity post-HA (min/desired/max — must be ≥ 2 to survive an AZ failure) | *[Your numbers]* | *[Rationale referencing concurrent-user load + AZ-failure resilience]* |
| C3 | Cross-Region backup destination region (if in scope) | *[Your choice]* | *[Rationale]* |
| C4 | HA-tuned alarm thresholds (per-AZ instance count, replica lag, etc.) | *[Your thresholds]* | *[Rationale]* |
| *[Add additional decisions you made during implementation]* | | | |

---

## §6 Testing, Simulation and Validation

*Document the testing you ran to verify the HA design works. This section is meaningfully bigger than the AT2 testing section — it includes the failure and resize simulations that are the core of AT3's HA verification work.*

### 6.1 Connectivity tests (regression check)

*Re-verify the basic connectivity tests from AT2 still pass after the HA changes. Cross-reference: Test evidence C1, C2.*

| Test | Outcome (Pass/Fail) | Notes |
|---|---|---|
| ALB → EC2 health check (both AZs) | | |
| EC2 → RDS MySQL connection (Multi-AZ endpoint) | | |
| Cross-AZ ASG instances reach RDS | | |
| Pre-failover RDS endpoint resolution | | |

### 6.2 Failure simulation *(evidences [ICTCLD502 PC 4.4] · [ICTCLD502 PE 3])*

*Execute each failure simulation from your HA Design §6.1. For each, record the method used, the observed outcome, and reference the supporting evidence in Appendix C.*

| # | Simulation (from HA Design §6.1) | Method used | Observed outcome | LMS reachable throughout? | Evidence |
|---|---|---|---|---|---|
| F1 | *[e.g. EC2 instance termination]* | *[Terminated EC2 instance via console]* | *[ASG launched replacement within X seconds; ALB de-registered failed target; new target healthy at Y seconds]* | ☐ Yes ☐ No (briefly: explain) | Appendix C1 |
| F2 | *[e.g. RDS Multi-AZ failover]* | *[Reboot with failover]* | *[RDS failed over to standby in X seconds; LMS reconnections succeeded after retry]* | ☐ Yes (with brief blip) ☐ No | Appendix C2 |
| F3 | *[e.g. AZ network partition]* | *[Method — e.g. SG modification or instance termination across an AZ]* | *[…]* | | Appendix C3 |
| *[Add additional simulations as needed]* | | | | | |

### 6.3 Resize simulation *(evidences [ICTCLD502 PC 4.5])*

*Execute each resize simulation from your HA Design §6.2.*

| # | Simulation (from HA Design §6.2) | Method used | Observed outcome | Availability impact | Evidence |
|---|---|---|---|---|---|
| R1 | *[e.g. ASG manual capacity increase]* | *[set desired=4 via console]* | *[2 new instances launched in ~5 min; all healthy in ALB]* | *[No downtime; ALB target count grew gradually]* | Appendix C4 |
| R2 | *[e.g. RDS instance class change]* | *[modify db.m6i.large → db.m6i.xlarge, apply immediately]* | *[~45 sec failover blip during apply]* | *[≤ 1 min — application reconnected on retry]* | Appendix C5 |
| *[Add as needed]* | | | | | |

### 6.4 Availability measurement *(evidences [ICTCLD502 PC 4.3] · [ICTCLD502 PE 5])*

*Document how you set up the measurement of resource availability — and the data captured during the simulation window. Reference the CloudWatch dashboard or metric outputs.*

*[Your availability measurement narrative here. Examples: "I deployed a CloudWatch dashboard with the following widgets... The service-level metric for the LMS over the 3.5-hour maintenance window was X%, with brief dips of Y seconds during the RDS failover sim and Z seconds during the resize sim..."]*

### 6.5 Simulation findings — comparison against the documented HA design *(evidences [ICTCLD502 PC 4.6])*

*For each simulation, compare the observed outcome against the *expected* outcome you wrote in your HA Design §6 simulation plan. Where the actual diverges from the expected, document the divergence and the reason.*

| Simulation | Expected outcome (from HA Design) | Actual outcome | Divergence? Why? |
|---|---|---|---|
| F1 | *[…]* | *[…]* | *[None / explanation]* |
| F2 | *[…]* | *[…]* | *[…]* |
| *[…]* | | | |

### 6.6 Adjustments made per simulation outcomes *(evidences [ICTCLD502 PC 5.1])*

*Document any adjustments you made to the architecture, configuration, or monitoring based on what the simulations revealed. If no adjustments were needed (the design held up), state that explicitly with reasoning.*

*[Your adjustments narrative here]*

---

## §7 Operational Handover

*Hand-over information for YAT IT, who take over the HA-hardened infrastructure from here. Per the MTS scope statement in the role brief, organisational change management around any further LMS work is YAT IT's responsibility.*

### 7.1 Access for YAT ICT

*Confirm: who has what access post-handover, MFA enforcement, IAM group changes (typically unchanged from AT2 handover).*

### 7.2 Runbook references

*Pointer to:*
- The HA Design document (Part A of this AT3 submission) — operational reference
- The AT2 supplied baseline design — the design this HA work supersedes
- The HA-tuned monitoring + alarms list (§4.8 of this report) + notification destinations
- The simulation outcomes (§6) — operational expectations for future HA testing
- The cross-Region backup schedule (if applicable) + restoration procedure

### 7.3 Known limitations and what's not in this phase

*Be explicit about what's still open. Examples:*

- *Cross-Region DR (active-active or hot-standby) — not in scope; would require additional consulting engagement*
- *Application-layer HA — YAT IT scope (DOODLE clustering, session affinity tuning)*
- *Ongoing chaos-engineering programme — would be a separate operational engagement*
- *Cost optimisation post-HA — Multi-AZ DB roughly doubles the DB cost line; documented for YAT planning*

### 7.4 Documentation filing *(evidences [ICTCLD401 PC 4.3])*

*Per YAT's documented procedures, this report and its appendices are to be filed in the YAT ICT shared documentation repository per the `internal-records-management-policy.md` and `internal-backup-retention-policy.md`. Confirm filing and provide reference.*

| Item | Filed in | Reference |
|---|---|---|
| HA Design document (Part A) | YAT ICT shared documentation | *[Reference]* |
| This HA Deployment Report (v1.0) | YAT ICT shared documentation | *[Reference]* |
| Configuration exports (Appendix B) | YAT ICT shared documentation | *[Reference]* |
| Simulation evidence (Appendix C) | YAT ICT shared documentation | *[Reference]* |

### 7.5 Feedback record *(evidences [ICTCLD502 PC 5.2])*

*Capture the feedback received from YAT ICT (or in-scenario equivalents — Sam Walker, Pat Lin) on the HA Design and the HA implementation. Use the YAT Feedback Record template (or document inline). Cover at least: feedback received, source of the feedback, your response, and any resulting actions.*

| Feedback received | From | Your response | Resulting action |
|---|---|---|---|
| *[e.g. "The cost impact of Multi-AZ doubling the DB line wasn't called out in the design — please document"]* | *[Sam Walker, YAT ICT Manager]* | *[Acknowledged; updated §4.5 and §7.3 to call out the cost impact explicitly]* | *[HA Design v1.1 issued (if applicable)]* |
| *[…]* | | | |

### 7.6 Sign-off *(evidences [ICTCLD502 PC 5.3])*

*Final sign-off from the role-played YAT ICT Manager confirming acceptance of the HA hardening work.*

| | |
|---|---|
| **Approved by (role-played YAT ICT Manager)** | Sam Walker |
| **Signature** | _______________________ |
| **Date** | [DD/MM/YYYY] |
| **Acceptance note** | *[Free-form acceptance — e.g. "HA hardening accepted. Multi-AZ database, cross-AZ ASG, and HA-tuned monitoring all confirmed operational. Cross-Region DR remains open for a future engagement."]* |

---

## §8 Knowledge Evidence Responses

*Answer each question below. Reference specific sections, decisions, components, or simulation outcomes from your own report — do not give generic textbook answers.*

### Q1 — HA concepts in your design *(evidences [ICTCLD502 KE 4])*

In your own design and implementation, you encountered several HA concepts: fault tolerance, single points of failure, RPO/RTO, SLAs, vertical vs horizontal scalability, MTTF/MTTR/MTBF.

For **at least three** of these concepts:

- (a) State the concept in your own words
- (b) Identify where in *your own work* (HA Design or this report) the concept applies — name the specific component or section
- (c) Briefly explain how the concept affected your design or implementation choices

*[Your response — ~350–500 words]*

### Q2 — Testing and debugging techniques *(evidences [ICTCLD502 KE 5])*

Your failure simulations and resize simulations (§6.2, §6.3) used specific techniques.

- (a) Describe **one** technique you used to **avoid causing** a single point of failure during your testing (e.g. ensuring traffic could still reach the LMS via the surviving AZ while you tested a failure in the other AZ)
- (b) Describe **one** debugging technique you used (or could have used) if a simulation result didn't match what you expected — e.g. how would you isolate whether a failover took longer than expected because of DB-level delays vs application-level connection retry behaviour?

*[Your response — ~200–300 words]*

### Q3 — Tools and techniques to measure availability impact *(evidences [ICTCLD502 KE 6])*

Your simulations (§6.2, §6.3) generated availability data.

- (a) Name the specific AWS tools you used to measure availability impact (e.g. CloudWatch metrics, CloudWatch alarms, ALB access logs, RDS event log)
- (b) For **one** simulation, state how you computed the actual availability impact (e.g. "I ran `curl` in a loop with 1-second interval against the ALB DNS name during the RDS failover sim; counted the failed responses to estimate the outage window")
- (c) State the limitation of your measurement approach (what wasn't captured)

*[Your response — ~200–300 words]*

### Q4 — Built-in vs designed fault tolerance *(evidences [ICTCLD502 KE 7])*

AWS services vary in how much fault tolerance is "built in" vs how much you have to design in yourself.

For **each of these three** services in your design, state whether the fault tolerance is **built-in by AWS** or **designed in by you**, and explain briefly:
- (a) S3
- (b) Amazon RDS (general, then specifically Multi-AZ)
- (c) Application Load Balancer

*[Your response — ~200–300 words]*

### Q5 — Load balancing and autoscaling for availability *(evidences [ICTCLD502 KE 8])*

Your design uses both load balancing (ALB) and autoscaling (ASG).

- (a) Explain how the **combination** of load balancing + autoscaling delivers availability above what either provides alone
- (b) Identify **one scenario** in your YAT design where this combination saved the LMS from going down (real or hypothetical — referenced to your simulation evidence if applicable)

*[Your response — ~150–250 words]*

### Q6 — Performance monitoring techniques and metrics *(evidences [ICTCLD502 KE 9])*

Your HA-tuned monitoring (§4.8) includes specific CloudWatch alarms and a service-level metric tracking approach.

- (a) Pick **one** metric you set up specifically for HA monitoring (i.e. didn't exist in the AT2 baseline)
- (b) Explain what the metric measures
- (c) State the threshold you set and why
- (d) State what failure mode the metric detects

*[Your response — ~150–250 words]*

---

## Appendix A — Build evidence (Screenshots)

*Capture each screenshot below from the AWS Management Console after the HA hardening is complete. Each screenshot must clearly show the named items, with the AWS region indicator visible (top-right).*

| # | Screenshot description | What must be visible |
|---|---|---|
| A1 | **VPC Subnets list — cross-AZ** | All six subnets (`public-web-a/b`, `private-app-a/b`, `private-data-a/b`) with correct CIDRs and AZs (showing both `ap-southeast-2a` and `ap-southeast-2b`) |
| A2 | **EC2 Auto Scaling Group — Instance management** | ASG with desired/min/max ≥ 2 across both AZs; instances visible in both AZs and listed as healthy |
| A3 | **EC2 → Load Balancers → Target group health** | ALB target group showing healthy targets in **both** AZs |
| A4 | **RDS Databases — Multi-AZ enabled** | RDS instance in `available` state, with Multi-AZ shown as **Yes** and standby AZ visible |
| A5 | **RDS Event log — Multi-AZ conversion event** | Event log showing the Multi-AZ conversion event |
| A6 | **CloudWatch Alarms — HA-tuned alarms list** | The HA-tuned alarms you added (per-AZ instance count, RDS failover detection, cross-AZ latency, etc.) |
| A7 | **CloudWatch Dashboard — service-level metric** | The availability/service-level dashboard you created for HA monitoring |
| A8 | **EC2 → ASG → Activity history — failure simulation event** | ASG activity history showing the scale-out / replacement event from your failure simulation (§6.2) |
| A9 | **CloudWatch Metrics — failure simulation timeline** | Graph showing the metrics during your failure simulation (instance health drop, replacement, recovery) |
| A10 | **RDS Event log — failover simulation event** | Event log showing the failover from primary to standby during your simulation |
| A11 | **CloudWatch — availability metric during maintenance window** | Service-level metric graph showing the overall availability across the 3.5-hour maintenance window, with any dips visible |
| A12 | **AWS Backup or cross-Region backup configuration** *(if in scope)* | The backup plan / cross-Region copy configuration |
| *[Add additional screenshots as your design requires]* | | |

---

## Appendix B — Configuration exports

*Export each configuration below and attach to this report. Place each export as a code block or attached file.*

| # | Export | Recommended source |
|---|---|---|
| B1 | Updated VPC + subnet + route table configuration | `aws ec2 describe-vpcs`, `describe-subnets`, `describe-route-tables` |
| B2 | Updated ASG + launch template configuration | `aws autoscaling describe-auto-scaling-groups` |
| B3 | Updated ALB + target group configuration (cross-AZ) | `aws elbv2 describe-load-balancers`, `describe-target-groups` |
| B4 | RDS instance configuration (showing Multi-AZ) | `aws rds describe-db-instances` |
| B5 | CloudWatch alarm configurations (HA-tuned set) | `aws cloudwatch describe-alarms` |
| B6 | AWS Backup / cross-Region replication configuration *(if in scope)* | `aws backup describe-backup-plan` or `aws s3api get-bucket-replication` |

---

## Appendix C — Simulation and test evidence

*Attach evidence supporting the simulations recorded in §6.*

| # | Test/simulation | Evidence type |
|---|---|---|
| C1 | Pre-implementation connectivity tests (regression baseline) | Terminal output / screenshots — ALB reachable, EC2 → RDS works, etc. |
| C2 | Failure simulation F1 — EC2 instance termination | ASG activity history (also A8), CloudWatch metric graph showing recovery time (also A9), `curl` log showing LMS reachable throughout |
| C3 | Failure simulation F2 — RDS failover | RDS event log (also A10), application-side connection retry log showing reconnect after failover, measurement of failover duration |
| C4 | Resize simulation R1 — ASG capacity increase | ASG activity history showing new instances + time-to-healthy, ALB target group during the change |
| C5 | Resize simulation R2 — RDS instance class change | RDS event log showing modify-and-apply, `curl` log measuring the failover-blip duration |
| C6 | Service-level availability measurement (CloudWatch over the maintenance window) | CloudWatch metric graph (also A11), computed availability % over the window |
| *[Additional evidence as your simulations require]* | | |

---

## Appendix D — Reflections

*Two short reflective responses, ~150–250 words each. Be honest — these are about your own learning during this HA phase.*

### R1 — Decisions in hindsight

Looking back at the HA hardening work:

- Identify **one decision** you made (during the HA design or during implementation) that turned out to be the right call — briefly evaluate why the outcome confirmed the decision
- Identify **one decision (or assumption)** you would revise if you were to do this again — briefly evaluate what you'd do differently and why

*[Your reflection]*

### R2 — Problem solving under time pressure

The maintenance window for this work was time-boxed (~3.5 hours simulated as a Saturday late-night slot). If you had a moment during the window where something didn't go as planned — a failover took longer than expected, a configuration change didn't behave as documented, a simulation result diverged from the design's expected outcome:

- Briefly describe the moment
- Describe how you reasoned through it under time pressure
- State what you would do differently next time to either avoid the issue or resolve it faster

If no such moment occurred (you executed the plan without incident), describe what you think the most likely "gotcha" would have been and how you'd have responded to it.

*[Your reflection]*

---

## §9 Document control

| | |
|---|---|
| **Document version** | 1.0 — HA Deployment Report (post-implementation submission) |
| **Author** | [Your name], MTS Consultant |
| **Engagement** | YAT LMS Cloud Migration — HA Hardening Phase |
| **Date submitted** | [DD/MM/YYYY] |
| **Distribution** | Sam Walker (YAT ICT Manager), Pat Lin (MTS Senior Consultant) |
| **Companion document** | YAT LMS Cloud Architecture — HA Design v1.0 (Part A of this AT3 submission) |
| **Successor document** | n/a — this submission closes out MTS's role on the YAT LMS Cloud Migration engagement |
