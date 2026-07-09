# YAT Scenario — Mock Website Specification

**Document type:** Meta — specification for the delivery vehicle, not scenario content. Reader audience is the team building the mock website, not students.

**UoC references this document satisfies:** None directly — this is the spec for *how* the scenario content (which does satisfy UoC ACs) is delivered to students.

**Status:** Specification for the delivery website (built on Astro — see the `diploma-cloud-cyber-website` repo). Items marked **TBD** are open.

---

## 1. Intent

The mock website is the delivery vehicle for the cluster scenario materials. Rather than handing students a bundle of separate documents, the scenario content is published as a website that students browse like a real corporate site + intranet during their cluster assessments. This reduces incongruence between the consultant-engagement narrative and the way reference materials are consumed: students "log in" to YAT's intranet, navigate by area, and read the materials in context — much as they would on a real engagement.

The intent is **realism + navigability**, not technical fidelity. The website is read-only, has no authentication backend, and stores no user data.

## 2. Site structure

The site has two distinct zones with different visual identity (per `scenario/branding/brand-pack.md` §5.1) and different content principles:

- **Public site** — marketing IA, warm cream background, marketing-adjacent voice
- **Intranet** — functional IA, neutral light-grey background, procedural voice; entered via the mock SSO sign-in gate (§3)

Every page on both zones carries the persistent simulated-environment disclosure banner described in `scenario/branding/brand-pack.md` §5.3.

### 2.1 Content principle — intranet is in-world only

> **Every intranet page is an in-world artefact.** Each page is something a real YAT staff member could plausibly land on while doing their job. Meta-scaffolding for the student / learner ("you are a consultant arriving at YAT…", "this assessment task asks you to…") lives in the assessment-brief documents (the AT `.docx` files), not on the intranet.

When in doubt about a piece of content, the test is: *would a YAT staff member ever read this?* If no, it's meta — and belongs in the AT brief, not the intranet.

### 2.2 Public site sitemap

Locked structure as of 2026-05-26. Stub pages flagged below are TBD content (one-paragraph placeholders sufficient for site-realism — full content not assessment-critical).

```
yat.timbaird.com/                                 [warm cream background, marketing tone]

├── /                                             Homepage — hero, study-areas teaser, why YAT, apply CTA
│                                                 ↳ content TBD
│
├── /study/                                       Study areas catalogue
│   ├── /study/                                   Index — all study areas (one-para each)
│   ├── /study/business                              ↳ stub TBD
│   ├── /study/community-services                    ↳ stub TBD
│   ├── /study/education                              ↳ stub TBD
│   ├── /study/information-technology                ↳ stub TBD (features the diploma this site supports)
│   │   └── /study/information-technology/
│   │         diploma-cloud-cyber-security        Course detail — light page TBD
│   ├── /study/health                                ↳ stub TBD
│   ├── /study/hospitality                           ↳ stub TBD
│   └── /study/trades                                ↳ stub TBD
│
├── /about/                                       About hub
│   ├── /about/                                   ← public-about-mission-vision.md
│   ├── /about/strategic-plan                     ← public-strategic-plan-summary.md
│   └── /about/people                             ← public-org-structure.md
│
├── /locations                                    ← public-locations-campus.md
│
├── /apply                                        How to enrol — process, intakes, fees
│                                                 ↳ content TBD
│
├── /contact                                      Contact — address, phone, form (submit does nothing)
│                                                 ↳ content TBD
│
└── /sign-in                                      Mock SSO gate (per §3) → redirects to /intranet/
```

### 2.3 Intranet sitemap

Top-level sections and the policy / reference files listed below are locked as of 2026-05-26. The interior of `/intranet/ict/`, `/intranet/projects/`, and `/intranet/templates/` is worked through document-by-document as content is authored. The structure shown for `/intranet/projects/lms-cloud-migration/` is the *current proposal* for the in-flight cluster, refined as files get reframed (engagement agreement, ICT cost baseline).

```
yat.timbaird.com/intranet/                        [neutral light-grey background, denser layout]

├── /intranet/                                    Intranet home — welcome, featured project banner, quick links
│                                                 ↳ content TBD
│
├── /intranet/ict/                                ICT department
│                                                 ↳ children worked through doc-by-doc;
│                                                   proposed state-bearing pages: environment, network-diagram,
│                                                   lms-server-status, hardware-inventory, backup-recovery
│
├── /intranet/policies/                           Policies & procedures (locked, all stable)
│   ├── /intranet/policies/change-management      ← internal-change-management-procedure.md
│   ├── /intranet/policies/user-access            ← internal-user-access-policy.md
│   ├── /intranet/policies/acceptable-use         ← internal-acceptable-use-policy.md
│   ├── /intranet/policies/whs                    ← internal-whs-policy.md
│   ├── /intranet/policies/privacy                ← internal-privacy-policy.md
│   ├── /intranet/policies/backup-retention       ← internal-backup-retention-policy.md
│   ├── /intranet/policies/security-incident      ← internal-security-and-incident-response.md
│   └── /intranet/policies/records-management     ← internal-records-management-policy.md
│
├── /intranet/projects/                           Projects — current + mock past
│                                                 ↳ per-project structure worked through doc-by-doc;
│                                                   current LMS-migration project's structure proposed below
│   │
│   └── /intranet/projects/lms-cloud-migration/   Current project — LMS cloud migration
│       ├── /intranet/projects/lms-cloud-migration/                        Project home — overview + artefact index
│       ├── /intranet/projects/lms-cloud-migration/master-services-agreement   ← NEW — reframed from public-cluster-project-narrative.md
│       ├── /intranet/projects/lms-cloud-migration/strategic-plan          ← internal-ict-strategic-plan-detail.md
│       ├── /intranet/projects/lms-cloud-migration/role-brief/                                state-bearing
│       │   └── /role-brief/s1-cl1-at1            ← internal-lms-migration-role-brief-S1-CL1-AT1.md
│       ├── /intranet/projects/lms-cloud-migration/lms-app-spec/                              state-bearing
│       │   └── /lms-app-spec/s1-cl1-at1          ← internal-lms-application-spec-S1-CL1-AT1.md
│       ├── /intranet/projects/lms-cloud-migration/migration-requirements/                    state-bearing
│       │   └── /migration-requirements/s1-cl1-at1                                            ← internal-lms-cloud-migration-requirements-S1-CL1-AT1.md
│       ├── /intranet/projects/lms-cloud-migration/ha-database-requirements/                  state-bearing
│       │   └── /ha-database-requirements/s1-cl1-at3                                          ← internal-ha-database-requirements-S1-CL1-AT3.md
│       ├── /intranet/projects/lms-cloud-migration/consultation-notes/                        state-bearing
│       │   └── /consultation-notes/s1-cl1-at1    ← internal-ict-manager-consultation-notes-S1-CL1-AT1.md
│       ├── /intranet/projects/lms-cloud-migration/ict-cost-baseline/                         state-bearing  [REFRAMED from CBA cost inputs]
│       │   └── /ict-cost-baseline/s1-cl1-at1     ← internal-cba-cost-inputs-S1-CL1-AT1.md (rename TBD)
│       └── /intranet/projects/lms-cloud-migration/cloud-architecture-design/                 state-bearing
│           └── /cloud-architecture-design/s1-cl1-at2                                         ← internal-lms-cloud-architecture-design-S1-CL1-AT2.md
│
├── /intranet/reference/                          Reference & standards (locked, all stable)
│   ├── /intranet/reference/industry-standards    ← internal-industry-standards-reference.md
│   ├── /intranet/reference/legislative           ← internal-legislative-requirements-reference.md
│   └── /intranet/reference/reference-architectures ← internal-reference-architectures.md
│
└── /intranet/templates/                          Document templates (downloadable .docx / .pptx)
                                                  ↳ children worked through doc-by-doc; current templates folder:
                                                    business-case, business-case-presentation, feedback-record,
                                                    deployment-report [state-bearing], ha-design [state-bearing],
                                                    ha-deployment-report [state-bearing]
```

### 2.4 Extensibility — adding sections cheaply

The intranet structure is designed so adding a new top-level section (or a new project under `/intranet/projects/`) costs minimal effort. Six patterns the build pipeline will follow:

1. **Section registry as config, not code.** A single small config file lists the intranet sections (`ict`, `policies`, `projects`, `reference`, `templates`) with display name, short description, ordering, and any per-section flags. Navigation components read from this list — adding a new section = one entry in the registry + one content folder; nav, breadcrumbs, sitemap-builders all update automatically.
2. **One section-landing template.** Every section index (`/intranet/ict/`, `/intranet/policies/`, …) renders from the same template: section heading + intro paragraph + listing of pages in the section grouped by topic. New section's landing page = zero new template code.
3. **SSG content collections per section.** Drop a markdown file into a section folder, the build picks it up automatically. New policy = drop the file in `/intranet/policies/`; new project = create `/intranet/projects/{slug}/` and drop files in. No manual route registration.
4. **Site chrome decoupled from section structure.** Disclosure banner, header, footer, breadcrumbs read from the registry — none hard-code section names. Adding / renaming a section doesn't touch global layout code.
5. **State-versioning is a page-level concern, not a section concern.** Any page in any section can be state-bearing or stable, signalled by filename suffix per §4.1. No section needs special-case handling to support versioned pages.
6. **Documented URL convention.** Public uses `/{section}/{page}`. Intranet uses `/intranet/{section}/{topic}` (stable pages) or `/intranet/{section}/{topic}/{version}` (state-bearing pages) per §4. New sections follow the same pattern — no per-section URL invention.

URL paths above are illustrative in detail (slug spellings, sub-page nesting) but follow this stable convention.

## 3. Mock SSO sign-in gate

The boundary between the public site and the intranet is a fake SSO sign-in page. The page exists purely for narrative realism — it has no auth backend and authenticates no one.

### 3.1 Visual / branding spec

- Page styled to resemble a familiar corporate SSO experience the student would expect at a real RTO (e.g. Microsoft Entra ID / Okta look-and-feel).
- YAT branding visible: YAT College logo, "Sign in to YAT College Intranet" heading.
- Email / username field with placeholder text (e.g. "you@yat.timbaird.com").
- Password field with placeholder text.
- Primary "Sign in" button.
- Optional secondary link styled as "Forgot password?" (non-functional — clicking either does nothing or shows a benign message).

### 3.2 Behaviour spec

- The sign-in button performs no authentication. Clicking it (with any input, no input, or any combination) redirects the browser to the intranet home page.
- Form fields do not validate. No client- or server-side data store touches the inputs.
- The "Forgot password?" link, if present, either does nothing or shows a static notice ("Contact your YAT ICT Service Desk to reset your password" — pure scenario flavour).

### 3.3 Copy

- Page heading: **Sign in to YAT College Intranet**
- Field 1 label: **Username or email**
- Field 2 label: **Password**
- Button text: **Sign in**
- Footer notice (recommended, small grey text): *"This is a simulated environment for educational use only. Do not enter real credentials."*

### 3.4 Implementation notes for the site builder

- No backend, no database, no auth library.
- Page is a single static HTML form whose submit action is a redirect (or whose submit handler is `window.location = "/intranet"`).
- Credentials, if any are typed, are not transmitted, logged, or stored.
- If the SSG used supports it, the form should disable browser autocomplete (`autocomplete="off"` on the fields) to discourage accidental password-manager storage.

## 4. State-versioned pages

Some intranet pages carry a state that evolves across the course. The current ICT environment, for example, is on-prem in S1-CL1, partially migrated by S1-CL2, fully migrated by S1-CL3.

### 4.1 How state is expressed

- Source filename suffix encodes the AT the version was authored for: `internal-ict-environment-overview-S1-CL1-AT1.md`.
- The "Relevant to:" header at the top of each markdown source file tells the reader which ATs the version applies to (`S1-CL1 AT1, AT2, AT3`).
- Each version is rendered as its own URL (one page per source file). There is **no global state machine** — the site does not ask students which assessment they are on, store that choice, or swap content based on it.

### 4.2 Surfacing versions to students — two complementary mechanisms

**(a) Versioned-document index on the linking page.** Wherever a state-bearing document is referenced from an intranet topic / index page, the link block lists every available version with the assessment range it applies to. Example markup:

```
ICT Environment Overview

The version to read depends on which assessment you are doing. Select the one that matches your current cluster + AT.

  S1-CL1 AT1 through S1-CL1 AT3  →  [link]
  S1-CL2 AT1                     →  [link]
  S1-CL3 AT1 and onward          →  [link]
```

**(b) "Other versions" breadcrumb at the top of each version page.** A small passive note (not an interactive selector) tells the student which version they are looking at and points at sibling URLs. Example:

```
You are viewing the S1-CL1-AT1 version.
Other versions: S1-CL2-AT1 · S1-CL3-AT1
```

Purpose: students who arrive via a direct link, search result, or browser history still know which version they have and can pivot to a sibling without going back to the index page.

### 4.3 Why this approach

The index-listing + passive-breadcrumb model (no global state machine):

- **exposes YAT's evolution** as part of the learning — students can see how the environment changed at each cluster boundary;
- avoids state-storage edge cases (localStorage / cookies / URL params), multi-tab inconsistency, and direct-link breakage;
- costs nothing beyond ordinary markdown links and a tiny breadcrumb snippet;
- needs no special handling for single-version pages — the index lists one link and the breadcrumb says "current version".

### 4.4 Initial scope

For this cluster (S1-CL1) only the AT1-suffixed versions exist. Later clusters will add their own snapshots; each addition is a new file at a new URL, a new line on the relevant index page, and a new entry in the "other versions" breadcrumb on existing version pages.

## 5. Stable pages

Pages without an AT suffix on the source file are stable across all clusters. They have a single URL, no state-selector menu, and no version history.

The current stable set includes the public-facing pages (mission, vision, strategic plan summary, locations, org structure) and the cross-cluster intranet content (the change management procedure, the policy suite, the reference lists, the YAT ICT strategic plan detail).

If a stable document later needs versioning (e.g. the org structure when YAT expands to multiple campuses per its strategic plan), it can be promoted to a state-bearing page by re-publishing the new version with an AT-suffix filename and leaving the existing version as the earliest snapshot.

## 6. Navigation and discoverability

- **Public homepage:** a marketing-style RTO homepage (hero, study-areas teaser, why YAT, apply CTA) with a prominent "Sign in" link top-right routing to the SSO gate (§3).
- **Public global nav:** Study · About · Locations · Apply · Contact · Sign in.
- **Intranet home:** welcome + featured-project banner + section nav matching the five top-level intranet sections in §2.3 (ICT, Policies, Projects, Reference, Templates).
- **Intranet global nav:** ICT · Policies · Projects · Reference · Templates, plus breadcrumbs on every interior page.
- **Cross-references:** in-text links between scenario markdown files (`internal-change-management-procedure.md` etc.) are preserved as in-page hyperlinks in the rendered site.
- **Version surfacing on state-bearing content:** index pages list each version with its assessment range; each version page carries a small "other versions" breadcrumb (see §4.2). No global state machine.
- **Site-wide simulated-environment disclosure banner:** thin ochre strip across the very top of every page on both zones and the sign-in gate, per `scenario/branding/brand-pack.md` §5.3.

## 7. Hosting and build

- **Hosting (TBD):** Cloudflare Pages (per Tim's earlier suggestion) or similar free static-site hosting. Alternative candidates: GitHub Pages, Netlify, Vercel, an internal-Kangan-hosted equivalent.
- **Build pipeline:** **Astro** (locked 2026-05-26). Component-based SSG, handles the dual public/intranet layout + the SSO page well, native content collections for markdown source files with frontmatter validation, idiomatic support for the state-versioned URL scheme.
- **Version surfacing implementation:** the build process needs to detect AT-suffixed source files, group them by topic, render each as its own URL, and (a) feed the grouped list into the linking index page and (b) inject the "other versions" breadcrumb at the top of each version page (see §4.2). No global state, no client-side JS required for this.
- **Domain:** `yat.timbaird.com` (deployed) — a personal domain hosting the fictional YAT College; not a real organisation's own domain.

## 8. What's not in scope for the website

- No real authentication, no user accounts, no session management.
- No analytics tracking of student behaviour.
- No forms that submit data anywhere.
- No external API integrations.
- No content management system — content is authored as markdown in the source tree, version-controlled in the repo, and built into the site by the pipeline.

## 9. Open items

### 9.1 Design questions (TBD)

1. Hosting platform (Cloudflare Pages vs alternatives).
2. Domain.
3. Visual theme — full custom design vs adapting an Astro starter template (e.g. Starlight for docs-style intranet content). Brand pack at `scenario/branding/brand-pack.md` provides direction; CSS / theme implementation still to design.
4. SSO page styling — match a specific real-world SSO (Entra / Okta) closely, or generic-looking.
5. Cross-repo content sourcing — scenario `.md` files live in `diploma-cloud-cyber/scenario/`; the Astro site repo (`diploma-cloud-cyber-website`) needs them at build time. Options: git submodule, CI sync step, or local-dev path-mapping + CI copy.

### 9.2 Pending content

1. **Public-site stub pages.** `/`, `/study/*`, `/apply`, `/contact` content listed as TBD in §2.2.
2. **Intranet home + project landing page content.** `/intranet/` and the project landing pages.
