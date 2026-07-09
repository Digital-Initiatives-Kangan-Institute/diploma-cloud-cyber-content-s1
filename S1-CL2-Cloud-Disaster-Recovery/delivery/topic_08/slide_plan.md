# Topic 08 Building & deploying the serverless microservice — Slide plan
> **Covers:** Topic 08 — see coverage.md
> **Subtitle:** Provision the serverless audit-log microservice from the supplied code, wire it to the store, and confirm it records
> **STATUS: DRAFT** (authored 2026-07-01).

## Depth ceiling
BUILD — where Topics 6–7 (IaC) converge with the serverless services: your *own* template (Topic 7 skill) provisions the microservice, from the *provided* code, writing to the *provided* store (Topic 6). `teach → demo → practice`. Deploys in the lab (us-east-1, substituted).

## Teaching source
AWS ACA serverless-deploy decks pinned at Step 4 (TBD); bespoke for wiring the provided code + contract to the store, and the test/troubleshoot discipline.

## AWS pin table
TBD — AWS ACA serverless (Lambda / API Gateway / SQS / DynamoDB) deploy modules to be pinned.

## Slides

### Opener
- [BESPOKE] Build the microservice
  - This Topic converges the strands: your template (Topic 7) provisions the microservice, from the provided code, writing to the provided store (Topic 6).
  - It realises the AT1 microservice design (Topic 2): API gateway → queue → function → NoSQL store.
  - The design places the store in India (ap-south-1); in the lab you deploy to us-east-1 — `[scenario: ap-south-1 (India) | deploy: us-east-1]`.
  - The lab's `LabRole` serves as both the function's execution role and the API-GW→queue credentials.
  image: gen flat vector hero illustration of a serverless event pipeline from an API into a datastore, blue and gold accents, minimal, no text
  notes:
    Frame this Topic as the convergence point of AT2 — the strands from Topics 6–8 come together into
    one deployed thing. Set the mode; don't teach the wiring yet.
    • First bullet: name the three strands they already hold — their OWN template (Topic 7 skill), the
    PROVIDED code, and the PROVIDED store (Topic 6). Today those three assemble into a running
    microservice. Deployment is assembling parts they understand, not inventing.
    • Second bullet: this realises the microservice they DESIGNED in AT1 (Topic 2) — API gateway → queue
    → function → NoSQL store. Point back to that design; today the paper design becomes real.
    • Third bullet (the substitution): the design places the store in India (ap-south-1) for the
    scenario's reasons; in the lab they deploy to us-east-1 — `[scenario: ap-south-1 (India) | deploy:
    us-east-1]`. Say it out loud — same build, only the location label changes.
    • Fourth bullet: in the Learner Lab the provided `LabRole` is BOTH the function's execution role and
    the API-GW→queue credentials — they don't create roles, they pass LabRole. Flag it now so nobody
    goes hunting for IAM to build.
    Misconception to pre-empt: "deploying means writing the service." No — the code is supplied; their
    job is to provision and wire it correctly. The skill is faithful assembly + confirming it works.
    Question to pose: "You designed this pipeline in AT1 — name the four pieces in order and what passes
    between them." (API gateway → queue → function → store; draws out the flow before they build it.)
    UoC/AT2 tie: opens the ICTCLD503 build arc (PC 3.1–3.4); everything today is evidenced in AT2 §4.4 —
    the deployed, tested microservice (criterion D4).

### C1 — Review the design & code
- Teaches: [ICTCLD503 PC 3.1]
- Kicker: read before you deploy
- [BESPOKE] Review the design & supplied code
  - Review the microservice design from AT1 (services chosen, the flow, the contract).
  - Review the supplied code components and the webhook contract they implement before deployment.
  - Know what each piece does and how it wires up — deployment is assembling, not inventing.
  image: none
  notes:
    Teach the discipline that must come BEFORE any console work — review the design and the supplied
    code so deployment is informed assembly. Short slide, firm point.
    • First bullet: review the microservice design from AT1 — the services chosen, the flow, the contract
    the webhook implements. They wrote this design; make them re-read it as the build spec.
    • Second bullet: review the SUPPLIED code components and the webhook contract they implement before
    deploying. Know what each component expects (its event shape, its config) so you wire it right.
    • Third bullet (the point): deployment is ASSEMBLING, not inventing. If they know what each piece does
    and how it connects, the deploy is mechanical; if they skip the review, they wire it blind.
    Misconception to pre-empt: "the code is given, so I can just deploy it and read it later." No —
    deploying code you haven't read is how you get a mis-wired event source you can't diagnose. Read first.
    Question to pose: "The function needs to know which table to write to — where does that come from, the
    code or the deployment config?" (config — sets up the C2 wiring, and why review matters).
    UoC/AT2 tie: ICTCLD503 PC 3.1 (review microservice design and code components) → AT2 §4.4 (D4); the
    review is the first assessed step of the build.

### C2 — Deploy & configure
- Teaches: [ICTCLD503 PC 3.2] · [ICTCLD503 PE 3] · [ICTCLD503 PE 4]
- Kicker: wire the pipeline end to end
- [PRIMER] The serverless wiring
  - API route: the gateway receives the webhook and hands it on.
  - The queue is the function's event source — it triggers the function as events arrive.
  - The function writes to the provided store; the store's table name is supplied to the function as config.
  image: none
  notes:
    A vendor-neutral primer on how the pieces connect — teach the event-driven wiring pattern before the
    AWS specifics. This is the mental model for the whole deploy.
    • First bullet: the API route — the gateway receives the webhook and hands it on. It's the front door;
    it doesn't process, it accepts and forwards.
    • Second bullet (the key idea): the queue is the function's EVENT SOURCE — the function is triggered as
    events arrive on the queue, not called directly. This decoupling is what makes it resilient and
    scalable; stress it, because students expect a direct API→function call.
    • Third bullet: the function writes to the provided store; the store's TABLE NAME is handed to the
    function as config (not hard-coded). Connect back to C1's review point.
    Misconception to pre-empt: "the API calls the function directly." No — the queue sits between them as
    the event source; that buffer is deliberate (absorbs bursts, retries failures). Draw the four boxes.
    Question to pose: "Why put a queue between the API and the function instead of calling the function
    straight from the API?" (decouples producer from consumer; buffers bursts; enables retry/DLQ — the
    scaling signal they'll monitor in Topic 9).
    UoC/AT2 tie: ICTCLD503 PC 3.2 + PE 3 — the wiring model they must implement; evidenced in AT2 §4.4 (D4).
- [BESPOKE] Deploy & configure the services
  - Deploy and configure the serverless services to implement the application, from the provided code.
  - Pass `LabRole` as the execution role; wire the API → queue → function → store.
  - Use the console, CLI or SDK to deploy and confirm (PE 4).
  image: diagram microservice-deploy
  notes:
    The concrete AWS deploy, off the wiring diagram — turn the primer's pattern into the actual services.
    Walk it against the `microservice-deploy` diagram on screen.
    • First bullet: deploy and configure the serverless services to implement the application FROM THE
    PROVIDED CODE — API, queue, function, store, in the lab.
    • Second bullet: pass `LabRole` as the execution role, and wire API → queue → function → store. This
    is the Learner Lab substitution for building IAM roles — say it plainly so nobody builds a role.
    • Third bullet: they may use the console, CLI or SDK to deploy and confirm (PE 4 — the tooling
    evidence). Any of the three is fine; what's assessed is that it stands up and they can show it.
    Misconception to pre-empt: "I need to create an execution role for the function." No — in the lab you
    pass the provided `LabRole`; creating IAM is out of scope here and just costs them time.
    Question to pose: "What's the ONE thing you must configure so the function fires when an event lands on
    the queue?" (the event-source mapping between queue and function — the piece students forget).
    UoC/AT2 tie: ICTCLD503 PC 3.2 + PE 3 (deploy/configure the services) + PE 4 (console/CLI/SDK) → AT2
    §4.4 (D4); this is the core build step.
- [DEMO] Deploy the microservice
  - Deploy the API/queue/function from the supplied code in the lab (us-east-1), wired to the provided store.
  - Confirm each resource and the event-source mapping.
  source: recorded/live demo
  image: none
  notes:
    LIVE DEMONSTRATION (educator-led against the lab-pack — screen your own deploy of the course's
    microservice; there is no recorded demo for this). Show it end to end, then they replicate on the
    practice scenario next.

    WHAT TO DEMONSTRATE (step by step, in the lab, us-east-1):
    1. Deploy the API, queue and function from the SUPPLIED code — provision the resources.
    2. Pass `LabRole` as the execution role; do NOT create a role.
    3. Wire the event-source mapping so the queue triggers the function; point it at the provided store.
    4. Confirm each resource exists and the event-source mapping is enabled.

    WHAT TO EMPHASISE:
    • Say the substitution out loud — `[scenario: ap-south-1 (India) | deploy: us-east-1]` — as you set
    the Region.
    • The event-source mapping is the make-or-break wiring step — show where it lives and that it's ON.
    • This is assembling supplied parts, not writing code — narrate that mindset as you go.

    PREP: clean Learner Lab open with `LabRole` available; the supplied microservice code + template to
    hand; the provided store already in place (Topic 6). ~8–10 min to screen + narrate before the activity.
- [EX] Deploy & configure
  - On the practice scenario, deploy the practice microservice from the supplied code and wire it to the practice store.
  - Deploy to us-east-1; confirm the pipeline stands up.
  timer: ~30 min
  image: none
  notes:
    Facilitation — the C2 practice; students deploy the practice microservice they just watched demoed.
    Tell students, in these words: "On the practice scenario, deploy the practice microservice from the
    supplied code and wire it to the practice store. Deploy to us-east-1, pass `LabRole`, and confirm the
    pipeline stands up."
    Steps (put on the board):
    1. Deploy the API, queue and function from the supplied practice code.
    2. Pass `LabRole` as the execution role; configure the event-source mapping (queue → function).
    3. Point the function at the practice store (its table name as config).
    4. Confirm each resource, and that the event-source mapping is enabled.
    Must produce: a stood-up pipeline in us-east-1 — API, queue, function and store all present and wired,
    ready to test in the next activity.
    Timing: ~30 min. Where they get stuck: the event-source mapping (a deployed function that never fires
    because nothing triggers it) and hunting for an IAM role instead of passing `LabRole` — circulate and
    check both.
    Share-back prompt: ask one student to show their event-source mapping is enabled and points queue → function.
    No-leakage note: the practice scenario is comparable-not-identical to the AT2 build — the assessed
    microservice is a different one. Keep them on the practice artefacts here.

### C3 — Test & confirm functioning
- Teaches: [ICTCLD503 PC 3.3] · [ICTCLD503 KE 5]
- Kicker: post an event, find the record
- [BESPOKE] Test the microservice
  - Post sample events to the contract; confirm each is persisted exactly once in the data store.
  - Confirm an invalid event is rejected — the validation works, not just the happy path.
  - Testing/debugging technique: assert the observable outcome (the record), not just a 200 response (KE 5).
  image: none
  notes:
    Teach testing as confirming the OBSERVABLE OUTCOME, not trusting a status code. This is the discipline
    that separates "it deployed" from "it works."
    • First bullet: post sample events to the contract and confirm each is persisted EXACTLY ONCE in the
    data store. Exactly-once matters — a duplicate is a bug even if nothing errored.
    • Second bullet: also post an INVALID event and confirm it is rejected — prove the validation works,
    not just the happy path. A service that accepts garbage is not done.
    • Third bullet (the technique, KE 5): assert the observable outcome — the RECORD in the store — not
    just a 200. A 200 says the API accepted it; only the record says the pipeline delivered it.
    Misconception to pre-empt: "I got a 200, so it works." No — the 200 is the API gateway accepting the
    event; the function runs asynchronously off the queue. Only the stored record proves end-to-end.
    Question to pose: "You post an event and get a 200 but find no record in the store — where did it get
    lost, and how would you know?" (somewhere queue→function→store; the record's absence is the signal —
    leads into troubleshooting, C4).
    UoC/AT2 tie: ICTCLD503 PC 3.3 + KE 5 (testing/debugging techniques) → AT2 §4.4 / §6 (D5).
- [DEMO] Post events & confirm records
  - Post a valid event → find the item in the store; post an invalid event → confirm it is rejected.
  source: recorded/live demo
  image: none
  notes:
    LIVE DEMONSTRATION (educator-led — screen it live against your deployed microservice; no recorded
    demo for this). Show both paths, then they replicate on the practice scenario.

    WHAT TO DEMONSTRATE (in the lab):
    1. Post a VALID event to the contract → go to the store and find the item written (exactly once).
    2. Post an INVALID event → confirm it is REJECTED and no bad record is written.
    3. Show WHERE you look — the store item, not just the API response.

    WHAT TO EMPHASISE:
    • The 200 is not the proof — walk from the API response THROUGH to the stored record every time.
    • Show the exactly-once check: one post, one item (not zero, not two).
    • Contrast the two paths side by side — valid persists, invalid is turned away — so students see the
    validation is real.

    PREP: the microservice from the previous demo deployed and running; a valid and an invalid sample
    event ready to post; the store open in another tab. ~6–8 min to screen before the activity.
- [EX] Test & confirm
  - On the practice scenario, post sample events and confirm each is recorded exactly once; confirm an invalid event is rejected.
  timer: ~20 min
  image: none
  notes:
    Facilitation — the C3 practice; students test the pipeline they deployed in the C2 activity.
    Tell students, in these words: "On the practice scenario, post sample events and confirm each is
    recorded exactly once in the store; then post an invalid event and confirm it is rejected."
    Steps (put on the board):
    1. Post a valid event to the contract; find the item in the store — confirm exactly one record.
    2. Repeat with a second valid event; confirm a second distinct record (no duplicates, no misses).
    3. Post an invalid event; confirm it is rejected and no record is written.
    Must produce: evidence that valid events persist exactly once and invalid events are rejected — the
    functional-test result for their pipeline.
    Timing: ~20 min. Where they get stuck: they check the 200 and stop — push them to open the store and
    verify the RECORD; and a "missing" record that's actually a wiring fault, which sets up C4.
    Share-back prompt: "Who had an event that returned 200 but never reached the store?" — surface it as
    the bridge into troubleshooting.
    No-leakage note: the practice scenario is comparable-not-identical to the AT2 build; keep them on the
    practice microservice here.

### C4 — Troubleshoot
- Teaches: [ICTCLD503 PC 3.4] · [ICTCLD503 KE 5]
- Kicker: the logs tell you why
- [BESPOKE] Diagnose from the logs
  - Troubleshoot and fix microservice errors: a permission error, a payload-validation bug, a mis-wired event source.
  - Read the function logs and the queue/dead-letter behaviour — the failure is recorded, find it (KE 5).
  - Fix, redeploy, re-test — confirm the record now writes.
  image: none
  notes:
    Teach troubleshooting as a log-driven procedure — the failure is recorded somewhere; the skill is
    reading it, not guessing. Frame it as read → diagnose → fix → redeploy → re-test.
    • First bullet: the faults they'll meet — a permission error, a payload-validation bug, a mis-wired
    event source. Name the categories so they know the shape of what they're hunting.
    • Second bullet (the technique): read the FUNCTION LOGS and the queue/dead-letter behaviour — the
    failure is recorded, find it (KE 5). A message stuck on a dead-letter queue is telling you something.
    • Third bullet: fix, redeploy, re-test — confirm the record now writes. The loop isn't done until the
    observable outcome is restored (ties back to C3's testing discipline).
    Misconception to pre-empt: "if it didn't work I'll just redeploy and hope." No — read the log first;
    blind redeploys fix nothing and burn the lab clock. The log names the cause.
    Question to pose: "The function runs but nothing lands in the store, and the logs show access-denied —
    what's the likely cause?" (a permissions/wiring issue — LabRole or the event-source mapping; reason
    from the log to the fix).
    UoC/AT2 tie: ICTCLD503 PC 3.4 (troubleshoot and fix errors) + KE 5 → AT2 §6 troubleshooting log (D9).
- [EX] Troubleshoot the microservice
  - On the practice scenario, diagnose a seeded fault from the logs, fix it, redeploy, and confirm the event records.
  timer: ~20 min
  image: none
  notes:
    Facilitation — the C4 practice; students diagnose a SEEDED fault, so everyone practises reading logs
    (not just those who happened to break something).
    Tell students, in these words: "On the practice scenario, a fault has been introduced. Diagnose it
    from the logs, fix it, redeploy, and confirm the event records."
    Steps (put on the board):
    1. Post an event — observe that no record is written (or an error surfaces).
    2. Read the function logs and the queue/dead-letter behaviour — find where and why it fails.
    3. Fix the cause, redeploy, and re-test — confirm the record now writes.
    Must produce: a short diagnosis (what the log showed, what the cause was, what you changed) plus a
    passing re-test — this is the troubleshooting-log evidence AT2 wants.
    Timing: ~20 min. Where they get stuck: they try to fix before reading the log — hold them at the log
    until they can NAME the cause; and they fix but forget to redeploy before re-testing.
    Share-back prompt: take one seeded fault and have a student walk log → cause → fix out loud.
    No-leakage note: the practice scenario is comparable-not-identical to the AT2 build; keep them on the
    practice microservice here.
- [TAKEAWAYS] Topic 8 · Key takeaways
  - Deployment assembles a design: review the design + supplied code before you build.
  - Wire API → queue (event source) → function → store; `LabRole` is the execution role.
  - Test by the observable outcome — the record is written exactly once; invalid events are rejected.
  - Troubleshoot from the logs: read, diagnose, fix, redeploy, re-test.
  image: none

### Close
- [BESPOKE] Next: Topic 9 — monitoring
  - The microservice and the web-scale build are running; next you make them observable.
  - You add the monitoring that sits behind the DR plan's detection step.
  image: none

## Build notes
~16 slides. `teach → demo → practice` on the practice scenario in us-east-1 (substituted); `LabRole` execution role. One generated diagram (`diagram microservice-deploy`); one decorative `gen` image (opener hero); two DEMOs (deploy, test).

## Changelog
- 2026-07-01 — authored to full content.
