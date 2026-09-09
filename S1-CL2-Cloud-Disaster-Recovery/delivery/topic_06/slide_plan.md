# Topic 06 IaC: fundamentals & operating provided templates — Slide plan
> **Covers:** Topic 06 — see coverage.md
> **Subtitle:** Infrastructure as Code from first principles, then operating a template you were given
> **STATUS: DRAFT — redrafted 2026-09-08 from the AT2 practice workbook, tasks 1–10.**

## Depth ceiling
BUILD — first hands-on Topic of AT2. Work through the IaC concepts, then take a provided template
through review, deploy, failure, fix, confirm, update and reset. Authoring your own is Topic 7.

**Answer discipline:** activities run on the practice workbook's template and scenario; the assessment
operates a different provided template. Teach the method; never pre-solve the assessed template's
planted failure.

## Teaching source
AWS ACA CloudFormation / IaC decks pinned at Step 4 (TBD); bespoke for the supplied-template
discipline and the shared-foundations KE.

## AWS pin table
TBD — AWS ACA CloudFormation / IaC modules to be pinned.

## Slides

### Opener
- [BESPOKE] From design to build
  - AT1 is signed off; AT2 begins — you build in the lab, to the approved design.
  - This Topic: what IaC is, then operating a template someone else wrote — including when it fails.
  - Region substitution starts here: the design names its real region, but you deploy to us-east-1 in the lab. Same build, only the console region differs.
  - teach, demo, practice: watch the demo, then do it on the practice workbook.
  image: gen flat vector hero illustration of code turning into cloud infrastructure blocks, blue and gold accents, minimal, no text
  notes:
    Start of the AT2 build arc — workbook tasks 1 to 10 today, in order.
    Say the region substitution out loud: the design still mandates the real region for legal reasons; the lab just can't host it.
    Misconception: us-east-1 means residency doesn't matter. No — substitute and label it.

### C1 — Why IaC, and choosing the service
- Teaches: [ICTCLD505 PC 1.1] · [ICTCLD505 PC 1.2] · [ICTCLD505 PC 1.3] · [ICTCLD505 PC 1.4] · [ICTCLD505 KE 3] · [ICTCLD505 KE 4] · [ICTCLD505 KE 7]
- Kicker: describe infrastructure, don't click it
- [PRIMER] What Infrastructure as Code is
  - IaC describes infrastructure in a text template the platform provisions for you.
  - Benefits over manual console work: repeatable, versioned, reviewable, fast to rebuild.
  - The same template gives the same result every time — no click-to-click drift.
  image: none
  notes:
    Workbook task 1's subject — the benefits are the examinable list; say them as the reasons a professional uses IaC.
    Question to pose: you built it perfectly in the console last week and need it again today — what does the console give you?
- [BESPOKE] What automation gives, and what can go wrong
  - One template stands up many related resources consistently, in the right order, without manual steps.
  - The failure modes are real: drift from manual edits, a bad change rolling a stack back, permission and quota errors.
  - Knowing what can go wrong is part of the competence — it's a workbook task, not a footnote.
  image: none
  notes:
    Workbook tasks 2 and 3 — the upside and the downside, as separate written answers.
    Drift is the one to make concrete: someone hand-edits a deployed resource and the template no longer tells the truth.
- [BESPOKE] Select the infrastructure-as-code service
  - Choose an IaC service compatible with the platform — on AWS, CloudFormation is native.
  - Compatibility is the criterion: the service must speak the platform's resources directly.
  - Record the choice and the reason — it's a decision, and decisions get justified.
  image: none
  notes:
    Workbook task 4. Native versus third-party is worth naming, but the workbook asks for a justified selection, not a survey.
- [EX] The IaC groundwork
  - Workbook — tasks 1, 2, 3 and 4.
  - Record why IaC fits this job, what the automation gives, what can go wrong, and the service you select.
  timer: ~25 min
  image: none
  notes:
    Activity = practice workbook tasks 1–4, all written answers.
    Push past generic answers — each one is about this job and this platform.
- [TAKEAWAYS] Section 1 · The groundwork
  - Repeatable, versioned, reviewable, rebuildable.
  - The failure modes are part of the knowledge.
  - Select the service for compatibility, and justify it.
  image: none

### C2 — Reading a template you were given
- Teaches: [ICTCLD505 PC 2.1] · [ICTCLD505 PC 2.2] · [ICTCLD505 KE 5]
- Kicker: read it before you run it
- [PRIMER] Template syntax
  - The parts: Parameters take inputs, Resources declare what to create, Outputs share results, intrinsic functions wire them together.
  - Resources declare desired state; the platform works out how to reach it.
  - Read top-down: inputs, then resources, then outputs.
  image: none
  notes:
    The anatomy, so students can read one. Declarative is the mindset shift — file order is not execution order.
    Question to pose: the template says a database and a server should exist — who decides the creation order? (the references).
- [BESPOKE] Review the provided template
  - Determine what resources it creates and what depends on what — the build order falls out of the references.
  - Know what a template does before you deploy it; deploying blind is how surprises get expensive.
  - The provided data-store template is the case: read it, list its resources, trace its references.
  image: diagram cfn-template-anatomy
  notes:
    Workbook task 5 — the assessed reading skill. Trace one reference live on the diagram.
    A professional reviews before running; the workbook's table asks for exactly that review.
- [EX] Review the data-store template
  - Workbook — task 5.
  - Review the provided template: the resources it creates, their dependencies, and what the parameters control.
  timer: ~20 min
  image: none
  notes:
    Activity = practice workbook task 5, on the practice template.
    The dependency question is the one to press: how do you know, from the file alone, what must exist first?
- [TAKEAWAYS] Section 2 · Reading
  - Parameters, resources, outputs — read top-down.
  - Desired state, not steps; references make the order.
  - Never deploy what you haven't read.
  image: none

### C3 — Deploy it, fix it, confirm it
- Teaches: [ICTCLD505 PC 2.3] · [ICTCLD505 PC 2.4] · [ICTCLD505 PC 2.6] · [ICTCLD505 PE 1] · [ICTCLD505 PE 3] · [ICTCLD505 KE 6] · [ICTCLD505 KE 7] · [ICTCLD503 PE 4] · [ICTCLD503 KE 5]
- Kicker: the first failure is the cause
- [PRIMER] The tooling, and what failure looks like
  - The console or the CLI executes the template — either tool, same operations.
  - When a deployment fails it rolls back, and the rollback fills the log with consequences, not causes.
  - Find the first failure event and read its reason — that one is the cause.
  image: none
  notes:
    Sets up the deploy-fail-fix run the workbook stages: the practice template fails first time by design.
    The first-CREATE_FAILED discipline is the whole method; the later failures are downstream.
- [DEMO] Deploy, hit the failure, fix it
  - Deploy the provided template in the lab and let it fail.
  - Find the first failure event, read its reason aloud, make the one-line fix, redeploy to success.
  - Confirm the resource exists using the console or CLI — deploy then confirm, every time.
  source: recorded/live demo
  image: none
  notes:
    Live demonstration, educator-led (screen it live or your own capture — no recorded-demos catalogue in CL2).
    Set the region first and say the substitution out loud.
    Narrate the diagnosis before touching anything — model reading over guessing.
    Common errors worth naming as you go: a bad reference, a missing permission, an invalid property, a name clash.
    Prep: clean lab, the practice data-store template to hand. ~8–10 min.
- [BESPOKE] Confirming a deployment
  - A green status is the platform's claim; confirmation is you checking the resource itself.
  - Use the console or the CLI: does the resource exist, with the properties the template declared?
  - Deploy, then confirm — the habit that catches the gap between claimed and real.
  image: none
  notes:
    Workbook task 8 makes confirmation its own task — treat it as one, not as glancing at the status colour.
- [EX] Deploy, diagnose, fix, confirm
  - Workbook — tasks 6, 7 and 8.
  - Deploy the provided template, diagnose and fix the failure it hits, redeploy, and confirm the deployment properly.
  timer: ~30 min
  image: none
  notes:
    Activity = practice workbook tasks 6–8. The failure is planted; hitting it is the exercise, not a mistake.
    Watch for reading the last failure instead of the first, and for random property-poking instead of diagnosis.
- [TAKEAWAYS] Section 3 · Deploy and fix
  - Read the first failure event; the rest is rollback noise.
  - One deliberate fix, then redeploy — diagnosis over trial and error.
  - Confirm the resource, not the status colour.
  image: none

### C4 — Update it, and put it back
- Teaches: [ICTCLD505 PC 2.3] · [ICTCLD505 PC 2.4] · [ICTCLD505 PE 1] · [ICTCLD505 KE 10] · [ICTCLD505 KE 11]
- Kicker: every change is a reviewable diff
- [BESPOKE] Updating through the template
  - To change a deployed stack, change the template — never the live resources by hand.
  - A change set shows the diff before it runs: what will be added, modified, replaced.
  - Review the diff, execute, confirm — the same confirm habit as the deploy.
  image: none
  notes:
    Workbook task 9. Hand-editing a templated resource is drift — connect back to C1's failure modes.
    Pause on the change set in any demo; the review-before-run moment is the teaching.
- [BESPOKE] Return it to a known state
  - A practice environment ends where it began: return the store to its known state.
  - Known state means provable — the template and the deployed reality agree again, and you can say how you know.
  - Stacks you manage through templates go up and come back down the same way.
  image: none
  notes:
    Workbook task 10 — the reset, done through the tooling, confirmed like everything else.
    Full removal is a later closeout task; today is about returning to baseline.
- [EX] Update and reset
  - Workbook — tasks 9 and 10.
  - Update the provided template and redeploy through a change set, then return the store to its known state and show how you know.
  timer: ~25 min
  image: none
  notes:
    Activity = practice workbook tasks 9–10.
    Ask each student what their change set listed before they executed it.
- [TAKEAWAYS] Section 4 · Change and reset
  - Change the template, not the resources.
  - Review the diff before it runs.
  - Known state is provable state.
  image: none

### C5 — Shared cloud foundations
- Teaches: [ICTCLD503 KE 1] · [ICTCLD505 KE 1] · [ICTCLD503 KE 2] · [ICTCLD505 KE 2]
- Kicker: the standards under the build
- [BESPOKE] Standards and standard products
  - Industry technology standards underpin the build: interoperability, security and management baselines.
  - Standard products are what the platform assembles from: compute families, managed databases, object and block storage.
  - This foundation sits under both halves of the build — the templates and the microservice — and it comes back in the written questions.
  image: none
  notes:
    Shared KE across both units, taught once here, assessed in the AT2 written questions at closeout.
    Make it concrete: name one standard product in this build and a baseline it implements.

### Close
- [BESPOKE] Next: Topic 7 — author your own
  - You can read, deploy, fix, update and reset a template someone else wrote.
  - Next you write your own — and what it deploys is the microservice you designed in Topic 2.
  image: none
  notes:
    The Topic 2 design comes back as the build spec — tell them to bring it.

## Build notes
~24 slides. Four activities, mapping to practice workbook tasks 1–4 · 5 · 6–8 · 9–10. One generated
diagram (`diagram cfn-template-anatomy`, already in `diagrams/`); one decorative `gen` opener hero
(cached in `images/`); one DEMO (deploy–fail–fix–confirm; the old separate operate/fix demos merge to
match the workbook's staged failure). Content carried from the 2026-07-01 plan, reordered to the
workbook: troubleshooting now sits inside the deploy run (the practice template fails by design), and
stack deletion moves out to the closeout Topic with the teardown task.

## Changelog
- 2026-09-08 — redrafted from the AT2 practice workbook (tasks 1–10): concepts get a written EX;
  deploy–fail–fix–confirm taught as one run; reset-to-known-state replaces delete.
- 2026-07-01 — authored to full content.
