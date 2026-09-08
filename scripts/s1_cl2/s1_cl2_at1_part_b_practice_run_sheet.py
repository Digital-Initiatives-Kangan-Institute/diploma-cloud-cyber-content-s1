#!/usr/bin/env python3
"""The S1-CL2 AT1 Part B PRACTICE disaster-recovery run sheet — content.

Same shape as the AT1 Part B assessment workbook, different everything else. The system being
recovered is the LMS the student designed in the Part A practice, not the public website.

WHAT MAKES THE LMS A DIFFERENT RECOVERY PROBLEM — and these are the reasons an answer worked
out here cannot be transposed onto the assessment:

  no object storage    the website's media and backups already sit in S3, which replicates to
                       another region with a setting. The LMS holds course materials and
                       student submissions on EBS volumes. Getting them to a second region is
                       a snapshot-and-copy problem, not a checkbox.
  a machine image      the application tier is Windows Server with DOODLE pre-installed. An
                       AMI does not exist in a region until someone copies it there, and a
                       recovery that has not is a recovery that stalls at step one.
  authentication       every LMS user signs in against AD-LDAP over the campus VPN. Recover
                       the LMS into Melbourne and nobody can log in until the VPN reaches it.
                       The website is anonymous and has no equivalent of this at all.
  what an outage costs students cannot submit at the end of term. That is an academic-integrity
                       and appeals problem, not lost enrolments.

TASK ORDER FOLLOWS THE DR PLAN TEMPLATE'S SECTION ORDER, exactly as the assessment's does, so
the closing task is transcription rather than translation. Practising that is part of the
point.

WHAT PRACTICE ADDS: a "Things to consider" block on every task, and one worked exemplar row
per table showing the SHAPE of an answer without ever being one of the answers asked for.

No marking criteria, no UoC tags. Rendered by the assessment's own renderer in
s1_cl2_at1_part_b_run_sheet, with these lists passed in.
"""

SITE = "https://yat.timbaird.com"
STATE = "s1-cl2-at1"
PROJECT = f"{SITE}/intranet/{STATE}/projects/lms-global-expansion"
ICT = f"{SITE}/intranet/{STATE}/ict"
POLICY = f"{SITE}/intranet/{STATE}/policies"
REFERENCE = f"{SITE}/intranet/{STATE}/reference"

# ---------------------------------------------------------------- front matter

INTRO = [
    "Part A designed the extended LMS. This part plans its recovery: what could take it down, "
    "what that would cost YAT, how you would get it back, and how long that would take.",
    "You are writing for two readers. One is Sam Walker, who approves the plan. The other is "
    "whoever is on call at 3am when the Sydney region is unavailable and this is the document "
    "they open. Write for the second one.",
    "Work the tasks in order. They follow the sections of the YAT Disaster Recovery Plan "
    "template, so when you reach the last task the plan assembles from what you have already "
    "written — which is exactly how the assessment works, so it is worth feeling how that goes.",
]

RESOURCES = [
    ("LMS Global Expansion — Functional & Non-Functional Requirements — the recovery objectives "
     "YAT signed off on", f"{PROJECT}/requirements"),
    ("LMS Infrastructure Specifications — the environment, and the backup arrangements currently "
     "in place", f"{ICT}/lms-server-status-ha-hardened"),
    ("Deprecated on-premises DR Plan — superseded by the move to the cloud. Context for what an "
     "organisational plan looks like, not a model to copy", f"{ICT}/lms-dr-plan-onprem-deprecated"),
    ("Backup & Retention Policy — YAT's standing backup and retention obligations",
     f"{POLICY}/backup-retention"),
    ("Industry Standards — the information-security and continuity standards YAT works to",
     f"{REFERENCE}/industry-standards"),
    ("Records Management Policy — where a completed engagement document has to be lodged",
     f"{POLICY}/records-management"),
]

TEMPLATE_NOTE = ("You will need the YAT Disaster Recovery Plan template — the same one the "
                 "assessment uses. Download it from the intranet's Templates section. You do not "
                 "need it until the last task, but read its section headings before you start so "
                 "you can see where your answers land.")

# ---------------------------------------------------------------- the plan tasks

PLAN = [
    dict(n=20, title="The recovery requirements this plan has to meet",
         resources=[
             ("LMS Global Expansion — Functional & Non-Functional Requirements — the recovery "
              "objectives and the availability floor", f"{PROJECT}/requirements"),
             ("Engagement Role Brief — what MTS is engaged to deliver and what is out of scope",
              f"{PROJECT}/role-brief"),
         ],
         prompt="Establish what the plan is held to before you write any of it. Record the "
                "recovery requirements YAT has set, what business need each one comes from, and "
                "where you read it. A requirement you cannot attribute is one you have assumed.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Requirement", "What it is", "The business need behind it"],
                [["Scope",
                  "cloud infrastructure only — the DOODLE application, the India-cohort data and "
                  "end-user support stay with YAT",
                  "The role brief draws the line, and it belongs in the plan: a recovery plan "
                  "that quietly assumes someone else's team will do something has not planned "
                  "for it. Every other row in this table is a target; this one is a boundary."],
                 ["Recovery time objective", "", ""],
                 ["Recovery point objective", "", ""],
                 ["Availability floor", "", ""],
                 ["Recovery independent of the primary region", "", ""]]),
         consider=["RTO and RPO are both in the requirements document. Which is 'how long until "
                   "it is back' and which is 'how much work is lost'?",
                   "PC 1.1 in the real assessment says 'according to business needs'. For each "
                   "target, what is the sentence that starts 'because otherwise…'?",
                   "What does an LMS outage actually cost YAT? Think about which week of term it "
                   "happens in before you answer.",
                   "One of the requirements says recovery must not depend on the primary region. "
                   "That sounds obvious. What in the current environment quietly depends on it?"]),

    dict(n=21, title="Existing recovery arrangements",
         resources=[
             ("LMS Infrastructure Specifications — the backup arrangements in place today",
              f"{ICT}/lms-server-status-ha-hardened"),
             ("Backup & Retention Policy — YAT's standing obligations",
              f"{POLICY}/backup-retention"),
             ("Deprecated on-premises DR Plan — the plan the cloud migration superseded. Context "
              "only — do not copy it", f"{ICT}/lms-dr-plan-onprem-deprecated"),
         ],
         prompt="Determine what recovery arrangements already exist. Go through what is actually "
                "in place today and say what each one would and would not get you back. Be honest "
                "about the difference between a backup and a recovery plan.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Existing arrangement", "What it protects against", "What it does not cover"],
                [["The deprecated on-premises DR plan",
                  "nothing current — it was written for the on-premises LMS that no longer exists",
                  "It is in the resources list precisely so you can rule it out. Reading a "
                  "superseded document and saying why it does not apply is part of determining "
                  "what exists; skipping it and assuming is not."],
                 ["Multi-AZ database with automatic failover", "", ""],
                 ["Automated database backups, 7-day retention", "", ""],
                 ["Auto Scaling across two zones", "", ""],
                 ["EBS volumes holding course materials and submissions", "", ""]]),
         consider=["Every arrangement in that list is inside ap-southeast-2. Write the third "
                   "column for each one and watch the same answer appear five times.",
                   "Multi-AZ failover is very good at what it does. Name precisely what it does, "
                   "and then name what this plan is about.",
                   "Where are course materials and student submissions stored? Is there any "
                   "automated copy of them anywhere?",
                   "The infrastructure specification says region recovery 'is not provided for "
                   "and remains an open gap'. Is that a finding you can use, or one you should "
                   "check yourself?"]),

    dict(n=22, title="Vendor provisions and service level agreements",
         resources=[
             ("Master Services Agreement — the engagement's contractual frame",
              f"{PROJECT}/master-services-agreement"),
             ("Industry Standards — the provider commitments YAT works to",
              f"{REFERENCE}/industry-standards"),
         ],
         prompt="Identify what your cloud provider commits to, and what it does not. Record the "
                "service commitments that matter to this plan, and be clear about where the "
                "provider's responsibility ends and YAT's begins — that boundary is where your "
                "plan has to do the work.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Provision", "What the provider commits to", "What remains YAT's responsibility"],
                [["Incident communication", "status reporting during a service event",
                  "Noticing that the event affects the LMS, and deciding to invoke this plan. The "
                  "provider tells you a region is unwell; nobody but YAT can tell you what that "
                  "means for a class sitting an assessment."],
                 ["Compute service level", "", ""],
                 ["Managed database", "", ""],
                 ["Block storage durability", "", ""],
                 ["Regional isolation", "", ""]]),
         consider=["'Regions fail independently' is a provider commitment. What does YAT have to "
                   "have done in advance for that to be worth anything?",
                   "The managed database service takes backups automatically. Does it put them "
                   "anywhere you could reach if Sydney were gone?",
                   "If the provider's availability figure were YAT's recovery plan, this document "
                   "would be one page long. Why is it not?",
                   "The MSA is a contract between YAT and MTS, not between YAT and the cloud "
                   "provider. Does anything in it bear on recovery?"]),

    dict(n=23, title="Recovery objectives",
         prompt="State the recovery objectives this plan commits to, per component of the system "
                "you designed in Part A. Take the targets from task 20 as the requirement, then "
                "say what each component's objective is and why. Not everything needs the same "
                "objective — say where you differentiate, and why that is defensible.",
         given=1, blank_rows=7, exemplar=1,
         table=(["Component", "RTO", "RPO", "Why this objective"],
                [["Teacher marking and gradebook entry", "≤ 24 hours", "≤ 1 hour",
                  "Marking can wait a day; losing an hour of marking already entered is a real "
                  "cost to a real person. The two numbers do not have to move together, and "
                  "noticing that is the whole reason this table has two columns."],
                 ["Course content delivery", "", "", ""],
                 ["Assessment submission", "", "", ""],
                 ["Authentication (sign-in)", "", "", ""],
                 ["India activity-audit store", "", "", ""],
                 ["Attendance and student notes", "", "", ""]]),
         consider=["One figure for the whole system is the easy answer and the weaker one. Which "
                   "part of the LMS genuinely cannot wait four hours in submission week?",
                   "What is the RPO of something that holds no data of its own?",
                   "Authentication is a row here. If sign-in is not recovered, what is the "
                   "recovery time of everything else, whatever you wrote against it?",
                   "The India audit obligation does not pause because Sydney is having a bad day. "
                   "What does that mean for the store's objectives?",
                   "Every figure you write must be within the task 20 targets, or you have to say "
                   "why not."]),

    dict(n=24, title="The data you are protecting",
         resources=[
             ("LMS Application Specification — the data the LMS holds, its volume and its "
              "sensitivity", f"{ICT}/lms-application-spec-cloud"),
             ("Privacy / Data Handling Policy — the classification and handling obligations",
              f"{POLICY}/privacy"),
         ],
         prompt="Estimate what data this system holds, how much of it there is, and how sensitive "
                "each kind is. Volume drives how long a recovery takes; sensitivity drives how "
                "carefully it has to be handled while you are recovering it.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Data", "Approximate volume", "Sensitivity", "What that means for recovery"],
                [["Published course materials", "the bulk of the file storage", "Internal",
                  "Large, and it is what makes a restore take hours rather than minutes. Nothing "
                  "about handling it is delicate — which is exactly why it belongs in a different "
                  "row from the next four."],
                 ["Student assessment submissions", "", "", ""],
                 ["Gradebook and unit completion records", "", "", ""],
                 ["Attendance and student notes", "", "", ""],
                 ["India activity-audit records", "", "", ""]]),
         consider=["The infrastructure specification gives you an annual growth figure for the "
                   "database. Is that the same as the total volume you have to move?",
                   "Which of these is personal information, and which is an academic record? They "
                   "carry different obligations and a plan that lumps them together has not done "
                   "the task.",
                   "Teacher notes about a student are the most sensitive thing in the list and "
                   "the smallest. Does volume or sensitivity decide how carefully you handle "
                   "them?",
                   "One category must not be recovered into your DR region at all. Which one, and "
                   "what does DR-R1 say?"]),

    dict(n=25, title="Risk assessment — the major risk events",
         resources=[
             ("Security & Incident Response Policy — how YAT classifies and responds to incidents",
              f"{POLICY}/security-incident"),
         ],
         prompt="Identify the major risk events this plan is written for. You need at least "
                "three. For each, say how likely it is, what the impact on YAT would be, and how "
                "you rated it — name the method you used, because a rating with no method behind "
                "it is an opinion.",
         given=1, blank_rows=7, exemplar=1,
         table=(["Risk event", "Likelihood", "Impact on YAT", "Rating"],
                [["Loss of the campus link carrying AD-LDAP authentication", "Possible",
                  "Nobody can sign in. The LMS is running perfectly and is useless to every "
                  "student and teacher at once — an impact worth stating in those terms rather "
                  "than as 'authentication unavailable'.",
                  "High"],
                 ["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""],
                 ["", "", "", ""]]),
         consider=["Three is the floor, not the target. Work down the architecture and ask what "
                   "would take the LMS out at each layer.",
                   "The obvious one is the loss of the Sydney region. What are the ones that are "
                   "far more likely and still serious?",
                   "'Impact on YAT' is not 'the database is unavailable'. Who cannot do what, and "
                   "when does it hurt most?",
                   "How did you decide one risk is High and another Medium? Whatever you did has "
                   "a name — write it down, because you will be asked.",
                   "The exemplar row is an authentication risk. The public website has no "
                   "equivalent. What else about the LMS is unlike a public website?"]),

    dict(n=26, title="Plan exclusions",
         prompt="Say what this plan does not cover, and why each exclusion is defensible against "
                "the business requirements. An exclusion is a decision you are accountable for — "
                "it is not the same as something you forgot.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Excluded from this plan", "Why", "Who does own it"],
                [["Recovery of individual staff and student devices",
                  "not part of the LMS service — a student with a broken laptop is a service-desk "
                  "matter, not a disaster",
                  "YAT ICT service desk. Note the shape of the row: what, why, and who instead. "
                  "An exclusion with no owner is an orphan, not a decision."],
                 ["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""]]),
         consider=["Go back to the role brief. What did YAT keep for itself? Each of those is a "
                   "candidate exclusion.",
                   "The DOODLE application itself — is recovering it in scope for this plan, and "
                   "what does the engagement scope say?",
                   "The campus network and the AD-LDAP directory sit on YAT's side. Are they "
                   "excluded, or are they a dependency you have to name in task 32?",
                   "An exclusion you cannot justify against a requirement is a gap wearing a "
                   "disguise. Read yours back and check each one."]),

    dict(n=27, title="Record the outcomes of the impact analysis",
         resources=[
             ("Records Management Policy — how analysis outcomes are recorded and retained",
              f"{POLICY}/records-management"),
             ("Change Management Procedure — the governance a production-affecting plan sits "
              "under", f"{POLICY}/change-management"),
         ],
         prompt="Your analysis in tasks 23 to 26 has to be recorded in a way YAT can act on and "
                "audit later. Say what gets recorded, where it is held, who owns it, and when it "
                "is reviewed — according to YAT's policies, not your preference.",
         given=1, blank_rows=5, exemplar=1,
         table=(["What is recorded", "Where it is held", "Owner", "Reviewed when"],
                [["Data volumes and classifications", "with the lodged DR plan", "YAT ICT",
                  "annually, or whenever the data profile changes. The trigger matters more than "
                  "the frequency — 'annually' alone means a change made in March is wrong until "
                  "December."],
                 ["Risk register and ratings", "", "", ""],
                 ["Recovery objectives per component", "", "", ""],
                 ["Plan exclusions and their justification", "", "", ""]]),
         consider=["The Records Management Policy says where an engagement document is lodged and "
                   "how long it is kept. Have you read it, or are you writing what sounds "
                   "sensible?",
                   "Who owns a record? Name a role, not a team — 'ICT' cannot review anything.",
                   "What would trigger a review other than the calendar? There is at least one "
                   "obvious event.",
                   "This task is the difference between analysis that informs a decision and "
                   "analysis that is filed and forgotten. Which is yours?"]),

    dict(n=28, title="Recovery options evaluated",
         resources=[
             ("Reference Architectures — the recovery patterns YAT's architects work from",
              f"{REFERENCE}/reference-architectures"),
         ],
         prompt="Develop a range of recovery solutions — not one. For each, say what it would "
                "cost YAT to run, what recovery time it would actually achieve, and what it would "
                "not do. You are building the comparison your recommendation in the next task "
                "rests on.",
         given=1, blank_rows=5, exemplar=1,
         table=(["Option", "How it works", "Realistic RTO", "Cost posture"],
                [["Do nothing beyond today's arrangements",
                  "rebuild by hand from whatever backups exist inside the lost region",
                  "Indefinite — you cannot reach the backups, so there is no honest number to "
                  "write here.",
                  "nil, until the day it is not"],
                 ["Backup and restore", "", "", ""],
                 ["Pilot light", "", "", ""],
                 ["Warm standby", "", "", ""],
                 ["Multi-site active/active", "", "", ""]]),
         consider=["There are four recognised cloud recovery techniques. Name all four and then "
                   "argue — a recommendation with nothing beside it is a preference.",
                   "For each option, what actually exists in the second region on an ordinary "
                   "Tuesday? That is what decides both the cost and the recovery time.",
                   "The LMS runs on a Windows AMI with DOODLE pre-installed. For each option, ask "
                   "whether that image is already in the second region — and what it costs you if "
                   "it is not.",
                   "'Realistic RTO' means the time it would really take, including the bit where "
                   "someone has to be woken up. Not the marketing figure."]),

    dict(n=29, title="The recommended approach",
         prompt="Recommend one of the options from task 28 and align it to the business "
                "requirement. Say why it is the right level of protection for this system — not "
                "the most protection available. Name the option you would choose if the "
                "requirements changed, and what change would make you switch.",
         # No exemplar row: all four rows are the recommendation the task exists to ask for.
         given=1, blank_rows=4,
         table=(["Decision", "Your answer", "Why"],
                [["Recommended strategy", "", ""],
                 ["Why not the cheaper option", "", ""],
                 ["Why not the stronger option", "", ""],
                 ["What would change the recommendation", "", ""]]),
         consider=["Aligning to the requirement cuts both ways. Recommending the strongest option "
                   "available is as much a failure to align as recommending the weakest.",
                   "Check your recommendation against your own task 23 numbers. Does it reach "
                   "them? Does it overshoot them, and whose money is that?",
                   "Cost-effectiveness was a stated requirement. Where in this table do you "
                   "address it?",
                   "If Sam Walker asked 'why not the cheap one?', you need one sentence. Write "
                   "that sentence."]),

    dict(n=30, title="Vendor protections and risk prioritisation",
         prompt="Come back to the provider protections you identified in task 22, now that you "
                "have a strategy. For each risk event from task 25, say what the provider already "
                "covers, what your plan has to cover, and in what order you would deal with them.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Risk event", "Provider protection", "What your plan must add", "Priority"],
                [["Accidental deletion of infrastructure by a change",
                  "none — this is a YAT action, not a provider event",
                  "Change discipline, and infrastructure defined as code so what was deleted can "
                  "be rebuilt from a file rather than from memory. Not every risk has a provider "
                  "protection, and saying 'none' is a finding.",
                  "your call"],
                 ["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]),
         consider=["Copy your task 25 risks into the first column. Same list, no new ones.",
                   "Priority is not the same as likelihood. What would you deal with first, and "
                   "what makes that the right order?",
                   "Where the provider covers something entirely, your plan's job is to say so "
                   "and move on. Where it covers nothing, that is where the work is.",
                   "Does your priority order agree with your task 25 ratings? If not, one of them "
                   "is wrong."]),

    dict(n=31, title="Insurance",
         prompt="Assess whether external insurance protection is appropriate here, and at what "
                "level. This is a real question with a real answer either way — say what you "
                "would recommend to YAT and on what basis. If your answer is that it sits outside "
                "your scope, say who it belongs to and what you would tell them.",
         given=1, blank_rows=5, exemplar=1,
         table=(["Cover type", "What it would protect", "Suitability here"],
                [["Provider service credits",
                  "a partial refund of service charges for a breached service level",
                  "Included as a trap worth spotting: service credits are not insurance. They do "
                  "not restore the LMS and they do not cover what the outage cost YAT."],
                 ["Cyber liability", "", ""],
                 ["Business interruption", "", ""],
                 ["Recommendation to YAT", "", ""]]),
         consider=["The LMS holds student personal information and academic records. Does that "
                   "point at one kind of cover more than another?",
                   "What is YAT's actual financial loss when the LMS is down for a day? It is not "
                   "obvious, and that is the interesting part.",
                   "'Out of scope' is a legitimate answer if you say whose it is and what they "
                   "need to know. It is not a legitimate way to skip the question.",
                   "MTS advises on the technical exposure. Who decides on cover?"]),

    dict(n=32, title="Other recovery components",
         prompt="A recovery plan is more than infrastructure. Identify the other components this "
                "plan needs to work at 3am — the people, the access, the contacts, the "
                "communications, and anything else without which the technical steps cannot be "
                "carried out.",
         given=1, blank_rows=7, exemplar=1,
         table=(["Component", "What it is", "Why the plan fails without it"],
                [["An off-region copy of this plan",
                  "the document itself, readable when Sydney is unavailable",
                  "If the only copy of the recovery plan is in the environment that has failed, "
                  "there is no plan. It is the most embarrassing failure mode in this task and it "
                  "is genuinely common."],
                 ["Invocation authority", "", ""],
                 ["Access to the second region", "", ""],
                 ["Contact list", "", ""],
                 ["Stakeholder communications", "", ""],
                 ["DNS control", "", ""]]),
         consider=["Who is allowed to declare a disaster? If the answer is 'someone will', the "
                   "clock runs while people wait for each other.",
                   "Every LMS user authenticates against AD-LDAP through the campus link. What "
                   "has to be true for anyone to sign in to a recovered LMS in another region? "
                   "This one is specific to the LMS and it is easy to miss.",
                   "Who tells students the LMS is down in submission week, and what do they say "
                   "about the deadline?",
                   "Recovery needs credentials that work when the primary region does not. Where "
                   "do those live today?",
                   "Aim for more rows than the technical ones. The technical steps are the easy "
                   "half."]),

    dict(n=33, title="Detection and alerting",
         prompt="A recovery plan starts when someone finds out. Say how a region-level disaster "
                "affecting this LMS would be detected, what would alert whom, and how long you "
                "would expect detection to take. Remember detection has to work from outside the "
                "region that has failed.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Signal", "What raises it", "Who is alerted", "Expected detection time"],
                [["Detection counts against the RTO",
                  "the clock starts at the event, not at the alert", "—",
                  "Not a signal at all — a reminder placed in the table so it is not forgotten. "
                  "Twenty minutes of nobody noticing is twenty minutes of your four hours."],
                 ["External endpoint health check", "", "", ""],
                 ["Edge origin errors", "", "", ""],
                 ["Provider service health notification", "", "", ""],
                 ["Students and teachers reporting they cannot sign in", "", "", ""]]),
         consider=["If your monitoring runs inside ap-southeast-2, what tells you ap-southeast-2 "
                   "is gone?",
                   "The last row of the exemplar table lists users as a detection signal. It is a "
                   "real one. Is it a good one, and what is its detection time?",
                   "Out of hours, who receives the alert? A dashboard nobody is looking at is not "
                   "detection.",
                   "The provider publishes service health. Would you rely on it as your trigger? "
                   "Why not?"]),

    dict(n=34, title="The recovery steps",
         prompt="Write the recovery steps for your recommended strategy — what is actually done, "
                "in order, by whom, and how long each step takes. This is the section someone "
                "follows under pressure. Number the steps, give each a duration, and make the "
                "total add up to less than your RTO.",
         given=1, blank_rows=10, exemplar=1,
         table=(["#", "Step", "Who", "Duration"],
                [["1", "Confirm the event and declare a disaster",
                  "on-call YAT ICT → Sam Walker",
                  "15 min. Note the shape: a step names an action, a role and a duration. Every "
                  "row below yours has to do the same, or the total cannot be added up."],
                 ["2", "", "", ""], ["3", "", "", ""], ["4", "", "", ""], ["5", "", "", ""],
                 ["6", "", "", ""], ["7", "", "", ""], ["8", "", "", ""]]),
         consider=["Write the steps in the order someone would actually do them, then check "
                   "whether any of them can run at the same time.",
                   "Somewhere in your sequence, the application tier has to exist in the second "
                   "region. What does that take, given it is a Windows image with DOODLE "
                   "installed?",
                   "Somewhere else, users have to be able to sign in. Where is that step, and how "
                   "long does it take?",
                   "Course materials and submissions are on block storage. What is the step that "
                   "gets them there, and is its duration honest for the volume from task 24?",
                   "Add your durations up. If the total exceeds your RTO, change the plan — do "
                   "not change the objective."]),

    dict(n=35, title="How the plan meets the recovery objectives",
         prompt="Show that your plan actually achieves the objectives you set in task 23. Add up "
                "your recovery steps against the RTO, and explain what mechanism delivers the "
                "RPO. If the numbers do not work, change the plan — do not change the objective.",
         given=1, blank_rows=5, exemplar=1,
         table=(["Objective", "Target", "What the plan achieves", "The mechanism"],
                [["India log residency during recovery", "maintained",
                  "logs recover into an Indian region, never into the DR region",
                  "The audit store is deployed separately and parameterised by region — which is "
                  "why Part A's DR-R4 answer matters here. An objective can be met by a design "
                  "decision rather than by a recovery step."],
                 ["RTO", "", "", ""],
                 ["RPO", "", "", ""],
                 ["Course materials", "", "", ""]]),
         consider=["The RTO row needs arithmetic, not an assertion. Sum of steps, plus detection, "
                   "versus the target.",
                   "What mechanism actually delivers your RPO? Nightly backups do not deliver one "
                   "hour, whatever the plan says.",
                   "If your numbers do not reach the target, the honest move is to go back to "
                   "task 34 or task 29. Say what you changed.",
                   "Which objective is the hardest to meet for the LMS specifically? Write that "
                   "row first."]),

    dict(n=36, title="The standards this plan reflects",
         resources=[
             ("Industry Standards — the information-security and continuity standards YAT works "
              "to", f"{REFERENCE}/industry-standards"),
         ],
         prompt="Name the information-security and business-continuity standards that informed "
                "this plan, and for each say where it shows up in what you have written. A "
                "standard you cannot point to in your own plan is one you have listed rather than "
                "applied.",
         given=1, blank_rows=4, exemplar=1,
         table=(["Standard", "What it covers", "Where it shows up in your plan"],
                [["ISO/IEC 27031",
                  "ICT readiness for business continuity — the standard closest to this document",
                  "Your recovery objectives, your strategy and your step-by-step plan. The third "
                  "column is the point of the task: naming a standard is listing, pointing at "
                  "your own task numbers is applying."],
                 ["ISO/IEC 27001", "", ""],
                 ["ISO/IEC 27002", "", ""]]),
         consider=["There is a recognised trio of standards here and they are all in the Industry "
                   "Standards reference. Which is the management system, which is the control "
                   "set, and which is continuity?",
                   "For each, find a task number in your own plan to point at. If you cannot, you "
                   "have listed it.",
                   "Is there anything in your plan that a standard would say you have missed?"]),

    dict(n=37, title="Assemble the Disaster Recovery Plan",
         prompt="Now build the document. Open the YAT Disaster Recovery Plan template and copy "
                "your answers across using the map below — your work is done, this is "
                "transcription. Write the Executive Summary last, once you can see the whole "
                "plan. This is practice, so nothing is submitted; do it anyway, because the "
                "assessment version of this task is worth an hour you will not have.",
         given=2, blank_rows=18,
         table=(["Template section", "Comes from", "Done"],
                [["1. Executive Summary", "written last, from the whole plan", ""],
                 ["2. Engagement Context and Scope", "task 20, and the Part A engagement framing",
                  ""],
                 ["3.1 Existing recovery arrangements", "task 21", ""],
                 ["3.2 Vendor provisions and SLAs", "task 22", ""],
                 ["4.1 Recovery objectives (RTO / RPO)", "task 23", ""],
                 ["4.2 Data managed", "task 24", ""],
                 ["4.3 Risk assessment", "task 25", ""],
                 ["4.4 Plan exclusions", "task 26", ""],
                 ["4.5 Recording the analysis", "task 27", ""],
                 ["5.1 Options evaluated", "task 28", ""],
                 ["5.2 Recommended approach", "task 29", ""],
                 ["5.3 Vendor protections and risk prioritisation", "task 30", ""],
                 ["5.4 Insurance", "task 31", ""],
                 ["5.5 Other recovery components", "task 32", ""],
                 ["6.1 Detection and alerting", "task 33", ""],
                 ["6.2 Recovery steps", "task 34", ""],
                 ["6.3 Meeting the recovery objectives", "task 35", ""],
                 ["7. Plan Validation and Approval", "completed at your Part C walkthrough", ""]]),
         clicks=["Download the YAT Disaster Recovery Plan template from the intranet's Templates "
                 "section and save it under a name of your own.",
                 "Fill in the document control table at the front — title, owner, prepared by, "
                 "classification. It is the first thing a reader sees and the easiest thing to "
                 "leave on the template's placeholder text.",
                 "Work down the map above, one row at a time. Open the task it names, and move "
                 "the answer across.",
                 "Where a task produced a table, keep it a table. Do not turn it into prose — the "
                 "person reading this at 3am wants a table.",
                 "Where a task produced a written answer, it goes in as written. This is the part "
                 "that is transcription rather than translation, and it is only true because the "
                 "tasks were ordered to match the template.",
                 "Write the Executive Summary last. Half a page: what the plan covers, the "
                 "strategy, the objectives it meets, and what it excludes.",
                 "Read the finished document end to end as if you had not written it. Anything "
                 "that only makes sense if you remember the worksheet needs a sentence around "
                 "it."],
         consider=["Time this task. The assessment version is the same job on a bigger plan, and "
                   "students routinely underestimate it.",
                   "Does your assembled plan still contain at least three major risk events? "
                   "Check, because the assessment's does not pass without them.",
                   "Would the on-call person at 3am be able to follow section 6.2 without ringing "
                   "you? That is the only test that matters.",
                   "Compare the plan against the worksheet. If the plan says something the "
                   "worksheet does not, where did it come from?"]),
]
