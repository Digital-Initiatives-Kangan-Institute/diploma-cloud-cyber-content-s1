# Topic 13 — HA implementation & simulation · Coverage

**Topic 13 of 14** · **AT3 content Topic** (High Availability — build & prove it) · teaching source: **mixed** — bespoke **ICTCLD502 Topic 4** (implement & finalise: approaches, IaC, testing tiers, monitoring, simulating failures, load/stress testing, improving availability) + **ACA M10** (the recorded "Creating a Highly Available Application" demo, S44) / ACA M11 (IaC, light); bespoke to anchor to the Accounting baseline.

The coverage spec — what this Topic must cover, in UoC and AT terms. `slide_plan.md` and the deck are built to satisfy it.

> **Build it, then break it.** Topic 12 produced the HA design; Topic 13 **implements** it on the running baseline and **simulates failures/resizes to prove it's fault tolerant** — then compares the findings to the design and improves. This is ICTCLD502 element 4 (+ 5.1). **teach → demonstrate → practice** for the AWS build (recorded demo); **teach → practice** for the simulations (student-driven). AT3 = ICTCLD502 (primary).

---

## Teaching-design note

The build is an AWS practical → recorded demo (ACA M10 S44) then practice. The simulations are student-driven lab work (no recorded "simulate a failure" demo exists), so they run **teach → practice**. Reuse-first: the implement/simulate/finalise *method* is the bespoke 502 Topic 4 deck; the worked HA build is ACA M10. Students implement and simulate **their own Topic 12 HA design** on the Accounting baseline.

---

## What this Topic must cover

Implement the HA design, prove it under simulated failure, and finalise — to the student's own design, on the practice baseline. Three components:

- **C1 — Implement the design.** Implementation approaches (big-bang / incremental / parallel — in-place hardening = incremental); IaC; implement the hardening; **demonstrate connectivity at all tiers** (incl. failover). *(ICTCLD502 PC 4.1, 4.2.)*
- **C2 — Simulate failures & resizes.** **Monitor & measure availability**; **simulate component/AZ failures** and confirm fault tolerance; **simulate resizing** and measure the availability impact; load/stress testing. *(ICTCLD502 PC 4.3, 4.4, 4.5.)*
- **C3 — Compare, improve & document.** **Compare** the simulation findings against the documented design; **improve** availability where simulations show gaps; **document** the findings. *(ICTCLD502 PC 4.6, 5.1.)*

---

## 1. UoC mapping

UoC **taught / developed** in this Topic:

| UoC item | Descriptor | Component |
|---|---|---|
| [ICTCLD502 PC 4.1] | Implement architecture design in cloud environment | C1 |
| [ICTCLD502 PC 4.2] | Demonstrate connectivity between resources at all tiers | C1 |
| [ICTCLD502 PC 4.3] | Monitor and measure availability of resources | C2 |
| [ICTCLD502 PC 4.4] | Simulate failures of component and confirm infrastructure is fault tolerant | C2 |
| [ICTCLD502 PC 4.5] | Simulate resizing components likely to impact performance and measure availability impact | C2 |
| [ICTCLD502 PC 4.6] | Compare and document simulation findings according to documented design | C3 |
| [ICTCLD502 PC 5.1] | Adjust and improve availability of architecture according to simulations as required | C3 |
| [ICTCLD502 PE 1] | Design and implement at least one fault-tolerant cloud infrastructure resilient to networking/compute/storage/database/data-centre failures | C1 · C2 *(the implement + prove portion)* |
| [ICTCLD401 PC 3.2] | Test automatic scaling and fix errors (applied under load/resize) | C2 *(applied)* |

> **AT3 marking home: Part B — implementation + simulation window.** This Topic develops the skills assessed in AT3 Part B (the ~3.5 h maintenance-window implementation + the failure/resize simulations). AT3 build-topic refs **T9–T14** (implement · connectivity · availability measurement · failure sim · resize sim · compare/test).

UoC **applied** here but **taught earlier** (not re-taught):

| What | Where |
|---|---|
| The HA design being implemented | Topic 12 (produced there; built here) |
| HA concepts (SPOF, RTO/RPO, the toolkit) | Topic 11 |
| Building EC2/ALB/ASG/RDS; CloudWatch monitoring | AT2 / Topics 8–9 (used here at the HA layer) |

---

## 2. AT3 equivalence / alignment

| AT3 element | Where assessed | How Topic 13 aligns |
|---|---|---|
| **Implement HA** (502 4.1–4.2) | AT3 Part B | C1 — implement the hardening in place; demonstrate connectivity at all tiers. |
| **Monitor + simulate** (502 4.3–4.5) | AT3 Part B | C2 — measure availability; simulate failures (confirm fault tolerant) + resizes (measure impact). |
| **Compare + improve** (502 4.6, 5.1) | AT3 Part B → closure | C3 — compare findings to the design; improve and re-test; document. |

**Practice-activity alignment:** students **implement and simulate their own Topic 12 HA design** on the practice baseline (Accounting / Ledgerline) in the AWS Academy lab — mirroring the AT3 Part-B window on the LMS (where the supplied AT2 baseline is deployed to a known start state, then hardened + simulated).

---

## Out of scope for this Topic (covered elsewhere)

- **Producing the HA design** → **Topic 12** (implemented here, not designed here).
- **HA concepts** → **Topic 11**.
- **Closure — HA Deployment Report, feedback, sign-off** → **Topic 14** (502 Topic 4 S11–S12 / element 5.2–5.3).
- **Multi-Region / full DR** → CL2 (single-Region HA only).

---

## Coverage checklist (for `slide_plan.md` + the deck to satisfy)

- [ ] C1 = teach → **recorded demo (ACA M10 S44)** → practice (implement); C2/C3 = teach → practice (student-driven simulations).
- [ ] **Implementation approaches** (big-bang/incremental/parallel) taught; in-place hardening framed as **incremental** (no outage).
- [ ] **Connectivity at all tiers** demonstrated after implementing (client→app, app→db, failover + fail-back) (C1, PC 4.2).
- [ ] **Simulate failures** (disable assets / network disruption) + **confirm fault tolerant**; **measure availability** throughout (C2, PC 4.3–4.4).
- [ ] **Simulate a resize** + **measure the availability impact**; load/stress testing (C2, PC 4.5).
- [ ] **Compare** findings to the documented design's recovery objectives; **improve** where gaps appear; **document** the findings (C3, PC 4.6 / 5.1).
- [ ] Students implement + simulate **their own Topic 12 design** on the Accounting baseline.
- [ ] In-world; source-deck refs by title may stay; UoC refs off slides; depth ceiling single-Region HA (cross-AZ).
- [ ] A student leaving this Topic can implement an HA design, prove it under simulated failure, and document the findings — ready to close out in Topic 14.
