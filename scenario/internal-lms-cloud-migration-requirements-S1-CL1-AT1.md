# YAT College — LMS Cloud Migration: Functional and Non-Functional Requirements

**Relevant to:** S1-CL1 AT1, AT2, AT3

**UoC references this document satisfies:**
- [ICTCLD502 AC 5] business and functionality requirements
- [ICTCLD502 PC 1.1] Determine reliability, recoverability and service levels required for application
- [ICTCLD502 PC 1.2] Determine cloud infrastructure according to business needs

**Source status:** ✅ Complete — rebranded from Llamazonia (502 AT2 Activity 1) to YAT LMS context on 2026-05-23. OS changed from Linux to Windows Server 2016 (per the YAT migration role brief); availability target adjusted to 99.9% (per the YAT ICT Strategic Plan); cloud certification claim reattributed to MTS (since YAT ICT staff lack cloud expertise per the case study).

---

## Context

The following functional and non-functional requirements for the YAT LMS cloud migration were established during the consultation with the YAT ICT manager — see `internal-ict-manager-consultation-notes-S1-CL1-AT1.md` for the consultation record this list was derived from. These requirements drive the cloud foundation build (AT2) and the high-availability hardening (AT3).

## Requirements

The migrated YAT LMS must:

- **Run on a cloud vendor supported by the engaged consultancy.** YAT's ICT staff have limited cloud experience (per the YAT case study). The cloud vendor selection must align with the qualifications of the MTS consultancy supporting the migration. MTS holds AWS Certified Cloud Practitioner and AWS Certified Solutions Architect certifications, so **AWS is the cloud platform of choice**.
- **Achieve 99.9% availability.** YAT requires the migrated LMS to be available and operating normally at least 99.9% of the time. This is a step change from the current on-prem baseline of 99.2% and is the success criterion stated in YAT's ICT Strategic Plan.
- **Preserve the existing OS and application stack.** The LMS will continue to run on Windows Server 2016 with the existing DOODLE application and MySQL database. Full administrative control of the operating system is required to install and maintain the LMS application stack. Per the migration role brief, the OS and application software versions will not change as part of the transition.
- **Meet RTO ≤ 4 hours and RPO ≤ 1 hour.** In a system failure, the LMS must be recoverable with no more than 1 hour of data loss (RPO ≤ 1 hour) and back to operational service within 4 hours (RTO ≤ 4 hours).
- **Scale flexibly with demand.** All scalable components of the migrated infrastructure must scale up and down automatically in response to changes in demand. YAT's LMS load varies substantially across the academic calendar — typical weekday teaching hours, ~3× concurrent users during assessment submission windows (last two weeks of each term), and very low load overnight and during term breaks.
- **Receive prompt vendor support for severity-1 incidents.** When the LMS is down, the cloud vendor must respond to severity-1 support requests within 1 hour.
- **Add capacity automatically to maintain performance.** When user demand increases significantly or response time degrades, the system must add resources automatically to maintain performance against the LMS application specification's SLA targets.
- **Reduce running cost during quiet periods.** When demand reduces (overnight, weekends, term breaks), the system must scale down to reduce running cost.
