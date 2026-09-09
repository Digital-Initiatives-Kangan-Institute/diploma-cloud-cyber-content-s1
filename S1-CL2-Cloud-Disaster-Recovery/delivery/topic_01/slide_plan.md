# Topic 01 Web-scale architecture design — Slide plan
> **Covers:** Topic 01 — see coverage.md
> **Subtitle:** Design the changes that scale the platform for a global audience
> **STATUS: DRAFT — redrafted 2026-09-08 from the AT1 Part A practice workbook, tasks 1–14.**

## Depth ceiling
DESIGN — work through the web-scale design half of AT1 Part A on the practice workbook: establish the
needs, design tier by tier, check it, draw it, justify it. The build is AT2. No implementation; no
over-engineering.

**Answer discipline:** activities run on the practice workbook (the LMS engagement); the assessment is
the same work on the website. Teach the method on the practice vehicle; never supply website answers.

## Teaching source
Bespoke for the workbook framing + the target architecture; AWS web-scale decks pinned at Step 4 (TBD).

## AWS pin table
TBD — AWS web-scale modules (edge/CDN, ELB + auto scaling, managed data tiers) to be pinned.

## Slides

### Opener
- [BESPOKE] From design to web-scale
  - Topic 1 opens AT1: you design the changes that ready a platform for serving a large, distant audience.
  - Design for scale, reach, availability and a public surface — to the supplied requirements, with a source for every number.
  - This Topic is the web-scale half of the design; the microservice half is Topic 2.
  - Design only — the build is AT2.
  image: gen flat vector hero illustration of global web traffic reaching a scalable cloud data centre, blue and gold accents, minimal, no text
  notes:
    First slide of AT1 and the cluster's design work — set the job and the boundary, don't teach yet.
    The workbook walks them through this design task by task; today runs tasks 1 to 14 in order.
    Hold the line: design only, to the supplied requirements — gold-plating is a defect, not a bonus.
    Question to pose: name one thing that has to change about how a site is delivered when its audience goes global.

### C1 — The needs, and the current position
- Teaches: [ICTCLD503 PC 1.1] · [ICTCLD503 PC 1.2]
- Kicker: what to scale, and the gaps to close
- [PRIMER] What web-scale means
  - Web-scale means serving large, variable, global demand without manual intervention.
  - Scale elastically: add capacity as load rises, release it as load falls — pay for what you use.
  - The three things that scale: network, compute, storage.
  image: none
  notes:
    Vocabulary slide — vendor-neutral, tight. Stress "without manual intervention"; that separates web-scale from buying a bigger server.
    The network/compute/storage triple is the spine of the whole design — every change scales one of the three.
    Misconception: scaling up (one big server) vs scaling out (many small units, added and removed automatically).
- [BESPOKE] Establish what the design is held to
  - Before designing anything, read the requirements and the application specification and record the needs.
  - Who uses it, from where, how much, how variable — plus the non-functionals: availability, latency, cost.
  - Name the document each need came from. A target you cannot attribute is one you have assumed.
  image: none
  notes:
    This is workbook task 1's discipline: needs with sources. A consultant reads the brief; they don't invent numbers.
    Press the attribution line — "where would 99.9% availability actually be written down?"
    The load-bearing requirements are non-functional; a feature list doesn't size an architecture.
- [BESPOKE] Review the current architecture against those needs
  - Go through the current architecture layer by layer and ask: does it meet the needs just recorded?
  - Where it does not, say why not — that gap is what the design must close.
  - Some layers already meet their needs. Finding those matters as much as finding the gaps — a review that rebuilds what already works has misread the job.
  image: none
  notes:
    A review is a comparison against requirements, not a description. Every gap ties to the need it fails.
    The already-adequate layers are the trap worth naming — the workbook's worked example row deliberately answers "yes".
- [EX] Record the needs and review the architecture
  - Workbook — tasks 1 and 2.
  - Record the scaling and performance needs with the document each came from, then review the current architecture layer by layer against them.
  timer: ~25 min
  image: none
  notes:
    Activity = practice workbook tasks 1–2. Both are table tasks with a given example row.
    Where they get stuck: vague needs with no source — point them back to the named intranet documents.
    Share-back: one gap and the exact requirement it breaks.
- [TAKEAWAYS] Section 1 · Needs and gaps
  - Web-scale is elastic scaling of network, compute and storage to variable global demand.
  - Every need carries a source; every gap ties to a need.
  - A layer that already meets its needs stays as it is.
  image: none

### C2 — The design inputs: residency and services
- Teaches: [ICTCLD503 PC 1.5] · [ICTCLD503 PC 1.3]
- Kicker: constraints and building blocks first
- [BESPOKE] The residency obligation is a design input
  - Some data is legally obliged to stay in, or be copied to, a particular country — read what the obligation actually requires before designing around it.
  - Record what it obliges, and just as importantly what it does not — an obligation read too broadly costs as much as one ignored.
  - It is a constraint you carry through the design, not a feature you add at the end.
  image: none
  notes:
    Workbook task 3 — read the residency requirements document and record what it does and does not oblige.
    The over-read is the common failure: assuming everything must live onshore when only certain data must.
    This constraint recurs through the whole cluster; establish the careful-reading habit now.
- [BESPOKE] Choose the services before you place them
  - List the cloud services the design needs, layer by layer, and what job each does.
  - Managed services first: they scale, replicate and patch without you operating them.
  - This list is the palette; the next section arranges it into an architecture.
  image: none
  notes:
    Workbook task 4 — identify the services before designing with them. Keeps the design honest: every box on the later diagram comes from this list.
    Press "what job does it do" over brand names — the service category is the decision, the product follows.
- [EX] Record the obligation and pick the services
  - Workbook — tasks 3 and 4.
  - Record what the residency requirements oblige and do not oblige, then list the cloud services the design needs and the job each does.
  timer: ~20 min
  image: none
  notes:
    Activity = practice workbook tasks 3–4.
    Watch for the residency over-read; the document says precisely what is in scope.
- [TAKEAWAYS] Section 2 · Inputs
  - Read the obligation; record what it requires and what it does not.
  - Pick the services and the job each does before arranging them.
  image: none

### C3 — Designing the tiers
- Teaches: [ICTCLD503 PC 1.4] · [ICTCLD503 PC 1.5] · [ICTCLD503 PE 5] · [ICTCLD503 KE 3] · [ICTCLD503 KE 6]
- Kicker: scale by layer, reach the globe
- [PRIMER] Scaling by layer
  - Network: load balancing spreads traffic; edge delivery shortens the path to the user.
  - Compute: a pool that grows and shrinks on demand, not one fixed server.
  - Storage: managed, replicated data services that scale reads.
  image: none
  notes:
    Turns the triple into three concrete moves, one layer per line — still vendor-neutral.
    The read-heavy audience is why scaling reads is the storage job; connect it back to the recorded needs.
- [BESPOKE] The target web-scale architecture
  - The edge absorbs read-heavy global traffic and the public attack surface.
  - A load balancer fronts an auto-scaling application tier spread across locations.
  - Managed data tiers and an in-memory cache scale the reads.
  image: diagram web-scale-arch
  notes:
    The keystone slide — assemble the diagram live, tier by tier, mapping each tier to a gap from C1.
    Every box answers a named gap; a component that closes no requirement doesn't belong.
    This is a worked example to adapt, not a template to copy — their workbook design is their own.
- [BESPOKE] Designing for a distant audience
  - Serve static and cacheable content from the edge, close to the users.
  - DNS and a global entry point route each user to the nearest healthy edge.
  - The web-scaling principles at work: statelessness, caching, horizontal scale, loose coupling.
  image: none
  notes:
    The global-reach slice — task 8's subject. "Healthy" matters: routing is an availability mechanism too.
    The four principles are examinable and underpin every box; students cite them in the knowledge questions later.
- [BESPOKE] The caching decision
  - Two different caches solve two different problems: the edge caches static content near users; an in-memory cache holds hot data near compute.
  - Cache what is read often and changes rarely; every cache carries a staleness trade-off.
  - Choose the simplest option that meets the requirement, and be ready to say why.
  image: none
  notes:
    Workbook task 9 makes caching its own decision — treat it as one, not a checkbox.
    The staleness trade-off is the discussion: what happens when the cached copy is wrong, and how long can that last?
- [TABLE] The four web-scale choices
  | Choice | Use when | Trade-off |
  | SQL vs NoSQL | relational + transactional vs flexible, high-scale reads | consistency vs scale/flexibility |
  | Monolith vs microservice | simple and small vs independent scale and deploy | simplicity vs operational complexity |
  | VM / container / serverless | control vs portability vs no-ops scale | management overhead vs flexibility |
  | CDN vs in-memory cache | cache static at the edge vs cache hot data near compute | global static reads vs dynamic hot data |
  note: Choose the simplest option that meets the requirement — you will justify each choice in writing.
  image: none
- [EX] Design the tiers
  - Workbook — tasks 5 to 9.
  - Design the network and entry point, the compute tier, the database and storage tier, the global serving approach, and make the caching decision.
  timer: ~45 min
  image: none
  notes:
    Activity = practice workbook tasks 5–9, one design table per tier. The biggest block of the Topic.
    Circulate against orphan components — every choice traces to a recorded need from tasks 1–3.
    They design their own; the teaching diagram is a model, not an answer.
- [TAKEAWAYS] Section 3 · The design
  - Scale each layer with its own mechanism; deliver at the edge.
  - Statelessness, caching, horizontal scale, loose coupling.
  - Two caches, two problems; every cache trades staleness for speed.
  image: none

### C4 — Checking the design
- Teaches: [ICTCLD503 PC 1.4] · [ICTCLD503 PC 1.6]
- Kicker: prove it scales, keep it up, keep it safe
- [BESPOKE] Check it scales as utilisation increases
  - Walk the design up: double the load, then ten times it — which layer moves first, and does anything sit fixed?
  - A fixed component in a scaling path is the next bottleneck; find it on paper before it finds you in production.
  image: none
  notes:
    Workbook task 10 — a thought experiment against their own design, layer by layer.
    Push for the mechanism: "what exactly adds capacity at this layer, and what triggers it?"
- [BESPOKE] Protecting the public surface
  - A public site faces the open internet: web exploits, bots and volumetric attacks.
  - Defend at the edge: a firewall for malicious requests, the delivery network absorbing volume.
  - Deployment across locations plus health checks keeps the service available through failures.
  image: gen flat vector illustration of a shield protecting a cloud web server from bots and DDoS arrows, blue and charcoal palette, minimal, no text
  notes:
    Task 11's subject — availability and security are one check, not two: a volumetric attack is an availability attack.
    The three threat classes map one-to-one to the defences; have students make the pairing.
- [BESPOKE] Review your design and revise it
  - Read the whole design back against every requirement: scale, reach, availability, security, residency.
  - Where a requirement is not met, make the simplest change that satisfies it, and record what you changed.
  - A review that changes nothing and finds nothing has usually not been done.
  image: none
  notes:
    Task 12 — the review discipline. It is an engineering step that can send you back, not a proofread.
    A recorded revision is good evidence, not an admission of error — say so explicitly.
- [EX] Check, harden and revise
  - Workbook — tasks 10, 11 and 12.
  - Check the design scales with utilisation, confirm availability and security are maintained, then review the whole design and record any revision.
  timer: ~30 min
  image: none
  notes:
    Activity = practice workbook tasks 10–12, all against their own tasks 5–9 answers.
    The common miss is skipping the revise step — press for at least an honest "checked, nothing changed, because…".
- [TAKEAWAYS] Section 4 · The checks
  - Walk the load up and find the fixed component.
  - Availability and security are one check on a public surface.
  - Review against every requirement; record what changed.
  image: none

### C5 — Draw it, and justify it
- Teaches: [ICTCLD503 PE 1] · [ICTCLD503 PC 1.7]
- Kicker: one picture, one argument
- [BESPOKE] Draw the architecture
  - One diagram of the whole design: every tier, every service you chose, and where the users come in.
  - Label what each component is, not just what product it uses — a reader should see the job of every box.
  - The diagram must agree with the tables that produced it; a box with no design decision behind it is a decoration.
  image: none
  notes:
    Workbook task 13. The drawing is evidence the design hangs together — mismatches with tasks 5–9 surface here.
    Any drawing tool is fine; legibility and agreement with the design beat prettiness.
- [BESPOKE] Justify the design in writing
  - For each major choice: the requirement it serves, the option you took, and why that option over the alternative.
  - Write to be checked: someone holding the requirements should be able to tick your justification off against them.
  - The simplest design that meets the requirements is the strongest claim you can make.
  image: none
  notes:
    Workbook task 14 closes the web-scale half — the written argument for the design.
    Push requirement-option-why as the sentence shape; "because it is best practice" is not a justification.
- [EX] Draw and justify the web-scale design
  - Workbook — tasks 13 and 14.
  - Draw the full architecture, then justify the design choice by choice against the requirements.
  timer: ~30 min
  image: none
  notes:
    Activity = practice workbook tasks 13–14.
    Have pairs swap diagrams and try to read each other's — the questions they ask are the missing labels.
- [TAKEAWAYS] Topic 1 · Key takeaways
  - Needs with sources; gaps tied to needs; constraints read precisely.
  - Scale each layer with its own mechanism; check it scales, stays up and stays safe.
  - Draw the whole design; justify every choice against a requirement.
  image: none

### Close
- [BESPOKE] Next: Topic 2 — the microservice
  - The web-scale half of the design is done: designed, checked, drawn and justified.
  - Next you design the second half — a small service with its own architecture and contract — and it plugs into this one.
  image: none
  notes:
    Hand off to Topic 2. The design is a live input from here — it comes back in the walkthrough, the build and the monitoring.

## Build notes
~28 slides. Five activities, mapping to practice workbook tasks 1–2 · 3–4 · 5–9 · 10–12 · 13–14.
One generated architecture diagram (`diagram web-scale-arch`, already in `diagrams/`); two decorative
`gen` images carried over from the previous plan (opener hero, public-surface shield — cached in
`images/`). Content carried forward from the 2026-06-25 plan, regrouped to workbook task order;
new teaching: the residency reading discipline, the service palette, the caching decision, the
scaling walk-up, and the draw/justify pair.

## Changelog
- 2026-09-08 — redrafted from the AT1 Part A practice workbook (tasks 1–14): five sections matching
  the task spine, each ending in the workbook tasks it prepares.
- 2026-06-25 — authored to full content; first topic built by the slide-plan-driven deck builder.
