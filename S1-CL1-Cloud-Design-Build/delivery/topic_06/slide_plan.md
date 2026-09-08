# Topic 06 Getting to work — the account and the network fabric — Slide plan
> **Covers:** Topic 06 — see coverage.md
> **STATUS: DRAFT — redrafted 2026-08-28 from the AT2 practice run sheet. Teacher `notes:` not yet
> authored (deliberate — they are written once the plan is agreed). `coverage.md` not yet reconciled,
> so `validate-slide-plan` backwards-coverage will fail until it is.**

## Depth ceiling
Stand up the account, the private network and its paths in and out, working to a run sheet that states
the settings. Single-zone workload placement; no availability work (that is AT3).

## Teaching source
Bespoke for the run-sheet working mode and the evidence discipline. AWS-sourced for the
requirements→design→build chain (ACA M02) and the networking fundamentals (ACF M05, ACA M07).

## AWS pin table
ACA M02 (architecture roles); ACF M05 S5–S9, S11; ACA M07 S10, S12–S16.

## Slides

### Opener
- [BESPOKE] Building what someone else designed
  - AT1 was advice on paper. From here you build, in the console, and evidence it.
  - Your run sheet tells you what to build and the settings to build it to. Finding your way around the console is your job.
  - Today: the account and its region, then the private network and the paths in and out of it.
  - Every block of teaching today ends with the next task on your run sheet.
  kicker: advice becomes a build
  image: none

### C1 — Working to a run sheet
- Teaches: [ICTCLD401 PC 1.4]
- Kicker: the implementer's seat
- [BESPOKE] Requirements → design → build
  - Cloud architecture turns requirements into a structure:
    - the customer sets the requirements · an architect produces the design · a delivery crew builds it
  - Three roles, a hand-off between each. From here you sit in the third one.
  kicker: three roles, one hand-off each
  image: reuse 06-aws-arch-reqs-design-build.png
- [BESPOKE] What a run sheet gives you, and what it doesn't
  - It gives you the task, the settings to build it to, and what your screenshot must show.
  - It does not give you the clicks. Working out where a setting lives is part of the job.
  - Build what it specifies. Where it asks you to choose, the choice — and your reasoning — is yours.
  - Work the tasks in order. Each one is built on the one before it.
  kicker: the settings are given; the route is not
  image: none
- [BESPOKE] Region is the first decision
  - Everything you create belongs to one region, so it is set before you create anything.
  - The driver is compliance, not preference — where the data is allowed to live.
  - Your run sheet names a production region and a build region. They differ, and only the location label changes; the build is identical.
  - Make the region visible in your evidence.
  kicker: set it before you create anything
  image: none
- [BESPOKE] Capture as you build
  - Take each screenshot as you finish that task, not at the end of the session.
  - Console state moves on. A screen you have navigated away from often cannot be recreated.
  - The bar for a screenshot is simple: clear enough for the assessor to read. If they cannot make out the setting you are claiming, it is not evidence.
  kicker: build → capture → move on
  image: none
- [EX] Set your region and confirm it
  - Run sheet — task 1.
  - Sign in, set the region your run sheet names for building, and capture the console with the region selector visible.
  timer: ~10 min
  image: none
  notes:
    Activity = practice run sheet task 1. They should finish with the region set and one capture.
    Circulate for the lab launch/console hand-off; check the region indicator on each screen.
- [TAKEAWAYS] Section 1 · Working to a run sheet
  - You are the builder. The settings are given; finding them is yours.
  - Region first — it is compliance, and everything is region-scoped.
  - Capture each task as you finish it.
  image: none

### C2 — The private network and its subnets
- Teaches: [ICTCLD401 PC 2.2] · [ICTCLD401 KE 5] · [ICTCLD401 KE 10] · [ICTCLD401 PE 1]
- Kicker: the fabric everything sits in
- [PRIMER] Networks, addresses and ranges
  - A network connects machines so they can reach each other; it can be divided into subnets.
  - Every machine has an IP address — a unique numeric label.
  - A CIDR block describes a range of addresses. The number after the slash says how many bits are fixed, so a smaller number means a bigger range.
  - Traffic moves between networks through routers and gateways.
  kicker: the vocabulary the build assumes
  image: reuse 07-ip-cidr.png
- [BESPOKE] Your own private network in the cloud
  - A virtual private network is a logically isolated slice of the provider's cloud that you define.
  - It belongs to one region and spans the availability zones inside it.
  - You size it with a CIDR block when you create it, and you cannot change that later — so it is given room to grow.
  kicker: region-scoped, spans zones
  image: none
- [BESPOKE] Names — the two settings you are about to turn on
  - DNS turns a name into an address. Machines connect to addresses; people and configuration use names.
  - Creating the network asks you to enable two things, and they are not the same:
    - DNS resolution — things inside the network can look names up at all
    - DNS hostnames — things inside the network get a name of their own, not just an address
  - You are not building a DNS service here. You are switching on the one the platform already runs.
  - It pays off at the end: the load balancer is given a name, and that name is what you open in a browser to prove the build works. Its addresses change over time; the name does not — which is the whole reason anything uses names.
  - Get this wrong and every server can be running perfectly and still be unreachable by name.
  kicker: two tick boxes, and why they matter later
  image: none
- [BESPOKE] Subnets
  - You divide the network into subnets. Each subnet lives in exactly one availability zone.
  - A subnet is public or private according to whether it has a route to the internet — not according to what it is called.
  - Set the zone yourself on every subnet. Left alone the console picks one for you, and a subnet in the wrong zone causes failures much later that never mention subnets.
  kicker: one zone each; public or private
  image: none
- [BESPOKE] Why there are more subnets than tiers
  - Your run sheet asks for more subnets than you have tiers to put in them.
  - Some managed services refuse to be created unless you hand them subnets in two zones — even when everything you are running sits in one.
  - So a couple of subnets exist to satisfy a service requirement, and stay empty.
  - Worth remembering. It becomes the starting point of the availability work later.
  kicker: a service requirement, not a tier
  image: none
- [EX] Create the network and its subnets
  - Run sheet — tasks 2 and 3.
  - Create the private network at the range your run sheet gives, then every subnet it lists, setting the zone on each one yourself.
  timer: ~20 min
  image: none
  notes:
    Activity = practice run sheet tasks 2–3. Circulate for the zone dropdown left on "No preference" —
    it is the failure that shows up three tasks later. Check the Availability Zone column on share-back.
- [TAKEAWAYS] Section 2 · The network
  - A virtual private network is yours, region-scoped, and sized once.
  - Subnets each sit in one zone; public or private is decided by routing.
  - Some subnets exist only because a service demands two zones.
  image: none

### C3 — Paths in and out
- Teaches: [ICTCLD401 PC 2.2] · [ICTCLD401 KE 5] · [ICTCLD401 PE 1]
- Kicker: what can reach what
- [BESPOKE] Two gateways, two jobs
  - An internet gateway gives a subnet a two-way path to the internet.
  - A NAT gateway lets private resources reach out — for updates and external calls — while nothing on the internet can reach in.
  - A NAT gateway is placed in a public subnet, and serves the private ones.
  kicker: one way in, one way out
  image: diagram vpc-anatomy
- [BESPOKE] Route tables decide what is public
  - A route table holds the rules that direct a subnet's traffic, and every table has a built-in local route so anything inside the network can talk.
  - Add a 0.0.0.0/0 route to an internet gateway and the subnet is public. Point it at a NAT gateway instead and the subnet reaches out but cannot be reached.
  - A subnet with no route table of its own falls back to the network's default, which has no path out at all.
  kicker: public or private is a routing decision
  image: none
- [BESPOKE] A tier that should have no way out
  - Your data subnets get no route table and no path to the internet. That is not an omission.
  - A database has no business making outbound connections, so it is given no means to.
  - Least privilege applies to routing, not just to permissions.
  kicker: deliberately unreachable
  image: none
- [EX] Build the gateways and the routing
  - Run sheet — tasks 4, 5 and 6.
  - Create and attach the internet gateway, create the NAT gateway, then build the route tables and associate them with the right subnets.
  timer: ~25 min
  image: none
  notes:
    Activity = practice run sheet tasks 4–6. The NAT gateway takes several minutes to become available
    and cannot be routed to before it does — warn them so they do not assume it has failed.
    Common miss: associating the subnets after adding the route.
- [TAKEAWAYS] Section 3 · Paths in and out
  - An internet gateway is two-way; a NAT gateway is outbound only.
  - The route table is what makes a subnet public or private.
  - The data tier is given no route out, deliberately.
  image: none

### Close
- [BESPOKE] Next — who may talk to what
  - The network exists. Nothing yet controls which tier may reach which.
  - Next: the firewall rules that chain the tiers, and the identities that operate the platform.
  image: none

## Build notes
~19 slides. Three activities, mapping to practice run sheet tasks 1 · 2–3 · 4–6.
Assets to move into `topic_06/`: `07-ip-cidr.png` (from `topic_07/images/`) and the `vpc-anatomy`
diagram (from `topic_07/diagrams/`). `06-iam-components.png` moves out to `topic_07/`;
`06-shared-responsibility.png` is no longer used here (the concept is now Topic 10 knowledge-question
material). `coverage.md` still declares the previous components and needs reconciling.

## Changelog
- 2026-08-28 — redrafted from the AT2 practice run sheet; sequence now follows tasks 1–6.
