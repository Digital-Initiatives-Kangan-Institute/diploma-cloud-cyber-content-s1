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
  notes:
    Frame Topic 9 as the pivot from "it runs" to "you can SEE it running." Set the mode; don't configure
    an alarm yet.
    • First bullet: the microservice runs (Topic 8); now make it observable so you can see trouble coming
    before users feel it. Observability is a build step, not an afterthought.
    • Second bullet (the tie-back): this is the PRACTICAL form of the DR plan's detection step they
    designed in AT1 (Topic 4) — the paper "we'll detect failures" becomes real CloudWatch config today.
    Point back to that plan.
    • Third bullet: the rhythm — `teach → demo → practice`: watch a metric + alarm configured and fired,
    then do it themselves.
    • Fourth bullet: configured in the lab (us-east-1); the metrics and alarms are the same anywhere — no
    substitution caveat beyond the Region.
    Misconception to pre-empt: "monitoring is something ops bolts on later." No — the detection step of the
    DR plan REQUIRES it; a system you can't observe can't meet its own recovery objectives. It's the build.
    Question to pose: "Your AT1 DR plan says failures will be detected — concretely, what has to exist for
    that to be true?" (a metric being watched + an alarm that alerts someone; today builds exactly that).
    UoC/AT2 tie: opens the monitoring build — ICTCLD503 PC 4.1 + ICTCLD501 KE 6 — evidenced in AT2 §4.5 (D6).

### C1 — Metrics & monitoring
- Teaches: [ICTCLD503 PC 4.1] · [ICTCLD501 KE 6]
- Kicker: watch the right signals
- [PRIMER] Cloud metrics
  - A metric is a time-series number the platform emits about a resource.
  - Monitoring watches the metrics that predict trouble, before users feel it (KE 6).
  - You cannot manage what you do not measure.
  image: none
  notes:
    A vendor-neutral primer on what a metric IS, before naming the microservice's specific signals. Keep
    it foundational.
    • First bullet: a metric is a time-series number the platform emits about a resource — a queue length,
    an error count, a duration. It's data over time, not a snapshot.
    • Second bullet (KE 6): monitoring is watching the metrics that PREDICT trouble, before users feel it.
    The art is choosing the few signals that lead the problem, not lag it.
    • Third bullet (the motto): you cannot manage what you do not measure. Say it out loud — it's why the
    next slide picks specific signals.
    Misconception to pre-empt: "monitor everything." No — a wall of dashboards nobody reads is not
    monitoring; you pick the leading signals for THIS service. Selection is the skill.
    Question to pose: "What makes a metric useful for prevention rather than a post-mortem?" (it moves
    BEFORE the failure — a leading signal like a rising queue, not a lagging one like a user complaint).
    UoC/AT2 tie: ICTCLD503 PC 4.1 + ICTCLD501 KE 6 — the monitoring foundation evidenced in AT2 §4.5 (D6).
- [BESPOKE] What to watch on the microservice
  - Queue depth: the scaling signal for a queue-driven function — a rising backlog means the consumer can't keep up.
  - Function errors and throttles: the code failing, or the platform limiting concurrency.
  - Store throttles: the datastore rejecting writes under load.
  - These are the techniques to monitor a serverless service in the cloud.
  image: none
  notes:
    Make the primer concrete — the specific signals that matter on THIS queue-driven serverless
    microservice. These are the ones they'll choose from for the alarm.
    • Queue depth: the scaling signal for a queue-driven function — a rising backlog means the consumer
    (the function) can't keep up with arrivals. This is the headline metric; it predicts overload.
    • Function errors and throttles: the code failing (errors) or the platform limiting concurrency
    (throttles). Distinguish the two — an error is your bug; a throttle is a capacity limit.
    • Store throttles: the datastore rejecting writes under load — the pipeline's far end pushing back.
    • Together these are the techniques to monitor a serverless service (KE 6) — pick the leading one.
    Misconception to pre-empt: "watch CPU like a server." No — serverless has no server CPU to watch; the
    meaningful signals are queue depth, function errors/throttles, store throttles. The metrics differ from a VM.
    Question to pose: "Which single metric best tells you the microservice is falling behind under load?"
    (queue depth — a growing backlog is the scaling signal; sets up the alarm spec next).
    UoC/AT2 tie: ICTCLD503 PC 4.1 (set up metrics) + KE 6 → AT2 §4.5 (D6); queue depth is the natural
    scaling-relevant metric to alarm on.

### C2 — Scaling alarms & alerts
- Teaches: [ICTCLD503 PC 4.1] · [ICTCLD501 KE 6]
- Kicker: a threshold that tells someone
- [BESPOKE] Set an alarm to the design spec
  - Set up a metric and a scaling-relevant alarm to the design specification — a threshold that triggers.
  - Attach a notification so a person or system is alerted when it fires (the alert method).
  - Alarm to the spec, not to a guess — the threshold traces to the design's target.
  image: none
  notes:
    Teach the discipline that the alarm THRESHOLD must trace to the design, not be plucked from the air.
    This is where monitoring meets the DR plan's numbers.
    • First bullet: set up a metric and a scaling-relevant alarm to the DESIGN SPECIFICATION — a threshold
    that triggers when the signal crosses the line.
    • Second bullet: attach a NOTIFICATION so a person or system is alerted when it fires — the alert
    method (KE 6). An alarm nobody is told about is useless; the notification is half the point.
    • Third bullet (the point): alarm to the SPEC, not to a guess — the threshold traces back to the
    design's target (e.g. the throughput or RPO/RTO the DR plan committed to). Justify the number.
    Misconception to pre-empt: "pick a round number that looks reasonable." No — the threshold must trace
    to a design target; "why 100?" should be answerable from the design, not "it felt right."
    Question to pose: "Where does your alarm threshold come from — and could you defend the number to the
    client?" (from the design spec / DR targets; if you can't defend it, it's a guess).
    UoC/AT2 tie: ICTCLD503 PC 4.1 (trigger scaling alarms per design specs) + KE 6 → AT2 §4.5 (D6); the
    spec-traceable threshold is exactly what's assessed.
- [DEMO] Configure & fire an alarm
  - Configure a queue-depth (or function-error) alarm with a notification in the lab.
  - Drive the metric past the threshold; watch it go to ALARM and send the notification, then back to OK.
  source: recorded/live demo
  image: none
  notes:
    LIVE DEMONSTRATION (educator-led — screen it live in the lab; no recorded demo for this). Configure it
    AND fire it, then they replicate on the practice microservice.

    WHAT TO DEMONSTRATE (in the lab):
    1. Configure a queue-depth (or function-error) alarm on the running microservice, with a threshold.
    2. Attach a notification so an alert is sent when it fires.
    3. DRIVE the metric past the threshold (e.g. flood the queue) — watch the alarm go to ALARM and send
    the notification.
    4. Let it recover — watch it return to OK.

    WHAT TO EMPHASISE:
    • Say WHERE the threshold number comes from (the design spec) as you type it — model spec-traceable,
    not guessed.
    • Show the full lifecycle: OK → ALARM → notification → back to OK. A configured-but-never-fired alarm
    is untested.
    • Point out the notification actually arriving — the alert method is the assessed half.

    PREP: the microservice running (Topic 8 deploy); a way to drive the metric (a burst of events to grow
    queue depth); the notification target set up so it visibly fires. ~8–10 min to screen before the activity.
- [EX] Configure & test an alarm
  - On the practice microservice, configure a metric + a scaling-relevant alarm with a notification.
  - Drive it to ALARM and back; confirm the notification fired.
  timer: ~25 min
  image: none
  notes:
    Facilitation — the C2 practice; students configure AND test an alarm on their practice microservice.
    Tell students, in these words: "On the practice microservice, configure a metric and a
    scaling-relevant alarm with a notification. Then drive it to ALARM and back, and confirm the
    notification fired."
    Steps (put on the board):
    1. Choose a scaling-relevant metric (queue depth is the natural one) and set a threshold traceable to
    the design spec.
    2. Create the alarm and attach a notification.
    3. Drive the metric past the threshold — confirm it goes to ALARM and the notification fires.
    4. Let it recover — confirm it returns to OK.
    Must produce: a configured metric + alarm with a notification, and evidence it fired (ALARM state +
    notification) and recovered — the §4.5 / §6.5 evidence.
    Timing: ~25 min. Where they get stuck: configuring the alarm but never firing it (untested), and
    picking a threshold they can't justify — push them to trace the number to the spec.
    Share-back prompt: ask one student for their threshold and WHY that number (should trace to a design target).
    No-leakage note: the practice microservice is comparable-not-identical to the AT2 build; keep them on
    the practice service here.
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
