#!/usr/bin/env python3
"""The S1-CL2 AT1 Part C PRACTICE approval run sheet — content.

Same shape as the AT1 Part C assessment workbook, on the LMS engagement rather than the
website one.

WHAT PRACTISING THIS IS FOR. Part C is the only part of AT1 that cannot be practised by
writing. It is a live session: the student walks a stakeholder through two documents they
wrote, answers questions on them, takes feedback and closes the loop. The failure modes are
all behavioural — reading the document aloud, running out of time in the first three minutes,
being unable to explain a decision that is written in their own plan, or presenting well and
never actually asking for approval.

So the practice version rehearses the SESSION, not the paperwork. Sam Walker is played by
whoever will do it — the teacher, or a classmate who has worked the same practice run sheet
and can therefore ask real questions. Nothing here is marked, nothing is signed, and no
document is lodged for real; the point is to have said it out loud once before the assessment
is the first time.

WHAT PRACTICE ADDS: "Things to consider" on every task, an exemplar row showing the shape of
an answer, and — on the walkthrough itself — click-by-click running order for the session,
because "present your work" is not an instruction anyone can follow the first time.

Rendered by the assessment's own renderer in s1_cl2_at1_part_c_run_sheet, with these lists
passed in.
"""

SITE = "https://yat.timbaird.com"
STATE = "s1-cl2-at1"
PROJECT = f"{SITE}/intranet/{STATE}/projects/lms-global-expansion"
POLICY = f"{SITE}/intranet/{STATE}/policies"

# ---------------------------------------------------------------- front matter

INTRO = [
    "This is the approval gate, rehearsed. You walk Sam Walker (YAT ICT Manager — played by your "
    "teacher, or by a classmate who has worked this run sheet) through the LMS design you "
    "produced in Part A and the disaster recovery plan you produced in Part B, answer questions "
    "on both, respond to the feedback you are given, and close the loop.",
    "Nothing here is assessed and nothing is signed off for real. This is the one part of the "
    "assessment you cannot rehearse by writing, so rehearse it by doing it — badly the first "
    "time, which is the entire point of practice.",
    "There is no slide deck to build, here or in the assessment. You are walking your listener "
    "through two documents you have already written, which is what a consultant does. Bring "
    "them, printed or on screen, and know your way around them.",
]

EVENT = [
    ("Format", "in person, or by video call — whatever you can arrange"),
    ("Duration", "10–15 minutes walking through, then about 5 minutes of questions and feedback. "
                 "Time it. Running out of time is the most common way this goes wrong."),
    ("Bring", "your completed Part A practice worksheet and your completed practice Disaster "
              "Recovery Plan"),
    ("Send beforehand", "both documents, so whoever is playing Sam has actually read them and can "
                        "ask about something specific"),
    ("Who plays Sam", "your teacher, or a classmate who has worked the same run sheet. A "
                      "classmate who has done the work asks better questions than one who has "
                      "not."),
]

RESOURCES = [
    ("Records Management Policy — the lodgement protocol a completed engagement document follows",
     f"{POLICY}/records-management"),
    ("Engagement Role Brief — who signs off what on this engagement",
     f"{PROJECT}/role-brief"),
]

# ---------------------------------------------------------------- the tasks

APPROVAL = [
    dict(n=38, title="Plan your walkthrough",
         prompt="Plan the order you will take Sam through the two documents, and for each part "
                "write down the ONE point you want Sam to understand. You have 10 to 15 minutes, "
                "which is not long enough to read your work out — so decide what matters.",
         given=1, blank_rows=8, exemplar=1,
         table=(["What you cover", "The one point Sam should take away", "Roughly how long"],
                [["Why the engagement exists",
                  "the India campus makes the LMS a system with users on the other side of an "
                  "ocean — that is why any of this is worth doing",
                  "1 min. Notice the column is 'the ONE point', not a summary. If you cannot say "
                  "it in a sentence you will not say it in a minute."],
                 ["The web-scale design", "", ""],
                 ["The microservice", "", ""],
                 ["The risks you assessed", "", ""],
                 ["The recovery strategy", "", ""],
                 ["What you are asking for", "", ""],
                 ["What you deliberately did not do", "", ""]]),
         clicks=["Add up your minutes. If the total is over 15, cut something now rather than "
                 "discovering it live.",
                 "Open both documents and put a marker at each place you will need to turn to. "
                 "Hunting through a document while someone watches is what eats the time.",
                 "Decide how you will open. One sentence on why the engagement exists beats "
                 "'so, um, I did the design first'.",
                 "Decide how you will close. You are asking for approval to proceed — say those "
                 "words.",
                 "Say the whole thing out loud once, to nobody, with a timer running. It will be "
                 "worse than you expect and shorter than you expect."],
         consider=["Which of these could you drop entirely if you were running out of time? "
                   "Decide now, not at minute twelve.",
                   "Sam has read both documents. What is the value of you being in the room — "
                   "what can you say that the documents do not?",
                   "The last row is the exclusions. Why would you volunteer what you did NOT do?",
                   "Is there anything in your design you are least confident about? That is "
                   "probably where you should spend a minute rather than hoping it is not "
                   "raised."]),

    dict(n=39, title="Anticipate the questions",
         prompt="Write down the questions you would ask if you were Sam, and your answer to each. "
                "The ones worth preparing are the ones where you made a choice someone could "
                "reasonably disagree with — that is exactly where you will be asked.",
         given=1, blank_rows=7, exemplar=1,
         table=(["Question you expect", "Your answer"],
                [["Do we have to move the whole LMS to India?",
                  "No — the obligation is on activity logs. The residency document is explicit "
                  "that the main LMS data may stay in Australia. This is the shape to aim for: a "
                  "direct answer, then the document it comes from."],
                 ["", ""], ["", ""], ["", ""], ["", ""], ["", ""]]),
         consider=["Go through your own design looking for decisions with a defensible "
                   "alternative. Each one is a question.",
                   "What does this cost YAT to run? You will be asked, and 'I did not cost it' is "
                   "a worse answer than a rough one with its basis stated.",
                   "What happens if the audit-log service is down for an hour? You answered this "
                   "in Part A task 19 — can you say it out loud in fifteen seconds?",
                   "'How do we know the plan works?' is the question with the uncomfortable "
                   "answer. What is it?",
                   "Which question would you least like to be asked? Prepare that one first."]),

    dict(n=40, title="The walkthrough",
         prompt="Do it. Then record the session: when it happened, who was there, and what you "
                "actually covered. Fill this in immediately afterwards, while you remember it.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Record", "Your entry"],
                [["What you covered",
                  "per your task 38 plan, noting anything you changed on the day — and something "
                  "always changes on the day, which is worth recording rather than tidying away"],
                 ["Date and time of the session", ""],
                 ["Who played Sam, and who else was there", ""],
                 ["Documents you walked through", ""],
                 ["Questions you were asked", ""]]),
         clicks=["Open with why the engagement exists. One sentence, then move.",
                 "Walk the design at the level of decisions, not components. 'I put an edge layer "
                 "in front of the load balancer because the India cohort is 10,000 km from "
                 "Sydney' — not a tour of the diagram.",
                 "When you reach the recovery strategy, give the recommendation first and the "
                 "reasoning second. Sam wants to know what you are recommending before why.",
                 "Do not read from the document. Look at your listener. The document is in front "
                 "of them already.",
                 "When you are asked something you do not know, say so and say what you would do "
                 "to find out. Inventing an answer in front of a client is the one unrecoverable "
                 "move.",
                 "Ask for approval to proceed to implementation. Out loud. In those words.",
                 "Afterwards, before you do anything else, fill in the table above."],
         consider=["How did the timing go? If you overran, what would you cut next time?",
                   "Which question did you answer worst? That is the most useful thing you will "
                   "learn today.",
                   "Did you explain a decision, or describe a design? There is a large difference "
                   "and your listener felt it.",
                   "Did you actually ask for approval, or did you stop talking and wait?"]),

    dict(n=41, title="Feedback sought, and your response",
         prompt="Record the feedback Sam gave you and what you did about it. Whoever is playing "
                "Sam should give you at least one thing to change — that is the point of an "
                "approval gate. For each item, say what you were told, what you decided to do, "
                "and if you disagreed, say that and why.",
         given=1, blank_rows=6, exemplar=1,
         table=(["Feedback from Sam", "Your response", "Change made?"],
                [["e.g. the recovery steps do not say who re-establishes the campus VPN link",
                  "accepted — assigned to YAT ICT and added as its own step with a duration",
                  "Yes. The pattern matters: what you were told, what you decided, and whether "
                  "anything actually changed."],
                 ["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""]]),
         consider=["Did you ASK for feedback, or wait to be corrected? They are different things "
                   "and only one of them is what the assessment is looking for.",
                   "Agreeing with everything is not responding to feedback. Was there anything "
                   "you should have pushed back on?",
                   "A reasoned disagreement, recorded, is a perfectly good response. What would "
                   "one look like here?",
                   "Go and make one of the changes now, while you remember why."]),

    dict(n=42, title="Lodge the plan",
         resources=[
             ("Records Management Policy — where a completed engagement document is lodged, and "
              "how it is retained", f"{POLICY}/records-management"),
         ],
         prompt="Work out how you would lodge the approved plan the way YAT requires. Read the "
                "Records Management Policy and follow it — record where it would be lodged, under "
                "what classification, and who can retrieve it. Nothing is really being filed "
                "here; what is being practised is reading a policy and doing what it says rather "
                "than what seems reasonable.",
         given=1, blank_rows=5, exemplar=1,
         table=(["Lodgement record", "Your entry"],
                [["Who can retrieve it, and how, during an outage",
                  "named roles, and a copy held outside the primary region — the point you made "
                  "yourself in Part B task 32, which is why this row is the one worth getting "
                  "right"],
                 ["Where it is lodged", ""],
                 ["Classification applied", ""],
                 ["Retention period", ""]]),
         consider=["Open the Records Management Policy and find the actual answer. Do not write "
                   "what sounds plausible — that is the habit this task exists to break.",
                   "Who is allowed to read a document classified Internal — ICT? Are engaged "
                   "consultants included, and under what?",
                   "You wrote in Part B that a plan nobody can reach during an outage is not a "
                   "plan. Does your lodgement answer contradict your own plan?"]),

    dict(n=43, title="Obtain sign-off",
         prompt="Ask for sign-off and record the decision — including if it is approval with "
                "conditions, which is a real outcome and not a failure. Nothing is really being "
                "approved; what is being practised is closing the loop rather than trailing off.",
         given=1, blank_rows=5, exemplar=1,
         table=(["Sign-off record", "Your entry"],
                [["Decision", "Approved / Approved with conditions / Not approved"],
                 ["Any conditions attached", ""],
                 ["Signed by", ""],
                 ["Date", ""]]),
         consider=["Did you ask, or did the session just end? Presenting well and never asking is "
                   "the most common way this task is failed.",
                   "'Approved with conditions' is a normal professional outcome. What conditions "
                   "would you expect on this engagement?",
                   "If the answer were 'not approved', what would you need to know before you "
                   "left the room?"]),
]
