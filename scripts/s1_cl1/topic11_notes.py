"""Teacher speaker notes for Topic 11 — HA concepts (S1-CL1).

One entry per teaching/activity slide. Keys are the EXACT slide title strings from
build_s1_cl1_topic11_deck.py so they match at build time. Read only by the teacher
(Presenter View), never shown to students.
"""

NOTES = {

    "Making the baseline highly available": """
        Frame this as the map for the whole AT3 arc — set expectations, don't teach HA content yet.
        • Where this fits: AT2 built a working SINGLE-AZ baseline. AT3's job is to make it highly
          available — resilient to losing an Availability Zone. This Topic is the vocabulary.
        • Walk the four-Topic arc off the accent-bold line: T11 = concepts (today), T12 = you DESIGN
          the upgrade, T13 = you implement + simulate the failure, T14 = you close out. Say it plainly
          so the keen student knows nothing gets built today.
        • What today gives them: the words — availability, fault tolerance, SPOFs, recovery objectives —
          plus the cloud toolkit that removes each weakness. Everything downstream reuses this.
        • How they practise: on the single-AZ Accounting baseline (Ledgerline) — the same client system
          they've carried all term; today they learn to REASON about its availability.
        Misconception to pre-empt: "we're on the cloud, so we're already highly available." No — a
        single-AZ cloud design has a SPOF just like on-prem; HA is DESIGNED, not automatic.
        Question to pose: "The baseline works — so what's actually wrong with it that AT3 has to fix?"
        (it can't survive losing its one AZ / one database — draws out the whole point of AT3).
        UoC/AT3 tie: Topic 11 develops the ICTCLD502 concepts examined through AT3 Part A (design) and
        Part B (implement/simulate); today itself is teach + light activity, not graded.
    """,

    "What is high availability?": """
        The anchor definition of Section 1 — teach it deliberately; students must be able to reason with
        the % ↔ downtime mapping in the AT3 design.
        • Read the bolded definition: HA = a system stays operational and accessible with MINIMAL
          downtime, even when parts fail. Stress "even when parts fail" — HA assumes failure happens.
        • Make the numbers concrete: availability is a percentage that maps to real downtime — 99% ≈ 7
          hours/month offline; 99.999% ("five nines") ≈ 26 seconds/month. Let that gap land.
        • Third bullet (accent): more nines cost a LOT more — often 2-5× — and aren't always achievable.
          This is the hinge for the "YAT's target" slide: you buy only the availability you need.
        Misconception to pre-empt: "highly available means never goes down." No — it means minimal,
        tolerable downtime; even five-nines is ~26 seconds a month, not zero.
        Question to pose: "If 99% sounds great, why might 7 hours offline a month be unacceptable for a
        payroll run — and what does closing that gap cost?" (surfaces the cost-of-nines trade-off).
        UoC/AT3 tie: ICTCLD502 PC 1.1 (reliability/recoverability/service levels) and KE 4/7/8; this
        vocabulary is what AT3 Part A uses to STATE the HA requirement.
    """,

    "Reliability & service levels": """
        Draw the reliability-vs-availability distinction cleanly — students routinely collapse the two,
        and AT3 asks them to state service levels precisely.
        • Reliability = how CONSISTENTLY a service works CORRECTLY; availability only says it's online.
          A service can be up (available) yet returning errors (unreliable) — different properties.
        • A service level is a measurable performance TARGET — availability %, response time. Name it as
          the number you promise.
        • Third bullet (accent): a Service Level Agreement (SLA) sets the MINIMUM service level; miss it
          and credits/penalties apply. The SLA is the contract that makes the target real.
        Misconception to pre-empt: "available and reliable are the same thing." No — online ≠ working
        correctly; you can be highly available and still unreliable if it errors while up.
        Question to pose: "If Ledgerline is up but the report screen throws errors half the time, is that
        an availability problem or a reliability problem?" (reliability — sharpens the distinction).
        UoC/AT3 tie: ICTCLD502 PC 1.1 / KE; stating reliability, recoverability and service levels is
        exactly what AT3 Part A's "identify HA requirements" step evidences.
    """,

    "YAT's availability target": """
        Apply the concept to the actual client — this is where "how many nines?" becomes a real design
        decision, not trivia.
        • Walk the requirement: Ledgerline needs ≥ 99.5% availability in BUSINESS HOURS (Mon-Fri
          ~07:30-18:00) — there is NO 24/7 requirement. The workload shape sets the target.
        • The accent line is the design goal: survive the loss of an Availability Zone — NOT chase
          99.999%. HA here means AZ resilience, sized to the business.
        • Third bullet: five-nines would MULTIPLY the cost (callback to the 2-5× line) for resilience a
          business-hours workload simply doesn't need. Right-sizing availability is the consultant skill.
        Misconception to pre-empt: "more availability is always better, so aim for five-nines." No — you
        buy the availability the business needs; over-buying wastes money on downtime nobody would notice.
        Question to pose: "Ledgerline is idle overnight and on weekends — how does that change what
        availability target is worth paying for?" (business-hours target, AZ resilience, not 24/7 five-nines).
        UoC/AT3 tie: ICTCLD502 PC 1.1/1.2 (reliability/service levels + infrastructure to business needs);
        this target is the requirement AT3 Part A designs against.
    """,

    "Match the target to the business": """
        Facilitation — a short paired discussion, the Section 1 practice. Light and verbal; no writing
        needed. Circulate and listen for the cost-of-nines reasoning.
        Tell students: "You're the MTS consultant advising YAT. Talk to the person next to you and be
        ready to justify the availability target for THIS client — not a textbook answer."
        Prompts (put on the board):
        1. Why does 99.5% business-hours fit Ledgerline — and what downtime does that actually allow?
        2. When would chasing five-nines be the WRONG call for a client like YAT, and why?
        Must produce: a spoken justification each pair can defend — a target tied to YAT's business hours
        plus the cost trade-off (not "more nines is better").
        Timing: ~5 min then share. Where they get stuck: they reach for the highest number by reflex —
        redirect them to what the BUSINESS needs (business hours only) and what extra nines cost.
        Share-back prompt: take one pair who defended 99.5% and one who over-shot, and let the room weigh
        which is the more client-specific call.
        No-leakage note: this is practice reasoning on Ledgerline; AT3 assesses the same skill on the LMS
        system — comparable, not identical. Keep them anchored to the Accounting baseline here.
    """,

    "What is a single point of failure?": """
        Open Section 2 with the SPOF primer — the single idea the whole availability argument turns on.
        Teach it plainly before applying it to the baseline.
        • Definition: a single point of failure (SPOF) is any component whose failure stops the WHOLE
          service. One weak link and everything downstream is down.
        • Use the everyday analogy: a car's engine — one failure and nothing moves, however good the rest
          of the car is. That's a SPOF.
        • Third bullet (accent) makes it IT-concrete: many app servers all on ONE database; a whole office
          on ONE internet link; one server; one Availability Zone. Each is a single failure that stops it all.
        Misconception to pre-empt: "if I have several servers I have no SPOF." Not necessarily — several
        app servers sharing ONE database still have a SPOF; redundancy at one tier doesn't remove it at another.
        Question to pose: "Point at the single-AZ baseline — which one failure takes ALL of Ledgerline
        down?" (the single AZ, or the single database — previews the activity).
        UoC/AT3 tie: ICTCLD502 PC 2.2 (identify single points of failure — concept here, applied to the
        baseline in Topic 12) and KE 4/7/8.
    """,

    "Recovery objectives — RTO & RPO": """
        Teach the two recovery objectives precisely — students swap them constantly, and AT3 asks them to
        ESTIMATE both. Slow down and make each stick.
        • RTO (Recovery Time Objective) = the maximum DOWNTIME the business will tolerate — how long to get
          back up. Think TIME.
        • RPO (Recovery Point Objective) = the maximum DATA LOSS the business will tolerate — how far back
          your last good copy is. Think DATA.
        • Work the accent example live: backups every 15 min → RPO 15 min; recover three layers at 30 min
          each + 1 h testing → RTO 2.5 h. Doing the arithmetic out loud is what makes it concrete.
        • Last bullet: why not set both to zero? COST — zero loss / zero downtime is extremely expensive;
          you set objectives the business can afford (echoes the cost-of-nines theme).
        Misconception to pre-empt: RTO and RPO are the same, or "RPO is about time." No — RPO is measured
        in data (how much you'd lose); RTO is measured in time (how long you're down). Anchor: Point vs Time.
        Question to pose: "If YAT backs up nightly, how much accounting data could a mid-afternoon crash
        lose — and is that RPO or RTO?" (up to a day's data → RPO; forces the distinction).
        UoC/AT3 tie: ICTCLD502 PC 2.3 (estimate recovery objectives) — concept here; students estimate the
        baseline's RPO/RTO in Topic 12.
    """,

    "Vertical scaling and its availability cost": """
        Teach why the SCALING choice is an availability decision — the non-obvious point of this slide is
        that scaling up carries a downtime cost.
        • Define both plainly: vertical scaling = a BIGGER server (more CPU/RAM); horizontal scaling = MORE
          servers. Same workload, two directions.
        • Accent line — the teaching point: vertical scaling usually needs a shutdown/restart and hits a
          hardware CEILING, so it's an availability COST. You take the service down to grow it, and one day
          you can't grow it further.
        • Last bullet: horizontal scaling is PREFERRED for availability (add servers with no outage);
          mitigate an unavoidable vertical change via an overnight window, a standby switch, or hot-swap.
        Misconception to pre-empt: "scaling up is the easy, safe option." For availability it isn't —
        vertical scaling means downtime and a ceiling; horizontal adds capacity without an outage.
        Question to pose: "The Ledgerline database needs more grunt — resize the one box, or add servers?
        Which costs you availability, and how would you soften it?" (vertical = downtime; use a window/standby).
        UoC/AT3 tie: ICTCLD502 PC 2.4 (determine components that must scale vertically and the impact on
        availability) — concept here; applied to the baseline in Topic 12.
    """,

    "Spot the SPOFs in the baseline": """
        Facilitation — the Section 2 practice, and it directly feeds Topic 12's design. Students work on
        the single-AZ Accounting baseline they'd be hardening. Have the baseline design open.
        Tell students: "Here's the single-AZ Accounting baseline you'll be making highly available. As the
        MTS consultant, find its weak points — where would ONE failure take the whole thing down?"
        Steps (put on the board):
        1. List its single points of failure — think through each tier: the AZ, the database, the running
           instance, the egress/NAT path.
        2. Estimate the baseline's recovery objectives (RPO / RTO) and note where they fall short of the
           99.5% business-hours target.
        Must produce: a written SPOF list plus a rough RPO/RTO estimate — KEEP it; Topic 12 designs these out.
        Timing: ~10 min then share. Where they get stuck: they stop at "the server" — prompt them tier by
        tier (network, compute, database, egress) so they find the single AZ and single RDS as the big ones.
        Share-back prompt: build a combined SPOF list on the board; flag which single failure is the most
        damaging (the AZ — it takes every tier at once).
        No-leakage note: this is practice on the Ledgerline/Accounting baseline; AT3 assesses the same SPOF
        analysis on the LMS system — comparable, not identical. Don't let them work the assessed system here.
    """,

    "Built-in vs designed fault tolerance": """
        Open Section 3 with the myth-buster — the mindset the whole HA toolkit rests on. Short slide, high
        leverage; give it weight.
        • First bullet, say it flatly: using the cloud does NOT make you highly available by itself.
        • Accent line — the real principle: YOU design redundancy — across compute, storage and network —
          so no single failure takes the service down. HA is an act of design, not a property of the platform.
        • Third bullet closes the loop back to Section 2: a single-AZ cloud design has a SPOF just like an
          on-prem one. The baseline is the proof.
        Misconception to pre-empt: "it's on AWS, so it's automatically resilient." No — the cloud gives you
        the TOOLS for redundancy; whether you're highly available depends on how you design with them.
        Question to pose: "The baseline runs entirely on AWS — so why isn't it already highly available?"
        (it's single-AZ; no redundancy was designed in — the platform doesn't add it for you).
        UoC/AT3 tie: underpins ICTCLD502 element 3 (design for HA); frames the toolkit slide next as the
        redundancy you deliberately design in.
    """,

    "The cloud HA toolkit": """
        The workhorse slide of Section 3 — name the four mechanisms AT3 designs with. Recognition + role
        for each; the design work is Topic 12, so don't over-drill here.
        • Multi-AZ — run resources ACROSS Availability Zones so losing one AZ doesn't stop the service.
          This is the headline move against the baseline's biggest SPOF.
        • Load balancing — spread traffic across servers AND route only to HEALTHY ones (health checks are
          half the value, not just distribution).
        • Auto Scaling across AZs — keep healthy CAPACITY in each AZ; frame it as availability, not just
          handling load — if an AZ's instances die, the ASG replaces them elsewhere.
        • Accent line — managed Multi-AZ databases: a SYNCHRONOUS standby with AUTOMATIC failover. And state
          the ceiling out loud: Multi-Region / full DR is OUT of scope (that's CL2). CL1 HA = cross-AZ.
        Misconception to pre-empt: "load balancing and autoscaling are just for handling busy periods." Not
        only — across AZs they're availability mechanisms: they route around and replace failed capacity.
        Question to pose: "Match one to the baseline's single-AZ SPOF — which tool removes it?" (Multi-AZ /
        a second AZ — previews the match activity).
        UoC/AT3 tie: ICTCLD502 KE 4/7/8 and element 3 underpinning; this is the toolkit AT3 Part A designs with.
    """,

    "Multi-AZ in action": """
        Visual slide — walk the Multi-AZ database diagram; it's the mechanism students find most abstract,
        so narrate the failover story rather than reading bullets.
        • Trace the picture: a PRIMARY database in one AZ, a SYNCHRONOUS standby in ANOTHER AZ — every write
          is copied to the standby in real time, so the standby is always current.
        • Second bullet is the payoff: if the primary (or its whole AZ) fails, the standby is PROMOTED
          automatically — service continues with SECONDS of downtime, not hours. Automatic is the key word.
        • Accent line, the detail students miss: the application reaches the database BY NAME (an endpoint),
          so failover needs NO app reconfiguration — the name now points at the promoted standby.
        Misconception to pre-empt: "the standby serves reads / shares the load." No — a Multi-AZ standby is
        for AVAILABILITY, not scaling; it sits idle until failover. (Read replicas are a different thing.)
        Question to pose: "The primary AZ dies mid-invoice-run — what does the app have to change to keep
        working?" (nothing — it connects by name; the endpoint follows the promoted standby).
        UoC/AT3 tie: ICTCLD502 KE 4/7/8; the Multi-AZ database is the mechanism that removes the baseline's
        single-database SPOF in the AT3 design.
    """,

    "Match the mechanism to the SPOF": """
        Facilitation — the Section 3 practice, and the shape of the Topic 12 design in miniature. Students
        pair each baseline SPOF from the earlier activity with its cloud fix. Have their SPOF list to hand.
        Tell students: "For each single point of failure you found in the baseline, name the ONE cloud
        mechanism that removes it. This is exactly the design you'll produce in full in Topic 12."
        Steps (put up):
        1. Work the four: single AZ → ?  ·  single database → ?  ·  single running instance → ?  ·  single
           NAT gateway → ?
        2. For each, say WHY that mechanism removes the SPOF (not just the label).
        Answers to reveal: a second AZ · a Multi-AZ database · an ASG across AZs · a NAT gateway per AZ.
        Must produce: four matched SPOF→mechanism pairs, each with a one-line why.
        Timing: ~10 min then reveal. Where they get stuck: the NAT gateway (they forget egress is a SPOF
        too) and conflating "ASG for load" with "ASG for availability" — clarify it's per-AZ healthy capacity.
        Share-back prompt: read a SPOF, take the mechanism from the room, confirm the reasoning — then note
        that stitched together, these four ARE the HA design they build in Topic 12.
        No-leakage note: practice on the Accounting baseline; AT3 assesses this design skill on the LMS
        system — comparable, not identical. Keep them on Ledgerline here.
    """,

}
