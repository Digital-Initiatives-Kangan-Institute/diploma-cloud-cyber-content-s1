# Topic 2 — Microservice & serverless design · Coverage

**Topic 2 of 10** · **AT1 content Topic** (Part A, Solution Design — microservice strand) · teaching source: AWS serverless (functions, API gateway, managed datastore, messaging/queuing, event routing) + bespoke for the audit-log microservice + webhook-contract framing · *DRAFT 2026-06-25; deck pinning TBD (Step 4)*.

This file is the **coverage spec** for the Topic.

**Depth ceiling: DESIGN.** Design the serverless audit-log microservice — services, data transactions, architecture and the integration contract — on paper. The deploy/build is AT2 (Topic 8); do not implement.

---

## What this Topic must cover

The microservice half of the Solution Design (Part A): a serverless audit-log microservice that records India-cohort access events. Three components:

- **C1 — Microservices & data transactions.** Identify the microservice(s) and the data transaction(s) each handles, to meet business needs (what the audit-log service captures and records).
- **C2 — Supporting cloud services.** Determine the cloud services that support the microservice architecture — serverless compute, a managed/persistent datastore, and API / messaging / queuing services.
- **C3 — Microservice architecture & contract.** Design the architecture using cloud services — highly cohesive and loosely coupled, persistent storage, API/messaging/queuing — and define the interface/webhook integration contract; grounded in the definitions and features of web-scale cloud infrastructure.

---

## 1. UoC mapping

| UoC item | Descriptor | Component |
|---|---|---|
| [ICTCLD503 PC 2.1] | Identify microservices and data transactions required to meet business needs | C1 |
| [ICTCLD503 PC 2.2] | Determine cloud services to support microservice architecture | C2 |
| [ICTCLD503 PC 2.3] | Design microservice architecture using cloud services | C3 |
| [ICTCLD503 PE 2] | Design at least one microservice architecture for implementing a simple web application | C3 |
| [ICTCLD503 KE 4] | Definitions, functions, features and uses of web-scale cloud infrastructure (cohesion/coupling; persistent datastore; API/messaging/queuing) | C3 |

> Taught here; formally **evidenced** in AT1 Part A (Solution Design, microservice sections) + the Part A KE appendix.

---

## 2. AT1 alignment

| AT1 element | Criterion | How Topic 2 aligns |
|---|---|---|
| **Part A — microservice** | A8 | identifies the microservice(s) and the data transaction(s) each handles (C1). |
| **Part A — microservice** | A9 | determines the cloud services that support the microservice architecture (C2). |
| **Part A — microservice + KE** | A10, A12 | designs the architecture (cohesion/coupling, persistent storage, API/messaging/queuing) with the interface/integration contract; KE appendix on microservice concepts (C3). |

**Practice-activity alignment:** design a serverless microservice (services + data transactions, supporting cloud services, cohesive/loosely-coupled architecture + contract) for the **practice scenario**, to the business need.

---

## Out of scope for this Topic (covered elsewhere)

- **The web-scale architecture design** → Topic 1.
- **Assembling, documenting & justifying the Solution Design, and presenting for approval** → Topic 5.
- **Deploying/building the microservice** (review design + code, deploy, test, troubleshoot) → AT2 Topic 8 (ICTCLD503 element 3).
- **DR requirements, impact analysis, strategy and plan** → Topics 3–4.

---

## Coverage checklist

- [ ] Every UoC item in §1 is taught.
- [ ] Each of C1–C3 has teaching content (AWS/bespoke).
- [ ] The exercise designs a serverless microservice (services + data transactions, supporting services, architecture + contract) on the practice scenario.
- [ ] Depth stays at design — no deploy/build.
- [ ] A student leaving this Topic could attempt the microservice half of Part A.
