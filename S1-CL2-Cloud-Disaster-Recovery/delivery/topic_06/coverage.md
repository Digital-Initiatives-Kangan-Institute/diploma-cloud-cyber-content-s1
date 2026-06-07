# Topic 6 — IaC: fundamentals & operating provided templates · Coverage

**Topic 6 of 10** · **AT2 content Topic** (build — IaC operate half) · teaching source: AWS ACA CloudFormation/IaC + bespoke (supplied-template discipline) · *deck pinning TBD (Step 3)*.

This file is the **coverage spec** for the Topic.

**Depth ceiling: BUILD.** First hands-on Topic of AT2. Per the process, AWS practicals run `teach → demo → practice`.

---

## What this Topic must cover

Infrastructure as Code from first principles, then operating a template you were *given* — the first of AT2's two IaC skills. Five components:

- **C1 — Why IaC.** What IaC is and its benefits over manual console provisioning; how automation leverages the platform; the potential issues/errors; selecting an IaC service compatible with the platform.
- **C2 — Template anatomy & review.** The template syntax (parameters, resources, outputs, intrinsic functions); reviewing a *pre-defined* template to determine the resources it creates and any dependencies.
- **C3 — Operating a provided template.** Deploy, update and delete resources using the predefined template; confirm via console/CLI; remove cleanly.
- **C4 — Troubleshooting templates.** Test and troubleshoot template errors (read the error, diagnose, fix, redeploy) — using the deliberately broken copy.
- **C5 — Shared cloud foundations.** Industry technology standards and standard hardware/software/storage products that underpin building — the foundational knowledge shared with ICTCLD503.

---

## 1. UoC mapping

| UoC item | Descriptor | Component |
|---|---|---|
| `[ICTCLD505 PC 1.1]` | Identify and review benefits of IaC | C1 |
| `[ICTCLD505 PC 1.2]` | Determine ways automation leverages cloud platforms | C1 |
| `[ICTCLD505 PC 1.3]` | Determine potential issues and errors when implementing IaC | C1 |
| `[ICTCLD505 PC 1.4]` | Evaluate and select an IaC service compatible with the platform | C1 |
| `[ICTCLD505 PC 2.1]` | Learn template syntax of the selected IaC service | C2 |
| `[ICTCLD505 PC 2.2]` | Review pre-defined templates; determine resources and dependencies | C2 |
| `[ICTCLD505 PC 2.3]` | Deploy, update and delete resources using predefined templates | C3 |
| `[ICTCLD505 PC 2.4]` | Confirm deployments; configure via console or CLI | C3 |
| `[ICTCLD505 PC 2.5]` | Remove deployed resources; delete templates | C3 |
| `[ICTCLD505 PC 2.6]` | Test and troubleshoot template errors | C4 |
| `[ICTCLD505 PE 1]` | Deploy, update and remove infrastructure using templates | C3 |
| `[ICTCLD505 PE 3]` | Use management console, SDKs or command line tools | C3 |
| `[ICTCLD505 KE 3]` | Benefits of IaC vs manual provisioning | C1 |
| `[ICTCLD505 KE 4]` | IaC services on a cloud platform | C1 |
| `[ICTCLD505 KE 5]` | Template syntax | C2 |
| `[ICTCLD505 KE 6]` | Tooling to execute templates | C3 |
| `[ICTCLD505 KE 7]` | Testing/debugging techniques and common errors | C4 |
| `[ICTCLD505 KE 10]` | Methods to create, manage, provision and update templates | C3 |
| `[ICTCLD505 KE 11]` | Techniques/metrics to deploy and manage templates | C1, C3 |
| `[ICTCLD503 KE 1]` / `[ICTCLD505 KE 1]` | Industry technology standards | C5 |
| `[ICTCLD503 KE 2]` / `[ICTCLD505 KE 2]` | Industry standard hardware/software/storage | C5 |

> Taught here; formally **evidenced** in AT2 §4.2 (operate the provided data-store template) + the written KE appendix (assembled in Topic 10).

---

## 2. AT2 alignment

| AT2 element | Criterion | How Topic 6 aligns |
|---|---|---|
| **§4.2 — Operating the provided data-store template** | D2 | Direct — review/deploy/update/delete/troubleshoot the *provided* DynamoDB template (C2–C4). |
| **§5 / §8 — config decisions & foundations** | D8, D12 | IaC-service choice + the shared-foundations KE (C1, C5). |

**Practice-activity alignment:** `teach → demo → practice` — operate a *provided* practice template (deploy → update a parameter → delete → fix a broken copy) in the lab, on the practice scenario.

---

## Out of scope for this Topic (covered elsewhere)

- **Authoring your own template** → Topic 7.
- **The microservice build** (API/queue/function) → Topic 8.
- **Monitoring** → Topic 9; **documentation/sign-off** → Topic 10.

---

## Coverage checklist

- [ ] Every UoC item in §1 is taught.
- [ ] Each of C1–C5 has teaching content (AWS deck reference and/or bespoke).
- [ ] A `[DEMO]` precedes the practice (operate a provided template).
- [ ] The exercise covers the full lifecycle — deploy, update, delete, troubleshoot.
- [ ] A student leaving this Topic could attempt AT2 §4.2.
