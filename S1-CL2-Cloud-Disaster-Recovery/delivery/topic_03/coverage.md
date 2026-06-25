# Topic 3 — DR: requirements & impact analysis · Coverage

**Topic 3 of 10** · **AT1 content Topic** (Part B, DR strand — front half) · teaching source: AWS DR concepts (RTO/RPO, risk in cloud) + bespoke for requirements gathering + impact analysis on the practice scenario · *DRAFT 2026-06-25; deck pinning TBD (Step 4)*.

This file is the **coverage spec** for the Topic.

**Depth ceiling: ANALYSIS.** Develop the DR plan requirements and the impact analysis (the front half of the DR-plan lifecycle) for the system designed in Topics 1–2. The recovery strategy and the finalised plan are Topic 4; recovery is not executed.

---

## What this Topic must cover

The requirements-and-impact half of the DR-plan lifecycle — establish what recovery must achieve, then analyse the risks and their impact. Three components:

- **C1 — Plan requirements & current recovery position.** Identify the DR plan requirements per business needs; determine the existing organisational recovery arrangements; identify the vendor (cloud provider) DR provisions and SLAs.
- **C2 — Recovery objectives & data managed.** Determine RTO and RPO to business needs and explain them; estimate the amount and security level of data managed.
- **C3 — Risk & impact analysis.** Assess at least three major risk events (likelihood, impact, severity) and plan exclusions; evaluate the severity of impact and disruption; document the impact-analysis outcomes per organisational policies — grounded in the cloud risk environment and a data-analysis methodology.

---

## 1. UoC mapping

| UoC item | Descriptor | Component |
|---|---|---|
| [ICTCLD501 PC 1.1] | Identify disaster recovery plan requirements according to business needs and requirements | C1 |
| [ICTCLD501 PC 1.2] | Determine existing organisational recovery plans | C1 |
| [ICTCLD501 PC 1.3] | Identify vendor disaster recovery plan and service level agreements | C1 |
| [ICTCLD501 PC 2.1] | Determine time and recovery point objectives according to business needs | C2 |
| [ICTCLD501 PC 2.3] | Estimate amount of data and security level of data managed | C2 |
| [ICTCLD501 PC 2.2] | Assess potential risks plan exclusions according to business requirements | C3 |
| [ICTCLD501 PC 2.4] | Evaluate severity of impact and disruption of risk events | C3 |
| [ICTCLD501 PC 2.5] | Document outcomes of impact analysis according to organisational policies and procedures | C3 |
| [ICTCLD501 PE 2] | Determine likelihood and impact of risk event to assist in the development of one cloud disaster recovery plan | C3 |
| [ICTCLD501 KE 1] | Risk environments in cloud/ICT environment | C3 |
| [ICTCLD501 KE 2] | Data analysis methodologies to determine risk environment | C3 |
| [ICTCLD501 KE 5] | Recovery Time Objective (RTO) and Recovery Point Objective (RPO) standards and techniques | C2 |

> Taught here; formally **evidenced** in AT1 Part B §1–2 (requirements + impact analysis) + the Part B KE appendix.

---

## 2. AT1 alignment

| AT1 element | Criterion | How Topic 3 aligns |
|---|---|---|
| **Part B — requirements & context** | B1, B2 | plan requirements per business needs; current recovery position + vendor DR provisions/SLAs (C1). |
| **Part B — impact analysis** | B3, B4 | RTO/RPO determined and explained; amount + security level of data managed (C2). |
| **Part B — impact analysis** | B5, B6, B7 | risk assessment (≥3 events, likelihood/impact/severity), exclusions, documented outcomes (C3). |
| **Part B — KE appendix** | B15 | risk environment, data-analysis method, RTO/RPO (C2, C3). |

**Practice-activity alignment:** establish the DR requirements + recovery objectives and produce the impact analysis (≥3 major risk events with likelihood/impact/severity) for the **practice scenario** — the input to the Topic 4 recovery plan.

---

## Out of scope for this Topic (covered elsewhere)

- **Recovery strategy, vendor protections, insurance, other components, and the finalised DR plan** → Topic 4.
- **The system design the plan protects** → Topics 1–2.
- **Documenting & presenting the plan for approval** → Topic 5.
- **Live detection/monitoring behind the plan's detection step** → Topic 9 (AT2).

---

## Coverage checklist

- [ ] Every UoC item in §1 is taught.
- [ ] Each of C1–C3 has teaching content (AWS/bespoke).
- [ ] The exercise produces the DR requirements + impact analysis (≥3 risks, RTO/RPO, data managed) on the practice scenario.
- [ ] Depth stays at analysis — no recovery strategy/plan (Topic 4) and no execution.
- [ ] A student leaving this Topic could attempt Part B §1–2.
