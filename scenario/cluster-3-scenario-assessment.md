# Cluster 3 — Scenario (Assessment)

> **Role:** Assessment · **Vehicle:** Ledgerline (Accounting) · per `scenario-flow.md`.
>
> Lean cluster-and-role delta — see `scenario-flow.md` and the Accounting ICT records. This doc records what is specific to **CL3 assessment on Ledgerline**. Meta/design doc.

## 1. Engagement

A student **team**, led in rotation, is engaged to **improve the cloud infrastructure** of YAT's **Ledgerline (Accounting)** system — confirming it is stable, reliable, fit for purpose, and **compliant with the Indian regulatory requirements** arising from YAT's India-campus partnership — across **security, reliability, scalability, and cost** (ICTCLD504), while practising **team leadership and facilitation** (BSBXTW401). The team **analyses** the baseline, **proposes** improvements in a **business case**, and **implements** those YAT approves. The cluster runs **individual → group → individual**: AT1 engagement setup / AT2 group improvement design via led meetings / AT3 implement an owned dimension.

## 2. Scenario deltas

- **Owned-dimension model:** each student owns one of security / reliability / scalability / cost → individual 504 evidence inside a group effort.
- **Team leadership (401):** each student leads ≥ 1 meeting → an **assessor observation checklist** (primary performance evidence, incl. *managed a conflict*) + a **reflection** appendix (secondary) + a **performance review**. How the assessor stimulates a conflict is the assessor's conduct, out of the instrument's scope.
- **Financial-system criticality** gives the improve-loop real stakes — regulatory exposure, tight RTO/RPO, 7-year audit retention — a substantive contrast to the lower-stakes website practice vehicle.
- **India-campus compliance driver.** The engagement is triggered by YAT's India-campus partnership: the team assesses whether Ledgerline's infrastructure meets the applicable **Indian regulatory requirements** (DPDP Act, CERT-In log residency, financial-records obligations) and proposes what would close any gaps — alongside the general reliability / scalability / security / cost improvement. The **Indian Regulatory Requirements are provided** (the YAT Compliance area owns the law; the team designs the infrastructure to it); the compliance **analysis and proposals are student-authored**. The improvement is open — students may or may not harden for HA; it depends on their analysis.
- **Ledgerline single-AZ cloud baseline (AT1 analysis input).** CL3 improves Ledgerline's cloud infrastructure from a single-AZ baseline, established by the completed **Accounting System Cloud Migration** engagement (on-prem → single-AZ cloud; HA deferred). The `s1-cl3-at1` state must surface, as AT1's analysis inputs: the accounting **cloud ICT records** (application specification, operational costing, infrastructure/server specifications), the **Accounting Baseline Solution Design** (single-AZ architecture), and a network topology depicting the **Ledgerline single-AZ** environment.

## 3. Vehicle state

CL3 improves Ledgerline from a **single-AZ cloud baseline** — the `network-accounting-baseline-singleaz` topology and the Accounting Baseline Solution Design (single-AZ; HA deferred) — toward a hardened state. The baseline is established by the completed Accounting System Cloud Migration engagement (§2); these baseline records must be available in the `s1-cl3-at1` state as the team's analysis inputs. The improved target states are the team's assessed output.

**Provided engagement.** The CL3 vehicle is the **Ledgerline Cloud Infrastructure Improvement** project, whose **provided framing** (Master Services Agreement, Engagement Role Brief, Improvement Requirements, ICT Manager Consultation Notes, Indian Regulatory Requirements) sets up the engagement **without pre-supplying student work**: the team authors the **Team Plan**, the **requirements & architecture analysis** (incl. the compliance assessment), the **improvement design**, the **business case**, and the **implementation**. Standing state requirements for `s1-cl3-at1`: the Accounting Baseline Solution Design and the cloud ICT records (incl. a network topology depicting the Ledgerline single-AZ environment) remain available as the team's analysis inputs.

## 4. Assessed focus

Units **ICTCLD504**, **BSBXTW401**. The plan and UoC mapping live in `S1-CL3-Cloud-Infrastructure-Improvement/`.

## 5. References

- `scenario-flow.md`; `cluster-3-scenario-practice.md` — the website practice
- **Baseline foundation** (the single-AZ Ledgerline the team improves): the completed *Accounting System Cloud Migration* project; the accounting cloud ICT records (application specification, operational costing, infrastructure/server specifications); the *Accounting Baseline Solution Design*; the `network-accounting-baseline-singleaz` topology
- **Improvement engagement** (CL3 vehicle): the *Ledgerline Cloud Infrastructure Improvement* project — provided framing: Master Services Agreement, Engagement Role Brief, Improvement Requirements, ICT Manager Consultation Notes, Indian Regulatory Requirements
- `S1-CL3-Cloud-Infrastructure-Improvement/` — assessment plan, consolidated UoC
