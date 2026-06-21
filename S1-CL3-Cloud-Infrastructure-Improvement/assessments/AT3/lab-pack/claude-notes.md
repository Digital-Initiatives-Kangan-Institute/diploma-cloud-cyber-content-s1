# Claude notes — CL3 AT3 lab pack (Ledgerline)

Pack-specific notes only. The generic pattern, AWS Academy constraints, validation harness and
hard-won lessons live in the canonical standard — `docs/lab-pack-standard.md` (umbrella). Below is
only what is specific to THIS pack. See also `assessments/assessment_plan.md` §6.8.

## What this pack is

The AT3 environment for **Ledgerline** (the YAT Accounting System). AT3 follows an **apply-as-update**
model:

- **`baseline.yaml`** — the existing single-AZ state the student deploys first.
- **`improved.yaml`** — the **approved improvement** applied as a CloudFormation **change-set / stack
  update** to the *same* stack (same logical IDs, so every change is in-place/additive — no replacement).
  Doubles as the AT2 model answer and the AT3 assessor reference/fallback if a team's AT2 write is unusable.
- **`india-residency.yaml`** — the light IR-3 residency slice, a **separate** stack in `ap-south-1`
  (Mumbai), because one CloudFormation stack is region-bound.

## Design decisions specific to this pack

1. **The database is single-AZ in BOTH templates — on purpose.** Ledgerline does not support a Multi-AZ
   (mirrored) database (it is a legacy app, vendor-certified single-instance only — see the scenario's
   *Cloud Migration Technical Finding*). So the improvement makes the **application tier** Multi-AZ (ASG
   across two AZs) but the **RDS instance stays single-AZ**. DB reliability is recovery-based: wider
   backup retention + point-in-time restore + a cross-Region DR copy. The pytest enforces `MultiAZ: false`
   in both templates — this is the central invariant of the whole CL3 design, do not "fix" it to Multi-AZ.

2. **Internal ALB (faithful) → console-based verification.** Unlike CL1 AT3 (internet-facing ALB you could
   curl), Ledgerline is internal-only (VPN), so the ALB is `Scheme: internal` and is **not browser-reachable
   in the lab** (no VPN). Verification is via the console: stack status, Target Group health, RDS status,
   ASG instance AZs. The README says so explicitly. This is a deliberate divergence from the CL1 pattern,
   driven by the scenario.

3. **SQL Server edition is a parameter; default `sqlserver-se` (Standard, license-included).** The scenario
   establishes Standard edition. The edition does **not** gate anything in this lab — the DB is empty and is
   never made Multi-AZ — so if SE `license-included` proves infeasible or too credit-hungry in the sandbox,
   flip `DBEngine` to `sqlserver-ex` (Express, free). The no-Multi-AZ decision is an *application* constraint,
   not an edition one, so the substitution does not change what AT3 assesses. **Confirm SE feasibility in the
   proving run** (the one real unknown — see below).

4. **Cross-Region DR backup copy is a documented CLI step, not in the template.** RDS automated-backup
   replication to a second Region (Melbourne, `ap-southeast-4`, to keep financial data in Australia) is set
   via `aws rds start-db-instance-automated-backups-replication`, not a CloudFormation property. The exemplar
   design names it; the lab treats it as an out-of-band step. Do not expect it in `improved.yaml`.

5. **2-AZ network, single-AZ compute baseline.** An internal ALB needs >= 2 subnets in 2 AZs and an RDS
   subnet group needs >= 2 AZs, so a 2nd app subnet and 2nd data subnet are present in the baseline; the
   ASG is kept single-AZ (one subnet) so the baseline is genuinely non-HA at the compute tier. `improved.yaml`
   adds the 2nd app-subnet route-table association and spreads the ASG across both app subnets.

## Status & parked (for the proving run)

- **NOT yet proven live.** Required before AT3 is final — one Academy session (Cloud Architecting Sandbox):
  1. Deploy `baseline.yaml` in Sydney; confirm CREATE_COMPLETE, target healthy, RDS Available + Multi-AZ No.
  2. Update the stack with `improved.yaml`; confirm the change-set preview is **Modify only (no Replace)**,
     UPDATE_COMPLETE, and the ASG now runs 2 instances across 2 AZs.
  3. Demonstrate reliability: terminate an app instance and watch the ASG replace it across AZs; run an RDS
     point-in-time restore (and, if doing DR, a cross-Region restore) — these are the AT3 reliability
     demonstrations (there is no DB failover to show; that is the point).
  4. Demonstrate scalability (scale-out) and confirm the S3 lifecycle on the attachments bucket.
  5. Deploy `india-residency.yaml` in Mumbai; confirm the two buckets; tear everything down.
- **KEY UNKNOWN: SQL Server SE `license-included` on `db.t3.medium` in the Cloud Architecting Sandbox.**
  MySQL Multi-AZ was proven there (2026-06-15) but SQL Server SE has not been deployed there. If SE will not
  create (edition/class/license restriction) or burns credits too fast, set `DBEngine=sqlserver-ex` and
  re-run — record the outcome back into this file and `docs/lab-pack-standard.md`.
- Watch SQL Server RDS **create time** (typically longer than MySQL); the README budgets ~15 min.

## Local validation (done)

- **cfn-lint:** clean (exit 0) on all three templates via the `.cfnlintrc.yaml` template list (W1011 suppressed
  and justified — NoEcho DB password supplied at deploy, not Secrets Manager, to avoid IAM in the lab).
- **pytest:** 15/15. Asserts the no-DB-Multi-AZ invariant (both templates), single-AZ→2-AZ compute, SQL Server
  engine, internal ALB, encrypted+empty DB, no IAM, optional instance profile, SSM AMI, locked buckets, the
  India slice (2 buckets + >=180-day CERT-In retention), and **pure ASCII** (a non-ASCII char in an RDS
  description fails the live deploy and cfn-lint does not catch it).
- Run: `python -m venv .venv && .venv/bin/python -m pip install -r requirements.txt`, then
  `.venv/bin/cfn-lint` and `.venv/bin/python -m pytest -q`.
