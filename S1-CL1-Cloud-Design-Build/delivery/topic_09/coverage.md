# Topic 9 — Operability & justification · Coverage

**Topic 9 of 14** · **AT2 content Topic** (cloud build — operability + decision justification) · teaching source: **mixed** — AWS (ACF M10, ACA M10 monitoring section) for CloudWatch / alarms / logging; **bespoke** for the validation discipline and — the largest part — **justifying the configuration decisions against the workload** (AWS decks teach the services, not how to justify a build to a VET standard).

The coverage spec — what this Topic must cover, in UoC and AT2 terms. `slide_plan.md` and the deck are built to satisfy it.

> **From "built" to "defensible".** Topics 6–8 built the workload (foundation → network → workload tier). Topic 9 makes it **operable and defensible**: monitor it (CloudWatch baseline), confirm it works (validation), and **justify the open configuration decisions (C1–C8) against the Ledgerline workload** — the judgement the Deployment Report is marked on. Topic 10 then *writes* the report from the evidence. AT2 = ICTCLD401 (primary) + ICTCLD502 (partial).

---

## Teaching-design note — primer-first (no assumed baseline)

Per the standing rule, each technical concept gets a vendor-neutral **primer** before the AWS-context slide: what **monitoring / a metric / an alarm / a log** is; what **validation** means (does it meet the requirement?); what it means to **justify** a decision (trade-off against the workload's needs + cost). Reuse-first still governs: pin an AWS slide where it teaches the fundamental (ACA M10 monitoring section); bespoke for the justification + validation discipline AWS doesn't cover. Per-concept: **primer → AWS-context teach → (recorded) demo → practice**, except the analytical justification work, which is **teach → practice** (no AWS demo exists for "justify your decision").

---

## What this Topic must cover

Operability and justification of the workload built in Topics 6–8, to the supplied design, evidenced for the report. Three components:

- **C1 — Monitoring & logging (CloudWatch baseline).** What monitoring / metrics / alarms / logs are (primer) → Amazon CloudWatch (metrics, alarms, dashboards, Logs) → stand up the design's baseline alarms + logging. *(ICTCLD401 KE — performance monitoring and alarms.)*
- **C2 — Validation (does it meet the design?).** What validation is (primer) → testing tools + method → consolidate the tests from Topics 7–8 (connectivity PC 2.6; scaling PC 3.2) into a **validation against the design + recovery objectives** (RPO ≤ 1 h, RTO ≤ 1 business day), and confirm/fix. *(ICTCLD401 PC 2.6 · PC 3.2 — developed earlier, validated here.)*
- **C3 — Justifying the configuration decisions (C1–C8).** What "justify" means (primer) → method: each open decision weighed against the **Ledgerline workload** (performance, cost, security, residency) → produce a defensible justification for each of the design's C1–C8 implementer decisions. **Bespoke; the core AT2 judgement.** *(ICTCLD401 PC 1.3 · PC 1.8 + the options/cost-model KE.)*

---

## 1. UoC mapping

UoC **taught / developed** in this Topic:

| UoC item | Descriptor | Component |
|---|---|---|
| [ICTCLD401 KE 5] | Performance monitoring and alarms | C1 |
| [ICTCLD401 PC 2.6] | Test external/internal access and fix errors (validated against the design) | C2 *(developed T7–T8)* |
| [ICTCLD401 PC 3.2] | Test automatic scaling and fix errors (validated) | C2 *(developed T8)* |
| [ICTCLD401 PC 1.3] | Select best cloud computing solution and service according to business requirements | C3 |
| [ICTCLD401 PC 1.8] | Define workload according to business requirements and needs | C3 *(the workload the decisions are justified against)* |
| [ICTCLD401 KE 6] | Functions/features/uses of compute, storage, scaling, database **options** (the basis for choosing) | C3 |
| [ICTCLD401 KE 4] | Cost models and cloud economics (the cost basis of a decision, e.g. SQL licence-included vs BYOL) | C3 |
| `[ICTCLD502]` | Monitor/measure resources (baseline) — *partial; full availability monitoring is AT3* | C1 *(confirm)* |

> **AT2 marking home: A4 (justification of configuration decisions) + the monitoring/validation portion of the build narrative** *(confirm criterion letters against the AT2 assessor doc)*. Deployment Report sections **§4.10 Monitoring · §4.13 Recovery objectives · §4.16 Configuration decisions (C1–C8, justified)**. AT2 build-topic refs **T10 (CloudWatch) · T13 (config-decision justification) · T14 (testing/validation)**.

UoC **applied** here but **taught earlier**:

| What | Where |
|---|---|
| The resources being monitored/validated (EC2, ALB, ASG, RDS, S3) | Topics 7–8 (built there) |
| Connectivity + scaling tests | Topics 7–8 (run there; consolidated into validation here) |
| Cost models / pricing (the cost side of a justification) | Topic 1 / AT1 (applied here to the build decisions) |

---

## 2. AT2 equivalence / alignment

| AT2 element | Criterion | How Topic 9 aligns |
|---|---|---|
| **§4.10 Monitoring (baseline)** | A-build | C1 — the design's CloudWatch metrics + baseline alarms + logging, evidenced. |
| **§4.13 Recovery objectives (baseline state)** | A-build | C2 — validate the build meets RPO ≤ 1 h / RTO ≤ 1 business day; name the single-AZ SPOF (deferred to AT3). |
| **§4.16 Configuration decisions C1–C8** | **A4 (justification)** | C3 — each decision made + **justified against the Ledgerline workload**, the marked judgement. |
| **Validation; fix errors** | A-build · A10 | C2 — connectivity + scaling tests consolidated into a validation; results evidenced. |

**Practice-activity alignment:** students stand up the **baseline monitoring** for the **practice** engagement (Accounting / Ledgerline), **validate** the build against the design, and **write a justified rationale for each C1–C8 decision** against the Ledgerline workload — mirroring the AT2 operability + justification on the LMS.

**The design's relevant sections:** §4.10 baseline alarms (EC2/RDS CPU ≥ 80%/10 min; RDS free storage < 15%; ALB 5XX / unhealthy host; RDS connections > 80%) + logging (flow logs/RDS → CloudWatch Logs; ALB → S3; EC2 agent; 7-yr retention). §4.13 RPO ≤ 1 h, RTO ≤ 1 business day, single-AZ SPOF. §4.16 the eight implementer decisions (EC2 type, RDS class, SQL licence model, EBS sizing, ASG params, backup/RPO, DNS/ACM, bastion/RDP) — each justified against the Ledgerline workload (15–25 typical / 45–55 month-end peak; read-heavy at month-end; financial residency + 7-yr retention).

---

## Out of scope for this Topic (covered elsewhere)

- **Writing the Deployment Report** (assembling the narrative + appendices) → **Topic 10**. Topic 9 produces the *monitoring*, the *validation result*, and the *decision justifications*; Topic 10 writes them up.
- **HA-tuned alarms, availability monitoring, failure simulation, cross-Region backup** → **AT3** (the design's §4.10 says HA-tuned alarms come in the HA design; §4.13 names the SPOF as the AT3 objective).
- **Building the resources** (EC2/ALB/ASG/RDS/S3) → **Topics 7–8** (monitored/validated here, not re-built).
- **The cost model itself** (how to build a CBA) → **AT1 / Topic 3** (applied here as the cost basis of a justification).

---

## Coverage checklist (for `slide_plan.md` + the deck to satisfy)

- [ ] Each of C1–C3 is covered; C1 has primer → AWS teach → (recorded if one fits) demo → practice; C3 is **teach → practice** (analytical — no AWS demo for "justify").
- [ ] **CloudWatch** taught (metrics, alarms, dashboards, Logs) from the AWS source; the design's **baseline alarm table** + **logging** are built/configured (C1).
- [ ] **Validation** consolidates the Topic 7–8 tests (connectivity, scaling) into a check **against the design + recovery objectives**; the single-AZ SPOF is named (C2).
- [ ] **C3 is the centrepiece:** a clear **method for justifying a decision against the workload** (performance / cost / security / residency), then students justify each of the design's **C1–C8** decisions — defensibly, in-world, on the practice scenario.
- [ ] Cost reasoning (e.g. SQL Server licence-included vs BYOL) is shown as part of a justification (C3), reusing the AT1 cost-model thinking.
- [ ] Depth ceiling respected: **baseline** operability — baseline alarms, baseline recovery objectives; HA-tuned monitoring + availability + failure-sim are **AT3**.
- [ ] Student-facing slides stay in-world (AWS source refs may remain visible per the 2026-06-03 exception); no tipping which system is assessed.
- [ ] AT2 alignment (§2) explicit enough that a student leaving this Topic could monitor + validate the build and justify every open decision.
