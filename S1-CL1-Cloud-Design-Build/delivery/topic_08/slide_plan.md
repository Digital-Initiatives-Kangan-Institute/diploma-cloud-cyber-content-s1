# Topic 08 The application tier — Slide plan
> **Covers:** Topic 08 — see coverage.md
> **STATUS: DRAFT — redrafted 2026-08-28 from the AT2 practice run sheet. Supersedes
> `slide_plan_08a.md` + `slide_plan_08b.md` (the a/b split is no longer needed — the data tier has
> moved to Topic 9). Teacher `notes:` not yet authored. `coverage.md` not yet reconciled.**

## Depth ceiling
Define a server once, front it with a load balancer, and let a scaling group manage how many there
are. Single-zone capacity — spreading across zones is AT3.

## Teaching source
AWS-sourced for compute, block storage, load balancing and scaling (ACF M06, ACA M05, ACA M10).
Bespoke for the template-not-a-server framing and the justification method.

## AWS pin table
ACF M06 S10–S26, S35 (recorded demo); ACA M10 S19–S26 (scaling policies demo at S26).

## Slides

### Opener
- [BESPOKE] Something to run
  - The network is built and the rules are written. Today the workload moves in.
  - Three moves: define what a server is, put something in front of it, and hand over how many there are.
  - You will also make the first of the run sheet's two real decisions — and have to defend it.
  kicker: the workload moves in
  image: none

### C1 — Defining a server, once
- Teaches: [ICTCLD401 PC 2.3] · [ICTCLD401 PC 2.4] · [ICTCLD401 PC 1.1] · [ICTCLD401 PC 1.3] · [ICTCLD401 KE 5] · [ICTCLD401 KE 6]
- Kicker: a definition, not a machine
- [PRIMER] What a server is
  - A server is a computer that runs your application for other people to use.
  - Its size is four things at once: processing, memory, disk, and network throughput.
  - A virtual machine is a software-defined server — you rent one and size it to the workload rather than buying a box.
  kicker: four dimensions
  image: none
- [BESPOKE] Launching a server — the choices
  - Machine image — the template the server starts from: an operating system, and anything pre-installed on it.
  - Instance type — the named size that sets processing, memory and network together.
  - Storage — the disk attached to the server: durable block storage that survives a stop and start.
  - Role, security group, first-boot script — permission, firewall, and what it configures itself with when it starts.
  kicker: image · size · disk · permission
  image: none
- [BESPOKE] Two kinds of storage, and which one this is
  - Disk storage — a volume attached to one server, which the operating system treats as a drive. It is what an operating system boots from and what a database writes to.
  - Object storage — whole files kept by name and fetched over the network. Effectively unlimited, cheaper at scale, and able to age old files off to a cheap archive tier.
  - Nothing mounts object storage like a drive, and nothing runs an operating system from it.
  - You are attaching disk storage here, in two places — the server's own volumes, and later the storage behind the database. Both are disks.
  - Object storage would be the right answer for something else: uploads, attachments, backups kept off the machine that made them.
  kicker: a drive, or a file store
  image: none
- [BESPOKE] Configuring at boot, not by hand
  - A first-boot script runs once, the first time a server starts, and installs and configures what it needs.
  - It means every server comes up identical, whether the platform builds one or ten.
  - The alternative — logging in and setting each one up — cannot survive a platform that creates servers on its own.
  kicker: identical every time
  image: none
- [BESPOKE] Why you build a template and not a server
  - You are not launching a server today. You are writing the definition one is built from.
  - Something else will create the servers from it, on demand, without anyone touching the console.
  - So the template carries no subnet — whatever creates the servers decides where they go.
  - Nothing gets configured on a running server by hand. If it did, the next server would not have it.
  kicker: the definition is the artefact
  image: none
- [BESPOKE] Making a choice you can defend
  - "I chose this one" is not a justification. Neither is "it is best practice".
  - A justification has four parts:
    - state what you chose · the facts about this workload that bear on it · weigh the trade-off · name the option you rejected and why
  - The rejected option is what most people leave out, and it is what proves the choice was a judgement rather than a default.
  - Both of the run sheet's decisions ask for it explicitly. This is the first one.
  kicker: name what you rejected
  image: none
- [EX] Create the launch template
  - Run sheet — task 10.
  - Build the template to the settings your run sheet gives, including the role you noted last topic and the first-boot script exactly as written.
  - Then make the sizing decision: choose, name the option you did not choose, and justify it against what this workload actually has to do.
  timer: ~30 min
  image: none
  notes:
    Activity = practice run sheet task 10, including its decision box. Two reliable stumbles: the
    security group left unset (the servers come up unreachable much later), and the first-boot script
    pasted without its first line. Push the justification past "it's cheaper" to the workload facts.
- [TAKEAWAYS] Section 1 · The server definition
  - A server is sized in four dimensions; the instance type sets them together.
  - A first-boot script makes every server identical.
  - You wrote a definition, not a machine — nothing is configured by hand.
  - A defensible choice names the option you rejected.
  image: none

### C2 — Putting something in front
- Teaches: [ICTCLD401 PC 2.2] · [ICTCLD502 PC 4.1] · [ICTCLD401 KE 5]
- Kicker: one address, many servers
- [BESPOKE] What a load balancer does
  - It takes traffic on one address and spreads it across however many servers are running.
  - It health-checks each one and sends traffic only to those passing.
  - So servers can come and go without anyone re-pointing anything.
  kicker: the front door
  image: diagram alb-target-instances
- [BESPOKE] Listeners and target groups
  - A listener is the port the balancer answers on, and what it forwards to.
  - A target group is the list of servers it forwards to, plus the health check that decides which of them are fit to receive traffic.
  - You create the target group empty. You do not register servers by hand — whatever creates them will register them for you.
  kicker: answer here, forward there
  image: none
- [BESPOKE] Internet-facing or internal
  - A balancer is either reachable from the internet or only from inside the network.
  - Which one is a design decision about who the users are and how they arrive.
  - Your run sheet states which. Build that.
  kicker: who is meant to reach it
  image: none
- [BESPOKE] Why it needs two zones
  - A load balancer will not create unless you give it subnets in two availability zones.
  - This is the requirement that put the extra subnets in your network back in Topic 6.
  - It does not mean your workload is spread across two zones. It means the balancer is.
  - Hold that distinction. It is exactly the trap the availability work opens with.
  kicker: the balancer spans; the workload may not
  image: none
- [EX] Create the target group and the load balancer
  - Run sheet — tasks 11 and 12.
  - Create the target group, registering nothing. Then create the balancer across the subnets your run sheet names, with its listener forwarding to that target group.
  timer: ~20 min
  image: none
  notes:
    Activity = practice run sheet tasks 11–12. The console will add a default security group to the
    balancer — it has to be removed and replaced with the one they built. Nothing is healthy yet;
    there are no servers. Say so, or they will think it is broken.
- [TAKEAWAYS] Section 2 · The load balancer
  - One address in front, health-checked servers behind.
  - The listener answers; the target group receives.
  - It requires two zones — which is not the same as the workload having two.
  image: none

### C3 — Letting the platform manage capacity
- Teaches: [ICTCLD401 PC 3.1] · [ICTCLD401 PE 2] · [ICTCLD401 KE 5] · [ICTCLD401 KE 6]
- Kicker: how many, decided for you
- [BESPOKE] Scaling in two directions
  - Vertical — replace what you have with something bigger. There is a ceiling, and usually a restart.
  - Horizontal — add more of the same alongside what is already running. No outage, and no ceiling worth worrying about.
  - Horizontal is the cloud pattern, and it is the foundation everything in AT3 is built on.
  kicker: bigger, or more
  image: reuse 08-asg-horizontal-scaling.png
- [BESPOKE] The scaling group
  - It creates and removes servers from your launch template, and registers them with the target group.
  - Minimum, desired, maximum: minimum and maximum are the guard-rails, desired is where it sits now.
  - It replaces a server that fails its health check without anyone being paged. It is self-healing as much as it is scaling.
  kicker: it builds them, it replaces them
  image: none
- [BESPOKE] The policy that moves capacity
  - A target-tracking policy names a metric and a value to hold it near, and the group adds or removes servers to keep it there.
  - Set the guard-rails from what the workload needs; set the target value from what you want the servers doing.
  - Health-check type matters: checking with the load balancer means "is it serving?", not merely "is it running?".
  kicker: hold this number
  image: none
- [EX] Create the scaling group
  - Run sheet — task 13.
  - Create the group from your template, into the subnet your run sheet names, attached to your target group with load-balancer health checks on, then set the capacity numbers and the scaling policy.
  timer: ~20 min
  image: none
  notes:
    Activity = practice run sheet task 13. The load-balancer step defaults to "no load balancer" and is
    the single most-skipped page in the whole run sheet — call it out before they start.
    A server should appear within a couple of minutes; have them watch the Activity tab.
- [TAKEAWAYS] Section 3 · Capacity
  - Horizontal scaling adds servers without an outage; vertical replaces with a bigger one.
  - The group builds from the template, registers with the target group, and replaces failures.
  - A policy holds a metric near a value between the guard-rails.
  image: none

### Close
- [BESPOKE] Next — the data tier
  - The application tier is running and scaling. It has nowhere to keep anything.
  - Next: a managed database, and the alarms that tell you when any of this stops working.
  image: none

## Build notes
~19 slides. Three activities, mapping to practice run sheet tasks 10 · 11–12 · 13.
Supersedes `slide_plan_08a.md` and `slide_plan_08b.md` — those two files are now unused and should be
removed once this plan is accepted. `alb-target-instances` diagram and `08-asg-horizontal-scaling.png`
are already in `topic_08/`. `coverage.md` needs reconciling: this Topic no longer owns the data tier.

## Changelog
- 2026-08-28 — redrafted from the AT2 practice run sheet; a/b split collapsed, data tier moved to
  Topic 9, standalone server launch removed (the run sheet has no such task).
