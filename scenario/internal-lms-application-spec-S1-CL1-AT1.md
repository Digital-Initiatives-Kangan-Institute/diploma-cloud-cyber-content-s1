# YAT College — LMS Application Specification

**Relevant to:** S1-CL1 AT1, AT2, AT3

**UoC references this document satisfies:**
- [ICTCLD502 AC 5] business and functionality requirements
- [ICTCLD502 AC 3] information and data sources required to design and implement cloud infrastructure
- [ICTCLD401 PC 1.8] Define workload according to business requirements and needs

**Source status:** ✅ Complete — basic description from YAT case study preserved verbatim; remaining sections are Claude-authored using plausible defaults for an Australian RTO LMS and marked **TBD** for confirmation.

---

## What YAT source material tells us

YAT is using 'Diverse Object-Orientated Dynamic Learning Environment' (DOODLE) as their custom learning and student management system (LMS).

### Functions used by students
- Access course-related resources
- Submit assessments

### Functions used by teachers
- Record student attendance
- Record assessment submission
- Record unit completion
- Record student's notes
- Other applicable student management tasks including support and notifications for classes

### Technical platform
- Runs on Windows Server 2016
- Uses a MySQL database
- Distributed under the GNU General Public License Support
- Application support and customisation provided by MP Tech Solutions (MTS)

---

## Extended functional specification **TBD**

The following sections are Claude-proposed; confirm with Tim before treating as authoritative.

## Functions used by Administrative staff

- Enrol students into qualifications and units
- Manage student records (contact details, enrolment status, fee status)
- Issue notifications to staff and students
- Export reports (enrolments, attendance, completions) for compliance reporting to ASQA and DET

## Functions used by ICT staff

- Administer accounts (via AD integration)
- Configure course shells, permissions, user groups
- Support, troubleshoot, and restore (per the Backup and Recovery Process)

## User population and concurrent load **TBD**

| Metric | Value |
|---|---|
| Total user accounts | ~860 (800 students + 60 staff) |
| Typical concurrent users (weekday teaching hours) | ~200–300 |
| Peak concurrent users (assessment submission windows, last 2 weeks of term) | ~500–700 |
| Off-hours concurrent users (overnight, weekends) | ~20–50 |
| Assessment submission spike pattern | ~3× typical concurrent users for ~10–14 days each term |

## Data stored **TBD**

| Data category | Approx volume | Storage location | Notes |
|---|---|---|---|
| Student records (PII, enrolment, fee status) | ~50 MB | MySQL DB | Subject to Privacy Act 1988 + APPs |
| Course content (text, structured materials) | ~10 GB | MySQL DB + filesystem references | Authored in LMS by Trainers |
| Course attachments (PDFs, slides, video links) | ~80 GB | Filesystem on LMS server | Growing ~15 GB/year |
| Student submissions (assessments) | ~30 GB | Filesystem on LMS server | Growing ~10 GB/year; retained per RTO records-retention obligations |
| Gradebook / outcomes | ~5 GB | MySQL DB | Statutory retention applies |
| Attendance records | ~2 GB | MySQL DB | Statutory retention applies |
| Audit logs (LMS-internal) | ~1 GB | MySQL DB | Rolling 12 months retention |
| **Total data footprint (current)** | **~178 GB** | (consistent with ~250 GB allocated storage at ~70% used per `internal-lms-server-status-S1-CL1-AT1.md`) | |

## Authentication / SSO

- Integrated with Active Directory via LDAP bind (current state).
- Single sign-on from AD-joined campus desktops via Integrated Windows Authentication.
- Off-campus access requires interactive sign-in (AD credentials + MFA for staff with grading or course-management roles per the User Access Policy).
- **TBD:** confirm whether the LMS supports modern federated SSO (SAML / OIDC). If yes, migration to AWS-hosted environment should preserve federated SSO using AWS IAM Identity Center or a third-party identity provider.

## Integration points **TBD**

| External system | Integration type | Direction | Purpose |
|---|---|---|---|
| Active Directory 2016 | LDAP bind | LMS → AD | Authentication |
| Application Services system (Accounting / Office Admin) | Manual export / batch import | LMS → AppSvc (enrolment data); AppSvc → LMS (fee status flags) | Tuition fee management |
| Office 365 (email) | SMTP outbound | LMS → O365 | Student and staff notifications |
| ASQA / DET reporting | Manual export (CSV) | LMS → external regulators | Statutory compliance reporting |

## Reporting / export requirements

- Monthly attendance report (PDF + CSV)
- Quarterly enrolments and completions report
- Annual ASQA AVETMISS reporting export (statutory)
- Ad-hoc grade and submission exports per Program Leader request

## Browser and device support

- **Supported browsers (current):** Microsoft Edge (Chromium), Google Chrome, Mozilla Firefox, Apple Safari — last two major versions of each.
- **Mobile / tablet:** the LMS web UI is responsive; supports student access from personal mobile devices for read-only and submission-upload use cases. Trainer authoring is desktop-only.
- **Native apps:** none currently.

## Service-level expectations

| Service-level metric | Current value | Migration target |
|---|---|---|
| Availability (rolling 12 months) | 99.2% | **99.9%** (per ICT Strategic Plan) |
| RPO (acceptable data loss in incident) | ~24 hours (nightly backups) | **≤ 1 hour** (per LMS Cloud Migration Requirements) |
| RTO (time to recover from a major outage) | ~7–11 hours (per Backup and Recovery Process) | **≤ 4 hours** (per LMS Cloud Migration Requirements) |
| Support response (during business hours) | Best-effort by YAT ICT + MTS | ≤ 1 hour from cloud vendor for severity-1 incidents (per LMS Cloud Migration Requirements) |

## Backup and maintenance windows

- **Backup window:** nightly, 22:00–04:00 local time (Melbourne).
- **Maintenance window:** Sunday 02:00–06:00 local time, by prior change-management notification.
- **Restrictions:** no maintenance during assessment submission windows (last 2 weeks of each term) except for severity-1 incidents.

## Accessibility

- The LMS must meet **WCAG 2.1 Level AA** conformance, consistent with YAT's obligations under the *Disability Discrimination Act 1992* (Cth) and good practice for an Australian RTO. **TBD** confirm with YAT Compliance Manager.

## Data residency

- **All YAT student personal information and student records must remain within Australia** to support compliance with the Privacy Act 1988, the Australian Privacy Principles (APP 8 — cross-border disclosure), and the Standards for RTOs 2015. The migrated LMS infrastructure must be deployed in an Australian cloud region (e.g. AWS `ap-southeast-2` Sydney).

---

**Notes for the cluster engagement:**
- The student (acting as MTS consultant) should treat this specification as the design brief for AT2 (cloud foundation build) and AT3 (HA design). The SLA targets in the table above are the targets to design to.
- The migration brief states "no intention to change the OS and/or application software versions as part of the transition" — so the migrated environment must still run Windows Server 2016 + MySQL with the existing DOODLE codebase (per the role brief). Cloud-native re-platforming (e.g. moving to a managed PaaS LMS) is out of scope for this engagement.
