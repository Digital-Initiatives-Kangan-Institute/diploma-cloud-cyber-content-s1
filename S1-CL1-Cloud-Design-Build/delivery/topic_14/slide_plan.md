# Topic 14 Implementing the design — Slide plan
> **Covers:** Topic 14 — see coverage.md
> **STATUS: DRAFT — redrafted 2026-08-28 from the AT3 practice workbook, Part B tasks 19–24. Teacher
> `notes:` not yet authored. `coverage.md` not yet reconciled.**

## Depth ceiling
Apply your own design to a running environment, in the order you planned. Cross-zone only. Proving it
works is Topic 15.

**Answer discipline:** every build task here is built *from the student's own Part A answer*. The slides
teach how to work from your own design and what to expect from the platform. They must not state what
the design should have been.

## Teaching source
Bespoke for the build-from-your-own-design discipline and the waiting behaviour. AWS-sourced for the
cross-zone build (ACA M10 S44).

## AWS pin table
ACA M10 S44 (recorded demo — creating a highly available application); ACA M11 (infrastructure as code,
light).

## Slides

### Opener
- [BESPOKE] Build what you designed
  - You are not being told what to build today. You are building your own design, in your own order.
  - Each task names the design task it comes from. Copy your answer across first, then build exactly that — not what you now wish you had written.
  - If a task exposes a design that will not work, that is a finding. Record what you changed and why; do not quietly build something else.
  kicker: your design, your order
  image: none

### C1 — Starting from a known state
- Teaches: [ICTCLD502 PE 4]
- Kicker: everyone starts in the same place
- [BESPOKE] Deploying an environment from a template
  - The environment you are hardening is deployed from a template rather than clicked together.
  - A template is repeatable, reviewable and disposable — everybody starts from an identical environment, and it can be torn down and rebuilt exactly.
  - This is the same reason you built a launch template rather than a server back in AT2. It is the same idea, one level up.
  kicker: repeatable, reviewable, disposable
  image: none
- [BESPOKE] Reading a deployment that failed
  - When a template deployment fails, it rolls back — and the rollback fills the log with errors that are consequences, not causes.
  - Scroll to the first failure. That one is the cause; everything below it is the tidy-up.
  - A rolled-back deployment usually has to be removed before the same name can be used again.
  kicker: the first error is the cause
  image: none
- [BESPOKE] Things you set once and cannot see again
  - Some values are write-only: you supply them at creation and the platform will never show them to you afterwards.
  - Write them down as you type them. Nothing will prompt you, and nothing can recover them.
  kicker: write it down now
  image: none
- [EX] Deploy the baseline environment
  - Workbook — task 19.
  - Deploy the environment from the template, set the region first, record anything you are asked to invent, and confirm the service loads before you change anything.
  timer: ~25 min
  image: none
  notes:
    Activity = practice workbook task 19. Region must be set before the deployment starts — the stack
    builds into whatever is selected. Deployment takes around ten minutes; plan the session around it.
    The service listens on plain HTTP, so a browser left to itself will fail to reach it.
- [TAKEAWAYS] Section 1 · The starting state
  - A template gives everyone an identical, disposable starting environment.
  - On a failure, read the first error; the rest is rollback.
  - Record write-only values as you set them.
  image: none

### C2 — Building the network and compute changes
- Teaches: [ICTCLD502 PC 4.1] · [ICTCLD502 PE 1] · [ICTCLD502 PE 2]
- Kicker: from your own answers
- [BESPOKE] Copy your answer across first
  - Before each task, write your design answer at the top of it. Then build that.
  - It sounds like bureaucracy. It is what stops you building something subtly different from what you documented, and then producing evidence that does not match your own design.
  kicker: the design is the instruction
  image: none
- [BESPOKE] Placement is a decision the console will make for you
  - Where something is placed is the entire point of this work, and it is exactly the field the console is happiest to fill in on your behalf.
  - Set it explicitly every time, then go back and confirm what it actually did — read the column, do not trust the form.
  - If it landed in the wrong place, remove it and do it again. It is far cheaper now than three tasks later.
  kicker: set it, then verify it
  image: none
- [BESPOKE] Capacity has to be told to use the new space
  - Giving a scaling group access to a new location does not put anything in it. The capacity numbers are what make it happen.
  - Both settings, or neither works: reach without capacity leaves the new location empty; capacity without reach has nowhere to go.
  kicker: reach and capacity, together
  image: none
- [BESPOKE] Healthy takes longer than running
  - A new server is not healthy the moment it exists. It has to start, and configure itself, before it passes a health check.
  - Until then the target group will report it as failing. That is the expected sequence, not a fault.
  - How long depends on what the server is running — a lightweight system is a minute or two; a heavier one can be ten. Wait. Do not terminate it or start changing settings because it looks stuck.
  kicker: failing, then healthy
  image: none
- [EX] Build the network and application-tier changes
  - Workbook — tasks 20, 21 and 22.
  - Create the subnet from your design, give it the outbound path you designed, then extend the application tier and wait for it to become healthy in both locations.
  timer: ~40 min
  image: none
  notes:
    Activity = practice workbook tasks 20–22. Task 21 branches on their own task 11 answer — both
    branches are correct, and the workbook covers each. Do not push them onto one.
    The zone dropdown is the reliable error; have them check the column afterwards.
- [TAKEAWAYS] Section 2 · Network and compute
  - Copy the design answer across, then build it.
  - Set placement explicitly and verify what the console actually did.
  - Reach and capacity are two settings and you need both.
  - Failing health checks on a new server are expected for a while.
  image: none

### C3 — The data tier and the monitoring
- Teaches: [ICTCLD502 PC 4.1] · [ICTCLD502 PC 4.3] · [ICTCLD502 PE 1] · [ICTCLD502 PE 5]
- Kicker: start the slow one first
- [BESPOKE] Start the long-running change early
  - Converting a data tier runs in the background and takes longer than anything else here.
  - Start it, then go and do something else while it runs. This is exactly the ordering point you planned for — now you get to use it.
  - Watch for a setting that defers the change to a future maintenance window. Leave it as it is and nothing will happen today.
  kicker: kick it off, then move on
  image: none
- [BESPOKE] Building an alarm you designed yourself
  - You are not being given a metric. You are finding the one your design named.
  - Similar-looking metric groupings are the trap: one aggregates across locations, another breaks it down by location. Only one of them can answer a question about a single location.
  - Metrics for deleted resources hang around. If several similar things are listed, confirm you are pointing at the one that is live — an alarm on a resource that no longer exists never fires.
  kicker: the right grouping, the live resource
  image: none
- [BESPOKE] Some things are not alarms
  - Not every event you might want to know about is a metric with a threshold.
  - Some are events published by the service itself, configured somewhere else entirely and notifying directly, with no alarm in between.
  - If what you designed cannot be built as an alarm, that is worth knowing and worth recording — it is a real distinction, not a mistake in your design.
  kicker: metrics and events are different
  image: none
- [BESPOKE] An alarm that fires immediately may still be right
  - A practice environment does not generate the activity a real one does. An alarm watching something nothing is doing will sit in an alarm state.
  - That does not mean the alarm is wrong. Note why, and leave it — do not change a correct threshold to make a light go green.
  kicker: note it, do not tune it away
  image: none
- [EX] Convert the data tier and build your monitoring
  - Workbook — tasks 23 and 24.
  - Apply the data-tier change from your design, start it before the monitoring work, then build the alarms you designed.
  timer: ~35 min
  image: none
  notes:
    Activity = practice workbook tasks 23–24. The conversion takes twenty minutes or more; they should
    start it and move straight to the alarms.
    A new alarm reads insufficient-data for a few minutes — normal, not a fault.
- [TAKEAWAYS] Topic 14 · Key takeaways
  - Build from your own design; copy the answer across first.
  - Set placement explicitly, then verify it.
  - Start the long-running change first and work alongside it.
  - The right metric grouping and the live resource both matter.
  image: none

### Close
- [BESPOKE] Next — proving it
  - It is built. Whether it survives anything is still a claim.
  - Next: confirm it is healthy, then break it on purpose and measure what it cost.
  image: none

## Build notes
~19 slides. Three activities, mapping to practice workbook tasks 19 · 20–22 · 23–24.
No images used yet — the cross-zone build would benefit from a diagram, but any diagram showing the
finished topology gives away Part A and must not be added. `coverage.md` needs reconciling — this Topic
previously covered closure and documentation.

## Changelog
- 2026-08-28 — new plan; carries workbook Part B tasks 19–24. Task 19 (deploying from a template) and
  the waiting/health-check behaviour taught for the first time.
