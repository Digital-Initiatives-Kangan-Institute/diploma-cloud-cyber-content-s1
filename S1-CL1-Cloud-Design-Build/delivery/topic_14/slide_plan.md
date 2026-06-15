# Topic 14 — Closure & documentation · Slide plan

Build sheet for `scripts/build_s1_cl1_topic14_deck.py` → `Topic_14_Slides.pptx`. Satisfies `coverage.md`. **Disposable scaffold** — delete once built.

**Markers.** `[BESPOKE]` author from brief · `[502 ref]` from the pinned slide · `[EX]` activity. **All bespoke, teach → practice** (no AWS slides, no demos). Accents A1/A2/A3; topic-level GOLD. Reference: the AT3 HA Deployment Report template (§1–§8 + Appendices A–D).

## Sequence (~19 slides)
1. **title_slide** "14 · Closure & documentation" / "Write the HA report, evidence what you know, and close the engagement."
2. **content** opener — Topic 13 implemented + simulated; now write the **HA Deployment Report**, evidence the knowledge, reflect, and **close out** (feedback + sign-off). The end of AT3 — and the course's build arc.

### C1 — Write the HA Deployment Report · A1
3. **divider** "01" · "Write the HA Deployment Report"
4. **content** `[BESPOKE]` "Evidence into the appendices" — organise the implementation + simulation evidence into Appendix A (screenshots) / B (config exports) / **C (test & simulation evidence)**; label + number so the narrative cites it. (Same discipline as AT2.)
5. **content** `[BESPOKE]` "The HA report structure" — §1 Exec Summary · §2 Context · §3 Scope (maintenance window) · §4 Build/Change Narrative (HA changes from baseline) · §5 Config Decisions · §6 Testing/Simulation/Validation · §7 Operational Handover · §8 Knowledge Evidence · Appendices A–D (D = reflections).
6. **content** `[BESPOKE]` "The heart — §6 simulation findings" — your failure sim, resize sim, availability measurement, **findings vs the design**, adjustments made. This is the proof of fault tolerance — what AT3 is marked on.
7. **content** `[BESPOKE]` "§4 narrative · §5 decisions · §7 handover" — §4 the HA changes from baseline (cross-AZ network/ASG/ALB, Multi-AZ DB), cross-referencing appendices; §5 the HA decisions justified; §7 what YAT ICT now runs.
8. **activity** `[EX]` "Draft the HA Deployment Report" (~40 min) — write to the template; §6 your simulation findings as the centrepiece; cross-reference your appendices.
9. **takeaways** "Section 1 · The report".

### C2 — Contextual knowledge evidence · A2
10. **divider** "02" · "Knowledge in context"
11. **content** `[BESPOKE]` "Evidence what you know (§8)" — answer the AT3 knowledge questions **grounded in your HA work** — availability, fault tolerance, recovery objectives, redundancy — citing your design + simulations, not textbook definitions.
12. **activity** `[EX]` "Answer the knowledge questions in context" (~20 min) — answer §8 referencing your own HA design + simulation findings.

### C3 — Close the engagement · A3
13. **divider** "03" · "Close the engagement"
14. **content** `[502 · Implement & finalise S11–S12]` "Feedback & sign-off" — collect unbiased feedback (surveys / interviews / focus groups); confirm, seek and respond to feedback; **obtain final sign-off** from the project sponsor or delegated authority — the last step in closing a project.
15. **content** `[BESPOKE]` "Reflect" — Appendix D: an honest review of the HA engagement — what worked, what you'd do differently, what you learned.
16. **activity** `[EX]` "Close out — feedback, sign-off & reflection" (~20 min) — seek feedback on the report + record your response (§7.5); obtain + record sign-off (§7.6); write your reflection (Appendix D).
17. **takeaways** "Section 3 · Close".

### Close
18. **takeaways** "Topic 14 · Key takeaways" (GOLD) — write the HA report (simulation findings = the heart); evidence knowledge in context; close with feedback + sign-off + reflection; AT3 is complete.
19. **close_slide** "AT3 complete — advise (AT1) → build (AT2) → make it highly available (AT3). The cluster's teaching arc is done." (GOLD)

## Notes
- **All bespoke** — report-writing / KE / feedback / sign-off to a VET standard; AWS decks don't teach it. The one reused source is **502 Topic 4 S11–S12** (feedback + sign-off).
- **Continuity:** §6 ← Topic 13 simulation findings; Appendices ← evidence since Topic 13; §8 KE in context; closure = 502 element 5.2–5.3.
- **Practice:** students produce the HA Deployment Report for the Accounting engagement and close it out.
- **No image placeholders, no demos** (documentation/closure topic).
