# Topic 08 Monitoring & alarms — Slide plan
> **Covers:** Topic 08 — see coverage.md
> **Subtitle:** Make the running microservice observable — a metric and a scaling-relevant alarm
> **STATUS: DRAFT — redrafted 2026-09-08 from the AT2 practice workbook, task 19. Renumbered from the
> old Topic 09 (the old Topics 7–8 merged).**

## Depth ceiling
BUILD — configure monitoring on the microservice built in Topic 7: one task, done properly — a metric
that means something and an alarm that provably fires. Small Topic by design.

**Answer discipline:** activities run on the practice microservice; the assessment monitors a
different build. Teach the method; the metric choice and threshold are the student's own.

## Teaching source
AWS ACA CloudWatch decks pinned at Step 4 (TBD); bespoke for what to watch on a serverless service and
the alarm-to-spec discipline.

## AWS pin table
TBD — AWS ACA CloudWatch metrics/alarms modules to be pinned.

## Slides

### Opener
- [BESPOKE] Make it observable
  - The microservice runs; now you make it observable so you can see trouble coming.
  - This is the practical form of the DR plan's detection step from Topic 4 — the paper promise becomes real configuration.
  - One workbook task today, done properly: a metric that means something, and an alarm that provably fires.
  image: gen flat vector hero illustration of a monitoring dashboard with a metric line crossing an alarm threshold, blue and amber accents, minimal, no text
  notes:
    The pivot from "it runs" to "you can see it running" — workbook task 19.
    Tie back to Topic 4's detection step: a system you can't observe can't meet its own recovery objectives.

### C1 — Metrics, and what to watch
- Teaches: [ICTCLD503 PC 4.1] · [ICTCLD501 KE 6]
- Kicker: watch the right signals
- [PRIMER] Cloud metrics
  - A metric is a time-series number the platform emits about a resource.
  - Monitoring watches the metrics that predict trouble, before users feel it.
  - You cannot manage what you do not measure.
  image: none
  notes:
    Foundation slide. The art is choosing the few leading signals, not building a dashboard wall.
    A useful metric moves before the failure — a rising queue, not a user complaint.
- [BESPOKE] What to watch on the microservice
  - Queue depth: the scaling signal for a queue-driven function — a rising backlog means the consumer can't keep up.
  - Function errors and throttles: the code failing, or the platform limiting concurrency.
  - Store throttles: the datastore pushing back under load.
  image: none
  notes:
    The primer made concrete for their pipeline. No server CPU to watch — the serverless signals differ from a VM's.
    Queue depth is the headline: it predicts overload, which makes it the natural alarm candidate.
- [TAKEAWAYS] Section 1 · The signals
  - Metrics are time-series signals; pick the leading ones.
  - Queue depth, function errors and throttles, store throttles.
  image: none

### C2 — The alarm, set and proven
- Teaches: [ICTCLD503 PC 4.1] · [ICTCLD501 KE 6]
- Kicker: a threshold that tells someone
- [BESPOKE] Set an alarm to the design spec
  - A scaling-relevant alarm: a threshold on a meaningful metric, with a notification attached.
  - The threshold traces to a design target — "why that number?" has an answer from the spec, not a shrug.
  - An alarm nobody is told about is a light in an empty room; the notification is half the point.
  image: none
  notes:
    Workbook task 19's discipline: metric, threshold, notification — and the threshold defensible from the design.
    Round numbers plucked from the air are the thing to challenge.
- [DEMO] Configure and fire an alarm
  - Configure a queue-depth alarm with a notification, then drive the metric past the threshold.
  - Watch it go to alarm, see the notification arrive, and watch it recover.
  source: recorded/live demo
  image: none
  notes:
    Live demonstration, educator-led (screen it live — no recorded-demos catalogue in CL2).
    Say where the threshold number comes from as you type it.
    Show the full lifecycle: OK, alarm, notification, back to OK — a configured-but-never-fired alarm is untested.
    Prep: the microservice running, a way to flood the queue, the notification target visible. ~8–10 min.
- [EX] Set up the metric and the alarm
  - Workbook — task 19.
  - Set up the metric and the scaling-relevant alarm with a notification, drive it to alarm, and confirm the notification fired.
  timer: ~25 min
  image: none
  notes:
    Activity = practice workbook task 19.
    The two misses: an alarm configured but never fired, and a threshold they can't justify.
- [TAKEAWAYS] Topic 8 · Key takeaways
  - Monitor the signals that predict trouble on a serverless service.
  - Threshold from the spec, notification attached.
  - An untested alarm is not an alarm — fire it and prove it.
  image: none

### Close
- [BESPOKE] Next: Topic 9 — close out the build
  - The build is complete and observable.
  - Next you document it for the people who inherit it, take it down cleanly, and get it signed off.
  image: none
  notes:
    Everything captured during the build becomes the closeout material — remind them their notes matter.

## Build notes
~12 slides. One activity, mapping to practice workbook task 19. One decorative `gen` opener hero
(assets live in the old `topic_09/images/` — move on renumber); one DEMO (configure + fire).
Renumbered from the old Topic 09; content carried, notes trimmed.

## Changelog
- 2026-09-08 — redrafted from the AT2 practice workbook (task 19); renumbered 09 → 08 after the
  Topics 7–8 merge.
- 2026-07-01 — authored to full content (as Topic 09).
