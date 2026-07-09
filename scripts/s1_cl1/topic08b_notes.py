"""Teacher speaker notes for Topic 08b — The workload tier: data & storage (S1-CL1).

One entry per teaching/demo/activity slide. Keys are the EXACT slide title strings from
build_s1_cl1_topic08b_deck.py so they match at build time. Read only by the teacher
(Presenter View), never shown to students.
"""

NOTES = {

    "The data tier": """
        Set the scene for 8b — a bridge slide, not new content. Remind them where 8a left off.
        • 8a stood up the COMPUTE and put it behind a scaling load balancer; the app can run and heal.
        • 8b (accent-bold) adds the DATA layer: a managed database (Amazon RDS) and object/archive
          storage (Amazon S3 + Glacier). Same design, same network — now the tiers that hold the data.
        • Keep the discipline explicit: still building the SUPPLIED design, still capturing evidence as
          they go. Nothing free-hand.
        • Set the rhythm for the session: watch the recorded demo, then do it yourself in the lab.
        Misconception to pre-empt: that the database and storage are "extra" or optional. They're core PE
        — the workload tier isn't done until data + storage are built and evidenced.
        Question to pose: "The app servers are up — so why can't YAT use Ledgerline yet?" (no database
        for the records, no store for the scanned documents).
        UoC/AT tie: sets up ICTCLD401 PC 2.5 (managed DB) + the storage KE; both fold into the core PE
        (compute + storage + database + autoscaling in a VPC) that AT2 §4.7/§4.8 evidence.
    """,

    "Databases, and who runs them": """
        Vendor-neutral PRIMER — no AWS yet. Establish two ideas: what a relational DB is, and that
        someone always has to operate it. This is the hinge the managed-vs-self-hosted teach turns on.
        • A relational database stores STRUCTURED data in tables, queried with SQL — Ledgerline's
          accounts, ledgers and transactions are exactly this shape.
        • The operations reality (walk it slowly): install + patch the OS and the DB engine, take and
          test backups, secure it, scale it. That work never goes away — the only question is WHO does it.
        • The split (accent-bold): self-hosted = YOU do all of it (e.g. on an EC2 instance); managed =
          the cloud provider does it. Plant this now; RDS is the payoff two slides on.
        Misconception to pre-empt: "the cloud means no database admin at all." No — managed shifts the
        OS/engine/backup toil to AWS, but schema, data and query optimisation stay yours.
        Question to pose: "If Ledgerline's database lived on one EC2 server, whose job is the 2am patch and
        the nightly backup?" (yours — the argument for managed).
        UoC/AT tie: ICTCLD401 KE 6 (relational; self-hosted vs managed vs cloud-native) — the primer the
        PC 2.5 build rests on.
    """,

    "Self-hosted vs managed — EC2 vs RDS": """
        The AWS-context teach for the primer — make the trade-off concrete with EC2 vs RDS.
        • Run it yourself on EC2: full control of engine and OS — but you own ALL the admin work (patching,
          backups, scaling, availability). Control has a labour cost.
        • Amazon RDS (accent-bold) is a MANAGED service: AWS handles OS/DB install + patching, automated
          backups, scaling and availability. The toil from the last slide is offloaded.
        • Be precise about the line: you KEEP application optimisation and your data — managed isn't
          "hands off everything," it's "hands off the undifferentiated ops."
        • The trade-off in one line: control vs effort — choose managed UNLESS you need engine-level
          control. For a small RTO with thin cloud skills, managed is the obvious call.
        Misconception to pre-empt: "managed = less capable / a toy database." It's the same SQL Server
        engine; you're paying AWS to run the plumbing, not getting a lesser product.
        Question to pose: "What would make YAT choose self-hosted on EC2 instead — and does Ledgerline
        need any of that?" (engine-level control; it doesn't — so RDS).
        UoC/AT tie: ICTCLD401 PC 2.5 + KE 6; this is the reasoning a student writes into AT2 §4.7.
    """,

    "Amazon RDS": """
        Anchor the service — the concrete anatomy students must be able to name and configure.
        • RDS sets up and OPERATES a relational database in the cloud; engines include Microsoft SQL
          Server (Ledgerline's engine — preserved, not migrated to something new).
        • A DB instance has two dials: an instance CLASS (CPU/memory/network) and STORAGE (gp3 SSD or
          provisioned IOPS). Same mental model as sizing an EC2 instance in 8a.
        • It runs INSIDE your VPC (not on the public internet); automated backups give point-in-time
          restore; encryption at rest is available. Tie each back to the network they built in Topic 7.
        • Multi-AZ (accent-bold) gives a standby in another AZ for high availability — NAME it, then park
          it: it's deferred to AT3. Baseline here is single-AZ.
        Misconception to pre-empt: "RDS is public / lives outside my network like a SaaS." No — it sits in
        your private subnet, reachable only from where you allow.
        Question to pose: "Two dials size an RDS instance — which two, and which one did we decide in C2?"
        (class + storage; class = C2 decision).
        UoC/AT tie: ICTCLD401 PC 2.5 + KE 5 (backups/lifecycle); the depth ceiling is deliberate —
        Multi-AZ/HA is AT3, not here.
    """,

    "The database you'll build": """
        The design's specifics — this is the exact instance students provision, straight from the
        supplied Solution Design. Read it as a spec, not a lecture.
        • RDS for SQL Server, STANDARD edition — chosen to preserve the existing engine + data; not a
          re-platform.
        • Instance class db.m6i.large (a C2 decision, implementer-set); gp3 storage ~22 GB + growth; in
          private-data-a, locked to sg-db, NOT public. Every one of those is a design mandate.
        • Multi-AZ OFF at baseline; KMS encryption ON; automated backups + tx-log backups to RPO <= 1 hour.
        • The boundary that matters most (accent-bold): MTS provisions an EMPTY instance — schema and data
          migration are YAT ICT's responsibility. Students build the container, not the contents.
        Misconception to pre-empt: "I need to load Ledgerline's data to finish." No — an empty, correctly-
        configured instance is the deliverable; loading data is the customer's job and out of scope.
        Question to pose: "Why does MTS hand over an empty database rather than migrate the data itself?"
        (scope + data-custody — it's YAT's data and responsibility).
        UoC/AT tie: ICTCLD401 PC 2.5; the settings here map one-to-one to AT2 §4.7 evidence.
    """,

    "Provision an RDS database": """
        WHERE TO FIND THE RECORDED DEMO: AWS Academy Cloud Foundations -> Module 08 (Databases) -> slide 22,
        "Recorded demo: Amazon RDS console"; pair it with AWS Academy Cloud Architecting -> Module 06 ->
        slide 37, "Demo: Amazon RDS Automated Backup & Read Replicas" for the backup/RPO step. Both live in
        original-materials/AWS-Instructor Presentations/… — instructor-facing, screen in class, don't
        distribute. Preview and queue both before class.

        WHAT TO DEMONSTRATE (follow the recorded demos, then relate each step to OUR build):
        1. Create a DB subnet group and the database security group (sg-db).
        2. Launch an RDS DB instance — choose engine (SQL Server Standard), instance class, storage and
           backup settings.
        3. Connect from the application tier to confirm the database is reachable.

        WHAT TO EMPHASISE:
        • The subnet group is what pins RDS into private-data-a — show it lands in the private subnet, not
          public. This is the network discipline from Topic 7 paying off.
        • Turn ON automated backups + KMS encryption during creation; narrate RPO <= 1 hour (use the ACA M06
          backup demo here). Leave Multi-AZ OFF — say out loud that HA is AT3.
        • Show the app-tier -> DB connectivity test; this completes the PC 2.6 test begun in Topic 7.
        • Narrate the evidence capture — instance, network/SG, backup + encryption settings — model it.

        PREP: clean lab, the supplied Solution Design open for the exact settings, both demos queued.
        ~8-10 min to screen + narrate before the activity.
    """,

    "Provision the Ledgerline database": """
        Facilitation — the C3 practice build. They provision the database to the design and complete the
        connectivity test. You circulate; they build and evidence.
        Tell students, in these words: "Open the lab and the Accounting Baseline Solution Design. Provision
        Ledgerline's database exactly to the design — RDS for SQL Server in the private data subnet — then
        test the app can reach it. Capture evidence as you go."
        The task, step by step (put on the board / read out):
        1. Provision RDS for SQL Server (class + storage per the design), in private-data-a with sg-db, NOT
           public.
        2. Enable automated backups + KMS encryption; leave Multi-AZ OFF (baseline).
        3. Test app -> database connectivity (this completes the Topic 7 connectivity test) and fix any
           errors.
        4. Capture evidence — the instance, its network/SG, backup + encryption settings.
        MUST PRODUCE (AT2 evidence): screenshots of the RDS instance, its subnet/SG placement, and the
        backup + encryption settings, plus a successful app->db connectivity check.
        TIMING: ~20 min. Where they get stuck: (a) putting RDS in the wrong subnet / making it public —
        send them back to the subnet group; (b) SG rules blocking the app->db test — check sg-db allows
        the app SG on the DB port.
        SHARE-BACK: ask one student to show their instance is private + encrypted with Multi-AZ off; confirm
        nobody flipped HA on.
        No-leakage note: this practice uses the Accounting / Ledgerline system; the ASSESSED build is a
        different system on the LMS — comparable, not identical.
    """,

    "Block vs object vs archive": """
        Vendor-neutral PRIMER opening the storage section — the block/object/archive distinction is the
        examinable point, so make it stick before any AWS names.
        • Block storage = a virtual DISK attached to one instance (EBS) — you can change one block of a
          file in place. This is the EC2 disk from 8a; students already met it.
        • Object storage (accent-bold) = whole files (OBJECTS) + metadata, reached by API, virtually
          unlimited (S3). You replace a whole object; no OS mounts it like a drive.
        • Archive storage = very cheap, SLOW to retrieve, for long-term retention (Glacier). Cold storage.
        • The teaching line: match the storage to the job — performance AND cost both depend on the choice.
        Misconception to pre-empt: "S3 is just a hard drive in the cloud." No — it's object storage reached
        by API; you don't mount it like a block disk. This block-vs-object line is the whole slide.
        Question to pose: "Ledgerline's scanned invoices — block, object or archive, and why?" (object for
        the live docs; archive/Glacier once they age into the 7-year hold).
        UoC/AT tie: ICTCLD401 KE 6 (storage options — block/object/archive); EBS = block (C1), S3/Glacier
        = object/archive (C4). The distinction is explicit by design.
    """,

    "Amazon S3": """
        Anchor the service — the properties that matter for a correct, secure bucket.
        • S3 stores OBJECTS in BUCKETS; virtually unlimited; designed for 11 nines of durability (say it
          plainly — you effectively don't lose objects).
        • Buckets are REGION-scoped but their NAME is globally unique; access is granular (IAM + bucket
          settings). The name being global trips students up — flag it.
        • The three protections (accent-bold): BLOCK public access, ENCRYPT (SSE), and enable VERSIONING.
          For a client holding financial records these aren't optional niceties — they're the baseline.
        • Common uses: backups, application assets, document stores — exactly Ledgerline's scanned invoices
          and off-instance backups.
        Misconception to pre-empt: "S3 buckets are public by default / someone could stumble on my files."
        Modern default is private; the risk is a MIS-configuration that opens them — which is why "block
        public access" is a deliberate, evidenced step.
        Question to pose: "A bucket name is globally unique but the bucket lives in one Region — why does
        that distinction matter for YAT's data residency?" (data sits in the Region; the name is just a
        global label).
        UoC/AT tie: ICTCLD401 KE 6 (object storage) + KE 5 (backups); the three protections are AT2 §4.8
        evidence.
    """,

    "Lifecycle to Glacier — retention": """
        Teach the retention mechanism — this is how the design meets a hard business/legal requirement, so
        anchor it to the 7-year rule, not the feature for its own sake.
        • Amazon S3 Glacier is extremely low-cost ARCHIVE storage; retrieval takes minutes to hours — cheap
          because it's cold, not instant.
        • A LIFECYCLE RULE (accent-bold) transitions objects from S3 to Glacier by AGE — automatic, and
          cheaper the longer data lives. Set once, runs forever; no one moves files by hand.
        • Object Lock enforces WRITE-ONCE retention — for records that must not be altered or deleted. This
          is the integrity guarantee auditors want on financial records.
        • The payoff line: this is how the design meets the 7-year financial-records retention — a
          requirement, met by a rule, evidenced.
        Misconception to pre-empt: "Glacier is a separate service I upload to." No — objects LAND in S3 and
        a lifecycle rule TRANSITIONS them to Glacier automatically; students shouldn't upload straight to
        an archive tier.
        Question to pose: "Financial records must be kept 7 years and not tampered with — which two features
        cover 'kept cheaply' and 'not tampered with'?" (lifecycle-to-Glacier + Object Lock).
        UoC/AT tie: ICTCLD401 KE 5 (storage backups + lifecycle); directly evidenced in AT2 §4.8.
    """,

    "The storage you'll build": """
        The design's specifics — the exact buckets and settings students create, from the supplied design.
        Read as a spec.
        • Documents bucket — scanned invoices / POs / supporting docs; lifecycle to Glacier for the 7-year
          hold. This bucket is where the retention rule lives.
        • Backups bucket — off-instance SQL backup exports and file snapshots (complements RDS's own
          automated backups; belt and braces).
        • Both buckets (accent-bold): block ALL public access; SSE(-KMS) encryption; versioning ON; access
          logging. Same three protections from the S3 teach, applied.
        • Object Lock CONSIDERED for the financial-records hold — flag it as a design consideration on the
          Documents bucket, not an afterthought.
        Misconception to pre-empt: "one bucket for everything." The design separates Documents (retained,
        Glacier-bound) from Backups (operational) on purpose — different lifecycles, different roles.
        Question to pose: "Why does the design put the lifecycle-to-Glacier rule on the Documents bucket but
        not the Backups bucket?" (7-year records retention lives with the documents; backups have a
        different rotation).
        UoC/AT tie: ICTCLD401 KE 5/KE 6; each setting maps to AT2 §4.8 evidence.
    """,

    "S3 buckets, versioning & lifecycle": """
        WHERE TO FIND THE RECORDED DEMO: for the bucket build, AWS Academy Cloud Foundations -> Module 07
        (Storage) -> slide 35, "Recorded demo: Amazon S3", with slide 55 "Recorded demo: Amazon S3 Glacier"
        for the archive tier. For versioning + lifecycle, AWS Academy Cloud Architecting -> Module 04 ->
        slide 36 "Demo: Managing Lifecycles in Amazon S3" and slide 43 "Demo: Amazon S3 Versioning". All in
        original-materials/AWS-Instructor Presentations/… — instructor-facing, screen in class, don't
        distribute. Preview and queue before class.

        WHAT TO DEMONSTRATE (follow the recorded demos, then relate each step to OUR build):
        1. Create a bucket; block public access; enable encryption and versioning.
        2. Add a lifecycle rule to transition objects to Glacier after an age threshold.
        3. Point out Glacier is the ARCHIVE tier the lifecycle rule targets — not a separate upload.

        WHAT TO EMPHASISE:
        • "Block public access" is a deliberate, evidenced click — show the toggle and say why it matters
          for financial data.
        • Enable versioning BEFORE objects go in; explain it protects against overwrite/delete.
        • On the lifecycle rule, tie the age threshold to the 7-year retention story — this is the design
          requirement made real (use the ACA M04 lifecycle demo here).
        • Narrate the evidence capture — bucket settings, encryption, versioning, the lifecycle rule.

        PREP: clean lab, the supplied Solution Design open for the bucket names/settings, all four demo
        clips queued. ~8-10 min to screen + narrate before the activity.
    """,

    "Create the buckets per the design": """
        Facilitation — the C4 practice build. Students create both buckets to the design and evidence every
        setting. You circulate; they build.
        Tell students, in these words: "Open the lab and the Accounting Baseline Solution Design. Create
        Ledgerline's storage exactly to the design — the two buckets, each locked down and versioned, with
        the retention rule on Documents. Capture evidence of every setting as you go."
        The task, step by step (put on the board / read out):
        1. Create the Documents bucket and the Backups bucket.
        2. On each: block public access; enable SSE encryption + versioning + access logging.
        3. Add the lifecycle rule transitioning Documents objects to Glacier (the 7-year retention).
        4. Capture evidence — bucket settings, encryption, versioning, the lifecycle rule.
        MUST PRODUCE (AT2 evidence): screenshots of both buckets showing public access blocked, encryption
        on, versioning on, and the Documents lifecycle-to-Glacier rule.
        TIMING: ~15 min. Where they get stuck: (a) enabling versioning after uploading test objects — show
        it's a per-bucket setting to turn on first; (b) the lifecycle rule on the wrong bucket — it belongs
        on Documents, not Backups.
        SHARE-BACK: ask one student to show a bucket with public access blocked + the Glacier lifecycle
        rule; confirm nobody left a bucket public.
        No-leakage note: this practice uses the Accounting / Ledgerline system; the ASSESSED build is a
        different system on the LMS — comparable, not identical.
    """,

}
