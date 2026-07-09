"""Teacher speaker notes for Topic 07 — Network & security base (S1-CL1).

One entry per teaching/activity/demo slide. Keys are the EXACT slide title strings
from build_s1_cl1_topic07_deck.py so they match at build time. Read only by the
teacher (Presenter View), never shown to students.
"""

NOTES = {

    "Continuing the build": """
        Frame this as the bridge from Topic 6 — set the shape of the day, don't teach yet.
        • Callback: Topic 6 laid the foundation (account, identity, the shared-responsibility line).
          Today you build the network the workload will sit inside — Topic 8 fills it.
        • Read the three parts off the slide: virtual network (VPC + subnets), traffic control
          (security groups), name resolution (DNS). Everything today maps to one of those three.
        • Hammer the two disciplines that continue from Topic 6 (bolded lines): still building to a
          SUPPLIED design (they're the builder, not the designer), still capturing evidence as they go.
        • Set the rhythm for every AWS task today: watch the demo, then do it yourself.
        Misconception to pre-empt: "we're designing the network." No — the topology is given; their job
        is to build it faithfully and evidence it, exactly as in AT2.
        Question to pose: "Topic 6 gave the workload an identity — what's still missing before an app can
        run?" (a network for it to live in, and rules for who reaches it).
        UoC/AT2 tie: this Topic develops the network portion of AT2 criterion A2 (§4.2 of the Deployment
        Report); it's the network tier the Topic 8 workload moves into.
    """,

    "Networking, the essentials": """
        Primer — vendor-neutral fundamentals BEFORE any AWS. Don't assume a networking baseline; some
        students meet IP/CIDR for the first time here. Use the IP/CIDR image.
        • Network = machines connected to share resources; it can be split into smaller pieces (subnets).
        • IP address = a unique numeric label for a machine (e.g. 10.0.0.17) — like a street address.
        • CIDR (the bolded line, the hard bit): 10.0.0.0/16 describes a RANGE; the /number says how many
          bits are fixed. Small /number = big range; big /number = small range. Give the /16-vs-/28 feel
          rather than the binary maths — that's enough for building to a supplied design.
        • Routers/gateways move traffic between networks — sets up the VPC gateways two slides on.
        Misconception to pre-empt: "the /16 is 16 addresses." No — the slash counts FIXED bits, not
        addresses; /16 is a large block, /28 a tiny one.
        Question to pose: "Which is the bigger network — a /16 or a /24?" (/16 — fewer fixed bits, more room).
        UoC/AT2 tie: ICTCLD401 KE 5 (virtual networks) — the vocabulary the VPC build rests on.
        [Primer slide — reuses ACF M05 S5–S9; keep it brisk, it's foundation for the AWS slides.]
    """,

    "The VPC — your private network in AWS": """
        The AWS-context teach after the primer — this is the core C1 concept. Teach it deliberately.
        • A VPC is a logically isolated slice of AWS that YOU define — your own private virtual network.
        • It belongs to ONE Region and can span the AZs in it; you size it with a CIDR block (largest /16,
          smallest /28). Stress: you can't change the CIDR later — sizing is a decision, not a default.
        • The bolded line: you divide the VPC into subnets, each in one AZ, classified public or private.
          "Public/private" is about whether there's a path to the internet, not about secrecy — flag it now
          because it drives the next activity.
        Misconception to pre-empt: "a VPC lives in an AZ." No — a VPC is Region-scoped and spans AZs; a
        SUBNET lives in one AZ. This is the Topic 1 Region/AZ hierarchy made concrete.
        Question to pose: "Our design's VPC is 10.0.0.0/16 — why give it that much room when Ledgerline is
        small?" (headroom to add subnets/tiers later without rebuilding).
        UoC/AT2 tie: ICTCLD401 PC 2.2 (create a virtual multi-tier network) + KE 5 → AT2 §4.2. This is the
        VPC students build to the supplied design.
    """,

    "Routing: gateways & route tables": """
        Teach how traffic actually reaches (or doesn't reach) a subnet — the mechanism behind public vs
        private. Use the VPC-anatomy diagram; walk it, don't read.
        • Route table = rules that direct a subnet's traffic; every table has a built-in LOCAL route so
          anything inside the VPC can talk without extra config.
        • Public subnet = a 0.0.0.0/0 route to an Internet Gateway → direct internet path.
        • Private subnet = no such route → no direct internet path. "Public/private is decided by the ROUTE
          TABLE" is the sentence to land.
        • The bolded line — NAT gateway: lets private resources reach OUT (e.g. patching) WITHOUT being
          reachable from the internet. Outbound-only. This is exactly the design's egress-only model.
        Misconception to pre-empt: "a NAT gateway lets the internet into the private subnet." No — it's
        one-way OUT; nothing inbound. Students routinely invert this.
        Question to pose: "The database subnet must never be reachable from the internet but still needs OS
        patches — how?" (private subnet, no IGW route, patches via the NAT gateway).
        UoC/AT2 tie: ICTCLD401 PC 2.2 / KE 5 (traffic routing) → AT2 §4.2 (subnets + routing).
    """,

    "Public or private?": """
        Facilitation — a quick sorting task that forces the public/private decision they'll make for real
        in the lab. Whole-room or pairs, fast.
        Tell students: "For each resource, decide the subnet it belongs in — public or private — and be
        ready to say WHY in one line."
        The four (put up): the database · a batch-processing job · the web/app server · a NAT gateway.
        Expected landing: database → private; batch job → private; web/app server → private (behind a load
        balancer); NAT gateway → public. The rule of thumb (bolded): anything that shouldn't be reachable
        from the internet goes private; only internet-facing entry points and the NAT gateway go public.
        Must produce: four placements, each with a one-line reason tied to "is it reachable from the net?"
        Timing: ~10 min then share. Where they get stuck: they put the web/app server in a public subnet
        because "users reach it" — push them to AWS's pattern (app tier private, behind a public ALB); the
        LOAD BALANCER is the public entry point, not the server.
        Share-back prompt: "Who put the app server public — what changes if it sits behind an ALB instead?"
        No-leakage note: reasoning practice on the Accounting design; AT2 assesses the same call on the LMS.
    """,

    "The network you'll build": """
        Pivot from concept to the actual thing they build — the supplied design's network topology. Get
        them into the Solution Design on the intranet; this is the spec they build to.
        • The bolded line: open the Solution Design (§4.4) and study its network topology — you build to
          THAT, you don't invent it. Model reading a supplied design before touching the console.
        • Walk the specifics: VPC 10.0.0.0/16 (room to expand), DNS resolution + flow logs on; subnets in
          the first AZ — public-egress-a (NAT only), private-app-a (app + internal ALB), private-data-a
          (database).
        • Egress-only: the Internet Gateway is for outbound patching via NAT; NO inbound path from the
          internet. Staff reach the service over the campus Site-to-Site VPN; route tables set per tier.
        Misconception to pre-empt: "public-egress means the public can get in." No — it's the subnet that
        holds the NAT for OUTbound only; the name describes egress, not inbound access.
        Question to pose: "Where does a member of YAT staff actually connect from, if there's no inbound
        internet path?" (over the campus Site-to-Site VPN — a given in the design, not built here).
        UoC/AT2 tie: PC 2.2 → AT2 §4.2; this is the concrete topology their build + evidence must match.
    """,

    "What a firewall does": """
        Primer for C2 — what a firewall / stateful packet filter IS, before AWS security groups. Bespoke
        primer (ACA M07 S23 analogy); some students have never met the concept.
        • A firewall filters traffic by rule — it decides what's allowed through.
        • The bolded analogy: a security group is like an apartment door — it lets in only the right key,
          protecting ONE resource (not the whole building). Contrast with a building's front gate (that's
          more like a network ACL — out of scope here, don't go there).
        • Traffic is identified by address + PORT: 443 = HTTPS, 1433 = SQL Server, 3389 = RDP. Give them
          these three because the design's rules use exactly them.
        • Least privilege: open only the ports the job needs, only to who needs them — the whole ethic of
          the next two slides.
        Misconception to pre-empt: "a firewall blocks bad traffic." More precisely, it DENIES everything by
        default and you ALLOW what's needed — it's a whitelist, not a bad-traffic detector.
        Question to pose: "The database speaks SQL Server on 1433 — who should be allowed to reach that
        port?" (only the app tier — nobody else; sets up the chain).
        UoC/AT2 tie: ICTCLD401 KE 9 (limiting network traffic within virtual networks) → AT2 §4.2.
    """,

    "Security groups": """
        The AWS-context teach for C2 — the properties that make security groups behave the way they do.
        Teach the three behaviours precisely; students lose marks on these in AT2.
        • A security group is a virtual firewall attached to a resource (an instance or interface) — per
          resource, not per subnet.
        • STATEFUL: allow traffic in and the return traffic is automatically allowed out — you don't write
          a matching outbound rule. This is the one they forget.
        • ALLOW-rules only, no deny; a brand-new SG blocks ALL inbound until you add rules (deny-by-default).
        • The bolded line — the big idea for this design: you can name ANOTHER security group as the source.
          That's how tiers chain (allow 443 only FROM the load balancer's SG), instead of hard-coding IPs.
        Misconception to pre-empt: "you must open the return port too." No — stateful means the reply is
        automatic. Also "source must be an IP range" — no, it can be another SG.
        Question to pose: "If the app server's IP changes, does a rule that allows FROM sg-app break?" (No —
        SG-as-source follows the membership, not the address; that's why we chain by SG).
        UoC/AT2 tie: KE 9 → AT2 §4.2 (the sg-alb → sg-app → sg-db chain). The table next shows the design's SGs.
    """,

    "Build a VPC and its security groups": """
        DEMONSTRATE step for C1+C2 — this is a RECORDED AWS demo; screen it, then have them build (activity
        next). teach → DEMONSTRATE → practice.

        WHERE TO FIND THE RECORDED DEMO: AWS Academy Cloud Architecting → Module 07 (Creating a Networking
        Environment) → slide 30, "Demo: Creating an Amazon VPC in the Console" (VPC + security groups +
        Elastic IP), inside the ACA M07 instructor deck (original-materials/AWS-Instructor Presentations/…).
        Instructor-facing — screen it in class, DON'T distribute to students. Preview it and cue it to this slide.

        WHAT TO DEMONSTRATE (follow the recorded demo, then relate each step to OUR design):
        1. Create a public and a private subnet, each with its own route table.
        2. Create an Internet Gateway, attach it to the VPC, configure the internet route.
        3. Create a NAT gateway, assign an Elastic IP, add the private-subnet route.
        4. Create a web-server security group and a database security group.

        WHAT TO EMPHASISE:
        • Public vs private is decided by the ROUTE TABLE (IGW route or not) — point at it as it's built.
        • NAT gateway is OUTBOUND only — say it as you add the Elastic IP; ties back to the egress-only design.
        • SG-as-source when you build the DB SG — allow from the web SG, not an IP; the payoff of the SG teach.
        • Narrate evidence capture — Region visible in every shot; students must screenshot for AT2, model it.
        Note: the demo builds a generic VPC; OUR design is 10.0.0.0/16 with three named subnets — flag the deltas.
        PREP: clean lab open, Solution Design §4.4 handy (names/CIDRs), demo queued. ~10–12 min to screen + narrate.
    """,

    "Build the network fabric": """
        Facilitation — the main C1+C2 hands-on build in the lab, straight after the demo. This is the AT2
        network build rehearsed on the practice system.
        Tell students, in these words: "Open the AWS Academy lab and the supplied Accounting design. Build
        the network tier exactly as the design specifies, and capture named evidence as you go."
        The task, step by step (put on the board / read out):
        1. Create the VPC 10.0.0.0/16.
        2. Create the three subnets: public-egress, private-app, private-data (first AZ).
        3. Create the Internet Gateway + NAT gateway + per-tier route tables — egress-only (no inbound path).
        4. Build the security-group chain: sg-alb → sg-app → sg-db (source = the upstream SG, not an IP).
        Must produce (the AT2 evidence): named screenshots of the VPC, subnets, route tables, and SG rules —
        Region visible in each.
        Timing: ~25 min. Set Region to us-east-1 first — [scenario: ap-southeast-2 (Sydney) | deploy:
        us-east-1] — visible in all evidence. Where they get stuck: forgetting the NAT route on the private
        table (private subnet can't reach out), and writing IP sources instead of SG-as-source — circulate for both.
        Share-back: ask one student to show their sg-db inbound rule; confirm it allows FROM sg-app only.
        No-leakage note: this practice uses the Accounting design; the assessed build uses a different system
        (public-facing ALB) — comparable, not identical.
    """,

    "How DNS works — and Route 53": """
        Primer + teach for C3 — how DNS resolves a name, then AWS Route 53. Use the DNS-flow image; don't
        assume they know what DNS does.
        • DNS translates a NAME (ledgerline.yat.internal) into the IP address machines actually use.
        • A resolver walks the DNS hierarchy and returns the address — we use NAMES not IPs because addresses
          change; the name is stable, what it points to can move.
        • The bolded line: Amazon Route 53 is AWS's highly available DNS service.
        • The distinction that matters for this design: PUBLIC hosted zone = internet-facing names; PRIVATE
          hosted zone = names that resolve ONLY inside your VPC. Ledgerline uses a private zone (staff-only).
        Misconception to pre-empt: "DNS is the internet / a website." No — it's the phone book that turns
        names into addresses; nothing about content.
        Question to pose: "If Ledgerline's server is rebuilt and gets a new IP, why don't staff bookmarks
        break?" (they use the NAME; DNS re-points it — that's the whole value).
        UoC/AT2 tie: ICTCLD401 KE 10 (purpose of DNS) → AT2 §4 (the design's internal name via Route 53).
    """,

    "The design's name & certificate": """
        Apply DNS to the supplied design — the specific internal name + certificate students configure.
        Short, but it carries an implementer decision they must own.
        • Ledgerline gets an INTERNAL hostname in a PRIVATE hosted zone — staff-only, over the VPN; there is
          NO public internet name. Consistent with the egress-only, VPN-reached design.
        • An ACM TLS certificate secures HTTPS to that name — connect the cert to the name, not to an IP.
        • The bolded line: the exact hostname + certificate domain is implementer decision C8 — they CONFIRM
          it with YAT ICT, they don't guess it. Model treating an open design decision as a question to ask,
          not an assumption to make.
        Misconception to pre-empt: "internal name means no certificate needed." No — HTTPS/TLS still applies
        inside the VPN; internal ≠ unencrypted.
        Question to pose: "Why a private hosted zone here rather than a public one like a normal website?"
        (the service is staff-only over the VPN; no reason to publish the name to the internet).
        UoC/AT2 tie: KE 10 → AT2 §4 (DNS / name resolution). C8 is the kind of design decision AT2 expects
        them to surface and confirm.
    """,

    "Prove it works — test connectivity": """
        Teach the test-and-fix discipline — introduced here (PC 2.6), completed in Topic 8/9 once compute
        exists. This is the "evidence it works", not just "it's built" mindset.
        • After building, CONFIRM reachability: external access IN (reach the service over the VPN) and access
          BETWEEN tiers (app → db). Building isn't done until it's tested.
        • Reachability Analyzer traces the path and NAMES the blocking component when something can't connect
          — it turns "it doesn't work" into "this rule is blocking it".
        • The bolded line — VPC flow logs show ACCEPT / REJECT; a REJECT is usually a missing SG rule or a
          missing route. Teach the reflex: read the log, find the block, fix, retest, capture.
        • Be honest about scope: full app → db testing completes in Topic 8 once compute exists — here they
          test what exists so far.
        Misconception to pre-empt: "no error means it's correct." Absence of an error isn't proof — you have
        to actively test the paths the design requires and evidence the result.
        Question to pose: "Staff can't reach Ledgerline over the VPN — what two things do you check first?"
        (the SG inbound rule and the route table / flow-log REJECT).
        UoC/AT2 tie: ICTCLD401 PC 2.6 (test access + fix errors, introduced) + PE 3 → AT2 A2/A10.
    """,

    "Create a DNS record & test reachability": """
        DEMONSTRATE step for C3 — this is a LIVE instructor demo, not a recorded one. teach → DEMONSTRATE →
        practice.

        WHERE TO FIND THE RECORDED DEMO: none fits — the recorded Route 53 demos in the catalogue (ACA M10
        S52 Failover, S51 Simple Routing) are PUBLIC-routing demos and don't fit a PRIVATE hosted zone, so
        do this one LIVE in the console. (Per the demos catalogue, Topic 7's Route 53 need has no recorded
        private-zone demo — live is the intended fallback.)

        WHAT TO DEMONSTRATE (live, narrated):
        1. In Route 53, create / confirm the PRIVATE hosted zone for the internal domain.
        2. Add the record for the Ledgerline name (and note the ACM certificate).
        3. From a test point, resolve the name and check reachability.
        4. If it's blocked, read the flow logs / Reachability Analyzer and fix the SG or route — then retest.

        WHAT TO EMPHASISE:
        • PRIVATE zone — show it's associated with the VPC; the name resolves only inside, not on the internet.
        • Resolve the NAME, not the IP — prove DNS is doing its job.
        • Model the fix loop live: deliberately hit (or narrate) a REJECT, read it, fix the SG/route, retest —
          this is exactly the PC 2.6 discipline they're assessed on.
        • Narrate evidence capture — the DNS config and the test result both go in the log, Region visible.
        PREP: lab open with the Topic-7 network already built (or a prepared account), Solution Design C8
        handy for the hostname, Reachability Analyzer/flow logs ready to show. ~10 min live.
    """,

    "Configure DNS + test connectivity": """
        Facilitation — the closing C3 hands-on: finish the network tier with DNS, then test what exists.
        Straight after the live demo.
        Tell students, in these words: "In the lab, finish the network tier — create the internal DNS name,
        then test the paths you can test so far and fix anything that's blocked. Capture evidence throughout."
        The task, step by step (put on the board / read out):
        1. Create the PRIVATE hosted zone + the record for the internal hostname (note the ACM cert; confirm
           the exact name is the C8 decision).
        2. Run reachability tests for what exists so far (the network paths; full app → db waits for Topic 8).
        3. If a test is blocked, read the flow logs / Reachability Analyzer, fix the SG or route, and retest.
        Must produce (the AT2 evidence): the DNS config screenshot AND a test result — plus a note of any fix
        made (what was blocked, what you changed).
        Timing: ~15 min. Where they get stuck: expecting to test app → db when there's no compute yet — scope
        them to the paths that exist; and forgetting to associate the private zone with the VPC (name won't
        resolve).
        Share-back: ask a student who hit a REJECT to narrate their fix loop — the fix, not just the pass, is
        the assessable skill.
        No-leakage note: practice on the Accounting design (internal name); AT2 assesses the same skill on the
        LMS — comparable, not identical.
    """,

}
