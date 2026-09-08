#!/usr/bin/env python3
"""The S1-CL3 AT2 PRACTICE team-implementation run sheet — content.

Same shape as the AT2 assessment workbook, with the team building the website improvement
rather than the Ledgerline one.

BE HONEST ABOUT WHAT THE CONTRAST IS WORTH HERE. In AT1 and AT3 the practice vehicle changes
the answers: a public 24x7 site is a different design and a different deployment from an
internal finance system. In AT2 it mostly does not. A conflict is a conflict, coaching is
coaching, and the criteria this workbook carries are about how the student worked with people
— which does not change because the template builds a load balancer instead of a subnet. The
system swap is still worth having (it keeps the four component briefs genuinely different,
and it keeps the no-leakage rule intact across the cluster), but it is not where the value is.

WHERE THE VALUE IS, and why this practice sheet exists at all: every part of the assessment
version depends on the student having recorded things AS THEY HAPPENED. Parts D and E cannot
be reconstructed honestly at the end, and students discover this in week nine of the assessed
project, which is far too late. So the practice sheet exists to make them find that out on a
build where it does not count — and it adds what the assessment cannot:

  Part A   click-by-click running order for the planning meeting, because "hold a planning
           meeting" is not an instruction anyone can follow the first time
  Part C   how to actually chair a meeting, and how to arrange being observed
  Part D   what a usable reflection looks like versus a tidy one, and a standing instruction
           to keep a running note from day one
  Part E   how to give feedback to someone you will still be sitting next to tomorrow

The observed meeting is peer-or-teacher observed here; nobody signs anything off for real.

No marking criteria, no UoC tags. Rendered by the assessment's own renderer in
s1_cl3_at2_run_sheet, with these lists passed in.
"""

SITE = "https://yat.timbaird.com"
STATE = "s1-cl3-at2"
PROJECT = f"{SITE}/intranet/{STATE}/projects/website-improvement"
ICT = f"{SITE}/intranet/{STATE}/ict"
POLICY = f"{SITE}/intranet/{STATE}/policies"

# ---------------------------------------------------------------- front matter

SCENARIO = [
    "YAT College has approved the improvement design for the public website's cloud "
    "infrastructure. Your MP Tech Solutions team now implements it. The team is four members, "
    "each owning one cloud component — network, compute, database, or storage — and together you "
    "produce one integrated, deployable template.",
    "You are an MTS Consultant reporting to Pat Lin (MTS Senior Consultant). Sam Walker (YAT ICT "
    "Manager) is the client. You implement the agreed design; you do not redesign it.",
    "This is practice. Nothing here is assessed. What is being rehearsed is not the code — it is "
    "how you work as part of the team, and, just as much, the habit of writing things down while "
    "they are happening. The assessed version of this workbook cannot be filled in honestly at "
    "the end, and finding that out here is the entire point.",
]

INSTRUCTIONS = [
    "This worksheet is yours. Everyone in your team has one and each of you fills in your own, "
    "including where you are recording something the team agreed together.",
    "Part A is a meeting agenda. Work through it with your team in the room: talk about each item, "
    "agree it, then write it down. It tells you how to run the meeting as well as what to cover.",
    "Part B is the actual build. Your code is submitted as itself; the worksheet only records "
    "where it is and what you contributed.",
    "Part C is you leading a meeting with someone watching — your teacher, or a classmate from "
    "another team. Arrange it early.",
    "READ THIS ONE TWICE. Parts D and E run across the whole project and cannot be written "
    "afterwards. Start a running note today — a document, a notebook, anything — and add to it the "
    "day something happens. Students who skip this in the assessment lose real marks for work they "
    "genuinely did but cannot describe.",
]

HOW_ASSESSED = [
    ("What this rehearses", "your teamwork and leadership — planning, allocating, facilitating, "
                            "coaching, supporting, monitoring and reviewing"),
    ("What it does not", "the quality of the CloudFormation. The technical work is the vehicle, "
                         "not the subject"),
    ("Your team", "four members, one cloud component each — network, compute, database, storage"),
    ("The build", "the website improvement your team designed — which starts from a single "
                  "instance with no load balancer, so the components are not evenly sized. That "
                  "is a planning problem, and it is task 5's."),
    ("The observed meeting", "one team meeting that you lead, watched by your teacher or a "
                             "classmate from another team. Nothing is signed off for real"),
    ("The running note", "start one today. Parts D and E depend on it entirely"),
]

# ---------------------------------------------------------------- Part A — the planning meeting

PLAN = [
    dict(n=1, title="Agree what the team is here to do",
         resources=[
             ("Improvement Requirements — the outcomes the client has asked for",
              f"{PROJECT}/improvement-requirements"),
             ("Engagement Role Brief — what MTS is engaged to deliver", f"{PROJECT}/role-brief"),
         ],
         prompt="With your team: agree what you are collectively here to achieve, what each of you "
                "is responsible for, and what has to exist at the end for the engagement to be "
                "done. Talk about it first, then record what the team agreed, in your own words.",
         given=1, blank_rows=7, exemplar=1,
         table=(["", "What the team agreed"],
                [["Required outcome — how we know it is good enough",
                  "one template that deploys clean as a change-set onto the baseline, with each "
                  "component's part reviewed by one other member. Note this row is a TEST someone "
                  "could apply, not an aspiration — 'it works well' is not something you can check."],
                 ["Our common objective", ""],
                 ["Required outcome — the deliverable", ""],
                 ["Responsibilities — network", ""],
                 ["Responsibilities — compute", ""],
                 ["Responsibilities — database", ""],
                 ["Responsibilities — storage", ""]]),
         clicks=["Get everyone in one place with the design open. This meeting does not work over "
                 "chat.",
                 "Read the objective row out loud once you have written it. If two people would "
                 "describe the job differently, you have not agreed it yet.",
                 "Write it in your own words in your own worksheet. Four identical worksheets are "
                 "a sign one person talked and three typed.",
                 "Assign a note-taker for the meeting — but everyone still fills in their own "
                 "sheet afterwards."],
         consider=["Copying the Improvement Requirements into the objective row restates the "
                   "client's ask. What is YOUR team's job, in your words?",
                   "'Required outcome' means something that has to exist and could be checked. "
                   "What would you point at to say you were done?",
                   "Does every member know what the other three are responsible for? Ask them."]),

    dict(n=2, title="Set what is expected of each member",
         resources=[
             ("Acceptable Use Policy — the code of conduct your team works under",
              f"{POLICY}/acceptable-use"),
         ],
         prompt="With your team: agree what each member is expected to produce, by when, and how "
                "you expect each other to behave while doing it. Behaviours matter as much as "
                "deliverables — most teams that struggle do not struggle over the work.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Member", "Expected outcome", "Goal we can measure", "Behaviours we agreed"],
                [["Where these behaviours come from",
                  "the YAT Acceptable Use Policy and code of conduct",
                  "Not a member — a row that anchors the last column to something outside the "
                  "team's opinion.",
                  "Go and read the policy before you fill this in. Agreeing 'be respectful' "
                  "without reference to anything is what every team does and it helps nobody at "
                  "the moment it is needed."],
                 ["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]),
         clicks=["Do the deliverables column first — it is the easy one and it warms the group up.",
                 "Then do behaviours, and make someone say out loud what 'let the team know if you "
                 "are stuck' actually means. By when? Told to whom?",
                 "Write the agreed behaviours somewhere the whole team can see them later, not "
                 "only in four separate worksheets.",
                 "Check every member has a measurable goal. 'Finish the compute component' is not "
                 "measurable; 'the compute component validates and deploys by Friday' is."],
         consider=["What happens if someone does not meet an expectation? You are about to agree "
                   "that in task 3 — notice that it only works if the expectation was specific.",
                   "Which behaviour would your team most likely break under pressure? Is it on the "
                   "list?",
                   "Are the four workloads actually even? The website's compute component is much "
                   "bigger than its storage one. Does that change what you expect of each person?"]),

    dict(n=3, title="Agree how you will hold each other accountable",
         prompt="With your team: agree how you will know whether people are on track, and what you "
                "will do when someone is not. Decide this now, while everyone is comfortable — the "
                "point of agreeing it in advance is that nobody has to invent it in the moment.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Strategy", "How it works", "Who does it"],
                [["How we check progress",
                  "a ten-minute stand-up at the start of each session: what I did, what I am doing, "
                  "what is blocking me",
                  "Everyone, in turn. The example is deliberately the most ordinary answer "
                  "available — this task is not asking for something clever, it is asking for "
                  "something the team will actually do."],
                 ["How we make work visible", "", ""],
                 ["What we do when someone falls behind", "", ""],
                 ["How we raise a problem with each other", "", ""],
                 ["When we escalate outside the team", "", ""]]),
         clicks=["Agree the check-in rhythm first and put it in everyone's calendar before you "
                 "leave the room.",
                 "For 'what we do when someone falls behind', make the team say the first step out "
                 "loud. Usually it is 'someone asks them', and agreeing WHO makes it happen.",
                 "Agree what 'escalate' means here — for you it means telling your teacher, and "
                 "agreeing now that it is not a betrayal makes it possible later."],
         consider=["'We will communicate well' is not a strategy. Could a stranger follow each row "
                   "of your table?",
                   "How will you know someone is behind before they tell you?",
                   "The person who falls behind is often the one who has stopped coming to the "
                   "stand-up. Does your plan catch that?"]),

    dict(n=4, title="Plan for what could go wrong",
         prompt="With your team: work out what could disrupt you, and agree what you would do about "
                "each one. Think about people, not just technology — the most common disruption to "
                "a four-person team is one of the four not being there.",
         given=1, blank_rows=7, exemplar=1,
         table=(["What could happen", "How likely", "What we would do"],
                [["A member is away unexpectedly", "likely at least once",
                  "Name who picks up which component, and agree now that the work is kept "
                  "somewhere the others can reach it. The response has to be an ACTION — 'we would "
                  "manage' is not a contingency."],
                 ["A member's component turns out much bigger than expected", "", ""],
                 ["Someone's work has to be re-allocated", "", ""],
                 ["The person who understands one component is away at integration", "", ""],
                 ["The components do not integrate cleanly", "", ""],
                 ["", "", ""]]),
         consider=["Most of these rows are about people, and that is deliberate. If your answers "
                   "are all technical, read the rows again.",
                   "Could anyone else on the team pick up your component tomorrow? What would they "
                   "need from you for that to be true?",
                   "The compute component on this build is the biggest — it has to create a load "
                   "balancer and an Auto Scaling group where neither exists. What is your plan if "
                   "it is not done in time?",
                   "'We would work harder' is not a contingency. Neither is 'we would ask the "
                   "teacher'."]),

    dict(n=5, title="Allocate the work",
         prompt="With your team: allocate the four components, and give each other real "
                "instruction — what the component covers, where it touches someone else's, and "
                "what done looks like. Allocate on the basis of what people are good at or want to "
                "develop, and record which of those it was.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Component", "Who", "Why them", "The instruction they were given",
                 "Done looks like"],
                [["Integration — who owns it", "", "",
                  "Somebody has to own bringing the four together, and it is a job, not a moment. "
                  "Allocate it explicitly.",
                  "One template that validates and previews cleanly as a change-set."],
                 ["Network", "", "", "", ""],
                 ["Compute", "", "", "", ""],
                 ["Database", "", "", "", ""],
                 ["Storage", "", "", "", ""]]),
         clicks=["Before allocating, agree out loud where the components touch: compute needs "
                 "subnets from network; storage and compute both touch where media lives; database "
                 "needs the security group the network owner creates.",
                 "Ask each person what they want to get better at. Allocating purely on who is "
                 "already good at something is efficient and teaches nobody anything.",
                 "For 'the instruction they were given', write what you would need if you were "
                 "picking that component up cold.",
                 "Agree the seams in writing — the names of the things one component hands to "
                 "another. Most integration pain is two people naming the same thing differently."],
         consider=["Are the four components the same size on this build? They are not. What did "
                   "the team do about that — and is the answer recorded anywhere?",
                   "Did you allocate on expertise or on development? Both are legitimate and the "
                   "task asks you to say which.",
                   "Does each person know what 'done' is for their component, in a form someone "
                   "else could check?"]),

    dict(n=6, title="Agree how you will work with people outside the team",
         prompt="With your team: identify who outside the team you will need, and what for. Note "
                "where another team or another person could help you — a team that only ever talks "
                "to itself misses things.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Who", "What we need from them", "How we will communicate our objectives to them"],
                [["Another team working the same build",
                  "a second opinion on the seams between components, and whatever they hit first",
                  "Show them the design and the component split, and ask what broke for them. The "
                  "row that most teams never write, and the one that saves the most time."],
                 ["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""]]),
         consider=["A row naming only your teacher is thin. Who else genuinely has something you "
                   "need?",
                   "What would you have to tell an outsider for their help to be useful? That is "
                   "the third column.",
                   "Is there someone whose input you need at a particular MOMENT rather than in "
                   "general? Put the timing in."]),
]

# ---------------------------------------------------------------- Part B — the work itself

WORK = [
    dict(n=7, title="Do your allocated work, and record where it is",
         prompt="Build your component of the approved design, and keep your work where the team "
                "can see it. Your code is submitted as itself, not copied into this worksheet — "
                "record here where it lives and what part of it is yours.",
         given=1, blank_rows=6, exemplar=1,
         table=(["", "Your entry"],
                [["Anything I handed to, or took from, another member",
                  "the subnet IDs the network component creates, which my compute component "
                  "consumes — agreed as outputs on the first day rather than at integration"],
                 ["My allocated component", ""],
                 ["Where the team's work is kept", ""],
                 ["Where my own contribution is, specifically", ""],
                 ["What state it is in", ""]]),
         clicks=["Agree with your team where the work lives before anyone writes anything — a "
                 "shared repository, a shared folder, whatever you can all reach.",
                 "Keep your component in its own file while you work on it. Four people editing "
                 "one file is a lesson nobody needs twice.",
                 "Validate your own component before you hand it to integration. cfn-lint or the "
                 "console's own validation will catch most of it.",
                 "Write down what you took from and gave to other components AS you find out — "
                 "this is the first row that depends on the running note."],
         consider=["Could someone point at the integrated template and say which parts are yours? "
                   "If not, what would make that possible?",
                   "Is your work reachable by the rest of the team right now, or is it on your "
                   "machine?",
                   "The technical quality is not what is being rehearsed here. Doing what you were "
                   "allocated, and keeping it visible, is."]),

    dict(n=8, title="Integrate and confirm the team's build",
         prompt="With your team: bring the four components into one deployable template, validate "
                "it, and agree together that it is ready. Record what integration actually took — "
                "components rarely fit together first time, and how the team handled that is worth "
                "more here than a clean result.",
         given=1, blank_rows=6, exemplar=1,
         table=(["", "Your entry"],
                [["What did not fit first time",
                  "whatever it was for you — a name that did not match, two people creating the "
                  "same resource, a dependency nobody owned. If nothing did, look harder before "
                  "you write 'nothing'; it is almost never true."],
                 ["Who owned the integration", ""],
                 ["How the team worked out what to do", ""],
                 ["My part in resolving it", ""],
                 ["How the team agreed it was ready", ""]]),
         clicks=["Integrate earlier than feels comfortable — a rough integration in week one finds "
                 "the naming mismatches while they are cheap.",
                 "Run the change-set preview against the deployed baseline. It shows what would be "
                 "added, modified and replaced without changing anything.",
                 "Anything showing a replacement it should not — stop and work out why together. "
                 "That conversation is the most useful five minutes of the project.",
                 "Agree 'ready' explicitly, out loud, as a team. Otherwise one person decides and "
                 "three assume."],
         consider=["What was YOUR part in resolving what integration surfaced? Not the team's — "
                   "yours.",
                   "Did the team find the problem, or did one person find it and fix it quietly? "
                   "Those evidence different things.",
                   "Did anything change in how the team worked because of what integration "
                   "surfaced? That is worth recording."]),
]

# ---------------------------------------------------------------- Part C — the observed meeting

MEETING = [
    dict(n=9, title="Lead a team meeting, with someone observing",
         prompt="Lead one of your team's meetings while your teacher, or a classmate from another "
                "team, watches. Pick one where there is something to actually coordinate — "
                "allocating work, working through a problem, or getting the integration agreed — "
                "because that gives you something to lead. Record the meeting below.",
         given=1, blank_rows=8, exemplar=1,
         table=(["Meeting record", "Your entry"],
                [["What you did to open it — the objectives you communicated",
                  "the row that is easiest to forget and most visible to an observer. Two "
                  "sentences: why we are here, and what we need to have decided by the end."],
                 ["Date and time", ""],
                 ["Type of meeting", ""],
                 ["Who attended", ""],
                 ["What the meeting was for", ""],
                 ["What was allocated or confirmed, and to whom", ""],
                 ["How you made sure everyone contributed", ""]]),
         clicks=["Arrange the observation now, not in the last week. In the assessment this is the "
                 "single most common thing students leave too late.",
                 "Pick a meeting with real content. A stand-up where everyone says 'same as "
                 "yesterday' gives you nothing to lead.",
                 "Open by saying why you are all there and what has to be decided. Out loud, in "
                 "two sentences.",
                 "Watch who has not spoken and ask them something directly. That single habit is "
                 "most of what facilitation looks like from the outside.",
                 "Close by saying who is doing what next. If you cannot, the meeting has not "
                 "finished.",
                 "Fill in the record immediately afterwards, while you remember it."],
         consider=["What is your meeting actually FOR? If you cannot answer in one sentence, "
                   "neither can anyone attending.",
                   "Who in your team talks least? What will you do about that, specifically?",
                   "Did you allocate anything, or only discuss? The assessed version looks for "
                   "tasks allocated with instruction.",
                   "How long did it run, and how long did you intend?"]),

    dict(n=10, title="Observation notes",
         prompt="Whoever watched completes this at the end of the meeting. Nothing is signed off "
                "for real here — the point is to hear what someone outside your team saw, while "
                "there is still time to do something about it. Ask them to be blunt.",
         given=2, blank_rows=8, exemplar=1,
         table=(["Observed", "Demonstrated?", "Note"],
                [["Communicated the team's objectives and the meeting's purpose", "—",
                  "The observer writes what they actually saw, not a grade. 'Opened by listing "
                  "tasks; never said why the meeting was happening' is worth ten times "
                  "'satisfactory'."],
                 ["Allocated or confirmed tasks and gave appropriate instruction", "", ""],
                 ["Facilitated open, respectful collaboration, including quieter members", "", ""],
                 ["Coached or supported a member toward the team goals", "", ""],
                 ["Facilitated the team to identify and resolve an issue", "", ""],
                 ["Managed a conflict or challenge constructively", "", ""],
                 ["Monitored progress and gave constructive feedback", "", ""]]),
         clicks=["Hand this page to your observer before the meeting starts so they know what to "
                 "watch for.",
                 "Afterwards, ask them the one question that matters: what would you have done "
                 "differently?",
                 "Write their answer down even if you disagree with it."],
         consider=["Several rows will be blank because the meeting did not call for them. That is "
                   "normal and it costs nothing — in the assessed version those criteria are "
                   "carried by Part D, not by the meeting.",
                   "Which row surprised you? That is the one to work on.",
                   "If your observer wrote only positive things, they were being kind rather than "
                   "useful. Ask again."]),
]

# ---------------------------------------------------------------- Part D — across the project

RUNNING = [
    dict(n=11, title="Describe a conflict or challenge you dealt with during the project",
         prompt="Describe a conflict or challenge you personally dealt with — a disagreement about "
                "the work, someone not delivering, a difficult conversation, or work that had to "
                "be taken off someone. Say what happened, what you did about it, and how it turned "
                "out. Write about the parts that did not go well too: an honest account of "
                "something you handled imperfectly is worth more than a tidy one.",
         points=[
             "what actually happened, in enough detail that the situation is clear",
             "what you did — the specific action, not 'I communicated'",
             "why you chose that over the alternative",
             "how it turned out, including if it did not fully resolve",
             "the connection to the behaviours the team agreed in task 2",
             "what you would do differently",
         ],
         consider=["Write this the week it happens. Reconstructed at the end it will be vague, and "
                   "vague is what loses marks in the assessed version.",
                   "'I communicated with them' describes nothing. What did you say, to whom, and "
                   "when?",
                   "A conflict does not have to be a row. Two people quietly building the same "
                   "thing, or someone going silent, are the common ones.",
                   "If you genuinely had no conflict at all, you were either not involved or you "
                   "are not being frank with yourself. Which?",
                   "Did the way you handled it match what your team agreed in task 2? Say so "
                   "either way."]),

    dict(n=12, title="Describe a time you coached or helped a team member",
         prompt="Describe a situation where you helped or coached someone on your team — explaining "
                "something they were stuck on, working through a problem with them, or supporting "
                "them to get back on track. Say what they needed, what you did, and what changed. "
                "Helping someone solve their own problem counts for more than solving it for them.",
         points=[
             "who needed help and what with — the specific difficulty",
             "how you noticed, or how it was raised with you",
             "what you actually did: explained, paired, asked questions, took something off them",
             "why that suited that person and that problem",
             "what changed — what they could do afterwards",
             "the effect on the team, not just on the task",
         ],
         consider=["Did you fix their problem or help them fix it? Both are worth doing and only "
                   "one is coaching.",
                   "What could they do afterwards that they could not before? If the answer is "
                   "nothing, you did their work.",
                   "How did you know they were stuck? Noticing is part of the skill.",
                   "The smallest instances count. Ten minutes at someone's screen is a real "
                   "example if you can say what changed."]),

    dict(n=13, title="Describe an issue the team hit, and your part in resolving it",
         prompt="Describe a task-related problem or inefficiency your team ran into, and your part "
                "in sorting it out. The interesting ones are usually nobody's fault — a dependency "
                "nobody spotted, two people building the same thing, a decision nobody actually "
                "made. Say how the team found it and what you did to help the team resolve it.",
         points=[
             "the issue, and how it came to light",
             "how the team worked out what to do — who was involved and how it was discussed",
             "your own part: raising it, running the discussion, proposing the option, getting "
             "the decision made",
             "what was decided and whether it worked",
             "anything the team changed in how it worked so it would not recur",
         ],
         consider=["This one is about facilitating the TEAM. An account of you fixing it alone "
                   "evidences problem solving but not facilitation — say what you did to get the "
                   "team to a decision.",
                   "Integration usually supplies this. What did it surface for you?",
                   "Did anything change in how the team worked afterwards? That is the strongest "
                   "part of the answer.",
                   "'We had a meeting about it' — and? Who said what, and how was it decided?"]),
]

# ---------------------------------------------------------------- Part E — review and close out

REVIEW = [
    dict(n=14, title="Measure the team against the plan",
         prompt="Go back to the expectations you agreed in task 2 and measure what actually "
                "happened against them, member by member — including yourself. Be fair and be "
                "specific. This is a professional judgement, not a popularity contest.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Member", "What was expected", "What happened", "Met?"],
                [["Where your assessment came from",
                  "your own observation, what the team said at the review, and the work itself",
                  "Not a member — the row that stops this being one person's opinion. The assessed "
                  "version looks for evidence that you gathered input rather than judged alone.",
                  "—"],
                 ["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]),
         consider=["Measure against what was actually agreed in task 2. If the expectations were "
                   "vague, you will find that out here — which is a lesson about task 2.",
                   "Include yourself, and be as specific about your own shortfalls as about "
                   "anyone else's.",
                   "'Met' with no evidence beside it is an impression. What did you observe?",
                   "Did you ask the team, or decide alone?"]),

    dict(n=15, title="The feedback you gave",
         prompt="Record the performance feedback you gave each member, and when. Feedback given at "
                "the end of a project is a report card; feedback given during it is useful. Note "
                "which of yours was which — and if some of it was late, say so.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Member", "What you told them", "When", "How they responded"],
                [["", "",
                  "The 'when' column is the point of this task. Feedback in week two changed "
                  "something; the same words in week ten changed nothing.",
                  ""],
                 ["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]),
         clicks=["Give feedback to one person this week rather than saving it up. That is the "
                 "whole rehearsal.",
                 "Say the specific thing, not the general one: 'the subnet outputs you added made "
                 "my component work first time' beats 'good job'.",
                 "For anything critical, say it privately and say it about the work.",
                 "Write down what you said and when, the same day."],
         consider=["Was any of your feedback critical? All-praise feedback is comfortable and "
                   "evidences half the item.",
                   "How did they respond — and did anything change?",
                   "If all your feedback landed at the end, say so. Noticing that about yourself "
                   "is worth more than pretending otherwise."]),

    dict(n=16, title="Development opportunities and what you did about them",
         prompt="Identify what would make each member — and the team as a whole — better next "
                "time, and say what was actually done about it during this project. An identified "
                "opportunity that nobody acted on is a note; what is wanted is an action that was "
                "actually taken.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Who", "Development need", "The action plan", "What was actually done"],
                [["The team as a whole", "", "",
                  "The last column is where this task is won or lost. An action plan with nothing "
                  "in the fourth column is a recommendation, and recommendations are not what is "
                  "being asked for."],
                 ["", "", "", ""], ["", "", "", ""], ["", "", "", ""],
                 ["Yourself", "", "", ""]]),
         consider=["Act on at least one of these DURING the project, not after. That is what makes "
                   "the fourth column fillable.",
                   "What would make the team better next time — not what would make the template "
                   "better?",
                   "Include yourself, honestly. What did this project show you that you need?"]),

    dict(n=17, title="Reflect on how you led",
         prompt="Look back over the project at your own leadership. What did you do well, what did "
                "you do badly, and what would you do differently with the same team tomorrow? "
                "Write this properly — it is the one place in the whole exercise where the honest "
                "answer is worth more than the impressive one.",
         points=[
             "something specific you did well, with the evidence for it",
             "something you did badly or late, named plainly",
             "how you behaved when the team was under pressure",
             "what you would do differently with the same team tomorrow",
             "what you now know about leading that you did not at task 1",
         ],
         consider=["A reflection that identifies no weakness has not reflected.",
                   "Under pressure is where this is actually tested. What were you like in the "
                   "last week?",
                   "Go back and read your task 1 answer. What did you not understand then?",
                   "This is practice. Nobody is marking it, which makes it the safest place you "
                   "will ever have to write the honest version. Use that."]),
]
