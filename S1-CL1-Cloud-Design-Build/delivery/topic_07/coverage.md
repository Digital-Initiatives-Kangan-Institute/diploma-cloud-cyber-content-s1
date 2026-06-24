# Topic 7 — Network & security base · Coverage

**Topic 7 of 14** · **AT2 content Topic** (cloud build — network tier) · teaching source: **mostly AWS-sourced** — ACF M05 (Networking & Content Delivery) + ACA M07 (Creating a Networking Environment) carry the VPC / subnets / route tables / security groups / Route 53 teaching and the recorded build demo; **bespoke** fills only the working-to-the-design framing, the design's specific topology, the concept **primers**, and the connectivity-test discipline.

The coverage spec — what this Topic must cover, in UoC and AT2 terms. `slide_plan.md` and the deck are built to satisfy it.

> **Continues the AT2 build arc** (after Topic 6 — foundations). Students keep *building* a **supplied design** in the AWS Academy lab and capturing **evidence** for the Deployment Report. Topic 7 lays the **network fabric** the Topic 8 workload tier will sit inside: the VPC, its subnets, traffic control (security groups), and name resolution (DNS). AT2 = ICTCLD401 (primary) + ICTCLD502 (partial).

---

## Teaching-design note — primer-first (no assumed baseline)

**We cannot assume students arrive with base IT/networking knowledge.** So every technical concept is taught **fundamentals-first**: a short, vendor-neutral **primer** (what the thing *is* — e.g. what an IP address / subnet is, how DNS resolves a name, what a firewall does) **before** the AWS-context slide that shows how AWS implements it. The per-concept shape is:

> **primer (the fundamental) → AWS-context teach (how AWS does it) → recorded demo → practice activity.**

Reuse-first still governs the primer: where an AWS deck already teaches the fundamental (ACF M05 opens with a **"Networking basics"** section), pin those slides as the primer; author a **bespoke primer only where AWS assumes the knowledge** (e.g. a plain "how DNS works" or "what a firewall is" explainer). *(Tim, 2026-06-02 — applies to this Topic; candidate principle for all AWS-heavy build Topics, TBD to confirm across Topics 8–9.)*

---

## What this Topic must cover

The **network tier** of the cloud build: stand up the virtual network the workload will live in, control traffic into and between its tiers, and make resources reachable by name — all to a **supplied design**, evidenced as built. Three components:

- **C1 — Virtual network & subnets (VPC).** What a network/subnet *is* (primer) → how AWS does it (VPC, CIDR, multi-tier subnets across an AZ, internet gateway, NAT, route tables) → build the design's VPC + subnets + routing. *(ICTCLD401 PC 2.2.)*
- **C2 — Controlling traffic (security groups).** What a firewall / stateful packet filter *is* (primer) → AWS security groups (stateful, allow-rules, chained between tiers) → build the design's `sg-alb → sg-app → sg-db` least-privilege chain. *(ICTCLD401 KE — limiting network traffic within virtual networks.)*
- **C3 — Name resolution & connectivity (DNS + testing).** How DNS *works* (primer) → Route 53 (the design's internal/private name + ACM) → and **test reachability** (external access in, access between tiers) and fix errors. *(ICTCLD401 KE — DNS; PC 2.6 — test access, introduced here, completed in Topic 8/9 once compute exists.)*

---

## 1. UoC mapping

UoC **taught / developed** in this Topic:

| UoC item | Descriptor | Component |
|---|---|---|
| [ICTCLD401 PC 2.2] | Create virtual multi-tier network to support core services and autoscaling | C1 |
| [ICTCLD401 PC 2.6] | Test external network access and access between resources within virtual network and fix errors | C3 *(introduced; completed Topic 8/9)* |
| [ICTCLD401 KE 5] | Functions/features of networking options — **virtual networks and traffic routing** | C1 |
| [ICTCLD401 KE 9] | Security mechanisms — **securities as it applies to limiting network traffic within virtual networks** | C2 |
| [ICTCLD401 KE 10] | **Purpose of domain name system (DNS)** required to connect remote servers when web browsing | C3 |
| [ICTCLD401 PE 1] | Build at least one simple **virtual network** capable of supporting a workload (the network portion) | C1 · C2 |
| [ICTCLD401 PE 3] | Conduct simple tests to confirm access to resources (network reachability portion) | C3 |

> AT2 criterion **A2** is the marking home (per Topic 6, **A2 bundles IAM + network + security**; Topic 6 took IAM + shared responsibility, **Topic 7 takes network + security groups + DNS**). AT2 Deployment Report section **§4.2 (VPC / subnets / security groups)** + the DNS portion of §4. Maps to the AT2 build-topic refs **T4 (VPC) · T5 (security groups) · T12 (DNS)**.

UoC **applied** here but **taught earlier** (not re-taught):

| What | Where |
|---|---|
| Account / Region setup; evidence-capture discipline | Topic 6 (C1) — continued, not re-taught |
| What IAM/regions/shared responsibility are; the workload's identity model | Topic 6 |
| The IaaS framing (a VPC is the I in IaaS) | Topic 1 |

---

## 2. AT2 equivalence / alignment

| AT2 element | Criterion | How Topic 7 aligns |
|---|---|---|
| **§4.2 Network — VPC / subnets / routing** (Build Narrative — network tier) | A2 | C1 — VPC, multi-tier subnets, IGW/NAT, route tables built to the design; evidenced in Appendix A screenshots + Appendix B exports. |
| **§4.2 Network — security groups** | A2 | C2 — the `sg-alb → sg-app → sg-db` least-privilege chain built to the design. |
| **§4 DNS / name resolution** | A2 | C3 — the design's internal/private DNS name (Route 53) + ACM cert reference. |
| **Connectivity testing; fix errors** | A2 · A10 | C3 — reachability tests (external-in, tier-to-tier), captured as evidence; completed once compute exists (Topic 8/9). |

**Practice-activity alignment:** students stand up the **network tier** (VPC + subnets + routing + security groups + DNS) of the **practice** engagement (Accounting / Ledgerline) in the AWS Academy lab, capturing evidence — mirroring the AT2 network build on the LMS.

**The design students build to (network section):**
- **Practice (Accounting/Ledgerline):** VPC `10.0.0.0/16`; subnets in ap-southeast-2a — `public-egress-a` (NAT only), `private-app-a` (app + internal ALB), `private-data-a` (RDS); **IGW for egress only, no inbound internet**; route tables per tier; staff reach the service over the **campus Site-to-Site VPN**. SGs: `sg-alb` (443 from staff CIDR) → `sg-app` (from sg-alb; SQL out to sg-db) → `sg-db`. DNS = internal Ledgerline hostname + ACM (a C8 implementer decision).
- **Assessed (LMS):** parallels the above but **internet-facing** (public ALB) — same structure, different exposure. The HA follow-on (AT3) adds the `-b` subnets in ap-southeast-2b.

---

## Out of scope for this Topic (covered elsewhere)

- **Compute / ALB / ASG / RDS / S3** (the workload that fills the network) → **Topic 8**. *(Security groups are built here as rule shells; their targets — EC2/RDS/ALB — arrive in Topic 8.)*
- **CloudWatch, VPC flow-logs analysis, config-decision justification, full connectivity testing** → **Topic 9**.
- **DNS failover / Route 53 health checks** (HA routing) → **AT3** (Topics 11–14).
- **Site-to-Site VPN / Direct Connect build** (ACA M08) — the campus VPN is a *given* in the design; students don't build it. Understanding-only.
- **CloudFront / edge** (in ACF M05) — not in the YAT/Accounting design.
- **What these services are conceptually** beyond the primers → applied here, built not re-taught.

---

## Coverage checklist (for `slide_plan.md` + the deck to satisfy)

- [ ] Every UoC item in §1 (taught/developed) is taught in the deck.
- [ ] Each of C1–C3 has **primer → AWS-context teach → (recorded) demo → practice activity** (hands-on in the lab, not a document).
- [ ] A vendor-neutral **primer precedes every concept** — subnet/IP/CIDR, firewall/ports, DNS resolution — reusing ACF M05 "Networking basics" where it teaches the fundamental, bespoke only for gaps.
- [ ] AWS teaching slices pinned: **ACF M05** (networking basics, VPC, subnets, security groups, Route 53) + **ACA M07** (VPC, subnets, IGW, route tables, security groups). Bespoke covers working-to-design + the design's topology + test discipline.
- [ ] **Demos are recorded AWS demos** where one fits: **ACA M07 S30** (VPC + security groups + Elastic IP build — covers C1+C2) and **ACF M05 S30** (VPC); Route 53 simple routing (**ACA M10 S51**) for C3 if used. Live demo only if no recorded demo fits.
- [ ] The design's network topology (VPC/subnets/SGs/DNS) is shown explicitly — the thing students build to (C1–C3).
- [ ] Security groups taught as **stateful, least-privilege, chained between tiers** (C2).
- [ ] Connectivity **testing + fix-errors** introduced (C3, PC 2.6) — noting full resource-to-resource testing completes once compute exists.
- [ ] Depth ceiling respected: stand up the network tier per a supplied design — single-AZ baseline, **no HA / Multi-AZ** (deferred to AT3).
- [ ] AT2 alignment (§2) explicit enough that a student leaving this Topic could build + evidence the network tier.
