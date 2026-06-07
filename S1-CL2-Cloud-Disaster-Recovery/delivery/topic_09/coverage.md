# Topic 9 — Monitoring & alarms · Coverage

**Topic 9 of 10** · **AT2 content Topic** (build — monitoring) · teaching source: AWS ACA CloudWatch + bespoke · *deck pinning TBD (Step 3)*.

This file is the **coverage spec** for the Topic.

**Depth ceiling: BUILD.** Configure monitoring on the running microservice from Topic 8. `teach → demo → practice`.

---

## What this Topic must cover

Observing the running system — metrics and a scaling-relevant alarm on the serverless microservice. Two components:

- **C1 — Metrics & monitoring.** Cloud metrics and what to watch on a serverless microservice — queue depth (the scaling signal for a queue-driven function), function errors/throttles, store throttles; the techniques to monitor in a cloud environment.
- **C2 — Scaling alarms & alerts.** Set up metrics and a scaling-relevant alarm to the design specification — a threshold that triggers and a notification — and the methods to create alerts.

---

## 1. UoC mapping

| UoC item | Descriptor | Component |
|---|---|---|
| `[ICTCLD503 PC 4.1]` | Set up metrics and trigger scaling alarms according to design specifications | C1, C2 |
| `[ICTCLD501 KE 6]` | Techniques and methods to monitor and create alerts in cloud environments | C1, C2 |

> Taught here; formally **evidenced** in AT2 §4.5 (the configured metric + alarm). `[ICTCLD501 KE 6]` is the monitoring/alerting knowledge that also underpins the DR plan's detection step (AT1 Topic 4) — taught here in its practical form.

---

## 2. AT2 alignment

| AT2 element | Criterion | How Topic 9 aligns |
|---|---|---|
| **§4.5 — Monitoring and alarms** | D6 | Direct — configure a metric + a scaling-relevant alarm with threshold and notification on the microservice (C1, C2). |
| **§6.5 — alarm test** | D9 | Drive the metric past the threshold and confirm the alarm fires (C2). |

**Practice-activity alignment:** `teach → demo → practice` — configure a queue-depth (or function-error) alarm with a notification on the practice microservice, then drive it to ALARM and back.

---

## Out of scope for this Topic (covered elsewhere)

- **The microservice build** the monitoring sits on → Topic 8.
- **The DR plan's detection/alerting concept** (planning depth) → AT1 Topic 4; here it's the practical CloudWatch configuration.
- **Documentation/sign-off** → Topic 10.

---

## Coverage checklist

- [ ] Both UoC items in §1 are taught.
- [ ] Each of C1–C2 has teaching content (AWS deck reference and/or bespoke).
- [ ] A `[DEMO]` precedes the practice (configure + fire an alarm).
- [ ] The exercise configures a real metric + alarm with notification and tests it.
- [ ] A student leaving this Topic could attempt AT2 §4.5.
