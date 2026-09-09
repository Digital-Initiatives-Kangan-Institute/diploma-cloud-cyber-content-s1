# Topic 07 Building the microservice with your own IaC — Slide plan
> **Covers:** Topic 07 — see coverage.md
> **Subtitle:** Author your own template, deploy the microservice from it, prove it works, then make it reusable
> **STATUS: DRAFT — redrafted 2026-09-08 from the AT2 practice workbook, tasks 11–18. Merges the old
> Topics 7 and 8: the workbook has one continuous build — the template you author IS the microservice.**

## Depth ceiling
BUILD — the core of AT2: review the supplied code, author your own template that provisions the
microservice, deploy it, confirm it, test it end to end, troubleshoot it, then parameterise and extend
it. One continuous run of work, in workbook order.

**Answer discipline:** activities run on the practice workbook's code, contract and store; the
assessment builds a different microservice. Teach the method; never pre-solve the assessed build.

## Teaching source
AWS ACA CloudFormation authoring + serverless deploy decks pinned at Step 4 (TBD); bespoke for
authoring practice, the wiring, the test/troubleshoot discipline, and parameterisation.

## AWS pin table
TBD — AWS ACA CloudFormation authoring + serverless (Lambda / API Gateway / SQS / DynamoDB) modules to
be pinned.

## Slides

### Opener
- [BESPOKE] Build what you designed
  - This is the centre of AT2: the microservice you designed in Topic 2, built by a template you author yourself.
  - The code is supplied; the infrastructure is yours to declare — review, author, deploy, confirm, test, troubleshoot, reuse.
  - The design names its real region; in the lab you deploy to us-east-1 — same build, different console label.
  - The lab's LabRole serves as every execution role and credential — you never create IAM here.
  image: gen flat vector hero illustration of a hand-written template assembling a serverless event pipeline, blue and gold accents, minimal, no text
  notes:
    The biggest Topic of AT2 — workbook tasks 11 to 18, one continuous build in workbook order.
    Point back to the Topic 2 design: the paper design is today's build spec.
    Flag LabRole now so nobody goes hunting for IAM to build.

### C1 — Review before you build
- Teaches: [ICTCLD503 PC 3.1]
- Kicker: read the code, hold the contract
- [BESPOKE] Review the supplied code and the contract
  - Read the provided handler and the webhook contract: what the code expects, what it writes, what it needs from config.
  - Your design from Topic 2 is the build spec — re-read it beside the code and note where they meet.
  - Deployment is assembling parts you understand; skipping the review means wiring blind.
  image: none
  notes:
    Workbook task 11 — the read-first discipline before any console work.
    The config question is the hook: the code needs a table name — where does it come from? (deployment config, which their template supplies).
- [EX] Review the code and contract
  - Workbook — task 11.
  - Work out what the supplied code does, what the contract promises, and what the infrastructure must provide for both.
  timer: ~20 min
  image: none
  notes:
    Activity = practice workbook task 11.
    The output that matters: a list of what the template must create — it becomes the plan for task 12.
- [TAKEAWAYS] Section 1 · The review
  - Know what the code expects before you provision anything.
  - The Topic 2 design plus the contract is the build spec.
  image: none

### C2 — Author your template
- Teaches: [ICTCLD505 PC 3.1] · [ICTCLD505 PC 3.2] · [ICTCLD505 KE 5] · [ICTCLD505 KE 9]
- Kicker: declare the microservice's infrastructure
- [PRIMER] Authoring from syntax
  - Apply the template syntax to declare a set of related resources — the reading skill from last Topic, reversed.
  - Start from the outcome: what resources, what depends on what, what inputs and outputs.
  - Build incrementally — a few resources, deploy, confirm, add more. Don't write it all then drown in errors.
  image: none
  notes:
    The step up from reading to producing. Design the template before typing it.
    Incremental authoring is the habit that saves the session — a big-bang deploy buries the first failure under many.
- [BESPOKE] The wiring your template declares
  - The gateway receives the webhook and hands it on; the queue is the function's event source; the function writes to the store.
  - The event-source mapping is the make-or-break declaration — a deployed function that nothing triggers just sits there.
  - The store's table name reaches the function as configuration, not hard-coded.
  image: diagram microservice-deploy
  notes:
    The event-driven wiring pattern, on the diagram — this is what their template has to say.
    Students expect a direct API-to-function call; the queue in between is the design point worth pressing.
- [BESPOKE] Industry IaC practice
  - Parameters over hard-coded values; least privilege on any role; tag every resource.
  - Outputs expose what other stacks and services need — the integration seam.
  - Standard practice is what makes a template safe to reuse and hand over.
  image: none
  notes:
    The professional checklist their authored template is judged against.
    In the lab, least privilege means passing LabRole — the practice point still stands outside the lab.
- [DEMO] Author a template from scratch
  - Author a small template live: state the outcome, declare a couple of resources with a dependency, apply the practices as you go.
  - Deploy it and watch it reach CREATE_COMPLETE.
  source: recorded/live demo
  image: none
  notes:
    Live demonstration, educator-led (screen it live or your own capture — no recorded-demos catalogue in CL2).
    Design before typing — say the resources and dependencies out loud first.
    Point at each practice as you write it: a parameter, a tag, the role passed not created.
    Prep: clean lab in us-east-1, a small related resource set in mind, editor ready. ~8–10 min.
- [EX] Author your template
  - Workbook — task 12.
  - Write the template that deploys the microservice: the resources the review said you need, wired the way the design says.
  timer: ~40 min
  image: none
  notes:
    Activity = practice workbook task 12 — the biggest single task in AT2. Authoring is slow; budget for it.
    Push incremental: a tiny deployable version first, grown resource by resource.
    The task 11 list is their checklist — every item on it becomes a declaration.
- [TAKEAWAYS] Section 2 · Authoring
  - Design the template before typing it; build it incrementally.
  - The event-source mapping is the wiring that makes it a pipeline.
  - Parameters, least privilege, tags, outputs — the professional checklist.
  image: none

### C3 — Deploy it, and confirm it
- Teaches: [ICTCLD505 PC 3.2] · [ICTCLD505 PC 3.4] · [ICTCLD505 PE 2] · [ICTCLD505 PE 3] · [ICTCLD503 PC 3.2] · [ICTCLD503 PE 3] · [ICTCLD503 PE 4]
- Kicker: expect more than one attempt
- [BESPOKE] Deploying your own template
  - Expect it to take more than one attempt — that is normal, and the workbook says so.
  - Same discipline as last Topic: first failure event, read the reason, one deliberate fix, redeploy.
  - Each failure you fix is evidence — record what broke and what fixed it as you go.
  image: none
  notes:
    Workbook task 13. Normalise the fail-fix loop before they start; the record-as-you-go habit feeds task 16.
    Blind redeploys burn the lab clock; hold them at the log until they can name the cause.
- [DEMO] Deploy the microservice from your template
  - Deploy the authored template in the lab; pass LabRole; watch the events through to CREATE_COMPLETE.
  - Confirm each resource exists and the event-source mapping is enabled.
  source: recorded/live demo
  image: none
  notes:
    Live demonstration, educator-led. Say the region substitution out loud as you set it.
    The event-source mapping check is the one students skip — show where it lives and that it's on.
    Prep: the C2 demo template ready to deploy, lab open. ~6–8 min.
- [BESPOKE] Confirm the deployment properly
  - Confirmation is checking the resources, not the status colour — console or CLI, either counts.
  - Does each resource exist, with the properties your template declared? Is the wiring live?
  - Deploy, then confirm — every time, and record what you checked.
  image: none
  notes:
    Workbook task 14 makes confirmation its own task. The green stack status is the platform's claim; the check is theirs.
- [EX] Deploy and confirm
  - Workbook — tasks 13 and 14.
  - Deploy your template — expect and work through failures — then confirm every resource and the wiring.
  timer: ~35 min
  image: none
  notes:
    Activity = practice workbook tasks 13–14.
    Failures here are the workbook working as designed; the record of them feeds the troubleshooting task.
- [TAKEAWAYS] Section 3 · Deploy and confirm
  - More than one attempt is normal; read the first failure.
  - Record each break and fix as you go.
  - Confirm resources and wiring, not the status colour.
  image: none

### C4 — Test it end to end, and troubleshoot
- Teaches: [ICTCLD503 PC 3.3] · [ICTCLD503 PC 3.4] · [ICTCLD503 KE 5] · [ICTCLD505 PC 3.7] · [ICTCLD505 KE 7] · [ICTCLD505 PE 3]
- Kicker: the record is the proof, the logs are the map
- [BESPOKE] Test by the observable outcome
  - Send a real event through the contract and find the record in the store — that is the test.
  - A success response only says the front door accepted it; the pipeline behind is asynchronous.
  - Test the unhappy path too: an invalid event should be turned away, and no bad record written.
  image: none
  notes:
    Workbook task 15. The 200-is-not-proof point is the heart of it — walk from response to stored record every time.
    Exactly-once matters: one post, one item — not zero, not two.
- [DEMO] Post events and confirm records
  - Post a valid event and find the item in the store; post an invalid one and confirm it is rejected.
  source: recorded/live demo
  image: none
  notes:
    Live demonstration, educator-led, against the deployed demo pipeline.
    Show where you look — the store item, not the API response. Both paths, side by side.
    Prep: valid and invalid sample events ready, store open in another tab. ~6–8 min.
- [BESPOKE] Troubleshoot from the logs
  - The failure is recorded somewhere — function logs, queue behaviour, dead letters. Find it before touching anything.
  - The usual suspects: a permission error, a payload-validation bug, a mis-wired event source.
  - Fix, redeploy, re-test — the loop ends when the record writes, not when the error stops.
  image: none
  notes:
    Workbook task 16 asks for the record of what actually broke across tasks 12–15 and what was done — the fail-fix notes pay off here.
    Read-diagnose-fix-redeploy-retest, narrated from the log; guessing is the anti-pattern.
- [EX] Test and troubleshoot
  - Workbook — tasks 15 and 16.
  - Test the microservice end to end through the contract, then record what actually broke along the way and how you fixed it.
  timer: ~30 min
  image: none
  notes:
    Activity = practice workbook tasks 15–16.
    Task 16 is honest history, not hypotheticals — what broke for them, found in their own notes and logs.
- [TAKEAWAYS] Section 4 · Prove and fix
  - The stored record is the proof; the response code is not.
  - Invalid events turned away is half the test.
  - The logs name the cause; the notes become the troubleshooting record.
  image: none

### C5 — Make it reusable, then grow it
- Teaches: [ICTCLD505 PC 3.3] · [ICTCLD505 PC 3.5] · [ICTCLD505 KE 8] · [ICTCLD505 KE 10]
- Kicker: one template, many environments
- [PRIMER] Parameterisation and reuse
  - Parameterise so the same template body deploys different configurations — values in, nothing edited.
  - Names, sizes, environments, regions: anything that varies between deployments is a parameter.
  - Write once, deploy many — this is the code-reuse payoff of IaC.
  image: none
  notes:
    Workbook task 17's idea. Copying the template and editing it is the anti-pattern — two templates drift apart.
    Region as a parameter is the neat tie back to the scenario/deploy substitution.
- [BESPOKE] Add a resource through an update
  - Grow the template, not the console: add the new resource to the file and update the stack.
  - The change set shows the diff — the existing resources stay, the new one arrives.
  - Update, confirm, and the template still tells the whole truth about the stack.
  image: none
  notes:
    Workbook task 18. Tearing down and rebuilding loses state; the update-in-place is the skill.
    The template-tells-the-truth framing connects back to drift from Topic 6.
- [DEMO] Parameterise, redeploy, extend
  - Turn a hard-coded value into a parameter and deploy a second environment beside the first.
  - Then add a resource to the template and update the running stack — watch the diff apply.
  source: recorded/live demo
  image: none
  notes:
    Live demonstration, educator-led. The template body not changing between the two environments is the point made visible.
    Pause on the change set before the update — review before run, one more time.
    Prep: the deployed demo stack, one obvious value to parameterise, one small resource to add. ~8 min.
- [EX] Parameterise and extend
  - Workbook — tasks 17 and 18.
  - Redeploy your template as a second environment by changing only parameter values, then add a resource and update the existing stack in place.
  timer: ~30 min
  image: none
  notes:
    Activity = practice workbook tasks 17–18.
    Insist the body stays fixed between the two environments — editing it defeats the exercise.
- [TAKEAWAYS] Topic 7 · Key takeaways
  - Review the code, author to the design, build incrementally.
  - Expect failures; read the first one; record the history honestly.
  - The stored record is the proof of a working pipeline.
  - One parameterised template: many environments, grown by updates, never drifting.
  image: none

### Close
- [BESPOKE] Next: Topic 8 — monitoring
  - The microservice is built, tested and reusable — by a template you wrote yourself.
  - Next you make it observable: the metric and alarm that tell you it's alive without you looking.
  image: none
  notes:
    The monitoring they configure next is the build-side of the DR plan's detection thinking from Topic 4.

## Build notes
~34 slides. Six activities, mapping to practice workbook tasks 11 · 12 · 13–14 · 15–16 · 17–18 (task 12
gets its own EX — the biggest single task in AT2). Four DEMOs (author, deploy, test, parameterise —
carried from the old Topics 7 and 8). One generated diagram: `diagram microservice-deploy` — **its
assets live in the old `topic_08/diagrams/` and must move here before build**. One new `gen` opener
hero. This Topic merges the old Topic 7 (authoring/parameterising, minus removal — now the closeout
Topic's teardown) and old Topic 8 (the microservice build, minus its generic what-is-serverless primer,
taught in Topic 2): the workbook has one continuous build, so the decks follow it.

## Changelog
- 2026-09-08 — new merged plan from the AT2 practice workbook (tasks 11–18); replaces the old
  Topic 7 (author generic template) / Topic 8 (microservice build) split, which matched no seam in the
  workbook. Clean-removal teaching moved to the closeout Topic with the teardown task.
