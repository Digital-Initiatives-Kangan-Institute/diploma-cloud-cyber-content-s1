# Topic 3 — DR: requirements & impact analysis · Coverage

**Topic 3 of 10** · **AT1 content Topic** (Part B, DR strand — opening half) · teaching source: AWS resilience/DR concepts + bespoke (501 risk/impact discipline) · *deck pinning TBD (Step 3)*.

This file is the **coverage spec** for the Topic.

**Depth ceiling: PLAN.** 501 is a planning unit — the DR is planned and approved, never executed. Teach to "determine requirements and analyse impact", not "recover".

---

## What this Topic must cover

The opening half of the DR-plan lifecycle — establishing the plan's requirements and conducting the impact analysis the solutions build on. Three components:

- **C1 — DR plan requirements & current recovery position.** Identify the DR requirements from business needs; determine existing organisational recovery arrangements; identify the vendor's DR provisions and SLAs (shared-responsibility, native protections).
- **C2 — Recovery objectives.** Determine RTO and RPO from the business's tolerance for downtime and data loss; RTO/RPO standards and what they drive.
- **C3 — Impact analysis.** Identify at least three major risk events, rate likelihood × impact for severity, the data managed (volume/sensitivity), plan exclusions, and record the outcomes — the basis for the recovery strategy.

---

## 1. UoC mapping

| UoC item | Descriptor | Component |
|---|---|---|
| `[ICTCLD501 PC 1.1]` | Identify DR plan requirements according to business needs | C1 |
| `[ICTCLD501 PC 1.2]` | Determine existing organisational recovery plans | C1 |
| `[ICTCLD501 PC 1.3]` | Identify vendor DR plan and SLAs | C1 |
| `[ICTCLD501 PC 2.1]` | Determine RTO and RPO according to business needs | C2 |
| `[ICTCLD501 PC 2.2]` | (Plan exclusions) determine scope of the impact analysis | C3 |
| `[ICTCLD501 PC 2.3]` | Determine the data managed (volume/sensitivity) | C3 |
| `[ICTCLD501 PC 2.4]` | Evaluate severity of impact and disruption | C3 |
| `[ICTCLD501 PC 2.5]` | Record impact-analysis outcomes | C3 |
| `[ICTCLD501 PE 2]` | Determine likelihood and impact of risk events | C3 |
| `[ICTCLD501 KE 1]` | Risk environments | C3 |
| `[ICTCLD501 KE 2]` | Data-analysis methodologies | C3 |
| `[ICTCLD501 KE 5]` | RTO/RPO standards and techniques | C2 |
| `[ICTCLD501 FS Planning & organising]` | Plan/sequence the impact analysis | C3 |

> Taught here; formally **evidenced** in AT1 Part B §2–4 + the KE appendix.

---

## 2. AT1 alignment

| AT1 element | Criterion | How Topic 3 aligns |
|---|---|---|
| **Part B §2–3 — requirements & current recovery position** | B1, B2 | Identify requirements (C1); existing org plans + vendor DR/SLAs (C1). |
| **Part B §4 — impact analysis** | B3, B5 | RTO/RPO (C2); severity, data, likelihood/impact, ≥3 risk events (C3). |
| **Part B — KE appendix** | B15 | Written responses on risk environment, RTO/RPO, data methodologies (C2, C3). |

**Practice-activity alignment:** produce a DR requirements + impact analysis (risk register + RTO/RPO + severity) for the **practice scenario** system — not the LMS.

---

## Out of scope for this Topic (covered elsewhere)

- **DR solutions, strategy and the recovery plan** → Topic 4.
- **Documenting the plan + the presentation/approval** → Topic 5.
- **The system design** the plan protects → Topics 1–2.
- **Practical monitoring/alerting** (CloudWatch alarms) → Topic 9 (AT2). Here, detection is a planning concept only.

---

## Coverage checklist

- [ ] Every UoC item in §1 is taught.
- [ ] Each of C1–C3 has teaching content (AWS/bespoke).
- [ ] The exercise produces a requirements + impact analysis (risk register, RTO/RPO, severity) on the practice scenario.
- [ ] Depth stays at planning — no recovery execution.
- [ ] A student leaving this Topic could attempt Part B §2–4.
