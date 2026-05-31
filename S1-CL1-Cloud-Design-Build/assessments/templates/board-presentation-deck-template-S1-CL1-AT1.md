# YAT LMS Cloud Migration — Board Presentation Deck Template

> **Template for student completion (S1-CL1 AT1).** This deck **presents your Business Case** to the YAT board (role-played by your assessor + a peer). The Business Case is the artefact of record; this deck is the walkthrough you use to take the board through it. The Business Case is sent to the board ahead of the meeting; the deck guides the conversation.
>
> **What you are asking the board to do:** approve the action plan in §10 of your Business Case, authorise the budget envelope in §10.3, and unblock the next stage of work.
>
> Each section below corresponds to one slide, with the Business Case section it draws from named at the top. Final submitted form is a `.pptx` (or equivalent) deck built to this structure.
>
> Recommended deck length: **8–10 slides**. Presentation duration: **10–15 minutes**, followed by 5 minutes of questions / feedback / sign-off.

---

## UoC requirements evidenced by this deck and the presentation event

The deck and the live presentation together evidence:

- **[ICTICT517 PC 1.4]** — Report on proposed changes, gaps and improvement opportunities to superior. *(The deck is the report-out medium; the Business Case is the supporting written report.)*
- **[ICTICT517 PC 2.4]** — Document evaluation process and provide to superior for feedback. *(The Business Case is the documented evaluation; the deck signals "it's available — let's discuss it".)*
- **[ICTICT517 PC 3.3]** — Provide action plan to superior for feedback and approval. *(The asked-for decision at the end of the presentation.)*
- **[ICTCLD401 PC 4.1]** — Document and communicate work to required personnel. *(The presentation event is the communication.)*
- **[ICTCLD401 PC 4.2]** — Seek and respond to feedback as required. *(Q&A and the post-presentation feedback exchange.)*
- **[ICTCLD502 PC 5.2]** — Confirm, seek and respond to feedback with required personnel. *(Same — Q&A and feedback exchange.)*
- **[ICTICT517 FS Oral Communication]** — plain English, translating technical terminology, articulating ideas/requirements/plans, listening and questioning techniques.
- **[ICTCLD502 FS Oral communication]** — listening and questioning to articulate complex concepts using industry language for intended audience.
- **[ICTICT517 AC 4]** — Individual superior in the organisation. *(The role-played Sam Walker / Pat Lin.)*

---

## Slide 1 — Title

**Required content:**
- Project title: *YAT LMS Cloud Migration — Business Case and Recommendation*
- Your name + MTS role
- Date of presentation
- YAT logo placeholder

---

## Slide 2 — Engagement context

*Walks the board through: Business Case §2 (Engagement Context)*

**Speaker's purpose:** establish in 60–90 seconds who you are, why you are presenting, and what the board is being asked to decide today.

**Required content (3–5 bullets):**
- Engagement: MTS consulting to YAT on the LMS migration
- Your role: [FILL IN]
- The board's decision today: approve the action plan in your Business Case and the budget envelope it carries
- Where your Business Case sits in the bigger picture (the LMS-first directive in YAT's Planned ICT Initiatives)

---

## Slide 3 — Strategic context

*Walks the board through: Business Case §3 (Strategic Alignment Analysis)*

**Speaker's purpose:** connect this engagement to YAT's strategic plan and ICT objectives. Show you have understood the strategic context before you started costing options.

**Required content:**
- 2–3 ICT Strategic Plan objectives the migration is intended to address (cite verbatim — pull from the YAT intranet's *ICT Strategic Plan (Detail)* page)
- The 99.9% availability commitment in the Strategic Plan
- Where YAT's plan aligns with industry direction (relevant external research from your §3 analysis)

---

## Slide 4 — Current state and the gap

*Walks the board through: Business Case §4 (Current State of YAT's ICT) + §5 (Gap Analysis)*

**Speaker's purpose:** show the board, in concrete terms, why staying as-is isn't viable. Acknowledge they know their own environment — your job is to characterise it for the migration conversation.

**Required content:**
- Headline current-state facts: LMS at end-of-life, 99.2% measured availability, ~24h RPO / 7–11h RTO, single-server SPOF
- Headline gap-analysis findings (2–3): the largest gaps between current state and the Strategic Plan targets
- Visual: a "current vs target" comparison table (4–6 rows) or a simple gap-diagram

---

## Slide 5 — Options compared

*Walks the board through: Business Case §6 (Options Considered and Evaluation)*

**Speaker's purpose:** name the options and their high-level shape; explain how you evaluated them.

**Required content:**
- **Option A — In-house renewal:** replace the LMS server, continue on-prem
- **Option B — Cloud migration to AWS:** lift-and-shift the LMS stack to AWS with managed multi-AZ database, autoscaling, Multi-AZ HA
- The evaluation method you applied (CBA + intangibles + risk register)
- One-line summary of each option's value proposition

---

## Slide 6 — The numbers — 5-year cost comparison

*Walks the board through: Business Case §7 (Cost-Benefit Analysis) — referencing the §7 summary tables and the Appendix 1 detail*

**Speaker's purpose:** the financial-comparison slide. Senior management will fixate here.

**Required content:**
- Table or bar chart: 5-year direct cost — Option A vs Option B (from BC §7.5)
- Year-1 cash-flow position for each option (from BC §7.5.1) — material because the Year-1 outlay difference matters to YAT
- Highlight delta (Option B − Option A)
- Avoided-downtime benefit (5-year quantified figure, from BC §7.4)
- One-line caveat on the key sensitivities (e.g. *"Cloud advantage holds across the sensitivity range I tested — see Business Case §7.6 for the recalculations"*)
- Pointer: *"Line-item detail is in the Business Case Appendix 1; the summary tables on this slide draw from §7.2 / §7.3 / §7.5."*

---

## Slide 7 — Intangibles and risks

*Walks the board through: Business Case §8 (Risk and Impact Assessment)*

**Speaker's purpose:** acknowledge that the recommendation is not made on cost alone, and surface the top risks.

**Required content (pick 4–5 most impactful — don't list all 9 intangibles):**
- Reliability and recovery (which option meets the target)
- Capacity for growth (15%/year) and peak handling (assessment weeks)
- YAT ICT staff capability impact
- Vendor lock-in (be honest)
- One more material to YAT (your choice)

Plus the **top 2–3 risks** of the recommended option (from BC §8.2) with one-line mitigations.

---

## Slide 8 — Recommendation

*Walks the board through: Business Case §9 (Recommendation)*

**Speaker's purpose:** state the recommendation crisply, name the rationale in two or three sentences, signal what comes next.

**Required content:**
- **Recommendation:** [Option A / Option B]
- 2–3 sentence rationale tying back to the analysis
- Next slide: the action plan that flows from this recommendation

---

## Slide 9 — Action plan summary

*Walks the board through: Business Case §10 (Action Plan) — the asked-for-approval section*

**Speaker's purpose:** show that you have a credible, executable plan, not just a number and a recommendation.

**Required content:**
- Top 5–7 prioritised changes (from BC §10.1)
- Implementation sequencing in broad strokes (from BC §10.2)
- Key sign-off gates within the action plan (via the YAT change management procedure — from BC §10.5)
- Standards / targets at a glance (from BC §10.3 — e.g. 99.9% availability, RPO ≤ 1h, RTO ≤ 4h, data residency)
- Indicative overall duration

**This is the slide where the board's attention sits longest** — the action plan is what they're being asked to approve.

---

## Slide 10 — Decision required + Q&A

*Walks the board through: Business Case §11 (Next Steps and Decision Requested) — closes the loop and invites the conversation*

**Speaker's purpose:** name the decision being asked for, signal what's deferred, invite questions, and close with sign-off.

**Required content:**
- **Decision asked for today:**
  - Approve Option [A / B] as the recommended approach
  - Approve the action plan in BC §10 as the implementation roadmap
  - Authorise the budget envelope in BC §10.3
- **Deferred for later approval:** specific procurement items, the high-risk cutover change request at the appropriate phase, etc. (from BC §11)
- "Questions / feedback" placeholder for the live Q&A
- The Sign-off block (BC Sign-off section) is brought up at the end of the meeting — the board signs against the action plan; the student records feedback in the Feedback Record template (which becomes BC Appendix 4)

---

## Speaker notes — required for every slide

For each slide in your `.pptx`, populate the speaker-notes pane with:
- Key talking points (3–5 bullets)
- Likely board questions you anticipate
- Your prepared response framing

Speaker notes are not delivered verbally but are reviewed by the assessor — they evidence your preparation and contribute to [ICTICT517 FS Writing] coverage.

---

## Visual / formatting expectations

- YAT branding visible on every slide (header or footer placeholder is fine for the markdown draft)
- Charts and tables preferred over walls of text
- One concept per slide
- Plain English, with technical terms translated when first used (Foundation Skill: Oral Communication explicitly calls this out — *"translating technical terminology when necessary"*)
- Maximum 6 lines of text per slide (excluding tables / charts)

---

## What you'll be assessed on (per the Observation Rubric)

The assessor observes your delivery against the rubric document (see `assessments/AT1/presentation-observation-rubric.md`). Every criterion in that rubric is tagged with the UoC element it evidences. Headline assessment dimensions:

- The PCs evidenced by the presentation event (reporting, providing the action plan, seeking and responding to feedback)
- The Oral Communication Foundation Skills (plain English + translation of technical terminology, listening and questioning techniques, industry language for the intended audience)
- The assessment condition that an individual superior is present to receive the report
- Q&A questions that probe both PC understanding and KE topics

The Q&A also covers Knowledge Evidence not fully captured in your Business Case Appendix 2 — the assessor may probe more deeply or differently than the written appendix questions.

---

## Submission

The deck is one component of the AT1 submission bundle. Submit:

- [ ] The `.pptx` deck built to this structure
- [ ] Speaker notes populated for every slide

The deck does not stand alone — it is submitted together with the populated Business Case (which itself includes the populated CBA detail in its Appendix 1, the Knowledge Evidence responses in its Appendix 2, the supporting research in Appendix 3, and the post-presentation Feedback Record in Appendix 4).
