# Topic 2 — Microservices & serverless design · Coverage

**Topic 2 of 10** · **AT1 content Topic** (Part A, microservice strand) · teaching source: AWS ACA serverless (Lambda, API Gateway, SQS, DynamoDB) + bespoke · *deck pinning TBD (Step 3)*.

This file is the **coverage spec** for the Topic.

**Depth ceiling: DESIGN.** AT1 *designs* the microservice; it is built in AT2 (Topics 6–8). Teach to "design and justify the architecture", not "deploy".

---

## What this Topic must cover

Designing one serverless, event-driven microservice for a simple application — the audit-log strand of the Solution Design. Four components:

- **C1 — Identify the microservice & its data transactions.** A single-responsibility service (record an access event durably); the one append-only data transaction; highly cohesive, loosely coupled.
- **C2 — Supporting serverless services.** The services that support the architecture: an HTTPS ingress/API, a messaging/queue buffer, serverless compute, and a managed NoSQL store — what each is and why it fits an event-driven log.
- **C3 — The microservice architecture.** The end-to-end flow (event → API → queue → function → store); the three KE 4 elements — cohesion/coupling, managed database/storage, API + messaging + queuing.
- **C4 — The integration contract.** The single coupling point (a signed event payload over a defined endpoint); how a defined contract lets the producer and the service evolve independently.

---

## 1. UoC mapping

| UoC item | Descriptor | Component |
|---|---|---|
| `[ICTCLD503 PC 2.1]` | Identify microservices and data transactions required | C1 |
| `[ICTCLD503 PC 2.2]` | Determine cloud services to support the microservice architecture | C2 |
| `[ICTCLD503 PC 2.3]` | Design microservice architecture using cloud services | C3 |
| `[ICTCLD503 PE 2]` | Design at least one microservice architecture for a simple web application | C1–C4 |
| `[ICTCLD503 KE 4]` | Web-scale infrastructure — cohesive/coupled systems, database/storage, API/messaging/queuing | C1, C3 |

> Taught here; formally **evidenced** in AT1 Part A §6 + the KE appendix.

---

## 2. AT1 alignment

| AT1 element | Criterion | How Topic 2 aligns |
|---|---|---|
| **Part A §6 — Microservice & Serverless Design** | A8–A10 (microservice design criteria) | Direct — identify the service + transaction (C1), supporting services (C2), the architecture (C3), the contract (C4). |
| **Part A §6.4 — integration contract** | A10 (`[PC 2.3]` + `[KE 4]`) | The webhook contract as the single coupling point (C4). |
| **Part A — KE appendix** | A12 | Written contextual responses on the student's own microservice design choices. |

**Practice-activity alignment:** design one serverless microservice for the **practice scenario** (e.g. a transaction-audit log on the practice Accounting System) — the service + transaction, the supporting services, the flow and the contract — justified against the requirement it serves.

---

## Out of scope for this Topic (covered elsewhere)

- **The web-scale architecture** → Topic 1.
- **Documenting/justifying the design + the presentation** → Topic 5.
- **`[PC 2.4]` document microservice design** → Topic 5.
- **Building/deploying the microservice** (IaC + serverless deploy) → AT2 Topics 6–8 (the design here is realised there).
- **Disaster recovery** → Topics 3–4.

---

## Coverage checklist

- [ ] Every UoC item in §1 is taught.
- [ ] Each of C1–C4 has teaching content (AWS deck reference and/or bespoke framing).
- [ ] The exercise has students *design* one microservice (service + transaction + supporting services + flow + contract) on the practice scenario.
- [ ] Depth stays at design — no deployment steps.
- [ ] A student leaving this Topic could attempt Part A §6.
