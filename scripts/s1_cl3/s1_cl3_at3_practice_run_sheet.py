#!/usr/bin/env python3
"""The S1-CL3 AT3 PRACTICE deployment run sheet — content.

Same shape as the AT3 assessment workbook, on the public website rather than Ledgerline. The
starting point is `delivery/practice-lab-pack/baseline.yaml`, which builds the single-AZ
website environment the practice design exercise analysed.

THE ONE STRUCTURAL DIFFERENCE, and it is deliberate: the assessment's lab-pack ships a
reference improved template so a student is never blocked by their team's work. The practice
pack ships **only the baseline** — the improvement applied here is the student's own, carried
forward from the practice design and team-build exercises. Practice is where being blocked by
your own unfinished template is a lesson rather than an assessment problem.

WHAT ELSE DIFFERS, and why an answer here does not transfer:

  the system        a public, internet-facing site on MySQL — not an internal finance system
                    on PostgreSQL behind a campus VPN
  the before state  ONE EC2 instance with no load balancer and no Auto Scaling group. The
                    Ledgerline baseline already has both. So the first improvement here is
                    building a tier, not widening one.
  the database      MySQL carries no legacy single-instance constraint, so whether it becomes
                    Multi-AZ is genuinely the student's call — argued on goals and cost.
  the test that     reliability is demonstrated against a public 24x7 audience; the scaling
  matters           event is the intake window, not month-end close.
  build time        about 15 minutes for the baseline — MySQL builds faster than the
                    assessment's SQL Server.

WHAT PRACTICE ADDS: click-by-click steps on every task that touches the console, and "Things
to consider" leading questions on the tasks that ask for judgement.

No marking criteria, no UoC tags. Rendered by the assessment's own renderer in
s1_cl3_at3_run_sheet, with these lists passed in.
"""

SITE = "https://yat.timbaird.com"
STATE = "s1-cl3-at3"
PROJECT = f"{SITE}/intranet/{STATE}/projects/website-improvement"
ICT = f"{SITE}/intranet/{STATE}/ict"
POLICY = f"{SITE}/intranet/{STATE}/policies"

# ---------------------------------------------------------------- front matter

SCENARIO = [
    "Your improvement design was approved and your team has encoded it as infrastructure as code. "
    "This is the deployment phase: you stand the environment up, apply the approved improvement, "
    "prove it does what you said it would, and hand it over.",
    "You are an MTS Consultant reporting to Pat Lin (MTS Senior Consultant). Sam Walker (YAT ICT "
    "Manager) accepts the completed work. The website is a public 24x7 front door, so your work "
    "happens inside a maintenance window and outside the Peak Intake Period.",
    "This is practice. Nothing here is assessed and nothing is submitted. It is the same work the "
    "assessment will ask for, on a different system with a different starting point — including "
    "one thing the assessment does not do to you: there is no reference improved template here. "
    "The improvement you apply is your own.",
]

RESOURCES = [
    ("Improvement Requirements — the outcomes IR-1 to IR-7 the deployed result is judged against",
     f"{PROJECT}/improvement-requirements"),
    ("Website Infrastructure Specifications — the baseline you are deploying and improving",
     f"{ICT}/website-server-status"),
    ("Change Management Procedure — the governance a production-affecting change sits under, and "
     "the Peak Intake Period", f"{POLICY}/change-management"),
    ("Records Management Policy — where completed engagement documentation is filed",
     f"{POLICY}/records-management"),
]

INSTRUCTIONS = [
    "Work the tasks in order. Task 1 deploys the baseline; everything after it improves and proves "
    "that environment.",
    "Every task that touches the console tells you where to click. The assessment will not — so "
    "pay attention to WHERE things are, not just what you clicked.",
    "Take a screenshot at the end of each task even though this is not assessed. In the assessment "
    "you need one per task, and building the habit here is the point.",
    "Tasks 5 to 8 ask you to demonstrate, not to assert. Make something happen and record what you "
    "observed. A test with no observation is not a test.",
    "You need your own improved template for task 3. If it is not finished, finish it first — "
    "being blocked here is the lesson, and it is much better learned now than in the assessment.",
    "Delete your stacks when you finish a session.",
]

REGION_NOTE = ("The scenario places the website in Sydney — [scenario: ap-southeast-2 | deploy: "
               "us-east-1]. Build in us-east-1 in the AWS Academy Learner Lab. Where a task refers "
               "to availability zones, read the first two zones of whichever region you are in.")

# ---------------------------------------------------------------- the tasks

TASKS = [
    dict(n=1, title="Deploy the baseline environment",
         prompt="Deploy the practice baseline template. This builds the current single-AZ website "
                "environment — the state your design analysis was written against. Confirm it came "
                "up before you change anything, because everything after this is measured against "
                "it.",
         given=1, blank_rows=5, exemplar=1,
         table=(["Step", "What you did", "Result"],
                [["Recorded the before state",
                  "one instance, no load balancer, single-AZ MySQL, media on the instance disk",
                  "This row is the one that makes tasks 4 to 8 possible. Write down what the "
                  "environment IS before you change it, or you will have nothing to compare "
                  "against and will end up asserting the improvement instead of showing it."],
                 ["Deployed the baseline template", "", ""],
                 ["Tooling used", "console or CLI — name it", ""],
                 ["Confirmed the site responds", "", ""]]),
         clicks=["Start the AWS Academy Learner Lab and open the console. Check the region reads "
                 "N. Virginia (us-east-1) before anything else.",
                 "Get baseline.yaml from the practice lab-pack your teacher points you at.",
                 "CloudFormation → Create stack → With new resources (standard) → Upload a "
                 "template file → select baseline.yaml → Next.",
                 "Stack name: yat-website-baseline. Set DBMasterPassword — 8+ characters, and "
                 "write it down, because you are not shown it again.",
                 "Next, Next, Submit. It takes about 15 minutes; the database is most of that.",
                 "When it reads CREATE_COMPLETE, open the Outputs tab and click SiteUrl. The "
                 "placeholder page should load — this one is public, unlike Ledgerline.",
                 "Screenshot the stack at CREATE_COMPLETE and the page loading."],
         consider=["Before you move on: what exactly is the 'before' you will be comparing "
                   "against? Write it down now rather than reconstructing it later.",
                   "How many instances are serving the site? Is there anything in front of them?",
                   "Check RDS: is the database Multi-AZ? That answer is your starting point, not "
                   "your ending one."],
         evidence=["the baseline stack deployed, and the site responding"]),

    dict(n=2, title="Record your approved scope",
         prompt="Before you deploy anything else, write down what you are actually authorised to "
                "build. Copy the approved improvements from your design exercise sign-off. If "
                "something you proposed was not approved, it does not get deployed here — record "
                "it as out of scope so the difference is deliberate rather than forgotten.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Improvement", "Approved?", "In scope for this deployment"],
                [["Re-platforming the CMS", "No — never proposed",
                  "Out of scope. Listing something you deliberately did NOT propose is not "
                  "padding: it is what stops the scope quietly growing while you are in the "
                  "console and something looks easy to add."],
                 ["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""]]),
         consider=["Open your design worksheet at the sign-off task and copy from it. Do not work "
                   "from memory — the point of the sign-off was that it is the record.",
                   "Is there anything you are tempted to add now that nobody approved? That "
                   "temptation is exactly what this task exists to catch.",
                   "If your approved list is vague — 'improve reliability' — you have found a "
                   "defect in your own earlier work. Note it; it is a useful thing to have "
                   "learned here rather than there."]),

    dict(n=3, title="Apply the approved improvement",
         prompt="Apply your approved improvement to the running baseline as an update — not by "
                "tearing it down and rebuilding. Updating a live environment is what YAT would "
                "actually experience, and it is where the interesting problems are. Record each "
                "attempt.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Attempt", "What you applied", "What happened", "What you changed"],
                [["1", "your improved template", "the change set previewed a replacement you did "
                                                 "not intend",
                  "Yours will differ. Record the failures rather than tidying them away — task 9 "
                  "and the write-up both need them, and a first attempt that worked perfectly is "
                  "rarer than students think."],
                 ["2", "", "", ""], ["3", "", "", ""],
                 ["Final", "", "", ""],
                 ["What the update did to existing resources", "", "", ""]]),
         clicks=["Select your stack in CloudFormation → Update → Replace existing template → "
                 "Upload a template file → your own improved template → Next.",
                 "Work through to the review page. Before you submit, look at the CHANGE SET "
                 "PREVIEW — it lists every resource as Add, Modify or Remove.",
                 "Read the Replacement column. 'True' means the resource is destroyed and "
                 "recreated. On a database that is your data gone.",
                 "If something shows a replacement you did not intend, cancel, fix the template, "
                 "and try again. This is the whole reason the preview exists.",
                 "Submit, and watch the Events tab.",
                 "If it rolls back, scroll to the FIRST red row for the cause — everything under "
                 "it is the rollback.",
                 "Screenshot the completed update and the Resources tab."],
         consider=["What did the update do to the resources that already existed — modified, "
                   "replaced, or left alone? The Events tab tells you, and it is the interesting "
                   "part of this task.",
                   "Did anything get replaced? Was that intended? What would that have meant on a "
                   "production site with real content?",
                   "The site should still be serving while you did this, or should have come back "
                   "quickly. Did you check, or did you only watch CloudFormation?"],
         evidence=["the update completing, and the resources it changed"]),

    dict(n=4, title="Monitor and measure against your metrics",
         prompt="Measure the improved environment against the performance metrics and business "
                "goals you set in the design exercise. For each metric, record what you measured, "
                "what the target was, and whether it is met. Where a metric cannot be measured "
                "yet, say what would be needed — that is a finding, not a failure.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Metric (from your design)", "Target", "What you measured", "Met?"],
                [["Healthy targets behind the load balancer", "at least one in each zone",
                  "Whatever the target group actually shows. Note the third column asks what you "
                  "MEASURED — a number or a state you observed, not 'yes'."],
                 ["", "", "", ""], ["", "", "", ""], ["", "", "", ""],
                 ["", "", "", ""], ["", "", "", ""]]),
         clicks=["EC2 → Target Groups → your target group → the Targets tab shows each target, its "
                 "zone and its health.",
                 "CloudWatch → All metrics → by service, for request counts, error counts and "
                 "instance metrics.",
                 "CloudWatch → Alarms shows anything you configured, and its current state.",
                 "For cost: the Billing console, or the cost figures on the resources themselves. "
                 "In a lab the absolute numbers are not meaningful — the comparison is.",
                 "Screenshot each measurement as you take it."],
         consider=["Use YOUR metrics from the design exercise, not new ones invented now. If they "
                   "turn out to be unmeasurable, that is a finding worth recording.",
                   "A metric marked 'met' with no observed value beside it evidences nothing.",
                   "Which of your metrics genuinely cannot be measured in a lab? Say what would be "
                   "needed in a real environment."],
         evidence=["your monitoring showing the measurements you recorded"]),

    dict(n=5, title="Test and demonstrate reliability",
         prompt="Demonstrate that the environment is more reliable than the baseline was. Make a "
                "failure happen — terminate an instance, or fail over whatever you improved — and "
                "record what the service did while it was happening. If your approved improvement "
                "did not touch reliability, test the reliability you have and say so.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Test", "What you did", "What you expected", "What actually happened"],
                [["Service during the failure", "kept reloading the site throughout",
                  "brief or no interruption",
                  "The row people skip, and the only one that shows the improvement was worth "
                  "anything. Terminating an instance proves the group replaces it; requesting the "
                  "site throughout proves a visitor did not notice."],
                 ["Instance failure", "", "", ""],
                 ["Recovery", "", "", ""],
                 ["Zone-level behaviour", "", "", ""],
                 ["Database behaviour", "", "", ""]]),
         clicks=["Open the site in a browser tab first and set it reloading — you need to watch it "
                 "during the failure, not after.",
                 "EC2 → Instances → select one of your application instances → Instance state → "
                 "Terminate.",
                 "Watch the target group: the terminated target goes unhealthy and is removed.",
                 "Watch your browser tab. Does the site keep serving? If it does not, that is a "
                 "finding, not a mistake.",
                 "EC2 → Auto Scaling groups → Activity tab shows the group noticing and launching "
                 "a replacement. Note the time it takes.",
                 "Wait for the replacement to become healthy in the target group.",
                 "Screenshot the failure, the site still serving, and the recovered state."],
         consider=["What did a visitor experience? That is the question the whole improvement was "
                   "for.",
                   "How long from termination to a healthy replacement? Compare that with the "
                   "recovery goal you set.",
                   "If your design spans two zones, did the surviving zone carry the load on its "
                   "own? What does that say about your minimum capacity?",
                   "If you made the database Multi-AZ, can you demonstrate a failover — and if you "
                   "did not, what does that mean for your recovery number?"],
         evidence=["the failure you induced",
                   "the site continuing during it",
                   "the environment after recovery"]),

    dict(n=6, title="Test and demonstrate security",
         resources=[
             ("Security & Incident Response Policy — the obligations the environment is held to",
              f"{POLICY}/security-incident"),
         ],
         prompt="Demonstrate the security position of the deployed environment. Show the controls "
                "working rather than listing them — that the paths you intended to be closed are "
                "closed, and that anything you improved is actually in effect.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Control", "How you tested it", "What you observed"],
                [["Database reachable only from the application tier",
                  "tried to connect to the database endpoint from outside the tier",
                  "A refused connection is the evidence. A screenshot of the security group rule "
                  "shows configuration; making the connection fail shows behaviour, and behaviour "
                  "is what this task asks for."],
                 ["Public ingress reaches only what it should", "", ""],
                 ["Administrative access", "", ""],
                 ["Transport encryption, if you improved it", "", ""],
                 ["Storage encryption", "", ""]]),
         clicks=["For the database: from CloudShell or your own machine, try to reach the RDS "
                 "endpoint on port 3306. It should refuse or time out.",
                 "For public ingress: the site itself should answer on the load balancer. Try "
                 "reaching an application instance's private address directly — it should not "
                 "answer.",
                 "For TLS, if you added it: load the site over HTTPS and check the certificate. "
                 "Then check what happens on HTTP — does it redirect, or does it still serve?",
                 "RDS → your database → Configuration tab shows encryption at rest.",
                 "Screenshot each attempt and its result, including the failures — the failures "
                 "ARE the evidence here."],
         consider=["This site is public by design. What SHOULD be reachable from the internet, and "
                   "what should not?",
                   "A control you cannot demonstrate failing is a control you have not tested.",
                   "If you added filtering for bots or form abuse, how would you show it working?",
                   "Anything you improved in the design should be visibly in effect here. Is it?"],
         evidence=["a connection attempt being refused where it should be",
                   "the security improvement you deployed, in effect"]),

    dict(n=7, title="Test and demonstrate scalability",
         prompt="Demonstrate that the environment scales. The website's real scaling event is the "
                "intake window, so make the tier scale — generate load, or change the desired "
                "capacity — and record what happened and how long it took.",
         given=1, blank_rows=5, exemplar=1,
         table=(["Test", "What you did", "What happened", "How long it took"],
                [["Service during scale-out", "kept requesting the site throughout",
                  "Uninterrupted, ideally. Same principle as the reliability test: the scaling "
                  "event is only interesting if you can say what a visitor experienced while it "
                  "happened."],
                 ["Scale out", "", "", ""],
                 ["Scale in", "", "", ""],
                 ["Behaviour against the intake profile", "", "", ""]]),
         clicks=["The reliable route in a lab: EC2 → Auto Scaling groups → your group → Edit → "
                 "raise Desired capacity → Update. Watch the Activity tab.",
                 "The realistic route: generate load against the site until the scaling policy "
                 "triggers. More convincing, slower, and it may not trigger inside a lab session.",
                 "Either way, time it. Note when the new instance launches and when it becomes "
                 "healthy in the target group — those are different moments.",
                 "Scale back in the same way and watch what the group removes.",
                 "Screenshot the group before and after, and the Activity history."],
         consider=["Which route did you use, and what does the other one cost you in evidence?",
                   "How long from the scaling decision to a target actually serving traffic? Is "
                   "that fast enough for an intake-window surge?",
                   "IR-7 forbids production change during the intake window. So the scaling has to "
                   "work on its own, with nobody touching it. Does yours?",
                   "What happens on scale-in — could a visitor be mid-request on an instance being "
                   "removed?"],
         evidence=["the scaling event, showing the group before and after"]),

    dict(n=8, title="Test and demonstrate cost optimisation",
         resources=[
             ("Website Operational Costing — the cost basis you compared against in the design",
              f"{ICT}/website-operational-costing"),
         ],
         prompt="Demonstrate the cost position of what you deployed. Show what the improvement "
                "actually costs to run against what you estimated, and show any cost measure you "
                "designed working — right-sizing, an origin-offloading layer, or a budget alert.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Item", "Your estimate", "What you deployed", "Observed position"],
                [["Net position against your cost goal", "", "",
                  "Finish this row last, and finish it honestly. 'This costs more than I estimated "
                  "and here is why' is a good answer; the estimate being right is not what is "
                  "interesting."],
                 ["Additional compute", "", "", ""],
                 ["Load balancing", "", "", ""],
                 ["Database", "", "", ""],
                 ["Cost measure in effect", "", "", ""]]),
         clicks=["Compare what is now running against the baseline you recorded in task 1 — count "
                 "instances, and list anything new that bills by the hour.",
                 "If you designed a budget alert: Billing → Budgets shows it, and whether it has "
                 "fired.",
                 "If you designed right-sizing: show the instance types you actually deployed "
                 "against what you proposed.",
                 "Screenshot whichever cost measure you designed, in effect."],
         consider=["This site has to answer around the clock, so whatever cost measure you "
                   "designed had to work without turning anything off. What did you do, and "
                   "did it work?",
                   "Is anything running that nothing needs? That is a finding.",
                   "Lab dollar figures are not meaningful. The comparison against your estimate "
                   "is. Reason in relative terms."],
         evidence=["the cost measure you designed, working"]),

    dict(n=9, title="Apply short-term refinements",
         prompt="Your tests will have found something — a threshold set too tight, a missing alarm, "
                "a health check slower than it needs to be, capacity that is wrong. Apply the "
                "refinements your own test results point to, and record what drove each one. A "
                "refinement with no test result behind it is a change, not a refinement.",
         given=1, blank_rows=5, exemplar=1,
         table=(["What the test showed", "The refinement you applied", "What it changed"],
                [["The replacement instance took longer than expected to become healthy",
                  "shortened the health-check interval and reduced the healthy threshold",
                  "Recovery time dropped. Note the chain: an observation from a specific test, a "
                  "change made because of it, and what it did. All three, or it is not a "
                  "refinement."],
                 ["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""]]),
         clicks=["Make the change in your template, not in the console — otherwise the template "
                 "stops describing what is deployed.",
                 "Update the stack the same way as task 3, checking the change-set preview again.",
                 "Re-run whichever test found the problem, and confirm the refinement actually "
                 "improved it.",
                 "Screenshot the refinement applied and its effect."],
         consider=["Go back through tasks 4 to 8. What did each one show that you were not "
                   "expecting?",
                   "If your tests genuinely found nothing, say what you checked and why you are "
                   "satisfied — but look again first, because that is rare.",
                   "Why is changing the template better than clicking the change in the console? "
                   "IR-5 has an opinion about this."],
         evidence=["a refinement applied, and its effect"]),

    dict(n=10, title="Document the as-deployed architecture and test results",
         prompt="Document what is actually deployed, and how it differs from what was approved. "
                "Write it for the YAT ICT person who inherits this environment and was not here. "
                "Include the test results — the as-deployed state without the evidence it works is "
                "half a handover. Highlight every change from the approved design, with the "
                "reason.",
         points=[
             "the as-deployed architecture, tier by tier, as it actually stands",
             "the deployment steps in enough detail that someone else could repeat them",
             "the test results from tasks 4 to 8, with what was observed",
             "every difference from the approved design, with the reason — including the task 9 "
             "refinements",
             "anything approved but not deployed, and why",
             "known limitations of the deployed result",
         ],
         consider=["As-deployed means what is actually there, not what you designed. Where those "
                   "differ, the difference is the most valuable thing in the document.",
                   "Could someone repeat your deployment from this alone? That is the test for the "
                   "steps section.",
                   "Your reader was not here and cannot ask you anything. What would they need "
                   "that is currently only in your head?",
                   "Known limitations — what does this environment still not do? Naming it is what "
                   "stops someone assuming otherwise."]),

    dict(n=11, title="Describe the long-term improvement strategy",
         prompt="You have deployed what was approved. Describe what YAT should do next and over "
                "the longer term, and what each thing would buy them. This is not a list of "
                "everything possible — it is what you would advise a client you have just spent a "
                "project with, in the order you would advise it.",
         given=1, blank_rows=5, exemplar=1,
         table=(["Strategy", "Why, and when", "The benefit to YAT"],
                [["Test the restore on a schedule, not just once",
                  "within the next quarter — a backup nobody has restored is a hope, and you have "
                  "now proved it once",
                  "Recovery becomes something YAT knows it can do, rather than something it "
                  "believes. Note the middle column carries a WHEN — a strategy with no timing is "
                  "a wish."],
                 ["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""]]),
         consider=["What did you propose that was not approved? That is the obvious first entry, "
                   "and it is now better evidenced than it was.",
                   "What did your tests suggest would matter next?",
                   "At what point does the CMS application itself become the constraint rather "
                   "than the infrastructure?",
                   "Order matters. What would you do first, and why that?"]),

    dict(n=12, title="Hand over and obtain final sign-off",
         prompt="Walk Sam Walker (played by your teacher or a classmate) through what you "
                "deployed, what your tests showed, and what you are recommending next. Answer "
                "questions, respond to feedback, and close the loop. Work out where your "
                "documentation would be filed per the Records Management Policy.",
         resources=[
             ("Records Management Policy — where completed engagement documentation is filed",
              f"{POLICY}/records-management"),
         ],
         given=1, blank_rows=6, exemplar=1,
         table=(["Record", "Your entry"],
                [["What you handed over",
                  "the as-deployed documentation and the test results — both, because the "
                  "documentation without the evidence is a claim"],
                 ["Where you would file it", ""],
                 ["Feedback given, and your response", ""],
                 ["Decision", ""],
                 ["Signed by, and date", ""]]),
         clicks=["Lead with what the tests showed, not with what you built. Sam approved the "
                 "design already; what is new is the evidence it works.",
                 "Name the differences from the approved design yourself, before you are asked. "
                 "Volunteering them is what makes the rest credible.",
                 "Ask for final sign-off. Out loud.",
                 "Record the outcome immediately afterwards."],
         consider=["Did you present evidence or assertions? 'It is more reliable' versus 'I "
                   "terminated an instance and the site kept serving; here is the screenshot'.",
                   "Did you close the loop, or did the conversation just end?",
                   "Open the Records Management Policy and find the real answer for filing. Do not "
                   "write what sounds plausible."]),

    dict(n=13, title="Remove what you deployed",
         prompt="Tear the environment down through the infrastructure-as-code tooling and confirm "
                "it is gone. Lab environments are not free, and an environment left running is a "
                "cost nobody agreed to.",
         given=1, blank_rows=4, exemplar=1,
         table=(["What you removed", "How", "Confirmed gone"],
                [["Anything left behind", "checked for orphaned resources",
                  "Look in EC2, RDS, and Load Balancers after the stack has gone. Anything still "
                  "there was created by hand rather than by the template — which is worth knowing "
                  "about your own habits."],
                 ["The improved environment", "", ""],
                 ["The baseline stack", "", ""],
                 ["Elastic IPs and volumes", "", ""]]),
         clicks=["CloudFormation → select your stack → Delete → confirm. Wait for it to leave the "
                 "list.",
                 "Then go and look: EC2 Instances, Load Balancers, Target Groups, RDS, and Elastic "
                 "IPs. All should be free of your resources.",
                 "An Elastic IP that is allocated but not attached still bills. Check for one.",
                 "Screenshot the empty stack list."],
         consider=["Why tear down through the tooling rather than deleting resources by hand?",
                   "Did anything refuse to delete? What was holding it?",
                   "If something was left behind, where did it come from — and would the same "
                   "thing happen in the assessment?"]),
]
