#!/usr/bin/env python3
"""The S1-CL2 AT2 PRACTICE microservice-and-IaC build run sheet — content.

Same shape as the AT2 assessment workbook, different everything else. A student who works
through this has deployed a provided template, found and fixed a fault in it, authored their
own template, wired a function to a queue and a table, tested it and torn it down — without
having seen any of the assessment's answers:

  scenario   the LMS activity-audit service — not the website's access-log service
  template   lms-activity-store.yaml, table yat-lms-activity-<env> — not yat-audit-<env>
  the fault  ProvisionedThroughput declared alongside BillingMode: PAY_PER_REQUEST — not the
             assessment's KeySchema / AttributeDefinitions name mismatch. A different error
             message, a different diagnosis, the same skill.
  code       activity_writer.py, environment variable ACTIVITY_TABLE — not handler.py and
             AUDIT_TABLE
  fields     activity_id / action / module_ref — not event_id / event_type / source_ip

THE FAULT IS THE POINT OF THE PRACTICE, and it is deliberately a different KIND of fault. The
assessment's is an internal inconsistency: two parts of the same resource disagree, and the
fix is to make them agree. This one is a mutual exclusion: two properties that are each
individually valid cannot both be present. A student who has only ever seen the first kind
reads "the error names a property" and starts renaming things. Seeing both teaches the actual
move — read the error, work out which of the two properties this table should have, delete
the other.

WHAT PRACTICE ADDS: click-by-click steps on every build task. The assessment says "deploy the
provided template"; practice says which console, which button, and what the failure will look
like when it comes. The thinking tasks get "Things to consider" instead — leading questions,
never answers.

No marking criteria, no UoC tags. Rendered by the assessment's own renderer in
s1_cl2_at2_run_sheet, with these lists passed in.
"""

SITE = "https://yat.timbaird.com"
STATE = "s1-cl2-at2"
PROJECT = f"{SITE}/intranet/{STATE}/projects/lms-global-expansion"
ICT = f"{SITE}/intranet/{STATE}/ict"
POLICY = f"{SITE}/intranet/{STATE}/policies"
REFERENCE = f"{SITE}/intranet/{STATE}/reference"

# ---------------------------------------------------------------- front matter

SCENARIO = [
    "The LMS Global Expansion engagement has been approved. The design and the disaster recovery "
    "plan were produced in the previous practice exercise, and this is the implementation phase.",
    "You are an MTS Consultant reporting to Pat Lin (MTS Senior Consultant), with Sam Walker as "
    "the person who accepts the build. Your job is to stand up the activity-audit microservice "
    "the approved design calls for, and to do it as code so YAT can reproduce it.",
    "This is practice. Nothing here is assessed and nothing is submitted. It is the same work the "
    "assessment will ask for, on a different system with different settings and a different fault "
    "waiting in the provided template — so do it properly, because the moves are the point.",
]

RESOURCES = [
    ("LMS Global Expansion — Functional & Non-Functional Requirements — the requirement the "
     "microservice exists to satisfy", f"{PROJECT}/requirements"),
    ("Data Residency & Sovereignty Requirements — why the store is in India and why it is "
     "parameterised", f"{PROJECT}/data-residency-requirements"),
    ("LMS Activity-Audit — Provided Data-Store Template — the template you operate",
     f"{PROJECT}/provided-data-store-template"),
    ("LMS Activity-Audit — Provided Microservice Code & Contract — the code you deploy and the "
     "contract you build to", f"{PROJECT}/provided-microservice-code"),
    ("Change Management Procedure — the governance a production-affecting change sits under",
     f"{POLICY}/change-management"),
]

INSTRUCTIONS = [
    "Work the tasks in order. Tasks 1 to 4 are the thinking you do before touching anything; "
    "tasks 5 to 10 operate a template someone else wrote; tasks 11 to 19 build your own.",
    "Every build task tells you where to click. The assessment will not — it will tell you what "
    "to build and leave you to find your way around. So pay attention to WHERE things are, not "
    "just what you clicked.",
    "Take a screenshot at the end of each task even though this is not assessed. In the "
    "assessment you need one per task, and building the habit here is the point.",
    "Things will fail, and one of them is meant to. Read the error before you change anything — "
    "that is the single most useful habit in this whole run sheet.",
    "Delete your stacks when you finish a session. The lab charges for what is running whether "
    "you are using it or not.",
]

REGION_NOTE = ("The approved design places the activity store in India — "
               "[scenario: ap-south-1 | deploy: us-east-1]. Build everything in us-east-1 in the "
               "AWS Academy Learner Lab, which does not offer the Indian regions. Where a task "
               "asks you to name the region the design calls for, name ap-south-1; where it asks "
               "what you deployed to, that is us-east-1. The work is identical either way, and "
               "the parameterisation in task 17 is exactly what makes the difference a parameter.")

# ---------------------------------------------------------------- the supplied material

SUPPLIED_INTRO = [
    "Two files are provided to you and are reproduced here in full. You do not write either of "
    "them. Read them both before you start — task 5 and task 11 depend on you having done so.",
    "They are also on the intranet, under the LMS Global Expansion project, so you can copy from "
    "there rather than retyping.",
]

DATASTORE_YAML = [
    "AWSTemplateFormatVersion: '2010-09-09'",
    "Description: >-",
    "  YAT LMS activity-audit data store (PROVIDED - you operate this, you do not",
    "  author it). A single DynamoDB table holding the append-only LMS activity",
    "  records the microservice writes. Operate it: review, deploy, update a",
    "  parameter, and delete. It has not been validated in this account and may",
    "  not deploy as supplied - if so, diagnose the error, fix it, and redeploy.",
    "",
    "Parameters:",
    "  EnvName:",
    "    Type: String",
    "    Default: dev",
    "    AllowedValues: [dev, prod]",
    "    Description: Environment suffix used in the table name.",
    "",
    "Resources:",
    "  ActivityTable:",
    "    Type: AWS::DynamoDB::Table",
    "    Properties:",
    "      TableName: !Sub 'yat-lms-activity-${EnvName}'",
    "      BillingMode: PAY_PER_REQUEST",
    "      ProvisionedThroughput:",
    "        ReadCapacityUnits: 5",
    "        WriteCapacityUnits: 5",
    "      AttributeDefinitions:",
    "        - { AttributeName: activity_id, AttributeType: S }",
    "      KeySchema:",
    "        - { AttributeName: activity_id, KeyType: HASH }",
    "      Tags:",
    "        - { Key: Project, Value: YAT-LMS }",
    "        - { Key: Environment, Value: !Ref EnvName }",
    "        - { Key: DataClassification, Value: activity-audit }",
    "",
    "Outputs:",
    "  ActivityTableName:",
    "    Description: The activity table name - your microservice stack reads this.",
    "    Value: !Ref ActivityTable",
    "    Export:",
    "      Name: !Sub 'yat-lms-activity-table-${EnvName}'",
]

WEBHOOK_CONTRACT = [
    "POST  {ApiEndpoint}              # an Output of your deployed stack",
    "Content-Type: application/json",
    "",
    "{",
    '  "activity_id": "7b2c9d1a-...",          # unique id (UUID) - the idempotency key',
    '  "occurred_at": "2026-06-07T01:23:45Z",  # ISO-8601 UTC timestamp',
    '  "user_ref":    "u-48217",               # opaque user reference, not a name',
    '  "cohort":      "IN",                    # "AU" or "IN"  (IN = the India cohort)',
    '  "action":      "open_course",           # sign_in | open_course | submit_assessment',
    '  "module_ref":  "ICTCLD-DR-01"           # the LMS module the action related to',
    "}",
    "",
    "Responses:   200 = accepted and queued for writing      400 = malformed request",
]

HANDLER_SUMMARY = [
    ("What it is", "activity_writer.py — an SQS-triggered Lambda written in Python 3.12. Provided "
                   "to you in full; you deploy it, you do not write it."),
    ("What it does", "reads LMS activity messages from the queue, validates each one, and writes "
                     "it to the DynamoDB table as an immutable audit record"),
    ("Data flow", "HTTP API  →  SQS queue  →  this Lambda  →  DynamoDB table"),
    ("Validation", "all six fields required; cohort must be AU or IN; action must be sign_in, "
                   "open_course or submit_assessment. Anything else is rejected and logged."),
    ("Idempotency", "activity_id is the partition key and the write is conditional, so a "
                    "re-delivered message is skipped rather than duplicated"),
    ("What it needs from you", "an environment variable ACTIVITY_TABLE holding the table name, "
                               "and permission to write to that table"),
    ("Runtime note", "boto3 is provided by the Lambda runtime — there are no dependencies to "
                     "package"),
]

# ---------------------------------------------------------------- the tasks

TASKS = [
    # ---------------------------------------- before you build
    dict(n=1, title="Why infrastructure as code for this job",
         resources=[
             ("LMS Global Expansion — Functional & Non-Functional Requirements — the requirement "
              "that the changes be provisioned as code", f"{PROJECT}/requirements"),
             ("Data Residency & Sovereignty Requirements — DR-R4, keeping the Indian footprint "
              "extensible", f"{PROJECT}/data-residency-requirements"),
         ],
         prompt="Before you build anything, establish why this is being built as code at all. "
                "Identify the benefits infrastructure as code brings to THIS engagement — not in "
                "general — and tie each one to a business need you can point at in the "
                "requirements.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Benefit", "What it gives YAT here", "The business need it answers"],
                [["No undocumented drift",
                  "what is deployed is what is in the template, so nobody has to reverse-engineer "
                  "the environment later",
                  "YAT ICT operates this after MTS leaves. Notice the third column names a real "
                  "consequence for a real party — not 'best practice'. Every row you write needs "
                  "that."],
                 ["Reproducible in another region", "", ""],
                 ["Repeatable disaster recovery", "", ""],
                 ["Consistency between environments", "", ""],
                 ["Reviewable change", "", ""]]),
         consider=["Two of the answers are sitting in documents you have already read. Which "
                   "requirement asks for the environment to be stood up in another region by "
                   "changing configuration?",
                   "DR-R4 is about keeping options open. What does infrastructure as code have to "
                   "do with that?",
                   "Your own DR plan committed to a four-hour recovery. What does deploying from "
                   "a template do to that number, compared with rebuilding by hand?",
                   "If you can write the same row about any project anywhere, it is a generic "
                   "benefit and it does not belong here."]),

    dict(n=2, title="What automation gives the platform",
         prompt="Infrastructure as code is one kind of automation. Determine what else about this "
                "build is automated rather than done by hand, and what YAT gets from each. Think "
                "about what happens without anyone present — at 2am, or when a message fails.",
         given=1, blank_rows=6, exemplar=1,
         table=(["What is automated", "How the platform does it", "What YAT no longer does by hand"],
                [["Detection", "the alarm evaluates the metric and notifies",
                  "Watching a dashboard. That is the shape of the third column — a job a human "
                  "would otherwise have to do, named as a job."],
                 ["Provisioning", "", ""],
                 ["Retry on failure", "", ""],
                 ["Scaling the processor", "", ""],
                 ["Capacity for the store", "", ""]]),
         consider=["A message fails to process. What happens next, and who does it?",
                   "The event rate goes up ten times during submission week. What sizes the "
                   "processor, and when?",
                   "The store is billed per request. What did that save someone from having to "
                   "decide in advance?",
                   "This task is about capability the PLATFORM supplies, not scripts you wrote. "
                   "Read your rows back with that in mind."]),

    dict(n=3, title="What can go wrong with infrastructure as code",
         prompt="Determine and assess what can go wrong when infrastructure is deployed this way. "
                "You are about to find at least one of these for real, so think about it now: "
                "what kinds of error does this approach produce, and how serious is each?",
         given=1, blank_rows=7, exemplar=1,
         table=(["What can go wrong", "What it looks like", "How serious"],
                [["Template syntax error", "the service rejects the file before creating anything",
                  "Low — fast to find, and nothing was created. Starting with the least serious "
                  "makes the rest of the column mean something; if everything is 'high' you have "
                  "not assessed anything."],
                 ["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""]]),
         consider=["Sort the failures by when they happen: before anything is created, during "
                   "creation, or after the stack already exists and holds data.",
                   "The last of those is the dangerous one. What kind of change destroys a "
                   "resource instead of modifying it, and how would you find out?",
                   "Two properties can each be valid and still not be allowed together. Is that a "
                   "syntax error? Where would that failure show up?",
                   "What happens when someone changes something in the console afterwards? Is "
                   "that an error, and when does it bite?",
                   "You will meet one of your own rows in about three tasks' time."]),

    dict(n=4, title="Select the infrastructure-as-code service",
         prompt="Evaluate the infrastructure-as-code services available for this platform and "
                "select one. Say what you compared it against and why your choice suits this "
                "engagement. A choice with no alternative beside it is not an evaluation.",
         given=1, blank_rows=5, exemplar=1,
         table=(["Service", "What it is", "Suitability here"],
                [["Terraform", "a third-party tool that works across multiple cloud platforms",
                  "Genuinely strong, and its main advantage — working across several cloud "
                  "providers — is not one YAT needs. An alternative rejected for a stated reason "
                  "is worth more than one not mentioned."],
                 ["AWS CloudFormation", "", ""],
                 ["AWS CDK", "", ""],
                 ["Your selection", "", ""]]),
         consider=["What is already true about this engagement that points at one of them? Look "
                   "at what you were handed.",
                   "Who operates this after you leave, and what will they be able to read?",
                   "Does the Learner Lab let you install extra tooling?",
                   "Any of the three is a defensible choice if the reasoning holds. What is "
                   "yours?"]),

    # ---------------------------------------- operate the provided template
    dict(n=5, title="Review the provided data-store template",
         prompt="Read the provided template above, closely. Work out what it creates, what each "
                "part of it does, and what depends on what. Do not deploy it yet — the point of "
                "this task is that you can read a template someone else wrote before you run it.",
         given=1, blank_rows=7, exemplar=1,
         table=(["Part of the template", "What it does", "What depends on it"],
                [["What it does NOT create",
                  "no API, no queue, no function — those are yours to build in task 12",
                  "Nothing depends on it, and that is why the row is here: knowing where the "
                  "provided work stops is the first thing you need before you author anything."],
                 ["Parameters — EnvName", "", ""],
                 ["Resources — ActivityTable", "", ""],
                 ["TableName — !Sub", "", ""],
                 ["Tags", "", ""],
                 ["Outputs — ActivityTableName with Export", "", ""]]),
         consider=["The Export at the bottom is the most important line in the file for you "
                   "personally. Why?",
                   "Trace EnvName through the template. How many things change when it changes?",
                   "The table has one attribute defined and one key. Does anything else in the "
                   "template or the contract use that name?",
                   "There are two properties in this resource that both talk about capacity. Look "
                   "at them. Do not fix anything yet — task 6 needs you to deploy it as supplied."]),

    dict(n=6, title="Deploy the provided template",
         prompt="Deploy the provided template using the infrastructure-as-code service's tooling. "
                "Use the console or the command line — your choice, but say which you used and "
                "why. It will not succeed. Capture what happens.",
         given=1, blank_rows=5, exemplar=1,
         table=(["Step", "What you did", "What happened"],
                [["Tooling used", "console or CLI — name it, and why you chose it",
                  "Both are fine. The reason is the answer: 'the console, because I wanted to see "
                  "the events as they happened' is a reason; 'the console' is not."],
                 ["Stack name", "yat-lms-activity-store", ""],
                 ["Parameter", "EnvName=dev", ""],
                 ["Result", "", ""]]),
         clicks=["Save the template above as lms-activity-store.yaml, or copy it from the "
                 "intranet page rather than retyping it.",
                 "Start the lab and check your region reads N. Virginia (us-east-1) before you do "
                 "anything else.",
                 "Search CloudFormation in the top search bar and open it.",
                 "Choose Create stack → With new resources (standard).",
                 "Choose Upload a template file, select your file, and Next.",
                 "Stack name: yat-lms-activity-store. Leave EnvName on dev. Next, Next, Submit.",
                 "Watch the Events tab. It will fail. Do not delete anything yet — task 7 needs "
                 "the error message.",
                 "Screenshot the failed stack with the Status reason visible."],
         consider=["Before you look at the error properly: what did you expect to go wrong from "
                   "your reading in task 5?",
                   "Do not fix it yet. Capturing the failure as supplied is the whole evidence "
                   "for the next task."],
         evidence=["the failed stack showing its status and the failure reason"]),

    dict(n=7, title="Diagnose and fix the failure",
         prompt="The template does not deploy as supplied. Read the error before changing "
                "anything. Work out what is actually wrong, fix it, and redeploy. Record the "
                "error you saw, what you worked out, and the change you made — this task is about "
                "the diagnosis, not the fix.",
         # No exemplar row: every row in this table IS one of the answers the task asks for, and
         # a worked one would hand over the diagnosis. The clicks and considerations teach it.
         given=1, blank_rows=4,
         table=(["Diagnosis", "Your answer"],
                [["The error message you saw", ""],
                 ["What you worked out it meant", ""],
                 ["The change you made", ""],
                 ["Why that fix and not the other one", ""]]),
         clicks=["Open the failed stack, Events tab, and scroll to the FIRST red row. That is the "
                 "cause; everything under it is the rollback.",
                 "Read the Status reason in full. It names the properties involved — it is more "
                 "specific than you expect.",
                 "Go back to the template and find both properties it is talking about.",
                 "Decide which one this table should keep. Read the Description at the top of the "
                 "template and think about the write pattern before you choose.",
                 "Delete the other one. Save the file.",
                 "The failed stack has to go before you can reuse the name: select it, Delete, "
                 "and wait for it to disappear.",
                 "Create the stack again with the same name and EnvName=dev. Watch it reach "
                 "CREATE_COMPLETE."],
         consider=["The error is not a spelling mistake. Both properties are individually valid. "
                   "What is the actual rule being broken?",
                   "PAY_PER_REQUEST and provisioned capacity are two different ways to pay for "
                   "the same table. Can a table be on both?",
                   "Which one suits a workload that is quiet most of the time and spikes at the "
                   "end of term?",
                   "If you changed things until it worked without being able to say why, go back. "
                   "The assessment version of this task marks the diagnosis, not the fix."],
         evidence=["the stack reaching CREATE_COMPLETE after your fix"]),

    dict(n=8, title="Confirm the deployment",
         prompt="Confirm the resources actually exist and are configured the way the template "
                "said. Do not take the stack's success message as proof — go and look at the "
                "resource itself, using the console or the command line.",
         given=1, blank_rows=5, exemplar=1,
         table=(["What you confirmed", "How you confirmed it", "What you saw"],
                [["The stack output and export", "the stack's Outputs tab",
                  "The exported name — write it down exactly. Your own template imports it in "
                  "task 12 and a single character wrong there costs you a deployment cycle."],
                 ["The table exists with the expected name", "", ""],
                 ["The partition key", "", ""],
                 ["The tags applied", "", ""],
                 ["The billing mode", "", ""]]),
         clicks=["Search DynamoDB in the top search bar and open it.",
                 "Choose Tables in the left menu. Your table should be listed as "
                 "yat-lms-activity-dev.",
                 "Open it. The Overview tab shows the partition key and the capacity mode.",
                 "Open the Additional settings or Tags tab and check the three tags.",
                 "Go back to CloudFormation, open your stack, and open the Outputs tab. Copy the "
                 "export name.",
                 "Screenshot the table page with the name and key visible."],
         consider=["Why is looking at the stack not enough? What could be true of a stack that "
                   "says CREATE_COMPLETE?",
                   "The billing mode row is worth checking specifically. It is the thing you just "
                   "changed.",
                   "Where would you look for the same information from the command line?"],
         evidence=["the deployed table showing its name, key schema and tags"]),

    dict(n=9, title="Update the provided template and redeploy",
         prompt="Change the parameter and redeploy the same template, so the stack modifies what "
                "is already there rather than creating something new. Record what changed and — "
                "more importantly — what happened to the resource that already existed.",
         given=1, blank_rows=4,
         table=(["Step", "What you did", "What happened"],
                [["The change", "redeployed with EnvName=prod", ""],
                 ["What the service did", "", ""],
                 ["What that means for real data", "", ""],
                 ["Which task warned you", "", ""]]),
         clicks=["Open your stack in CloudFormation and choose Update.",
                 "Choose Use existing template, then Next.",
                 "Change EnvName from dev to prod. Next, Next, Submit.",
                 "Watch the Events tab as it runs — the interesting rows go past quickly.",
                 "When it finishes, go to DynamoDB → Tables and look at what is there now.",
                 "Screenshot the table list."],
         consider=["Before you look: do you expect the table to be RENAMED, or replaced?",
                   "The table name is built from the parameter. Is a name something a table can "
                   "change, or is it part of what the table IS?",
                   "If that table had held 180 days of activity records the regulator expects to "
                   "see, what just happened?",
                   "Nobody is marking whether you predicted it. What matters is whether you "
                   "noticed."],
         evidence=["the stack update, and the resulting table"]),

    dict(n=10, title="Return the store to a known state",
         prompt="You need the data store running with EnvName=dev for the rest of this build. Put "
                "it back there, and confirm it. Say what you did — whether you updated again or "
                "removed and redeployed — and why that was the right way round.",
         given=1, blank_rows=3,
         table=(["Step", "What you did", "Confirmed how"],
                [["Returned the store to EnvName=dev", "", ""],
                 ["Confirmed the table name and key", "", ""],
                 ["Confirmed the export is available for your own stack", "", ""]]),
         clicks=["Update the stack again with EnvName=dev, the same way you did in task 9.",
                 "Check DynamoDB shows yat-lms-activity-dev and nothing else of yours.",
                 "In CloudFormation, choose Exports in the left menu. Find "
                 "yat-lms-activity-table-dev and confirm it is there.",
                 "If it is not, your stack is not deployed at dev — go back."],
         consider=["Either route works. Which did you choose, and what made it the right way "
                   "round?",
                   "How do you know you are in the state you need, rather than assuming?"]),

    # ---------------------------------------- your own build
    dict(n=11, title="Review the microservice code and contract",
         prompt="Read the provided handler and the webhook contract above. Work out what the code "
                "expects from the infrastructure you are about to build — what it reads, what it "
                "writes, what it needs to be told, and what permissions it will need. Everything "
                "your template has to provide is discoverable from these two things.",
         given=1, blank_rows=6, exemplar=1,
         table=(["What the code needs", "Where you found it", "What your template must provide"],
                [["A Python 3.12 runtime",
                  "the module docstring says so, and notes that boto3 comes with the runtime",
                  "The runtime setting on the function, and nothing else — no packaging, no "
                  "dependencies. Worth confirming rather than assuming, because the alternative "
                  "is an afternoon spent zipping libraries you did not need."],
                 ["To be triggered by queue messages", "", ""],
                 ["The table name", "", ""],
                 ["Permission to write to the table", "", ""],
                 ["Something to receive the HTTP call", "", ""]]),
         consider=["The handler reads one environment variable. What is it called, exactly? Case "
                   "matters.",
                   "What does the code do with event['Records']? What kind of event has that "
                   "shape, and what has to be wired up for the function to receive one?",
                   "The function calls put_item on a table. What does it need to be allowed to "
                   "do, and on which resource?",
                   "The contract describes an HTTP POST. The handler does not handle HTTP at all. "
                   "What sits between them, and what does it have to do?",
                   "If you start authoring without finishing this table, you are guessing. Every "
                   "requirement is discoverable from these two documents."]),

    dict(n=12, title="Author your template",
         prompt="Write the infrastructure-as-code template that deploys the microservice. It "
                "provisions the API, the queue and the function, sets the function's environment "
                "variable from the provided stack's export, and grants the permissions the "
                "function needs. Record the structure of what you wrote.",
         given=1, blank_rows=7, exemplar=1,
         table=(["Section of your template", "What you put in it", "Why"],
                [["Parameters", "EnvName, matching the provided stack",
                  "The two stacks have to agree on which environment they are, because the import "
                  "name is built from it. Starting here is not arbitrary — get the parameter "
                  "wrong and every row below inherits the mistake."],
                 ["The HTTP API", "", ""],
                 ["The queue", "", ""],
                 ["The function", "", ""],
                 ["Environment variable", "", ""],
                 ["Permissions", "", ""]]),
         clicks=["Start a new file. Give it the same first two lines as the provided template — "
                 "AWSTemplateFormatVersion and a Description that says what this stack is.",
                 "Add a Parameters section with EnvName, the same three lines as the provided "
                 "template. Copy them; they are already right.",
                 "Add the queue first. It is the simplest resource and the other two refer to it.",
                 "Add the function. Runtime python3.12, handler "
                 "activity_writer.handler, and the role. In the Learner Lab you cannot create "
                 "roles — use the lab-provided LabRole by its ARN.",
                 "Set the function's Environment → Variables → ACTIVITY_TABLE using "
                 "!ImportValue with the export name you copied in task 8. Build it with !Sub so "
                 "it follows EnvName.",
                 "Add the event source mapping — the resource that connects the queue to the "
                 "function. Without it nothing ever invokes the function and everything looks "
                 "fine.",
                 "Add the HTTP API, a route for POST, and the integration that puts the request "
                 "body on the queue.",
                 "Add an Outputs section publishing the API endpoint URL. You need it in task 15 "
                 "and hunting for it later is annoying.",
                 "Read the file top to bottom once before you deploy it. Most first-attempt "
                 "failures are visible on that read."],
         consider=["Where does the function's code actually come from? There is more than one "
                   "way, and the simplest one in a lab is not the same as the one you would use "
                   "in production.",
                   "Should the table name be typed into your template? What did task 8 give you "
                   "instead, and what happens if the store is redeployed?",
                   "Least privilege: the function writes to one table and reads from one queue. "
                   "What would 'more than it needs' look like here?",
                   "Would YAT ICT be able to read this file in six months? Named parameters, "
                   "sensible logical IDs, described outputs — that is what makes it readable."]),

    dict(n=13, title="Deploy your template",
         prompt="Deploy your own template. Expect it to take more than one attempt — that is "
                "normal for a first template and it is not a mark against you. Record the "
                "attempts.",
         given=1, blank_rows=5, exemplar=1,
         table=(["Attempt", "What happened", "What you changed"],
                [["1", "the stack rolled back on the first resource it could not create",
                  "Whatever yours actually says. Recording the failed attempts is the habit — the "
                  "assessment has a whole task (16) that is impossible to fill in honestly if you "
                  "did not write them down as they happened."],
                 ["2", "", ""], ["3", "", ""], ["Final", "", ""]]),
         clicks=["CloudFormation → Create stack → With new resources (standard) → Upload a "
                 "template file.",
                 "Stack name: something of your own, e.g. yat-lms-activity-service. EnvName=dev, "
                 "matching the store.",
                 "On the review page, tick the acknowledgement about IAM resources if it appears, "
                 "then Submit.",
                 "If it fails: Events tab, first red row, read the Status reason.",
                 "A rolled-back stack has to be deleted before you can create one with the same "
                 "name again.",
                 "Write down each failure and its fix as you go — do not rely on remembering "
                 "them in task 16.",
                 "Screenshot the stack at CREATE_COMPLETE with its Resources tab open."],
         consider=["If the failure names the import, what does that tell you about which stack is "
                   "wrong?",
                   "If it names permissions, is that your template or the lab environment?",
                   "How many attempts did it take? The honest number is more useful to you than a "
                   "tidy one."],
         evidence=["your stack showing CREATE_COMPLETE and the resources it created"]),

    dict(n=14, title="Confirm your deployment",
         prompt="Confirm the resources your template created, using the console or the command "
                "line. Check the wiring, not just the existence — the function has to be "
                "connected to the queue, and it has to know the table name.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Resource", "What you checked", "What you saw"],
                [["Environment variable", "ACTIVITY_TABLE on the function's Configuration tab",
                  "It should hold the real table name — yat-lms-activity-dev — not a placeholder "
                  "and not the export name. This is the check that separates confirming from "
                  "glancing, and it is the one that catches a broken !ImportValue."],
                 ["HTTP API", "", ""],
                 ["Queue", "", ""],
                 ["Function", "", ""],
                 ["Trigger", "", ""]]),
         clicks=["Lambda → Functions → open yours. The Configuration tab has Triggers and "
                 "Environment variables in the left menu.",
                 "Triggers should list your SQS queue. If it is empty, your event source mapping "
                 "is missing — nothing will ever run.",
                 "Environment variables should show ACTIVITY_TABLE with the real table name.",
                 "SQS → Queues confirms the queue exists with the name your template gave it.",
                 "API Gateway → APIs → yours → the Invoke URL is what you POST to in task 15. "
                 "Copy it.",
                 "Screenshot the function's Configuration page showing the trigger and the "
                 "variable."],
         consider=["A resource existing and a resource being wired up are different things. Which "
                   "of your five rows are existence checks and which are wiring checks?",
                   "If the trigger is missing, what would you see in task 15 — an error, or "
                   "silence?"],
         evidence=["the function's configuration showing its trigger and environment variable"]),

    dict(n=15, title="Test the microservice end to end",
         prompt="Send a real event through the contract and confirm it arrives in the store. Use "
                "the payload shape from the webhook contract above. Then send one that breaks the "
                "contract — a missing field or an invalid action — and record what happens to it.",
         given=1, blank_rows=5, exemplar=1,
         table=(["Test", "What you sent", "What you expected", "What happened"],
                [["Valid event", "a complete payload per the contract",
                  "200 accepted, and one record in the table",
                  "Fill in what actually happened, not what should have. The gap between those "
                  "two columns is where every useful thing in task 16 comes from."],
                 ["The record itself", "", "", ""],
                 ["Duplicate event", "", "", ""],
                 ["Invalid event", "", "", ""]]),
         clicks=["Use curl, or any HTTP client you like. The command is:",
                 "curl -X POST <your invoke URL> -H 'Content-Type: application/json' -d "
                 "'{\"activity_id\":\"11111111-aaaa\",\"occurred_at\":\"2026-06-07T01:23:45Z\","
                 "\"user_ref\":\"u-48217\",\"cohort\":\"IN\",\"action\":\"open_course\","
                 "\"module_ref\":\"ICTCLD-DR-01\"}'",
                 "Then look in DynamoDB → Tables → your table → Explore table items. The record "
                 "should be there within a few seconds.",
                 "Send the exact same command again, unchanged. Check the table — there should "
                 "still be ONE record.",
                 "Now send one with \"action\":\"deleted_everything\" and a new activity_id.",
                 "Check the table (nothing new should appear) and then check the function's log: "
                 "Lambda → Monitor → View CloudWatch logs → the most recent log stream.",
                 "Screenshot the request and response, the record in the table, and the log line "
                 "showing the rejection."],
         consider=["If nothing appears in the table, work backwards along the flow: did the API "
                   "return 200? Is there a message in the queue? Did the function run? What does "
                   "its log say?",
                   "The duplicate test is the one people skip. Why does sending the same event "
                   "twice matter for an audit log?",
                   "The invalid event should be rejected and logged, not silently dropped. Can "
                   "you see the reason in the log?",
                   "Testing only the path that works has tested half of it."],
         evidence=["the request and its response",
                   "the record in the table",
                   "the function log showing the rejection of the invalid event"]),

    dict(n=16, title="Troubleshoot what went wrong",
         prompt="Record what actually broke during tasks 12 to 15 and what you did about it. "
                "Every real build has these. An empty table here is not a sign of a perfect build "
                "— it is a sign you did not write them down as you went.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Symptom", "How you diagnosed it", "The fix"],
                [["Events accepted by the API but no record appears",
                  "checked the function's log and found an access-denied error on the write",
                  "The middle column is the task. 'It was broken so I fixed it' records nothing "
                  "useful; naming what you looked at and what it told you is a method someone "
                  "else could follow."],
                 ["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""]]),
         consider=["Look at your task 13 attempts table. Every failed attempt is a row here.",
                   "Two is the realistic minimum for a first build. If you genuinely had none, "
                   "you either had help or you are not counting the ones you fixed in thirty "
                   "seconds.",
                   "For each, what was the FIRST thing you looked at? That is the method.",
                   "Which of these would you have found faster with what you know now?"]),

    dict(n=17, title="Parameterise for a second environment",
         prompt="Redeploy your template as a second, separate environment by changing "
                "configuration only — not by editing resource definitions. This is the thing that "
                "makes the India region a parameter rather than a rebuild, which is what the "
                "residency requirement asked for. Confirm the two environments are genuinely "
                "separate.",
         given=1, blank_rows=4,
         table=(["Step", "What you did", "Result"],
                [["Second deployment", "", ""],
                 ["What you did NOT change", "the template file itself", ""],
                 ["Confirmed separate", "", ""],
                 ["What this proves for the design", "", ""]]),
         clicks=["First, deploy the provided store a second time at EnvName=prod, under a "
                 "different stack name — your service stack needs an export to import.",
                 "Now create a second stack from YOUR template, unchanged, with a different stack "
                 "name and EnvName=prod.",
                 "Do not open the file. If you find yourself editing it, stop and work out why "
                 "you needed to.",
                 "When it completes, check you have two of everything: two APIs, two queues, two "
                 "functions, two tables.",
                 "POST an event to the prod endpoint and confirm it lands in the prod table and "
                 "not the dev one.",
                 "Screenshot both stacks side by side in the CloudFormation list."],
         consider=["If your template needed editing to deploy twice, what was hard-coded in it?",
                   "The requirement was about REGION, not environment. Is the mechanism any "
                   "different?",
                   "How do you know the two environments are genuinely separate rather than "
                   "sharing something?"],
         evidence=["both stacks existing side by side"]),

    dict(n=18, title="Update your template to add a resource",
         prompt="Modify your template to add a new resource, and redeploy so the existing stack is "
                "updated rather than replaced. A dead-letter queue for messages the function could "
                "not process is the sensible addition. Record what the update did to what was "
                "already there.",
         given=1, blank_rows=4,
         table=(["Change", "What you added or modified", "What the update did"],
                [["New resource", "a dead-letter queue", ""],
                 ["Modified resource", "", ""],
                 ["Unchanged", "", ""],
                 ["Why this addition", "", ""]]),
         clicks=["Open your template file and add a second SQS queue — the dead-letter queue.",
                 "On the ORIGINAL queue, add a RedrivePolicy pointing at the new queue's ARN, "
                 "with maxReceiveCount set to something small like 3.",
                 "Save, then CloudFormation → your dev stack → Update → Replace existing template "
                 "→ upload the new file.",
                 "On the review page, look at the change set before you submit — it lists what "
                 "will be added, modified and replaced. This is the preview that would have "
                 "warned you in task 9.",
                 "Submit, and watch which resources appear in the Events tab and which do not.",
                 "Screenshot the updated stack showing the new queue in its Resources tab."],
         consider=["Which existing resources did the update touch, and which did it leave "
                   "completely alone? The Events tab tells you.",
                   "The change set preview — where was that in task 9, and what would it have "
                   "shown you?",
                   "What happens to a message after three failed attempts now, and where does it "
                   "go?"],
         evidence=["the updated stack showing the new resource"]),

    dict(n=19, title="Set up a metric and an alarm",
         prompt="Set up monitoring for the service you have built: a metric that tells you it is "
                "healthy, and an alarm that fires when it is not. Say what the alarm means in "
                "business terms — what has actually gone wrong for YAT when it fires.",
         given=1, blank_rows=5, exemplar=1,
         table=(["Metric", "Alarm condition", "What it means has gone wrong"],
                [["Dead-letter queue depth", "greater than zero",
                  "Activity events have been abandoned after retries. In business terms: records "
                  "the regulator expects to exist do not. Note that the third column names a "
                  "consequence for YAT, not a technical state — that is what the column is for."],
                 ["Age of the oldest message on the queue", "", ""],
                 ["Function errors", "", ""],
                 ["Who is notified", "", ""]]),
         clicks=["CloudWatch → Alarms → Create alarm → Select metric.",
                 "Choose SQS → Queue Metrics, find your dead-letter queue, and pick "
                 "ApproximateNumberOfMessagesVisible.",
                 "Statistic Maximum, period 1 minute. Condition: Greater than 0.",
                 "For the notification, create an SNS topic and put your own email in it. Confirm "
                 "the subscription from your inbox or the alarm can never notify anyone.",
                 "Name the alarm something an on-call person would understand at 3am — not "
                 "'Alarm 1'.",
                 "Force it: put a message on the dead-letter queue directly (SQS → the queue → "
                 "Send and receive messages) and watch the alarm go to In alarm.",
                 "Screenshot the alarm showing its condition and its state."],
         consider=["An alarm on something that does not indicate a problem is noise, and noise is "
                   "worse than nothing because people learn to ignore it. Does yours indicate a "
                   "real problem?",
                   "Queue depth rising is normal during a spike. Message AGE rising is not. Why "
                   "is that the better signal?",
                   "Who receives this at 3am, and what is the first thing you would want them to "
                   "check?"],
         evidence=["the alarm you created, showing its condition and its state"]),

    # ---------------------------------------- hand it over
    dict(n=20, title="Write the user documentation",
         prompt="Write the user documentation for what you have built. Its reader is the YAT ICT "
                "person who has to operate this after you leave and who was not here while you "
                "built it. Include your templates — documentation for infrastructure as code that "
                "does not contain the code is not documentation. Write it in the box below.",
         points=[
             "what the service is and what it is for, in two or three sentences",
             "the two stacks, the order they deploy in, and why the store goes first",
             "every parameter, its allowed values, and what changing it does — including the "
             "warning from task 9",
             "how to deploy, update and remove, with the actual commands",
             "the templates themselves",
             "what the alarm means when it fires, and the first thing to check",
             "known limitations",
         ],
         consider=["Who is reading this? Not your assessor, and not you in a week. Someone who "
                   "was not here.",
                   "The single most valuable sentence you can write is the task 9 warning. Where "
                   "does it go so that someone about to make that mistake actually sees it?",
                   "Would your reader be able to deploy this from scratch using only your "
                   "document? Try reading it as if you knew nothing.",
                   "'I deployed the stack and it failed, so I fixed the template' is a build log. "
                   "What is the difference between that and user documentation?",
                   "What does this service NOT do? Naming the limits is what stops someone "
                   "assuming it does more."]),

    dict(n=21, title="Remove what you deployed",
         prompt="Tear down everything you created, using the infrastructure-as-code tooling rather "
                "than deleting resources by hand. Confirm it is gone. This is part of the "
                "lifecycle, not housekeeping — and doing it by hand would leave the templates "
                "describing resources that no longer exist.",
         # The row order IS the deletion order — a stack whose export is imported cannot go first.
         given=1, blank_rows=5, exemplar=1,
         table=(["What you removed", "How", "Confirmed gone"],
                [["Your second environment stack", "deleted the stack via CloudFormation",
                  "The stack left the list, and the API, queue and function it created are gone "
                  "from their own consoles. 'Confirmed gone' means looked, not assumed."],
                 ["Your microservice stack", "", ""],
                 ["The provided data-store stacks", "", ""],
                 ["Anything left behind", "", ""]]),
         clicks=["Delete your stacks BEFORE the store stacks. A stack whose export is being "
                 "imported by another cannot be deleted.",
                 "CloudFormation → select the stack → Delete → confirm. Wait for it to leave the "
                 "list.",
                 "Repeat for each stack, service stacks first, store stacks last.",
                 "Then go and look: DynamoDB Tables, Lambda Functions, SQS Queues, API Gateway "
                 "APIs. All should be empty of your resources.",
                 "Screenshot the empty stack list and one of the empty resource lists."],
         consider=["Why does the order matter? What does the error say if you get it wrong?",
                   "Why is deleting via the templates the right way rather than deleting the "
                   "resources directly?",
                   "If something was left behind, where did it come from?"],
         evidence=["the stacks removed, and the resource list showing nothing left behind"]),

    dict(n=22, title="Confirm the build and obtain sign-off",
         prompt="Walk Sam Walker (played by your teacher or a classmate) through what you built, "
                "confirm it meets what was designed in the Part A practice, ask for feedback, "
                "respond to it, and close the loop. Record the conversation and the decision.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Record", "Your entry"],
                [["What you confirmed against the approved design",
                  "the microservice matches the design: API, queue, function, in-region store — "
                  "and here is where the build differs from what was designed, and why"],
                 ["Feedback you sought and were given", ""],
                 ["How you responded", ""],
                 ["Decision", ""],
                 ["Signed by, and date", ""]]),
         consider=["Did you go back to your Part A design and check, or did you describe what you "
                   "built? Those are different tasks and only one of them is this one.",
                   "Did anything end up different from the design? Say so — an unexplained "
                   "difference is the thing an acceptance conversation exists to surface.",
                   "Did you ASK for feedback, or wait for it? The assessment version of this task "
                   "has three verbs in it: confirm, seek, respond.",
                   "'Signed off' with nothing else recorded evidences half of it."]),
]
