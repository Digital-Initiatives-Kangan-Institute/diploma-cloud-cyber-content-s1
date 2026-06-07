# S1-CL2 Cloud Disaster Recovery — Consolidated UoC

> **STATUS: DRAFT.** Every assessable item (PC / FS / PE / KE / AC) from the three cluster units, quoted **verbatim** from the validated UoC transcriptions and tagged `[UNIT SECTION numbering]`. Items are organised under a **topic** structure (Tim's direction, 2026-06-06), with the finer groupings as **sub-topics**. **The group-level *assessment ideas* are proposals — marked TBD per CLAUDE.md Rule 1.** The topic taxonomy, the two-AT division, and AT1's three-part shape (Part A Solution Design / Part B DR Plan / Part C presentation) are per Tim's direction; see the assessment plan (`assessments/assessment_plan.md`) for the full structure and coverage map.

**Cluster units**

| Unit | Title | Primary contribution |
|---|---|---|
| ICTCLD501 | Develop cloud disaster recovery plans | DR planning — risk/impact analysis, RTO/RPO, DR plan, test & sign-off |
| ICTCLD503 | Implement web-scale cloud infrastructure | Scalable web architecture, microservices, serverless implementation |
| ICTCLD505 | Implement cloud infrastructure with code | Infrastructure as Code — templates, deploy/update/delete, parameterisation |

**Item inventory (expected by the Step 2 validator)**

| Unit | PC | FS | PE | KE | AC | Total |
|---|---|---|---|---|---|---|
| ICTCLD501 | 19 | 5 | 3 | 6 | 4 | 37 |
| ICTCLD503 | 18 | 4 | 5 | 6 | 10 | 43 |
| ICTCLD505 | 19 | 5 | 4 | 11 | 9 | 48 |
| **Total** | **56** | **14** | **12** | **23** | **23** | **128** |

**Reference-tag format.** `[<UNIT> <SECTION> <numbering>]` — e.g. `[ICTCLD501 PC 1.1]`, `[ICTCLD503 FS Reading]`, `[ICTCLD505 PE 2]`, `[ICTCLD501 KE 4]`, `[ICTCLD503 AC 10]`. PCs keep their source numbering and prefix; FS uses the verbatim skill name; PE/KE/AC are numbered `1..N` in source order. (Example tags in this preamble are backtick-wrapped so the validator does not count them.)

**Verbatim discipline.** Every quoted item is copied directly from the source `.md` (validated EXACT MATCH against the `.docx` on 2026-06-06). KE items with nested sub-bullets are quoted as one item (parent + children) under the parent's tag.

---

## Topic & assessment structure

The cluster organises into **four delivery topics**, each with sub-topics (the groups below). The same topics structure both the teaching/exercises and the assessment.

| Topic | Sub-topic groups | Units | Assessment |
|---|---|---|---|
| **1. Architecture & Planning** | G1, G2 (DR), G3 (web-scale design), G4a (microservice design) | 501, 503 | **AT1** |
| **2. Implementation** | G4b (microservice build), G5, G6 (IaC), G7 (shared foundations — underpin building) | 503, 505 | **AT2** |
| **3. Monitoring** | G8 (metrics, alarms, alerts) | 501, 503 | **AT2** |
| **4. Documenting** | G9 (technical writing), G10 (feedback, sign-off, lodgement) | 501, 503, 505 | **AT1 + AT2** (split) |

**Assessment deliverables (per Tim's direction — modelled on the S1-CL1 pattern):**

- **AT1 — Cloud Expansion: Design & DR Plan** *(modelled on CL1 AT1 Business Case)* — three parts:
  - **Part A — Solution Design** — the web-scale architecture for the global user base **and the microservice** (the audit-log service), documented & justified (`[ICTCLD503 PC 1.7]` / `[ICTCLD503 PC 2.4]`). Data residency is an **input constraint** that shapes this design — it is *why* the microservice exists and where the edge/log-slice sits — not a separate deliverable.
  - **Part B — DR Plan** — the disaster recovery plan for the system designed in Part A: requirements & impact analysis, RTO/RPO, recovery solutions and the finalised plan (ICTCLD501 elements 1–4). **Pure DR** — "what we do if the system goes down"; no microservice or regulatory content.
  - **Part C — presentation of Part A + Part B for approval** — the required verbal walkthrough (`[ICTCLD501 PC 5.1]`), seeking/responding to feedback (`[ICTCLD501 PC 5.2]`), lodgement (`[ICTCLD501 PC 5.3]`) and obtaining sign-off (`[ICTCLD501 PC 5.4]`); evidences FS Oral communication. This is the **design-approval gate** — approval before implementing.
- **AT2 — Cloud Microservice & IaC Implementation** *(modelled on CL1 AT2 Deployment Report)* — single part:
  - **A written Deployment Report** submitted for finalisation/approval of the implemented infrastructure — operating a provided data-store template (ICTCLD505 elements 1–2) and authoring + deploying the microservice from the provided code (ICTCLD505 element 3 + ICTCLD503 element 3), the monitoring (Topic 3), the **IaC user documentation** (`[ICTCLD505 PC 4.1]`, `[ICTCLD505 PE 4]`), and the **build sign-off** (`[ICTCLD503 PC 4.2]` / `[ICTCLD503 PC 4.3]`, `[ICTCLD505 PC 4.2]`). The provided artefacts (the data-store template, the microservice code, the webhook contract) are supplied as appendices to the assessment document.

**Two approval moments (by design, and UoC-faithful):**
- **End of AT1 — design approval:** the Solution Design (Part A) + DR Plan (Part B) approved at the Part C presentation, before any build. Carries ICTCLD501's element-5 closure.
- **End of AT2 — build sign-off:** the implemented, monitored infrastructure signed off via the Deployment Report. Carries ICTCLD503/505's element-4 closure.

**Documenting resolves cleanly into the ATs:**

| Documenting item | Lands in | As |
|---|---|---|
| `[ICTCLD503 PC 1.7]`, `[ICTCLD503 PC 2.4]` + FS Writing (503) | AT1 Part A | the Solution Design — architecture documented & justified |
| `[ICTCLD501 PC 5.1–5.4]` + FS Oral communication (501) | AT1 Part C | design-approval presentation + feedback + lodgement + sign-off (of Part A + Part B) |
| `[ICTCLD505 PC 4.1]`, `[ICTCLD505 PE 4]` + FS Writing (505) | AT2 | Deployment Report — IaC user documentation |
| `[ICTCLD503 PC 4.2]`/`4.3`, `[ICTCLD505 PC 4.2]` + FS Oral communication (505) | AT2 | Deployment Report — build feedback + final sign-off |

**Scenario is *not* a topic.** The scenario is the YAT website / narrative / intranet documents that support the assessments *and* the delivery exercises (the inputs students work from). It supplies the materials and the assessment environment — it is not a body of competency to assess.

**Cross-cutting & delivery environment.** Groups 11–13 are not a topic either: the generic foundation skills (G11) are co-evidenced inside both ATs' deliverables; the environment/resource access conditions (G12) are provided by the scenario website + AWS Academy labs; the assessor-requirement condition (G13) is institutional.

---

# Topic 1 — Architecture & Planning → AT1

Design and plan before building: the cloud DR plan (501) and the web-scale + microservice **designs** (503). The AT1 deliverables originate here.

## Group 1 — Cloud DR: requirements & impact analysis

**Units:** ICTCLD501

**Why grouped:** the opening half of the DR-plan lifecycle — establishing plan requirements against business needs, then conducting the risk/impact analysis (RTO/RPO, data volume/sensitivity, severity) the solutions are built on. One impact-analysis work product plausibly evidences all of these.

**Assessment idea (TBD):** a DR requirements + impact-analysis deliverable (risk register + RTO/RPO determination + impact assessment) for the scenario, feeding the DR plan in Group 2.

- 1.1 Identify disaster recovery plan requirements according to business needs and requirements [ICTCLD501 PC 1.1]
- 1.2 Determine existing organisational recovery plans [ICTCLD501 PC 1.2]
- 1.3 Identify vendor disaster recovery plan and service level agreements [ICTCLD501 PC 1.3]
- 2.1 Determine time and recovery point objectives according to business needs [ICTCLD501 PC 2.1]
- 2.2 Assess potential risks plan exclusions according to business requirements [ICTCLD501 PC 2.2]
- 2.3 Estimate amount of data and security level of data managed [ICTCLD501 PC 2.3]
- 2.4 Evaluate severity of impact and disruption of risk events [ICTCLD501 PC 2.4]
- 2.5 Document outcomes of impact analysis according to organisational policies and procedures [ICTCLD501 PC 2.5]
- determine likelihood and impact of risk event to assist in the development of one cloud disaster recovery plan [ICTCLD501 PE 2]
- risk environments in cloud/ICT environment [ICTCLD501 KE 1]
- data analysis methodologies to determine risk environment [ICTCLD501 KE 2]
- Recovery Time Objective (RTO) and Recovery Point Objective (RPO) standards and techniques [ICTCLD501 KE 5]
- **Planning and organising** — Uses a broad range of strategies to evaluate and resolve risk events in cloud and technical environment and demonstrates the knowledge that design choices will influence the security of virtually stored information [ICTCLD501 FS Planning and organising]

## Group 2 — Cloud DR: solutions & plan finalisation

**Units:** ICTCLD501

**Why grouped:** the back half of the DR-plan lifecycle — developing and prioritising DR solutions, then assembling and documenting the finalised DR plan that reaches the RTO/RPO targets. One DR plan deliverable evidences all members.

**Assessment idea (TBD):** the cloud DR plan deliverable (≥3 major risk events, solution options, prioritisation, plan steps/timelines, RTO/RPO alignment), built on the Group 1 analysis.

- 3.1 Develop range of disaster recovery solutions according to business requirements [ICTCLD501 PC 3.1]
- 3.2 Determine vendor protections and prioritise risks [ICTCLD501 PC 3.2]
- 3.3 Assess external insurance protection levels and their suitability requirements [ICTCLD501 PC 3.3]
- 3.4 Identify other disaster recovery solution components [ICTCLD501 PC 3.4]
- 4.1 Align disaster recovery risk potential according to business requirements [ICTCLD501 PC 4.1]
- 4.2 Outline steps of disaster recovery plan including timelines, key features, service providers and any other aspect [ICTCLD501 PC 4.2]
- 4.3 Document disaster recovery plan according to business needs and requirements [ICTCLD501 PC 4.3]
- develop and evaluate a cloud disaster recovery plan that includes at least three major risk events. [ICTCLD501 PE 1]
- document disaster recovery plan and ways the plan reaches Recovery Time Objective (RTO) and Recovery Point Objective (RPO) targets. [ICTCLD501 PE 3]
- disaster recovery techniques applicable to cloud environments [ICTCLD501 KE 3]
- ISO270001, ISO27002 and ISO 27031 standards [ICTCLD501 KE 4]

## Group 3 — Web-scale architecture design

**Units:** ICTCLD503

**Why grouped:** designing the scalable web-application architecture — confirming scaling needs, reviewing and re-designing to scale network/compute/storage and for a global user base while maintaining availability and security. One web-scale architecture design deliverable evidences these.

**Assessment idea (TBD):** a scalable web-application architecture design (the scenario's web workload) demonstrating elastic scaling of network, compute and storage, with availability/security maintained.

- 1.1 Determine and confirm cloud web-scaling needs [ICTCLD503 PC 1.1]
- 1.2 Review architecture for web application according to business needs [ICTCLD503 PC 1.2]
- 1.3 Identify cloud services required to scale web application [ICTCLD503 PC 1.3]
- 1.4 Design architecture changes using cloud services and check design scales network, compute and storage as utilisation increases [ICTCLD503 PC 1.4]
- 1.5 Determine architecture changes to scale for a global user base [ICTCLD503 PC 1.5]
- 1.6 Check availability and security of application is maintained with design changes and review design as required [ICTCLD503 PC 1.6]
- design at least one architecture that will scale networking, compute and storage for a multi-tier web application [ICTCLD503 PE 1]
- apply web-scaling principles and technologies. [ICTCLD503 PE 5]
- functions, benefits and differences of web-scale cloud components, including: [ICTCLD503 KE 3]
  - structured query language (SQL) and NoSQL databases
  - monolithic and microservice architectures
  - virtual, container and serverless compute models
  - content delivery networks and in-memory data stores
- web-scaling principles and technologies. [ICTCLD503 KE 6]

## Group 4a — Microservices & serverless: design

**Units:** ICTCLD503

**Why grouped:** the *design* half of the microservice strand — identifying microservices and data transactions, selecting supporting cloud services, and designing the microservice architecture. Sits in Architecture & Planning (the build is Group 4b).

**Assessment idea (TBD):** a microservice architecture design for a simple application — services, data transactions, and the cloud services chosen to support them.

- 2.1 Identify microservices and data transactions required to meet business needs [ICTCLD503 PC 2.1]
- 2.2 Determine cloud services to support microservice architecture [ICTCLD503 PC 2.2]
- 2.3 Design microservice architecture using cloud services [ICTCLD503 PC 2.3]
- design at least one microservice architecture for implementing a simple web application [ICTCLD503 PE 2]
- definitions, functions, features and uses of web-scale cloud infrastructure, including: [ICTCLD503 KE 4]
  - highly cohesive and loosely coupled systems
  - database and storage services for persistent data storage
  - application program interface (API), messaging and queuing services

---

# Topic 2 — Implementation → AT2

Build it: implement and deploy the microservice (503), and provision cloud infrastructure as code (505). The shared cloud foundations underpin the building.

## Group 4b — Microservices & serverless: implementation

**Units:** ICTCLD503

**Why grouped:** the *implementation* half of the microservice strand — reviewing the design and code components, deploying and configuring the serverless services, testing the application, and troubleshooting. One microservice deploy work product evidences these.

**Assessment idea (TBD):** deploy the Group 4a microservice design on serverless cloud services, with functional testing and troubleshooting evidence.

- 3.1 Review microservice design and code components for application [ICTCLD503 PC 3.1]
- 3.2 Deploy and configure cloud services to implement the application [ICTCLD503 PC 3.2]
- 3.3 Test microservice components and confirm that the application is functioning [ICTCLD503 PC 3.3]
- 3.4 Troubleshooting and fix errors as required [ICTCLD503 PC 3.4]
- deploy a microservice application utilising cloud serverless technologies. [ICTCLD503 PE 3]
- use cloud management consoles, software development kits or command line tools [ICTCLD503 PE 4]
- testing and debugging techniques [ICTCLD503 KE 5]

## Group 5 — Infrastructure as Code: deploy & manage with templates

**Units:** ICTCLD505

**Why grouped:** the prepare-and-deploy half of IaC — understanding the benefits and selecting a service, then using predefined templates to deploy, configure, update, delete and troubleshoot cloud resources. One "operate provided IaC templates" work product evidences these.

**Assessment idea (TBD):** a hands-on lab where students deploy/configure/update/remove cloud resources from predefined IaC templates (e.g. CloudFormation) and troubleshoot template errors.

- 1.1 Identify and review benefits of infrastructure as code according to business needs [ICTCLD505 PC 1.1]
- 1.2 Determine ways automation leverages cloud platforms according to business needs [ICTCLD505 PC 1.2]
- 1.3 Determine and assess potential issues and errors when implementing infrastructure as code [ICTCLD505 PC 1.3]
- 1.4 Evaluate and select infrastructure as code service compatible with selected cloud platform and business requirements [ICTCLD505 PC 1.4]
- 2.1 Learn template syntax of selected cloud infrastructure as code service [ICTCLD505 PC 2.1]
- 2.2 Review pre-defined templates and determine what resources they create and any dependencies [ICTCLD505 PC 2.2]
- 2.3 Utilise the cloud infrastructure as code service tools to deploy, update and delete resources using predefined templates as required [ICTCLD505 PC 2.3]
- 2.4 Confirm deployments of cloud resources and configure resources using cloud platform console or command line tools [ICTCLD505 PC 2.4]
- 2.5 Remove deployed resources using cloud infrastructure as code tools and delete templates as required [ICTCLD505 PC 2.5]
- 2.6 Test and troubleshoot template errors as required [ICTCLD505 PC 2.6]
- deploy, update and remove cloud infrastructure using cloud platform templates [ICTCLD505 PE 1]
- use cloud management console, cloud software development kits or command line tools [ICTCLD505 PE 3]
- benefits of deploying infrastructure as code compared to manual provisioning in a console [ICTCLD505 KE 3]
- different infrastructure as code services that can be used on a cloud platform [ICTCLD505 KE 4]
- syntax of selected infrastructure as code service templates [ICTCLD505 KE 5]
- tooling required to execute cloud infrastructure templates [ICTCLD505 KE 6]
- testing and debugging techniques, including common issues and errors relating to deploying cloud infrastructure as code [ICTCLD505 KE 7]
- uses and methods to create, manage, provision and update cloud resources and templates [ICTCLD505 KE 10]
- techniques, methods and industry standard metrics used to leverage cloud platform capabilities and deploy and manage templates. [ICTCLD505 KE 11]

## Group 6 — Infrastructure as Code: author & parameterise own templates

**Units:** ICTCLD505

**Why grouped:** the author-your-own half of IaC — writing a template from scratch to provision related resources, updating/redeploying it, and parameterising it for configuration and code reuse. One student-authored template evidences these.

**Assessment idea (TBD):** students author their own IaC template to provision a related set of resources, then update/redeploy and parameterise it for reuse — the "create at least one own template" performance evidence.

- 3.1 Learn template syntax of selected cloud infrastructure as code service [ICTCLD505 PC 3.1]
- 3.2 Create and deploy template to provision a set of related cloud resources according to business needs [ICTCLD505 PC 3.2]
- 3.3 Update and redeploy template to modify previously deployed resources and add new resources [ICTCLD505 PC 3.3]
- 3.4 Confirm deployment of cloud resources and configure resources using the cloud platform console or command line tools [ICTCLD505 PC 3.4]
- 3.5 Parameterise and deploy template to reuse configuration with a modified resource configuration [ICTCLD505 PC 3.5]
- 3.6 Remove deployed resources using cloud infrastructure as code tools and delete templates as required [ICTCLD505 PC 3.6]
- 3.7 Test and troubleshoot template errors [ICTCLD505 PC 3.7]
- create, run and update at least one own template required to deploy and modify cloud infrastructure. [ICTCLD505 PE 2]
- parameterisation of templates to support configuration and code reuse [ICTCLD505 KE 8]
- industry standard practices to define infrastructure as code [ICTCLD505 KE 9]

## Group 7 — Shared cloud foundations: industry standards, hardware/software/storage

**Units:** ICTCLD503, ICTCLD505

**Why grouped:** these KE items are near-identical across ICTCLD503 and ICTCLD505 (industry technology standards; industry-standard hardware/software products and storage technology) — foundational knowledge that underpins building. A single foundational knowledge instrument can co-evidence all four.

**Assessment idea (TBD):** shared knowledge questions (or a KE appendix) on cloud industry technology standards and standard hardware/software/storage products — co-evidencing both units once.

- industry technology standards used in cloud computing solutions and services [ICTCLD503 KE 1]
- industry standard hardware and software products, their general features, capabilities and application, including storage technology [ICTCLD503 KE 2]
- industry technology standards used in cloud computing solutions and services [ICTCLD505 KE 1]
- industry standard hardware and software products, their general features, capabilities and application, including storage technology [ICTCLD505 KE 2]

---

# Topic 3 — Monitoring → AT2

Observe the running system: metrics, scaling alarms and alerts.

## Group 8 — Metrics, monitoring, alerts & scaling alarms

**Units:** ICTCLD501, ICTCLD503

**Why grouped:** the monitoring/alerting strand — knowing the techniques to monitor and create alerts (DR context) and setting up metrics with scaling alarms (web-scale context). Plausibly co-evidenced by a single monitoring/alarms configuration task during the build.

**Assessment idea (TBD):** configure metrics, monitoring and alarms (e.g. CloudWatch) — scaling alarms for the web-scale workload and DR-style alerting — as part of the AT2 build. *(Note: `[ICTCLD501 KE 6]` could alternatively be co-evidenced in the AT1 DR plan; placed here with the monitoring practical — TBD.)*

- 4.1 Set up metrics and trigger scaling alarms according to design specifications [ICTCLD503 PC 4.1]
- techniques and methods to monitor and create alerts in cloud environments. [ICTCLD501 KE 6]

---

# Topic 4 — Documenting → AT1 + AT2 (split)

Write it up and close it out. The design documentation + DR-plan closure ride AT1; the build's user documentation + sign-off ride AT2. *(Item-level AT allocation TBD — see Topic & assessment structure above.)*

## Group 9 — Documentation & technical writing

**Units:** ICTCLD503, ICTCLD505

**Why grouped:** documenting and justifying design changes (503 → AT1) and producing user documentation for the IaC infrastructure (505 → AT2), both underpinned by the Writing foundation skill. One documentation work product per deliverable, assessed as a writing-quality strand.

**Assessment idea (TBD):** the architecture-justification documentation (503, in AT1) and the IaC user documentation (505, in AT2), assessed for clarity, structure and technical accuracy.

- 1.7 Document and justify architecture changes [ICTCLD503 PC 1.7]
- 2.4 Document and justify architecture design [ICTCLD503 PC 2.4]
- 4.1 Create user documentation including cloud infrastructure as code templates [ICTCLD505 PC 4.1]
- create user documentation. [ICTCLD505 PE 4]
- **Writing** — Develops complex documentation in required formats using clear and detailed language to convey explicit information, requirements and recommendations<br>Writes and edits code, and technical data in a logical manner using required syntax and ensuring flow [ICTCLD503 FS Writing]
- **Writing** — Prepares user documentation detailing developed cloud infrastructure in a logical manner using required syntax and language [ICTCLD505 FS Writing]

## Group 10 — Finalisation: feedback, sign-off & lodgement

**Units:** ICTCLD501, ICTCLD503, ICTCLD505

**Why grouped:** every unit ends with a finalise/closeout element — walkthrough, seeking and responding to feedback, lodgement, and obtaining final sign-off — underpinned by Oral communication. The DR-plan closure (501) rides AT1; the build closure (503, 505) rides AT2.

**Assessment idea (TBD):** a closure step per deliverable — verbal walkthrough/feedback and a recorded final sign-off block — applied to the AT1 DR plan and the AT2 build.

- 5.1 Conduct verbal walkthrough of cloud disaster recovery plan with required personnel [ICTCLD501 PC 5.1]
- 5.2 Seek and respond to feedback as required [ICTCLD501 PC 5.2]
- 5.3 Lodge cloud disaster recovery plan according to organisation and legislative protocol [ICTCLD501 PC 5.3]
- 5.4 Obtain final sign off from required personnel [ICTCLD501 PC 5.4]
- 4.2 Confirm, seek and respond to feedback with required personnel [ICTCLD503 PC 4.2]
- 4.3 Obtain final sign off from required personnel [ICTCLD503 PC 4.3]
- 4.2 Obtain final sign off from required personnel [ICTCLD505 PC 4.2]
- **Oral communication** — Uses listening and questioning techniques to articulate complex concepts and requirements using industry language in cloud computing and risk environment [ICTCLD501 FS Oral communication]
- **Oral communication** — Uses listening and questioning techniques to confirm requirements and articulate complex concepts and matters using relevant industry for intended audience [ICTCLD505 FS Oral communication]

---

# Cross-cutting & delivery environment (not a topic)

These items are not a delivery topic. The generic foundation skills are co-evidenced inside both ATs' deliverables; the environment/resource conditions are provided by the scenario website + AWS Academy labs; the assessor condition is institutional.

## Group 11 — Foundation skills: reading, self-management & problem solving

**Units:** ICTCLD501, ICTCLD503, ICTCLD505

**Why grouped:** the recurring generic foundation skills shared across all three units — interpreting technical documentation (Reading), troubleshooting/keeping current with cloud technology (Self-management), and structured problem solving. Co-evidenced wherever students work with documentation and resolve issues, across both ATs.

**Assessment idea (TBD):** evidenced implicitly through the technical deliverables and troubleshooting activities; the marking guides note where each FS is naturally co-evidenced rather than assessing it separately.

- **Reading** — Interprets complex technical and operational documentation to determine and confirm job requirements [ICTCLD501 FS Reading]
- **Self-management** — Demonstrates a sophisticated knowledge of principles, concepts, language and practices associated with the cloud and digital world and uses them to troubleshoot and understand the uses and potential of new technology [ICTCLD501 FS Self-management]
- **Problem solving** — Uses a mix of intuitive and formal processes to identify key information and issues, evaluate alternative strategies, anticipate consequences and consider implementation issues and contingencies<br>Uses knowledge of context to address common threats in the cloud and technical environment [ICTCLD501 FS Problem solving]
- **Reading** — Interprets complex technical and operational documentation to determine and confirm job requirements [ICTCLD503 FS Reading]
- **Self-management** — Demonstrates a sophisticated knowledge of principles, concepts, language and practices associated with cloud computing and the digital world and uses them to troubleshoot and understand the uses and potential of new technology [ICTCLD503 FS Self-management]
- **Problem solving** — Uses a mix of intuitive and formal processes to identify key information and issues, evaluates alternative strategies, anticipates consequences and considers implementation issues and contingencies<br>Uses knowledge of context to address common problems in cloud computing applications and cloud-based environments [ICTCLD503 FS Problem solving]
- **Reading** — Interprets complex technical and operational documentation to determine and confirm job requirements [ICTCLD505 FS Reading]
- **Self-management** — Demonstrates a sophisticated knowledge of principles, concepts, language and practices associated with cloud computing and the digital world and uses them to troubleshoot and understand the uses and potential of new technology [ICTCLD505 FS Self-management]
- **Problem solving** — Uses a mix of intuitive and formal processes to identify key information and issues, evaluates alternative strategies, anticipates consequences and considers implementation issues and contingencies<br>Uses knowledge of context to address common problems in cloud computing applications and cloud-based environments [ICTCLD505 FS Problem solving]

## Group 12 — Assessment conditions: required environment & resource access

**Units:** ICTCLD501, ICTCLD503, ICTCLD505

**Why grouped:** the Assessment Conditions "access to" requirements across all three units — the simulated/working environment and the data, services, tooling and reference materials assessment must provide. Provided by the scenario website + AWS Academy labs; defines the delivery environment rather than mapping to a marking criterion.

**Assessment idea (TBD):** captured in the cluster delivery environment spec (AWS Academy labs + scenario site + IDE/CLI/SSH access + reference data), not as assessed criteria.

- data required to assess current and future risk events in specified environment [ICTCLD501 AC 1]
- legislation applicable to risk type [ICTCLD501 AC 2]
- reporting standards for documenting and communicating disaster recovery plan. [ICTCLD501 AC 3]
- cloud vendor service provider [ICTCLD503 AC 1]
- cloud managed database service [ICTCLD503 AC 2]
- cloud serverless environment [ICTCLD503 AC 3]
- pre-prepared code elements for microservice deployment [ICTCLD503 AC 4]
- information and data sources required to design and implement cloud infrastructure [ICTCLD503 AC 5]
- integrated development environment (IDE) [ICTCLD503 AC 6]
- specific requirements and industry standards, organisational procedures and legislative requirements, including business and functionality requirements, as required [ICTCLD503 AC 7]
- internet and web browser [ICTCLD503 AC 8]
- data to gather information from to determine output and user requirements, including user access and business protocols. [ICTCLD503 AC 9]
- cloud vendor service provider [ICTCLD505 AC 1]
- cloud vendor or 3rd party infrastructure as code service [ICTCLD505 AC 2]
- specific requirements and industry standards, organisational procedures and legislative requirements, including business and functionality requirements, as required [ICTCLD505 AC 3]
- information and data sources required to design and implement cloud infrastructure [ICTCLD505 AC 4]
- integrated development environment (IDE) [ICTCLD505 AC 5]
- internet and web browser [ICTCLD505 AC 6]
- secure shell (SSH) or remote desktop protocol (RDP) client to connect to cloud-hosted instances [ICTCLD505 AC 7]
- cloud management console, cloud software development kit or command line tools. [ICTCLD505 AC 8]

## Group 13 — Assessment conditions: assessor requirements

**Units:** ICTCLD501, ICTCLD503, ICTCLD505

**Why grouped:** the identical trailing Assessment Conditions clause in each unit — assessor competency/qualification requirements. Institutional boilerplate, common to all three.

**Assessment idea (TBD):** satisfied by the institution's assessor-qualification policy; no AT artefact required.

- Assessors of this unit must satisfy the requirements for assessors in applicable vocational education and training legislation, frameworks and/or standards. [ICTCLD501 AC 4]
- Assessors of this unit must satisfy the requirements for assessors in applicable vocational education and training legislation, frameworks and/or standards. [ICTCLD503 AC 10]
- Assessors of this unit must satisfy the requirements for assessors in applicable vocational education and training legislation, frameworks and/or standards. [ICTCLD505 AC 9]
