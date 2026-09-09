# S1-CL2 Cloud Disaster Recovery — Delivery Plan (2026-T2)
> **INSTANCE: 2026-T2.** Frame: cluster-specification.md · Generates: S1_CL2_Delivery_Plan.docx

## 1. Instance prerequisites
- Intake: 2026-T2
- Total sessions available: 24
- Teaching days per week: 2
- Teaching days: Thursday, Friday
- Online/classroom split: all online
- Assessment types: AT1: Project · AT2: Project

## 2. Document details
- Qualification code and title: ICT50220 Diploma of Information Technology
- Unit code and title: ICTCLD501 Develop cloud disaster recovery plans; ICTCLD503 Implement web-scale cloud infrastructure; ICTCLD505 Implement cloud infrastructure with code
- Cohort description: This cluster is delivered to a small cohort of approximately seven to eight adult learners based in Bendigo, a regional town in Victoria. As Diploma-level (AQF Level 5) vocational students, they are post-secondary learners who have generally completed secondary schooling and are studying outside the school system. Most are expected to bring some prior IT background — it is reasonable to assume many, if not all, have completed a lower-level Certificate III or IV qualification in an IT-related discipline — so the cohort enters with foundational ICT knowledge on which this cluster's cloud and cybersecurity content builds. The small group size supports an individualised, hands-on delivery approach, while the regional setting means delivery and assessment rely on cloud-based lab environments accessible online.
- Materials and resources: AWS Academy Learner Lab (us-east-1) for all build and deploy work; the cluster's assessment workbooks (AT1 Design & DR Plan, AT2 Microservice & IaC) and their practice run sheets; the YAT scenario intranet; Topic decks 1–9; AWS service documentation

## 3. Session grid
|  # | Date       | Week | Day | Time     | Mode   | Activity   | Placed |
|----|------------|------|-----|----------|--------|------------|--------|
|  1 | 2026-10-08 |    1 | Thu | 9am-12pm | online | teach      | T1     |
|  2 | 2026-10-08 |    1 | Thu | 1pm-4pm  | online | teach      | T2     |
|  3 | 2026-10-09 |    1 | Fri | 9am-12pm | online | teach      | T3     |
|  4 | 2026-10-15 |    2 | Thu | 9am-12pm | online | teach      | T4     |
|  5 | 2026-10-15 |    2 | Thu | 1pm-4pm  | online | teach      | T5     |
|  6 | 2026-10-16 |    2 | Fri | 9am-12pm | online | assessment | AT1    |
|  7 | 2026-10-22 |    3 | Thu | 9am-12pm | online | assessment | AT1    |
|  8 | 2026-10-22 |    3 | Thu | 1pm-4pm  | online | assessment | AT1    |
|  9 | 2026-10-23 |    3 | Fri | 9am-12pm | online | assessment | AT1    |
| 10 | 2026-10-29 |    4 | Thu | 9am-12pm | online | assessment | AT1    |
| 11 | 2026-10-29 |    4 | Thu | 1pm-4pm  | online | assessment | AT1    |
| 12 | 2026-10-30 |    4 | Fri | 9am-12pm | online | teach      | T6     |
| 13 | 2026-11-05 |    5 | Thu | 9am-12pm | online | teach      | T7     |
| 14 | 2026-11-05 |    5 | Thu | 1pm-4pm  | online | teach      | T8     |
| 15 | 2026-11-06 |    5 | Fri | 9am-12pm | online | teach      | T9     |
| 16 | 2026-11-12 |    6 | Thu | 9am-12pm | online | assessment | AT2    |
| 17 | 2026-11-12 |    6 | Thu | 1pm-4pm  | online | assessment | AT2    |
| 18 | 2026-11-13 |    6 | Fri | 9am-12pm | online | assessment | AT2    |
| 19 | 2026-11-19 |    7 | Thu | 9am-12pm | online | assessment | AT2    |
| 20 | 2026-11-19 |    7 | Thu | 1pm-4pm  | online | assessment | AT2    |
| 21 | 2026-11-20 |    7 | Fri | 9am-12pm | online | assessment | AT2    |
| 22 | 2026-11-26 |    8 | Thu | 9am-12pm | online | spare      | —      |
| 23 | 2026-11-26 |    8 | Thu | 1pm-4pm  | online | spare      | —      |
| 24 | 2026-11-27 |    8 | Fri | 9am-12pm | online | spare      | —      |

## 4. Notes / decisions
- **Term 2 2026: teaching runs w/c 5 Oct, completing Fri 27 Nov** — 8 weeks x 3 sessions (Thu AM, Thu
  PM, Fri AM) = 24 sessions. No Victorian public holiday falls on a Thursday or Friday in the window
  (AFL Grand Final Friday is 25 Sep, before term; Melbourne Cup is Tue 3 Nov), so all 24 slots are live.
- **No onboarding session.** CL2 starts mid-semester with a cohort already onboarded in CL1; the frame
  was amended accordingly (2026-09-09).
- **Teach then assess, twice.** T1-T5 teach AT1 and T6-T9 teach AT2. AT1 must complete before T6
  begins: its Part C presentation is the design-approval gate that AT2 builds against.
- **All three contingency sessions are held at the end** (S22-S24, 26-27 Nov) rather than spread
  before each assessment. The trade-off: a Topic running long now pushes the assessment that follows
  it, instead of being absorbed in place — but the reserve is pooled, so a single bad week can draw on
  all three rather than only the one session sitting in front of it.
- **Emergency contingency is held OUTSIDE this plan** — w/c 30 Nov and w/c 7 Dec (6 further sessions).
  Not planned into and not expected to be used; the intent is to finish by 27 November.
- Every session is online for this intake.
- **LLN requirements are not held here.** They are derived at generation time from this cluster's own
  units (501/503/505) via `lln_requirements.py` — they have no per-instance variation, so a copy in the
  outline could only go stale when the units change. CL2's units declare no Numeracy demand, so that
  heading is legitimately absent from the generated document.

## Changelog
- 2026-09-09 — initial plan for the 2026-T2 intake.
