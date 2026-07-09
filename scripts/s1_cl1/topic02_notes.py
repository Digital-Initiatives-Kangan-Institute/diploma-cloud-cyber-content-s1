"""Teacher speaker notes for Topic 02 — The case for change (S1-CL1).

One entry per teaching/activity slide. Keys are the EXACT slide title strings from
build_s1_cl1_topic02_deck.py so they match at build time. Read only by the teacher
(Presenter View), never shown to students.
"""

NOTES = {

    "The consultant's first real job": """
        Frame the whole Topic as the pivot from Topic 1: they can speak cloud now — today they DIAGNOSE.
        Set expectations, don't yet teach a section.
        • First bullet: literacy was the warm-up; the real consulting job is working out where the
          organisation is, where it needs to be, and the gap between. No solutions yet.
        • Second bullet: that's the whole job of a case for change — locate the client on the map before
          you plot a route.
        • Third bullet (bolded): the three moves — align to strategy → describe the current state → expose
          the gaps. Say them in that order; each depends on the one before.
        • Fourth bullet: these three become the OPENING SECTIONS of the business case (AT1 §3–§5). What
          they build today is directly the front half of the AT1 deliverable.
        Misconception to pre-empt: "we're picking a cloud solution today." No — diagnosis comes before
        prescription; solutions are Topic 3. Manage the student who jumps straight to "move it to AWS".
        Question to pose: "Before you can recommend a fix, what three things must you establish about the
        client?" — draws out strategy / current state / gap.
        UoC/AT1 tie: this Topic develops PC 1.1–1.3 and PE 1–3; the output is AT1 Part A §3–§5.
    """,

    "A case for change is evidence, not opinion": """
        The anchor framing for the Topic — a case for change is an EVIDENCE chain, not a hunch. Teach it
        deliberately; the three-question order is the skeleton of everything today.
        • Walk the three questions in order: where does the org want to go (strategy) → where is it now
          (current state) → what's missing to get there (gaps). Each answer feeds the next.
        • Stress the last two bullets: they are NOT choosing a solution yet — they're proving the problem
          is real and worth solving. "Diagnose before you prescribe" (the magenta line) is the Topic's motto.
        Misconception to pre-empt: students treat "the case for change" as arguing FOR cloud. It isn't — it
        argues the problem exists; the solution could even be "renew on-prem". Keep it solution-neutral.
        Question to pose: "If a doctor prescribed before diagnosing, what would go wrong — and how is a rushed
        cloud recommendation the same mistake?"
        UoC/AT1 tie: PE 1–3 in sequence; this three-part spine maps one-to-one onto AT1 §3 / §4 / §5.
    """,

    "Start with strategy": """
        Open Section 1. Teach WHY the business case leads with strategy — it's what unlocks funding.
        • First two bullets: a board funds change that moves the organisation toward ITS OWN stated goals;
          so you lead by showing the initiative serves the strategy, not technology for its own sake.
        • Third bullet: define strategic alignment plainly — "here's what they said they want; here's how
          this delivers it." It's an argument, not a description.
        • Fourth bullet (bolded): it's the "why this, why now" that earns everything downstream. If you can't
          tie the initiative to a stated goal, the case is already weak.
        Misconception to pre-empt: "strategic alignment = describe the company." No — it's a targeted argument
        connecting THIS initiative to a specific organisational objective, with a citation.
        Question to pose: "YAT's board has limited money — why would 'the servers are old' persuade them less
        than 'this serves your national-growth goal'?" (funders back strategy, not maintenance).
        UoC/AT1 tie: PC 1.1 / PE 1 → AT1 §3 Strategic Alignment Analysis (criterion A1).
    """,

    "Read a strategic plan in three layers": """
        The how-to slide for Section 1 — teach students to READ a strategic plan structurally instead of
        skimming it. The three layers are the examinable technique.
        • Walk the layers top-down: business objectives (where the whole org is going, e.g. grow students
          15%/yr) → ICT goals (how ICT supports that, e.g. reduce in-house dependency, 99.9% for critical
          systems) → initiatives (the planned actions, e.g. move suitable systems to cloud).
        • The payoff (magenta line): trace YOUR initiative UP these layers to a real business objective, and
          pull only what's MATERIAL — don't recite the whole plan.
        Misconception to pre-empt: students copy every objective in the plan. No — most won't be relevant;
        selecting the material few and tracing them up is the analytical skill being marked.
        Question to pose: "Migrating Ledgerline — which ICT goal does it serve, and which business objective
        sits above that goal?" (traces the chain live).
        UoC/AT1 tie: PC 1.1 / PE 1 → AT1 §3; the "trace up, material only" habit is exactly what A1 rewards.
    """,

    "Add the outside view": """
        Second half of Section 1 — a strategic argument needs the EXTERNAL industry context, not just the
        client's internal plan.
        • First bullet: a plan doesn't exist in a vacuum; compare it against where the industry is heading.
        • Second bullet: name the trends that matter here — cloud adoption, managed services, OPEX over CAPEX,
          resilience. These are the yardsticks.
        • Third/fourth bullets: name BOTH directions — alignment (plan matches industry direction →
          strengthens the case) and divergence (plan lags or differs → a risk, or an opportunity to flag).
        Misconception to pre-empt: "industry context = cheerlead for cloud." No — a balanced analysis names
        where the client is behind AND where a trend might not fit them; honesty is the mark of analysis.
        Question to pose: "The sector is moving to managed cloud services — where does that ALIGN with YAT's
        plan, and is there anywhere it might DIVERGE for a small RTO?"
        UoC/AT1 tie: KE 4 (current/emerging trends and directions) → AT1 §3; the outside view is what lifts
        A1 from description to analysis.
    """,

    "What good looks like": """
        The quality checklist for Section 1 — read it as the marker's-eye view of a strong §3, right before
        they attempt it. Keep it short; it's a rubric, not new content.
        • Every claim CITED to the plan (e.g. "ICT Strategic Plan — ICT Goals") — no unsourced assertions.
        • MATERIAL items only — not the whole plan recited.
        • TRACES the initiative up to a real organisational goal (the three-layer move).
        • ALIGNMENT AND DIVERGENCE both named (magenta line) — balanced, not cheerleading.
        Misconception to pre-empt: "more is better." No — a padded §3 that recites the plan scores worse than
        a tight one that cites four material objectives and traces them.
        Question to pose: "If I marked your §3, what's the single fastest way to lose marks?" (uncited claims /
        reciting everything / no divergence named).
        UoC/AT1 tie: this is the A1 acceptance standard for AT1 §3 — hand them the bar before the activity.
    """,

    "Write a Strategic Alignment section": """
        Facilitation — the Section 1 practice; students draft §3 of the PRACTICE business case (Ledgerline).
        This mirrors AT1 §3 against a different system.
        Tell students: "In your working copy of the Business Case, write the Strategic Alignment section for
        moving YAT's Accounting System (Ledgerline) to the cloud. Argue it — don't just describe."
        Steps (put on the board):
        1. Read YAT's ICT Strategic Plan on the scenario intranet.
        2. Which ICT goals/objectives does this migration serve? Trace up to a business objective — CITE them.
        3. Add one or two points of industry context — where's the sector heading?
        4. Note both alignment and divergence honestly.
        Must produce: ~half a page — a cited strategic-alignment argument, traced up the three layers, with
        alignment AND divergence named.
        Timing: ~20 min then discuss. Where they get stuck: they DESCRIBE YAT instead of ARGUING alignment —
        circulate and push them to answer "which goal does this serve?"; also watch for uncited claims.
        Share-back prompt: take two answers and ask the room which one traces to a real business objective.
        No-leakage note: Ledgerline is the PRACTICE client — AT1 assesses the SAME skill on the LMS
        (comparable, not identical); keep them on the scenario plan here.
    """,

    "Current state is synthesis, not transcription": """
        Open Section 2 with its single governing idea — current state is SYNTHESIS, not a copy-paste of the
        IT docs. This is the one thing students most often get wrong.
        • First bullet: summarise the current environment IN YOUR OWN WORDS, focused on what's material to
          THIS decision.
        • Second bullet: the board needs the picture that explains why change is needed — not a reproduction
          of the source documents.
        • Third bullet (bolded): distil it down; don't transcribe it. Say the word "distil" out loud — it's
          the verb for the whole section.
        Misconception to pre-empt: "thorough = paste everything in." No — a wall of copied specs is a FAIL of
        synthesis; the skill is choosing and re-stating the material few in plain language.
        Question to pose: "If the board can already read the IT docs, what's YOUR value in the current-state
        section?" (you distil and interpret — you make it decision-relevant).
        UoC/AT1 tie: PC 1.2 / PE 2 → AT1 §4 Current State (criterion A2); "own words, material only" is A2.
    """,

    "The relevance filter": """
        The how-to for Section 2 — teach the KEEP/DROP filter that separates material facts from noise.
        • KEEP (if it bears on the decision): platform & stack, age/condition/capacity, availability today,
          dependencies & integrations, constraints, pain points. Read the list as "things that could change
          the renew-vs-migrate call".
        • DROP: detail that doesn't move the decision — printer counts, unrelated systems.
        • The sky-accent line: a good current state QUIETLY SURFACES the limitations that motivate the change
          — it sets up the gap analysis without shouting.
        Misconception to pre-empt: "keep vs drop is about importance." No — it's about RELEVANCE TO THIS
        DECISION; a fact can be true and important yet irrelevant to renew-vs-migrate, so it goes.
        Question to pose: "The Ledgerline server is 6 years old and there are 12 office printers — which fact
        do you keep, and why?" (age bears on renew-vs-migrate; printers don't).
        UoC/AT1 tie: PC 1.2 / PE 2 → AT1 §4; the filter is how A2 stays material rather than a data dump.
    """,

    "How to distil": """
        The three-step method that turns source docs into a synthesised current state — teach it as a
        repeatable procedure they'll run in the activity next.
        • Step 1: read the source docs — environment overview, server/app specs, consultation notes.
        • Step 2: for EACH fact ask "does this affect the renew-vs-migrate decision?" If no, cut it (this is
          the relevance filter applied).
        • Step 3: re-state what's left in PLAIN LANGUAGE, grouped — platform / workload / dependencies /
          condition-risk. Grouping is what makes it read as synthesis, not a list.
        • Aim ~half a page, no copy-paste (bolded).
        Misconception to pre-empt: "re-state = reword each sentence." No — you regroup and compress across
        documents; the output is shorter and organised by theme, not a paraphrase of every line.
        Question to pose: "You've got five source docs — what's the first question you ask of every fact in
        them?" ("does it affect the decision?").
        UoC/AT1 tie: PC 1.2 / PE 2 → AT1 §4; this procedure is exactly how a strong A2 gets written.
    """,

    "Add the Current State section": """
        Facilitation — the Section 2 practice; students draft §4 of the practice business case (Ledgerline),
        mirroring AT1 §4 on a different system.
        Tell students: "In your working copy of the Business Case, add the Current State section for the
        Accounting System (Ledgerline). Synthesise — in your own words, material facts only."
        Steps (put on the board):
        1. Use the Accounting application spec, server specs, operational costing, the ICT Environment
           Overview, and the consultation notes on the scenario intranet.
        2. Cover: platform & stack · workload (incl. month-end / EOFY peaks) · integrations (AD, O365, LMS
           fee-status, payroll, banking) · condition & constraints.
        3. Run the relevance filter on every fact; group what survives.
        Must produce: ~half a page, own words, grouped by theme, no verbatim copying.
        Timing: ~20 min then discuss. Where they get stuck: they PASTE spec tables verbatim — circulate and
        make them re-state in plain language; also watch for irrelevant detail creeping in.
        Share-back prompt: "Which limitation in your current state most obviously sets up a gap?" (bridges to
        Section 3).
        No-leakage note: Ledgerline is PRACTICE; AT1 assesses the same synthesis skill on the LMS —
        comparable, not identical. Keep them on the scenario source docs.
    """,

    "Gap analysis bridges “want” and “have”": """
        Open Section 3 — teach gap analysis as the BRIDGE that makes the problem concrete and hands the next
        stage its worklist.
        • First bullet: it bridges where we want to be (strategy + requirements) and where we are (your
          current state) — it literally joins §3 to §4.
        • Second/third bullets: it makes the problem CONCRETE and MEASURABLE, and it hands the next stage a
          list of changes to evaluate (the seed of Topic 3's options).
        • The green line: "No gap → no case." If you can't show a gap, there's no justified change — say it.
        Misconception to pre-empt: "the gap analysis is where I propose the solution." No — the "proposed
        change" is a CANDIDATE to evaluate later, not a decision; gap analysis proves the problem, Topic 3
        weighs the fix.
        Question to pose: "Where do the 'desired' and 'current' columns each come from?" (desired ← strategy
        + requirements; current ← your §4 synthesis — it's traceable both ways).
        UoC/AT1 tie: PC 1.3 / PE 3 → AT1 §5 Gap Analysis (criterion A3); it's the hinge into the options work.
    """,

    "Build the Gap Analysis": """
        Facilitation — the Section 3 practice; students build §5 of the practice business case (Ledgerline)
        as a structured gap table, mirroring AT1 §5.
        Tell students: "In your working copy of the Business Case, add the Gap Analysis for the Accounting
        System (Ledgerline) — a table of at least 3 rows, every column filled and traceable."
        Steps (put on the board):
        1. Draw objectives from your Strategic Alignment work + the migration requirements, e.g.: reduce
           in-house infrastructure dependency (ageing server); business-hours availability >=99.5% (RPO <=1h /
           RTO <=1 business day); keep financial data onshore + 7-year retention; size for month-end / EOFY
           peaks without year-round over-provisioning.
        2. Fill every column: objective → current → desired → gap → opportunity → proposed change.
        3. Check each row traces BACK to a real objective (from §3) and your current-state facts (from §4).
        Must produce: a >=3-row gap table, all six columns filled, each row traceable both ways.
        Timing: ~25 min then discuss. Where they get stuck: they jump to "move to AWS" in every "proposed
        change" cell — remind them proposed change is a CANDIDATE seed, not a chosen solution; and they leave
        "opportunity" blank — it's the bridge from gap to proposed change.
        Share-back prompt: take one row and trace it end-to-end — objective from the plan, current from §4.
        No-leakage note: Ledgerline is PRACTICE; AT1 assesses the gap-analysis skill on the LMS — comparable,
        not identical.
    """,

}
