# Cluster 2 — Scenario (Assessment)

> **Role:** Assessment · **Vehicle:** Website · per `scenario-flow.md`.
>
> Lean cluster-and-role delta of the greater YAT scenario — see `scenario-flow.md`, the intranet content, and the website ICT specs. This doc records what is specific to **CL2 assessment on the website**. Meta/design doc — uses assessment language freely. Markers: **[AGREED]** confirmed · **[TBD]** open · **[VERIFY]** confirm before it reaches a student-facing artefact.

## 1. Engagement

**Spine — the inciting event:** YAT announces a strategic partnership / offshore campus in India (anchored on GIFT City, Gujarat; a single primary partner). YAT's **public website** — its global front door for prospective students — must now serve a **global / offshore audience**, be **resilient across regions**, and be **provisioned repeatably**. One event motivates all three units on the website:

- **ICTCLD503 (web-scale):** the website serves a genuine global user base of **anonymous, public** visitors (prospective students worldwide + the India cohort) — latency, CDN / edge, scale-out, plus the public-exposure concerns an anonymous front door brings (WAF, bot/DDoS, SEO). *(This anonymous-public character is the one deliberate contrast with the LMS practice vehicle, which serves an authenticated cohort — see `cluster-2-scenario-practice.md`. Otherwise the two engagements are kept similar.)*
- **ICTCLD501 (DR):** as the enrolment front-door for the India campus, the website is business-critical across borders — DR, RTO/RPO and cross-border residency matter.
- **ICTCLD505 (IaC):** stand up the same website stack in a second region, as code (region as a parameter).

Assessment shape (per the CL2 assessment plan): **AT1 — DR Plan** (+ design-approval presentation); **AT2 — Cloud Microservice & IaC Implementation**.

## 2. Scenario deltas

- **Depth = "serve multiple regions," not "replicate data multi-region"** — met by global serving (CDN / edge) + a DR *plan* + *parameterised* IaC. This right-sizes complexity and largely de-risks the AWS Academy single-region constraint.
- **Audit-log microservice (503):** a webhook-driven, serverless, append-only **access-log microservice** — the website emits access / enquiry events via a generic webhook → SQS/SNS → Lambda → DynamoDB / S3. The **India-cohort access logs ship to an India-resident store**. Designing the webhook payload contract is the assessed task (`[ICTCLD503 PC 2.1]`); it is standalone-testable with sample events.
- **Data residency** (delivered via a mock, grounded **Data Residency & Sovereignty Requirements** doc — students design against a controlled requirement, not raw law):
  - **[VERIFY]** **DPDP Act 2023 + DPDP Rules 2025** — permissive "negative list": Indian personal data may transfer abroad by default, so the website's content / enquiry data **may stay in AU**.
  - **[VERIFY]** **CERT-In Directions 2022** — operational logs must be retained **in India for 180 days** (+ 6-hour breach reporting). This is the localisation hook → the audit microservice ships India-cohort access logs to an India store; the main website DB stays in AU.
- **AWS Academy substitution** (per the region-substitution standard, umbrella `docs/`): the Learner Lab is **single-region `us-east-1`**, so **everything deploys to `us-east-1`** while the design stays multi-region. The DR plan (501) and residency design name the real regions — AU `ap-southeast-2`, India `ap-south-1`; the IaC keeps **`region` as a parameter** (the assessed IaC skill — real) but **deploys to `us-east-1`** in the lab (the "second region" is design intent, not a second live region). The India-resident audit-log store (503) deploys as a **dedicated store in `us-east-1`** treated as the India store — the **routing/segregation mechanic is real and assessed; the geography is simulated**. Nothing is built cross-region live. Deploy steps carry the substitution token `[scenario: <real-region> | deploy: us-east-1]`.

## 3. Vehicle state

CL2 assessment operates against a **provided HA-hardened website baseline** — the website hardened to Multi-AZ high availability, supplied as a fixed snapshot the student designs DR, web-scale, IaC, and the microservice *against* (they do not build it). In narrative terms this is the output of the CL3 website-hardening practice; it is provided directly so CL2 does not depend on CL3's actual output. (The 2023 single-AZ pilot is the website's earlier state — CL1 and CL3-practice work from it; CL2 does not.) The HA-hardened state is established by the **Website HA Hardening** project and its as-built HA design.

## 4. Assessed focus

Units **ICTCLD501**, **ICTCLD503**, **ICTCLD505**. The item-level UoC mapping and the AT instruments live in `S1-CL2-Cloud-Disaster-Recovery/`.

## 5. References

- `scenario-flow.md` — cross-cluster system/usage model and the no-leakage invariant
- `cluster-2-scenario-practice.md` — the LMS practice contrast
- Intranet: the **MTS – Website Cloud Migration** project + baseline design; the CL2 offshore-expansion project docs; the **Data Residency & Sovereignty Requirements** doc
- `S1-CL2-Cloud-Disaster-Recovery/` — assessment plan, consolidated UoC, instruments
