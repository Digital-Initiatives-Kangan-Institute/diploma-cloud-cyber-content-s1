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

3. **SQL Server edition is a parameter; default `sqlserver-ex` (Express, free).** SE (Standard,
   license-included) is **not deployable in the sandbox** — `db.t3.medium` + `sqlserver-se` is rejected and the
   sandbox caps RDS at `db.t3.medium` (SE needs a larger class; proven live 2026-06-21), so both templates
   default to Express. The DB is empty and is never made Multi-AZ, so the edition does not change what AT3
   assesses (the no-Multi-AZ decision is an *application* constraint, not an edition one). **Decision
   (2026-06-21): the in-world scenario stays on Standard; the lab deploys Express as a documented stand-in** —
   the lab DB is empty, so Express's limits (10 GB/db, RAM/cores) never bite; same "the lab simulates X"
   pattern as region simulation. The README discloses the substitution to students. No scenario rewrite (a
   real engine change is huge — see the parked note below).

4. **Cross-Region DR backup copy is a documented CLI step, not in the template.** RDS automated-backup
   replication to a second Region (Melbourne, `ap-southeast-4`, to keep financial data in Australia) is set
   via `aws rds start-db-instance-automated-backups-replication`, not a CloudFormation property. The exemplar
   design names it; the lab treats it as an out-of-band step. Do not expect it in `improved.yaml`.

5. **2-AZ network, single-AZ compute baseline.** An internal ALB needs >= 2 subnets in 2 AZs and an RDS
   subnet group needs >= 2 AZs, so a 2nd app subnet and 2nd data subnet are present in the baseline; the
   ASG is kept single-AZ (one subnet) so the baseline is genuinely non-HA at the compute tier. `improved.yaml`
   adds the 2nd app-subnet route-table association and spreads the ASG across both app subnets.

## Proving run — PROVEN live 2026-06-21 (Cloud Architecting Sandbox)

What was confirmed:
- **Express baseline deploys clean** — `CREATE_COMPLETE` in **both `us-east-1` and `ap-southeast-2` (Sydney)**,
  `sqlserver-ex` on `db.t3.medium`.
- **Apply-as-update works with the DB untouched** — `UPDATE_COMPLETE`; the change-set modified only the ASG and
  the attachments bucket (lifecycle) and added the 2nd app-subnet route association — **no `Database` change**
  (see the `rds:ModifyDBInstance` finding below).
- **App-tier Multi-AZ** — ASG settled at `Desired=2`, two instances across two AZs; the DB stayed single-AZ /
  Multi-AZ No.
- **India residency slice** — `CREATE_COMPLETE` in **`ap-south-1` (Mumbai)**, both buckets; the cross-region
  split (main region + a separate Mumbai stack) works.

NOT run — config validated but no explicit live demo: the **failover** (terminate-an-instance) and **scale-out**
demos, and a **PITR restore**. Standard ASG behaviour and the scaling policy is in place; PITR/restore perms are
**unverified** (see the finding) and worth a future check.

Findings (also recorded in `docs/lab-pack-standard.md`):
- **SQL Server SE is NOT deployable in the sandbox.** `db.t3.medium` + `sqlserver-se` + `license-included` is
  rejected ("RDS does not support creating a DB instance with the following combination...") — SE needs a larger
  class than the sandbox permits. **Both templates default to `sqlserver-ex` (Express)**, which deploys fine.
- **The lab role denies `rds:ModifyDBInstance`.** The `voclabs` role can **create** an RDS instance (the
  baseline built) but **cannot modify** an existing one — the original `improved.yaml` raised
  `BackupRetentionPeriod` 7->14 and hit `AccessDenied`. So the change-set must leave the DB **untouched** (it
  now does). This blocks **any** in-lab DB modification (CFN *or* console), so the DB-tier DR improvements
  (wider retention, cross-Region copy) are **design-level only, not lab-executable**; DB reliability is shown
  via the baseline's automated backups + PITR (restore perms unverified).
- **DECIDED (2026-06-21): keep the scenario on SQL Server Standard; Express is a lab-only stand-in.** A real
  engine change (e.g. PostgreSQL) was scoped and rejected — it spans ~30+ files across the active CL3 **and the
  completed CL1/CL2 clusters**, and worse, it **deletes the commercial-licensing cost-benefit element** (the
  ~$27k/yr Ledgerline+SQL-Server licensing, license-included-vs-BYOL) that is the assessed differentiator from
  the open-source LMS. So the scenario is unchanged; the lab substitutes Express and the README says so. The
  only residual tidy: the soft `~13.5 vs ~22 GB` SQL-data figure (low priority). Tracked in MEMORY
  `[[s1cl3-assessment]]`.
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
