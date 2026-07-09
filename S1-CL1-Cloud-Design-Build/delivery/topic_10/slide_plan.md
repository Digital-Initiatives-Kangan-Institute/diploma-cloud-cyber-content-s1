# Topic 10 Evidencing & documenting — Slide plan
> **Covers:** Topic 10 — see coverage.md
> **Subtitle:** Turn everything you've built into the Deployment Report

## Slides

### Opener
- [BESPOKE] The build becomes the deliverable
  - Topics 6–9 built, monitored, validated and justified the workload — capturing evidence the whole way.
  - Topic 10 assembles that into the Deployment Report — the single AT2 deliverable.
  - Four moves: organise the evidence, write the report, evidence your knowledge in context, and reflect.
  - No new resources — everything you need was captured as you built.
  kicker: no new building — write it up
  image: none
  notes:
    Frame this as the map for the whole Topic — the pivot from building to writing up. No new
    building today.
    • Goal: read it out — by the end they can turn the Topics 6–9 build into the Deployment Report.
    That report IS the AT2 deliverable; everything today assembles it.
    • Where this fits: last AT2 content Topic. They're MTS consultants; the report is what YAT's ICT
    team and auditors actually receive — the running system alone isn't the handover.
    • The four moves: organise the evidence, write the report, evidence the knowledge in context,
    reflect. Each maps to a section today.
    • Stress it: no new resources — everything they need was captured as they built.
    Misconception to pre-empt: "documentation is an afterthought / a diary of what I did." No — it IS
    the deliverable; the build is worthless to the client without the document that explains it.
    Question to pose: "If you left YAT tomorrow, what would their ICT team have — the running system,
    or the running system PLUS a document that lets them run and audit it?"
    UoC/AT2 tie: this Topic develops ICTCLD401 element 4; the Deployment Report (§1–§7 + Appendices
    A/B/C) is the single AT2 deliverable everything is marked in.

### C1 — Evidence into the appendices
- Teaches: [ICTCLD401 PC 4.3] · [ICTCLD401 PE 1 · PE 2]
- Kicker: make it traceable
- [BESPOKE] What makes evidence count
  - Good evidence is named, dated, and shows the Region and identity it was taken under.
  - It's organised and referenceable — so a reader can find the exact item the narrative cites.
  - A screenshot nobody can place, or an export with no label, proves nothing.
  kicker: traceable, or it proves nothing
  image: none
  notes:
    The primer on traceable evidence — teach this before they touch the filing. Sets the bar for C1.
    • Walk it: good evidence is named, dated, and shows the Region and identity it was taken under.
    • The load-bearing line: it's organised and referenceable — a reader can find the exact item the
    narrative cites.
    • Give the counter-example: an unplaceable screenshot, or an export with no label, proves nothing.
    Misconception to pre-empt: "a screenshot is evidence." Only if it's placeable — an image with no
    label, date or context is not evidence an auditor can use.
    Question to pose: "If I hand you a folder of 40 unnamed screenshots, can you prove the database is
    encrypted? What would each one need on it to count?"
    UoC/AT2 tie: ICTCLD401 PC 4.3 (save/store documentation per organisational policy); this is the
    standard C1 organises evidence to meet.
- [BESPOKE] Appendices A / B / C
  - Appendix A — build evidence: the named screenshots taken as you built each tier.
  - Appendix B — configuration exports: the settings of what you built (e.g. security-group rules, RDS config).
  - Appendix C — test and validation evidence: connectivity, scaling and recovery-objective results.
  - Label and number every item so §4–§6 can cross-reference it.
  kicker: where the evidence lives
  image: none
  notes:
    The filing system — the three homes for evidence. Keep it crisp; the point is knowing what goes
    where.
    • A = build screenshots (the named captures taken as they built each tier). B = configuration
    exports (the settings — security-group rules, RDS config). C = test & validation evidence
    (connectivity, scaling, recovery-objective results).
    • The load-bearing line: label and number EVERY item so §4–§6 can cross-reference it.
    Misconception to pre-empt: students dump everything into one pile / one appendix. The A/B/C split
    is what makes the report navigable — a reader jumps straight to the right kind of evidence.
    Question to pose (fire three quick): "A security-group rule export — which appendix? A screenshot
    of the instance running? A failover test result?" (B, A, C).
    UoC/AT2 tie: PE 1 · PE 2 — the built artefacts are the evidence, assembled here; Appendices A/B/C
    are the evidence home in the AT2 report.
- [BESPOKE] Organise what you captured
  - Gather every screenshot, export and test result you captured across the build.
  - Sort them into A / B / C; give each a clear label and number.
  - Note any gaps — and recapture while the lab is still standing.
  kicker: since Topic 6
  image: none
  notes:
    The how-to just before the activity — the concrete steps, and the one time-critical warning.
    • Gather every screenshot, export and test result captured across Topics 6–9.
    • Sort into A / B / C; give each item a clear label and number.
    • The accent line: note any gaps — and recapture WHILE THE LAB IS STILL STANDING.
    Misconception to pre-empt: "I'll recapture it later." The lab is ephemeral — once it's torn down
    the evidence is gone for good; recapture now, not next week.
    Question to pose: "What's the one thing you can do today that you can't do after the lab closes?"
    (recapture missing evidence).
    UoC/AT2 tie: PC 4.3; this frames the Build-your-appendices activity that follows.
- [EX] Build your appendices
  - Assemble Appendices A, B and C from the evidence you captured since Topic 6:
    - sort into screenshots / config exports / test evidence
    - label and number each item
  - Flag any gaps and recapture them now.
  timer: ~20 min
  image: none
  notes:
    Facilitation — a filing/organising task, not a lecture. They've been capturing since Topic 6; now
    they assemble it.
    Tell students: "You've been capturing evidence since Topic 6 — now assemble it. Sort everything
    into three appendices: screenshots, config exports, test evidence. Label and number every item so
    your report can cite it. Flag anything missing and recapture it now, while the lab is up."
    Steps (put on the board):
    1. Gather all screenshots, exports and test results from Topics 6–9.
    2. Sort into A (screenshots) / B (config exports) / C (test evidence).
    3. Label and number each item.
    4. List any gaps — and recapture them immediately.
    Must produce: three organised appendices, every item labelled and numbered, gaps recaptured.
    Timing: ~20 min. Where they get stuck: they discover they never captured something — that's the
    point, not a failure; have them recapture live from the standing lab, don't let them fabricate it.
    Share-back prompt: "What gap did you find — and could you still recapture it?"
    No-leakage note: this is the PRACTICE engagement (Ledgerline); AT2 assembles the same appendices
    for the assessed system (LMS) — comparable, not identical.
- [TAKEAWAYS] Section 1 · Evidence
  - Evidence must be traceable — named, dated, Region/identity visible.
  - Appendix A = screenshots, B = config exports, C = test evidence.
  - Label and number every item so the narrative can cite it.
  - Capture as you build; organise here; recapture any gaps now.
  image: none

### C2 — Writing the Deployment Report
- Teaches: [ICTCLD401 PC 4.1] · [ICTCLD502]
- Kicker: §1–§7
- [BESPOKE] Technical documentation — who reads it
  - The Deployment Report is written for the people who will run and audit the system — YAT ICT and auditors.
  - Clear, factual, traceable — every claim backed by an appendix reference.
  - It's a record of what was built and why — not a diary of your day.
  kicker: write for the reader
  image: none
  notes:
    Opens C2 — the audience question before the structure. Who the report is for decides how it's
    written.
    • The report is for the people who will run and audit the system: YAT ICT and auditors.
    • The accent line: clear, factual, traceable — every claim backed by an appendix reference.
    • It's a record of what was built and why — not a diary of your day.
    Misconception to pre-empt: "write it for the marker" / "write down everything I did." No — write
    for the operator and auditor; relevance and traceability, not a blow-by-blow of your afternoon.
    Question to pose: "The person reading this has to run the system at 2am when an alarm fires — what
    do they need from your report, and what don't they care about?"
    UoC/AT2 tie: PC 4.1 (document and communicate work to required personnel) — the audience IS the
    "required personnel."
- [BESPOKE] The report structure
  - §1 Executive Summary · §2 Engagement Context · §3 Scope of Deployment.
  - §4 Build / Change Narrative · §5 Configuration Decisions · §6 Testing, Simulation & Validation.
  - §7 Operational Handover.
  - Appendices A (screenshots) · B (config exports) · C (test evidence) — referenced throughout.
  kicker: the template
  image: none
  notes:
    The template — the map of the seven sections. They write TO this; they don't invent structure.
    • Read the sections: §1 Exec Summary · §2 Context · §3 Scope · §4 Build/Change Narrative ·
    §5 Configuration Decisions · §6 Testing/Validation · §7 Operational Handover.
    • Appendices A/B/C are referenced throughout — the structure and the evidence interlock.
    • The point: same professional-writing discipline as AT1's Business Case, new document — the
    assessor exemplar sets the standard.
    Misconception to pre-empt: "I'll organise it my own way." No — the template IS the standard; a
    report that doesn't follow it costs marks and confuses the reader.
    Question to pose: "Which of these sections are you writing fresh today, and which are you dropping
    in from work you already did?" (§5/§6 come from Topic 9 — leads to the next slides).
    UoC/AT2 tie: PC 4.1; §1–§7 + Appendices A/B/C is the AT2 marking home — every criterion lives in it.
- [BESPOKE] The Build / Change Narrative (§4)
  - Walk the build in order: foundation → network → compute → elasticity → database → storage → monitoring.
  - For each, state what you built and what changed from the baseline design.
  - Cross-reference the Appendix A screenshots and Appendix B exports that prove it.
  - Factual and specific — not “I set up the server”, but what, where, and with which settings.
  kicker: what you built, tier by tier
  image: none
  notes:
    The biggest writing section — teach it as a factual, ordered record, not a story.
    • Walk the tier order: foundation → network → compute → elasticity → database → storage →
    monitoring. That order is the spine of §4.
    • For each tier: state what you built and what changed from the baseline design.
    • The accent line: cross-reference the Appendix A screenshots and Appendix B exports that prove it.
    • Factual and specific — not "I set up the server", but what, where, and with which settings.
    Misconception to pre-empt: "the narrative is the story of my day." No — it's a factual tier-by-tier
    record, and every claim is cross-referenced to evidence.
    Question to pose: "'I configured the database.' What three things does an auditor still not know
    from that sentence?" (which engine, what settings, where's the proof).
    UoC/AT2 tie: PC 4.1; §4 is the A-build criterion in AT2 — the written proof of what was built.
- [BESPOKE] §5 Configuration Decisions & §6 Testing
  - §5 Configuration Decisions = your Topic 9 C1–C8 justifications — drop in the rationales you wrote.
  - §6 Testing/Validation = your Topic 9 validation results, each referencing Appendix C.
  - This is where the marked judgement (justify) and the evidence of a working build come together.
  kicker: your Topic 9 work lands here
  image: none
  notes:
    The payoff of C2 — the least NEW writing, the most marks. Their Topic 9 work lands straight here.
    • §5 Configuration Decisions = the Topic 9 C1–C8 justifications — drop in the rationales already
    written.
    • The accent line: §6 Testing/Validation = the Topic 9 validation results, each referencing
    Appendix C.
    • The point: this is where the marked judgement (justify) and the evidence of a working build come
    together in one place.
    Misconception to pre-empt: "I have to write §5 and §6 from scratch." No — they wrote these in
    Topic 9; this is assembling and cross-referencing, not re-authoring.
    Question to pose: "Your Topic 9 justification for the managed database — which section does it go
    in, and what appendix backs the testing beside it?" (§5; and §6 references Appendix C).
    UoC/AT2 tie: PC 4.1; §5 = the A4 criterion, §6 = A-build in AT2.
- [BESPOKE] §1–§3 and §7
  - §2 Context + §3 Scope — what the engagement was, why, and what's in / out of this build.
  - §7 Operational Handover — what YAT ICT now owns and how to run it (alarms, backups, access).
  - §1 Executive Summary — write it last; a short, plain summary for a busy reader.
  kicker: frame it and hand it over
  image: none
  notes:
    The frame-and-handover sections — short, but do them properly; §7 especially is real consulting.
    • §2 Context + §3 Scope — what the engagement was, why, and what's in / out of this build.
    • §7 Operational Handover — what YAT ICT now owns and how to run it: alarms, backups, access.
    • The accent line: §1 Executive Summary — write it LAST; a short, plain summary for a busy reader.
    Misconception to pre-empt: "the Exec Summary is first, so I write it first." Write it last — you
    can't summarise a report you haven't finished.
    Question to pose: "§7 handover — if you vanished tomorrow, what does YAT's ICT team need from you
    to keep this running?" (alarms, backups, access — the operational reality).
    UoC/AT2 tie: PC 4.1; scope and handover complete the AT2 report the reader actually operates from.
- [EX] Draft the Deployment Report
  - Write the report to the template for the practice engagement:
    - §4 narrative cross-referencing your appendices; §5 from your justifications; §6 from your validation
    - §2/§3 context + scope; §7 handover; §1 summary last
  - Every claim ties back to a labelled appendix item.
  timer: ~40 min
  image: none
  notes:
    Facilitation — the major writing block of the Topic. Give it room; circulate constantly.
    Tell students: "Write the Deployment Report for the practice engagement, to the template. Drop
    your Topic 9 justifications into §5 and your validation into §6. Write the §4 narrative tier by
    tier, cross-referencing your appendices. Add §2/§3 context and scope, §7 handover — and write the
    Executive Summary last. Every claim ties back to a labelled appendix item."
    Steps:
    1. §4 narrative — tier by tier, cross-referencing Appendices A and B.
    2. §5 from your justifications; §6 from your validation (referencing Appendix C).
    3. §2/§3 context + scope; §7 operational handover.
    4. §1 Executive Summary — last.
    Must produce: a complete Deployment Report to the template, every claim cross-referenced to a
    labelled appendix item.
    Timing: ~40 min (the big one). Where they get stuck: they try to write §5/§6 fresh — redirect them
    to their Topic 9 work; or they write §4 as a diary — pull them back to factual and cross-referenced.
    Share-back prompt: swap reports and have a partner try to find one cited appendix item — if they
    can't, the cross-reference failed.
    No-leakage note: this is the practice report on Ledgerline; AT2 is the same report on the assessed
    system (LMS) — comparable, not identical.
- [TAKEAWAYS] Section 2 · The report
  - Write for the people who run and audit the system; factual and traceable.
  - Follow the template — §1–§7 + Appendices A/B/C.
  - §5 carries your justifications; §6 your validation; §4 cross-references the evidence.
  - Write the Executive Summary last.
  image: none

### C3 — Knowledge in context
- Teaches: [ICTCLD401 KE 4, 5, 6, 7]
- Kicker: evidence what you know
- [BESPOKE] Evidence what you know — in context
  - Some knowledge isn't shown just by building — shared responsibility, managed vs self-hosted, storage/scaling/database options, cost models.
  - Answer the knowledge questions grounded in your build: cite your actual design and decisions.
  - “Why a managed database here?” → because of the Ledgerline workload and these trade-offs — not a textbook definition.
  kicker: grounded, not abstract
  image: none
  notes:
    Opens C3 — the knowledge that building alone doesn't demonstrate. The whole trick is "in context."
    • Some knowledge isn't shown by a screenshot: shared responsibility, managed vs self-hosted,
    storage/scaling/database options, cost models.
    • The accent line: answer the knowledge questions grounded in YOUR build — cite your actual design
    and decisions.
    • The example to land: "why a managed database here?" → because of the Ledgerline workload and
    these trade-offs, NOT a textbook definition.
    Misconception to pre-empt: "knowledge questions = recite the definition." No — evidence it in
    context; tie every answer to your own system and the choices you made.
    Question to pose: "'What is the shared responsibility model?' versus 'In YOUR build, what did AWS
    secure and what did you?' — which one proves you actually understand it?"
    UoC/AT2 tie: ICTCLD401 KE 4–7, evidenced contextually in the report (this is C3).
- [EX] Answer the knowledge questions in context
  - Answer the AT2 knowledge questions for the practice engagement:
    - reference your own build, decisions and the Ledgerline workload
    - shared responsibility · managed vs self-hosted · storage/scaling/db options · cost models
  - Specific to your system — not generic best practice.
  timer: ~20 min
  image: none
  notes:
    Facilitation — a short written KE task; the discipline is grounding, not defining.
    Tell students: "Answer the AT2 knowledge questions for the practice engagement — but ground every
    answer in YOUR build. Shared responsibility, managed vs self-hosted, storage and scaling options,
    cost models: for each, don't define it — show it in your own system and your own decisions."
    Steps:
    1. Take each knowledge question in turn.
    2. Answer it by citing your build, your decisions, and the Ledgerline workload.
    Must produce: contextual answers, each tied to their own system — not generic best practice.
    Timing: ~20 min then compare. Where they get stuck: they slip into textbook definitions — push
    back every time with "yes, but in YOUR build?"
    Share-back prompt: read one generic answer and one contextual answer, ask the room which one
    evidences understanding.
    No-leakage note: practice questions on Ledgerline; AT2 asks the same contextual KE on the assessed
    system (LMS) — comparable, not identical.

### C4 — Reflection & feedback
- Teaches: [ICTCLD401 PC 4.2]
- Kicker: close the loop
- [BESPOKE] Reflect, and respond to feedback
  - A reflection is an honest review — what worked, what you'd do differently, what you learned — not a summary of what you did.
  - Then seek feedback on your report from the required personnel, and respond to it.
  - Acting on feedback is part of the job — and it's assessed.
  kicker: honest review, then improve
  image: none
  notes:
    Opens C4 — the professional close-out. Two distinct things: an honest reflection, then acting on
    feedback.
    • A reflection is an honest review — what worked, what you'd do differently, what you learned —
    NOT a summary of what you did.
    • The accent line: then seek feedback on the report from the required personnel, and respond to it.
    • Acting on feedback is part of the job — and it's assessed.
    Misconception to pre-empt: "a reflection is a recap of what I did." No — it's honest self-review;
    the value is in what you'd change, not what went fine.
    Question to pose: "Name one thing you'd do differently if you rebuilt this — that one sentence is
    worth more than a paragraph of what went smoothly."
    UoC/AT2 tie: PC 4.2 (seek and respond to feedback as required) — this is C4.
- [EX] Reflect & seek feedback
  - Close out the engagement:
    - write a short, honest reflection on the build and the process
    - seek feedback on your report, and note what you changed in response
  timer: ~15 min
  image: none
  notes:
    Facilitation — the close-out task. Short, but the "respond" half is the assessed bit.
    Tell students: "Close out the engagement. Write a short, honest reflection on the build and the
    process — what worked, what you'd do differently. Then seek feedback on your report from the
    required personnel, and note what you actually changed in response."
    Steps:
    1. Write a short, honest reflection (not a summary).
    2. Seek feedback on the report from the required personnel.
    3. Note what you changed in response.
    Must produce: a reflection plus a record of feedback sought and the response/change made.
    Timing: ~15 min. Where they get stuck: reflections that are just summaries — prompt "what would
    you change?"; or "responding to feedback" with no actual change — the change IS the assessed part.
    Share-back prompt: one honest "what I'd do differently" from the room.
    No-leakage note: practice reflection on the Ledgerline engagement; AT2 assesses the same
    reflect-and-respond on the LMS work — comparable, not identical.
- [TAKEAWAYS] Topic 10 · Key takeaways
  - Evidence is traceable and lives in Appendices A / B / C.
  - Write to the template, cross-referencing the evidence throughout.
  - §5 carries your C1–C8 justifications; §6 your validation results.
  - Evidence your knowledge in the context of your build; reflect and respond to feedback.
  - The Deployment Report is the AT2 deliverable — this is where it all comes together.
  image: none

### Close
- [BESPOKE] AT2 complete
  - You can now build a cloud workload to a supplied design, evidence it, justify it, and document it.
  - Next: the AT2 assessment build — then AT3, where the baseline becomes highly available.
  image: none
