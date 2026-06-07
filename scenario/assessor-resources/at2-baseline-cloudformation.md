# AT2 Baseline Environment — CloudFormation Template (placeholder)

**Artefact type:** Assessor-supplied operational resource (AT3 setup)
**Audience:** Assessor only — distributed to students at the start of the AT3 assessment day for them to deploy
**Status:** ✅ **AUTHORED — superseded by the lab pack.** The runnable template now lives at
`S1-CL1-Cloud-Design-Build/assessments/AT3/lab-pack/baseline.yaml` (lint-clean, structural tests
pass, README with deploy/verify/teardown + a local validation harness). It is the reference
implementation of the course-wide lab-pack standard. ⚠️ Live-lab deploy still to be proven once.
This spec is retained below as the authoring source; the deviations made to get it deploying
(ALB/RDS each need ≥2 AZs; HTTP not HTTPS; flow logs deferred; AMI via SSM; instance classes
parameterised) are documented in the lab pack's README.

---

> **⚠️ AUTHORING NOTE — this file is a placeholder, not the deployable template.**
>
> ## What this template needs to do
>
> Deploy a complete instance of the **AT2 baseline AWS environment** into a student's AWS Academy lab, so that AT3 begins from a consistent, known starting state regardless of what the student built in AT2.
>
> The template instantiates the architecture specified in `internal-lms-cloud-architecture-design-S1-CL1-AT2.md` (the AT2 supplied design) — single-AZ, non-HA, ready for HA hardening. Specifically:
>
> - **VPC** — `10.0.0.0/16` in `ap-southeast-2`, with DNS hostnames and DNS resolution enabled, plus VPC flow logs to CloudWatch
> - **Subnets** — `public-web-a` (`10.0.1.0/24`), `private-app-a` (`10.0.11.0/24`), `private-data-a` (`10.0.21.0/24`), all in `ap-southeast-2a`
> - **Gateways and routing** — Internet Gateway attached to VPC; NAT Gateway in `public-web-a`; appropriate route tables associated with each subnet
> - **Security groups** — `sg-alb` (HTTPS:443 inbound from internet), `sg-app` (HTTP/HTTPS from `sg-alb`, RDP from a bastion CIDR, outbound to `sg-db` and NAT), `sg-db` (MySQL:3306 from `sg-app` only)
> - **EC2 launch template + Auto Scaling Group** — single instance type from the general-purpose family, Windows Server 2016 AMI, EC2 instance profile using the Academy `LabRole`, in `private-app-a` only, ASG with min=1/desired=1/max=2, target-tracking CPU scaling policy. User-data installs IIS and writes a placeholder HTML page ("Infrastructure ready — awaiting application deployment") so the AT2 infrastructure smoke test still passes on a fresh deployment.
> - **Application Load Balancer** — internet-facing, in `public-web-a`, listener HTTPS:443 (or HTTP:80 with ACM cert deferred), target group pointing at the ASG, health check against the placeholder endpoint
> - **RDS MySQL** — `db.m6i.large` (or general-purpose equivalent), Single-AZ, encryption at rest enabled (AWS-managed key), 7-day automated backup retention, in `private-data-a`, no public accessibility. Empty MySQL schema (no DOODLE data — that's out of MTS scope per the scope statement).
> - **S3 buckets** — `yat-lms-attachments-<env>-<region>` and `yat-lms-backups-<env>-<region>`, block-public-access enabled, SSE-S3 encryption, versioning enabled
> - **CloudWatch alarms** — baseline alarms per the supplied design §10.2: EC2 CPU high, RDS CPU high, RDS free storage low, ALB 5XX rate, RDS connections high
> - **Naming and tagging** — all resources tagged per `internal-lms-cloud-architecture-design-S1-CL1-AT2.md` §11 conventions
>
> ## Operational usage (what the assessor distributes / what students do)
>
> 1. **Morning of the AT3 assessment day:** assessor distributes the `.yaml` template file (via the YAT intranet's `Assessor Resources` section, or shared during the lab session)
> 2. **Student deploys it** via AWS Academy → AWS Console → CloudFormation → Create stack → Upload template file. The student names the stack (e.g. `yat-lms-baseline-<student-id>`), provides any required parameters (e.g. SSH key pair name, AMI ID for the region if not hardcoded), and launches.
> 3. **Deployment takes ~10–15 minutes.** RDS provisioning is the long pole; ALB target health check needs a few minutes after EC2 boots to go green.
> 4. **Student verifies the baseline is healthy** before the afternoon assessment session begins — `curl` the ALB DNS name should return the placeholder page; `aws rds describe-db-instances` should show `available`.
> 5. **Afternoon session — AT3 maintenance window opens.** Student begins the HA hardening work against the baseline.
> 6. **End of assessment day:** student tears down the stack via `delete-stack` (or assessor sweeps remaining stacks) to free Academy credits.
>
> ## AWS Academy constraints to accommodate
>
> - **IAM creation is restricted** in Academy labs — the template must **not** attempt to create IAM users, groups, or custom managed policies. Use the pre-existing `LabRole` for the EC2 instance profile. The IAM groups specified in the AT2 supplied design (`YAT-ICT-Admins`, `MTS-Consultants`, `Application-Service`, `Read-Only-Auditors`) are conceptual scenario constructs and don't need to be created as real IAM resources.
> - **Region** — `ap-southeast-2` (Sydney). AMI IDs are region-specific; use a `Mappings` block to handle this or take the AMI ID as a `Parameter`.
> - **Cost** — ALB + NAT Gateway + RDS together run roughly USD $5–10 per assessment day; ensure tear-down at the end.
> - **Lab session lifetime** — AWS Academy labs typically auto-terminate after some hours. Confirm the session-length policy for the delivery context and ensure the morning-deploy + afternoon-assessment + tear-down fits.
>
> ## UoC mapping (context — not direct UoC evidence)
>
> The template itself is an **operational delivery artefact**, not a UoC-evidencing student-facing resource. It supports:
>
> - [ICTCLD401 AC 1] cloud vendor service provider — the lab environment
> - [ICTCLD401 AC 2] cloud managed database service — the deployed RDS instance
> - [ICTCLD502 AC 1, 2, 4, 6, 7] same lab-environment access conditions for AT3
>
> The student-facing scenario content is `internal-lms-cloud-architecture-design-S1-CL1-AT2.md` (the design the template instantiates). The CloudFormation template is the operational means of getting that design into a student's lab.
>
> ## Companion artefacts
>
> - `scenario/internal-lms-cloud-architecture-design-S1-CL1-AT2.md` — the design this template implements
> - `scenario/templates/template-deployment-report-S1-CL1-AT2.md` — references the AT2 smoke-test which the placeholder web page (deployed by user-data here) must satisfy
> - `scenario/templates/template-ha-design-S1-CL1-AT3.md` — students start from this baseline to design HA improvements
> - `scenario/templates/template-ha-deployment-report-S1-CL1-AT3.md` *(not yet authored)* — students document HA changes against this baseline
>
> ## Authoring sequence (when this is built)
>
> 1. Reference the supplied design §3–§12 as the specification
> 2. Draft the YAML in sections, top-down: VPC → subnets → gateways → SGs → compute (LT + ASG + ALB) → DB → storage → monitoring
> 3. Add `Parameters` block for student-id / region-AMI / key-pair
> 4. Add `Outputs` block exposing ALB DNS name, RDS endpoint, S3 bucket names — students will reference these
> 5. Test-deploy in a clean Academy lab to confirm end-to-end provisioning works
> 6. Verify the placeholder web page is reachable via the ALB DNS name after deployment
> 7. Verify tear-down (`delete-stack`) cleanly removes all resources

---

*This placeholder will be replaced with the actual CloudFormation template (renamed to `.yaml`) when it is authored as part of the AT3 delivery preparation work.*
