# Topic 07 — Building the microservice with your own IaC · Coverage

**Topic 07 of 9** · **AT2 content Topic** — the slides and the AT2 workbook advance together: each component ends in the workbook task it prepares.

The coverage spec — what this Topic must cover, in UoC and AT terms. `slide_plan.md` and the deck are built to satisfy it.

## Depth ceiling
BUILD — the core of AT2: review the supplied code, author your own template that provisions the
microservice, deploy it, confirm it, test it end to end, troubleshoot it, then parameterise and extend
it. One continuous run of work, in workbook order.

## What this Topic must cover

- **C1 — Review before you build.** Culminates in the workbook: **task 11**.
- **C2 — Author your template.** Culminates in the workbook: **task 12**.
- **C3 — Deploy it, and confirm it.** Culminates in the workbook: **tasks 13 and 14**.
- **C4 — Test it end to end, and troubleshoot.** Culminates in the workbook: **tasks 15 and 16**.
- **C5 — Make it reusable, then grow it.** Culminates in the workbook: **tasks 17 and 18**.

## 1. UoC mapping

UoC **taught / developed** in this Topic:

| UoC item | Descriptor | Component |
|---|---|---|
| [ICTCLD503 PC 3.1] | Review microservice design and code components for application | C1 |
| [ICTCLD505 PC 3.1] | Learn template syntax of selected cloud infrastructure as code service | C2 |
| [ICTCLD505 PC 3.2] | Create and deploy template to provision a set of related cloud resources according to business needs | C2 |
| [ICTCLD505 KE 5] | syntax of selected infrastructure as code service templates | C2 |
| [ICTCLD505 KE 9] | industry standard practices to define infrastructure as code | C2 |
| [ICTCLD505 PC 3.2] | Create and deploy template to provision a set of related cloud resources according to business needs | C3 |
| [ICTCLD505 PC 3.4] | Confirm deployment of cloud resources and configure resources using the cloud platform console or command line tools | C3 |
| [ICTCLD505 PE 2] | create, run and update at least one own template required to deploy and modify cloud infrastructure | C3 |
| [ICTCLD505 PE 3] | use cloud management console, cloud software development kits or command line tools | C3 |
| [ICTCLD503 PC 3.2] | Deploy and configure cloud services to implement the application | C3 |
| [ICTCLD503 PE 3] | deploy a microservice application utilising cloud serverless technologies | C3 |
| [ICTCLD503 PE 4] | use cloud management consoles, software development kits or command line tools | C3 |
| [ICTCLD503 PC 3.3] | Test microservice components and confirm that the application is functioning | C4 |
| [ICTCLD503 PC 3.4] | Troubleshooting and fix errors as required | C4 |
| [ICTCLD503 KE 5] | testing and debugging techniques | C4 |
| [ICTCLD505 PC 3.7] | Test and troubleshoot template errors | C4 |
| [ICTCLD505 KE 7] | testing and debugging techniques, including common issues and errors relating to deploying cloud infrastructure as code | C4 |
| [ICTCLD505 PE 3] | use cloud management console, cloud software development kits or command line tools | C4 |
| [ICTCLD505 PC 3.3] | Update and redeploy template to modify previously deployed resources and add new resources | C5 |
| [ICTCLD505 PC 3.5] | Parameterise and deploy template to reuse configuration with a modified resource configuration | C5 |
| [ICTCLD505 KE 8] | parameterisation of templates to support configuration and code reuse | C5 |
| [ICTCLD505 KE 10] | uses and methods to create, manage, provision and update cloud resources and templates | C5 |

## Changelog
- 2026-09-08 — regenerated from the redrafted slide plan; components re-cut so each one ends in a workbook task.
