# Topic 8 — Building & deploying the serverless microservice · Coverage

**Topic 8 of 10** · **AT2 content Topic** (build — the microservice) · teaching source: AWS ACA serverless deploy + the provided code/contract · *deck pinning TBD (Step 3)*.

This file is the **coverage spec** for the Topic.

**Depth ceiling: BUILD.** This is where Topics 6–7 (IaC) converge with the serverless services — the student's *own* template (Topic 7 skill) provisions the microservice, from the *provided* code, writing to the *provided* store (Topic 6). `teach → demo → practice`.

---

## What this Topic must cover

Deploying the serverless audit-log microservice from the supplied code — the implementation half of the microservice strand. Four components:

- **C1 — Review the design & code.** Review the microservice design (from AT1) and the supplied code components and contract before deployment.
- **C2 — Deploy & configure.** Deploy and configure the serverless services to implement the application — the API route, the queue as the function's event source, the function writing to the provided store (its table name supplied to the function).
- **C3 — Test & confirm functioning.** Post sample events to the contract; confirm each is persisted (exactly once) in the data store; confirm an invalid event is rejected.
- **C4 — Troubleshoot.** Diagnose and fix microservice errors (e.g. a permission error, a payload-validation bug) from the logs.

---

## 1. UoC mapping

| UoC item | Descriptor | Component |
|---|---|---|
| `[ICTCLD503 PC 3.1]` | Review microservice design and code components | C1 |
| `[ICTCLD503 PC 3.2]` | Deploy and configure cloud services to implement the application | C2 |
| `[ICTCLD503 PC 3.3]` | Test microservice components; confirm the application functions | C3 |
| `[ICTCLD503 PC 3.4]` | Troubleshoot and fix errors | C4 |
| `[ICTCLD503 PE 3]` | Deploy a microservice using cloud serverless technologies | C2 |
| `[ICTCLD503 PE 4]` | Use management consoles, SDKs or command line tools | C2 |
| `[ICTCLD503 KE 5]` | Testing and debugging techniques | C3, C4 |

> Taught here; formally **evidenced** in AT2 §4.4 (the deployed, tested microservice).

---

## 2. AT2 alignment

| AT2 element | Criterion | How Topic 8 aligns |
|---|---|---|
| **§4.4 — The audit-log microservice** | D4 | Direct — deploy/configure the serverless services from the provided code, wired to the store, and confirm it writes a record (C1–C3). |
| **§6 — testing/troubleshooting** | D5, D9 | Functional test + troubleshooting log (C3, C4). |

**Practice-activity alignment:** `teach → demo → practice` — deploy the practice microservice (author the template provisioning the API/queue/function from supplied practice code, wire it to the practice store, post a test event, confirm the record). This is the cumulative product of Topics 6–8.

---

## Out of scope for this Topic (covered elsewhere)

- **Generic IaC authoring skill** (taught) → Topic 7; **operating a provided template** → Topic 6.
- **The microservice *design*** (services chosen, the contract) → AT1 Topic 2.
- **Monitoring the running service** → Topic 9; **documentation/sign-off** → Topic 10.

---

## Coverage checklist

- [ ] Every UoC item in §1 is taught.
- [ ] Each of C1–C4 has teaching content (AWS deck reference and/or bespoke).
- [ ] A `[DEMO]` precedes the practice (deploy + test the microservice).
- [ ] The exercise has students deploy the service from supplied code and confirm a record is written.
- [ ] A student leaving this Topic could attempt AT2 §4.4.
