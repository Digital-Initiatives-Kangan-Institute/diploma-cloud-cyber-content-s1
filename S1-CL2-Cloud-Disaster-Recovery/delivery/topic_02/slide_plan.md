# Topic 02 Microservice & serverless design — Slide plan
> **Covers:** Topic 02 — see coverage.md
> **Subtitle:** Design the serverless microservice, its contract, and answer for the whole design
> **STATUS: DRAFT — redrafted 2026-09-08 from the AT1 Part A practice workbook, tasks 15–19 and the
> assessment's knowledge questions Q1–Q4.**

## Depth ceiling
DESIGN — the microservice half of AT1 Part A on the practice workbook: the service and its data, the
supporting services, the architecture and contract, the justification, and the Part A knowledge
questions. No implementation; the build is AT2.

**Answer discipline:** activities run on the practice workbook; the assessment is the same work on the
assessed system. Teach the method on the practice vehicle; never supply assessed-system answers.

## Teaching source
AWS serverless decks (functions, API gateway, managed datastore, messaging/queuing) pinned at Step 4
(TBD); bespoke for the audit-log microservice, the residency framing, and the webhook contract.

## AWS pin table
TBD — AWS serverless modules (Lambda, API Gateway, DynamoDB, SQS/SNS, event routing) to be pinned.

## Slides

### Opener
- [BESPOKE] From web-scale to the microservice
  - Topic 1 designed the web-scale platform; Topic 2 designs the small service that plugs into it.
  - The service records access events to a residency-compliant store — the localisation hook straight from the requirements.
  - Serverless: no servers to manage, event-driven, scales with demand, pay per request.
  - Design only — the build is AT2.
  image: gen flat vector hero illustration of event messages flowing through serverless functions into a datastore, blue and gold accents, minimal, no text
  notes:
    Second design half — today runs workbook tasks 15 to 19, then rehearses the Part A knowledge questions.
    Stress event-driven: the platform emits events, the service reacts.
    Misconception: serverless doesn't mean no servers — it means the operational responsibility isn't yours.

### C1 — The microservice and its data
- Teaches: [ICTCLD503 PC 2.1]
- Kicker: one service, one job, one record
- [PRIMER] What a microservice is
  - A microservice does one thing well — a small, independently deployable unit with a single responsibility.
  - It owns its data and exposes a narrow interface; other systems talk to it only through that contract.
  - Right-sized: big enough to be useful, small enough to reason about and scale on its own.
  image: none
  notes:
    The definition the whole Topic builds on — single responsibility is the test for whether something is its own service.
    If another system needs this service's data, it goes through the interface — never into the store directly.
- [BESPOKE] The audit-log microservice
  - The one job: capture each access event the platform emits and record it durably.
  - The platform is the event producer; it knows only the webhook contract, not the store behind it.
  - The residency obligation is why this service exists on its own — the log lands in a store the platform needn't host.
  image: none
  notes:
    Workbook task 15's subject made concrete. The service's reason to exist is the residency need.
    Question to pose: why build a separate service just to record events? (single job, independent scale, resident store).
- [BESPOKE] Its data transactions
  - One transaction: append an access event — who, what, when — written once and never updated.
  - Append-only buys idempotent writes and simple, high-scale reads.
  - A transaction exists because a business need demands it, not because it is technically possible.
  image: none
  notes:
    The data pattern defines the store's shape later. An audit log is immutable by nature — mutability would break its evidentiary value.
    Press transaction-to-need traceability; the workbook table asks for it.
- [EX] Identify the microservice and its transactions
  - Workbook — task 15.
  - Identify the microservice and the data it handles, and state the business need behind each transaction.
  timer: ~20 min
  image: none
  notes:
    Activity = practice workbook task 15.
    Watch for one big service that does everything — push single responsibility.
- [TAKEAWAYS] Section 1 · The service
  - One job, its own data, a narrow contract.
  - Append-only: written once, read at scale.
  - Every transaction traces to a business need.
  image: none

### C2 — The supporting services
- Teaches: [ICTCLD503 PC 2.2] · [ICTCLD503 KE 4]
- Kicker: pick the serverless building blocks
- [PRIMER] The serverless building blocks
  - Compute: a function service runs your code on demand, no servers to manage.
  - Front door: an API gateway receives requests and routes them to the function.
  - Messaging: a queue buffers events and decouples producer from consumer.
  - Persistence: a managed datastore keeps the data without you running a database server.
  image: none
  notes:
    The four building-block types, one per line — vendor-neutral, AWS named only as the example.
    Question to pose: which block lets the platform fire a thousand events a second when the logger writes two hundred? (the queue).
- [BESPOKE] Choosing services for the audit log
  - Ingress: an API gateway receives the webhook over HTTPS.
  - Buffer: a queue absorbs bursts and decouples the platform from the logger.
  - Compute: a function validates and writes each event — the only custom code in the service.
  - Store: a managed NoSQL datastore holds the append-only log, placed to honour residency.
  image: none
  notes:
    The selection decision made concrete — each block mapped to a job and a requirement.
    Misconception: relational by default. The access pattern (append-only, simple high-scale reads) and residency drive the choice.
- [EX] Determine the supporting services
  - Workbook — task 16.
  - Determine the cloud services that support your microservice, and justify each against a requirement.
  timer: ~20 min
  image: none
  notes:
    Activity = practice workbook task 16.
    Product names with no reason attached is the common miss — every choice names its requirement.
- [TAKEAWAYS] Section 2 · The services
  - Gateway, queue, function, managed store — each chosen for a named job.
  - The queue is the decoupling seam, not an optional extra.
  image: none

### C3 — The architecture, drawn, and its contract
- Teaches: [ICTCLD503 PC 2.3] · [ICTCLD503 PE 2] · [ICTCLD503 KE 4]
- Kicker: cohesive, loosely coupled, contract-first
- [PRIMER] Cohesion, coupling and the datastore
  - High cohesion: everything in the service serves its one job.
  - Loose coupling: the queue between producer and consumer means neither breaks the other.
  - Persistent datastore: the record survives independently of the compute that wrote it.
  image: none
  notes:
    Three examinable principles — cohesion is within a service, coupling is between services; you want high cohesion and loose coupling.
    The function runs for milliseconds then disappears; the datastore is why the record outlives it.
- [BESPOKE] The target architecture
  - The flow: webhook, then gateway, then queue, then function, then datastore.
  - The platform knows only the webhook; each stage is independently scalable and replaceable.
  - The store sits in the region the obligation names — resident by construction, not by policy.
  image: diagram microservice-arch
  notes:
    Trace the flow stage by stage; each stage delivers a principle from the previous slide.
    A worked example to adapt, not copy — workbook task 17 asks for their own drawing.
- [BESPOKE] The integration contract
  - Define the webhook payload: the fields the platform sends and what each means.
  - Version it and validate it — producer and consumer agree on this and nothing else.
  - A clear contract is what lets the two sides evolve independently.
  image: none
  notes:
    Workbook task 18's subject. Contract-first: it is defined before either side builds, not documented after.
    Question to pose: the platform team adds a field — how does versioning stop that breaking the logger?
- [EX] Draw the architecture and define the contract
  - Workbook — tasks 17 and 18.
  - Draw your microservice architecture, then define the webhook integration contract it hinges on.
  timer: ~30 min
  image: none
  notes:
    Activity = practice workbook tasks 17–18.
    The two common misses: redrawing the teaching diagram verbatim, and forgetting the queue seam.
- [TAKEAWAYS] Section 3 · Architecture and contract
  - Every stage independently scalable; the platform knows only the webhook.
  - Residency is where you put the box, not a policy you add later.
  - Contract-first keeps the two sides independent.
  image: none

### C4 — Justify it, and answer for it
- Teaches: [ICTCLD503 PC 2.4] · [ICTCLD503 KE 3] · [ICTCLD503 KE 4] · [ICTCLD503 KE 6] · [ICTCLD503 PE 5]
- Kicker: your design, your argument
- [BESPOKE] Justify the microservice design
  - For each choice: the requirement it serves, the option you took, and why that option over the alternative.
  - The strongest justification names what you did not choose and why the simpler option wins.
  - Someone holding the requirements should be able to tick your justification off line by line.
  image: none
  notes:
    Workbook task 19 — the written argument, same shape as the web-scale justification in Topic 1.
    "Because it is best practice" is not a justification; requirement, option, why.
- [BESPOKE] The knowledge questions ask about your own design
  - The Part A questions ask you to explain your component choices, your cohesion and coupling, the web-scaling principles you applied, and how the design keeps the residency option open.
  - Every answer cites your own design — the tables you filled in and the diagrams you drew are the material.
  - A definition with no reference to your design answers nothing.
  image: none
  notes:
    The assessment workbook carries Q1–Q4 at the end of Part A; the practice workbook carries none, so rehearse with the assessment's questions against the practice design.
    The failure mode is textbook definitions — push every answer back to their own tables and drawings.
- [EX] Justify the design and rehearse the questions
  - Workbook — task 19, then the assessment's Part A questions Q1 to Q4, answered from your practice design.
  - Justify the microservice design in writing, then answer the four knowledge questions citing your own choices.
  timer: ~30 min
  image: none
  notes:
    Activity = practice workbook task 19 + assessment Q1–Q4 rehearsed on the practice design.
    Listen for answers that quote their own design decisions rather than recite definitions.
- [TAKEAWAYS] Topic 2 · Key takeaways
  - One job, its own data, a narrow versioned contract.
  - High cohesion within, loose coupling between; the queue is the seam.
  - Justify choice by choice against requirements; answer questions from your own design.
  image: none

### Close
- [BESPOKE] Next: Topic 3 — disaster recovery
  - Part A's design work is done: the web-scale platform and the microservice, drawn, justified and defensible.
  - Next you plan for the day it all fails — DR requirements and impact analysis.
  image: none
  notes:
    Both designs come back later: the walkthrough presents them, AT2 builds the microservice.

## Build notes
~24 slides. Four activities, mapping to practice workbook tasks 15 · 16 · 17–18 · 19 + the
assessment's Part A Q1–Q4 (the practice workbook carries no questions — rehearse with the
assessment's, against the practice design). One generated architecture diagram
(`diagram microservice-arch`, already in `diagrams/`); one decorative `gen` opener hero (cached in
`images/`). Content carried from the 2026-07-01 plan; new teaching: the justification task and the
answer-from-your-own-design discipline. The design justification (PC 2.4) moves here from the old
Topic 5 — the workbook has students justify inside Part A, not at presentation time.

## Changelog
- 2026-09-08 — redrafted from the AT1 Part A practice workbook (tasks 15–19 + Q1–Q4): justification
  and knowledge-question rehearsal added; contract and drawing split into their workbook tasks.
- 2026-07-01 — authored to full content.
