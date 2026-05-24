# YAT Scenario — Mock Website Specification

**Document type:** Meta — specification for the delivery vehicle, not scenario content. Reader audience is the team building the mock website, not students.

**UoC references this document satisfies:** None directly — this is the spec for *how* the scenario content (which does satisfy UoC ACs) is delivered to students.

**Status:** DRAFT (Claude v1, 2026-05-23). All implementation choices below are **TBD** pending Tim's confirmation.

---

## 1. Intent

The mock website is the delivery vehicle for the cluster scenario materials. Rather than handing students a bundle of separate documents, the scenario content is published as a website that students browse like a real corporate site + intranet during their cluster assessments. This reduces incongruence between the consultant-engagement narrative and the way reference materials are consumed: students "log in" to YAT's intranet, navigate by area, and read the materials in context — much as they would on a real engagement.

The intent is **realism + navigability**, not technical fidelity. The website is read-only, has no authentication backend, and stores no user data.

## 2. Site structure

```
yat-college.example/                            ← public-facing site
├── /                                           ← homepage (cluster project narrative front page)
├── /about                                      ← public-about-mission-vision.md
├── /strategic-plan                             ← public-strategic-plan-summary.md
├── /people                                     ← public-org-structure.md
├── /locations                                  ← public-locations-campus.md
└── /sign-in                                    ← mock SSO sign-in gate (see §3)
                                                  ↓
yat-college.example/intranet/                   ← intranet (post-"sign-in")
├── /                                           ← intranet home (nav to sections below)
├── /ict/environment              ← state-selector menu → S1-CL1-AT1, etc.
├── /ict/network-diagram          ← state-selector menu
├── /ict/lms-server-status        ← state-selector menu
├── /ict/hardware-inventory       ← state-selector menu
├── /ict/backup-recovery          ← state-selector menu
├── /policies/change-management
├── /policies/user-access
├── /policies/acceptable-use
├── /policies/whs
├── /policies/privacy
├── /policies/backup-retention
├── /policies/security-incident-response
├── /project/strategic-plan       ← internal-ict-strategic-plan-detail.md
├── /project/role-brief           ← AT-specific
├── /project/lms-app-spec         ← state-selector menu
├── /project/migration-requirements
├── /project/ha-database-requirements
├── /project/consultation-notes
├── /project/cba-cost-data
├── /reference/industry-standards
├── /reference/legislative-requirements
├── /reference/reference-architectures
└── /templates/                                ← downloadable templates (xlsx, docx) — see `assessments/templates/checklist.md`
```

URL paths above are illustrative — the build pipeline can choose the actual structure.

## 3. Mock SSO sign-in gate

The boundary between the public site and the intranet is a fake SSO sign-in page. The page exists purely for narrative realism — it has no auth backend and authenticates no one.

### 3.1 Visual / branding spec

- Page styled to resemble a familiar corporate SSO experience the student would expect at a real RTO (e.g. Microsoft Entra ID / Okta look-and-feel).
- YAT branding visible: YAT College logo, "Sign in to YAT College Intranet" heading.
- Email / username field with placeholder text (e.g. "you@yat-college.example").
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
- The build process collects all versions of a given page into a single URL with a **state-selector menu**.

### 4.2 State-selector menu

At the top of every state-bearing page, the rendered HTML shows a menu listing all available versions of that page, with the current version highlighted. Example:

```
ICT Environment Overview — viewing state: [ S1-CL1 AT1, AT2, AT3 ✓ ] [ S1-CL2 AT1 ] [ S1-CL3 AT1 ] ...
```

Clicking a different state link navigates to the equivalent page for that AT. Students working on (say) S1-CL2 AT1 read the YAT environment as it is at that point; the URL path makes this obvious; the menu lets them flip back to see earlier states if they want to understand how YAT got here.

### 4.3 Initial scope

For this cluster (S1-CL1) only the AT1-suffixed versions exist. Later clusters will add their own snapshots. The state-selector should still render even when only one version exists (highlighted, no other options) — this keeps the UI consistent.

## 5. Stable pages

Pages without an AT suffix on the source file are stable across all clusters. They have a single URL, no state-selector menu, and no version history.

The current stable set includes the public-facing pages (mission, vision, strategic plan summary, locations, org structure) and the cross-cluster intranet content (the change management procedure, the policy suite, the reference lists, the YAT ICT strategic plan detail).

If a stable document later needs versioning (e.g. the org structure when YAT expands to multiple campuses per its strategic plan), it can be promoted to a state-bearing page by re-publishing the new version with an AT-suffix filename and leaving the existing version as the earliest snapshot.

## 6. Navigation and discoverability

- **Public homepage:** the cluster project narrative front page, with a clear path to the "sign in to intranet" gate.
- **Intranet home:** sectioned navigation matching the structure in §2 (ICT environment, Policies, Project materials, References).
- **Cross-references:** in-text links between scenario markdown files (`internal-change-management-procedure.md` etc.) are preserved as in-page hyperlinks in the rendered site.
- **State indicator on every state-bearing page:** so students always know which version of YAT they're looking at.

## 7. Hosting and build

- **Hosting (TBD):** Cloudflare Pages (per Tim's earlier suggestion) or similar free static-site hosting. Alternative candidates: GitHub Pages, Netlify, Vercel, an internal-Kangan-hosted equivalent.
- **Build pipeline (TBD):** a static site generator that takes the markdown source files in `scenario/` and produces the rendered HTML site. Plausible options:
  - **MkDocs / MkDocs Material** — markdown-native, generates clean documentation-style sites; supports search out of the box.
  - **Hugo** — fast, flexible, more theming work.
  - **Eleventy** — minimal, very flexible templating.
  - **Astro** — modern, component-based, good for the SSO page styling.
- **State-selector implementation:** the build process needs to detect AT-suffixed source files, group them by topic, and inject the state-selector menu at the top of each rendered page.
- **Domain (TBD):** something clearly fictional (e.g. `yat-college.example`, `yatcollege.test`) — must not be a real organisation's domain.

## 8. What's not in scope for the website

- No real authentication, no user accounts, no session management.
- No analytics tracking of student behaviour.
- No forms that submit data anywhere.
- No external API integrations.
- No content management system — content is authored as markdown in the source tree, version-controlled in the repo, and built into the site by the pipeline.

## 9. Open questions (TBD)

1. SSG choice (MkDocs / Hugo / Eleventy / Astro / other).
2. Hosting platform (Cloudflare Pages vs alternatives).
3. Domain.
4. Visual theme — full custom design vs adapting an SSG default theme.
5. SSO page styling — match a specific real-world SSO (Entra/Okta) closely, or generic-looking.
6. Whether the state-selector should be a horizontal bar, a dropdown, or a sidebar widget.
7. Whether the public homepage and intranet share visual identity, or whether the intranet has a distinctly "internal" look.

---

## Changelog

- **2026-05-23:** Initial spec. Absorbed the previously-stubbed `public-mock-sso-signin.md` (which is removed) into §3 here.
