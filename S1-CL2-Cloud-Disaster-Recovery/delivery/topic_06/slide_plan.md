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

### C1 — Why IaC
- Teaches: [ICTCLD505 PC 1.1] · [ICTCLD505 PC 1.2] · [ICTCLD505 PC 1.3] · [ICTCLD505 PC 1.4] · [ICTCLD505 KE 3] · [ICTCLD505 KE 4] · [ICTCLD505 KE 11]
- Kicker: describe infrastructure, don't click it
- [PRIMER] What Infrastructure as Code is
  - IaC describes infrastructure in a text template the platform provisions for you.
  - Benefits over manual console work: repeatable, versioned, reviewable, fast to rebuild (KE 3).
  - The same template gives the same result every time — no click-to-click drift.
  image: none
- [BESPOKE] Automation, risks & choosing a service
  - Automation leverages the platform: one template stands up many related resources consistently.
  - Potential issues: drift from manual edits, a bad change rolling back a stack, permission/quota errors.
  - Choose an IaC service compatible with the platform — on AWS, CloudFormation is native (KE 4); manage/measure deployments by stack status and change sets (KE 11).
  image: none

### C2 — Template anatomy & review
- Teaches: [ICTCLD505 PC 2.1] · [ICTCLD505 PC 2.2] · [ICTCLD505 KE 5]
- Kicker: read a template before you run it
- [PRIMER] Template syntax
  - The parts: Parameters (inputs), Resources (what to create), Outputs (what to share), intrinsic functions (`!Ref`, `!GetAtt`, `!Sub`).
  - Resources declare desired state; the platform works out how to reach it.
  - Learn to read it top-down: inputs → resources → outputs (KE 5).
  image: none
- [BESPOKE] Review a provided template
  - Review a pre-defined template to determine the resources it creates and their dependencies.
  - Trace `!Ref`/`!GetAtt` to see what depends on what — the build order falls out of the references.
  - Know what a template does before you deploy it (the provided data-store template is your AT2 case).
  image: diagram cfn-template-anatomy

### C3 — Operating a provided template
- Teaches: [ICTCLD505 PC 2.3] · [ICTCLD505 PC 2.4] · [ICTCLD505 PC 2.5] · [ICTCLD505 PE 1] · [ICTCLD505 PE 3] · [ICTCLD505 KE 6] · [ICTCLD505 KE 10] · [ICTCLD505 KE 11]
- Kicker: deploy, update, delete — cleanly
- [PRIMER] The template lifecycle & tooling
  - Create → update (change set) → delete: the three operations on a stack.
  - Tooling: the CloudFormation console or the CLI executes the template (KE 6); manage/provision/update via stacks and change sets (KE 10).
  - Every change is a reviewable diff before it runs.
  image: none
- [DEMO] Operate the provided template
  - Deploy the provided template in the lab (Region us-east-1 — `[scenario: ap-southeast-2 (Sydney) | deploy: us-east-1]`).
  - Update a parameter via a change set; confirm the resource in the console/CLI; then delete the stack.
  source: recorded/live demo
  image: none
- [EX] Deploy, update, delete
  - On the practice scenario, deploy the provided template, update a parameter, confirm it, then remove it.
  - Work in us-east-1; the deploy Region is the substitute, the process is identical.
  timer: ~25 min
  image: none

### C4 — Troubleshooting templates
- Teaches: [ICTCLD505 PC 2.6] · [ICTCLD505 KE 7]
- Kicker: read the error, don't guess
- [BESPOKE] Diagnose a template error
  - Test and troubleshoot template errors: read the failure event, find the first CREATE_FAILED, read its reason.
  - Common errors: a bad reference, a missing permission, an invalid property, a name clash (KE 7).
  - Fix the template, redeploy, confirm — diagnosis over trial-and-error.
  image: none
- [DEMO] Fix a broken template
  - Walk a deliberately broken copy: the error event, the diagnosis, the one-line fix, the redeploy.
  source: recorded/live demo
  image: none
- [EX] Troubleshoot the broken copy
  - On the practice scenario, deploy the broken template, read the error, fix it, and redeploy to success.
  timer: ~20 min
  image: none

### C5 — Shared cloud foundations
- Teaches: [ICTCLD503 KE 1] · [ICTCLD505 KE 1] · [ICTCLD503 KE 2] · [ICTCLD505 KE 2]
- Kicker: the standards under the build
- [BESPOKE] Standards & standard products
  - Industry technology standards that underpin cloud building — interoperability, security, and management baselines (KE 1).
  - Standard hardware/software/storage products the platform is built on — compute families, managed databases, object/block storage (KE 2).
  - This is the shared foundation behind both the IaC (505) and the microservice (503) strands.
  image: none

### Close
- [BESPOKE] Next: Topic 7 — author your own template
  - You can now read and operate a provided template; next you write one from scratch.
  - Same tooling, same lifecycle — this time you author the resources.
  image: none

## Build notes
~17 slides. `teach → demo → practice` on the practice scenario in us-east-1 (substituted). One generated diagram (`diagram cfn-template-anatomy`); one decorative `gen` image (opener hero); two DEMOs (operate, fix).

## Changelog
- 2026-07-01 — authored to full content.
