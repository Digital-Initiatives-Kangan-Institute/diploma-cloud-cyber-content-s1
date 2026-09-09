# Topic 06 — IaC: fundamentals & operating provided templates · Coverage

**Topic 06 of 9** · **AT2 content Topic** — the slides and the AT2 workbook advance together: each component ends in the workbook task it prepares.

The coverage spec — what this Topic must cover, in UoC and AT terms. `slide_plan.md` and the deck are built to satisfy it.

## Depth ceiling
BUILD — first hands-on Topic of AT2. Work through the IaC concepts, then take a provided template
through review, deploy, failure, fix, confirm, update and reset. Authoring your own is Topic 7.

## What this Topic must cover

- **C1 — Why IaC, and choosing the service.** Culminates in the workbook: **tasks 1, 2, 3 and 4**.
- **C2 — Reading a template you were given.** Culminates in the workbook: **task 5**.
- **C3 — Deploy it, fix it, confirm it.** Culminates in the workbook: **tasks 6, 7 and 8**.
- **C4 — Update it, and put it back.** Culminates in the workbook: **tasks 9 and 10**.
- **C5 — Shared cloud foundations.**

## 1. UoC mapping

UoC **taught / developed** in this Topic:

| UoC item | Descriptor | Component |
|---|---|---|
| [ICTCLD505 PC 1.1] | Identify and review benefits of infrastructure as code according to business needs | C1 |
| [ICTCLD505 PC 1.2] | Determine ways automation leverages cloud platforms according to business needs | C1 |
| [ICTCLD505 PC 1.3] | Determine and assess potential issues and errors when implementing infrastructure as code | C1 |
| [ICTCLD505 PC 1.4] | Evaluate and select infrastructure as code service compatible with selected cloud platform and business requirements | C1 |
| [ICTCLD505 KE 3] | benefits of deploying infrastructure as code compared to manual provisioning in a console | C1 |
| [ICTCLD505 KE 4] | different infrastructure as code services that can be used on a cloud platform | C1 |
| [ICTCLD505 KE 7] | testing and debugging techniques, including common issues and errors relating to deploying cloud infrastructure as code | C1 |
| [ICTCLD505 PC 2.1] | Learn template syntax of selected cloud infrastructure as code service | C2 |
| [ICTCLD505 PC 2.2] | Review pre-defined templates and determine what resources they create and any dependencies | C2 |
| [ICTCLD505 KE 5] | syntax of selected infrastructure as code service templates | C2 |
| [ICTCLD505 PC 2.3] | Utilise the cloud infrastructure as code service tools to deploy, update and delete resources using predefined templates as required | C3 |
| [ICTCLD505 PC 2.4] | Confirm deployments of cloud resources and configure resources using cloud platform console or command line tools | C3 |
| [ICTCLD505 PC 2.6] | Test and troubleshoot template errors as required | C3 |
| [ICTCLD505 PE 1] | deploy, update and remove cloud infrastructure using cloud platform templates | C3 |
| [ICTCLD505 PE 3] | use cloud management console, cloud software development kits or command line tools | C3 |
| [ICTCLD505 KE 6] | tooling required to execute cloud infrastructure templates | C3 |
| [ICTCLD505 KE 7] | testing and debugging techniques, including common issues and errors relating to deploying cloud infrastructure as code | C3 |
| [ICTCLD503 PE 4] | use cloud management consoles, software development kits or command line tools | C3 |
| [ICTCLD503 KE 5] | testing and debugging techniques | C3 |
| [ICTCLD505 PC 2.3] | Utilise the cloud infrastructure as code service tools to deploy, update and delete resources using predefined templates as required | C4 |
| [ICTCLD505 PC 2.4] | Confirm deployments of cloud resources and configure resources using cloud platform console or command line tools | C4 |
| [ICTCLD505 PE 1] | deploy, update and remove cloud infrastructure using cloud platform templates | C4 |
| [ICTCLD505 KE 10] | uses and methods to create, manage, provision and update cloud resources and templates | C4 |
| [ICTCLD505 KE 11] | techniques, methods and industry standard metrics used to leverage cloud platform capabilities and deploy and manage templates | C4 |
| [ICTCLD503 KE 1] | industry technology standards used in cloud computing solutions and services | C5 |
| [ICTCLD505 KE 1] | industry technology standards used in cloud computing solutions and services | C5 |
| [ICTCLD503 KE 2] | industry standard hardware and software products, their general features, capabilities and application, including storage technology | C5 |
| [ICTCLD505 KE 2] | industry standard hardware and software products, their general features, capabilities and application, including storage technology | C5 |

## Changelog
- regenerated from the slide plan by scripts/generate_topic_coverage.py; components re-cut so each one ends in a workbook task.
