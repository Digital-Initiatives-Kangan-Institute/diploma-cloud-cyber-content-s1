# Topic 4 — DR: strategy & plan · Coverage

**Topic 4 of 10** · **AT1 content Topic** (Part B, DR strand — finalisation half) · teaching source: AWS DR strategies (backup-restore / pilot-light / warm-standby / active-active) + bespoke · *deck pinning TBD (Step 3)*.

This file is the **coverage spec** for the Topic.

**Depth ceiling: PLAN.** Develop and document the recovery plan; it is not executed. Build on Topic 3's requirements + impact analysis.

---

## What this Topic must cover

The finalisation half of the DR-plan lifecycle — develop solution options, choose one to the objectives, and produce the documented plan. Three components:

- **C1 — Range of DR solutions.** The four cloud DR strategies (backup-restore, pilot-light, warm-standby, multi-region active-active) and their RTO/RPO/cost trade-offs; evaluating them against the objectives and choosing the simplest that meets them; DR techniques for cloud environments.
- **C2 — Vendor protections, prioritisation & other components.** Leaning on native protections (backups, cross-region copy, durable/immutable storage); prioritising the recovery against the risks; insurance as a complementary control; the other plan components (runbook, declaration/escalation, communications, DNS failover); continuity standards (ISO 27001/27002/27031).
- **C3 — The disaster recovery plan.** Align the recovery actions to the prioritised risks; the recovery steps, timelines, key features and service providers; show how the plan meets RTO/RPO; document the plan to business needs.

---

## 1. UoC mapping

| UoC item | Descriptor | Component |
|---|---|---|
| `[ICTCLD501 PC 3.1]` | Develop a range of DR solutions according to business requirements | C1 |
| `[ICTCLD501 PC 3.2]` | (Vendor protections) prioritise recovery against risks | C2 |
| `[ICTCLD501 PC 3.3]` | (Insurance) complementary risk-transfer control | C2 |
| `[ICTCLD501 PC 3.4]` | Identify other DR solution components | C2 |
| `[ICTCLD501 PC 4.1]` | Align DR risk potential according to business requirements | C3 |
| `[ICTCLD501 PC 4.2]` | Outline steps, timelines, key features, service providers | C3 |
| `[ICTCLD501 PC 4.3]` | Document the DR plan according to business needs | C3 |
| `[ICTCLD501 PE 1]` | Develop and evaluate a DR plan covering at least three major risk events | C1, C3 |
| `[ICTCLD501 PE 3]` | Document how the plan reaches RTO/RPO targets | C3 |
| `[ICTCLD501 KE 3]` | DR techniques applicable to cloud environments | C1 |
| `[ICTCLD501 KE 4]` | ISO/IEC 27001 / 27002 / 27031 standards | C2 |

> Taught here; formally **evidenced** in AT1 Part B §5–6 + the KE appendix.

---

## 2. AT1 alignment

| AT1 element | Criterion | How Topic 4 aligns |
|---|---|---|
| **Part B §5 — recovery strategy** | B8, B11 | Range of solutions + choice (C1); vendor protections, prioritisation, other components, standards (C2). |
| **Part B §6 — the DR plan** | B12, B13, B14 | Aligned actions, steps/timelines/providers, meeting RTO/RPO, documented (C3). |
| **Part B — KE appendix** | B15 | Written responses on DR techniques and continuity standards (C1, C2). |

**Practice-activity alignment:** evaluate the DR strategies, choose one, and write the recovery plan (runbook + steps + RTO/RPO alignment) for the **practice scenario** — building on the Topic 3 impact analysis.

---

## Out of scope for this Topic (covered elsewhere)

- **DR requirements & impact analysis** → Topic 3.
- **Documenting strand + the presentation/approval/sign-off** → Topic 5.
- **The system design** the plan protects → Topics 1–2.
- **Practical detection/monitoring** (the live CloudWatch alarms behind the plan's detection step) → Topic 9 (`[ICTCLD501 KE 6]`, AT2).

---

## Coverage checklist

- [ ] Every UoC item in §1 is taught.
- [ ] Each of C1–C3 has teaching content (AWS/bespoke).
- [ ] The exercise evaluates the strategies and produces a documented recovery plan (≥3 risks, runbook, RTO/RPO) on the practice scenario.
- [ ] Depth stays at planning — no recovery execution.
- [ ] A student leaving this Topic could attempt Part B §5–6.
