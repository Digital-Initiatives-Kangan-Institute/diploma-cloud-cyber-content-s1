# S1-CL1 — teaching Topic sequence (DRAFT)

**Status:** DRAFT, 2026-05-31. The cluster's content + assessment expressed as a **linear sequence of Topics**. A **Topic** is the coherent unit we build teaching + exercise materials for, and the level we schedule into sessions. A Topic groups one or more **chunks** (the finer components), and is **not** session-bound: one Topic may span two sessions, or two small Topics may share one session. Session allocation is a later step.

**Terminology (settled 2026-05-31):** `AT → Topic → chunk`. "Topic" (the delivery unit) aligns with the Delivery Plan template's *"Topic and description"* field and the AWS bespoke *"Topic 1–4"* decks. "chunk" = the finer teaching/activity component (formerly called "topic" in the decomposition drafts). The per-Topic **chunks** column below is a first cut of the explicit chunk→Topic mapping; formalising/verifying that mapping is an upcoming step. Chunk detail (coverage, activity, UoC tags) lives in the `at<n>-topic-decomposition-draft.md` chunk-inventory drafts; deck mapping in `aws-deck-catalogue-draft.md`.

**Teach / practice / assess rhythm at Topic scale:** content Topics teach + build a *practice* artefact in a **different scenario** than YAT (the Accounting System engagement); assessment Topics are where students produce/defend their **real** AT against YAT (the LMS engagement).

**Bookend anchors (fixed, from `cl1-delivery-sessions-draft.md`):** S1 = onboarding; S29 = AT3 baseline-deploy prep; S30 = AT3 implementation/outage window; S31–S32 = catch-up/resit. Everything else flows across S2–S28.

**TBD:** AT2/AT3 Topic groupings (Topics 9+) are proposed; Topic count and ordering not locked.

---

## Topic 0 — Onboarding *(S1, fixed)*
Orientation, systems/email/LMS access, scenario introduction. Not a content Topic.

## AT1 — Business Case *(Topics 1–8)*

| # | Topic | chunks | Teaching source | Nature |
|---|---|---|---|---|
| 1 | **Cloud literacy** (knowledge base) | AT1 T1–T5 | AWS decks (ACF M01/M02/M04/M06–M10, ACA M02) | teach + light activity |
| 2 | **The case for change** (diagnosis) | AT1 T6–T8 | bespoke | teach + practice (BC §3–§5) |
| 3 | **Building the evidence** (evaluation) | AT1 T9–T12 | mixed (Pricing Calculator activity + bespoke) | teach + practice (BC §6–§8, App. 1 & 3) |
| 4 | **The decision & the plan** | AT1 T13–T15 | bespoke | teach + practice (BC §9–§11) |
| 5 | **Making the case** (communication) | AT1 T16–T19 | bespoke | teach + practice presentation (of the practice BC) |
| 6 | **AT1 report preparation** | — | — | **assessment**: students produce their real Business Case (Part A) |
| 7 | **AT1 presentation rehearsal** | — | — | rehearse the real board presentation |
| 8 | **AT1 presentation assessment** | — | — | **assessment**: deliver Part B board presentation + Q&A + sign-off |

*Topics 2–5 build one cumulative practice business case (the Accounting System, different scenario); Topic 1 is the shared foundation with AT2.*

## AT2 — Cloud Foundation Build *(Topics 9–14, proposed)*

| # | Topic | chunks | Teaching source | Nature |
|---|---|---|---|---|
| 9 | **Build foundations** — working to a supplied design, console/region/evidence discipline, IAM, shared responsibility | AT2 T1,T2,T3,T11 | AWS decks (ACA M02/M03, ACF M03/M04) + bespoke (evidence discipline) | teach + practice build |
| 10 | **Network & security base** — VPC, security groups, DNS | AT2 T4,T5,T12 | AWS decks (ACF M05, ACA M07) | teach + practice build |
| 11 | **The workload tier** — EC2/EBS, ALB+ASG, RDS, S3 | AT2 T6,T7,T8,T9 | AWS decks (ACF M06–M08/M10, ACA M04/M05/M06, M10) | teach + practice build (largest Topic) |
| 12 | **Operability & justification** — CloudWatch baseline, config-decision justification, testing/validation | AT2 T10,T13,T14 | mixed (ACF M10 / ACA M10 + bespoke for the justify-against-workload + test discipline) | teach + practice build |
| 13 | **Evidencing & documenting** — evidence capture, Deployment Report writing, contextual KE, reflection | AT2 T15,T16,T17,T18 | bespoke | teach + practice |
| 14 | **AT2 assessment** | — | — | **assessment**: build the supplied YAT design in lab + produce the Deployment Report (single deliverable, no presentation) |

*Topics 9–13 build one cumulative practice stack (the Accounting System, different workload); Topic 14 is the real YAT LMS build. Cloud literacy (Topic 1) is assumed — these Topics build the services students met conceptually there.*

## AT3 — High Availability *(Topics 15–22, proposed)*

| # | Topic | chunks | Teaching source | Nature |
|---|---|---|---|---|
| 15 | **HA concepts** — fault tolerance/SPOFs/recovery objectives, scaling, built-in vs designed FT, LB+autoscaling for availability | AT3 T1–T4 | bespoke 502 Topics 1–3 + ACF M09 / ACA M10 | teach + light activity |
| 16 | **HA design** — baseline review & SPOFs, design the HA-equivalent, sequencing, simulation planning | AT3 T5–T8 | bespoke 502 Topic 2–3 + ACA M06/M10 | teach + practice (Part A skills) |
| 17 | **HA implementation & simulation** (practice) — implement in-place, failure sim, resize sim, availability measurement, compare/adjust, testing | AT3 T9–T14 | bespoke 502 Topic 4 + ACA M10/M11 | teach + practice build/simulate |
| 18 | **Closure & documentation** — engagement closure/sign-off, deliverable writing, contextual KE, reflection | AT3 T15–T18 | bespoke | teach + practice |
| 19 | **AT3 assessment — Part A: HA Design** | — | — | **assessment**: students produce their real HA Design document |
| 20 | **AT3 baseline-deploy prep** *(S29, fixed)* | AT3 T9 (CloudFormation) | ACA M11 | **assessment prep**: deploy the supplied AT2 baseline via CloudFormation to a known start state |
| 21 | **AT3 assessment — Part B: implementation + simulation window** *(S30, fixed)* | — | — | **assessment**: in-place HA hardening + failure/resize simulations in the ~3.5h maintenance window |
| 22 | **AT3 HA Deployment Report + engagement closure** | — | — | **assessment**: produce the HA Deployment Report, capture feedback, obtain final sign-off — closes the engagement |

## Catch-up *(S31–S32, fixed)*
Spare / resit / extra time; finished students may skip. Not a content Topic.

---

## Sequence summary

`S1 onboarding → [AT1: 1 literacy · 2 case-for-change · 3 evidence · 4 decision/plan · 5 making-the-case → 6 report prep · 7 rehearsal · 8 presentation assessment] → [AT2: 9 foundations · 10 network/security · 11 workload · 12 operability · 13 documenting → 14 build+report assessment] → [AT3: 15 HA concepts · 16 HA design · 17 implement/simulate · 18 closure → 19 HA Design assessment · 20 baseline prep (S29) · 21 window (S30) · 22 report+closure] → S31–32 catch-up`

**22 content/assessment Topics** across **27 teaching sessions (S2–S28)** plus the fixed S29/S30 anchors.

> **Note on `chunks` column IDs:** the `AT1 T1–T5`-style identifiers are the chunk IDs inherited from the chunk-inventory drafts (which still use a `T` prefix). They are *chunks*, not Topics. They can be relabelled when we do the explicit chunk→Topic mapping step.

## Upcoming steps (not yet done)

1. **Explicit chunk→Topic mapping** — formalise/verify which chunks belong to which Topic (the `chunks` column above is the first cut).
2. **Flesh out each Topic** — teaching-content outline + concrete re-scenarioed activity per Topic (pulling chunk detail up from the inventory drafts).
3. **Size Topics against the tempo bands** and lay them onto S2–S28.
