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
2. **Instance profile optional / none** — the sandbox has no usable role (no `LabRole`/
   `LabInstanceProfile`); the baseline EC2 (serving a placeholder page) needs none.
3. **HTTP:80, not HTTPS** — ACM needs a domain; deferred.
4. **VPC flow logs dropped** — CloudWatch flow logs need an IAM role (forbidden); could go to S3.
5. **AMI via SSM parameter; instance/DB classes parameterised** (`t3.medium` / `db.t3.medium`).

## Status & parked (for the AT3 revisit)

- ✅ **Proven live (2026-06-07):** CREATE_COMPLETE in the Cloud Architecting Sandbox (Sydney) and
  serves the placeholder page end-to-end. Committed `eae2e18`.
- ✅ **RDS Multi-AZ — supported (proven live 2026-06-15).** The earlier "not supported / do not
  create a standby instance" reading is **wrong for the Cloud Architecting Sandbox**: the AT3
  hardened end-state (RDS `MultiAZ: true`, MySQL 8.4.8, `db.t3.medium`, standby in `ap-southeast-2a`)
  reached CREATE_COMPLETE there, alongside cross-AZ compute (2× `t3.medium` in 2a/2b, healthy).
  Proven with a throwaway probe (baseline + both multi-AZ flips). **AT3 keeps the real live Multi-AZ
  DB failover demo — no fallback needed.** Required lab for AT3 = the Cloud Architecting Sandbox.
- **Parked — EC2 instance role:** the AT2 design gives the instance an "Application-Service" role
  (RDS/S3/CloudWatch access); this baseline runs with none. Decide whether to re-add it as a
  clean optional parameter (on if a lab supplies a usable role, off otherwise).
