# Topic 1 — Web-scale architecture & design · Coverage

**Topic 1 of 10** in the CL2 teaching sequence · **AT1 content Topic** (Part A, web-scale strand) · teaching source: AWS ACA (CloudFront/edge, ElastiCache, Auto Scaling, Route 53) + bespoke · *deck pinning TBD (Step 3)*.

This file is the **coverage spec** — what this Topic must cover, in UoC and AT1 terms. The slide plan + exercises are built to satisfy it.

**Depth ceiling: DESIGN.** AT1 *designs* the web-scale architecture; it is never built (no web-scale build in the cluster). Teach to "design and justify", not "deploy".

---

## What this Topic must cover

Designing a scalable web-application architecture for a global user base — the web-scale strand of the Solution Design. Five components:

- **C1 — Web-scaling needs & the existing architecture.** Confirm the scaling drivers (more concurrent users, a distant second cohort, spikier demand); review the current architecture and find the gaps (edge delivery, read-path scale).
- **C2 — Scaling the layers.** The cloud services that scale network, compute and storage as utilisation increases — load balancing + auto scaling (compute), read/session caching (in-memory), elastic/object storage — and *how* each scales.
- **C3 — Global delivery.** Serving a global user base with acceptable latency: a CDN at the edge + latency-based routing, so distant users hit the nearest edge rather than the origin.
- **C4 — Availability & security through change.** Maintaining availability (multi-AZ posture) and security (TLS, WAF, locked origin) while making the changes; reviewing the design against the requirements.
- **C5 — Web-scale component choices & principles.** SQL vs NoSQL, monolith vs microservice, container vs serverless, CDN + in-memory store — what each is and where it fits; the underlying web-scaling principles.

---

## 1. UoC mapping

UoC **taught / developed** in this Topic:

| UoC item | Descriptor | Component |
|---|---|---|
| `[ICTCLD503 PC 1.1]` | Determine and confirm cloud web-scaling needs | C1 |
| `[ICTCLD503 PC 1.2]` | Review architecture for web application | C1 |
| `[ICTCLD503 PC 1.3]` | Identify cloud services required to scale | C2 |
| `[ICTCLD503 PC 1.4]` | Design architecture changes; check it scales network/compute/storage | C2 |
| `[ICTCLD503 PC 1.5]` | Determine architecture changes to scale for a global user base | C3 |
| `[ICTCLD503 PC 1.6]` | Review design (maintain availability and security) | C4 |
| `[ICTCLD503 PE 1]` | Design at least one architecture that scales networking, compute and storage | C1–C4 |
| `[ICTCLD503 PE 5]` | Apply web-scaling principles and technologies | C5 |
| `[ICTCLD503 KE 3]` | Functions/benefits/differences of web-scale components | C5 |
| `[ICTCLD503 KE 6]` | Web-scaling principles and technologies | C5 |

> Taught here; formally **evidenced** in AT1 Part A §5 (the Solution Design) + the KE appendix (§2 below).

---

## 2. AT1 alignment

What in AT1 (Part A — Solution Design) this Topic prepares students for:

| AT1 element | Criterion | How Topic 1 aligns |
|---|---|---|
| **Part A §5 — Web-scale Design** (scaling by layer, global delivery, availability/security) | A4–A7 (web-scale design criteria) | Direct — the Topic teaches exactly the design the section requires: needs (C1), layer scaling (C2), global delivery (C3), availability/security (C4). |
| **Part A — component-choice justification** | A7 | `[KE 3/6]` + `[PE 5]` — the SQL/NoSQL, monolith/microservice, container/serverless, CDN/in-memory choices (C5). |
| **Part A — KE appendix** | A12 | Written contextual responses on the student's own web-scale design choices (C5). |

**Practice-activity alignment:** design a web-scale architecture for the **practice web-scale app** (the practice vehicle — TBD; *not* the LMS) — choose the scaling services per layer + the edge/global approach, and justify each against the requirements.

---

## Out of scope for this Topic (covered elsewhere)

- **The microservice design** (serverless audit-log service) → Topic 2.
- **Documenting/justifying the design + the presentation** → Topic 5.
- **`[PC 1.7]` document architecture changes** → Topic 5 (the documentation strand).
- **Disaster recovery** of this design → Topics 3–4.
- **Any build/implementation** — the web-scale architecture is design-only; nothing here is deployed.

---

## Coverage checklist (for the slide plan + exercises to satisfy)

- [ ] Every UoC item in §1 is taught.
- [ ] Each of C1–C5 has teaching content (AWS deck reference and/or bespoke framing).
- [ ] The exercise has students *design* a web-scale architecture (layer scaling + global delivery + justification) on the practice app.
- [ ] Depth stays at design — no deployment steps.
- [ ] A student leaving this Topic could attempt Part A §5.
