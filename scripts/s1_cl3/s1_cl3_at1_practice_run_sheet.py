#!/usr/bin/env python3
"""The S1-CL3 AT1 PRACTICE design run sheet — content.

Same shape as the AT1 assessment workbook, different everything else. The system being
improved is the public website, not Ledgerline.

WHY THE WEBSITE IS A DIFFERENT IMPROVEMENT PROBLEM — and these are the reasons an answer
worked out here cannot be transposed onto the assessment, or the reverse:

  who reaches it     Ledgerline is internal: campus VPN only, no public ingress, and that is
                     the strongest thing about it. The website is open to the internet,
                     anonymous, and exposed to bots, scraping and form spam by design. The
                     security task is a different task.
  when it runs       Ledgerline is business hours and genuinely idle overnight, which makes
                     scheduled scale-down the biggest cost lever available. The website is
                     24x7 with an international audience — that lever does not exist here,
                     so the cost task has to find different ones.
  what is there      Ledgerline already has a load balancer and an Auto Scaling group; its
                     gap is that they only span one zone. The website has NEITHER — one EC2
                     instance IS the website, with HTTPS terminating on it. So the compute
                     design is not "spread what exists across two zones", it is "there is no
                     tier here yet".
  where files live   Ledgerline has block storage only. The website serves uploaded media
                     from the instance's own disk, which stops being viable the moment there
                     is more than one instance — a problem Ledgerline does not have.
  the peak           month-end close and end of financial year, versus the intake windows
                     IR-7 forbids changing during.

WHAT PRACTICE ADDS: every task is presented exactly as the assessment presents it, then adds
a "Things to consider" block — leading questions, pointed enough that a student paying
attention cannot miss the answer, and which never state it. Tables carry one worked exemplar
row showing the shape of an answer, never one of the answers asked for.

No marking criteria, no UoC tags. Rendered by the assessment's own renderer in
s1_cl3_at1_run_sheet, with these lists passed in.
"""

SITE = "https://yat.timbaird.com"
STATE = "s1-cl3-at1"
PROJECT = f"{SITE}/intranet/{STATE}/projects/website-improvement"
MIGRATION = f"{SITE}/intranet/{STATE}/projects/website-cloud-migration"
ICT = f"{SITE}/intranet/{STATE}/ict"
POLICY = f"{SITE}/intranet/{STATE}/policies"
REFERENCE = f"{SITE}/intranet/{STATE}/reference"

# ---------------------------------------------------------------- front matter

SCENARIO = [
    "YAT College's offshore partnership in India has put a spotlight on the systems that support "
    "it. The public website — the front door for every prospective student, in Australia and now "
    "in India — was migrated to AWS in 2023 as YAT's first cloud project, deliberately as a "
    "low-risk pilot. High availability and disaster recovery were explicitly out of scope at the "
    "time, and nothing has been revisited since.",
    "You are an MTS Consultant on this engagement, reporting to Pat Lin (MTS Senior Consultant). "
    "Sam Walker (YAT ICT Manager) is your primary stakeholder, with YAT Marketing & Admissions as "
    "the business owner of the site.",
    "This is practice. Nothing here is assessed and nothing is submitted. It is the same work the "
    "assessment will ask for, on a different system — so do it properly, because the moves are "
    "the point, not the answers.",
]

INSTRUCTIONS = [
    "Work the tasks in order — each builds on the answer before it. Each is presented the way the "
    "assessment presents it, and then adds a Things to consider block underneath.",
    "Those considerations are leading questions, not answers. If you work through them honestly "
    "you will arrive at the answer yourself — which is the only version of it that will still be "
    "there in the assessment.",
    "Where a table has a worked first row, that row shows the SHAPE of an answer. It is never one "
    "of the answers the task is asking you for. Yours go underneath it.",
    "There is no right answer waiting to be found. The Improvement Requirements are outcomes, not "
    "solutions, and IR-2 asks for improvements proportionate to the site's business value. "
    "Proposing every improvement available is a worse answer than proposing three you can justify.",
    "This is analysis and design only. Nothing is deployed here.",
]

# The website's own topology — the same CL3 network diagram, read for a different system.
NETWORK_DIAGRAM = ("Network Diagram — the environment drawn out. Read section 3.3: the website is "
                   "the separate 2023 pilot, not the hardened LMS above it",
                   f"{ICT}/network-diagram-cl3")

CURRENT_ARCH = [
    ("Region", "ap-southeast-2 (Sydney), with the whole workload in a single availability zone"),
    ("Workload", "the YAT public website — marketing pages, the course catalogue, and the online "
                 "enquiry / application intake. An open-source PHP / MySQL CMS on a LAMP stack."),
    ("Access path", "public internet. Anonymous and unauthenticated: anyone can reach it, "
                    "including everything automated that crawls, scrapes and submits to public "
                    "forms. It is not connected to the campus network."),
    ("Application tier", "ONE EC2 instance, Linux + Apache + PHP + the CMS, with an Elastic IP. "
                         "No Auto Scaling group. No load balancer. The instance is the website."),
    ("TLS", "HTTPS terminates on the instance itself, on a certificate installed there"),
    ("Database", "Amazon RDS for MySQL, single-AZ with no standby, gp3, encrypted, 7-day backup "
                 "retention, in private-data-a; not publicly accessible"),
    ("Storage", "the instance's own EBS volume holds the OS, the CMS and all uploaded media — "
                "images, brochures and course PDFs are served off local disk. A separate S3 "
                "bucket holds nightly database and media backups, versioned and private."),
    ("Network", "a separate website VPC; public-web-a and private-data-a in one zone"),
    ("Monitoring", "an instance status-check alarm, and a database free-storage alarm"),
    ("Usage", "24x7. Traffic is public and international, and growing with the India campus. The "
              "annual peak is the intake and application windows, when the site matters most and "
              "when IR-7 forbids production-affecting change."),
    ("Target availability", "none formally set — it was a pilot, and nobody has set one since"),
    ("Administrative access", "SSH to the instance from a small allow-list; no bastion"),
]

SCOPE_NOTE = ("Your work is the cloud infrastructure. The CMS application and the website content "
              "are out of scope (IR-4) — the site must serve the same content and the same "
              "application, no media may be lost, and the visitor experience must not be degraded.")

SIZING_NOTE = ("Instance and database classes throughout this environment are sized to what will "
               "actually launch in an AWS Academy Learner Lab, which caps what is available. A "
               "real public website would warrant larger. Reason about sizing as you would at full "
               "scale — the reasoning is what matters, not the vCPU count.")

# ---------------------------------------------------------------- Part A — analyse and design

DESIGN = [
    dict(n=1, title="Review the current architecture",
         resources=[
             ("Website Infrastructure Specifications — the environment tier by tier",
              f"{ICT}/website-server-status"),
             ("Website Cloud Architecture — Baseline Design — how it was designed at migration, "
              "and why", f"{MIGRATION}/cloud-architecture-baseline"),
             ("Network Diagram — section 3.3 is the website", f"{ICT}/network-diagram-cl3"),
         ],
         prompt="Identify and review the architecture as it stands. Go tier by tier and record "
                "what is there, how it is configured, and what design decision it represents. You "
                "are not judging it yet — this task is establishing what you are looking at.",
         given=1, blank_rows=8, exemplar=1,
         table=(["Tier", "What is there", "The design decision it represents"],
                [["Backups", "nightly database and media snapshots to a versioned S3 bucket",
                  "Somebody did think about losing the data, even in a pilot. Note the shape of "
                  "the third column: it names the decision behind the configuration, not whether "
                  "the decision was good. That judgement is task 2's."],
                 ["Application", "", ""], ["TLS", "", ""], ["Database", "", ""],
                 ["Storage — uploaded media", "", ""], ["Network", "", ""],
                 ["Monitoring", "", ""]]),
         consider=["Read the baseline design before the specifications. It says why this was built "
                   "the way it was, and 'deliberately low-risk pilot' is a design decision, not an "
                   "oversight.",
                   "How many EC2 instances are there? Now look at the LMS in the same diagram. "
                   "What does the website not have that the LMS does?",
                   "Where does HTTPS terminate? On a load balancer, or somewhere else?",
                   "Where do uploaded course brochures and images physically live? Write that row "
                   "carefully — a lot of task 9 depends on it.",
                   "This task is review, not critique. If your rows are filling up with "
                   "recommendations you have jumped to task 2."]),

    dict(n=2, title="Evaluate the architecture and identify the business impact",
         resources=[
             ("Website Specification — who visits, how many, and when",
              f"{ICT}/website-application-spec"),
             ("Improvement Requirements — the outcomes the current state is judged against",
              f"{PROJECT}/improvement-requirements"),
         ],
         prompt="Now evaluate it. For each design decision from task 1, say what it means for the "
                "business — not what it means technically. 'Single EC2 instance' is a fact; 'the "
                "site is down until someone rebuilds it, and prospective students during intake "
                "go elsewhere' is a business impact.",
         given=1, blank_rows=7, exemplar=1,
         table=(["Design decision", "Business impact if it fails or falls short", "How serious"],
                [["Nightly backups held in the same region",
                  "Recoverable from most things that go wrong, but a regional event takes the "
                  "backups with the site. Worth stating even though it is the least of the "
                  "exposures here — an evaluation that only lists the alarming findings is not an "
                  "evaluation.",
                  "low, given what this site is"],
                 ["Single EC2 instance", "", ""],
                 ["Single availability zone", "", ""],
                 ["Single-AZ database", "", ""],
                 ["Media on the instance's local disk", "", ""],
                 ["Public and anonymous, with no traffic filtering", "", ""]]),
         consider=["When does an outage hurt most for this site? Look at what the specification "
                   "says about intake windows before you rate anything.",
                   "A system's operating profile changes what the same technical fact costs. What "
                   "is this site's profile — when is it used, and by whom — and where is that "
                   "written down rather than assumed?",
                   "If the single instance is lost, what actually has to happen to get the site "
                   "back — and how long is that, honestly?",
                   "The media is on the instance's disk. What is lost if the instance is lost, and "
                   "is it in the backups?",
                   "A public form that anyone on the internet can submit to, with nothing in front "
                   "of it. What does that cost YAT — not in security jargon, in business terms?"]),

    dict(n=3, title="Assess compliance against the Indian regulatory requirements",
         resources=[
             ("Indian Regulatory Requirements — the applicable instruments and what they oblige",
              f"{PROJECT}/indian-regulatory-requirements"),
             ("Privacy / Data Handling Policy — YAT's own obligations for the data held here",
              f"{POLICY}/privacy"),
         ],
         prompt="Assess the current infrastructure against the Indian Regulatory Requirements that "
                "now apply to the India-campus operation this site serves. Identify any gaps, and "
                "say what infrastructure change would close each one. You are designing to the "
                "compliance area's determination — you are not interpreting the law.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Requirement", "Current position", "Gap", "Infrastructure change that closes it"],
                [["Data handling and security safeguards",
                  "database storage encrypted; HTTPS to visitors; no filtering of hostile traffic",
                  "Partly met — the gap is at the edge, not at rest.",
                  "Whatever you propose in task 10. Note that a row can be partly compliant; the "
                  "middle two columns are not a yes/no."],
                 ["Log retention in-jurisdiction", "", "", ""],
                 ["Retrievability for incident reporting", "", "", ""],
                 ["", "", "", ""]]),
         consider=["Which of these obligations bite on a public marketing site that collects "
                   "enquiry forms, and which are about systems this one is not?",
                   "What does the site log today, where does it go, and how long is it kept? Look "
                   "before you answer.",
                   "The enquiry form collects personal information from prospective students, "
                   "including India-campus applicants. Does that change anything?",
                   "IR-3 and the Role Brief both say the same thing about legal advice. If you "
                   "find yourself writing about what the law means, stop."]),

    dict(n=4, title="Identify design patterns and architectural options",
         resources=[
             ("Reference Architectures — the patterns YAT's architects work from",
              f"{REFERENCE}/reference-architectures"),
         ],
         prompt="Identify the design patterns and architectural options available to address what "
                "you found in tasks 2 and 3. You are building the menu here, not choosing from "
                "it — include options you will later reject, because rejecting an option with a "
                "reason is part of the design.",
         given=1, blank_rows=8, exemplar=1,
         table=(["Pattern or option", "What it addresses", "Where it would apply here"],
                [["Infrastructure as code",
                  "reproducibility, reviewable change, and a rebuild path",
                  "The whole environment; IR-5 asks for it. It is on the menu in every version of "
                  "this engagement, which is why it is safe to work here as an example."],
                 ["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""],
                 ["", "", ""]]),
         consider=["The site has one instance and no load balancer. What pattern turns that into "
                   "a tier that survives losing a server?",
                   "Once there is more than one instance, where can uploaded media NOT live? What "
                   "pattern solves that?",
                   "The audience is international and growing. What sits in front of a website to "
                   "serve distant visitors quickly — and what else does that thing do for you?",
                   "The traffic is anonymous and public. What pattern addresses hostile and "
                   "automated traffic, and where does it sit?",
                   "Name the option of doing nothing to the database, too. It belongs on the menu "
                   "so you can reject it with a reason in task 7.",
                   "Frame these as principles, not products. 'Remove single points of failure' is "
                   "a principle; a service name is not."]),

    dict(n=5, title="Assess the benefits against the current business model",
         resources=[
             ("Website Operational Costing — what this environment costs today",
              f"{ICT}/website-operational-costing"),
         ],
         prompt="Determine and assess what the options from task 4 actually give YAT, against the "
                "way this business runs. The website is public, 24x7, and its busiest period is "
                "the one that generates enrolments — that shapes what an improvement is worth. Say "
                "what each option costs and what it buys.",
         given=1, blank_rows=7, exemplar=1,
         table=(["Option", "What it costs", "What it buys, for this business"],
                [["Infrastructure as code", "effort now, no ongoing run cost",
                  "Reproducibility and a rebuild path. Notice the cost column is not always "
                  "dollars — 'effort now' is a real cost and stating it that way is honest."],
                 ["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""]]),
         consider=["When is this site idle enough that you could turn something off? Answer that "
                   "honestly before you look for cost savings — it rules some of them out.",
                   "A load balancer plus a second instance roughly doubles compute. What does that "
                   "buy on a site whose value is being reachable when a prospective student looks?",
                   "Moving media to object storage costs almost nothing. What does it buy — and is "
                   "the answer only about resilience?",
                   "An edge layer costs money per request but can reduce what the origin serves. "
                   "Does it cost or save here? Say which and why.",
                   "The costing document gives you today's baseline. Every 'what it costs' should "
                   "be relative to that, not an abstract figure."]),

    dict(n=6, title="Set the business goals",
         resources=[
             ("Improvement Requirements — IR-1 to IR-7, the outcomes these goals must serve",
              f"{PROJECT}/improvement-requirements"),
         ],
         prompt="Set the business goals this improvement is aiming at, across security, "
                "reliability, performance and cost. These are yours to determine — the Improvement "
                "Requirements give outcomes, not numbers. Make each one measurable, because "
                "someone later has to demonstrate whether it was met.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Area", "Business goal", "Why this level, for this system"],
                [["Cost", "no more than a modest increase in monthly run cost",
                  "IR-2 and IR-6 — proportionate to a marketing site. Every other row in this "
                  "table pushes cost up, so setting the ceiling first is what makes the rest of "
                  "them decisions rather than a wish list."],
                 ["Reliability", "", ""],
                 ["Recovery", "", ""],
                 ["Security", "", ""],
                 ["Performance", "", ""]]),
         consider=["There is no availability target set for this site today. You have to invent "
                   "one and defend it. What is defensible for a public front door — and what would "
                   "be gold-plating?",
                   "'Improve reliability' is not a goal. What number, measured how?",
                   "Recovery has two numbers, not one. How long down, and how much lost?",
                   "For performance, whose experience are you setting a goal for — an Australian "
                   "visitor or an Indian one? Are they the same number?",
                   "Check every goal against IR-2. Would you be comfortable defending this number "
                   "to someone paying for it?"]),

    dict(n=7, title="Confirm your design decisions against business needs",
         prompt="Before you design in detail, confirm the direction. State the improvements you "
                "are going to propose, and for each name the business need from task 6 it serves "
                "and the option from task 4 you chose. Just as importantly, state what you are NOT "
                "proposing and why — that is where IR-2 is actually assessed.",
         given=1, blank_rows=8, exemplar=1,
         table=(["Proposing / not proposing", "Improvement", "The business need it serves"],
                [["Not proposing", "re-platforming the CMS onto a managed service",
                  "IR-4 puts the application out of scope, and nothing in the analysis needed it. "
                  "A rejected option with a reason is worth as much here as a proposed one — this "
                  "row is where IR-2 gets marked."],
                 ["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""],
                 ["", "", ""]]),
         consider=["Every improvement you list must trace to a goal in task 6. If it does not, "
                   "either the goal is missing or the improvement is not justified.",
                   "You should have at least two things in the 'not proposing' column. If you have "
                   "none, you have not made a proportionality judgement — you have made a wish "
                   "list.",
                   "Is there a decision here that could genuinely go either way? Mark it as one "
                   "and say you will argue it. Those are the interesting ones.",
                   "Would every item survive the question 'what does this buy YAT, and what does "
                   "it cost?' asked out loud by someone paying?"]),

    dict(n=8, title="Evaluate and confirm the performance metrics",
         prompt="Confirm the metrics that will show whether the goals in task 6 were achieved. For "
                "each, say what is measured, where the measurement comes from, and what value "
                "counts as meeting the goal. Someone later deploys this and has to demonstrate it "
                "against these metrics — write them so that is possible.",
         given=1, blank_rows=7, exemplar=1,
         table=(["Goal", "Metric", "Where it is measured", "Target value"],
                [["Cost", "monthly run cost", "cost reporting for the tagged resources",
                  "Within the increase agreed in task 6. The third column has to name a real place "
                  "the number comes from — 'monitoring' is not a place."],
                 ["Availability", "", "", ""],
                 ["Availability", "", "", ""],
                 ["Recovery", "", "", ""],
                 ["Security", "", "", ""],
                 ["Performance", "", "", ""]]),
         consider=["For each metric ask: could someone else read this and take the measurement "
                   "without asking me a question?",
                   "A metric with no threshold cannot be demonstrated against. Every row needs a "
                   "number or a stated condition.",
                   "How would you actually measure availability once there is a load balancer in "
                   "front? What does it count for you?",
                   "How do you measure a recovery goal without waiting for a disaster?",
                   "Performance for an international audience — what is measured, and where from?"]),

    dict(n=9, title="Design — compute, storage, database and network",
         prompt="Select and design the improvements to the resources themselves. Go tier by tier "
                "and say what changes, what stays, and why. Where you are leaving something alone, "
                "say so explicitly — an unmentioned tier reads as an oversight rather than a "
                "decision.",
         given=1, blank_rows=7, exemplar=1,
         table=(["Resource", "Your design", "Why"],
                [["Database", "your decision from task 7, designed out here",
                  "Carried forward deliberately. Wherever a task 7 decision lands in a later "
                  "table, say what you are doing and why — 'as above' is not a design."],
                 ["Compute", "", ""],
                 ["Load balancing", "", ""],
                 ["Storage — uploaded media", "", ""],
                 ["Storage — backups", "", ""],
                 ["Network", "", ""]]),
         consider=["The website has no load balancer and no Auto Scaling group. So the compute row "
                   "is not 'spread the tier across two zones' — it is 'build a tier'. What has to "
                   "exist first?",
                   "If you run two instances, and a visitor uploads nothing but the CMS serves "
                   "media from local disk — what breaks? Which visitor sees what?",
                   "Where does TLS terminate once there is a load balancer? Is that a change or "
                   "does it stay on the instance?",
                   "A second zone needs subnets in it. Does the website VPC have them?",
                   "What is the smallest set of changes that produces a tier that survives losing "
                   "an instance? Start there, then justify anything beyond it."]),

    dict(n=10, title="Design — security improvements",
         resources=[
             ("Security & Incident Response Policy — YAT's security obligations",
              f"{POLICY}/security-incident"),
             ("User Access Policy — access control requirements", f"{POLICY}/user-access"),
         ],
         prompt="Review the security of the environment and design the improvements you judge "
                "necessary. Note what is already adequate — improving what is already fine is how "
                "an improvement proposal loses credibility.",
         given=1, blank_rows=7, exemplar=1,
         table=(["Layer", "Current position", "Your design"],
                [["Data at rest", "database storage encrypted with a managed key",
                  "Unchanged; confirm encryption on any new storage you introduce. Not every row "
                  "is a change — saying 'this is already right' is part of the review."],
                 ["Network — exposure", "", ""],
                 ["Application traffic — bots and abuse", "", ""],
                 ["Transport", "", ""],
                 ["Administrative access", "", ""],
                 ["Detection", "", ""]]),
         consider=["This site is public by design. You cannot fix that, and you should not try — "
                   "so what CAN you do about the traffic it attracts?",
                   "The enquiry form is a public form on the open internet. What happens to it "
                   "today when someone points a script at it?",
                   "Administrative access is SSH from an allow-list. Compare that with how the "
                   "LMS and Ledgerline are administered. Is there a better answer available?",
                   "TLS already exists here — it terminates on the instance. Is that a strength, "
                   "or does it become a problem in your task 9 design?",
                   "Think in layers: network, transport, application, identity, data. A proposal "
                   "that is one control at one layer has not reviewed the environment."]),

    dict(n=11, title="Design — reliability and scalability improvements",
         prompt="Design the reliability and scalability improvements in detail. This is where your "
                "database decision from task 7 gets designed out properly — say exactly what you "
                "are doing and what recovery behaviour it produces. Be specific about what happens "
                "when each component fails.",
         given=1, blank_rows=7, exemplar=1,
         table=(["Component", "Your design", "What now happens when it fails"],
                [["Backups", "unchanged in mechanism; verify the restore actually works",
                  "A backup that has never been restored is a hope. Note that the third column "
                  "here describes behaviour, not configuration — that is what the column is for."],
                 ["Application instance", "", ""],
                 ["Availability zone", "", ""],
                 ["Database", "", ""],
                 ["Uploaded media", "", ""],
                 ["Traffic peak at intake", "", ""]]),
         consider=["Go back to the single points of failure you found in task 2. Each one is "
                   "either removed here or explicitly accepted with a reason. There is no third "
                   "option.",
                   "For each row, finish the sentence 'when this fails, a visitor sees…'. If you "
                   "cannot, the design is not specific enough yet.",
                   "Scalability for this site means the intake peak. What scales, on what signal, "
                   "and how fast does it need to be?",
                   "IR-7 forbids production change during the intake window. Does that change what "
                   "your scaling design has to do on its own?"]),

    dict(n=12, title="Design — cost optimisation and monitoring",
         prompt="Two things that pull in opposite directions. Say how you are keeping the cost of "
                "your improvements proportionate, and design the monitoring that will let someone "
                "demonstrate the goals from task 6 were actually met. A goal nobody can measure is "
                "not a goal.",
         given=1, blank_rows=7, exemplar=1,
         table=(["Item", "Your design", "Why"],
                [["Cost — the database decision", "carried from task 7",
                  "Usually the single biggest cost lever in a design like this, which is why it "
                  "gets a row of its own rather than being buried in a total."],
                 ["Cost — right-sizing", "", ""],
                 ["Cost — offloading the origin", "", ""],
                 ["Monitoring — availability", "", ""],
                 ["Monitoring — recovery readiness", "", ""],
                 ["Monitoring — cost", "", ""]]),
         consider=["What are the cost levers on a site that has to answer at 3am on a Sunday? "
                   "There are several; turning it off is not one of them.",
                   "If an edge layer serves most requests, what happens to the size of the origin "
                   "you have to run? Is that a cost or a saving?",
                   "Every monitor you design should map onto a metric from task 8. If it does not "
                   "measure a stated goal, why is it there?",
                   "What tells you a backup has stopped working, before you need it?"]),

    dict(n=13, title="Cost-benefit justification",
         resources=[
             ("Website Operational Costing — the current run cost, and the basis for your "
              "comparison", f"{ICT}/website-operational-costing"),
         ],
         prompt="IR-6 requires every improvement to be justified on cost versus benefit, with its "
                "ongoing operating-cost impact made explicit. Do that for each improvement you are "
                "proposing. Order does not matter, but nothing may be missing — an improvement "
                "without a line here is one YAT cannot approve.",
         given=1, blank_rows=8, exemplar=1,
         table=(["Improvement", "Ongoing cost impact", "Benefit", "Justified because"],
                [["Infrastructure as code", "no run cost; effort now",
                  "reproducibility and reviewable change",
                  "IR-5 asks for it. Not every line has a dollar impact, and saying so plainly is "
                  "better than inventing one."],
                 ["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""],
                 ["", "", "", ""], ["", "", "", ""]]),
         consider=["Cross-check against task 7. Every improvement you said you were proposing "
                   "needs a line here — a missing one is an improvement YAT cannot approve.",
                   "Exact dollars are not required. A direction and a magnitude, reasoned from the "
                   "costing document, is.",
                   "Does anything on your list REDUCE cost? Say so — it offsets the rest and it is "
                   "the strongest thing you can put in front of Sam.",
                   "Add it up roughly. Is the total inside the cost goal you set in task 6? If "
                   "not, something has to give, and deciding which is the work."]),

    dict(n=14, title="Draw the improved architecture",
         prompt="Draw the improved architecture: both availability zones, every tier, what you "
                "added, and what you kept. Mark clearly what is new. A reader who has not seen "
                "your tables should be able to see what changes and what does not.",
         diagram="the improved website architecture — both zones, every tier, and what is new",
         consider=["Draw the visitor's request path first and hang the components off it.",
                   "Mark what is new. A diagram where the reader cannot tell the change from the "
                   "baseline has not done this task's job.",
                   "Everything in tasks 9 to 12 should appear. Anything in the diagram that is in "
                   "none of those tables is unjustified.",
                   "Where does media live in your drawing? If it is still on the instance, check "
                   "that against your task 9 answer."]),

    dict(n=15, title="Document and justify the proposed architecture",
         prompt="Justify the architecture you have documented in tasks 9 to 14. For each "
                "significant improvement, say which business goal from task 6 it serves and why "
                "you chose it over the alternative you considered in task 4. Say plainly what you "
                "decided not to do and why. This is a written answer, and it is where your "
                "reasoning is assessed rather than your design.",
         points=[
             "each improvement tied to a specific goal from task 6, not to convention",
             "the genuinely arguable decision argued at length, on cost against benefit",
             "the improvements NOT proposed, with their reasons — IR-2 is assessed here",
             "the existing strengths named as deliberately retained",
             "the ongoing cost impact stated against the cost goal",
             "the design presented as changes to a working system, not as a rebuild",
         ],
         consider=["A justification is not a description. If a sentence would still be true "
                   "written by someone who had not made the choice, it is a description.",
                   "'Best practice' justifies nothing. What did THIS site need, and what did this "
                   "improvement do about it?",
                   "Which of your decisions could a reasonable person disagree with? Argue that "
                   "one hardest — it is where the marks are in the real thing.",
                   "Have you said what you deliberately left alone? A proposal that reads as a "
                   "rebuild has misread IR-4 and IR-2 both."]),
]

# ---------------------------------------------------------------- Part B — review and approval

APPROVAL = [
    dict(n=16, title="Prepare your presentation",
         prompt="Plan how you will take Sam Walker through your proposal in the time you have, and "
                "for each part write the one point Sam must take away. You are asking for approval "
                "to spend YAT's money, so lead with what it buys, not with what it is.",
         given=1, blank_rows=7, exemplar=1,
         table=(["What you cover", "The one point Sam should take away", "Roughly how long"],
                [["What you are asking for", "approval to proceed to deployment",
                  "1 min. It goes last and it is one sentence — but write it down now, because "
                  "the most common way this goes wrong is stopping without ever asking."],
                 ["What you found", "", ""],
                 ["The goals you set", "", ""],
                 ["What you propose", "", ""],
                 ["The arguable decision", "", ""],
                 ["What it costs", "", ""]]),
         clicks=["Add up your minutes. Over time, cut something now rather than live.",
                 "Open your worksheet and the diagram, and put a marker where you will turn to "
                 "each. Hunting through a document while someone watches eats the clock.",
                 "Decide your opening sentence. 'The site works; what it lacks is resilience' "
                 "beats 'so, I did the analysis first'.",
                 "Say it out loud once with a timer running. It will be shorter and worse than "
                 "you expect, which is exactly what you want to find out now."],
         consider=["Sam is paying. Which order puts the money question where it belongs — early "
                   "enough to matter, late enough to be justified?",
                   "What could you drop entirely if you were running out of time?",
                   "Which single decision are you least confident about? Spend a minute on it "
                   "rather than hoping it is not raised."]),

    dict(n=17, title="Present the proposed architecture for review",
         prompt="Present your proposed architecture to Sam Walker (played by your teacher, or by a "
                "classmate who has worked this run sheet) for review. Walk through the design and "
                "the reasoning, and answer questions on both. Record the session immediately "
                "afterwards.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Record", "Your entry"],
                [["Questions you were asked",
                  "the substance of them, and how you answered — including the one you answered "
                  "badly, which is the only entry in this table you will learn anything from"],
                 ["Date and time", ""],
                 ["Who played Sam", ""],
                 ["What you presented", ""],
                 ["Feedback given, and your response", ""]]),
         clicks=["Open with what you found, in one sentence.",
                 "Present decisions, not components. 'I put a load balancer in front and ran two "
                 "instances because losing the single server currently takes the site down' — not "
                 "a tour of the diagram.",
                 "Give the recommendation before the reasoning. Sam wants to know what you are "
                 "proposing before why.",
                 "Do not read from the worksheet. Look at your listener.",
                 "If you are asked something you do not know, say so and say how you would find "
                 "out. Inventing an answer in front of a client is the unrecoverable move.",
                 "Ask for approval to proceed. Out loud, in those words.",
                 "Fill in the table above before you do anything else."],
         consider=["Did you explain a design, or describe one? Your listener could tell.",
                   "Which question exposed something you had not thought about? Go and fix it.",
                   "Did the cost question come up, and were you ready for it?"]),

    dict(n=18, title="Obtain sign-off to proceed to deployment",
         prompt="Ask for sign-off to proceed to deployment, and record which improvements were "
                "approved. Approval with conditions, or approval of only some of your proposals, "
                "are real outcomes — record exactly what was agreed. Nothing is really being "
                "approved here; what is being practised is closing the loop and writing down a "
                "scope precisely enough that someone else could build to it.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Sign-off record", "Your entry"],
                [["Improvements approved",
                  "list them — in the assessment this is the scope the deployment task works from, "
                  "so vagueness here becomes someone's problem later"],
                 ["Decision", ""],
                 ["Improvements not approved, and why", ""],
                 ["Conditions attached", ""],
                 ["Signed by, and date", ""]]),
         consider=["Read your approved list back. Could someone build exactly that, without "
                   "asking you what you meant?",
                   "If something was cut, is the reason recorded? In three weeks nobody will "
                   "remember.",
                   "'Approved with conditions' is a normal professional outcome. What conditions "
                   "would you expect on this proposal?"]),
]
