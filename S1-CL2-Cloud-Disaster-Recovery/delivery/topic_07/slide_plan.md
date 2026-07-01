# Topic 07 Authoring & parameterising your own IaC template — Slide plan
> **Covers:** Topic 07 — see coverage.md
> **Subtitle:** Write your own template from scratch, parameterise it for reuse, redeploy and remove it
> **STATUS: DRAFT** (authored 2026-07-01).

## Depth ceiling
BUILD — the second IaC skill: authoring, not just operating. `teach → demo → practice`. Builds on Topic 6's template anatomy. Deploys in the lab (us-east-1, substituted).

## Teaching source
AWS ACA CloudFormation decks pinned at Step 4 (TBD); bespoke for authoring practice, parameterisation, and industry IaC standards.

## AWS pin table
TBD — AWS ACA CloudFormation authoring / parameters modules to be pinned.

## Slides

### Opener
- [BESPOKE] From operating to authoring
  - Topic 6 operated a provided template; now you write your own from scratch.
  - Same tooling and lifecycle — this time you declare the resources and their relationships.
  - You still deploy to us-east-1 in the lab — `[scenario: ap-southeast-2 (Sydney) | deploy: us-east-1]`.
  - This is the skill you apply to build the microservice template in Topic 8.
  image: gen flat vector hero illustration of a hand writing a template that assembles cloud resources, blue and gold accents, minimal, no text

### C1 — Authoring a template
- Teaches: [ICTCLD505 PC 3.1] · [ICTCLD505 PC 3.2] · [ICTCLD505 PE 2] · [ICTCLD505 KE 9]
- Kicker: declare a related set of resources
- [PRIMER] Authoring from syntax
  - Apply the template syntax to create a template that provisions a set of related resources.
  - Start from the outcome: what resources, what depends on what, what inputs and outputs.
  - Build incrementally — a few resources, deploy, confirm, add more.
  image: none
- [BESPOKE] Industry IaC practice
  - Parameters over hard-coded values; least-privilege on any role; tag every resource.
  - Outputs expose what other stacks/services need — the integration seam (KE 9).
  - Standard practice is what makes a template safe to reuse and hand over.
  image: none
- [DEMO] Author & deploy a template
  - Author a small template (a related resource set) and deploy it in the lab (us-east-1).
  - Confirm the stack reaches CREATE_COMPLETE and the resources exist.
  source: recorded/live demo
  image: none
- [EX] Author your own template
  - On the practice scenario, author a template that provisions a related resource set to a business need.
  - Deploy it to us-east-1 and confirm it.
  timer: ~30 min
  image: none

### C2 — Update & parameterise for reuse
- Teaches: [ICTCLD505 PC 3.3] · [ICTCLD505 PC 3.4] · [ICTCLD505 PC 3.5] · [ICTCLD505 PE 2] · [ICTCLD505 KE 8]
- Kicker: one template, many configurations
- [PRIMER] Parameterisation & reuse
  - Parameterise the template so the same body deploys to different configurations without editing it (KE 8).
  - Region, sizes, names, environment — pass them in, don't bake them in.
  - Parameterisation is the code-reuse outcome: write once, deploy many.
  image: none
- [BESPOKE] Update, redeploy & confirm
  - Update and redeploy the template to modify and add resources — via a change set.
  - Confirm the deployment via console or CLI after each change.
  - Region is itself a parameter — the same template targets us-east-1 in the lab or the design region in production.
  image: none
- [DEMO] Parameterise & redeploy
  - Add parameters to the template, then redeploy with new values to show the same template producing a different configuration.
  source: recorded/live demo
  image: none
- [EX] Parameterise & redeploy
  - On the practice scenario, parameterise your template and redeploy it with different values.
  - Confirm the reconfigured resources.
  timer: ~25 min
  image: none

### C3 — Remove & troubleshoot
- Teaches: [ICTCLD505 PC 3.6] · [ICTCLD505 PC 3.7] · [ICTCLD505 PE 2]
- Kicker: clean up, and fix your own errors
- [BESPOKE] Remove cleanly & troubleshoot
  - Remove the deployed resources and delete the template cleanly — no orphaned resources, no lingering cost.
  - Test and troubleshoot errors in your own template: read the event, diagnose, fix, redeploy.
  - Your own bugs are the best teacher — a bad `!Ref` or property tells you exactly what to fix.
  image: none
- [EX] Remove & troubleshoot
  - On the practice scenario, introduce and fix a template error, then remove the stack cleanly.
  timer: ~20 min
  image: none
- [TAKEAWAYS] Topic 7 · Key takeaways
  - Author a template that provisions a related resource set — declare desired state, build incrementally.
  - Industry practice: parameters over hard-coding, least-privilege, tagging, outputs for integration.
  - Parameterise for reuse — the same template, many configurations (Region included).
  - Update via change sets, confirm each change, and remove cleanly.
  image: none

### Close
- [BESPOKE] Next: Topic 8 — build the microservice
  - You can now author and parameterise your own template.
  - Next you use that skill to provision the serverless audit-log microservice from the supplied code.
  image: none

## Build notes
~15 slides. `teach → demo → practice` on the practice scenario in us-east-1 (substituted). One decorative `gen` image (opener hero); two DEMOs (author, parameterise).

## Changelog
- 2026-07-01 — authored to full content.
