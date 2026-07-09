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
  notes:
    Frame the Topic as the second design half — the microservice that plugs into Topic 1's web-scale site. Set the job and the boundary; don't teach serverless yet.
    • First bullet: callback to Topic 1 — they designed the web-scale site; today they design the serverless audit-log MICROSERVICE that plugs into it. Two halves of one Solution Design (AT1 Part A).
    • Second bullet: name the microservice's reason to exist — it records India-cohort access events to a RESIDENCY-COMPLIANT store. This is the localisation hook straight from the requirements, not an add-on.
    • Third bullet: define serverless plainly — no servers to manage, event-driven, scales with demand, pay per request. Stress "event-driven": the site emits events, the service reacts.
    • Hold the boundary (last bullet): DESIGN ONLY, to the supplied requirements — the build is AT2 (Topic 8). On paper today.
    Misconception to pre-empt: "serverless means there are no servers." No — there are servers; YOU just don't manage or provision them. The shift is operational responsibility, not physics.
    Question to pose: "The website already works — why build a SEPARATE service just to record access events?" (single responsibility, independent scale, and a residency-resident store the site itself needn't host).
    UoC/AT1 tie: this Topic develops [ICTCLD503 PC 2.1]–[ICTCLD503 PC 2.3] plus [ICTCLD503 PE 2] and [ICTCLD503 KE 4], evidenced in AT1 Part A (Solution Design, microservice sections) and the Part A KE appendix.

### C1 — Microservices & data transactions
- Teaches: [ICTCLD503 PC 2.1]
- Kicker: one service, one job, one record
- [PRIMER] What a microservice is
  - A microservice does one thing well — a small, independently deployable unit with a single responsibility.
  - It owns its data and exposes a narrow interface; other systems talk to it only through that contract.
  - Right-sized: big enough to be useful, small enough to reason about and scale on its own.
  image: none
  notes:
    Install the microservice concept — vendor-neutral, no AWS yet. Keep it tight; it's the definition the whole Topic builds on.
    • First bullet: a microservice does ONE thing well — small, independently deployable, single responsibility. Stress "single responsibility": that's the test for whether something should be its own service.
    • Second bullet: it OWNS its data and exposes a NARROW interface — others talk to it only through that contract, never reach into its data directly. This is what keeps services decoupled.
    • Third bullet: right-sized — big enough to be useful, small enough to reason about and scale on its own. Not "as small as possible"; sized to a responsibility.
    Misconception to pre-empt: "microservices = lots of tiny services always." No — the win is single-responsibility and independent deploy/scale, not smallness for its own sake; over-splitting adds coupling and operational cost.
    Question to pose: "If another system needs this service's data, how should it get it?" (through the service's interface/contract — never by reaching into its store).
    UoC/AT1 tie: [ICTCLD503 PC 2.1] (identify microservices and the data transactions to meet business needs) — the concept students apply to the audit log next.
- [BESPOKE] The audit-log microservice
  - The one job: capture each India-cohort access/enquiry event the website emits and record it durably.
  - The website is the event producer; it knows only the webhook contract, not the store behind it.
  - Residency: India-cohort access logs land in an India-resident store (ap-south-1) per the requirements.
  image: none
  notes:
    Make the concept concrete — THIS microservice, its single job. This is the design's first decision: what the service is responsible for.
    • First bullet: the one job — capture each India-cohort access/enquiry event the website EMITS and record it DURABLY. One responsibility, stated as a sentence.
    • Second bullet: the website is the PRODUCER; it knows ONLY the webhook contract, not the store behind it. This is the decoupling from the last slide, applied — the site can't and shouldn't know how the log is stored.
    • Third bullet (accent it): RESIDENCY — India-cohort access logs land in an India-resident store (ap-south-1) per the requirements. This is the whole reason the service exists on its own; residency is an input constraint, not a design choice.
    Misconception to pre-empt: "the website should just write the log itself." No — separating it gives single responsibility, independent scale, and lets the log live in a residency-compliant store the site needn't host. Coupling them would defeat all three.
    Question to pose: "Why does the website only need to know the webhook, and not where the log ends up?" (loose coupling — the store can change, move region, or scale without touching the site).
    UoC/AT1 tie: [ICTCLD503 PC 2.1] (identify the microservice to meet the business need) — AT1 Part A A8; residency is the business need it answers.
- [BESPOKE] Its data transactions
  - One transaction: append an access event (who / what / when) — write-once, never updated.
  - Append-only means idempotent writes and simple, high-scale reads for audit retrieval.
  - Identify each transaction by the business need it meets — here, the CERT-In access-log obligation.
  image: none
  notes:
    Teach the DATA-TRANSACTION half of C1 — what data moves through the service and how. Short and precise; this defines the store's shape.
    • First bullet: ONE transaction — append an access event (who / what / when), WRITE-ONCE, never updated. An audit log is immutable by nature; you add records, you don't edit them.
    • Second bullet: append-only buys you IDEMPOTENT writes (re-sending the same event is safe) and simple, high-scale READS for retrieval. The data pattern makes scaling trivial — no update contention.
    • Third bullet: identify each transaction by the BUSINESS NEED it meets — here the CERT-In access-log obligation. A transaction exists because a requirement demands it, not because it's technically possible.
    Misconception to pre-empt: "we'll need update and delete too." No — an audit log is append-only by design; mutability would break its evidentiary value. Fewer transactions, precisely justified, is the stronger design.
    Question to pose: "Why is 'write-once, never updated' actually an advantage for scale and integrity?" (idempotent writes, no update contention, and a tamper-evident record).
    UoC/AT1 tie: [ICTCLD503 PC 2.1] (data transactions to meet business needs) — AT1 Part A A8; each transaction traced to its business/compliance driver.
- [EX] Identify the microservice & transactions
  - For the practice scenario, identify the microservice(s) and the data transaction(s) each handles.
  - State the business need each transaction meets.
  timer: ~20 min
  image: none
  notes:
    Facilitation — the C1 practice: identify the service(s) and their transactions on the PRACTICE scenario. Rehearses AT1 Part A A8 in miniature.
    Tell students: "On the practice scenario, identify the microservice(s) you need and, for each, the data transaction(s) it handles — then state the business need behind every transaction."
    Steps (put on the board):
    1. Identify the microservice(s) — one responsibility each; name what each is FOR.
    2. For each, list its data transaction(s) — what data moves, in which direction (append / read).
    3. Against every transaction, write the business need it meets — no orphan transactions.
    Must produce: a short written list of microservice(s) with their transactions, each transaction tied to a business need.
    Timing: ~20 min. Where they get stuck: they design one big service that does everything (push single-responsibility — split by job), and they list transactions with no business need behind them (make them name the requirement).
    Share-back prompt: "Name one transaction and the exact business need it meets" — take two or three; listen for transaction→need traceability.
    No-leakage note: this runs on the PRACTICE scenario (comparable, not identical); AT1 evidences the same identify-the-service skill on the assessed system — keep them on the practice brief.
    UoC/AT1 tie: [ICTCLD503 PC 2.1] — identify microservices + data transactions to business needs, the opening move of AT1 Part A's microservice strand.

### C2 — Supporting cloud services
- Teaches: [ICTCLD503 PC 2.2]
- Kicker: pick the serverless building blocks
- [PRIMER] The serverless building blocks
  - Compute: a function service runs your code on demand, no servers to manage (e.g. AWS Lambda).
  - Front door: an API gateway receives requests and routes them to the function.
  - Messaging / queuing: a queue or topic buffers events and decouples producer from consumer.
  - Persistence: a managed datastore keeps the data without you running a database server.
  image: none
  notes:
    Open C2 with the serverless toolkit — the four building-block TYPES, still vendor-neutral (name AWS only as the example). One block per line.
    • COMPUTE: a function service runs your code ON DEMAND, no servers to manage (e.g. AWS Lambda). It runs when an event arrives, then stops — you pay per invocation.
    • FRONT DOOR: an API gateway RECEIVES requests and routes them to the function — the public, managed entry point that speaks HTTPS.
    • MESSAGING / QUEUING: a queue or topic BUFFERS events and DECOUPLES producer from consumer — the site can fire events faster than they're processed without anything breaking.
    • PERSISTENCE: a managed datastore keeps the data WITHOUT you running a database server — no patching, no capacity planning.
    Misconception to pre-empt: "serverless is just Lambda." No — it's a toolkit: gateway + queue + function + managed store, each a managed building block. The function is only one piece.
    Question to pose: "Which block lets the website fire 1,000 events a second even if the logger can only write 200 a second?" (the queue — it buffers and decouples).
    UoC/AT1 tie: [ICTCLD503 PC 2.2] (determine the cloud services that support the microservice architecture) — the palette students select from next.
- [BESPOKE] Choosing services for the audit log
  - Ingress: an API gateway receives the website's webhook over HTTPS.
  - Buffer: a queue absorbs bursts and decouples the site from the logger (loose coupling).
  - Compute: a function validates and writes each event.
  - Store: a managed NoSQL datastore holds the append-only log, resident in India.
  image: none
  notes:
    Apply the toolkit to OUR service — map each building block to a specific job in the audit log. This is the service-selection decision (PC 2.2) made concrete.
    • INGRESS: an API gateway receives the website's webhook over HTTPS — the front door for the producer's events.
    • BUFFER: a queue absorbs bursts and DECOUPLES the site from the logger — loose coupling, so a slow or failed logger never backs up the website.
    • COMPUTE: a function VALIDATES and writes each event — the only custom code in the whole service; everything else is managed.
    • STORE: a managed NoSQL datastore holds the APPEND-ONLY log, RESIDENT IN INDIA. NoSQL fits the write-once, high-scale-read pattern from C1; residency picks the region.
    Misconception to pre-empt: "pick a relational database, it's the default." No — the access pattern (append-only, high-scale simple reads) and residency point to managed NoSQL; justify the choice against the requirement, don't default to SQL.
    Question to pose: "Each service here is chosen for a reason — pick one and tell me the requirement it answers." (gateway→ingress, queue→decoupling/burst, NoSQL store→append pattern + residency).
    UoC/AT1 tie: [ICTCLD503 PC 2.2] (determine cloud services to support the architecture) — AT1 Part A A9; each service justified against a requirement.
- [EX] Determine the supporting services
  - For the practice scenario, determine the cloud services that support your microservice.
  - Justify each choice against a requirement (scale, residency, decoupling).
  timer: ~20 min
  image: none
  notes:
    Facilitation — the C2 practice: choose the supporting services for the practice-scenario microservice and JUSTIFY each. Rehearses AT1 Part A A9.
    Tell students: "For the microservice you identified last activity, determine the cloud services that support it — and for EACH one, name the requirement it answers (scale, residency, or decoupling)."
    Steps (put on the board):
    1. Pick a service for each job: ingress, buffer/decouple, compute, persistence.
    2. Against each choice, write the requirement it satisfies — scale, residency, or decoupling.
    3. Prefer managed/serverless building blocks; note where a choice is forced by residency.
    Must produce: a service list with a one-line justification per service, each tied to a requirement.
    Timing: ~20 min. Where they get stuck: they name product names with no reason attached (make them state the requirement), and they skip the queue (ask "what absorbs a burst?").
    Share-back prompt: "Name one service and the requirement that forced it" — spotlight choice→requirement traceability.
    No-leakage note: practice scenario only (comparable, not identical); AT1 evidences the same service-selection skill on the assessed system — keep them on the practice brief.
    UoC/AT1 tie: [ICTCLD503 PC 2.2] — determine the supporting cloud services, justified to requirements (AT1 Part A A9).

### C3 — Microservice architecture & contract
- Teaches: [ICTCLD503 PC 2.3] · [ICTCLD503 PE 2] · [ICTCLD503 KE 4]
- Kicker: cohesive, loosely coupled, contract-first
- [PRIMER] Cohesion, coupling & the datastore
  - High cohesion: everything in the service serves its one job.
  - Loose coupling: the queue between producer and consumer means neither breaks the other.
  - Persistent datastore: the record survives independently of the compute that wrote it.
  image: none
  notes:
    Open C3 with the three architecture PRINCIPLES the design must demonstrate — vendor-neutral, examinable. One principle per line.
    • HIGH COHESION: everything in the service serves its ONE job. Nothing unrelated bolted on — cohesion is single-responsibility seen from inside the service.
    • LOOSE COUPLING: the queue between producer and consumer means neither BREAKS the other — the site can fail, the logger can fail, independently. The queue is the coupling seam.
    • PERSISTENT DATASTORE: the record SURVIVES independently of the compute that wrote it. The function is ephemeral (it runs and stops); the data must outlive it.
    Misconception to pre-empt: "cohesion and coupling are the same idea." No — cohesion is WITHIN a service (does it do one job?); coupling is BETWEEN services (how tightly do they depend?). You want high cohesion AND loose coupling.
    Question to pose: "The function runs for 200ms then disappears — so where does the audit record live?" (in the persistent datastore — compute is ephemeral, storage is durable).
    UoC/AT1 tie: [ICTCLD503 KE 4] (features of web-scale infrastructure: cohesion/coupling, persistent datastore, API/messaging/queuing) and [ICTCLD503 PC 2.3]/[ICTCLD503 PE 2] — the principles the architecture on the next slide must show.
- [BESPOKE] The target architecture
  - Flow: website webhook -> API gateway -> queue -> function -> NoSQL datastore.
  - The website knows only the webhook; each stage is independently scalable and replaceable.
  - The store sits in the India region (ap-south-1) so the access logs are resident by construction.
  image: diagram microservice-arch
  notes:
    The keystone slide — the target architecture, on the diagram. Trace the flow live, stage by stage, and tie each stage back to a principle from the last slide.
    • Walk the flow left to right: website webhook → API gateway → queue → function → NoSQL datastore. Five stages, one event's journey; say each stage's job as you pass it.
    • Second bullet: the website knows ONLY the webhook, and each stage is independently SCALABLE and REPLACEABLE — loose coupling made visible. Any stage can change without the others knowing.
    • Third bullet (accent it): the store sits in the India region (ap-south-1) so the access logs are RESIDENT BY CONSTRUCTION — residency isn't a policy you enforce later, it's where you put the box.
    • Point out this is a DESIGN artefact — boxes and a contract, not a built system. The .drawio is student-editable; they adapt this shape to their practice scenario.
    Misconception to pre-empt: "the queue is an optional extra." No — the queue is what makes producer and consumer independent; remove it and a slow logger backs up the website. Every stage answers a principle.
    Question to pose: "Point at one stage and tell me which principle it delivers — cohesion, coupling, or persistence." — go round the room; every box should trace to a principle.
    UoC/AT1 tie: [ICTCLD503 PC 2.3] (design the architecture using cloud services) + [ICTCLD503 PE 2] (design at least one microservice architecture for a simple web app) — this diagram is the PE 2 evidence.
- [BESPOKE] The integration contract
  - Define the webhook payload contract: the fields the website sends and what each means.
  - Version it and validate it — producer and consumer agree on this and nothing else.
  - A clear contract is what lets the two sides evolve independently.
  image: none
  notes:
    Teach the CONTRACT — the interface the whole loosely-coupled design hinges on. Short and sharp; this is the "and nothing else" idea.
    • First bullet: define the webhook payload CONTRACT — the fields the website sends and what each MEANS. A contract is a shared, explicit agreement, not an implied one.
    • Second bullet: VERSION it and VALIDATE it — producer and consumer agree on THIS and nothing else. Versioning lets the contract change safely; validation rejects malformed events at the door.
    • Third bullet (accent it): a clear contract is what LETS THE TWO SIDES EVOLVE INDEPENDENTLY — the payoff of loose coupling. The site team and the logger team can work without meetings.
    Misconception to pre-empt: "the contract is just documentation you write at the end." No — it's the design's load-bearing interface; you define it FIRST (contract-first), and both sides build to it. It's an agreement, not a write-up.
    Question to pose: "The website team wants to add a new field to the event — how does the contract let them do that without breaking the logger?" (versioning + the consumer validating/ignoring unknown fields — evolve independently).
    UoC/AT1 tie: [ICTCLD503 PC 2.3] (design the architecture including the interface/integration contract) + [ICTCLD503 KE 4] — AT1 Part A A10/A12; the contract is the interface half of the design.
- [EX] Design the architecture & contract
  - For the practice scenario, design the microservice architecture (cohesive, loosely coupled, persistent, API / messaging).
  - Define the webhook integration contract.
  timer: ~30 min
  image: none
  notes:
    Facilitation — the biggest activity in the Topic: students draw their OWN microservice architecture and write its contract for the practice scenario. The core AT1 Part A microservice rehearsal.
    Tell students: "Using the target architecture as a model — not a template to copy — design your microservice architecture for the practice scenario: cohesive, loosely coupled, persistent, with API and messaging. Then define the webhook integration contract."
    Steps:
    1. Draw the flow: ingress → buffer → compute → persistent store, each stage independently scalable.
    2. Show high cohesion (one job) and loose coupling (the queue seam); place the store to honour residency.
    3. Define the webhook contract — the fields, their meanings, and a version.
    Must produce: a labelled architecture sketch (their own .drawio or on paper) PLUS a written payload contract.
    Timing: ~30 min. Where they get stuck: they redraw the teaching diagram verbatim (push them to adapt it to THEIR scenario), they forget the contract (half the mark is the interface), and they omit the queue (ask "where's your decoupling seam?").
    Share-back prompt: "Show your contract's fields and where the queue sits" — surface both loose coupling and the interface.
    No-leakage note: practice scenario only (comparable, not identical); AT1 evidences the same design skill on the assessed system — keep them on the practice brief.
    UoC/AT1 tie: [ICTCLD503 PC 2.3] · [ICTCLD503 PE 2] · [ICTCLD503 KE 4] — the full architecture-and-contract core of AT1 Part A's microservice strand.
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
