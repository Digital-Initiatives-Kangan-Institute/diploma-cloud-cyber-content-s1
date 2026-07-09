# Topic 14 Closure & documentation — Slide plan
> **Covers:** Topic 14 — see coverage.md
> **Subtitle:** Write the HA report, evidence what you know, and close the engagement

## Slides

### Opener
- [BESPOKE] Close it out
  - Topic 13 implemented the HA design and proved it under simulated failure.
  - Topic 14 turns that into the HA Deployment Report, evidences your knowledge, and closes the engagement.
  - Three moves: write the report (the simulation findings are its heart), evidence knowledge in context, and close out with feedback + sign-off.
  - This is the end of AT3 — and of the journey from advising to building to hardening.
  kicker: the final step
  image: none
  notes:
    Frame this as the map for the whole Topic — and for the whole course. Set expectations;
    don't write the report yet.
    • Where this fits: Topic 13 implemented the HA design and proved it under simulated failure.
    Topic 14 turns that evidence into the deliverable and closes the engagement.
    • The three moves: write the HA Deployment Report (the simulation findings are its heart),
    evidence knowledge in context, close out with feedback + sign-off.
    • Stress the arc (the bolded line): this is the end of AT3 — and of advise → build → harden.
    They advised in AT1, built in AT2, hardened in AT3; today they document and sign off.
    • How they practise: on the Accounting System (Ledgerline), from their own Topic 13 evidence.
    Misconception to pre-empt: "the build is done, so we're finished." No — an engagement isn't
    complete until it's documented, the knowledge is evidenced, and the client has signed off.
    Question to pose: "You've proven the HA design works — why isn't the job done yet?" — draws
    out that documentation + closure ARE the deliverable, not an afterthought.
    UoC/AT3 tie: AT3 = ICTCLD502; this Topic evidences PC 3.5, 4.6, 5.2, 5.3, KE 4 and PE 1 — the
    whole finalise-and-document end of the unit.

### C1 — Write the HA Deployment Report
- Teaches: [ICTCLD502 PC 3.5] · [ICTCLD502 PC 4.6] · [ICTCLD502 PE 1]
- Kicker: from evidence to deliverable
- [BESPOKE] Evidence into the appendices
  - Organise everything you captured into the appendices: A — build screenshots; B — configuration exports; C — test & simulation evidence.
  - Label and number each item so the narrative can cite it.
  - Traceable evidence is what turns a claim into proof.
  kicker: the same discipline as AT2
  image: none
  notes:
    Teach evidence discipline first — it's the foundation the whole report cites. Callback hard
    to Topic 10 (AT2): same skill, the HA deliverable.
    • Walk the three appendices: A — build screenshots; B — configuration exports; C — test &
    simulation evidence. Everything captured in Topic 13 gets organised here.
    • The key move (bolded): label and number each item so the narrative can cite it. An
    unlabelled screenshot proves nothing; a cited one turns a claim into proof.
    • Frame traceability as the assessor's job made easy — every §6 finding points to a numbered
    appendix item they can check.
    Misconception to pre-empt: "the appendices are a dumping ground for screenshots." No — they're
    a curated, labelled evidence set the narrative references by number; unorganised evidence is
    unusable evidence.
    Question to pose: "If you write 'the failover succeeded' in §6, what in the appendices has to
    be there for an assessor to believe you?" (the labelled simulation evidence in Appendix C).
    UoC/AT3 tie: supports PC 3.5 (document the implemented design) and PE 1 — the documented
    fault-tolerant infrastructure rests on traceable evidence.
- [BESPOKE] The HA report structure
  - §1 Executive Summary · §2 Engagement Context · §3 Scope (the maintenance window).
  - §4 Build/Change Narrative (the HA changes from the baseline) · §5 Configuration Decisions · §6 Testing, Simulation & Validation.
  - §7 Operational Handover · §8 Knowledge Evidence.
  - Appendices A–D — A screenshots · B config exports · C test/simulation evidence · D reflections.
  kicker: the template
  image: none
  notes:
    Teach the template as the deliverable's skeleton — students write to it, so walk it
    deliberately.
    • Walk the sections: §1 Executive Summary · §2 Engagement Context · §3 Scope (the maintenance
    window) · §4 Build/Change Narrative · §5 Configuration Decisions · §6 Testing, Simulation &
    Validation · §7 Operational Handover · §8 Knowledge Evidence.
    • Appendices A–D: A screenshots · B config exports · C test/simulation evidence · D reflections.
    • Flag which sections carry the weight: §6 (the heart, next slide) and §8 (contextual KE, C2).
    §1 is written last.
    Misconception to pre-empt: "this is a different report from AT2." It's the same template shape
    as the AT2 Deployment Report — the content is the HA change, not the whole build. Reassure
    them they've done this once already.
    Question to pose: "Which section does an assessor turn to first to see the HA design actually
    works?" (§6 — the proof).
    UoC/AT3 tie: PC 3.5 — documenting the implemented HA design to the required structure; the
    report as a whole is AT3's marking home.
- [BESPOKE] The heart — §6 simulation findings
  - §6 is where you prove fault tolerance: the failure simulation, the resize simulation, and the availability you measured.
  - Compare the findings to the design's recovery objectives, and record any adjustments you made.
  - This section is what AT3 is marked on — the evidence the HA design actually works.
  kicker: your Topic 13 work
  image: none
  notes:
    This is the highest-value slide of the Topic — §6 is what AT3 is marked on. Give it the weight.
    • Walk what §6 holds: the failure simulation, the resize simulation, and the availability you
    measured — all from the Topic 13 work.
    • The key move (bolded): compare the findings to the design's recovery objectives, and record
    any adjustments you made. It's not "here's what happened" — it's "here's what happened,
    measured against what we designed for."
    • Drive the point: this section is the evidence the HA design actually delivers fault
    tolerance; everything else in the report supports it.
    Misconception to pre-empt: "§6 is a description of the tests I ran." No — it's an evaluation:
    did the results MEET the recovery objectives, and if not, what did you change? Narration
    without comparison earns little.
    Question to pose: "Your failover took longer than the design's recovery target — does that go
    in §6, and how do you write it up?" (yes — record the gap and the adjustment; honesty is
    evidence).
    UoC/AT3 tie: PC 4.6 (compare and document simulation findings against the documented design) —
    produced in Topic 13, written up here; the centre of AT3's mark.
- [BESPOKE] §4 narrative · §5 decisions · §7 handover
  - §4 — the HA changes from the baseline (cross-AZ network, cross-AZ ASG + ALB, Multi-AZ database), cross-referencing the appendices.
  - §5 — the HA configuration decisions, justified.
  - §7 — operational handover: what YAT ICT now runs (the HA-tuned alarms, the failover behaviour, what to watch).
  - §1 Executive Summary — write it last.
  kicker: the rest of the report
  image: none
  notes:
    Teach the supporting sections — the report body around §6. Keep the pace up; these frame the
    heart.
    • §4 the Build/Change Narrative: the HA changes FROM the baseline — cross-AZ network, cross-AZ
    ASG + ALB, Multi-AZ database — cross-referencing the appendices as it goes.
    • §5 the configuration decisions, each justified (why Multi-AZ, why cross-AZ scaling).
    • §7 Operational Handover: what YAT ICT now runs — the HA-tuned alarms, the failover behaviour,
    what to watch. This is what the client operates after you leave.
    • §1 Executive Summary (bolded): write it LAST — you can't summarise a report you haven't
    written.
    Misconception to pre-empt: "§4 is the whole build from scratch." No — it's the HA CHANGES from
    the AT2 baseline, not a rebuild narrative; the baseline is assumed, the delta is documented.
    Question to pose: "§7 hands the system to YAT's ICT team — what do they need to know that they
    didn't before the HA work?" (the failover behaviour and the new alarms to watch).
    UoC/AT3 tie: PC 3.5 (as-built documentation) and PE 1 (the fault-tolerant infrastructure
    documented in full).
- [EX] Draft the HA Deployment Report
  - Write the report to the template for the practice engagement:
    - §4 the HA changes; §5 the decisions; §6 your simulation findings (the centrepiece)
    - cross-reference Appendices A/B/C; §7 the handover
  - Every claim ties back to a labelled appendix item.
  timer: ~40 min
  image: none
  notes:
    Facilitation — the Section 1 build task; the main writing activity of the Topic. They assemble
    the report from their own Topic 13 evidence.
    Tell students: "Write the HA Deployment Report to the template for the practice engagement.
    Your Topic 13 evidence and simulation findings are the raw material — organise them into the
    appendices, then write the narrative that cites them."
    Steps (put on the board):
    1. §4 — the HA changes from the baseline.
    2. §5 — the configuration decisions, justified.
    3. §6 — your simulation findings, compared to the recovery objectives (the centrepiece).
    4. Cross-reference Appendices A/B/C; write §7 the handover.
    Must produce: a drafted report (§4–§7 + organised appendices) where every claim ties back to a
    labelled appendix item.
    Timing: ~40 min. Where they get stuck: they narrate §6 without comparing to the design
    objectives — circulate and push "measured against what?"; and unlabelled evidence — send them
    back to number it.
    Share-back: take one §6 write-up and ask the room whether the finding is evidenced by a cited
    item.
    No-leakage note: this is the PRACTICE report on Ledgerline; the assessed HA report is built on
    the LMS in AT3 — comparable, not identical. Keep them on the scenario system here.
- [TAKEAWAYS] Section 1 · The report
  - Organise evidence into Appendices A/B/C; label and cross-reference.
  - Follow the template — §1–§8 + Appendices A–D.
  - §6 simulation findings is the heart — the proof of fault tolerance.
  - Write the Executive Summary last.
  image: none

### C2 — Knowledge in context
- Teaches: [ICTCLD502 KE 4]
- Kicker: evidence what you know
- [BESPOKE] Evidence what you know (§8)
  - Answer the knowledge questions about high availability — fault tolerance, recovery objectives, redundancy, the trade-offs.
  - Ground every answer in your own HA work: cite your design and your simulation findings.
  - “Why Multi-AZ for the database?” → because of this workload and what my failover simulation showed — not a textbook definition.
  kicker: grounded, not abstract
  image: none
  notes:
    Teach contextual KE — the distinctive move of §8. The knowledge must be grounded, not abstract.
    • What §8 asks: answer the knowledge questions about high availability — fault tolerance,
    recovery objectives, redundancy, the trade-offs.
    • The key move (bolded): ground every answer in your OWN HA work — cite your design and your
    simulation findings, not a textbook definition.
    • Make it concrete: "Why Multi-AZ for the database?" → "because of this workload and what my
    failover simulation showed" — the answer points back at their evidence.
    Misconception to pre-empt: "knowledge evidence means writing textbook definitions." No —
    contextual KE means proving you understand HA BY explaining your own design choices; a generic
    definition shows recall, not applied understanding.
    Question to pose: "How is 'define fault tolerance' different from 'explain the fault tolerance
    in YOUR design'?" (the second cites their build; that's what §8 wants).
    UoC/AT3 tie: KE 4, evidenced contextually — the unit's knowledge evidence proven through the
    learner's own HA work rather than abstractly.
- [EX] Answer the knowledge questions in context
  - Complete §8 for the practice engagement:
    - reference your HA design, your decisions, and your simulation results
    - availability · fault tolerance · recovery objectives · redundancy mechanisms
  - Specific to your system — not generic best practice.
  timer: ~20 min
  image: none
  notes:
    Facilitation — the Section 2 practice; short, grounded KE writing.
    Tell students: "Complete §8 for the practice engagement. For each knowledge question, don't
    define the term — explain it through YOUR design, YOUR decisions and YOUR simulation results."
    Steps:
    1. Take each question — availability · fault tolerance · recovery objectives · redundancy
    mechanisms.
    2. Answer it referencing your actual HA design and what your simulation showed.
    Must produce: §8 answers, each tied to a specific part of their own system — not generic best
    practice.
    Timing: ~20 min then compare. Where they get stuck: they slip into textbook definitions —
    circulate and ask "which part of YOUR design shows that?" to pull the answer back to their
    evidence.
    Share-back: read one generic answer and one grounded answer; ask the room which evidences
    understanding.
    No-leakage note: practice KE on Ledgerline here; AT3 assesses the same contextual-KE skill on
    the LMS build — comparable, not identical.

### C3 — Close the engagement
- Teaches: [ICTCLD502 PC 5.2] · [ICTCLD502 PC 5.3]
- Kicker: feedback · sign-off · reflection
- [BESPOKE] Feedback & sign-off
  - At completion, collect unbiased feedback to confirm the design meets requirements — surveys, one-on-one interviews, focus groups.
  - Confirm, seek and respond to feedback from the required personnel.
  - Then obtain final sign-off from the project sponsor (or delegated authority) — generally the last step in closing a project.
  kicker: ICTCLD502 · Implement & finalise
  image: none
  notes:
    Teach the finalise element — the formal close of an engagement, reused from 502 Topic 4
    S11–S12.
    • Walk it: at completion, collect UNBIASED feedback to confirm the design meets requirements —
    surveys, one-on-one interviews, focus groups.
    • Confirm, seek and RESPOND to feedback from the required personnel — feedback you ignore isn't
    closure.
    • Then obtain final SIGN-OFF from the project sponsor or delegated authority (bolded) —
    generally the last step in closing a project.
    Misconception to pre-empt: "sign-off is just a signature at the end." No — it follows seeking
    and responding to feedback; the client signs off because their requirements were confirmed met,
    not as a formality.
    Question to pose: "Why collect feedback from someone OTHER than yourself before sign-off?"
    (unbiased confirmation the design meets requirements — you can't sign off your own work).
    UoC/AT3 tie: PC 5.2 (confirm, seek and respond to feedback) and PC 5.3 (obtain final sign-off)
    — the finalise element that distinguishes closure from documentation.
- [BESPOKE] Reflect
  - Write an honest reflection on the HA engagement — what worked, what you'd do differently, what you learned.
  - A reflection is a review, not a summary of what you did.
  - It's how you improve the next engagement — and it's assessed.
  kicker: Appendix D
  image: none
  notes:
    Teach reflection as a genuine review — short slide, but the distinction matters and it's
    assessed.
    • What it is: an honest reflection on the HA engagement — what worked, what you'd do
    differently, what you learned.
    • The key move (bolded): a reflection is a REVIEW, not a summary of what you did. "I built a
    Multi-AZ database" is a summary; "Multi-AZ was the right call because… but I'd test failover
    earlier next time" is a reflection.
    • Frame the value: it's how you improve the next engagement — and it's marked (Appendix D).
    Misconception to pre-empt: "reflection = restate the tasks I completed." No — that's a summary;
    reflection evaluates the choices and names what you'd change.
    Question to pose: "What's one thing about your HA build you'd do differently — and why?" (models
    the evaluative move the reflection wants).
    UoC/AT3 tie: part of AT3's evidence (Appendix D); supports the finalise element and demonstrates
    the reflective practice the unit expects.
- [EX] Close out — feedback, sign-off & reflection
  - Finalise the engagement:
    - seek feedback on your report and record your response (§7.5)
    - obtain and record final sign-off (§7.6)
    - write your reflection (Appendix D)
  timer: ~20 min
  image: none
  notes:
    Facilitation — the Section 3 practice; the final activity of the Topic and the course. They
    formally close the practice engagement.
    Tell students: "Finalise the practice engagement. Seek feedback on your report and record your
    response, obtain and record final sign-off, then write your honest reflection."
    Steps:
    1. Seek feedback on your report and record your response (§7.5).
    2. Obtain and record final sign-off (§7.6).
    3. Write your reflection (Appendix D) — a review, not a summary.
    Must produce: recorded feedback + response, a recorded sign-off, and a written reflection.
    Timing: ~20 min. Where they get stuck: reflection reads as a task summary — circulate and ask
    "what would you CHANGE?"; and sign-off with no feedback recorded first — remind them of the
    5.2 → 5.3 order.
    Share-back: take one reflection and ask whether it evaluates or just restates.
    No-leakage note: practice closure on Ledgerline; AT3 assesses the same finalise skill on the
    LMS engagement — comparable, not identical. This closes the practice arc that mirrors the
    assessed one.
- [TAKEAWAYS] Section 3 · Close
  - Collect unbiased feedback; confirm, seek and respond to it.
  - Obtain final sign-off — the last step in closing the project.
  - Reflect honestly — what worked, what you'd change.
  - The engagement is now formally complete.
  image: none
- [TAKEAWAYS] Topic 14 · Key takeaways
  - The HA Deployment Report is the deliverable — write it to the template.
  - §6 simulation findings is the heart: the proof of fault tolerance.
  - Evidence your knowledge in the context of your own HA work.
  - Close with feedback, final sign-off, and an honest reflection.
  - AT3 — and the build journey — is complete.
  image: none

### Close
- [BESPOKE] AT3 complete
  - You advised the client (AT1), built the solution (AT2), and made it highly available (AT3) — designed, implemented, proven, documented, and signed off.
  - The cluster's teaching arc is done.
  image: none
