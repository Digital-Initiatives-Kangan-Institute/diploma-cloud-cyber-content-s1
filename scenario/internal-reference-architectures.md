# Reference Architectures

**Relevant to:** All clusters

**UoC references this document satisfies:**
- [ICTCLD401 KE 3] principles and functions of cloud computing solutions and technologies, including IaaS / PaaS / SaaS
- [ICTCLD401 KE 11] functions, uses and differences of cloud models, including on-premise and private cloud / hybrid cloud / public cloud

**Source status:** ✅ Authored 2026-05-23 (Claude). Pointers to architectural patterns and reference materials students should consult when designing and building the YAT cloud environment. Mostly a reading list rather than original content.

---

## How to use this list

Students working on AT2 (cloud foundation build) and AT3 (HA design and implementation) should consult these references when:

- Choosing between cloud service options (e.g. should the LMS workload run on EC2, on ECS, on Elastic Beanstalk?)
- Designing for the AWS Well-Architected pillars
- Justifying architecture decisions in their action plan and design documents
- Looking for canonical patterns that map onto the YAT scenario

## Cloud service model definitions

- **NIST SP 800-145** — the canonical definitions of IaaS, PaaS, SaaS, public/private/hybrid/community cloud. See `internal-industry-standards-reference.md` for the full citation.
- **AWS service-model mapping** — for each AWS service the student uses, identify the service-model layer: e.g. EC2 (IaaS), RDS (managed PaaS for databases), S3 (storage service), AWS Lambda (FaaS / PaaS).

## AWS Well-Architected Framework

The Well-Architected Framework is the primary reference for design decisions on AWS. Six pillars:

- **Operational Excellence** — running and monitoring systems, continuously improving processes
- **Security** — protecting information, systems, and assets
- **Reliability** — recovering from failures, dynamically acquiring computing resources to meet demand
- **Performance Efficiency** — using computing resources efficiently
- **Cost Optimisation** — avoiding unnecessary cost
- **Sustainability** — minimising environmental impact

Each pillar has a whitepaper and a set of design principles. Students should be able to identify, for any architecture decision they make on YAT, which pillar(s) the decision serves and which trade-offs it imposes.

## AWS reference architectures relevant to the YAT cluster

- **Highly available multi-tier web application** — the canonical pattern for an application like the YAT LMS post-migration: VPC with subnets in two or more availability zones, web tier behind an Application Load Balancer with an Auto Scaling Group, database tier on RDS Multi-AZ. Referenced directly in the AWS Academy Cloud Architecting module 10 lab (see `assessment_plan.md` §4 AT3 sources).
- **AWS hybrid cloud / migration patterns** — relevant during the transition phase. Patterns include "lift-and-shift" (rehost), "re-platform", "refactor" (the AWS "6 Rs" of migration: rehost, replatform, repurchase, refactor, retire, retain). The YAT migration is principally **rehost / replatform**: same OS and application stack, new cloud-hosted infrastructure.
- **AWS multi-AZ RDS for MySQL** — the canonical pattern for the YAT HA database requirements (`internal-ha-database-requirements-S1-CL1-AT3.md`).
- **AWS IAM patterns** — least-privilege groups and policies, identity federation, role-based access. Relevant to AT2 IAM design and the Security Responsibilities Matrix sub-deliverable in AT3 closure.

## AWS Cloud Adoption Framework (CAF)

For the AT1 strategic-alignment work, the AWS CAF provides a structure for thinking about cloud adoption beyond pure technology. Six perspectives:

- **Business** (the business case for cloud)
- **People** (capability and skills)
- **Governance** (policy, controls, risk management)
- **Platform** (the technical platform itself)
- **Security** (cloud-specific security)
- **Operations** (running cloud workloads)

The YAT migration touches all six — particularly "People" given the case study's explicit note that YAT ICT staff lack cloud experience.

## Migration approaches

- **AWS Migration Strategy "6 Rs"** — Rehost, Replatform, Repurchase, Refactor, Retire, Retain. For YAT's LMS: principally rehost (same OS + application stack) with elements of replatform (managed database for the HA tier).
- **AWS Migration Hub** — service for tracking migrations across multiple workloads (less relevant for YAT's single-LMS scope but worth knowing).

## Operational patterns

- **CloudWatch monitoring patterns** — metric, log, alarm, dashboard. Referenced in AT3 monitoring work.
- **AWS Backup** — managed backup for RDS, EBS, and other AWS resources. Relevant to the cloud-side equivalent of YAT's current on-prem backup process.
- **AWS Trusted Advisor** — automated best-practice checks across cost, performance, security, fault tolerance, and service limits.

## 12-Factor App methodology

Not strictly an "AWS" reference, but a widely-used framework for designing cloud-native applications. The DOODLE LMS as it exists today does not follow 12-Factor (it's a traditional server-installed application). Students may discuss this as a future-state consideration rather than a current-state requirement — the migration brief explicitly preserves the existing application stack.

## Notes on use in the cluster ATs

- In AT1, reference Well-Architected and the CAF when justifying the strategic direction of the migration.
- In AT2, reference the multi-tier web application pattern and IAM patterns when implementing the foundation build.
- In AT3, reference the multi-AZ RDS pattern, the highly-available web application pattern, and CloudWatch monitoring patterns.
- Cite by name in your design documents. Students should not paraphrase an entire whitepaper into their submission — link or cite, and apply the pattern to the YAT scenario.
