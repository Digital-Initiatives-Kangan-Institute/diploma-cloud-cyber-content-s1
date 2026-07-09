# Topic 06 IaC: fundamentals & operating provided templates — Slide plan
> **Covers:** Topic 06 — see coverage.md
> **Subtitle:** Infrastructure as Code from first principles, then operating a template you were given
> **STATUS: DRAFT** (authored 2026-07-01).

## Depth ceiling
BUILD — first hands-on Topic of AT2. AWS practicals run `teach → demo → practice`. Operate a *provided* template (deploy/update/delete/troubleshoot); authoring your own is Topic 7.

## Teaching source
AWS ACA CloudFormation / IaC decks pinned at Step 4 (TBD); bespoke for the supplied-template discipline and the shared-foundations KE.

## AWS pin table
TBD — AWS ACA CloudFormation / IaC modules to be pinned.

## Slides

### Opener
- [BESPOKE] From design to build
  - AT1 is signed off; AT2 begins — you build in the lab, to the approved design.
  - This Topic: what IaC is, and operating a template someone else wrote.
  - Region substitution starts here: the design targets Sydney/India, but you deploy to us-east-1 — `[scenario: ap-southeast-2 (Sydney) | deploy: us-east-1]`. Same build, only the console Region differs.
  - `teach → demo → practice`: watch the demo, then do it on the practice scenario.
  image: gen flat vector hero illustration of code turning into cloud infrastructure blocks, blue and gold accents, minimal, no text
  notes:
    Frame Topic 6 as the START of AT2 — the design is signed off; now you build it in the lab. Set the mode
    and the two conventions (Region substitution, teach→demo→practice); don't teach CloudFormation yet.
    • First bullet: AT1 is signed off; AT2 begins — you build in the lab, TO the approved design. The design
    is settled; your job is faithful implementation.
    • Second bullet: scope today — what IaC is, and OPERATING a template someone else wrote (authoring your
    own is Topic 7).
    • Third bullet (say it explicitly): Region substitution starts here — the design targets Sydney/India,
    but you deploy to us-east-1 in the Learner Lab: [scenario: ap-southeast-2 (Sydney) | deploy: us-east-1].
    Same build; only the console Region label differs.
    • Fourth bullet: the rhythm for every AWS practical — teach → demo → practice. Watch the demo, then do it
    on the practice scenario.
    Misconception to pre-empt: "us-east-1 means residency doesn't matter." No — the DESIGN still mandates the
    onshore Region for legal reasons; the lab just can't host it, so we substitute and label it.
    Question to pose: "Why describe infrastructure in a template at all, instead of just clicking it in the
    console?" (repeatable, versioned, reviewable — teased here, answered in C1).
    UoC/AT2 tie: opens the AT2 build arc — ICTCLD505 (IaC) primary; today feeds AT2 §4.2 (operate the
    provided data-store template).

### C1 — Why IaC
- Teaches: [ICTCLD505 PC 1.1] · [ICTCLD505 PC 1.2] · [ICTCLD505 PC 1.3] · [ICTCLD505 PC 1.4] · [ICTCLD505 KE 3] · [ICTCLD505 KE 4] · [ICTCLD505 KE 11]
- Kicker: describe infrastructure, don't click it
- [PRIMER] What Infrastructure as Code is
  - IaC describes infrastructure in a text template the platform provisions for you.
  - Benefits over manual console work: repeatable, versioned, reviewable, fast to rebuild (KE 3).
  - The same template gives the same result every time — no click-to-click drift.
  image: none
  notes:
    Vendor-neutral primer — install the core idea of IaC before any AWS specifics.
    • First bullet: IaC describes infrastructure in a TEXT TEMPLATE the platform then provisions for you —
    you declare what you want, the platform builds it.
    • Second bullet: walk the benefits over manual console work — repeatable, versioned, reviewable, fast to
    rebuild. These four are KE 3; say them as the reasons a professional uses IaC.
    • Third bullet: the same template gives the same result every time — no click-to-click drift between two
    people or two environments. Determinism is the whole point.
    Misconception to pre-empt: "IaC is just a faster way to click." No — it's a fundamentally different
    model: you version and review the DESCRIPTION of infrastructure like source code, and rebuild from it.
    Question to pose: "You built something perfectly in the console last week and need it again in a new
    account today — what does the console give you vs a template?" (memory/screenshots vs a repeatable
    artefact).
    UoC/AT2 tie: ICTCLD505 PC 1.1 (benefits of IaC) + KE 3 (IaC vs manual provisioning) → AT2 §4.2 / §8.
- [BESPOKE] Automation, risks & choosing a service
  - Automation leverages the platform: one template stands up many related resources consistently.
  - Potential issues: drift from manual edits, a bad change rolling back a stack, permission/quota errors.
  - Choose an IaC service compatible with the platform — on AWS, CloudFormation is native (KE 4); manage/measure deployments by stack status and change sets (KE 11).
  image: none
  notes:
    Bespoke — the three remaining C1 ideas: how automation leverages the platform, what can go wrong, and
    choosing the service. Balance the benefits slide with the risks.
    • First bullet: automation LEVERAGES the platform — one template stands up many related resources
    consistently, in the right order, without manual steps.
    • Second bullet: the potential ISSUES (students must know these, not just the upside) — drift from
    manual edits, a bad change rolling back a whole stack, permission/quota errors. Name them plainly.
    • Third bullet: choose an IaC service COMPATIBLE with the platform — on AWS, CloudFormation is native;
    manage/measure deployments by stack status and change sets.
    Misconception to pre-empt: "IaC removes all risk." No — it introduces its OWN failure modes (drift,
    rollbacks, quota/permission errors); knowing them is part of using it well and is examined.
    Question to pose: "Someone tweaks a resource by hand after it was deployed from a template — what problem
    have they just created?" (drift — the template and reality no longer match).
    UoC/AT2 tie: ICTCLD505 PC 1.2 (automation leverages platforms) + PC 1.3 (potential issues) + PC 1.4 /
    KE 4 (select a compatible service) + KE 11 (manage/measure via stack status, change sets) → AT2 §5/§8.

### C2 — Template anatomy & review
- Teaches: [ICTCLD505 PC 2.1] · [ICTCLD505 PC 2.2] · [ICTCLD505 KE 5]
- Kicker: read a template before you run it
- [PRIMER] Template syntax
  - The parts: Parameters (inputs), Resources (what to create), Outputs (what to share), intrinsic functions (`!Ref`, `!GetAtt`, `!Sub`).
  - Resources declare desired state; the platform works out how to reach it.
  - Learn to read it top-down: inputs → resources → outputs (KE 5).
  image: none
  notes:
    Primer — the anatomy of a template so students can READ one. Vendor-neutral framing, AWS examples.
    • First bullet: the parts — Parameters (inputs), Resources (what to create), Outputs (what to share),
    and intrinsic functions (!Ref, !GetAtt, !Sub) that wire them together. Name each part's job.
    • Second bullet: resources declare DESIRED STATE — you say what you want to exist; the platform works
    out how to reach it. This is the declarative mindset (contrast with scripting each step).
    • Third bullet: read a template TOP-DOWN — inputs → resources → outputs. Give them the reading order
    they'll use on the provided template next slide.
    Misconception to pre-empt: "a template is a script that runs line by line." No — it's a DECLARATION of
    the end state; the platform decides order and method. Order in the file isn't execution order.
    Question to pose: "If a template just says 'this database and this server should exist,' who decides the
    order they're created in?" (the platform, from the dependencies/references — not you).
    UoC/AT2 tie: ICTCLD505 PC 2.1 (template syntax) + KE 5 (template syntax) → AT2 §4.2 (read the provided
    template before operating it).
- [BESPOKE] Review a provided template
  - Review a pre-defined template to determine the resources it creates and their dependencies.
  - Trace `!Ref`/`!GetAtt` to see what depends on what — the build order falls out of the references.
  - Know what a template does before you deploy it (the provided data-store template is your AT2 case).
  image: diagram cfn-template-anatomy
  notes:
    Bespoke — the assessed skill of READING a template you were given, before running it. Use the anatomy
    diagram to point at each part live.
    • First bullet: review a pre-defined template to determine the RESOURCES it creates and their
    DEPENDENCIES — what will exist and what relies on what.
    • Second bullet: trace !Ref / !GetAtt to see what depends on what — the build ORDER falls out of the
    references, you don't specify it. Follow a reference on the diagram as you say this.
    • Third bullet (the point): know what a template does BEFORE you deploy it. The provided data-store
    template is your AT2 case — reading it is the graded skill, not just running it.
    Misconception to pre-empt: "just deploy it and see what happens." No — a professional reviews the
    template first; deploying blind into a real account can create cost or clash with existing resources.
    Question to pose: "How can you tell, from the template alone, that the database must exist before the app
    server?" (the app resource !Refs the database — the reference creates the dependency).
    UoC/AT2 tie: ICTCLD505 PC 2.2 (review pre-defined templates; determine resources & dependencies) + KE 5
    → AT2 §4.2 (operate the PROVIDED DynamoDB template — criterion D2).

### C3 — Operating a provided template
- Teaches: [ICTCLD505 PC 2.3] · [ICTCLD505 PC 2.4] · [ICTCLD505 PC 2.5] · [ICTCLD505 PE 1] · [ICTCLD505 PE 3] · [ICTCLD505 KE 6] · [ICTCLD505 KE 10] · [ICTCLD505 KE 11]
- Kicker: deploy, update, delete — cleanly
- [PRIMER] The template lifecycle & tooling
  - Create → update (change set) → delete: the three operations on a stack.
  - Tooling: the CloudFormation console or the CLI executes the template (KE 6); manage/provision/update via stacks and change sets (KE 10).
  - Every change is a reviewable diff before it runs.
  image: none
  notes:
    Primer — the operational lifecycle of a template and the tooling that runs it, right before the demo.
    • First bullet: the three operations on a stack — create → update (via a CHANGE SET) → delete. That's
    the whole lifecycle of operating a template.
    • Second bullet: tooling — the CloudFormation console OR the CLI executes the template; you
    manage/provision/update via stacks and change sets. Either tool, same operations.
    • Third bullet (the safety point): every change is a REVIEWABLE DIFF before it runs — a change set shows
    you exactly what will change before you commit. You look before you leap.
    Misconception to pre-empt: "updating means editing the live resources directly." No — you edit the
    template and apply it; the change set computes the diff and the platform makes the changes. Don't
    hand-edit resources a template owns (that's drift).
    Question to pose: "Before you apply an update to a running stack, what should you look at first?" (the
    change set — the diff of what will be added/modified/removed).
    UoC/AT2 tie: ICTCLD505 PC 2.3–2.5 (deploy/update/delete; confirm; remove) + PE 1 + PE 3 + KE 6/10/11 →
    AT2 §4.2 (operate the provided template — D2).
- [DEMO] Operate the provided template
  - Deploy the provided template in the lab (Region us-east-1 — `[scenario: ap-southeast-2 (Sydney) | deploy: us-east-1]`).
  - Update a parameter via a change set; confirm the resource in the console/CLI; then delete the stack.
  source: recorded/live demo
  image: none
  notes:
    LIVE DEMONSTRATION (educator-led — screen it live in the lab, or a screen capture you record yourself;
    CL2 has no recorded-demos catalogue). Demonstrate the COURSE'S OWN provided template against the
    lab-pack, then students replicate on the next slide.

    WHAT TO DEMONSTRATE (step by step, in the Learner Lab, Region us-east-1 —
    [scenario: ap-southeast-2 (Sydney) | deploy: us-east-1]):
    1. Open the provided data-store template; point out its Parameters/Resources/Outputs (tie back to the
    anatomy slide).
    2. Create the stack; watch the events to CREATE_COMPLETE; confirm the resource in the console.
    3. Make a change SET on one parameter, review the diff, then execute it; confirm the resource changed.
    4. Delete the stack; confirm the resources are removed (no orphans left behind).

    WHAT TO EMPHASISE:
    • Set the Region to us-east-1 FIRST and say the substitution out loud — everything is Region-scoped.
    • The change set is a DIFF you review BEFORE it runs — pause on it deliberately; don't rush past it.
    • Confirm at each step (console/CLI) rather than assuming — deploy → confirm is the habit.
    • Delete cleanly at the end — leaving stacks running costs money and clutters the account.

    PREP: clean Learner Lab open, the provided data-store template to hand, Region already thought about.
    ~8–10 min to screen + narrate before the activity.
- [EX] Deploy, update, delete
  - On the practice scenario, deploy the provided template, update a parameter, confirm it, then remove it.
  - Work in us-east-1; the deploy Region is the substitute, the process is identical.
  timer: ~25 min
  image: none
  notes:
    Facilitation — the C3 practice; students operate the provided template through its full lifecycle on
    the practice scenario. They do what you just demoed.
    Tell students, in these words: "On the practice scenario, deploy the provided template, update a
    parameter via a change set, confirm it, then remove it. Work in us-east-1 — the deploy Region is the
    substitute, the process is identical."
    Steps (put on the board):
    1. Set the Region to us-east-1 — [scenario: ap-southeast-2 (Sydney) | deploy: us-east-1].
    2. Deploy the provided template; wait for CREATE_COMPLETE; confirm the resource in the console/CLI.
    3. Update one parameter via a change set — review the diff, then execute; confirm the change.
    4. Delete the stack; confirm everything is removed.
    Must produce: a stack taken cleanly through create → update → delete, confirmed at each step.
    Timing: ~25 min. Where they get stuck: forgetting to set Region first; and trying to change the resource
    by hand instead of via a change set — circulate and redirect them to the template/change set.
    Share-back prompt: "What did the change set show you BEFORE you applied it?" (the diff — reinforce the
    review-before-run habit).
    No-leakage note: practice scenario template — AT2 §4.2 operates the provided data-store template on a
    different case (comparable, not identical); keep them on the practice template here.

### C4 — Troubleshooting templates
- Teaches: [ICTCLD505 PC 2.6] · [ICTCLD505 KE 7]
- Kicker: read the error, don't guess
- [BESPOKE] Diagnose a template error
  - Test and troubleshoot template errors: read the failure event, find the first CREATE_FAILED, read its reason.
  - Common errors: a bad reference, a missing permission, an invalid property, a name clash (KE 7).
  - Fix the template, redeploy, confirm — diagnosis over trial-and-error.
  image: none
  notes:
    Bespoke — teach diagnosis as a METHOD, not guesswork. This is the thinking behind the "fix a broken
    template" demo that follows.
    • First bullet: to troubleshoot, read the FAILURE EVENT — find the FIRST CREATE_FAILED in the stack
    events and read its reason. The first failure is the cause; the rest are knock-on.
    • Second bullet: the common errors (KE 7) — a bad reference, a missing permission, an invalid property,
    a name clash. Knowing the usual suspects speeds diagnosis.
    • Third bullet: fix the template, redeploy, confirm — diagnosis OVER trial-and-error. You reason from
    the error message, you don't poke randomly.
    Misconception to pre-empt: "when a stack fails, start changing things until it works." No — read the
    first CREATE_FAILED event and its reason; the message usually tells you exactly what's wrong. Random
    changes create new failures.
    Question to pose: "A stack shows five failed resources — which one do you read first, and why?" (the
    FIRST CREATE_FAILED — the others likely failed because it did).
    UoC/AT2 tie: ICTCLD505 PC 2.6 (test & troubleshoot template errors) + KE 7 (testing/debugging, common
    errors) → AT2 §4.2 (operate the provided template, incl. recovering from a failure).
- [DEMO] Fix a broken template
  - Walk a deliberately broken copy: the error event, the diagnosis, the one-line fix, the redeploy.
  source: recorded/live demo
  image: none
  notes:
    LIVE DEMONSTRATION (educator-led — screen it live, or your own screen capture; no recorded-demos
    catalogue in CL2). Walk a DELIBERATELY BROKEN copy of the provided template against the lab-pack, then
    students replicate on the next slide.

    WHAT TO DEMONSTRATE (in the Learner Lab, us-east-1):
    1. Deploy the deliberately broken template; let it fail.
    2. Open the stack events; scroll to the FIRST CREATE_FAILED and read its reason out loud.
    3. Diagnose from the message (e.g. a bad !Ref, an invalid property, a name clash — the KE 7 suspects).
    4. Make the one-line fix in the template; redeploy; confirm it reaches CREATE_COMPLETE.

    WHAT TO EMPHASISE:
    • Model reading the error BEFORE touching anything — narrate the diagnosis, don't just fix it silently.
    • It's the FIRST failure that matters — show how the later failures were downstream of it.
    • One deliberate fix, then redeploy — reinforce diagnosis over trial-and-error.
    • Clean up (delete the stack) at the end.

    PREP: have a broken copy of the provided template ready (a single planted error), the events view
    familiar, lab open in us-east-1. ~6–8 min to screen + narrate before the activity.
- [EX] Troubleshoot the broken copy
  - On the practice scenario, deploy the broken template, read the error, fix it, and redeploy to success.
  timer: ~20 min
  image: none
  notes:
    Facilitation — the C4 practice; students diagnose and fix the broken template on the practice scenario.
    They apply the method you just demoed.
    Tell students, in these words: "On the practice scenario, deploy the broken template, read the error,
    fix it, and redeploy to success."
    Steps (put on the board):
    1. Deploy the broken template in us-east-1; let it fail.
    2. Open the stack events; find the FIRST CREATE_FAILED and read its reason.
    3. Diagnose (bad reference / missing permission / invalid property / name clash) and make the fix.
    4. Redeploy; confirm CREATE_COMPLETE; then delete the stack.
    Must produce: the once-broken stack redeployed to success, plus a one-line statement of what the error
    was and how they knew.
    Timing: ~20 min. Where they get stuck: they read the LAST failure not the first, or start changing
    random properties — circulate and point them at the first CREATE_FAILED and its message.
    Share-back prompt: "What did the first failure event actually say, and what did that tell you to fix?"
    No-leakage note: practice scenario — AT2 assesses troubleshooting on the provided data-store template
    (comparable, not identical).

### C5 — Shared cloud foundations
- Teaches: [ICTCLD503 KE 1] · [ICTCLD505 KE 1] · [ICTCLD503 KE 2] · [ICTCLD505 KE 2]
- Kicker: the standards under the build
- [BESPOKE] Standards & standard products
  - Industry technology standards that underpin cloud building — interoperability, security, and management baselines (KE 1).
  - Standard hardware/software/storage products the platform is built on — compute families, managed databases, object/block storage (KE 2).
  - This is the shared foundation behind both the IaC (505) and the microservice (503) strands.
  image: none
  notes:
    Bespoke — the shared-foundations KE: the standards and standard products under the build. This is
    knowledge shared across BOTH units (503 and 505), so teach it once here.
    • First bullet: industry technology STANDARDS that underpin cloud building — interoperability, security,
    and management baselines (KE 1). These are the agreed rules that make cloud components work together and
    stay secure.
    • Second bullet: standard PRODUCTS the platform is built on (KE 2) — compute families, managed
    databases, object/block storage. The building blocks you assemble, not things you invent.
    • Third bullet: this is the shared foundation behind both the IaC strand (505) and the microservice
    strand (503) — flag that it earns marks in the written KE appendix, assembled in Topic 10.
    Misconception to pre-empt: "standards are abstract theory with no bearing on my build." No — they're why
    your template's resources interoperate and why the managed products behave predictably; it's the ground
    the whole build stands on.
    Question to pose: "Name a standard PRODUCT you'll use in this build and a standard it depends on." (e.g.
    a managed database + the security/interoperability baselines it implements).
    UoC/AT2 tie: ICTCLD503 KE 1/KE 2 + ICTCLD505 KE 1/KE 2 (industry standards + standard hardware/software/
    storage) → the AT2 written KE appendix (§8, assembled in Topic 10).

### Close
- [BESPOKE] Next: Topic 7 — author your own template
  - You can now read and operate a provided template; next you write one from scratch.
  - Same tooling, same lifecycle — this time you author the resources.
  image: none

## Build notes
~17 slides. `teach → demo → practice` on the practice scenario in us-east-1 (substituted). One generated diagram (`diagram cfn-template-anatomy`); one decorative `gen` image (opener hero); two DEMOs (operate, fix).

## Changelog
- 2026-07-01 — authored to full content.
