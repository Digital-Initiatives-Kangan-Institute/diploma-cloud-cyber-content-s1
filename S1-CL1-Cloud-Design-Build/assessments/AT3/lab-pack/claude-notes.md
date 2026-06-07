# Claude notes — AT3 baseline lab pack

My working notes. **Not student-facing** (the README is). This is where the pattern framing,
the AWS Academy discoveries, the local validation harness, and the deviations live.

> **Reference implementation of the course-wide "lab-pack" pattern** ([[lab-pack-standard]]).
> This is the FIRST pack proven against a live AWS Academy session — findings here feed back
> into the standard before the pattern is reused. CL2's `AT2/lab-pack/` predates it and is a
> back-port target.

---

## Live proving run — findings (2026-06-07, AWS Academy Cloud Architecting Sandbox)

**Where the sandbox is:** AWS Academy (Canvas) → **AWS Academy Cloud Architecting** course →
**Modules** → **Sandbox** section → **Sandbox environment** (a Vocareum "Elite" lab). This is
NOT the "Learner Lab" product the earlier memory assumed — it's the Architecting course's own
sandbox, and its allow-list differs.

**Sandbox allow-list (the relevant bits):** CloudFormation, CloudFront, CloudShell, CloudWatch,
DynamoDB, **EC2** (t2/t3 nano–medium; Amazon Linux + Windows AMIs; ≤9 instances; gp2 ≤35 GB),
**EC2 Auto Scaling**, **ELB**, **IAM (read-only)**, KMS (list), Lambda, **RDS** (db.t3.micro–
db.t3.medium; MySQL/Postgres/MariaDB/Aurora; gp2 ≤100 GB), Route53 (no domain reg), S3, SNS, SSM.

**What the proving run resolved (all previously [VERIFY]):**
- ✅ **Sydney `ap-southeast-2` deploys for real** — the sandbox is NOT region-locked to
  us-east-1. The console default is us-east-1, but switching to Sydney and deploying works.
  So the YAT scenario uses **real Sydney**, no simulation. (Mumbai `ap-south-1` likely also
  works for the CL2 audit-log — not yet deploy-tested, but the region selector offered it.)
- ✅ **NAT Gateway, Elastic IP, and ALB all deploy** in the sandbox (earlier watch-items).
- ✅ **`t3.medium` / `db.t3.medium` are allowed** (the nano/micro/small cap was Cloud9-only).
- 🔴 **Multi-AZ RDS is NOT supported** ("do not create a standby instance"). This is ONLY RDS —
  multi-AZ **compute** (ASG across AZs + ALB) is unrestricted. Impact: AT3's RDS-failover demo
  can't run here. Workaround under consideration: students **design** RDS Multi-AZ (knowledge/
  design evidence) but **demonstrate** Multi-AZ on the compute tier. TODO: check ICTCLD502's
  PE/PC wording — does it name RDS, or just "high availability"? If the latter, the compute-only
  demo satisfies it. (Parked with Tim 2026-06-07.)
- 🔴 **No `LabRole` / `LabInstanceProfile`** — `aws iam list-instance-profiles` returned only
  `EMR_EC2_DefaultRole` and `myS3Role` (leftovers from specific labs). **Instance-profile names
  vary by lab product and may not exist.** → made the instance profile **optional** in the
  template (default blank = none; baseline instances need no IAM).

**Two template bugs the live deploy caught that `cfn-lint` did NOT:**
1. **Em-dash (`—`, U+2014) in `DBSubnetGroupDescription`** → RDS rejects it: *"must not contain
   non-printable control characters."* cfn-lint only enforces the printable-char regex on
   **security-group** descriptions, not RDS ones. → **Rule: keep templates pure ASCII.** Fixed
   by replacing all em-dashes with hyphens; the Python non-ASCII scan in the harness guards it.
2. **`InstanceProfileName=LabInstanceProfile` invalid** → "Invalid IAM Instance Profile name."
   Fixed by making it optional (see above).

Both were found with **"Preserve successfully provisioned resources"** on stack-failure — worth
using on a proving run so the partial state is inspectable rather than rolled back.

---

## Local validation harness (assessor/Claude — NOT student)

Students never run this; they just deploy `baseline.yaml`. This is how I keep the template
honest before it reaches a lab.

```bash
cd lab-pack
python -m venv .venv
.venv/Scripts/python -m pip install -r requirements.txt   # cfn-lint, pytest (NO moto — MAX_PATH)
.venv/Scripts/cfn-lint baseline.yaml                      # lint clean (exit 0)
.venv/Scripts/python -m pytest -q                         # 8 structural checks
```

- `tests/test_baseline.py` asserts the non-HA invariants (Single-AZ RDS, single-subnet ASG),
  the Academy constraints (no IAM resources, optional instance profile, SSM AMI, locked-down
  buckets), and the expected Outputs.
- `.cfnlintrc.yaml` documents the one suppression (`W1011`, the NoEcho DB password).
- ⚠️ cfn-lint does NOT catch the em-dash-in-RDS-description bug — the harness has a Python
  non-ASCII scan for that (run it after edits; see the proving-run notes).

---

## Deviations from the original placeholder spec (`scenario/assessor-resources/at2-baseline-cloudformation.md`)

The paper spec couldn't anticipate deploy realities:
1. **2nd public subnet + 2nd data subnet added** — an internet-facing ALB and an RDS subnet
   group each need ≥2 AZs; a literal single-subnet baseline won't deploy. Compute (ASG) stays
   single-AZ, so it's still genuinely non-HA.
2. **HTTP:80, not HTTPS** — ACM needs a domain; deferred.
3. **VPC flow logs dropped** — CloudWatch flow logs need an IAM role (Academy forbids); could go
   to S3 instead, but no HA-hardening value. Deferred.
4. **AMI via SSM public parameter** — no hardcoded AMI to age.
5. **Instance/DB classes are parameters** — defaults `t3.medium` / `db.t3.medium`.
6. **Instance profile optional** — names vary by lab; baseline needs none.

---

## Status & next
- Baseline: lint clean, 8 structural tests pass, **live-deployed in the Sydney sandbox** (proving
  run in progress 2026-06-07 — first attempt found the two bugs above; redeploy after fixes).
- Feed the findings above into [[lab-pack-standard]] once the clean deploy is confirmed.
- Open: the ICTCLD502 RDS-Multi-AZ-wording check; back-port CL2 AT2 lab-pack to the standard.
