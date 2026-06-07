# Topic 7 — Authoring & parameterising your own IaC template · Coverage

**Topic 7 of 10** · **AT2 content Topic** (build — IaC author half) · teaching source: AWS ACA CloudFormation + bespoke · *deck pinning TBD (Step 3)*.

This file is the **coverage spec** for the Topic.

**Depth ceiling: BUILD.** The second IaC skill — authoring, not just operating. `teach → demo → practice`. Builds on Topic 6's template anatomy.

---

## What this Topic must cover

Writing your *own* template from scratch — the author-your-own half of IaC. Three components:

- **C1 — Authoring a template.** Apply the template syntax to create and deploy a template that provisions a set of related cloud resources to business needs.
- **C2 — Update & parameterise for reuse.** Update and redeploy the template to modify and add resources; parameterise it so the same template deploys to different configurations without editing the body; confirm via console/CLI — the key code-reuse outcome.
- **C3 — Remove & troubleshoot.** Remove the deployed resources and delete templates cleanly; test and troubleshoot errors in your own template.

Plus the industry practice that governs it: parameters over hard-coding, least-privilege, tagging, outputs for integration.

---

## 1. UoC mapping

| UoC item | Descriptor | Component |
|---|---|---|
| `[ICTCLD505 PC 3.1]` | Learn template syntax of the selected IaC service | C1 |
| `[ICTCLD505 PC 3.2]` | Create and deploy a template to provision a related resource set | C1 |
| `[ICTCLD505 PC 3.3]` | Update and redeploy to modify and add resources | C2 |
| `[ICTCLD505 PC 3.4]` | Confirm deployment; configure via console or CLI | C2 |
| `[ICTCLD505 PC 3.5]` | Parameterise and deploy to reuse configuration | C2 |
| `[ICTCLD505 PC 3.6]` | Remove deployed resources; delete templates | C3 |
| `[ICTCLD505 PC 3.7]` | Test and troubleshoot template errors | C3 |
| `[ICTCLD505 PE 2]` | Create, run and update at least one own template | C1–C3 |
| `[ICTCLD505 KE 8]` | Parameterisation for configuration and code reuse | C2 |
| `[ICTCLD505 KE 9]` | Industry standard practices to define IaC | C1 |

> Taught here; formally **evidenced** in AT2 §4.3 (the student's own microservice template) — the authored artefact realised in Topic 8.

---

## 2. AT2 alignment

| AT2 element | Criterion | How Topic 7 aligns |
|---|---|---|
| **§4.3 — Authoring the microservice IaC template** | D3 | Direct — author/parameterise/update/redeploy/remove an own template (C1–C3); reference the provided table. |
| **§5 — config decisions** | D8 | Parameterisation + industry IaC practice (KE 8, 9). |

**Practice-activity alignment:** `teach → demo → practice` — author a small template from scratch on the practice scenario (provision a related resource set, parameterise it, redeploy with new values, remove). The microservice template proper is built in Topic 8.

---

## Out of scope for this Topic (covered elsewhere)

- **Operating a *provided* template** → Topic 6.
- **The microservice services + the provided code** (what the authored template deploys) → Topic 8.
- **Monitoring** → Topic 9; **documentation/sign-off** → Topic 10.

---

## Coverage checklist

- [ ] Every UoC item in §1 is taught.
- [ ] Each of C1–C3 has teaching content (AWS deck reference and/or bespoke).
- [ ] A `[DEMO]` precedes the practice (author + parameterise a template).
- [ ] The exercise has students author their *own* template, parameterise it, redeploy and remove it.
- [ ] A student leaving this Topic could attempt AT2 §4.3.
