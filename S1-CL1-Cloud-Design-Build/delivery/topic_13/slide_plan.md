# Topic 13 HA implementation & simulation — Slide plan
> **Covers:** Topic 13 — see coverage.md
> **Subtitle:** Build your HA design — then break it on purpose to prove it works

## Slides

### Opener
- [BESPOKE] Build it, then break it
  - In Topic 12 you designed the HA upgrade; now you implement it on the running baseline.
  - Then you simulate failures and resizes — to prove the design is actually fault tolerant.
  - Build → demonstrate connectivity → simulate → compare to your design → improve → document.
  - For the build: watch the recorded demo, then do it. The simulations you drive yourself.
  kicker: AT3 Part B skills
  image: none
  notes:
    The map for the whole Topic — set the arc, don't teach content yet. This is AT3 Part B skills.
    • Frame the two moves: in Topic 12 they DESIGNED the HA upgrade; today they IMPLEMENT it on the
    running baseline, then SIMULATE failures/resizes to PROVE it's fault tolerant.
    • Read the pipeline out: build → demonstrate connectivity → simulate → compare to design →
    improve → document. Each phase maps to a section today (C1/C2/C3).
    • Stress the mode split (last bullet): for the BUILD they watch the recorded demo then do it;
    the SIMULATIONS they drive themselves — no recorded "break it" demo exists.
    Misconception to pre-empt: "designing it is the hard part; building is just clicking." No — the
    proof is the point: an HA design isn't HA until a simulated failure shows it stays up.
    Question to pose: "You designed for two AZs — how would you actually PROVE one AZ can fail and
    Ledgerline keeps serving?" (surfaces the simulate-to-prove logic).
    UoC/AT3 tie: this Topic develops the skills assessed in AT3 Part B (the implementation window +
    the failure/resize simulations) — ICTCLD502 element 4 (+ 5.1).

### C1 — Implement the design
- Teaches: [ICTCLD502 PC 4.1] · [ICTCLD502 PC 4.2] · [ICTCLD502 PE 1] · [ICTCLD502 PE 2] · [ICTCLD502 PE 4]
- Kicker: harden in place
- [BESPOKE] Implementation approaches
  - Big-bang / cutover — switch over all at once: fastest, but high risk.
  - Incremental — adopt in phases: easier to adapt and troubleshoot; slower.
  - Parallel — run old and new together: safest fall-back, but highest cost.
  - In-place HA hardening is incremental — add redundancy without taking the service down.
  kicker: ICTCLD502 · Implement & finalise
  image: none
  notes:
    Open C1 — the three ways to roll out a change, so they can place in-place HA hardening correctly.
    • Walk the three: big-bang/cutover (switch all at once — fastest, highest risk); incremental
    (phase it in — easier to adapt/troubleshoot, slower); parallel (run old + new together — safest
    fall-back, highest cost).
    • Land the accent-bold line: in-place HA hardening IS incremental — you add redundancy WITHOUT
    taking the service down. That's why it fits a live accounting system.
    Misconception to pre-empt: "adding HA means a maintenance outage / rebuild from scratch." No — you
    harden in place, service stays up; that's the whole appeal of the incremental approach here.
    Question to pose: "Ledgerline is used every business day — which approach lets you add a second AZ
    without an outage, and why not big-bang?" (incremental; big-bang risks the live service).
    UoC/AT3 tie: ICTCLD502 PC 4.1 (implement the architecture design) — the how-you-roll-it-out choice
    that AT3 Part B's implementation window assumes.
- [BESPOKE] Build it well
  - Deploy with scripts (infrastructure as code) — repeatable, documented, fewer errors.
  - Right-size with the Auto Scaling group instead of guessing capacity.
  - Automate security and monitoring (IAM, CloudWatch, alarms).
  kicker: ICTCLD502 · Implement & finalise
  image: none
  notes:
    Short but load-bearing — the quality bar for the implementation, not just "make it work."
    • Deploy with scripts (infrastructure as code) — repeatable, documented, fewer manual errors than
    clicking. Callback to their AT2 build habits.
    • Right-size with the Auto Scaling group rather than guessing capacity — the ASG sets the size to
    demand, so you don't over- or under-provision.
    • Automate security + monitoring (accent-bold): IAM, CloudWatch, alarms — bake it in as you build,
    not bolted on after.
    Misconception to pre-empt: "a working build is a good build." A build can function yet be fragile,
    undocumented and un-monitored — you can't prove availability you never instrumented.
    Question to pose: "If you had to rebuild this HA layer next week, what makes IaC better than
    repeating the clicks?" (repeatable, documented, fewer errors).
    UoC/AT3 tie: ICTCLD502 PE 2 (deploy automated scaling) + PE 4 (use console/SDK/CLI) — the build
    quality AT3 Part B is evidenced against.
- [BESPOKE] Demonstrate connectivity at all tiers
  - After implementing, confirm each tier works — and only talks to what it should:
    - client → application; application → database; database reachable only from the app tier
  - Confirm failover works — and that you can fail back to the primary.
  - This is the evidence that the build is correct, not just present.
  kicker: ICTCLD502 · Implement & finalise
  image: none
  notes:
    The evidence step of C1 — teach that a build isn't done until you've PROVEN each tier talks to the
    right thing and only the right thing.
    • Walk the sub-bullet: client → application; application → database; and the database reachable ONLY
    from the app tier — connectivity AND isolation, both matter.
    • Land the accent-bold line: confirm failover works AND that you can fail back to the primary — a
    failover you can't reverse isn't finished.
    • Last bullet is the teaching point: this is the evidence the build is CORRECT, not merely present.
    Misconception to pre-empt: "if the app loads, connectivity is fine." No — you must show the DB is
    NOT reachable from the internet, and that failover/fail-back both work; "it loads" proves neither.
    Question to pose: "How would you show an assessor the database can't be reached except from the app
    tier?" (test from the app tier vs from outside; show the SG/route).
    UoC/AT3 tie: ICTCLD502 PC 4.2 (demonstrate connectivity between resources at all tiers) — captured
    as AT3 Part B evidence.
- [DEMO] Build a highly available application
  - Create an Auto Scaling group spread across two Availability Zones, behind a load balancer.
  - Add a Multi-AZ database with an automatic-failover standby.
  - Confirm the load balancer routes only to healthy targets across both AZs.
  source: ACA M10 · Creating a Highly Available Application (S44)
  image: none
  notes:
    DEMONSTRATION slide (C1). This is the "demonstrate" step of teach → demonstrate → practice for the
    HA build — screen the recorded demo, then relate every step to OUR Accounting baseline.
    
    WHERE TO FIND THE RECORDED DEMO: AWS Academy Cloud Architecting (ACA) → Module 10 → slide 44,
    "Demo: Creating a Highly Available Application", inside the ACA M10 instructor deck
    (original-materials/AWS-Instructor Presentations/…). Instructor-facing — screen it in class, do not
    distribute to students. Preview it before class and cue it to this slide.
    
    WHAT TO DEMONSTRATE (follow the recorded demo, then map to our build):
    1. Create an Auto Scaling group spread across TWO Availability Zones, behind a load balancer.
    2. Add a Multi-AZ database with an automatic-failover standby.
    3. Confirm the load balancer routes only to HEALTHY targets across both AZs.
    
    WHAT TO EMPHASISE:
    • The redundancy is across AZs — two AZs is what survives a data-centre failure (callback Topic 11).
    • Multi-AZ RDS = automatic failover to a standby; students confuse this with a read replica — it's HA.
    • Health checks: the ALB only sends traffic to healthy targets — that's what makes failover invisible.
    • Narrate evidence capture — they screenshot as they build for AT3; model it here.
    
    PREP: clean Learner Lab open (deploy us-east-1), their Topic 12 HA design handy, demo queued.
    ~8–10 min to screen + narrate before the activity.
- [EX] Implement your HA design
  - On the running Accounting baseline, implement the hardening from your Topic 12 design:
    - add the second AZ + mirrored subnets; extend the ASG and ALB across both AZs
    - convert the database to Multi-AZ; add the second NAT gateway
  - Demonstrate connectivity at all tiers and capture evidence.
  timer: ~30 min
  image: none
  notes:
    Facilitation (C1 practice) — students implement THEIR OWN Topic 12 design on the running baseline.
    Tell students, in these words: "Open the lab and your Topic 12 HA design. On the running Accounting
    baseline, implement your hardening exactly as your design specifies — then prove connectivity at
    every tier and capture the evidence as you go."
    Steps (put on the board):
    1. Add the second AZ + mirrored subnets; extend the ASG and ALB across both AZs.
    2. Convert the database to Multi-AZ; add the second NAT gateway.
    3. Demonstrate connectivity at all tiers (client→app, app→db, DB isolated), and failover/fail-back.
    4. Capture the named evidence screenshots as you build each piece.
    Must produce: the hardened baseline running across two AZs, plus connectivity/failover evidence.
    Timing: ~30 min. Where they get stuck: forgetting the SECOND NAT gateway (breaks HA for the private
    subnet), and impatience with Multi-AZ conversion (it takes minutes) — circulate and reassure.
    Share-back: ask one student to show failover working, then failing back.
    No-leakage note: this practice uses the Accounting/Ledgerline baseline; AT3 assesses the same skill
    on a DIFFERENT supplied system (the LMS) — comparable, not identical.
- [TAKEAWAYS] Section 1 · Implement
  - In-place HA hardening is incremental — no outage.
  - Deploy with IaC; right-size with the ASG; automate security + monitoring.
  - Demonstrate connectivity at every tier, including failover and fail-back.
  - Capture the evidence as you build.
  image: none

### C2 — Simulate failures & resizes
- Teaches: [ICTCLD502 PC 4.3] · [ICTCLD502 PC 4.4] · [ICTCLD502 PC 4.5] · [ICTCLD502 PE 1] · [ICTCLD401 PC 3.2] · [ICTCLD502 PE 3] · [ICTCLD502 PE 5] · [ICTCLD502 KE 5, 6, 9]
- Kicker: break it on purpose
- [BESPOKE] Why simulate?
  - An untested backup plan isn't a plan.
  - In 2016 Delta Air Lines had an outage when failed equipment exposed a backup that had never been tested — about US$100 million.
  - You simulate failures to confirm every part of the HA design actually works.
  kicker: ICTCLD502 · Implement & finalise
  image: none
  notes:
    Open C2 — establish WHY you deliberately break a working system. The mindset shift of the section.
    • The one-liner (say it first): an untested backup plan isn't a plan.
    • Use the accent-bold Delta 2016 story: failed equipment exposed a backup that had NEVER been tested
    — about US$100 million. A real, memorable cost of assuming HA works.
    • Land the point: you simulate failures to CONFIRM every part of the HA design actually works —
    before a real failure does the testing for you.
    Misconception to pre-empt: "we built redundancy, so it's fault tolerant." Redundancy on paper isn't
    proof — until a failure is simulated and the service stays up, HA is a claim, not a fact.
    Question to pose: "Would you tell YAT's board 'it'll fail over fine' without ever having failed it
    over?" (draws out that proof, not confidence, is the deliverable).
    UoC/AT3 tie: sets up ICTCLD502 PC 4.3–4.4 and PE 3 (simulate failures, demonstrate fault tolerance)
    — the core of AT3 Part B's simulation window.
- [BESPOKE] Monitor & measure availability
  - Watch uptime, errors and latency throughout the simulation — you can't prove availability you didn't measure.
  - Use CloudWatch metrics + alarms and the AWS Health Dashboard.
  - Record the numbers before, during and after each simulated failure.
  kicker: ICTCLD502 · Implement & finalise
  image: none
  notes:
    The measurement discipline for C2 — you can't prove availability you didn't measure.
    • Walk it: watch uptime, errors and latency THROUGHOUT the simulation — not just a before/after
    glance.
    • Name the tools: CloudWatch metrics + alarms, and the AWS Health Dashboard (callback to their AT2
    monitoring build).
    • Accent-bold: record the numbers BEFORE, DURING and AFTER each simulated failure — the delta is the
    evidence of the availability impact.
    Misconception to pre-empt: "if it stayed up, that's enough." No — AT3 wants the measured impact
    (how long, how many errors, what latency); "it seemed fine" isn't evidence.
    Question to pose: "When you terminate an instance, what exactly do you watch to show users weren't
    affected?" (target health, error rate, latency across the failover).
    UoC/AT3 tie: ICTCLD502 PC 4.3 + PE 5 (define, monitor and record resource availability) + KE 6/9
    (measuring availability impact; performance metrics).
- [BESPOKE] Simulate failures
  - Disable assets — terminate an instance, or take down an Availability Zone's resources.
  - Network disruption — block traffic to a subnet.
  - Confirm the system fails over to the redundant assets and keeps serving — that's fault tolerance proven.
  kicker: ICTCLD502 · Implement & finalise
  image: none
  notes:
    The heart of C2 — teach the failure injections and what "fault tolerant" looks like when it works.
    • Disable assets — terminate an instance, or take down an AZ's resources; watch the ASG/Multi-AZ
    replace or fail over.
    • Network disruption — block traffic to a subnet, simulating a partition.
    • Accent-bold: confirm the system fails over to the redundant assets and KEEPS SERVING — that is
    fault tolerance PROVEN, the exact thing AT3 wants evidenced.
    Misconception to pre-empt: "simulate = just imagine/describe the failure." No — they actually inject
    the failure in the lab (terminate, block) and observe the real behaviour; a written thought
    experiment isn't a simulation.
    Question to pose: "You kill the instance in AZ-A — walk me through what SHOULD happen, and how you'd
    see it did?" (ALB drops the unhealthy target, ASG launches a replacement, service continues).
    UoC/AT3 tie: ICTCLD502 PC 4.4 + PE 1/PE 3 (simulate component failures, confirm fault tolerant,
    resilient to networking/compute/storage/database/data-centre failures).
- [BESPOKE] Simulate resizes & load
  - Load testing — does it work under the expected workload (e.g. month-end peak)?
  - Stress testing — where's the breaking point, and does it fail gracefully (queued / busy messages, data safe)?
  - Resize a component and measure the availability impact — vertical resizes often take a brief outage.
  kicker: ICTCLD502 · Implement & finalise
  image: none
  notes:
    The second half of C2 — resizing and load/stress, and their availability cost.
    • Load testing — does it hold under the EXPECTED workload (e.g. Ledgerline's month-end peak)?
    • Stress testing — where's the breaking point, and does it fail GRACEFULLY (queued/busy messages,
    data kept safe) rather than falling over?
    • Accent-bold: resize a component and MEASURE the availability impact — vertical resizes often take
    a brief outage, and that trade-off must be recorded.
    Misconception to pre-empt: "scaling up is free and instant." A vertical resize (bigger instance /
    DB class) usually needs a restart or failover — a short availability hit; horizontal (ASG) avoids
    it. Knowing which is which is the point.
    Question to pose: "Month-end doubles the load — do you scale UP the instance or OUT with the ASG,
    and what does each cost you in availability?" (out = no outage; up = a brief one).
    UoC/AT3 tie: ICTCLD502 PC 4.5 (simulate resizing, measure availability impact) + ICTCLD401 PC 3.2
    (test automatic scaling and fix errors, applied under load/resize) + KE 5 (testing/debugging).
- [EX] Run the simulations
  - Per your simulation plan, with monitoring on:
    - fail an instance / an AZ — confirm the service stays up (fault tolerant)
    - trigger a database failover, then fail back
    - resize under load and measure the availability impact
  - Record the availability impact of each, with evidence.
  timer: ~30 min
  image: none
  notes:
    Facilitation (C2 practice) — students run their own simulation plan against their hardened baseline.
    Tell students, in these words: "With your monitoring on, work through your simulation plan. Break
    the system on purpose, watch what happens, and record the availability impact of each with
    evidence."
    Steps (put on the board):
    1. Fail an instance / an AZ — confirm the service stays up (fault tolerant).
    2. Trigger a database failover, then fail back to the primary.
    3. Resize a component under load and measure the availability impact.
    Must produce: for each simulation, the measured availability impact (uptime/errors/latency before,
    during, after) with screenshots/metrics as evidence.
    Timing: ~30 min. Where they get stuck: forgetting to start monitoring BEFORE the failure (no
    baseline to compare), and panicking when a resize causes a brief outage — that's expected, tell them
    to record it, not fix it.
    Share-back: take one measured result and ask "did the design hold?" — bridges into C3.
    No-leakage note: simulations run on the Accounting baseline (practice); AT3 assesses the same on the
    supplied LMS system — comparable, not identical.
- [TAKEAWAYS] Section 2 · Simulate
  - Untested HA isn't HA — simulate to prove it.
  - Measure availability (CloudWatch) throughout each simulation.
  - Simulate failures (disable assets / block a subnet) and confirm failover.
  - Load/stress test and measure the impact of a resize.
  image: none

### C3 — Compare, improve & document
- Teaches: [ICTCLD502 PC 4.6] · [ICTCLD502 PC 5.1]
- Kicker: did it meet the design?
- [BESPOKE] Compare findings to the design
  - Measure what the simulations showed against your documented recovery objectives.
  - Did the build meet its RPO/RTO? Did each SPOF's fix actually hold under failure?
  - Note any gap between the design's intent and the simulated reality.
  kicker: your documented design
  image: none
  notes:
    Open C3 — turn the raw simulation results back against what the design PROMISED.
    • Walk it: measure what the simulations showed against your documented recovery objectives (the
    RPO/RTO and SPOF fixes from Topic 12).
    • Accent-bold: did the build meet its RPO/RTO? Did each single point of failure's fix actually hold
    under a real (simulated) failure?
    • Last bullet: note any GAP between the design's intent and the simulated reality — that gap is what
    C3 acts on next.
    Misconception to pre-empt: "the simulations passed, so we're done." Passing isn't the deliverable —
    comparing measured behaviour to the stated objectives is; a build can survive yet miss its RTO.
    Question to pose: "Your design promised recovery in under a minute — what did the simulation
    actually measure, and did it meet the promise?" (forces objective-vs-reality comparison).
    UoC/AT3 tie: ICTCLD502 PC 4.6 (compare and document simulation findings according to the documented
    design) — the compare half of AT3 Part B's closing work.
- [BESPOKE] Improve availability if needed
  - If a simulation shows a prolonged outage or poor availability, adjust the design:
    - more redundancy · Multi-AZ · managed services with built-in HA · monitoring with auto-triggered recovery
  - Make the change, then re-test to confirm the improvement.
  kicker: ICTCLD502 · Implement & finalise
  image: none
  notes:
    The improve step of C3 — what to do when a simulation exposes a gap.
    • The trigger: a simulation shows a prolonged outage or poor availability → adjust the design; don't
    leave a known weakness in.
    • Walk the levers (sub-bullet): more redundancy · Multi-AZ · managed services with built-in HA ·
    monitoring with auto-triggered recovery.
    • Accent-bold: make the change, then RE-TEST to confirm the improvement — an untested fix is just
    another claim (callback to "why simulate?").
    Misconception to pre-empt: "note the gap in the report and move on." No — where a simulation reveals
    a real weakness you adjust and re-simulate; the improvement only counts once re-tested.
    Question to pose: "Your single NAT gateway took the private tier down when its AZ failed — what's
    the fix, and how do you prove it worked this time?" (second NAT per AZ; re-run the AZ failure).
    UoC/AT3 tie: ICTCLD502 PC 5.1 (adjust and improve availability according to simulations as
    required).
- [EX] Compare, adjust & document
  - Finalise the implementation:
    - compare your simulation findings against your documented design
    - make any improvements the simulations call for, and re-test
  - Document the simulation findings against the design — this feeds the HA Deployment Report.
  timer: ~20 min
  image: none
  notes:
    Facilitation (C3 practice) — finalise the implementation and produce the documented findings.
    Tell students, in these words: "Finalise your HA implementation. Compare your simulation findings
    against your documented design, make any improvements the simulations call for and re-test, then
    document the findings against the design — this is what feeds your HA Deployment Report."
    Steps (put on the board):
    1. Compare your simulation findings against your documented design's recovery objectives.
    2. Make any improvements the simulations call for, and RE-TEST them.
    3. Document the findings against the design (what met the objective, what you changed and why).
    Must produce: a written findings-vs-design comparison plus any re-tested improvements — the raw
    material for the Topic 14 HA Deployment Report.
    Timing: ~20 min. Where they get stuck: documenting only what passed and hiding the gaps — remind
    them the gaps + fixes are the strongest evidence, not a weakness to bury.
    Share-back: ask one student for a gap they found and the improvement they made.
    No-leakage note: this finalises the Accounting-baseline practice; AT3 assesses the same on the
    supplied LMS system — comparable, not identical. Closure (the report, feedback, sign-off) is Topic 14.
- [TAKEAWAYS] Section 3 · Compare & improve
  - Compare simulation findings to the documented recovery objectives.
  - Improve where the simulations show gaps — then re-test.
  - Document the findings against the design.
  - What you record here becomes the HA Deployment Report.
  image: none
- [TAKEAWAYS] Topic 13 · Key takeaways
  - Implement incrementally — harden in place with no outage.
  - Demonstrate connectivity at all tiers, including failover.
  - Simulate failures and resizes to *prove* fault tolerance; measure availability.
  - Compare to the design, improve where needed, and document the findings.
  - You implemented and proved your own design.
  image: none

### Close
- [BESPOKE] Next: Topic 14 — Closure & documentation
  - Write the HA Deployment Report from your evidence and findings, seek and respond to feedback, and obtain final sign-off — closing the engagement.
  - Bring your simulation findings.
  image: none
