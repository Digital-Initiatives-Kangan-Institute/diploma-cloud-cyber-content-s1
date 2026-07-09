"""Teacher speaker notes for Topic 06 — Build foundations (S1-CL1).

One entry per teaching/demo/activity slide. Keys are the EXACT slide title strings from
build_s1_cl1_topic06_deck.py so they match at build time. Read only by the teacher
(Presenter View), never shown to students.
"""

NOTES = {

    "From advising to building": """
        Frame this as the pivot of the whole cluster — AT1 was advice on paper; AT2 is a build in AWS.
        Set the mode, don't teach IAM yet.
        • The shift (bolded line): they now work to a design they did NOT write — read it, build it
          faithfully, resist the urge to redesign it. This is a new professional posture.
        • The second new discipline: capture evidence AS they build. The Deployment Report is made from
          what they screenshot live — you cannot reconstruct it after the fact.
        • Scope this Topic: the FOUNDATION tier only — account & Region, identity & access, shared
          responsibility. Network, compute and the report come in Topics 7–10.
        • Set the rhythm for every AWS task today: watch the demo, THEN do it yourself.
        Misconception to pre-empt: "we're finally free to build whatever we think is best." No — the whole
        skill being assessed is faithful implementation of a supplied design, not invention.
        Question to pose: "What changes about your job when the design is already written and handed to you?"
        (you become the builder/implementer, and your judgement shows in the open decisions + the evidence).
        UoC/AT2 tie: opens the AT2 arc — ICTCLD401 (primary) + ICTCLD502 (partial); everything today feeds
        the foundation-tier build narrative (criterion A2) + the evidence appendices (A9/A10).
    """,

    "Cloud architecture: requirements → design → build": """
        AWS-sourced (ACA M02) — use the diagram to install the three-role picture, then land where THEY sit.
        • Walk the chain off the visual: the customer sets the REQUIREMENTS → the architect produces the
          DESIGN → the delivery crew BUILDS it. Three distinct roles, one hand-off line between each.
        • Drive the accent-bold point: in AT2 they are the DELIVERY CREW. The design is already done; their
          job starts at "build it," not "decide it."
        • Callback to AT1: there they were doing the architect/advisor work; now they step one role down the
          chain and execute. Same engagement, different seat.
        Misconception to pre-empt: that "architecture" means they get to make the big calls. Here the big
        calls are made — architecture literacy is what lets them READ the design correctly and build true to it.
        Question to pose: "If the customer, architect and builder are three roles, which one are you in AT2 —
        and what does that mean you must NOT do?" (builder; don't rewrite the design).
        UoC/AT2 tie: frames the whole foundation-build (A2); establishes the working-to-a-supplied-design
        mode that the next slide makes concrete.
    """,

    "Working to a supplied design": """
        Bespoke — the heart of the AT2 mode. Teach the discipline of building faithfully to someone else's design.
        • Rule one: read the design end to end BEFORE touching the console. You cannot build faithfully to a
          document you have only skimmed the first page of.
        • Rule two: build exactly what it specifies. The only decisions that are yours are the ones the design
          deliberately LEAVES OPEN — the implementer decisions (labelled C1–C8 in the supplied design).
        • The accent-bold line: an "implementer decision" is precisely where their judgement is ASSESSED.
          Everywhere else, deviating from the design is an error, not initiative.
        Misconception to pre-empt: "if I can build it a better way, I should." No — unrequested cleverness is
        marked down. The skill is fidelity; judgement is shown only in the open decisions, and must be justified.
        Question to pose: "You spot what you think is a better instance type than the design names — do you
        change it?" (No — unless it's an open implementer decision; otherwise build as specified).
        UoC/AT2 tie: ICTCLD401 PE 1/PE 2 — the built artefacts are the evidence; this establishes the standard
        the whole foundation build (A2) is judged against.
    """,

    "Choose your Region — data residency first": """
        The first real build decision — and it's compliance, not preference. Applied from Topic 1's residency teaching.
        • Region is decision number one because everything you create is Region-scoped — get it wrong and every
          resource lands in the wrong place.
        • WHY Sydney: the design mandates ap-southeast-2 because financial records + PII must stay ONSHORE.
          This is the residency driver from Topic 1 now being BUILT, not just argued.
        • The lab reality (be explicit): in the AWS Academy Learner Lab they deploy to us-east-1 —
          [scenario: ap-southeast-2 (Sydney) | deploy: us-east-1]. Same build; only the location label changes.
          Set the console Region before creating anything.
        • Accent-bold: deploy everything to the lab's Region (us-east-1) and make sure the Region is VISIBLE in
          every screenshot — the assessor checks it matches.
        Misconception to pre-empt: that the us-east-1 substitution means residency doesn't matter. It matters
        conceptually (design says Sydney, for legal reasons); the lab just can't host that Region.
        Question to pose: "Why is Region the FIRST thing you set, before you create a single resource?"
        (resources are Region-scoped; the design mandates it for data residency).
        UoC/AT2 tie: ICTCLD401 PC 1.4 (access the account per business requirements); evidenced in Appendix A
        with the Region visible (A9/A10).
    """,

    "Evidence discipline — capture as you build": """
        Bespoke — the consulting discipline that makes AT2 pass or fail. Teach it as part of the build, not a write-up.
        • The core truth: the Deployment Report is EVIDENCED from what they capture live. You cannot go back
          and reconstruct a screenshot of a resource you built an hour ago in a state you've since changed.
        • Concretely: the AT2 template LISTS named screenshots — capture each one as you build that resource,
          with the Region + the named resource visible in frame.
        • Configs too: export IAM policies, SG rules, VPC settings AS you go → they land in Appendix B.
        • Accent-bold rhythm: build → capture → move on. Evidence is a step in the build, not homework afterwards.
        Misconception to pre-empt: "I'll build it all, then screenshot at the end." By then the console state
        has moved on and half the evidence is gone or inconsistent. Capture is live or it's lost.
        Question to pose: "You finish the whole build, then realise you never screenshotted the group creation
        — can you get that evidence back?" (not the live creation state — you'd have to rebuild; capture as you go).
        UoC/AT2 tie: ICTCLD401 PE 1/PE 2; feeds Appendices A (screenshots) + B (config exports) — criteria A9/A10.
    """,

    "Set up the build workspace": """
        DEMONSTRATION (educator-led — no recorded demo fits this one; screen a live walk-through or a
        pre-recorded screen capture you make). Show, then they replicate on the next slide.

        WHAT TO DEMONSTRATE:
        1. Sign in to the AWS Academy Learner Lab and set the Region to us-east-1 —
           [scenario: ap-southeast-2 (Sydney) | deploy: us-east-1]. Say the substitution out loud as you do it.
        2. Confirm the identity you're building as (the lab's provided credentials).
        3. Capture the FIRST named screenshot — the Region selector — into the evidence log, Region visible.
        4. Show where configuration exports come from (the point in the console you'll later export policies/SGs).

        WHAT TO EMPHASISE:
        • Region BEFORE anything else — model setting it first, deliberately.
        • Narrate the evidence capture: name the file the way the AT2 template names it; students must mirror this.
        • This is the workspace they'll build the whole foundation in — get it set up correctly once.

        PREP: clean Learner Lab open, evidence-log/template handy, the Accounting Baseline Design ready to open.
        ~5–8 min to screen + narrate before the activity.

        WHERE TO FIND THE RECORDED DEMO: none — per the demos catalogue, no recorded demo fits the C1
        account/Region/evidence workspace setup, so this demo stays live/bespoke (screen your own capture).
    """,

    "Set up your build workspace": """
        Facilitation — the first hands-on step of the cumulative practice build. They do what you just demoed.
        Tell students, in these words: "In the AWS Academy Learner Lab, set yourself up to build the Accounting
        System foundation. Set the Region, confirm your identity, capture your first evidence, then open and skim
        the supplied design. Work in the lab account and capture evidence as you go."
        The task, step by step (put on the board):
        1. Set the console Region to us-east-1 — [scenario: ap-southeast-2 (Sydney) | deploy: us-east-1] — and
           confirm it in your evidence.
        2. Confirm your build identity.
        3. Capture your first named evidence screenshot (Region visible) into your evidence log.
        4. Open the supplied Accounting Baseline Solution Design and skim it end to end.
        MUST PRODUCE: the first evidence screenshot (Region visible) in the evidence log, and a workspace set to
        us-east-1, ready to build.
        TIMING: ~15 min. Where they get stuck: the Learner Lab login/console hand-off (have the lab-launch steps
        ready), and forgetting to set Region before poking around — circulate and check the Region indicator.
        SHARE-BACK: ask one student to show their first evidence screenshot; confirm the Region is visible in frame.
        No-leakage note: this practice runs on the Accounting System (Ledgerline); the ASSESSED AT2 build is a
        different system — comparable, not identical. Keep them anchored to the Accounting baseline here.
    """,

    "IAM — the essential components": """
        AWS-sourced (ACF M04) — teach IAM as the account's "who can do what." Use the components diagram.
        Walk the four in order — user → group → role → policy — stressing the split: the first two are about
        PEOPLE, the last two about PERMISSIONS.
        • IAM user — one identity per person or app. Emphasise: never share a login; each person their own user
          (that is what gives you accountability and an audit trail).
        • IAM group — how you manage permissions at scale: set permissions ONCE on the group, not per person.
          Analogy: a team like "Finance" — add someone and they inherit the access.
        • IAM role — the one students find hardest. Unlike a user it has NO permanent credentials; it is ASSUMED
          temporarily. Key example for this build: an EC2 instance assumes a role to reach RDS/S3 — no passwords
          or keys stored on the server.
        • IAM policy — the JSON that says what is allowed. Everything is DENIED by default; a policy grants. You
          attach policies to groups/roles, never the JSON straight onto a person.
        Misconception to pre-empt: students conflate authentication (who you are = user) with authorisation
        (what you can do = policy). Say both words out loud.
        Question to pose: "The web server needs to read from S3 — do we give it a username and password?"
        (No — a role. This sets up the next slides.)
        UoC/AT2 tie: ICTCLD401 KE 8 + PC 1.5; this identity foundation is what the AT2 build is assessed on (A2);
        the specific groups to build come two slides on.
    """,

    "Securing access — the best practices": """
        AWS-sourced (ACF M04) — the rules that turn IAM components into a secure configuration. Teach as a checklist they'll apply.
        • Attach policies to GROUPS, assign users to groups — never policy straight onto an individual. This is
          the manageability rule from the last slide, now stated as practice.
        • Least privilege: grant only what the task needs; everything is denied by default, so you add exactly
          what's required and no more.
        • MFA on human users; protect the root user (use it only when you must). Root is the master key — you
          lock it away, you don't build with it.
        • Accent-bold: roles, NOT long-lived keys, for services — an EC2 instance ASSUMES a role to reach RDS/S3.
          This is the payoff of the "role has no password" point.
        Misconception to pre-empt: "least privilege means I'll just grant AdministratorAccess to save time and
        tighten it later." No — that IS the failure; you grant narrow from the start. Assessors look for it.
        Question to pose: "Why attach the policy to the group and not to each user directly?" (set once, everyone
        in the group inherits it; add/remove people without touching policies — manageable + auditable).
        UoC/AT2 tie: ICTCLD401 PC 1.5 (access protocols/policies) + KE 8; these best practices are exactly what
        the foundation-tier IAM build (A2) is marked against, incl. the Essential Eight MFA requirement.
    """,

    "The design's IAM model": """
        The design made concrete — teach the FOUR groups + role they must build, and why each exists. This is the spec for the activity.
        • Walk each with its purpose (don't just read names):
          - YAT-ICT-Admins — read-only infra + console AFTER handover (YAT runs it once MTS leaves).
          - MTS-Consultants — build admin (the consultants doing the work now).
          - Application-Service — the EC2 INSTANCE ROLE (not a human group) — RDS + S3 + CloudWatch access.
          - Finance-Auditors — read-only on logs / metrics / configs.
        • Accent-bold: enforce MFA on the human groups — an Essential Eight requirement they're assessed on.
        • Flag the trap: Application-Service is a ROLE, not a user group — it's the one students try to add a
          person to. It exists so the server can reach other services without stored credentials.
        Misconception to pre-empt: that all four are the same KIND of thing. Three are human groups; one is a
        service role — different creation path, different purpose.
        Question to pose: "Why does YAT-ICT-Admins get read-only, when they'll own the system after handover?"
        (least privilege during the build; they get operational access at handover, not build access now).
        UoC/AT2 tie: ICTCLD401 PC 1.6 (configure users/groups/permissions) + PC 2.1 (create users/groups) +
        PC 1.7 (assign security responsibilities); this exact model is what the A2 IAM build is scored on.
    """,

    "Build an IAM group, user & MFA": """
        DEMONSTRATION (recorded demo available). Screen it, then relate each step to OUR build. Then they
        replicate on the next slide.

        WHAT TO DEMONSTRATE (follow the recorded demo, then tie each step to the Accounting build):
        1. Create a group and attach a least-privilege policy.
        2. Create a user, add them to the group, enable MFA.
        3. Create the EC2 instance role (Application-Service) and attach its policy.
        4. Capture the IAM evidence screenshot (groups list + a user showing MFA enabled).

        WHAT TO EMPHASISE:
        • Permissions go on the GROUP, then the user joins it — not policy-on-user. Show the difference explicitly.
        • MFA — show the "assign MFA device" step; students routinely skip it and it's an Essential Eight
          requirement they're assessed on.
        • The role has NO password — point out there are no long-lived credentials; the instance assumes it.
          This is the payoff of the "IAM components" teaching slide.
        • Narrate the evidence capture — students must screenshot as they go for AT2; model it here.

        PREP: clean lab account open, the Accounting Baseline Design handy (for the group names), recorded demo
        queued. ~8–10 min to screen + narrate before the activity.

        WHERE TO FIND THE RECORDED DEMO: "Recorded demo: IAM" — ACF M04 · S31 (AWS Academy Cloud Foundations,
        Module 04 "AWS Cloud Security"), inside the instructor deck (original-materials/AWS-Instructor
        Presentations/…). Instructor-facing — screen it in class, don't distribute to students. Preview and cue
        it to this slide before class.
    """,

    "Build the IAM model": """
        Facilitation — the C2 practice; they build the design's IAM foundation in the lab, evidencing as they go.
        Tell students, in these words: "Open the lab and the Accounting Baseline Design. Build the IAM foundation
        for the MTS engagement — exactly the groups and role in the design. Work in the lab account and capture
        evidence as you go."
        The task, step by step (put on the board / read out):
        1. Create the four groups from the design: YAT-ICT-Admins, MTS-Consultants, Application-Service (this one
           is the EC2 ROLE, not a human group), Finance-Auditors.
        2. Attach a least-privilege policy to each — only what that group needs.
        3. Create at least one user in each HUMAN group and enable MFA on it.
        4. Create the Application-Service role for the EC2 instance (RDS + S3 + CloudWatch access).
        5. Capture the IAM evidence: the groups list, a user with MFA on, and the role.
        MUST PRODUCE (the AT2 evidence): screenshots of the groups list, one user with MFA enabled, and the role
        with its policy.
        TIMING: ~30 min. Circulate — the two common sticking points are (a) forgetting MFA and (b) trying to
        attach a policy straight to a user.
        SHARE-BACK: ask one student to show their groups list; confirm least privilege (no AdministratorAccess
        shortcuts).
        No-leakage note: this practice uses the Accounting baseline; the assessed AT2 task uses a different system
        — comparable, not identical.
    """,

    "The shared responsibility model": """
        AWS-sourced (ACF M04) — teach the security dividing line. Use the shared-responsibility diagram.
        • The split, stated cleanly: AWS handles security OF the cloud — physical data centres, hardware, the
          network, the virtualisation infrastructure. YOU handle security IN the cloud — the EC2 OS (patching),
          your applications, security-group config, IAM, account management, and your DATA.
        • Accent-bold: knowing exactly where the line falls tells you what you must CONFIGURE versus what you can
          RELY ON. That's the whole practical value of the model.
        • Anchor it to the build: on our foundation, IAM and MFA sit firmly on the "you" side — which is why the
          last two slides mattered.
        Misconception to pre-empt: "it's the cloud, so AWS secures it all." No — AWS secures the infrastructure;
        misconfiguring a security group or skipping MFA is entirely on YOU, and that's where breaches happen.
        Question to pose: "The EC2 operating system needs a security patch — whose job is that, AWS's or yours?"
        (yours, on IaaS — sets up the next slide where the line shifts by service).
        UoC/AT2 tie: ICTCLD401 PC 1.2 + KE 7 (user/business/vendor responsibilities under shared models) +
        ICTCLD502 PC 1.3; the shared-responsibility assignment is marked under A2 (section detail A4).
    """,

    "The line shifts with the service": """
        AWS-sourced (ACF M04) — the crucial nuance: the responsibility line is not fixed; it MOVES by service type.
        • IaaS (EC2): you manage MORE — the OS, patching, security groups, access controls. Maximum control,
          maximum responsibility.
        • PaaS (RDS): AWS handles the OS, database patching, the firewall, DR; you manage your DATA + access. The
          line has shifted toward AWS.
        • Accent-bold: more managed = more on AWS. The SERVICE TYPE decides where the line falls — this is the
          IaaS/PaaS spectrum from Topic 1 now expressed as a security boundary.
        Misconception to pre-empt: that shared responsibility is one fixed diagram. It isn't — the same account
        can have EC2 (line well toward you) and RDS (line well toward AWS) side by side; you must map each service.
        Question to pose: "SQL Server needs patching — who does it if it's on an EC2 instance vs on RDS?" (EC2:
        you; RDS: AWS — same software, different service, different owner).
        UoC/AT2 tie: ICTCLD502 PC 1.3 (identify the LEVEL of shared responsibility per business needs) + KE 7;
        this per-service reasoning is exactly what the build assignment (next activity) requires.
    """,

    "Assigning responsibility on this build": """
        Bespoke — apply the model to the actual Accounting foundation. This is the bridge from concept to the activity.
        • The task in one line: map each layer of the Accounting build to its owner — AWS · YAT ICT · MTS (build)
          · end-users. Four possible owners, not two.
        • Point them at the source: the supplied design's security section NAMES the split; their job is to apply
          it, not invent it (the working-to-a-design discipline again).
        • Worked examples (the sub-bullet): AWS patches the RDS host · YAT patches the EC2 OS · MTS sets the IAM +
          SG config at build time. Note how the owner changes by both service AND lifecycle stage (build vs run).
        Misconception to pre-empt: that it's a binary AWS-vs-"you." Here "you" splits three ways — YAT ICT (the
        ongoing owner), MTS (the builder, now), and end-users. Who's responsible depends on the phase too.
        Question to pose: "Security-group configuration — who owns it during the build, and who owns it after
        handover?" (MTS sets it at build; YAT ICT owns it operationally after — draws out the build/run split).
        UoC/AT2 tie: ICTCLD401 PC 1.7 + KE 7 + ICTCLD502 PC 1.3; produces the input for the Deployment Report's
        security section (A2 / A4).
    """,

    "Complete the shared-responsibility assignment": """
        Facilitation — the C3 practice. Note this one is ANALYSIS, not a console build (say so up front).
        Tell students, in these words: "No building this time — an analysis task in the style of the AWS scenario.
        For each part of the Accounting foundation, name who is responsible — AWS, or you (YAT ICT / MTS) — using
        the supplied design and the shared-responsibility model. Write it up as about half a page."
        The parts to assign (put up):
        1. EC2 OS patching · security-group settings · application config · IAM / MFA
        2. SQL Server patching on RDS · physical data-centre security · S3 bucket access config · data
        MUST PRODUCE: a ~½-page written assignment naming the responsible party for each part, justified against
        the design + the model — this feeds their Deployment Report's security section.
        TIMING: ~15 min, then discuss as a group.
        Where they get stuck: the ones that shift by service — SQL Server patching is AWS's on RDS but would be
        theirs on EC2; physical security is always AWS. Circulate and probe the reasoning, not just the answer.
        SHARE-BACK: take the two trickiest (RDS patching, physical data-centre security), get the room's answer,
        and confirm WHY — the reasoning is the assessable skill.
        No-leakage note: practice on the Accounting foundation; AT2 assesses the same reasoning on a different
        system — comparable, not identical.
    """,

}
