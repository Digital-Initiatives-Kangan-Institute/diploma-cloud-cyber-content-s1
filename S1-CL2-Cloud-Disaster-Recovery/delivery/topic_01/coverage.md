# Topic 1 — Web-scale architecture design · Coverage

**Topic 1 of 10** · **AT1 content Topic** (Part A, Solution Design — web-scale strand) · teaching source: AWS web-scale architecture (edge/CDN, elastic load balancing + auto scaling, managed data tiers, caching) + bespoke for the supplied-requirements framing · *DRAFT 2026-06-25; deck pinning TBD (Step 4)*.

This file is the **coverage spec** for the Topic.

**Depth ceiling: DESIGN.** Design the architecture *changes* on paper, to the supplied requirements — the build is AT2. Justify choices against the requirements; do not implement, and do not over-engineer.

---

## What this Topic must cover

The web-scale half of the Solution Design (Part A): confirm the scaling needs, review the current website against them, and design the changes that scale network / compute / storage and serve a global, anonymous public audience while keeping availability and security. Four components:

- **C1 — Web-scaling needs & architecture review.** Determine and confirm the website's web-scaling needs from business requirements; review the current website baseline against those needs and identify the gaps the design must close.
- **C2 — Designing the scale-out & global reach.** Identify the cloud services that scale the web application; design changes that scale network, compute and storage as utilisation rises; scale for a global user base (edge delivery, discoverability); apply web-scaling principles and technologies.
- **C3 — Availability & security of the public surface.** Confirm availability and security are maintained through the changes — protecting the public attack surface (web exploits, bots, DDoS) — and review the design against the requirements.
- **C4 — Web-scale component choices.** The functions, benefits and differences of the web-scale components a design chooses between — SQL/NoSQL, monolith/microservice, virtual/container/serverless compute, CDN/in-memory store — the rationale captured in the Knowledge Evidence appendix.

---

## 1. UoC mapping

| UoC item | Descriptor | Component |
|---|---|---|
| [ICTCLD503 PC 1.1] | Determine and confirm cloud web-scaling needs | C1 |
| [ICTCLD503 PC 1.2] | Review architecture for web application according to business needs | C1 |
| [ICTCLD503 PC 1.3] | Identify cloud services required to scale web application | C2 |
| [ICTCLD503 PC 1.4] | Design architecture changes using cloud services and check design scales network, compute and storage as utilisation increases | C2 |
| [ICTCLD503 PC 1.5] | Determine architecture changes to scale for a global user base | C2 |
| [ICTCLD503 PC 1.6] | Check availability and security of application is maintained with design changes and review design as required | C3 |
| [ICTCLD503 PE 1] | Design at least one architecture that will scale networking, compute and storage for a multi-tier web application | C2 |
| [ICTCLD503 PE 5] | Apply web-scaling principles and technologies | C2 |
| [ICTCLD503 KE 3] | Functions, benefits and differences of web-scale cloud components (SQL/NoSQL; monolith/microservice; virtual/container/serverless; CDN/in-memory) | C4 |
| [ICTCLD503 KE 6] | Web-scaling principles and technologies | C2 |

> Taught here; formally **evidenced** in AT1 Part A (Solution Design, web-scale sections) + the Part A KE appendix.

---

## 2. AT1 alignment

| AT1 element | Criterion | How Topic 1 aligns |
|---|---|---|
| **Part A — purpose, inputs, review** | A1, A2, A3 | states the web-scale change + scope, the design inputs/requirements (data residency as an input constraint), and reviews the existing architecture for gaps (C1). |
| **Part A — web-scale design** | A4, A5, A6 | scaling by layer (network/compute/storage), global delivery, availability/security of the public surface (C2, C3). |
| **Part A — component choices + KE** | A7, A12 | justifies the SQL/NoSQL · monolith/microservice · compute-model · CDN/cache choices; KE appendix on web-scale concepts (C4). |

**Practice-activity alignment:** design the web-scale architecture changes for the **practice scenario's** public web workload — scaling by layer + global delivery, availability/security maintained — to the supplied requirements.

---

## Out of scope for this Topic (covered elsewhere)

- **The audit-log microservice design** → Topic 2.
- **DR requirements, impact analysis, strategy and plan** → Topics 3–4.
- **Assembling, documenting & justifying the Solution Design, and presenting for approval** → Topic 5.
- **Implementing/building the design** → AT2 (Topics 6–10).

---

## Coverage checklist

- [ ] Every UoC item in §1 is taught.
- [ ] Each of C1–C4 has teaching content (AWS/bespoke).
- [ ] The exercise designs a web-scale architecture (scales network/compute/storage + global delivery) on the practice scenario, to the supplied requirements.
- [ ] Depth stays at design — no implementation/build.
- [ ] A student leaving this Topic could attempt the web-scale half of Part A.
