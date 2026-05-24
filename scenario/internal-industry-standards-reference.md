# Industry Standards Reference List

**Relevant to:** All clusters

**UoC references this document satisfies:**
- [ICTCLD401 KE 1] industry technology standards used in cloud computing solutions and services
- [ICTCLD502 KE 1] industry technology standards used in cloud computing solutions and services
- [ICTCLD502 AC 5] industry standards

**Source status:** ✅ Authored 2026-05-23 (Claude). Curated reading list of standards relevant to YAT's cloud migration and ongoing cloud operations. Selection skews toward standards the cluster ATs will plausibly draw on; not intended to be exhaustive.

---

## How to use this list

Students should refer to this list when an assessment task calls for application of "industry technology standards" or "industry standard hardware and software". Cite the relevant standard by name and version where applicable. Where the YAT scenario or a specific cluster AT calls out a particular framework (e.g. the User Access Policy is aligned to the ACSC Essential Eight), use that framework for the specific work and reference this page for the broader landscape.

## Cloud computing — foundational definitions

- **NIST SP 800-145 — The NIST Definition of Cloud Computing.** Authoritative definitions of the service models (IaaS / PaaS / SaaS) and deployment models (private / public / hybrid / community) used throughout the cluster.
- **ISO/IEC 17788 — Cloud computing — Overview and vocabulary.** Aligned international counterpart to NIST 800-145.

## Cloud security and privacy

- **ISO/IEC 27001 — Information Security Management Systems (ISMS).** The umbrella standard for information security controls; YAT's security baseline (see `internal-security-and-incident-response.md`) is broadly aligned to its control families.
- **ISO/IEC 27017 — Code of practice for information security controls based on ISO/IEC 27002 for cloud services.** Cloud-specific extension of ISO 27001/27002; covers shared-responsibility allocation and cloud-specific controls.
- **ISO/IEC 27018 — Code of practice for protection of personally identifiable information (PII) in public clouds.** Relevant when YAT is processing student PII in AWS.
- **ACSC Essential Eight (Australian Cyber Security Centre).** YAT's security baseline is aligned to this — see the `internal-security-and-incident-response.md` baseline mapping.
- **Australian Government Information Security Manual (ISM) — Cloud Computing chapter.** ACSC guidance on consuming cloud services; relevant where YAT processes student personal information.

## Architecture frameworks

- **AWS Well-Architected Framework.** Six pillars — Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimisation, Sustainability. Used for review and design rationale across the cluster's AWS work.
- **AWS Cloud Adoption Framework (CAF).** Six perspectives (Business, People, Governance, Platform, Security, Operations) for cloud-adoption planning. Relevant to the AT1 strategic-alignment work.
- **Microsoft Cloud Adoption Framework.** Useful for context-only given YAT's Windows Server / O365 footprint.

## Operational management

- **ITIL 4 (IT Infrastructure Library).** Service management framework — particularly the change management, incident management, and service request management practices referenced in YAT's Change Management Procedure and Security & Incident Response policy.
- **ISO/IEC 20000 — Service management.** Aligned international standard for service management; conceptually close to ITIL.

## Web application and data

- **OWASP Top 10 (Open Web Application Security Project).** The standard reference list of web-application security risks; relevant to the LMS as a web application exposed (post-migration) to the internet.
- **OWASP Application Security Verification Standard (ASVS).** Deeper application-security control catalogue.
- **WCAG 2.1 Level AA (Web Content Accessibility Guidelines).** Required for YAT's LMS per the LMS application specification's accessibility section; also feeds the Disability Discrimination Act 1992 (Cth) compliance.

## Network and identity

- **IETF RFC standards** for the underlying protocols (TCP/IP, DNS, TLS, OAuth 2.0, OIDC, SAML 2.0). Not a single document — cited individually when the work calls for it.
- **NIST SP 800-63 — Digital Identity Guidelines.** Authentication and identity management reference.

## RTO-sector specific

- **Standards for Registered Training Organisations (RTOs) 2015.** ASQA-administered; sets the framework within which YAT operates. Cross-referenced from the Privacy Policy and the Backup and Retention Policy.
- **AVETMISS (Australian Vocational Education and Training Management Information Statistical Standard).** Data reporting standard for RTO statutory reporting to ASQA / DET; referenced in the LMS application specification's reporting requirements.

## Notes

- Standards versions listed are the latest at the time of writing (2026). Where a more recent version is published before delivery, the more recent version applies.
- Several standards above are paywalled (ISO/IEC items). Where students need to read source text, the institution library or vendor summaries (e.g. AWS documentation summaries of the Well-Architected pillars) are acceptable secondary sources.
