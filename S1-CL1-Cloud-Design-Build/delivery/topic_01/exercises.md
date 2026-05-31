# Topic 1 — Cloud literacy · Exercises

Practice for Topic 1, by coverage component (see `coverage.md`). For each: an **[AWS]** reference to an existing AWS Academy activity where one fits, or a **[BESPOKE]** write-up where none does.

**Tempo:** knowledge-heavy / light activity (top band) — the trainer picks from these within the activity budget; the **bespoke capstone** is the one to prioritise, as it rehearses the AT1 Appendix 2 form on the practice scenario. Bespoke exercises are set on the **YAT Accounting System (Ledgerline)** — the practice system, not the LMS.

---

## C1 — Cloud fundamentals & deployment models *(→ Appendix 2 Q2)*

**[AWS] ACF Module 1 — Knowledge check** *(S43):* formative MCQ on cloud concepts. Use as a quick check after the C1 teach.

*(Deployment-model selection is practised in the capstone, Q2.)*

---

## C2 — Service models: IaaS / PaaS / SaaS *(→ Appendix 2 Q1)*

**[BESPOKE]** — no Topic-1-owned AWS activity (AWS's "EC2 vs Managed Service" classification activity lives in M6, which is AT2). Covered by the **capstone, Q1** below — the classification of the Accounting System's components is the practice for this component.

---

## C3 — Core AWS services (name + role) *(→ Appendix 2 Q4)*

**[AWS] ACF Module 3 — "AWS Management Console clickthrough" activity** *(S24–26, has an answer key):* students explore the console and identify which service category each service sits under (IAM → Security; VPC → Networking; etc.). Good for fixing the service-catalogue map.

*(Naming the services + roles for the actual workload is practised in the capstone, Q4.)*

---

## C4 — Industry technology standards *(→ Appendix 2 Q3)*

**[AWS] ACF Module 9 — "AWS Well-Architected Framework Design Principles" activity** *(S9–40):* small groups work through the pillar questions. Use for the WAF half of C4.

**[BESPOKE] — "Match the standard to the decision"** (the non-AWS standards AWS doesn't cover):
```
Given five migration decisions (service-type choice, security controls, change-management
alignment, the HA/reliability approach, defining IaaS/PaaS/SaaS), match each to the standard
that informs it: NIST SP 800-145 · AWS Well-Architected · ISO/IEC 27017 · ACSC Essential
Eight · ITIL 4. One line each on why.
```
Short matching task — reinforces "name the right standard for the decision," which is what Q3 asks.

---

## C5 — Cloud cost models & economics *(→ Appendix 2 Q5)*

**[AWS] ACF Module 2 — "AWS Pricing Calculator" activity** *(S22):* groups build a cost estimate from supplied specs. **Run it on the Accounting System specs** (provide the Ledgerline workload sizing) rather than the generic specs — this doubles as the seed for the Topic 3 CBA.

**[AWS] ACF Module 2 — "Total Cost of Ownership" case study** *(S24–29):* optional, for the on-prem-vs-cloud cost-thinking.

---

## Capstone *(BESPOKE)* — "Cloud literacy on the Accounting System" *(→ Appendix 2 Q1–Q5)*

The core practice piece — same shape as AT1 Appendix 2, different system.

```
Supplied: a sketch of how YAT's Accounting System (Ledgerline) could run in AWS —
  Internet → ALB → EC2/Auto Scaling Group (Ledgerline app, Windows Server)
           → RDS for SQL Server   (+ S3 for scanned invoices/POs, CloudWatch monitoring)

Answer briefly (a short paragraph each), referencing this solution:
  Q1  Classify each component as IaaS / PaaS / SaaS and justify.
  Q2  Which deployment model is this, and why is it the right fit for YAT?
  Q3  Name three industry standards that would inform this migration, and what each informs.
  Q4  Name each AWS service in the sketch and its general feature / role.
  Q5  Which pricing model suits each component, and how does total cost scale with demand?
      (Note the commercial-licensing angle: SQL Server + Ledgerline licences — BYOL vs
       licence-included — which the open-source LMS doesn't have.)
```

**Why this is the practice that matters:** it is the exact form of AT1 Business Case Appendix 2 (Q1–Q5), set on the Accounting System. A student who can do this on Ledgerline is ready to do it on the LMS in the assessment — without having rehearsed the LMS answers.

---

## Facilitator notes

- **Reuse first:** C3, C4 (WAF), and C5 are existing AWS activities — run them as-is (C5 with Accounting specs). Only C2 and the non-AWS-standards half of C4 are bespoke.
- **Prioritise the capstone** if time is short — it covers Q1–Q5 and absorbs the C2 classification gap.
- Indicative answers for the capstone live with the trainer (model: EC2/EBS = IaaS, RDS/ALB = PaaS, S3 = object storage/IaaS-ish, Office 365 = SaaS but out of scope; public cloud; standards per the C4 list; cost models per the C5 teach).
