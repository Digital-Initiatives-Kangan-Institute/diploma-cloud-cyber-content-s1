# Topic 6 — Build foundations · Coverage

**Topic 6 of 14** · **AT2 content Topic** (cloud build — foundation tier) · teaching source: **mixed** — AWS decks (ACA M02/M03, ACF M03/M04) for the AWS skills + **bespoke** for working-to-a-design and evidence discipline.

The coverage spec — what this Topic must cover, in UoC and AT2 terms. `slide_plan.md` and the deck are built to satisfy it.

> **New sub-arc.** This is the first **AT2** Topic — the shape changes from AT1: students *build* in the AWS Academy lab (not write a document), implementing a **supplied design**, and capturing **evidence** as they go for the Deployment Report. AT2 = ICTCLD401 (primary) + ICTCLD502 (partial). Per the AT2 assessor doc, the deliverable is a single Deployment Report; there is no presentation.

---

## What this Topic must cover

The **foundation tier** of the cloud build and the disciplines that frame the whole AT2 engagement: working to someone else's design, setting up the account/region, capturing evidence, and standing up identity/access + the shared-responsibility model. Three components:

- **C1 — Working to a supplied design (+ account/region + evidence discipline).** The AT2 mode: implement a design *you didn't write* (the supplied baseline). Read the design, set up the AWS account and **Region** (data-residency driven), and — the consulting discipline — **capture build evidence** (named screenshots + config exports) as you go, because the Deployment Report is evidenced from it.
- **C2 — Identity & access management (IAM).** Configure access per the design: groups, users, roles, permissions, MFA enforcement.
- **C3 — Shared security responsibility.** Who owns what across vendor / YAT / MTS / end-users; assign security responsibilities to the build.

---

## 1. UoC mapping

UoC **taught / developed** in this Topic:

| UoC item | Descriptor | Component |
|---|---|---|
| [ICTCLD401 PC 1.4] | Access account on cloud platform according to business requirements | C1 |
| [ICTCLD401 PC 1.2] | Identify impact of shared security responsibility models | C3 |
| [ICTCLD502 PC 1.3] | Identify level of shared security responsibility models according to business needs | C3 |
| [ICTCLD401 PC 1.5] | Identify user access protocols and policies | C2 |
| [ICTCLD401 PC 1.6] | Configure access functions — users, groups, required permissions | C2 |
| [ICTCLD401 PC 1.7] | Identify and assign security responsibilities per policies/protocols/work function | C2 · C3 |
| [ICTCLD401 PC 2.1] | Create users and groups to create and manage infrastructure | C2 |
| [ICTCLD401 KE 7] | User, business and vendor responsibilities under shared security models | C3 |
| [ICTCLD401 KE 8] | User access protocols and policies per hierarchy and job function | C2 |
| [ICTCLD401 PE 1 · PE 2] | The built artefacts are the evidence (foundation-tier portion) — captured here | C1 |

> AT2 criterion **A2** (Foundation-tier build narrative: IAM, network, security) is the marking home for most of these. **A2 bundles IAM + network + security**; this Topic takes **IAM + shared responsibility**, and **network + security groups go to Topic 7**. *(Confirm this split.)*

UoC **applied** here but **taught earlier** (not re-taught):

| What | Where |
|---|---|
| What IAM / regions / shared responsibility *are* (conceptual) | Topic 1 (§3 Core AWS Services, §2 service models) — Topic 6 *builds* them |
| The cloud-service / IaaS-PaaS-SaaS framing | Topic 1 |

---

## 2. AT2 equivalence / alignment

| AT2 element | Criterion | How Topic 6 aligns |
|---|---|---|
| **§4.1 IAM** (Build Narrative — foundation tier) | A2 | C2 — groups/users/MFA/permissions, evidenced in Appendix A screenshots + Appendix B exports. |
| **§4.7 Security — shared responsibility** | A2 *(/ A4 in the section detail)* | C3 — the shared-responsibility model assigned to the build (refs the supplied design's §9.4). |
| **Account / Region setup; build-evidence capture** | A9 · A10 (Appendices A/B) | C1 — correct Region visible in evidence; named screenshots/exports captured as built. |

**Practice-activity alignment:** students stand up the **foundation tier** (account/Region + IAM + shared-responsibility assignment) of the **practice** engagement in the AWS Academy lab, capturing evidence — mirroring the AT2 foundation build on a different system.

> **⚠ Dependency (flag).** The AT2 *practice* runs on the Accounting System and assumes a **supplied Accounting baseline design** for students to implement (the analogue of the YAT-LMS Baseline Solution Design used in the real AT2). That design **does not yet exist** — Topics 6–10 (the cumulative practice build) need it authored. For Topic 6 alone a light "set up the foundation per this spec" suffices, but the AT2 arc needs the practice design resolved.

---

## Out of scope for this Topic (covered elsewhere)

- **Network & security groups, DNS** (§4.2 VPC/subnets/SGs) → **Topic 7**.
- **Compute / ALB / DB / storage** (the workload tier) → **Topic 8**.
- **CloudWatch, config-decision justification, testing** → **Topic 9**.
- **Writing the Deployment Report** (evidence is *captured* here; the report is *written*) → **Topic 10**.
- **What these services are, conceptually** → **Topic 1** (applied here, built not re-taught).
- **HA / Multi-AZ** — explicitly deferred to AT3.

---

## Coverage checklist (for `slide_plan.md` + the deck to satisfy)

- [ ] Every UoC item in §1 (taught/developed) is taught in the deck.
- [ ] Each of C1–C3 has teaching content + a practice activity (hands-on in the lab, not a document).
- [ ] The "working to a supplied design" mode + **evidence-capture discipline** (named screenshots / config exports) is taught explicitly (C1).
- [ ] Region selection is tied to **data residency** (C1).
- [ ] IAM build (groups/users/MFA/permissions) is taught + practised (C2).
- [ ] Shared-responsibility model is taught + assigned to the build (C3).
- [ ] AWS slices (ACA M02/M03, ACF M03/M04) are pinned in the slide plan; bespoke covers working-to-design + evidence discipline.
- [ ] Depth ceiling respected: stand up the foundation per a supplied design — non-HA, no Multi-AZ.
- [ ] AT2 alignment (§2) is explicit enough that a student leaving this Topic could build + evidence the foundation tier.
