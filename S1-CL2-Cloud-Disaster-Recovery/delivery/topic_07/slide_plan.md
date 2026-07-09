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
  notes:
    Frame Topic 7 as the step up from Topic 6 — you operated a template someone else wrote; now you AUTHOR
    your own. Set the mode; don't teach syntax yet.
    • First bullet: Topic 6 operated a PROVIDED template; now you write your OWN from scratch. The skill
    shifts from reading to producing.
    • Second bullet: same tooling and lifecycle as Topic 6 — this time YOU declare the resources and their
    relationships, rather than reading someone else's declarations.
    • Third bullet: still deploy to us-east-1 in the lab — [scenario: ap-southeast-2 (Sydney) | deploy:
    us-east-1]. The substitution convention carries over unchanged.
    • Fourth bullet (why it matters): this is the skill you APPLY in Topic 8 to build the microservice
    template. Today is the general skill; Topic 8 is the real artefact.
    Misconception to pre-empt: "authoring is just editing the provided template." No — you start from the
    OUTCOME (what resources, what relationships) and declare them yourself; editing someone else's is still
    operating, not authoring.
    Question to pose: "When you write a template from scratch, what do you decide that you only READ in
    Topic 6?" (the resources, their dependencies, the parameters and outputs — the design of the template).
    UoC/AT2 tie: opens the author-your-own arc — ICTCLD505 element 3 (PE 2, at least one own template) →
    AT2 §4.3 (the student's own microservice template).

### C1 — Authoring a template
- Teaches: [ICTCLD505 PC 3.1] · [ICTCLD505 PC 3.2] · [ICTCLD505 PE 2] · [ICTCLD505 KE 9]
- Kicker: declare a related set of resources
- [PRIMER] Authoring from syntax
  - Apply the template syntax to create a template that provisions a set of related resources.
  - Start from the outcome: what resources, what depends on what, what inputs and outputs.
  - Build incrementally — a few resources, deploy, confirm, add more.
  image: none
  notes:
    Primer — how to actually author a template: apply the syntax to build a related resource set.
    • First bullet: apply the template syntax (from Topic 6) to CREATE a template that provisions a SET of
    RELATED resources — not one resource, a related set that works together.
    • Second bullet: start from the OUTCOME — what resources, what depends on what, what inputs and outputs.
    Design the template before you type it.
    • Third bullet: build INCREMENTALLY — a few resources, deploy, confirm, add more. Don't write 200 lines
    then deploy and drown in errors.
    Misconception to pre-empt: "write the whole template, then deploy once at the end." No — incremental
    authoring (deploy early, deploy often) catches each error in isolation; a big-bang deploy buries the
    first failure under many.
    Question to pose: "Before you type a single resource, what three things should you have decided?" (what
    resources, their dependencies, and the inputs/outputs).
    UoC/AT2 tie: ICTCLD505 PC 3.1 (template syntax) + PC 3.2 (create & deploy a related resource set) + PE 2
    (at least one own template) → AT2 §4.3 (D3).
- [BESPOKE] Industry IaC practice
  - Parameters over hard-coded values; least-privilege on any role; tag every resource.
  - Outputs expose what other stacks/services need — the integration seam (KE 9).
  - Standard practice is what makes a template safe to reuse and hand over.
  image: none
  notes:
    Bespoke — the industry-standard practices that make an authored template professional. KE 9. Teach as a
    checklist they'll be judged against.
    • First bullet: PARAMETERS over hard-coded values; LEAST-PRIVILEGE on any role; TAG every resource.
    Three habits that separate a professional template from a throwaway.
    • Second bullet: OUTPUTS expose what other stacks/services need — the integration seam (KE 9). Outputs
    are how your template plugs into the rest of the system.
    • Third bullet (the why): standard practice is what makes a template safe to REUSE and to HAND OVER.
    You're building something someone else will run — write it so they can.
    Misconception to pre-empt: "hard-coding values is fine, it works." It runs, but it can't be reused or
    safely handed over — the same template can't target another environment, and a broad role is a security
    finding. "It works" isn't the bar; "safe to reuse and hand over" is.
    Question to pose: "Your template hard-codes the Region and grants AdministratorAccess to a role — name
    the two industry practices you've just broken." (parameterisation; least privilege).
    UoC/AT2 tie: ICTCLD505 KE 9 (industry-standard practices to define IaC) + PC 3.2 → AT2 §4.3 + §5 config
    decisions (D3/D8).
- [DEMO] Author & deploy a template
  - Author a small template (a related resource set) and deploy it in the lab (us-east-1).
  - Confirm the stack reaches CREATE_COMPLETE and the resources exist.
  source: recorded/live demo
  image: none
  notes:
    LIVE DEMONSTRATION (educator-led — screen it live, or your own screen capture; CL2 has no recorded-demos
    catalogue). Author a small template FROM SCRATCH against the lab-pack, then students replicate on the
    next slide.

    WHAT TO DEMONSTRATE (in the Learner Lab, us-east-1 —
    [scenario: ap-southeast-2 (Sydney) | deploy: us-east-1]):
    1. Start from the outcome — state the small related resource set you'll create and the dependency
    between them.
    2. Author the template incrementally — write a couple of resources, applying the industry practices
    (a parameter instead of a hard-coded value, a tag, least privilege on any role).
    3. Deploy it; watch it reach CREATE_COMPLETE.
    4. Confirm the resources exist in the console/CLI.

    WHAT TO EMPHASISE:
    • Design BEFORE typing — say the resources and dependencies out loud first.
    • Build incrementally — deploy the small set, confirm, and note how you'd add more; don't write it all
    at once.
    • Point at each industry practice AS you write it (parameter, tag, least-privilege role) — model the
    habits from the previous slide.
    • Set Region us-east-1 first and name the substitution.

    PREP: clean Learner Lab in us-east-1, a small resource set in mind (e.g. a couple of related resources
    with one dependency), editor ready. ~8–10 min to screen + narrate before the activity.
- [EX] Author your own template
  - On the practice scenario, author a template that provisions a related resource set to a business need.
  - Deploy it to us-east-1 and confirm it.
  timer: ~30 min
  image: none
  notes:
    Facilitation — the C1 practice; students author their OWN template on the practice scenario. First
    from-scratch authoring — expect it to be slower than operating.
    Tell students, in these words: "On the practice scenario, author a template that provisions a related
    resource set to a business need. Deploy it to us-east-1 and confirm it."
    Steps (put on the board):
    1. Decide the outcome first — what related resources, what depends on what, inputs and outputs.
    2. Author incrementally — a couple of resources, apply the industry practices (parameters, tags,
    least-privilege), deploy, confirm, add more.
    3. Deploy in us-east-1 — [scenario: ap-southeast-2 (Sydney) | deploy: us-east-1] — to CREATE_COMPLETE;
    confirm the resources.
    Must produce: their own working template that deploys a related resource set to CREATE_COMPLETE,
    confirmed.
    Timing: ~30 min (authoring is slower). Where they get stuck: syntax errors (a bad !Ref, indentation) and
    trying to write it all before deploying — push them to deploy a tiny version early and grow it.
    Share-back prompt: "What was your first CREATE_FAILED, and what fixed it?" (normalises debugging your own
    template).
    No-leakage note: practice scenario — AT2 §4.3 has students author their OWN microservice template on a
    different case (comparable, not identical); keep them on the practice need here.

### C2 — Update & parameterise for reuse
- Teaches: [ICTCLD505 PC 3.3] · [ICTCLD505 PC 3.4] · [ICTCLD505 PC 3.5] · [ICTCLD505 PE 2] · [ICTCLD505 KE 8]
- Kicker: one template, many configurations
- [PRIMER] Parameterisation & reuse
  - Parameterise the template so the same body deploys to different configurations without editing it (KE 8).
  - Region, sizes, names, environment — pass them in, don't bake them in.
  - Parameterisation is the code-reuse outcome: write once, deploy many.
  image: none
  notes:
    Primer — parameterisation as the code-reuse outcome. This is the "aha" of IaC: one template, many
    configurations.
    • First bullet: parameterise the template so the SAME body deploys to different configurations WITHOUT
    editing it (KE 8). The template stays fixed; the values change at deploy time.
    • Second bullet: the things you pass IN, not bake in — Region, sizes, names, environment. Anything that
    varies between deployments is a parameter.
    • Third bullet (the point): parameterisation IS the code-reuse outcome — write once, deploy many. This is
    why parameters matter, not just how.
    Misconception to pre-empt: "to deploy to a different environment I copy the template and edit it." No —
    that's two templates to maintain and they drift apart. One parameterised template, different values in.
    Question to pose: "You need dev, test and prod versions of the same infrastructure — do you write three
    templates?" (No — one template, three sets of parameter values).
    UoC/AT2 tie: ICTCLD505 PC 3.5 (parameterise & deploy to reuse) + KE 8 (parameterisation for config &
    code reuse) → AT2 §4.3 + §5 (D3/D8).
- [BESPOKE] Update, redeploy & confirm
  - Update and redeploy the template to modify and add resources — via a change set.
  - Confirm the deployment via console or CLI after each change.
  - Region is itself a parameter — the same template targets us-east-1 in the lab or the design region in production.
  image: none
  notes:
    Bespoke — updating an authored template safely and confirming it, and the Region-as-parameter payoff.
    • First bullet: UPDATE and redeploy to modify AND add resources — via a CHANGE SET (the same
    review-the-diff discipline from Topic 6, now on your own template).
    • Second bullet: CONFIRM the deployment via console or CLI after each change — deploy → confirm, every
    time.
    • Third bullet (the neat payoff): Region is itself a PARAMETER — the same template targets us-east-1 in
    the lab OR the design Region in production. This is exactly the [scenario | deploy] substitution
    expressed as a parameter.
    Misconception to pre-empt: "to add a resource I tear down and rebuild the stack." No — you update via a
    change set; the platform adds/modifies in place and shows you the diff first. Rebuilding loses state and
    data.
    Question to pose: "Why is 'Region as a parameter' the cleanest way to handle our scenario/deploy
    substitution?" (one template, deploy to us-east-1 in the lab or the design Region in prod — no editing).
    UoC/AT2 tie: ICTCLD505 PC 3.3 (update & redeploy) + PC 3.4 (confirm via console/CLI) + PE 2 → AT2 §4.3
    (D3).
- [DEMO] Parameterise & redeploy
  - Add parameters to the template, then redeploy with new values to show the same template producing a different configuration.
  source: recorded/live demo
  image: none
  notes:
    LIVE DEMONSTRATION (educator-led — screen it live, or your own screen capture; no recorded-demos
    catalogue in CL2). Take the template you authored in the C1 demo and PARAMETERISE it against the
    lab-pack, then students replicate on the next slide.

    WHAT TO DEMONSTRATE (in the Learner Lab, us-east-1):
    1. Take a value that was hard-coded (e.g. a name, size, or the Region) and turn it into a Parameter.
    2. Redeploy the SAME template with one set of values; confirm the configuration.
    3. Redeploy AGAIN with different values (change set); show the SAME template producing a DIFFERENT
    configuration.
    4. Confirm the reconfigured resources in the console/CLI.

    WHAT TO EMPHASISE:
    • The template BODY didn't change between the two deploys — only the parameter values. That's the reuse
    point made visible.
    • Use the change set to show the diff before the second deploy — review before run.
    • Confirm after each redeploy — don't assume it worked.
    • Tie Region-as-parameter to the [scenario | deploy] substitution.

    PREP: the C1-demo template to hand, one obvious value to parameterise, lab open in us-east-1.
    ~6–8 min to screen + narrate before the activity.
- [EX] Parameterise & redeploy
  - On the practice scenario, parameterise your template and redeploy it with different values.
  - Confirm the reconfigured resources.
  timer: ~25 min
  image: none
  notes:
    Facilitation — the C2 practice; students parameterise their own template and prove reuse by redeploying
    with different values.
    Tell students, in these words: "On the practice scenario, parameterise your template and redeploy it
    with different values. Confirm the reconfigured resources."
    Steps (put on the board):
    1. Pick a hard-coded value in your template (name, size, or Region) and make it a Parameter.
    2. Redeploy with one set of values via a change set; confirm.
    3. Redeploy AGAIN with different values; confirm the SAME template produced a different configuration.
    Must produce: one parameterised template deployed twice with different values, each confirmed — reuse
    demonstrated.
    Timing: ~25 min. Where they get stuck: they edit the template body instead of just the parameter values
    (defeats the point) — insist the body stays fixed between the two deploys; and parameter type/default
    errors.
    Share-back prompt: "Prove your template is reusable — what changed between your two deploys, and what
    stayed the same?" (values changed; body fixed).
    No-leakage note: practice scenario — AT2 §4.3 assesses parameterisation on the student's own
    microservice template (comparable, not identical).

### C3 — Remove & troubleshoot
- Teaches: [ICTCLD505 PC 3.6] · [ICTCLD505 PC 3.7] · [ICTCLD505 PE 2]
- Kicker: clean up, and fix your own errors
- [BESPOKE] Remove cleanly & troubleshoot
  - Remove the deployed resources and delete the template cleanly — no orphaned resources, no lingering cost.
  - Test and troubleshoot errors in your own template: read the event, diagnose, fix, redeploy.
  - Your own bugs are the best teacher — a bad `!Ref` or property tells you exactly what to fix.
  image: none
  notes:
    Bespoke — the two C3 skills: clean removal and troubleshooting your OWN template. Close the lifecycle.
    • First bullet: remove the deployed resources and DELETE the template cleanly — no orphaned resources, no
    lingering cost. Deleting the stack should leave nothing behind.
    • Second bullet: test and troubleshoot errors in your OWN template — read the event, diagnose, fix,
    redeploy (the Topic 6 method, now on code you wrote).
    • Third bullet (the encouragement): your own bugs are the best teacher — a bad !Ref or property tells you
    exactly what to fix. Debugging your own template is how the skill sticks.
    Misconception to pre-empt: "if a delete fails, just leave it — it's gone from my view." No — orphaned
    resources keep costing money and can block a rebuild; confirm the delete actually removed everything.
    Question to pose: "You delete your stack but a resource lingers — why does that matter, and what do you
    check?" (ongoing cost / clashes on rebuild; check the delete events and the console for orphans).
    UoC/AT2 tie: ICTCLD505 PC 3.6 (remove resources; delete templates) + PC 3.7 (troubleshoot own template
    errors) + PE 2 → AT2 §4.3 (D3).
- [EX] Remove & troubleshoot
  - On the practice scenario, introduce and fix a template error, then remove the stack cleanly.
  timer: ~20 min
  image: none
  notes:
    Facilitation — the C3 practice; students introduce and fix an error in their own template, then remove
    the stack cleanly. Closes the author-your-own lifecycle.
    Tell students, in these words: "On the practice scenario, introduce and fix a template error, then remove
    the stack cleanly."
    Steps (put on the board):
    1. Introduce a deliberate error into your own template (e.g. a bad !Ref or an invalid property).
    2. Deploy; read the first CREATE_FAILED event; diagnose and fix; redeploy to success.
    3. Remove the stack cleanly; confirm no resources are left behind.
    Must produce: a template broken and fixed by its author, then a clean teardown with no orphaned
    resources.
    Timing: ~20 min. Where they get stuck: fixing by trial-and-error instead of reading the first failure;
    and assuming delete worked — make them confirm the teardown in the console.
    Share-back prompt: "What error did you plant, how did the event tell you, and did your teardown leave
    anything behind?"
    No-leakage note: practice scenario — AT2 §4.3 assesses troubleshooting + clean removal on the student's
    own microservice template (comparable, not identical).
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
