# Topic 08a The workload tier — compute & elasticity — Slide plan
> **Covers:** Topic 08 — see coverage.md
> **Subtitle:** Launch the application server, give it storage, and put it behind a load balancer that scales
> **Covers-components:** C1, C2

## Slides

### Opener
- [BESPOKE] Filling the network
  - Topic 7 laid the network; now the workload goes inside it.
  - 8a — compute + elasticity (this deck); 8b — the managed database + storage.
  - Still building the supplied design, still capturing evidence as you go.
  - For every AWS build task: watch the recorded demo, then do it yourself.
  kicker: the workload moves in
  image: none
  notes:
    Frame the whole Topic — set the shape, don't teach content yet. Topic 7 laid an empty network;
    Topic 8 moves the workload in.
    • Where this fits: they're MTS consultants building the SUPPLIED design in the lab. The thinking
    was done in AT1; AT2 is disciplined execution + evidence.
    • Orient them: this is deck 8a (compute + elasticity); 8b covers the managed database + storage.
    Same Topic 8, split for manageability — say so, so no one thinks they've skipped anything.
    • Stress the working rhythm (last bullet): every AWS build task = watch the recorded demo, THEN do
    it yourself, capturing named evidence as you go. That rhythm repeats all Topic.
    Misconception to pre-empt: "we're designing now." No — the design is given; deviating from it is an
    error, not initiative. Build what's specified; the implementer decisions are already flagged.
    Question to pose: "What's the difference between what you did in AT1 and what you do here?" (advise
    vs build-and-evidence).
    UoC/AT2 tie: Topic 8 carries the core ICTCLD401 PE — compute/storage/database/autoscaling in a VPC;
    this deck opens on C1 compute + C2 elasticity.

### C1 — Compute — the application server
- Teaches: [ICTCLD401 PC 2.3] · [ICTCLD401 PC 2.4] · [ICTCLD401 PC 2.6] · [ICTCLD401 KE 5] · [ICTCLD401 KE 6] · [ICTCLD401 KE 6] · [ICTCLD401 PE 2]
- Kicker: EC2 + EBS
- [BESPOKE] What a server is — and a virtual one
  - A server is a computer that runs your application for others to use.
  - Its size is four dimensions: CPU (processing), memory (RAM), disk (storage), network bandwidth.
  - A virtual machine (VM) is a software-defined server — you rent one and size it to the workload.
  kicker: the fundamentals
  image: none
  notes:
    Vendor-neutral primer — no assumed baseline. Get the mental model of a server solid BEFORE EC2.
    • Walk it plainly: a server is just a computer that runs your application for others to use.
    • The four dimensions (make them concrete): CPU, memory (RAM), disk, network bandwidth — this is
    how you "size" a server, and it's exactly the KE 5 language they're assessed on.
    • The shift (bolded): a virtual machine is a software-defined server — you RENT one and size it to
    the workload, instead of buying a physical box. Callback to Topic 1's "infrastructure as software".
    Misconception to pre-empt: "virtual = less real / less powerful." No — a VM is a full server; it
    just runs as software on shared hardware, and you can resize it in ways a physical box never allows.
    Question to pose: "If you had to size a server for Ledgerline, what four things would you be
    deciding?" (CPU / RAM / disk / network — the four dimensions).
    UoC/AT2 tie: ICTCLD401 KE 5 (VM sizing) + KE 6 (virtual vs physical) — the primer under PC 2.3.
- [BESPOKE] Amazon EC2
  - Amazon EC2 provides resizable virtual machines — called instances — in the cloud.
  - You get full control of the guest OS (Windows or Linux).
  - You launch an instance from an Amazon Machine Image (AMI) into a subnet, ready in minutes.
  - You control traffic to and from it with security groups.
  kicker: AWS · ACF M06 S10
  image: none
  notes:
    The AWS-context teach after the primer — put names to the concept. Keep it recognition-level; the
    detail is the next slide.
    • Walk the bullets: EC2 gives resizable virtual machines called INSTANCES; you get full control of
    the guest OS (Windows or Linux); you launch from an AMI into a subnet, ready in minutes.
    • The accent line: security groups control traffic in and out — callback to Topic 7, where they
    built the SG shells the EC2 instance now fills.
    • Tie to the model: EC2 is IaaS (Topic 1) — you run the OS and app, AWS runs the hardware.
    Misconception to pre-empt: "an instance is a fixed size you're stuck with." No — you can stop it,
    change the instance type, and start it bigger; resizable is the point.
    Question to pose: "EC2 is IaaS — so after AWS hands you the instance, whose job is the operating
    system and patching?" (yours — the trade-off for full control).
    UoC/AT2 tie: ICTCLD401 PC 2.3 (create the VM to requirements); the SG link back to PC 2.6.
- [BESPOKE] Launching an instance — the key choices
  - AMI — the template (OS + any pre-installed software).
  - Instance type — family.generation.size (e.g. m6i.large) sets CPU / RAM / storage / network.
  - Network — which VPC and subnet; IAM role — an instance profile so the app can call AWS services.
  - User data — a first-boot script; storage — root + data volumes; tags; security group; key pair.
  kicker: AWS · ACF M06 S11–S26
  image: none
  notes:
    The workhorse teach for C1 — the launch-wizard decisions, so the demo and activity aren't a blur of
    unfamiliar fields. Don't read the list; explain what each choice DOES.
    • AMI = the template (OS + pre-installed software). Instance type = family.generation.size (e.g.
    m6i.large) — this is where the four sizing dimensions become a concrete pick.
    • Network = which VPC/subnet it lands in; IAM role = an instance profile so the app calls AWS
    services with NO stored keys (callback to the Topic 6 role they built).
    • User data = a first-boot script; storage = root + data volumes; plus tags, security group, key pair.
    Misconception to pre-empt: "the instance type is just 'how fast'." It sets CPU, RAM, storage AND
    network together — under-size any one and the app suffers; it's a balanced choice, not a speed dial.
    Question to pose: "Why give the instance an IAM ROLE instead of putting an access key on the box?"
    (no long-lived credentials to leak — the payoff of the Topic 6 IAM teaching).
    UoC/AT2 tie: ICTCLD401 PC 2.3; the launch choices are exactly what the §4.5 Compute evidence shows.
- [BESPOKE] Storage on the instance — EBS (block)
  - Block storage = a virtual disk attached to one instance (like a drive in a PC).
  - Amazon EBS is durable block storage — stop and start the instance and the data is still there.
  - (Instance store is ephemeral — it's lost when the instance stops.)
  - gp3 SSD volumes; you can resize or change type without downtime.
  kicker: primer + AWS · ACF M06 S22
  image: none
  notes:
    Primer + AWS teach for the disk on the server — and the first half of the examinable block-vs-object
    distinction (object storage / S3 is 8b).
    • Primer: block storage = a virtual disk attached to ONE instance, just like a drive inside a PC.
    • The accent line: Amazon EBS is DURABLE block storage — stop/start the instance and the data
    survives. Contrast hard with instance store (ephemeral, lost on stop) — bracketed on purpose.
    • gp3 SSD volumes; you can resize or change type WITHOUT downtime — reinforce "infrastructure as
    software": the disk is elastic too.
    Misconception to pre-empt: "EBS is like S3 / a shared drive." No — EBS attaches to a single instance
    as a block disk; it is not object storage and not shared. This block-vs-object line is the whole
    point, and it returns in 8b.
    Question to pose: "If you store the app's working data on INSTANCE STORE and the instance stops,
    what happens?" (it's gone — that's why the design uses EBS).
    UoC/AT2 tie: ICTCLD401 PC 2.4 (define/add/expand storage on the VM) + KE 6 storage options (block).
- [BESPOKE] The compute you'll build
  - EC2 Windows Server 2016 (m6i.large*, a C1 implementer decision), in private-app-a, no public IP.
  - An instance role grants it access to RDS, S3 and CloudWatch — no stored keys.
  - EBS: gp3 root 80 GB + a gp3 data volume (footprint + 12-month growth + headroom).
  - Attach sg-app; tag per the naming standard. (*= implementer decision.)
  kicker: the supplied design
  image: none
  notes:
    Pivot from generic teaching to THIS design — read the supplied spec so the activity is unambiguous.
    Everything here is specified; the *-marked items are already-made implementer decisions, not open
    questions.
    • Walk it: EC2 Windows Server 2016 (m6i.large*), in private-app-a, NO public IP — a private app
    server reached through the network, not the internet.
    • An instance role grants access to RDS, S3 and CloudWatch — no stored keys (callback again).
    • EBS: gp3 root 80 GB + a gp3 data volume sized for footprint + 12-month growth + headroom; attach
    sg-app; tag per the naming standard.
    Misconception to pre-empt: "no public IP must be a mistake — how do users reach it?" No — it's private
    by design; access comes via the ALB/network, and staff over the VPN. Private-by-default is correct.
    Question to pose: "Why does the app server sit in private-app-a with no public IP?" (defence in
    depth — nothing is exposed to the internet that doesn't need to be).
    UoC/AT2 tie: ICTCLD401 PC 2.3 + PC 2.4; this is the §4.5 Compute build, evidenced in Appendix A/B.
- [DEMO] Launch an EC2 instance
  - Use the Launch Instance Wizard: choose the AMI and instance type.
  - Set the network (VPC/subnet), IAM role, storage volumes, tags and security group.
  - Launch, then view the instance, its volumes and monitoring.
  - Resize the instance type / root volume to see how it changes.
  source: ACF M06 · EC2 (S35)
  image: none
  notes:
    DEMONSTRATION slide (recorded demo). Screen it, then relate each step to OUR supplied design before
    the students do it themselves — teach -> DEMONSTRATE -> practice.
    
    WHERE TO FIND THE RECORDED DEMO: AWS Academy Cloud Foundations → Module 06 (Compute) → slide 35,
    "Recorded Amazon EC2 demonstration", inside the ACF M06 instructor deck (original-materials/
    AWS-Instructor Presentations/…). Instructor-facing — screen it in class, don't distribute to
    students. Preview it and cue it to this slide before class.
    
    WHAT TO DEMONSTRATE (follow the recorded demo, then map each step to our build):
    1. Launch Instance Wizard — choose the AMI and instance type.
    2. Set the network (VPC/subnet), IAM role, storage volumes, tags and security group.
    3. Launch, then view the instance, its volumes and monitoring.
    4. Resize the instance type / root volume to show how it changes.
    
    WHAT TO EMPHASISE:
    • Ours is Windows Server 2016 into private-app-a with NO public IP — point out where in the wizard
    that's set (subnet + auto-assign public IP off).
    • The instance ROLE, not an access key — show the "IAM instance profile" field explicitly.
    • Add the gp3 DATA volume as well as the root — students forget the second volume.
    • Narrate the evidence capture — the instance, its volumes, the Region — model it as you go.
    
    PREP: clean Learner Lab open, the supplied design handy (instance type, subnet, tags), demo queued.
    ~8-10 min to screen + narrate before the activity. (Learner Lab deploys to us-east-1 — the design's
    Region is simulated; don't let the Region field derail them.)
- [EX] Launch the Ledgerline server
  - In the lab, per the supplied design, launch the application server:
    - AMI Windows Server 2016; instance type per the design; into private-app-a (no public IP)
    - attach the instance role + sg-app; add the gp3 data volume; tag it
  - Capture named evidence — the instance, its volumes, the Region.
  timer: ~25 min
  image: none
  notes:
    Facilitation — the C1 hands-on build on the PRACTICE engagement. They build; you circulate.
    Tell students, in these words: "Open the lab and the supplied Solution Design. Launch the Ledgerline
    application server exactly to the design — no improvising — and capture named evidence as you go."
    Steps (put on the board):
    1. Launch from AMI Windows Server 2016; instance type per the design.
    2. Into private-app-a, with NO public IP.
    3. Attach the instance role + sg-app; add the gp3 data volume; tag it per the naming standard.
    4. Capture evidence — the instance, its volumes, the Region.
    Must produce: a running EC2 instance matching the design + named evidence screenshots (instance,
    volumes, Region) in their evidence log.
    Timing: ~25 min. Where they get stuck: forgetting to turn OFF auto-assign public IP (they land in
    the wrong subnet or public); missing the second (data) volume; skipping tags. Circulate on these three.
    Share-back prompt: "Show me your evidence for the data volume — how do we know it's attached?"
    No-leakage note: Ledgerline is the PRACTICE client; AT2 assesses the SAME build on the LMS system —
    comparable, not identical. Keep them anchored to the supplied design here.
- [TAKEAWAYS] Section 1 · Compute
  - EC2 = a resizable virtual machine, launched from an AMI into your subnet.
  - The instance type sets CPU / RAM / storage / network — size it to the workload.
  - EBS = durable block storage attached to the instance (survives stop/start).
  - Build to the supplied design; no public IP; capture evidence as you go.
  image: none

### C2 — Elasticity — load balancing & scaling
- Teaches: [ICTCLD401 PC 3.1] · [ICTCLD401 PC 3.2] · [ICTCLD401 KE 5, 6]
- Kicker: ALB + Auto Scaling
- [BESPOKE] Load balancing & scaling
  - A load balancer spreads incoming traffic across several instances and checks their health.
  - Elasticity = the infrastructure grows and shrinks as demand changes.
  - Vertical scaling = replace with a bigger instance; horizontal scaling = add more instances.
  - Horizontal scaling is the cloud way — and the basis of high availability later.
  kicker: primer + AWS · ACA M10 S19
  image: none
  notes:
    Open Section 2 with the vendor-neutral primer — the two ideas C2 turns on, before any AWS names.
    • A load balancer spreads incoming traffic across several instances and checks their health.
    • Elasticity = the infrastructure grows and shrinks as demand changes — the cloud advantage over a
    fixed on-prem box (callback to Topic 1's over-provisioning pain).
    • The accent line: vertical scaling = replace with a bigger instance; horizontal = add MORE
    instances. Make the distinction crisp — it's examinable and students blur it.
    • Last bullet: horizontal is the cloud way, and the basis of high availability LATER (AT3).
    Misconception to pre-empt: "scaling means making the server bigger." That's only vertical; the cloud
    pattern is horizontal — many small instances behind a balancer, added/removed automatically.
    Question to pose: "Ledgerline gets a month-end spike — do you buy a bigger server, or add more of
    the same for a few days? Which is cheaper and safer?" (horizontal — pay only for the spike).
    UoC/AT2 tie: ICTCLD401 KE 5/6 (load balancing; vertical vs horizontal) — the primer under PC 3.1.
- [BESPOKE] The Application Load Balancer
  - An ALB receives requests on a listener (here HTTPS:443).
  - It forwards them to a target group and routes only to healthy targets (health checks).
  - It can be internet-facing or internal (this design is internal — staff over the VPN).
  kicker: AWS · ACA M07 / M10
  image: diagram alb-target-instances
  notes:
    Visual teach (diagram) — the ALB's job, using the target-group picture. Keep it to the three moving
    parts.
    • An ALB receives requests on a LISTENER (here HTTPS:443) — the front door and the port it answers on.
    • It forwards to a TARGET GROUP and routes only to HEALTHY targets — health checks are what make it
    safe; a sick instance is taken out of rotation automatically.
    • The accent line: internet-facing vs internal — THIS design is INTERNAL (staff reach it over the
    VPN), matching the private, no-public-IP app server.
    Misconception to pre-empt: "the load balancer runs the app." No — it DISTRIBUTES requests to the EC2
    instances that run the app; it holds no application logic itself (callback to Topic 1).
    Question to pose: "Why is this ALB internal, not internet-facing?" (the app is private, staff-only
    over the VPN — the whole tier stays off the public internet).
    UoC/AT2 tie: ICTCLD401 PC 3.1 (the balancer the ASG scales behind); §4.6 Load balancing evidence.
- [BESPOKE] Auto Scaling groups
  - An Auto Scaling group (ASG) manages a fleet of instances from a launch template.
  - Capacity settings: minimum / desired / maximum; it replaces unhealthy instances automatically.
  - Scaling policies — scheduled, dynamic (target-tracking), or step — adjust capacity.
  - It integrates with the ALB's health checks across Availability Zones.
  kicker: AWS · ACA M10 S20–S24
  image: reuse 08-asg-horizontal-scaling.png
  notes:
    Visual teach (diagram) — the ASG, the piece that actually does the elasticity. Pair with the
    horizontal-scaling image.
    • An ASG manages a FLEET of instances from a launch template — one definition, many copies.
    • Capacity settings: minimum / desired / maximum; it replaces unhealthy instances automatically
    (self-healing, not just scaling — flag both jobs).
    • Scaling POLICIES — scheduled, dynamic (target-tracking), or step — adjust capacity; ours is
    target-tracking (next slide).
    • The accent line: it integrates with the ALB's health checks ACROSS Availability Zones — the AZ
    hook that becomes HA in AT3.
    Misconception to pre-empt: "min/desired/max are the same thing / just a size." No — min and max are
    the guard-rails, desired is where it sits now; the policy moves desired between them.
    Question to pose: "If an instance dies at 2am, what does the ASG do without anyone paged?" (replaces
    it to hold desired capacity — self-healing).
    UoC/AT2 tie: ICTCLD401 PC 3.1 (configure autoscaling to business metrics); sets up the PC 3.2 test.
- [BESPOKE] The elasticity you'll build
  - Internal ALB, HTTPS:443 listener → a target group of the Ledgerline instances.
  - Auto Scaling Group: min 1 / desired 1 / max 2; target-tracking on CPU at 70%; 300 s cooldown.
  - Health checks: ELB + EC2 — an unhealthy instance is replaced.
  - This is baseline elasticity, single-AZ — cross-AZ resilience (HA) comes in AT3.
  kicker: the supplied design
  image: none
  notes:
    Pivot to THIS design's elasticity spec — read it so the demo and activity are unambiguous. Note the
    depth ceiling explicitly.
    • Internal ALB, HTTPS:443 listener → a target group of the Ledgerline instances.
    • ASG: min 1 / desired 1 / max 2; target-tracking on CPU at 70%; 300 s cooldown. Explain 70% = the
    trigger, cooldown = the wait before scaling again so it doesn't thrash.
    • Health checks: ELB + EC2 — an unhealthy instance is replaced.
    • The accent line (the ceiling): this is BASELINE elasticity, single-AZ — cross-AZ resilience (HA)
    is AT3. Don't let a keen student build Multi-AZ now; it's out of scope for this Topic.
    Misconception to pre-empt: "min 1 / max 2 is barely scaling." Correct — it's an elasticity INTRO,
    not HA. The point is proving the mechanism works, not surviving an AZ outage (that's AT3).
    Question to pose: "Why cap max at 2 and stay single-AZ here?" (this Topic teaches the mechanism; HA
    is deliberately deferred).
    UoC/AT2 tie: ICTCLD401 PC 3.1; §4.6 evidence; the single-AZ boundary keeps AT3 distinct.
- [DEMO] Create an Auto Scaling policy
  - Create a launch template and an Auto Scaling group with min / desired / max.
  - Attach a target-tracking scaling policy (e.g. keep average CPU near a target).
  - Watch the group launch and register instances with the load balancer.
  source: ACA M10 · Scaling policies (S26)
  image: none
  notes:
    DEMONSTRATION slide (recorded demo). Screen it, then map to our design — teach -> DEMONSTRATE ->
    practice. This one leads straight into the scaling TEST (PC 3.2), so foreground the test.
    
    WHERE TO FIND THE RECORDED DEMO: AWS Academy Cloud Architecting → Module 10 (ELB / Auto Scaling) →
    slide 26, "Demo: Creating Scaling Policies for EC2 Auto Scaling", inside the ACA M10 instructor deck
    (original-materials/AWS-Instructor Presentations/…). Instructor-facing — screen it, don't distribute.
    Preview it and cue it to this slide before class.
    
    WHAT TO DEMONSTRATE (follow the recorded demo, then map to our build):
    1. Create a launch template and an Auto Scaling group with min / desired / max.
    2. Attach a target-tracking scaling policy (keep average CPU near a target).
    3. Watch the group launch and REGISTER instances with the load balancer.
    
    WHAT TO EMPHASISE:
    • Ours: min 1 / desired 1 / max 2, target-tracking CPU 70%, 300 s cooldown — point to each field.
    • The ALB target group + health checks — show instances registering and the health state flipping
    healthy; that's what "behind the ALB" means concretely.
    • Foreshadow the TEST: driving CPU (or changing desired) makes it scale OUT then IN — students must
    OBSERVE and EVIDENCE this, not just build it (PC 3.2).
    
    PREP: Learner Lab open with the C1 instance already built (the ASG needs something to scale), the
    supplied design handy, demo queued. ~8-10 min to screen + narrate before the activity.
- [EX] Behind the ALB + ASG — then test scaling
  - In the lab, per the design:
    - create the internal ALB + target group + HTTPS:443 listener
    - create the launch template + ASG (min 1 / max 2, target-tracking CPU 70%)
  - Test scaling: drive the metric (or change desired capacity), watch it scale out then in; fix any errors.
  - Capture evidence — the ALB, target health, the ASG, and the scaling event.
  timer: ~25 min
  image: none
  notes:
    Facilitation — the C2 build AND the mandatory scaling test. The test is PC evidence, not optional;
    make that unmissable.
    Tell students, in these words: "Per the supplied design, put the Ledgerline instance behind an
    internal ALB in an Auto Scaling group — then TEST that it actually scales, and evidence the event."
    Steps (put on the board):
    1. Create the internal ALB + target group + HTTPS:443 listener.
    2. Create the launch template + ASG (min 1 / max 2, target-tracking CPU 70%).
    3. TEST scaling: drive the metric (or change desired capacity), watch it scale OUT then IN; fix any
    errors you hit.
    4. Capture evidence — the ALB, target health, the ASG, and the scaling EVENT.
    Must produce: a working ALB+ASG matching the design AND named evidence of a scaling event (before/
    after capacity, the activity history), plus any errors fixed.
    Timing: ~25 min. Where they get stuck: forgetting the test (they build and stop — push them to
    trigger a scale event); target group showing unhealthy (usually the SG/port or health-check path);
    confusing "desired" with a policy. Circulate on the test above all.
    Share-back prompt: "Show me the moment it scaled — what triggered it and what did the ASG do?"
    No-leakage note: Ledgerline is PRACTICE; AT2 assesses the same scaling build + test on the LMS —
    comparable, not identical. PC 3.2 is tested here so it's rehearsed, not first-seen in assessment.
- [TAKEAWAYS] Section 2 · Elasticity
  - A load balancer spreads traffic and routes only to healthy targets.
  - An Auto Scaling group scales horizontally between min and max on a policy.
  - Test that it scales and self-heals — that's PC evidence, not an optional extra.
  - Baseline here is single-AZ; cross-AZ high availability is AT3.
  image: none
- [TAKEAWAYS] Topic 8a · Key takeaways
  - EC2 is a virtual machine launched from an AMI; the instance type sizes it.
  - EBS gives the instance durable block storage.
  - An Application Load Balancer spreads load and health-checks the targets.
  - An Auto Scaling group scales horizontally to a policy and replaces failures.
  - Build to the supplied design, test the scaling, and evidence everything.
  image: none

### Close
- [BESPOKE] Next: Topic 8b — the data tier
  - The managed database (Amazon RDS) and object / archive storage (Amazon S3 + Glacier) — the data the application relies on.
  - Bring your evidence log.
  image: none
