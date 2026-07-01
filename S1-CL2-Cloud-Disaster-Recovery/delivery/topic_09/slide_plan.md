# Topic 09 Monitoring & alarms — Slide plan
> **Covers:** Topic 09 — see coverage.md
> **Subtitle:** Make the running microservice observable — a metric and a scaling-relevant alarm
> **STATUS: DRAFT** (authored 2026-07-01).

## Depth ceiling
BUILD — configure monitoring on the running microservice from Topic 8. `teach → demo → practice`. Deploys/configures in the lab (us-east-1, substituted).

## Teaching source
AWS ACA CloudWatch decks pinned at Step 4 (TBD); bespoke for what to watch on the serverless microservice and the alarm-to-spec discipline.

## AWS pin table
TBD — AWS ACA CloudWatch metrics/alarms modules to be pinned.

## Slides

### Opener
- [BESPOKE] Make it observable
  - The microservice runs (Topic 8); now you make it observable so you can see trouble coming.
  - This is the practical form of the DR plan's detection step (AT1 Topic 4) — the real CloudWatch config.
  - `teach → demo → practice`: watch a metric + alarm configured and fired, then do it yourself.
  - Configured in the lab (us-east-1); the metrics and alarms are the same anywhere.
  image: gen flat vector hero illustration of a monitoring dashboard with a metric line crossing an alarm threshold, blue and amber accents, minimal, no text

### C1 — Metrics & monitoring
- Teaches: [ICTCLD503 PC 4.1] · [ICTCLD501 KE 6]
- Kicker: watch the right signals
- [PRIMER] Cloud metrics
  - A metric is a time-series number the platform emits about a resource.
  - Monitoring watches the metrics that predict trouble, before users feel it (KE 6).
  - You cannot manage what you do not measure.
  image: none
- [BESPOKE] What to watch on the microservice
  - Queue depth: the scaling signal for a queue-driven function — a rising backlog means the consumer can't keep up.
  - Function errors and throttles: the code failing, or the platform limiting concurrency.
  - Store throttles: the datastore rejecting writes under load.
  - These are the techniques to monitor a serverless service in the cloud.
  image: none

### C2 — Scaling alarms & alerts
- Teaches: [ICTCLD503 PC 4.1] · [ICTCLD501 KE 6]
- Kicker: a threshold that tells someone
- [BESPOKE] Set an alarm to the design spec
  - Set up a metric and a scaling-relevant alarm to the design specification — a threshold that triggers.
  - Attach a notification so a person or system is alerted when it fires (the alert method).
  - Alarm to the spec, not to a guess — the threshold traces to the design's target.
  image: none
- [DEMO] Configure & fire an alarm
  - Configure a queue-depth (or function-error) alarm with a notification in the lab.
  - Drive the metric past the threshold; watch it go to ALARM and send the notification, then back to OK.
  source: recorded/live demo
  image: none
- [EX] Configure & test an alarm
  - On the practice microservice, configure a metric + a scaling-relevant alarm with a notification.
  - Drive it to ALARM and back; confirm the notification fired.
  timer: ~25 min
  image: none
- [TAKEAWAYS] Topic 9 · Key takeaways
  - Metrics are the signals; monitor the ones that predict trouble on a serverless service.
  - Watch queue depth (scaling signal), function errors/throttles, and store throttles.
  - Set an alarm to the design spec: a threshold that triggers plus a notification.
  - Test it — drive the metric past the threshold and confirm the alarm and alert fire.
  image: none

### Close
- [BESPOKE] Next: Topic 10 — document & close out
  - The build is complete and observable; next you document it, hand it over and get sign-off.
  - You package Topics 6–9 into the Deployment Report and its KE appendix.
  image: none

## Build notes
~11 slides. `teach → demo → practice` on the practice microservice in us-east-1 (substituted). One decorative `gen` image (opener hero); one DEMO (configure + fire an alarm).

## Changelog
- 2026-07-01 — authored to full content.
