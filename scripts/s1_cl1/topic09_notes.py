"""Teacher speaker notes for Topic 09 — Operability & justification (S1-CL1).

One entry per teaching/visual/demo/activity slide. Keys are the EXACT slide title strings from
build_s1_cl1_topic09_deck.py so they match at build time. Read only by the teacher
(Presenter View), never shown to students.
"""

NOTES = {

    "From built to defensible": """
        Frame this as the map for the whole Topic — set the pivot, don't teach content yet.
        • Where this sits: Topics 6–8 BUILT the workload (foundation, network, compute, data). Today is
          not more building — it's making that build operable and defensible.
        • Read the three verbs off the accent-bold line: monitor it, validate it, justify the open
          decisions. Each maps to a Section today (C1 monitoring, C2 validation, C3 justification).
        • The stakes line (third bullet): these three things are exactly what the Deployment Report is
          MARKED on — this isn't housekeeping, it's the assessed judgement.
        • Point forward: Topic 10 turns today's evidence and justifications into the report itself.
        Misconception to pre-empt: "the build is done, so the hard part's over." No — a build nobody can
        monitor or defend earns few marks; the judgement work starts now.
        Question to pose: "You've built it and it runs — why isn't that enough to hand to the client?"
        (because you must show it works AND why each choice was right).
        UoC/AT2 tie: this Topic develops ICTCLD401 (primary) + ICTCLD502 (partial); today's outputs feed
        AT2 Deployment Report §4.10, §4.13 and §4.16.
    """,

    "What monitoring is": """
        Primer — vendor-neutral fundamentals before any AWS service name. Keep it plain; the CloudWatch
        slide is next.
        • Define the three terms cleanly: a METRIC is a measurement over time (CPU %, free storage, DB
          connections); an ALARM is a threshold on a metric that fires an action/notification when
          crossed; a LOG is a record of events — what happened, and when.
        • Land the payoff line (accent-bold): you monitor so you find out before your USERS do — that's
          the whole reason it exists.
        • Keep metric vs alarm vs log distinct — they conflate them; the metric is the number, the alarm
          is the rule watching the number, the log is the diary.
        Misconception to pre-empt: "monitoring = looking at a dashboard sometimes." No — the value is the
        alarm doing the watching for you, so a human doesn't have to stare at graphs.
        Question to pose: "If YAT's database is about to run out of storage, would you rather find out from
        an alarm at 15% free, or from users when it's full?" (the alarm — proactive vs reactive).
        UoC/AT2 tie: ICTCLD401 KE 5 (performance monitoring and alarms); the concept the CloudWatch build
        and the §4.10 evidence rest on.
    """,

    "Amazon CloudWatch": """
        The AWS-context teach — pin the primer terms onto the real service. Lean on the diagram; source is
        ACA M10 monitoring section (S9–S12).
        • Walk the three roles: CloudWatch COLLECTS metrics + logs from AWS services into one place; ALARMS
          send notifications (e.g. to SNS) or trigger actions (e.g. Auto Scaling); DASHBOARDS visualise,
          and CloudWatch LOGS centralises log files.
        • Map each back to the primer: metric→collected, alarm→threshold+action, log→CloudWatch Logs.
        • Tie to the Ledgerline sketch from Topic 1 — CloudWatch is the box that was "watching all of it";
          now they see what it actually does.
        Misconception to pre-empt: "CloudWatch is one more thing you have to build separately." Much of it
        is automatic — services publish metrics to it by default; you add the ALARMS and the log
        destinations.
        Question to pose: "An alarm fires — what are the two things it can do?" (notify a human via SNS, or
        take an action like scaling). Sets up the demo.
        UoC/AT2 tie: ICTCLD401 KE 5; this is the tool that produces the §4.10 monitoring evidence.
    """,

    "Create a CloudWatch alarm": """
        DEMONSTRATION slide (teach → demonstrate → practice). Screen/drive the demo, then relate each step
        to OUR build before the activity.
        WHERE TO FIND THE RECORDED DEMO: the catalogue has NO isolated recorded CloudWatch demo for Topic 9
        (aws-recorded-demos-catalogue.md, "Topic 9" row: drawn from ACA M10 monitoring content, no
        standalone recording). So this is the ONE live/instructor-led demo in the Topic — drive it yourself
        in the Learner Lab, cued to the nearest module: ACA M10 (Automated Scaling & Monitoring), the
        CloudWatch monitoring section. Preview it before class.
        WHAT TO DEMONSTRATE (live, then relate to the design's §4.10):
        1. Pick a metric (e.g. EC2 CPU) and set a threshold and period.
        2. Choose the action — a notification (SNS), or an Auto Scaling action.
        3. Confirm the alarm state, and view it on a dashboard.
        WHAT TO EMPHASISE:
        • The threshold + period together are the alarm (e.g. ≥ 80% over 10 min) — not just the number.
        • Narrate the evidence capture — students screenshot the alarm for AT2; model it live.
        • Keep it BASELINE — HA-tuned alarms are AT3; don't gold-plate here.
        PREP: clean Learner Lab open (us-east-1), the Accounting Baseline Design handy for §4.10 thresholds.
        ~6–8 min to drive + narrate before the activity.
    """,

    "Stand up the baseline monitoring": """
        Facilitation — the C1 practice; students build the design's baseline monitoring in the lab.
        Tell students: "Open the lab and the Accounting Baseline Design at §4.10. Stand up the baseline
        monitoring for the Ledgerline engagement — exactly the alarms and logging the design specifies —
        and capture evidence as you go."
        Steps (put on the board):
        1. Create the baseline alarms: EC2/RDS CPU high, RDS free storage low, RDS connections high, ALB
           5XX / unhealthy host — thresholds per §4.10.
        2. Enable the logging destinations: CloudWatch Logs (flow logs + RDS), ALB access logs to S3, the
           CloudWatch Agent for EC2 OS logs.
        3. Capture the evidence — the alarms and the log configuration.
        Must produce: screenshots of the baseline alarms and the logging config (the AT2 §4.10 evidence).
        Timing: ~15 min. Where they get stuck: over-building HA-tuned alarms (rein them back to baseline),
        and forgetting the log destinations because alarms feel like "the monitoring."
        Share-back: ask one student to show their alarm list; confirm thresholds match the design.
        No-leakage note: this is practice on the Accounting/Ledgerline baseline; AT2 assesses the same
        skill on a different system — comparable, not identical.
    """,

    "What validation is": """
        Primer — the C2 fundamental. Short but load-bearing; students think building IS finishing.
        • The core distinction (first bullet): building something is NOT the same as confirming it does
          what was asked. Say it twice — it's the whole point.
        • Define the loop (accent-bold): validation = test → observe → compare to the requirement/design →
          fix. Four moves, not "have a look."
        • Frame it as how you AND the assessor know the build actually meets the spec — it's evidence, not
          a vibe.
        Misconception to pre-empt: "it launched without errors, so it's validated." No — no error at build
        time doesn't prove it meets the requirement (e.g. that staff can actually reach the app, that it
        scales). You must test against the spec.
        Question to pose: "You deployed it and nothing errored — what have you actually PROVEN, and what
        haven't you?" (proven it deployed; not proven it meets the design).
        UoC/AT2 tie: ICTCLD401 PC 2.6 (test access, fix errors) + PC 3.2 (test scaling, fix errors) —
        developed in Topics 7–8, VALIDATED here against the design.
    """,

    "Validate against the design + recovery objectives": """
        The C2 teach — consolidate earlier tests into one deliberate validation. This is where scattered
        testing becomes a defensible check.
        • Walk it: pull together the tests already run in Topics 7–8 — connectivity (Reachability
          Analyzer), app→database, and scaling — don't re-invent them, consolidate them.
        • Check against the design's RECOVERY OBJECTIVES: RPO ≤ 1 hour, RTO ≤ 1 business day. Explain both
          plainly — RPO = how much data you can afford to lose; RTO = how long to be back up.
        • The honesty line (accent-bold): name the known limit — this baseline is SINGLE-AZ; the single AZ
          and single RDS instance are SPOFs. Then the last bullet: that's TOLERABLE for a business-hours
          service now, and is precisely the objective of the AT3 HA design.
        Misconception to pre-empt: that naming the SPOF is admitting a failure. The opposite — naming a
        known, accepted limit honestly is what a professional validation DOES; hiding it loses marks.
        Question to pose: "The build has a single-AZ SPOF — do you hide that in the report, or name it?
        Why?" (name it — it's honest, and it's the AT3 brief).
        UoC/AT2 tie: PC 2.6 · PC 3.2; AT2 §4.13 recovery objectives (baseline state), A-build / A10.
    """,

    "Validate the build": """
        Facilitation — the C2 practice; a validation pass in the lab against the design.
        Tell students: "Run a validation pass on your Ledgerline build against the Accounting Baseline
        Design. You're not building — you're proving it meets the spec, and recording the result."
        Steps (put on the board):
        1. Confirm connectivity: staff→ALB and app→database; and confirm the scaling behaviour.
        2. Check the recovery objectives are met (RPO ≤ 1 h, RTO ≤ 1 business day); note the single-AZ SPOF.
        3. Record each result and any fix; capture evidence.
        Must produce: a short validation record — each test, its result, any fix, and the named SPOF (the
        AT2 §4.13 / A10 evidence).
        Timing: ~15 min. Where they get stuck: treating it as re-testing from scratch — remind them the
        tests were RUN in Topics 7–8; today is consolidating + comparing to the design. Also, students omit
        the SPOF because it feels like a fault — push them to name it.
        Share-back: take one student's validation record; confirm every result is compared to a design
        requirement, not just "it worked."
        No-leakage note: practice on the Accounting baseline; the assessed validation is on the LMS system —
        same discipline, different system.
    """,

    "What it means to justify": """
        Primer opening the centrepiece Section — the single highest-value idea in the Topic. Slow down.
        • Contrast the two bullets out loud: "I chose X" is NOT a justification. "I chose X because the
          workload needs Y, weighed against cost/security/residency — and the alternative was worse, for
          these reasons" IS (the accent-bold line).
        • The defining test (last bullet): a justification is SPECIFIC to this workload and NAMES the
          trade-off. Generic best practice ("it's more scalable") is not a justification.
        • Set expectations: this is the marked AT2 judgement (A4) — the difference between a pass build and
          a strong one lives here.
        Misconception to pre-empt: "justify = describe what I did." No — describing the config is the
        build; justifying is defending WHY, against this client's needs and the rejected alternative.
        Question to pose: "'I picked a t3.medium because it's a good all-rounder' — why does that earn
        almost nothing, and what would fix it?" (no workload link, no trade-off, no alternative).
        UoC/AT2 tie: ICTCLD401 PC 1.1 · PC 1.3 · PC 1.8 (+ KE 6 options / KE 4 cost); AT2 §4.16, criterion
        A4 — the marked judgement.
    """,

    "The method — justify against the workload": """
        The C3 method slide — give students the repeatable four-step scaffold they'll apply to every
        decision. Teach it as a template, not prose.
        • Walk the four steps in order: 1. State the decision (what you chose). 2. The workload FACTS that
          bear on it — load, pattern, data sensitivity, residency, cost appetite. 3. WEIGH it —
          performance vs cost vs security vs residency. 4. Name the ALTERNATIVE and why you rejected it.
        • Stress step 4 (accent-bold): the rejected alternative is what most students skip, and it's what
          proves the choice was a judgement, not a default.
        • Tell them: apply this SAME four steps to every open decision — consistency is what makes the
          report defensible.
        Misconception to pre-empt: "step 2 = any facts about the workload." No — only the facts that BEAR
        on this decision (for an instance type: the user load/pattern, not the residency rule).
        Question to pose: "Which of the four steps is the one you'll be tempted to drop — and why is it the
        one that earns the marks?" (step 4, the rejected alternative).
        UoC/AT2 tie: PC 1.1 (compare) · PC 1.3 (select) · PC 1.8 (define workload); the method operationalises
        A4 across the §4.16 decisions.
    """,

    "Worked example — SQL Server licensing (C3)": """
        The method made concrete — run one full example end to end so the abstract four steps become a
        pattern students can copy. This is the model answer's shape.
        • Walk the four steps on C3 (SQL licensing): DECISION — licence-included (pay hourly, licence built
          in) vs bring-your-own-licence (BYOL). WORKLOAD FACTS — steady business-hours use; YAT may already
          hold SQL Server licences; cost is a stated concern.
        • WEIGH (accent-bold): licence-included is simpler + better for variable/short use; BYOL is cheaper
          at steady use IF you already own licences. DECIDE + JUSTIFY: pick the cheaper-over-the-term option
          for this steady workload, and say why the other was rejected.
        • Point at how it reuses AT1 cost thinking — the CBA muscle from Topic 3, now applied to one build
          decision.
        Misconception to pre-empt: "there's a universally right answer here." No — it depends on YAT's
        facts (do they own licences? how steady?); the marks are in the reasoning, not the option chosen.
        Question to pose: "Change one fact — YAT owns no SQL licences — does your answer flip, and why?"
        (shows the justification is fact-driven, not memorised).
        UoC/AT2 tie: PC 1.3 + KE 4 (cost models); the template for the eight §4.16 justifications.
    """,

    "Justify the C1–C8 decisions": """
        Facilitation — the Topic's centrepiece practice; students write a justified rationale for every
        open design decision. Budget the most time here.
        Tell students: "Using the four-step method, write a justified rationale for each of the design's
        open decisions — C1 to C8. Ground every one in the Ledgerline workload, not generic best practice.
        These go straight into your Deployment Report."
        Steps (put on the board):
        1. For each decision (EC2 type, RDS class, SQL licence, EBS sizing, ASG params, backup/RPO,
           DNS/ACM, bastion/RDP): state it, give the workload facts, weigh it, name the rejected alternative.
        2. Anchor to the workload: 15–25 typical / 45–55 month-end users; read-heavy at month-end;
           financial-records residency; 7-year retention; business-hours, idle overnight.
        Must produce: a justified rationale per C1–C8 decision — each with a workload link, a trade-off,
        and a rejected alternative (the AT2 §4.16 / A4 content).
        Timing: ~30 min. Where they get stuck: generic reasoning ("more scalable", "best practice") with no
        workload link — circulate and ask "for THIS client, why?"; and skipping the rejected alternative.
        Share-back: take one decision (e.g. RDS class) from two students; ask the room which is more
        workload-specific and which named the trade-off.
        No-leakage note: practice justifications on the Accounting/Ledgerline workload; AT2 assesses the
        same judgement on the LMS build — comparable, not identical.
    """,

}
