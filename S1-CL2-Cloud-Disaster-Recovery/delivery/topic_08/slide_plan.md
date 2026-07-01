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

### C1 — Review the design & code
- Teaches: [ICTCLD503 PC 3.1]
- Kicker: read before you deploy
- [BESPOKE] Review the design & supplied code
  - Review the microservice design from AT1 (services chosen, the flow, the contract).
  - Review the supplied code components and the webhook contract they implement before deployment.
  - Know what each piece does and how it wires up — deployment is assembling, not inventing.
  image: none

### C2 — Deploy & configure
- Teaches: [ICTCLD503 PC 3.2] · [ICTCLD503 PE 3] · [ICTCLD503 PE 4]
- Kicker: wire the pipeline end to end
- [PRIMER] The serverless wiring
  - API route: the gateway receives the webhook and hands it on.
  - The queue is the function's event source — it triggers the function as events arrive.
  - The function writes to the provided store; the store's table name is supplied to the function as config.
  image: none
- [BESPOKE] Deploy & configure the services
  - Deploy and configure the serverless services to implement the application, from the provided code.
  - Pass `LabRole` as the execution role; wire the API → queue → function → store.
  - Use the console, CLI or SDK to deploy and confirm (PE 4).
  image: diagram microservice-deploy
- [DEMO] Deploy the microservice
  - Deploy the API/queue/function from the supplied code in the lab (us-east-1), wired to the provided store.
  - Confirm each resource and the event-source mapping.
  source: recorded/live demo
  image: none
- [EX] Deploy & configure
  - On the practice scenario, deploy the practice microservice from the supplied code and wire it to the practice store.
  - Deploy to us-east-1; confirm the pipeline stands up.
  timer: ~30 min
  image: none

### C3 — Test & confirm functioning
- Teaches: [ICTCLD503 PC 3.3] · [ICTCLD503 KE 5]
- Kicker: post an event, find the record
- [BESPOKE] Test the microservice
  - Post sample events to the contract; confirm each is persisted exactly once in the data store.
  - Confirm an invalid event is rejected — the validation works, not just the happy path.
  - Testing/debugging technique: assert the observable outcome (the record), not just a 200 response (KE 5).
  image: none
- [DEMO] Post events & confirm records
  - Post a valid event → find the item in the store; post an invalid event → confirm it is rejected.
  source: recorded/live demo
  image: none
- [EX] Test & confirm
  - On the practice scenario, post sample events and confirm each is recorded exactly once; confirm an invalid event is rejected.
  timer: ~20 min
  image: none

### C4 — Troubleshoot
- Teaches: [ICTCLD503 PC 3.4] · [ICTCLD503 KE 5]
- Kicker: the logs tell you why
- [BESPOKE] Diagnose from the logs
  - Troubleshoot and fix microservice errors: a permission error, a payload-validation bug, a mis-wired event source.
  - Read the function logs and the queue/dead-letter behaviour — the failure is recorded, find it (KE 5).
  - Fix, redeploy, re-test — confirm the record now writes.
  image: none
- [EX] Troubleshoot the microservice
  - On the practice scenario, diagnose a seeded fault from the logs, fix it, redeploy, and confirm the event records.
  timer: ~20 min
  image: none
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
