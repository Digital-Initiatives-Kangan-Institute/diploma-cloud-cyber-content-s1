# Claude notes — AT3 baseline lab pack

Pack-specific notes only. The **generic pattern, AWS Academy constraints, validation harness
and hard-won lessons** live in the canonical standard — `documentaion/lab-pack-standard.md`
(this pack was its reference / live-proving implementation, so those findings are recorded
there). Below is only what's specific to THIS baseline.

## What this baseline is

The post-AT2 **single-AZ, non-HA** YAT LMS environment a student deploys at the start of AT3
and then hardens to multi-AZ HA. It mirrors the AT2 supplied design end-state (ASG min 1 /
desired 1 / max 2 single-AZ; ALB; Single-AZ RDS; S3; baseline alarms). Design split is **A**
(ASG built in AT2 per ICTCLD401 Element 3; AT3 hardens to multi-AZ per ICTCLD502) — confirmed,
not changing.

## Deviations from the original placeholder spec (`scenario/assessor-resources/at2-baseline-cloudformation.md`)

The paper spec couldn't anticipate deploy realities:
1. **2nd public + 2nd data subnet added** — an internet-facing ALB and an RDS subnet group each
   need ≥2 AZs; a literal single-subnet baseline won't deploy. The **compute (ASG) stays
   single-AZ**, so it's still genuinely non-HA (that's what AT3 hardens).
2. **Instance profile optional / none** — the baseline EC2 (serving a placeholder page) needs no
   instance role, so it's an optional parameter (default blank). The Learner Lab does provide
   `LabRole` if a later step ever needs one.
3. **HTTP:80, not HTTPS** — ACM needs a domain; deferred.
4. **VPC flow logs dropped** — CloudWatch flow logs need an IAM role (forbidden); could go to S3.
5. **AMI via SSM parameter; instance/DB classes parameterised** (`t3.medium` / `db.t3.medium`).

## Status & parked (for the AT3 revisit)

- **Required lab = AWS Academy Learner Lab, `us-east-1`** (course-wide single product; see the
  region-substitution standard). Design region is Sydney (`ap-southeast-2`); deploy is `us-east-1`.
- ✅ **Deploy + Multi-AZ proven live in the Learner Lab `us-east-1` (2026-06-26).** Baseline and the
  AT3 hardened end-state (RDS `MultiAZ: true`, `db.t3.medium`, standby in a 2nd AZ; cross-AZ ASG) both
  reach CREATE_COMPLETE, no AZ/capacity refusal. Proven with a throwaway probe (baseline + both
  multi-AZ flips). *(Originally proven in the Cloud Architecting Sandbox — baseline 2026-06-07 `eae2e18`,
  Multi-AZ 2026-06-15 — before the single-product move; this corrected an earlier wrong "Multi-AZ not
  supported" note, do not reinstate it.)*
- ⚠️ **Open — placeholder health-check loop.** In the Learner Lab the Windows placeholder instances
  churn on an ELB health-check replace loop (~6 min) — a UserData/bootstrap issue, not multi-AZ; fix
  before any live "lose an AZ, stay up" failover demo. (Recorded in `docs/lab-pack-standard.md`.)
- **Parked — EC2 instance role:** the AT2 design gives the instance an "Application-Service" role
  (RDS/S3/CloudWatch access); this baseline runs with none. The Learner Lab provides `LabRole` if a
  later step needs one; keep it a clean optional parameter (off by default).
