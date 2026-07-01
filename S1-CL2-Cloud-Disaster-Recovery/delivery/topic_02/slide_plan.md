# Topic 02 Microservice & serverless design — Slide plan
> **Covers:** Topic 02 — see coverage.md
> **Subtitle:** Design the serverless audit-log microservice and its integration contract
> **STATUS: DRAFT** (authored 2026-07-01).

## Depth ceiling
DESIGN — design the serverless audit-log microservice (services, data transactions, architecture, contract) on paper. No implementation; the deploy/build is AT2 (Topic 8).

## Teaching source
AWS serverless decks (functions, API gateway, managed datastore, messaging/queuing, event routing) pinned at Step 4 (TBD); bespoke for the audit-log microservice, the residency framing, and the webhook integration contract.

## AWS pin table
TBD — AWS serverless modules (Lambda, API Gateway, DynamoDB, SQS/SNS, event routing) to be pinned.

## Slides

### Opener
- [BESPOKE] From web-scale to the microservice
  - Topic 1 designed the web-scale site; Topic 2 designs the serverless audit-log microservice that plugs into it.
  - The microservice records India-cohort access events to a residency-compliant store — the localisation hook from the requirements.
  - Serverless: no servers to manage, event-driven, scales with demand — you pay per request.
  - Design only, to the supplied requirements — the build is AT2 (Topic 8).
  image: gen flat vector hero illustration of event messages flowing through serverless functions into a datastore, blue and gold accents, minimal, no text

### C1 — Microservices & data transactions
- Teaches: [ICTCLD503 PC 2.1]
- Kicker: one service, one job, one record
- [PRIMER] What a microservice is
  - A microservice does one thing well — a small, independently deployable unit with a single responsibility.
  - It owns its data and exposes a narrow interface; other systems talk to it only through that contract.
  - Right-sized: big enough to be useful, small enough to reason about and scale on its own.
  image: none
- [BESPOKE] The audit-log microservice
  - The one job: capture each India-cohort access/enquiry event the website emits and record it durably.
  - The website is the event producer; it knows only the webhook contract, not the store behind it.
  - Residency: India-cohort access logs land in an India-resident store (ap-south-1) per the requirements.
  image: none
- [BESPOKE] Its data transactions
  - One transaction: append an access event (who / what / when) — write-once, never updated.
  - Append-only means idempotent writes and simple, high-scale reads for audit retrieval.
  - Identify each transaction by the business need it meets — here, the CERT-In access-log obligation.
  image: none
- [EX] Identify the microservice & transactions
  - For the practice scenario, identify the microservice(s) and the data transaction(s) each handles.
  - State the business need each transaction meets.
  timer: ~20 min
  image: none

### C2 — Supporting cloud services
- Teaches: [ICTCLD503 PC 2.2]
- Kicker: pick the serverless building blocks
- [PRIMER] The serverless building blocks
  - Compute: a function service runs your code on demand, no servers to manage (e.g. AWS Lambda).
  - Front door: an API gateway receives requests and routes them to the function.
  - Messaging / queuing: a queue or topic buffers events and decouples producer from consumer.
  - Persistence: a managed datastore keeps the data without you running a database server.
  image: none
- [BESPOKE] Choosing services for the audit log
  - Ingress: an API gateway receives the website's webhook over HTTPS.
  - Buffer: a queue absorbs bursts and decouples the site from the logger (loose coupling).
  - Compute: a function validates and writes each event.
  - Store: a managed NoSQL datastore holds the append-only log, resident in India.
  image: none
- [EX] Determine the supporting services
  - For the practice scenario, determine the cloud services that support your microservice.
  - Justify each choice against a requirement (scale, residency, decoupling).
  timer: ~20 min
  image: none

### C3 — Microservice architecture & contract
- Teaches: [ICTCLD503 PC 2.3] · [ICTCLD503 PE 2] · [ICTCLD503 KE 4]
- Kicker: cohesive, loosely coupled, contract-first
- [PRIMER] Cohesion, coupling & the datastore
  - High cohesion: everything in the service serves its one job.
  - Loose coupling: the queue between producer and consumer means neither breaks the other.
  - Persistent datastore: the record survives independently of the compute that wrote it.
  image: none
- [BESPOKE] The target architecture
  - Flow: website webhook -> API gateway -> queue -> function -> NoSQL datastore.
  - The website knows only the webhook; each stage is independently scalable and replaceable.
  - The store sits in the India region (ap-south-1) so the access logs are resident by construction.
  image: diagram microservice-arch
- [BESPOKE] The integration contract
  - Define the webhook payload contract: the fields the website sends and what each means.
  - Version it and validate it — producer and consumer agree on this and nothing else.
  - A clear contract is what lets the two sides evolve independently.
  image: none
- [EX] Design the architecture & contract
  - For the practice scenario, design the microservice architecture (cohesive, loosely coupled, persistent, API / messaging).
  - Define the webhook integration contract.
  timer: ~30 min
  image: none
- [TAKEAWAYS] Topic 2 · Key takeaways
  - A microservice does one job, owns its data, and exposes a narrow contract.
  - Serverless building blocks: API gateway, queue / topic, function, managed datastore.
  - Design for high cohesion and loose coupling; the queue decouples producer from consumer.
  - Contract-first: the webhook payload contract is what keeps the two sides independent.
  image: none

### Close
- [BESPOKE] Next: Topic 3 — DR requirements
  - You've designed the web-scale site (Topic 1) and the microservice (Topic 2) — Part A's build strands.
  - Next you turn to disaster recovery: the requirements, impact analysis, strategy and plan.
  image: none

## Build notes
~16 slides. Exercises run on the practice scenario (design only). One generated architecture diagram (`diagram microservice-arch`); one decorative `gen` image (opener hero).

## Changelog
- 2026-07-01 — authored to full content.
