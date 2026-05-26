# YAT LMS Cloud Architecture — HA Design — Template

**Document type:** Student-fillable template (downloadable from the YAT intranet Templates section)
**Relevant to:** S1-CL1 AT3 Part A
**Status:** DRAFT (Claude v1, 2026-05-25). All section prompts are Claude-drafted — **TBD** confirm wording before issuing to students.

---

> **⚠️ AUTHORING NOTES (out-of-template) — not to be included in the student-facing artefact:**
>
> This `.md` is the **source-of-truth** for the HA Design template. It will need to be transferred to a Word document for student download from the YAT intranet (mirror of the AT2 supplied design + AT2 Deployment Report template approach).
>
> **Design intent:** the HA Design is the student's response to the AT2 supplied baseline. Section structure approximately mirrors the AT2 supplied design (`internal-lms-cloud-architecture-design-S1-CL1-AT2.md`) so students see the parallel, but adds a pre-design **Review of AT2 baseline** section ahead of the design proper (to evidence the 502 architecture-review PCs), and adds **Implementation sequencing** + **Simulation plan** sections at the end (to feed the AT3 Part B work).
>
> **UoC traceability map** (which template section evidences which UoC item — used by assessor benchmark; not visible to students):
>
> | Template section | UoC items evidenced |
> |---|---|
> | §1 Purpose and scope | (scoping; not direct UoC evidence) |
> | §2 Design inputs and HA requirements | [ICTCLD502 PC 1.1] — Determine reliability, recoverability and service levels required for application |
> | §3 Review of AT2 baseline architecture | [ICTCLD502 PC 2.1] · [ICTCLD502 PC 2.2] · [ICTCLD502 PC 2.3] · [ICTCLD502 PC 2.4] · [ICTCLD502 PC 2.5] |
> | §4 HA architecture design | [ICTCLD502 PC 3.1] · [ICTCLD502 PC 3.2] · [ICTCLD502 PC 3.3] · [ICTCLD502 PC 3.4] · [ICTCLD502 PC 3.5] · [ICTCLD502 PE 1] *(design half)* · [ICTCLD502 PE 2] *(design half)* |
> | §5 Implementation sequencing | (plan feeding Part B; not direct UoC) |
> | §6 Simulation and verification plan | (plan feeding Part B; PC 4.4, 4.5, 4.6 evidence is captured in Part B execution) |
> | §7 Out of scope of this design | (scoping) |
> | §8 References | [ICTCLD502 FS Reading] — interprets complex technical and operational documentation |
> | §9 Document control | (administrative) |
>
> The student is **the author** of this design (unlike AT2 where the design was supplied). The HA Design becomes Part A of the AT3 submission.

---

## Cover sheet

| | |
|---|---|
| **Engagement** | YAT LMS Cloud Migration — HA Hardening Phase |
| **Engagement reference** | YAT-LMS-MIG-2026 |
| **Document version** | 1.0 |
| **Authored by (consultant name)** | [Your name] |
| **Consultant role** | MTS Consultant |
| **Student ID** | [Your student ID] |
| **Date submitted** | [DD/MM/YYYY] |
| **Submitted to** | Sam Walker, YAT ICT Manager · Pat Lin, MTS Senior Consultant |
| **Supersedes** | YAT LMS Cloud Architecture — Baseline Design v1.0 (AT2 — produced by MTS Senior Architecture) |

---

## §1 Purpose and scope

*Brief — what this design covers and what it doesn't. ≤ ½ page.*

State:

- This is the **HA Design** for the YAT LMS cloud infrastructure — the second phase of architectural work following the AT2 baseline design
- The design specifies the changes needed to take the AT2 baseline (single-AZ, non-HA) to YAT's strategic 99.9% availability target
- **In scope of this design:** Multi-AZ database, cross-AZ compute resilience, HA-tuned monitoring, cross-Region backup considerations, recovery-objective improvements, autoscaling tuned for availability
- **Out of scope of this design** (see also §7): DR to a second AWS region with active-active or hot-standby, application-layer HA (DOODLE LMS clustering — that's a YAT IT concern), zero-downtime migration of student PII, multi-region replication

*[Your purpose and scope statement here]*

---

## §2 Design inputs and HA requirements

*Brief — the inputs you're designing against. ≤ 1 page.*

### 2.1 Inputs from prior phases

Identify the source documents you are building this HA design from:

- The **AT2 baseline design** (`internal-lms-cloud-architecture-design-S1-CL1-AT2.md`) — what was deployed
- The **AT2 Deployment Report** (your own work from AT2) — what was actually built (and any deviations from the baseline)
- The **LMS Application Specification** (`internal-lms-application-spec-S1-CL1-AT1.md`) — what the workload is
- The **LMS Cloud Migration Requirements** (`internal-lms-cloud-migration-requirements-S1-CL1-AT1.md`) — the SLA targets the design must meet
- The **HA Database Requirements** (`internal-ha-database-requirements-S1-CL1-AT3.md`) — specific HA database expectations

### 2.2 HA requirements

State the targets the design must achieve (these come from the migration requirements / LMS app spec):

| Service-level metric | Target |
|---|---|
| Availability (rolling 12 months) | **99.9%** *(per ICT Strategic Plan)* |
| RPO (acceptable data loss in incident) | **≤ 1 hour** |
| RTO (time to recover from a major outage) | **≤ 4 hours** |
| Support response (severity-1) | **≤ 1 hour** from cloud vendor |

*[Restate / extend with any additional reliability, recoverability or service-level requirements you identify from the migration brief or other source documents]*

---

## §3 Review of AT2 baseline architecture

*The review section. The student documents what's in the AT2 baseline that needs HA treatment.*

### 3.1 Architecture review *(evidences [ICTCLD502 PC 2.1])*

*Review the AT2 baseline architecture against HA requirements. Cover at least: compute layer (EC2/ASG), load balancing (ALB), database layer (RDS), network layer (subnets, AZ distribution), monitoring layer. Identify how each layer currently meets — or fails to meet — HA expectations.*

*[Your architecture review here]*

### 3.2 Single points of failure *(evidences [ICTCLD502 PC 2.2])*

*Identify every single point of failure (SPOF) in the AT2 baseline. A SPOF is any component whose failure would take the LMS offline. Tabulate at least: the AT2 component, the failure mode, the consequence to LMS availability.*

| Component | Failure mode | Consequence to LMS availability |
|---|---|---|
| *[e.g. RDS Single-AZ instance]* | *[Instance fails, AZ outage]* | *[LMS offline until restore (minutes-to-hours), data loss up to last backup]* |
| … | … | … |

### 3.3 Recovery objectives — AT2 baseline (current state) *(evidences [ICTCLD502 PC 2.3])*

*Estimate the RPO and RTO the AT2 baseline currently achieves, per component and overall. Compare against the targets in §2.2.*

| Component | Estimated RPO (current) | Estimated RTO (current) | Meets target? |
|---|---|---|---|
| RDS Single-AZ database | *[e.g. up to 24 hr — last automated backup]* | *[e.g. 2–6 hr — backup restore]* | ☐ Yes ☐ No |
| EC2 instances (ASG with min=1) | *[…]* | *[…]* | ☐ Yes ☐ No |
| LMS application data on EBS | *[…]* | *[…]* | ☐ Yes ☐ No |
| LMS attachments on S3 | *[…]* | *[…]* | ☐ Yes ☐ No |
| Overall LMS service | *[…]* | *[…]* | ☐ Yes ☐ No |

### 3.4 Components requiring vertical scaling *(evidences [ICTCLD502 PC 2.4])*

*Identify components in the AT2 baseline that can only scale vertically (resize) rather than horizontally (add instances). For each, state the availability impact during vertical scaling — i.e. how long is the LMS affected when this component is resized.*

| Component | Vertical scale required for | Availability impact during scale |
|---|---|---|
| *[e.g. RDS instance class]* | *[CPU / memory growth]* | *[Modify-and-apply incurs ~5–30 min downtime; can be done in maintenance window]* |
| *[e.g. EBS volume size]* | *[Storage growth]* | *[Online resize available — no downtime; OS-level expansion required after]* |
| … | … | … |

### 3.5 Review findings summary *(evidences [ICTCLD502 PC 2.5])*

*Briefly summarise the gap between the AT2 baseline and YAT's HA requirements. State explicitly: which targets are met, which targets are not, and which components drive the gap.*

*[Your review findings here — ≤ 250 words]*

---

## §4 HA architecture design

*The design proper. The student documents the HA-equivalent design that addresses the gaps identified in §3.*

### 4.1 Design assumptions and constraints

*Inherit assumptions from the AT2 baseline (region, application stack, data residency, etc.). Add any HA-specific assumptions (e.g. RDS Multi-AZ within the same region; cross-Region backup acceptable; etc.).*

*[Your additional assumptions here]*

### 4.2 AWS account and region

*Confirm: same `ap-southeast-2` region (data residency); same AWS Academy account. Note any new region needed (e.g. cross-Region backup destination).*

*[Your statement here]*

### 4.3 Identity and Access Management (IAM)

*State changes to IAM from the AT2 baseline (if any). HA hardening typically doesn't change IAM — but document if you've added roles for cross-Region replication, AWS Backup, etc.*

*[Your IAM section here]*

### 4.4 Network topology

*Document the cross-AZ network topology. Specifically: which new subnets are added in which additional AZ, how route tables change, how the Internet Gateway / NAT Gateway configuration changes (or not).*

| Subnet | CIDR | AZ | Purpose | New for HA? |
|---|---|---|---|---|
| `public-web-a` | `10.0.1.0/24` | `ap-southeast-2a` | Web / ALB | No (AT2) |
| *[Add new subnets here]* | … | … | … | Yes |

*[Your network design narrative here]*

### 4.5 Compute layer (EC2 + ASG)

*Document the HA changes to the compute tier: ASG capacity (min/desired/max), AZ distribution, launch template changes (if any), scaling policy adjustments.*

*[Your compute design here — specifically:*
- *ASG cross-AZ configuration*
- *Capacity adjustments (typically min=2 minimum across two AZs to survive an AZ failure)*
- *Scaling policy tuning for HA (more aggressive scale-out during assessment-window peaks?)*
- *Health check configuration*

### 4.6 Application Load Balancer (ALB)

*Document any ALB changes. ALB is multi-AZ-capable by default — the change is typically adding the new AZ subnets to the ALB's subnet group so traffic distributes across both AZs.*

*[Your ALB section here]*

### 4.7 Database layer (RDS)

*Document the RDS Multi-AZ design. Specifically: enabling Multi-AZ, the standby AZ, the failover behaviour, the impact on connection endpoints (single endpoint resolves to current primary), backup retention adjustments if any.*

*[Your RDS HA design here]*

### 4.8 Storage

*Document HA changes to storage: S3 cross-Region replication (if proposed), EBS snapshot policy changes, RDS automated backup cross-Region copy (if proposed).*

*[Your storage section here]*

### 4.9 Security

*Document any security adjustments needed for the HA design. Most security groups remain unchanged when adding AZs (the SG rules apply across AZs), but document any specific HA-related security considerations.*

*[Your security section here]*

### 4.10 Monitoring

*Document the HA-tuned monitoring additions. This is meaningfully bigger than the AT2 baseline monitoring. Include at minimum:*
- *Availability metric tracking (per-AZ EC2 instance counts, per-AZ ALB target counts)*
- *RDS replica lag (if applicable)*
- *Cross-AZ network latency*
- *Service-level dashboard (against the 99.9% availability target)*
- *Alarms tuned for HA scenarios (e.g. "instances in single AZ" alarm, RDS failover-detection alarm)*

| Alarm | Metric | Threshold | Triggers |
|---|---|---|---|
| *[e.g. Single-AZ EC2]* | *[Count of healthy targets per AZ]* | *[< 1 in any AZ for > 5 min]* | *[Notify; investigate AZ issue]* |
| *[…]* | | | |

### 4.11 Naming and tagging conventions

*Confirm inheritance from AT2 baseline (same tagging scheme — Project, Environment, Owner, ManagedBy, CostCentre, DataClassification). State any additions for HA (e.g. an AZ tag to identify which AZ a resource is in).*

*[Your naming/tagging section here]*

### 4.12 Backup baseline (HA enhancements)

*Document the HA-enhanced backup baseline: cross-Region RDS snapshot copies, AWS Backup with cross-Region copy, retention adjustments.*

*[Your backup section here]*

### 4.13 Recovery objectives per component — designed state *(evidences [ICTCLD502 PC 3.3])*

*Restate the recovery objectives the design achieves, per component and overall. This should now meet the §2.2 targets.*

| Component | Designed RPO | Designed RTO | Notes |
|---|---|---|---|
| RDS Multi-AZ database | *[e.g. ~0 — synchronous replication]* | *[≤ 2 min — automatic failover]* | |
| EC2 instances (cross-AZ ASG) | *[N/A — stateless]* | *[≤ 5 min — replacement via ASG]* | |
| LMS application data on EBS | *[…]* | *[…]* | |
| LMS attachments on S3 | *[≤ 1 hr — versioning + cross-Region]* | *[N/A — region-local restore is instant]* | |
| Overall LMS service | *[≤ 1 hr]* | *[≤ 4 hr]* | **Meets target** |

### 4.14 Components requiring vertical scaling — designed state *(evidences [ICTCLD502 PC 3.4])*

*Restate which components still require vertical scaling (after HA design) and the availability impact. For Multi-AZ RDS specifically, the modify-and-apply still requires a brief failover, but the impact is much smaller than Single-AZ.*

| Component | Vertical scale required for | Availability impact (post-HA) |
|---|---|---|
| RDS Multi-AZ (modify instance class) | *[CPU/memory growth]* | *[~30–60 sec failover blip during apply-immediately]* |
| EBS volume size | Storage growth | *[Online resize — no downtime]* |
| *[…]* | | |

### 4.15 Single points of failure removed *(evidences [ICTCLD502 PC 3.2])*

*Cross-reference §3.2 — for each SPOF identified in the AT2 baseline, state how the HA design removes it (or, if it can't be removed, why it's acceptable to retain).*

| SPOF in baseline (from §3.2) | Mitigation in HA design |
|---|---|
| *[RDS Single-AZ instance]* | *[Multi-AZ enables automatic failover; AZ outage no longer kills the DB]* |
| *[ASG min=1]* | *[min=2 across two AZs; one AZ outage leaves at least one instance running]* |
| *[…]* | *[…]* |

---

## §5 Implementation sequencing

*Plan how the HA changes will be applied to the running AT2 baseline during the maintenance window. The order matters: some changes are non-disruptive (add subnets, expand ASG), some are mildly disruptive (RDS Multi-AZ conversion, brief failover), some are sensitive to order.*

State:

- The proposed sequence of changes
- Per change: estimated duration, expected service impact, verification step before proceeding
- Rollback plan per change (if a change fails, how to revert before going further)
- The total estimated window required and the buffer for unexpected issues

*[Your implementation sequencing here]*

| # | Change | Est. duration | Expected impact | Verification | Rollback if fails |
|---|---|---|---|---|---|
| 1 | Add cross-AZ subnets | ≤ 5 min | None | Verify subnets created | Delete subnets |
| 2 | Add subnets to ALB | ≤ 5 min | None | Verify ALB has both AZs | Remove subnet from ALB |
| 3 | Expand ASG (min=2 across both AZs) | ~10 min | None | Verify second instance healthy | Reduce min back to 1 |
| 4 | Enable RDS Multi-AZ | ~15–30 min | Brief failover blip | Verify Multi-AZ status | Modify back to Single-AZ |
| *[…]* | | | | | |

---

## §6 Simulation and verification plan

*Plan the post-implementation simulations that will validate the HA design. This feeds the AT3 Part B work — execution and evidence go in the HA Deployment Report.*

### 6.1 Failure simulation plan *(planning for [ICTCLD502 PC 4.4] execution in Part B)*

*Identify at least one component whose failure you will simulate to confirm fault tolerance. State the simulation method, the expected outcome, and how you will verify the outcome.*

| # | Simulation | Method | Expected outcome | Verification |
|---|---|---|---|---|
| F1 | *[e.g. EC2 instance failure]* | *[Terminate one EC2 instance via console]* | *[ASG replaces within ~5 min; ALB removes unhealthy target; LMS remains reachable throughout]* | *[curl ALB endpoint continuously during the test; capture CloudWatch metrics + ASG activity history]* |
| F2 | *[e.g. AZ network partition]* | *[Modify SG to drop traffic from one AZ]* | *[Traffic routes via remaining AZ; LMS remains reachable]* | *[As above]* |
| *[…]* | | | | |

### 6.2 Resize simulation plan *(planning for [ICTCLD502 PC 4.5] execution in Part B)*

*Identify at least one component whose resize you will simulate to measure availability impact during scaling. State the simulation method, the expected outcome.*

| # | Simulation | Method | Expected outcome | Verification |
|---|---|---|---|---|
| R1 | *[e.g. ASG capacity increase]* | *[Manually set desired=4]* | *[ASG launches 2 more instances over ~5 min; all healthy in ALB; no LMS downtime]* | *[curl ALB endpoint continuously]* |
| R2 | *[e.g. RDS instance class change]* | *[Modify db.m6i.large → db.m6i.xlarge with "apply immediately"]* | *[~30–60 sec failover blip; LMS reconnects on retry]* | *[curl ALB endpoint with retries; measure outage duration]* |
| *[…]* | | | | |

### 6.3 Verification criteria *(planning for [ICTCLD502 PC 4.6] documentation in Part B)*

*State the success criteria for the simulations. What evidence will demonstrate the design works as intended?*

*[Your verification criteria here]*

---

## §7 Out of scope of this design

*State what this HA design deliberately does not address. Examples:*

- *DR to a second AWS region (active-active or hot-standby cross-region) — deferred to a future phase if YAT decides multi-region resilience is required*
- *Application-layer HA — DOODLE LMS clustering, session affinity, sticky sessions — these are YAT IT concerns and out of MTS scope per the LMS Migration Role Brief*
- *Cutover from on-prem to cloud (still YAT IT's responsibility per the role brief)*
- *Performance optimisation beyond what's needed for availability*

*[Your out-of-scope statement here]*

---

## §8 References

*Cite all source documents and standards you used to inform this design.*

- `internal-lms-cloud-architecture-design-S1-CL1-AT2.md` — the AT2 baseline this design supersedes
- *[Your own AT2 Deployment Report — file reference]*
- `internal-lms-application-spec-S1-CL1-AT1.md`
- `internal-lms-cloud-migration-requirements-S1-CL1-AT1.md`
- `internal-ha-database-requirements-S1-CL1-AT3.md`
- `internal-industry-standards-reference.md` — industry standards informing the design (Well-Architected, ACSC Essential Eight, etc.)
- `internal-reference-architectures.md` — AWS reference patterns for HA
- *[Any external sources you cited — with URLs and access dates]*

---

## §9 Document control

| | |
|---|---|
| **Document version** | 1.0 — HA Design |
| **Author** | [Your name], MTS Consultant |
| **Engagement** | YAT LMS Cloud Migration — HA Hardening Phase |
| **Date submitted** | [DD/MM/YYYY] |
| **Distribution** | Sam Walker (YAT ICT Manager), Pat Lin (MTS Senior Consultant) |
| **Supersedes** | YAT LMS Cloud Architecture — Baseline Design v1.0 (AT2) |
| **Successor document** | YAT LMS HA Deployment Report (AT3 Part B) |
| **Approval status** | [Pending YAT IT Manager review / Approved / Rejected with comments] |
