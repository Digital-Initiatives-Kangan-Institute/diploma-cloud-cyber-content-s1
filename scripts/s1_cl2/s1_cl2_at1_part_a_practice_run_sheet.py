#!/usr/bin/env python3
"""The S1-CL2 AT1 Part A PRACTICE design run sheet — content.

Same shape as the AT1 Part A assessment workbook, different everything else. A student who
works through this has rehearsed every move the assessment needs without having seen its
answers:

  scenario   the YAT LMS — not the public website
  audience   an authenticated cohort of students and teachers — not anonymous public visitors
  peak       3x during end-of-term assessment windows — not the Jan-Feb enrolment peak
  storage    block storage only, no object storage at all — the website already has S3
  platform   Windows Server running DOODLE — not a LAMP stack

THAT LIST IS THE NO-LEAKAGE GUARD, and the third and fourth items are the load-bearing ones.
The website is anonymous and public, so its edge design turns on caching whole pages for
visitors who are all the same. The LMS is authenticated, so most of what it serves is
per-user and cannot be cached that way — the student has to reason about what actually can
be. And the LMS has no object storage, so "media is already in S3 and the CDN just serves
it" is not available here. An LMS answer transposed onto the website is wrong, and the
reverse is wrong too.

WHAT PRACTICE ADDS, and the whole reason it exists: every task is presented exactly as the
assessment presents it, then adds a "Things to consider" block — leading questions, pointed
enough that a student who is paying attention cannot miss the answer, and which never state
it. Tables carry one worked exemplar row to show the shape of an answer; the rest of the
table is the student's.

No marking criteria, no UoC tags, no institutional boilerplate — it is not an assessment.
Rendered by the assessment's own renderer in s1_cl2_at1_part_a_run_sheet, with these lists
passed in.
"""

SITE = "https://yat.timbaird.com"
STATE = "s1-cl2-at1"
PROJECT = f"{SITE}/intranet/{STATE}/projects/lms-global-expansion"
ICT = f"{SITE}/intranet/{STATE}/ict"
POLICY = f"{SITE}/intranet/{STATE}/policies"
REFERENCE = f"{SITE}/intranet/{STATE}/reference"

# ---------------------------------------------------------------- front matter

SCENARIO = [
    "YAT College is opening an offshore campus in India. The students there will use the same "
    "learning management system as everyone else — DOODLE, the LMS you already know — reaching "
    "it from the other side of the Indian Ocean.",
    "You are an MTS Consultant on the LMS Global Expansion engagement, reporting to Pat Lin (MTS "
    "Senior Consultant), with Sam Walker (YAT ICT Manager) as your YAT-side stakeholder. The LMS "
    "runs in Sydney, hardened across two availability zones by the previous engagement.",
    "This is practice. Nothing here is assessed and nothing is submitted. It is the same work the "
    "assessment will ask for, on a different system — so do it properly, because the moves are "
    "the point, not the answers.",
]

INSTRUCTIONS = [
    "Work the tasks in order — each one builds on the answer before it. Each is presented the way "
    "the assessment presents it, and then adds a Things to consider block underneath.",
    "Those considerations are leading questions, not answers. If you work through them honestly "
    "you will arrive at the answer yourself — which is the only version of it that will still be "
    "there in the assessment.",
    "Where a table has a worked first row, that row is an example of the SHAPE of an answer. It "
    "is never one of the answers the task is asking you for. Yours go underneath it.",
    "Tasks 1 to 14 are the web-scale design. Tasks 15 to 19 are the audit-log microservice. This "
    "is design only — nothing is deployed, and where a task asks for a region, name the region "
    "the design calls for.",
]

# The LMS's own topology — NOT the website diagram the assessment supplies.
NETWORK_DIAGRAM = ("Network Diagram (HA-hardened) — the environment drawn out, including the "
                   "campus VPN the LMS depends on", f"{ICT}/network-diagram-ha-hardened")

CURRENT_ARCH = [
    ("Region", "ap-southeast-2 (Sydney). This is a design exercise — no build, so the region is "
               "the one the design calls for."),
    ("Workload", "the YAT LMS (DOODLE) — course resources, assessment submission, gradebook, "
                 "attendance and teacher notes. Every user signs in: there are no anonymous "
                 "visitors, and nothing is served to anyone who has not authenticated."),
    ("Network", "VPC 10.0.0.0/16 across two zones  ·  public-web-a / -b (load balancer + NAT)  ·  "
                "private-app-a / -b (application tier)  ·  private-data-a / -b (database)"),
    ("Campus link", "Site-to-Site VPN from the campus edge — carries AD-LDAP authentication and "
                    "ICT management traffic. End-user traffic does not use it."),
    ("Load balancing", "internet-facing Application Load Balancer across both public subnets, "
                       "HTTP :80 to the LMS target group. TLS is not terminated here — the "
                       "hostname and its certificate are YAT ICT's."),
    ("Compute", "Auto Scaling group across private-app-a and -b, min 2 / desired 2 / max 4, "
                "target tracking on CPU at 70%; burstable general-purpose instances running "
                "Windows Server with DOODLE installed"),
    ("Database", "Amazon RDS for MySQL, Multi-AZ — primary in private-data-a, synchronous standby "
                 "in private-data-b, automatic failover typically under two minutes, encrypted, "
                 "7-day backup retention"),
    ("Storage", "block storage only. Course materials, uploaded submissions and the database all "
                "sit on EBS volumes attached to the instances and to RDS. There is no object "
                "storage in use for the LMS at all."),
    ("Internet", "an internet gateway, and a NAT gateway in each zone so an availability-zone "
                 "outage does not remove outbound access for the surviving zone"),
    ("Availability posture", "tolerates an instance failure and a single-zone failure without "
                             "intervention; meets the 99.9% target. Recovery from the loss of the "
                             "whole Sydney region is not provided for."),
    ("What is NOT in place", "anything outside this one region. No edge delivery, no presence in "
                             "India, no cross-region recovery, and no audit-log service."),
]

SCOPE_NOTE = ("Your work is the AWS infrastructure. DOODLE itself, the course content and the "
              "campus network are not yours to change — the requirements are explicit that no "
              "operating system or application version changes as part of this engagement.")

# ---------------------------------------------------------------- Part A — design
# Presented as the assessment presents it, plus `consider` — the leading questions.

DESIGN = [
    dict(n=1, title="The scaling needs this design has to meet",
         resources=[
             ("LMS Global Expansion — Functional & Non-Functional Requirements — the targets YAT "
              "signed off on. The figures you need are here", f"{PROJECT}/requirements"),
             ("LMS Application Specification — the workload those targets are set against: who "
              "uses it, how many at once, and when", f"{ICT}/lms-application-spec-cloud"),
         ],
         prompt="Before you design anything, establish what the design is held to. Read the "
                "requirements and the application specification, and record the scaling and "
                "performance needs this expansion must meet. Name the document each one came "
                "from — a target you cannot attribute is one you have assumed.",
         given=1, blank_rows=7, exemplar=1,
         table=(["Need", "What the requirement says", "Where it came from"],
                [["Preserve the operating system and application stack",
                  "no change to the LMS operating system or DOODLE version as part of this "
                  "engagement — whatever you design has to sit around the existing platform "
                  "rather than replace any of it",
                  "Functional & Non-Functional Requirements — non-functional requirements"],
                 ["Serve the India cohort with acceptable latency", "", ""],
                 ["Scale up and down with demand", "", ""],
                 ["Availability must not be degraded", "", ""],
                 ["Read-heavy traffic profile", "", ""],
                 ["Cost-effectiveness", "", ""]]),
         consider=["A target you cannot quote a source for is a target you invented. Where would "
                   "a figure like '99.9% availability' actually be written down for the LMS?",
                   "The requirements say the load varies across the academic calendar. By how "
                   "much, when, and which document puts a number on it?",
                   "'Read-heavy' means something specific for an LMS. What is being read all day, "
                   "and what is comparatively rare?",
                   "The India cohort is additional load, not replacement load. Does that change "
                   "any of the numbers you have just written down?"]),

    dict(n=2, title="Review the current architecture against those needs",
         resources=[
             ("LMS Infrastructure Specifications — the HA-hardened environment as it stands "
              "today, tier by tier", f"{ICT}/lms-server-status-ha-hardened"),
             ("Network Diagram (HA-hardened) — the same environment drawn out",
              f"{ICT}/network-diagram-ha-hardened"),
         ],
         prompt="Go through the current architecture layer by layer. For each, say whether it "
                "meets the needs you recorded in task 1, and if it does not, why not. Work from "
                "what is described above and in the infrastructure specifications — not from what "
                "you would expect a cloud LMS to look like.",
         given=1, blank_rows=8, exemplar=1,
         table=(["Layer", "Meets the needs?", "Why / why not"],
                [["Load balancing", "Yes",
                  "The ALB already spans both availability zones and scales with the tier behind "
                  "it. Nothing about adding a distant audience changes what it does. Notice that "
                  "this row says yes — several layers here are already adequate, and finding them "
                  "matters as much as finding the gaps."],
                 ["Compute", "", ""], ["Database", "", ""], ["Storage", "", ""],
                 ["Content delivery", "", ""], ["India presence", "", ""],
                 ["Campus VPN dependency", "", ""]]),
         consider=["Read the Storage row of the architecture table again. Where do course "
                   "materials and uploaded submissions actually live? What does that mean for "
                   "serving them to someone in India?",
                   "The Auto Scaling group is min 2 / max 4 on CPU at 70%. Is the problem with "
                   "the India cohort a capacity problem, a distance problem, or both?",
                   "The database is Multi-AZ in Sydney. For a student in India, how far does a "
                   "page request travel before anything is read?",
                   "Which layers here already meet their needs? A review that recommends "
                   "rebuilding something that already works has misread the task.",
                   "The campus VPN carries AD-LDAP authentication. Every user signs in. Is that a "
                   "layer worth a row?"]),

    dict(n=3, title="The residency obligation, as a design input",
         resources=[
             ("Data Residency & Sovereignty Requirements — the India obligations, and what they "
              "do and do not require", f"{PROJECT}/data-residency-requirements"),
         ],
         prompt="Read the Data Residency & Sovereignty Requirements and record what they oblige "
                "this design to do. Be precise about the boundary: note what must be held in "
                "India and what may remain in Australia. This is an input that shapes your "
                "design — you are not writing a compliance plan, and you are not interpreting the "
                "law.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Reference", "What the design must do", "What it does not require"],
                [["DR-R5",
                  "keep the handling of India-cohort personal data consistent with YAT's Privacy "
                  "/ Data Handling and Security and Incident Response policies",
                  "it does not ask for a separate compliance deliverable — this one is a "
                  "constraint on how you design, not a thing you build"],
                 ["DR-R1", "", ""], ["DR-R2", "", ""], ["DR-R3", "", ""], ["DR-R4", "", ""]]),
         consider=["DR-R1 and DR-R3 pull in opposite directions on purpose. One says something "
                   "must be in India; the other says something may stay in Australia. Exactly "
                   "which data is each one talking about?",
                   "If you read this and conclude the whole LMS has to move to India, every task "
                   "after this one will over-build. Is that what DR-R3 says?",
                   "DR-R2 sets a six-hour clock. Six hours from what, and what does that imply "
                   "about how the logs are stored — not just where?",
                   "DR-R4 is about the future, not now. What would you have to do differently "
                   "TODAY so that a later change is a deployment rather than a redesign?"]),

    dict(n=4, title="The cloud services this design needs",
         resources=[
             ("Reference Architectures — the service patterns YAT's architects work from",
              f"{REFERENCE}/reference-architectures"),
         ],
         prompt="Name the cloud services you will use to close the gaps you found in task 2, and "
                "say what each one does for you. One row per service. You are identifying the "
                "toolkit here; the design decisions come in the tasks after this one.",
         given=1, blank_rows=7, exemplar=1,
         table=(["Gap it closes", "Service", "What it does here"],
                [["Repeatable Indian footprint", "Infrastructure as code (CloudFormation)",
                  "lets the India-side resources be defined once and stood up by parameter, so a "
                  "second region is a deployment rather than a rebuild. This one is here because "
                  "DR-R4 asks for it, not because code is tidier than clicking."],
                 ["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""]]),
         consider=["Go back to your task 2 gaps. Every service you name here should close one of "
                   "them — if you cannot say which, it does not belong in the table.",
                   "Two gaps need something in front of the LMS and something inside India. What "
                   "kind of service does each of those?",
                   "The log store holds append-only records with one key, read by time window. "
                   "What kind of database is that, and is it the same kind the LMS already uses?",
                   "Something has to receive events from the LMS, hold them if the writer is "
                   "busy, process them and store them. That is more than one service."]),

    dict(n=5, title="Design — the network and entry point",
         prompt="Design how a user's request reaches the LMS once the expansion is in place. Say "
                "what sits in front of the load balancer, how a user in India is routed, and what "
                "changes inside the VPC. Remember the load balancer, subnets and security groups "
                "already exist — say where you leave them alone.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Element", "Your design", "Why"],
                [["Subnets and routing", "unchanged",
                  "Nothing about serving a distant audience requires a different VPC layout. "
                  "Saying so explicitly is part of the answer — the task is about designing "
                  "CHANGES, and 'no change, and here is why' is a design decision."],
                 ["Public entry point", "", ""], ["DNS", "", ""], ["Load balancer", "", ""],
                 ["Campus VPN", "", ""]]),
         consider=["If you put something in front of the load balancer, what does the load "
                   "balancer become to it?",
                   "The LMS has one hostname today. Does a user in India get a different one, or "
                   "the same one resolved differently? What would each choice cost you?",
                   "The ALB is internet-facing. Once there is an edge layer, can someone still "
                   "reach the ALB directly — and does that matter?",
                   "The campus VPN carries authentication traffic. Does anything you are adding "
                   "sit in that path?"]),

    dict(n=6, title="Design — the compute tier",
         prompt="Say what happens to the application tier under the expansion. Consider the "
                "end-of-term assessment peak with the India cohort added to it, and what an edge "
                "layer does — and does not do — to the volume of requests that actually reach an "
                "instance.",
         given=1, blank_rows=5, exemplar=1,
         table=(["Element", "Your design", "Why"],
                [["Scaling signal", "keep target tracking, and reconsider what it tracks",
                  "The tier scales on CPU at 70% today. Whether that is still the right signal "
                  "depends on what reaches an instance after you have designed the edge layer — "
                  "so this row cannot be settled until task 8 is."],
                 ["Auto Scaling group", "", ""], ["Minimum capacity", "", ""],
                 ["Maximum capacity", "", ""], ["Effect of the edge", "", ""]]),
         consider=["The minimum is 2 — one instance per zone. What is that number actually "
                   "holding up, and what happens to availability if you lower it?",
                   "The maximum is 4 and the peak is about 3x normal load. Add a cohort to that. "
                   "Does 4 still hold?",
                   "Here is the one that matters: the LMS is authenticated. How much of what a "
                   "signed-in student requests can be served without reaching an instance at all? "
                   "Be honest — the answer is not 'most of it'.",
                   "The instances run Windows Server with DOODLE pre-installed and the "
                   "requirements forbid changing either. Does that constrain how you scale?"]),

    dict(n=7, title="Design — the database and storage tier",
         prompt="Say what happens to the database and to file storage. Both already exist and "
                "both already work — the question is what the global audience and the read-heavy "
                "profile change about them, if anything. Look carefully at where LMS files "
                "actually live before you answer.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Element", "Your design", "Why"],
                [["Backups", "unchanged here",
                  "Backups are the recovery plan's business, not the scaling design's. Naming a "
                  "row and deliberately deferring it is a legitimate design move — what is not "
                  "legitimate is quietly leaving it out."],
                 ["Primary database", "", ""], ["Read scaling", "", ""],
                 ["Course materials and submissions", "", ""], ["Where those files live today",
                                                                "", ""]]),
         consider=["The website engagement has its media in object storage already. The LMS does "
                   "not — course materials and submissions are on EBS volumes attached to "
                   "instances. What does that mean for serving a 40 MB lecture recording to "
                   "someone in India?",
                   "If files live on an instance's own disk, what happens when the Auto Scaling "
                   "group launches a second instance? Is that already a problem today, or only "
                   "once you add distance?",
                   "The requirements forbid changing the operating system or the DOODLE version. "
                   "Do they forbid changing where the files sit?",
                   "The catalogue-equivalent for an LMS is course content: read constantly, "
                   "changed rarely. What does that suggest about read scaling?",
                   "Submissions are writes, and they arrive in a spike at the end of term. Which "
                   "part of the database tier does that land on?"]),

    dict(n=8, title="Design — serving a global audience",
         resources=[
             ("LMS Global Expansion — Functional & Non-Functional Requirements — the global "
              "serving requirement", f"{PROJECT}/requirements"),
         ],
         prompt="This is the task the whole expansion turns on. Set out how the architecture "
                "serves the India cohort: what is cached, where, for how long, and what cannot be "
                "cached. Every user of this system is signed in — say what that does to your "
                "answer, and how a user in Australia and a user in India each reach content.",
         given=1, blank_rows=7, exemplar=1,
         table=(["Content", "Cached where", "Policy", "Why"],
                [["The sign-in page itself", "edge", "cached, short TTL",
                  "It is the same for everybody and it is the first thing anyone in India "
                  "requests. It is also about the only whole page that is — which is the point "
                  "this table has to work out."],
                 ["Static assets (stylesheets, scripts, icons)", "", "", ""],
                 ["Course materials (documents, slides, recordings)", "", "", ""],
                 ["A student's own dashboard or gradebook", "", "", ""],
                 ["Assessment submission", "", "", ""],
                 ["Teacher marking and attendance", "", "", ""]]),
         consider=["Caching a page at the edge means one copy is served to many people. Which "
                   "parts of an LMS are the same for many people, and which are the same for "
                   "exactly one?",
                   "If you cached a student's gradebook at the edge, what would the next student "
                   "see? That failure mode is the reason this task exists.",
                   "A content delivery network does two things: it caches, and it carries traffic "
                   "over the provider's own network instead of the open internet. Which of those "
                   "helps a request that CANNOT be cached?",
                   "Course materials are large, they change rarely, and every student in a class "
                   "wants the same file. But they are behind a login. Is there a way to serve "
                   "them from the edge without serving them to the wrong person?",
                   "Authentication goes over the campus VPN to AD-LDAP. Does a user in India sign "
                   "in any faster because of anything you have designed?"]),

    dict(n=9, title="Design — the caching decision",
         prompt="Task 8 put content at the edge. There is a second, different caching question "
                "inside the architecture: repeated database reads. Choose between a content "
                "delivery network and an in-memory data store for this problem — or say where you "
                "use each — and explain the choice against your workload. Name the option you did "
                "not choose as well as the one you did.",
         given=1, blank_rows=4, exemplar=1,
         table=(["Option", "Where you would use it", "What it does not solve"],
                [["Neither, for assessment submissions", "nowhere in that path",
                  "A submission is a write. Caching does nothing for it in either place — worth "
                  "stating, because the end-of-term spike is a write spike and no caching "
                  "decision will help it."],
                 ["Content delivery network", "", ""],
                 ["In-memory data store", "", ""],
                 ["Your decision", "", ""]]),
         consider=["These two are not competing answers to one question. Where does each one "
                   "physically sit — how far from the user, and how far from the database?",
                   "The edge removes distance. What does an in-memory cache remove?",
                   "A course page runs the same handful of queries for every student in the "
                   "class, every time. Which of the two helps that, and where is it?",
                   "If you use both, say where the boundary is. If you use one, say what you are "
                   "accepting by not using the other."]),

    dict(n=10, title="Check the design scales as utilisation increases",
         prompt="Walk your design through a load increase. Take the end-of-term assessment peak "
                "with the India cohort added, and say what each layer does as demand rises — and "
                "what would run out first. A design that only works at today's volume has not met "
                "the requirement.",
         given=1, blank_rows=5, exemplar=1,
         table=(["Layer", "What happens as load rises", "What runs out first"],
                [["Network / edge", "the edge layer absorbs it — edge capacity is elastic",
                  "Nothing practical at YAT's scale. Not every row will be this comfortable, "
                  "which is what makes the rest of the table worth doing."],
                 ["Compute", "", ""], ["Database — reads", "", ""],
                 ["Database — writes", "", ""], ["Storage", "", ""]]),
         consider=["This task asks you to find where the design STOPS. If nothing in your table "
                   "runs out, you have not looked hard enough.",
                   "The Auto Scaling group has a configured maximum. What happens at that number, "
                   "and who finds out first?",
                   "How many writers does the database have? Can you add another one? What is the "
                   "only way to make that component bigger?",
                   "End of term is a submission spike — writes and file uploads at once. Trace "
                   "that particular load through every layer and see where it piles up."]),

    dict(n=11, title="Check availability and security are maintained",
         resources=[
             ("Privacy / Data Handling Policy — YAT's obligations for the personal information "
              "the LMS holds", f"{POLICY}/privacy"),
         ],
         prompt="Your changes must not cost the LMS the availability it already has, and they "
                "must not open it up. Go through what you have added and say, for each, what it "
                "does to availability and what it does to the attack surface.",
         given=1, blank_rows=6, exemplar=1,
         table=(["What you added", "Effect on availability", "Effect on security"],
                [["Nothing — the existing Multi-AZ platform", "unchanged, and that is the point",
                  "The baseline is not a thing you added, but starting the table here forces the "
                  "comparison the task wants: everything below this row is new, and new things "
                  "have effects in both columns."],
                 ["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""]]),
         consider=["An edge layer improves availability by serving cached content when the origin "
                   "is stressed. What does it do to availability when the edge layer itself has a "
                   "problem? You have just added something to the request path.",
                   "The LMS holds student submissions, grades and attendance — personal "
                   "information under the Privacy Policy. Does anything you designed move a copy "
                   "of that anywhere new?",
                   "If content is cached at the edge, who can retrieve it? Is 'anyone with the "
                   "URL' an acceptable answer for a course recording?",
                   "The audit-log service holds a record of who did what. What is the security "
                   "posture of the thing you are about to design in tasks 15 to 19?",
                   "'It is still Multi-AZ so availability is maintained' is not an answer. What "
                   "did you actually check?"]),

    dict(n=12, title="Review your design and revise it",
         prompt="Go back over tasks 5 to 11 as a whole. Does the design meet every need you "
                "recorded in task 1? Where it does not, or where two decisions you made pull "
                "against each other, say what you would change. If you change nothing, say what "
                "you checked and why you are satisfied — 'no changes' is an acceptable answer "
                "only if it is an argued one.",
         given=1, blank_rows=5, exemplar=1,
         table=(["Need from task 1", "Met?", "Change you would make"],
                [["Preserve the OS and application stack", "Yes",
                  "Nothing in the design touches Windows Server or DOODLE — the changes sit in "
                  "front of the platform and beside it. Worth checking rather than assuming: it "
                  "is the requirement a keen design is most likely to have broken."],
                 ["", "", ""], ["", "", ""], ["", "", ""]]),
         consider=["Copy your task 1 needs down the first column. Every one of them gets a row — "
                   "that is what makes this a review rather than a summary.",
                   "Look for a decision that pulls against another. A long cache lifetime serves "
                   "India well and publishes a corrected assessment brief slowly. Which do you "
                   "choose, and did you say so anywhere?",
                   "Cost-effectiveness was one of your needs. Is there anything in your design "
                   "you added because it is good practice rather than because a need asked for "
                   "it?",
                   "If you genuinely would change nothing, write down what you checked. An "
                   "unargued 'no changes' and a lazy 'no changes' look identical on the page."]),

    dict(n=13, title="Draw the web-scale architecture",
         prompt="Draw the extended architecture as a diagram: the path a request takes from India "
                "and from Australia, everything you added, and everything you kept. Label the "
                "regions. A reader who has not seen your tables should be able to follow how the "
                "LMS now serves a global cohort.",
         diagram="the extended LMS architecture — edge, region, tiers, the campus VPN, and the "
                 "request path from both cohorts",
         consider=["Draw the request path first and hang the components off it. A diagram of "
                   "boxes with no path through them does not show how anything is served.",
                   "Two users, two starting points, one system. Does your diagram let a reader "
                   "trace both?",
                   "Everything in tasks 5 to 8 should appear. Anything in your diagram that is in "
                   "none of those tables is something you have not justified.",
                   "Mark the region boundary. It is about to matter a great deal in task 17."]),

    dict(n=14, title="Justify the web-scale design",
         prompt="Justify the architecture you have documented in tasks 5 to 13. For each "
                "significant choice, say which of the scaling needs from task 1 it answers, and "
                "why you chose it over the alternative you considered. This is a written answer, "
                "not a table — and it is where your design reasoning goes, not your design.",
         points=[
             "each significant choice tied to a need from task 1, not to convention",
             "what you deliberately kept, and why keeping it was a decision",
             "at least one alternative you rejected, with the reason",
             "the authenticated-audience constraint and what it cost you at the edge",
             "cost-effectiveness — the simplest arrangement that meets the requirements",
         ],
         consider=["A justification is not a description. If a sentence would still be true "
                   "written by someone who had not made the choice, it is a description.",
                   "'CloudFront is fast and scalable' justifies nothing. What did YOUR system "
                   "need, and what did this answer about it?",
                   "Name something you rejected. A design with no rejected alternatives was not "
                   "chosen, it was assumed.",
                   "The website engagement can cache almost everything. You cannot. Say so — the "
                   "constraint you worked around is the most interesting thing in your design.",
                   "Would Sam Walker, reading this, be able to disagree with you? If not, you "
                   "have not said anything he could act on."]),

    # ------------------------------------------------ element 2: microservice design
    dict(n=15, title="The microservice and the data it handles",
         resources=[
             ("LMS Global Expansion — Functional & Non-Functional Requirements — the audit / "
              "access log requirement and why it is a separate service",
              f"{PROJECT}/requirements"),
             ("Data Residency & Sovereignty Requirements — what has to be captured and held in "
              "India", f"{PROJECT}/data-residency-requirements"),
         ],
         prompt="The residency obligation you recorded in task 3 is met by a dedicated service, "
                "not by changing the LMS. Identify what that service does: the events it "
                "receives, the data each event carries, and where the data comes to rest. One row "
                "per data transaction.",
         given=1, blank_rows=5, exemplar=1,
         table=(["Transaction", "What it carries", "Where it comes to rest"],
                [["Retrieval for incident reporting",
                  "a query over the retained records for a time window",
                  "read from the India-region store, inside the six-hour obligation. This row is "
                  "the one people forget: a store nobody can query in time does not satisfy "
                  "DR-R2, however well it is written to."],
                 ["Sign-in event from the LMS", "", ""],
                 ["Course-access event", "", ""],
                 ["Assessment-submission event", "", ""]]),
         consider=["An access log has to answer four questions about an event: who, what, when, "
                   "and from where. What field carries each?",
                   "'Who' is a problem. The obligation needs the record to be useful, and the "
                   "Privacy Policy would rather you did not copy student names into another "
                   "country. Is there a middle answer?",
                   "A submission event and the submission itself are different things. Which of "
                   "them goes to India, and which stays in Sydney? DR-R3 has the answer.",
                   "If you wrote these records into the existing MySQL database in Sydney, which "
                   "requirement would you have failed?"]),

    dict(n=16, title="The cloud services that support it",
         prompt="Name the services your microservice is built from, and say what each "
                "contributes. The service has to receive events from the LMS, hold them safely if "
                "it is busy or briefly unavailable, process them, and store them — say which "
                "service does each of those, and why that kind of service suits the job.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Role", "Service", "Why this kind of service"],
                [["Provision", "infrastructure as code, parameterised by region",
                  "Not a runtime component at all, but it belongs in the table: it is what makes "
                  "the Indian footprint reproducible, which is the whole of DR-R4."],
                 ["Receive events", "", ""], ["Decouple and buffer", "", ""],
                 ["Process", "", ""], ["Store", "", ""]]),
         consider=["Why not have the LMS write straight to the store? Work out what breaks the "
                   "first time the store is slow — and remember the requirement says this service "
                   "must not affect LMS availability.",
                   "The thing between the producer and the writer has a name and a specific job. "
                   "What does it protect against?",
                   "The event rate is bursty and low most of the time. What kind of compute costs "
                   "nothing while nothing is happening?",
                   "The store holds append-only records, one key, retained 180 days. Is that the "
                   "same kind of database as the LMS's MySQL? Why not?"]),

    dict(n=17, title="Draw the microservice architecture",
         prompt="Draw the microservice: the LMS as the event producer, each component of your "
                "service, the direction events travel, and the region boundary between Australia "
                "and India. Show where the LMS's responsibility ends and the service's begins.",
         diagram="the activity-audit microservice — producer, endpoint, queue, processor, store, "
                 "and the Australia / India region boundary",
         consider=["Events go one way. Does your diagram show that, or does it have arrows in "
                   "both directions between the LMS and the service?",
                   "Draw the region boundary as an actual line and put each component on the "
                   "correct side of it. Which components are in India?",
                   "Where exactly does the LMS's responsibility stop? There should be one place "
                   "the two systems touch — mark it.",
                   "If your diagram shows the LMS writing directly to the store, you have drawn "
                   "the coupling back in that task 16 designed out."]),

    dict(n=18, title="The interface contract",
         prompt="Define the contract between the LMS and your service — the one place they touch. "
                "Say what the LMS sends, what it gets back, and what happens if the same event "
                "arrives twice. Someone building either side from your contract alone should not "
                "have to ask you a question.",
         given=1, blank_rows=7, exemplar=1,
         table=(["Element of the contract", "Your definition", "Why"],
                [["Direction", "LMS → service, one way",
                  "The LMS does not read its own audit log. Stating the direction first is what "
                  "makes the rest of the contract answerable — everything below is about one "
                  "call going one way."],
                 ["Call", "", ""], ["Payload", "", ""], ["Success response", "", ""],
                 ["Failure response", "", ""], ["Duplicates", "", ""]]),
         consider=["What does the service tell the LMS on success — that the event was STORED, or "
                   "that it was RECEIVED? Those are different promises, and only one of them "
                   "keeps the decoupling you designed.",
                   "Networks redeliver. If the same event arrives twice, what stops a second "
                   "record being written? Which field makes that possible?",
                   "A contract someone can build against names types, not just fields. What type "
                   "is the timestamp, and in which time zone?",
                   "What happens to a malformed request? 'It fails' is not a contract.",
                   "Read your contract back and ask: does the LMS need to know anything about the "
                   "queue, the function or the store? If it does, the coupling is not as loose as "
                   "you think."]),

    dict(n=19, title="Justify the microservice design",
         prompt="Justify the microservice you have documented in tasks 15 to 18. Say why a "
                "separate service rather than a change to the LMS, why each component is there, "
                "and what your design would cost you if the service were unavailable for an hour. "
                "As with task 14, this is a written answer.",
         points=[
             "separation argued from the requirement, not from a preference for microservices",
             "the India region argued from DR-R1, and what stays in Australia argued from DR-R3",
             "the queue argued from what it protects against",
             "the store choice argued from the access pattern",
             "an honest answer to the hour-of-downtime question",
             "region as a parameter argued from DR-R4",
         ],
         consider=["Why is this a separate service? There is a requirement that says so almost in "
                   "those words. Quote it rather than reaching for 'best practice'.",
                   "The engagement forbids changing DOODLE. Does that make the separation easier "
                   "to justify, or is it a separate argument?",
                   "The hour-of-downtime question is the honest one. Are events lost, delayed, or "
                   "queued — and for how long before that stops being true?",
                   "You chose a store. Say what the alternative was and what would have made you "
                   "choose it instead."]),
]
