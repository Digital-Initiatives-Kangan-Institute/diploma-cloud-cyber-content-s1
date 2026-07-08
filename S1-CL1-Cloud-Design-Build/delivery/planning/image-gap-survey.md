# CL1 image-gap survey + fill checklist

**Status:** IN PROGRESS, 2026-07-08. A survey of the 14 CL1 topic decks for image gaps, each classified
into one of three fill routes, with a committed target asset per gap so the deck can be rebuilt with every
image already in place.

**Progress (2026-07-08):**
- ✅ **Engine change** — the builder places a committed `reuse <file>` from `topic_NN/images/` (was:
  human paste after build). `[TABLE]`-with-no-columns now degrades to a content slide instead of crashing.
- ✅ **10 diagrams** authored + rendered (`topic_NN/diagrams/`).
- ✅ **7 gen images** generated + cached (`topic_01/images/`).
- ✅ **13 / 14 AWS reuse images** extracted/exported into the topic `images/` folders. **Outstanding: only
  `01-aws-console`** (live AWS Console screenshot).
- ✅ **All 31 slide-plan `image:` directives wired** (`diagram` / `gen` / `reuse <file>`).
- ✅ **Pipeline verified** — a throwaway build of topic_01 embedded 17 images (5 diagram + 7 gen + 5 reuse).
- ✅ **Path A executed** — image placement wired into all 8 per-topic build scripts
  (`scripts/s1_cl1/build_s1_cl1_topic*_deck.py`, via a `_img()` helper → committed files); all 8 decks
  rebuilt with **30 / 31 images placed** (only `01-aws-console` is a placeholder pending the screenshot).
  Sizes 1–8 MB (all under the 25 MB gate). The per-topic scripts are the content-complete CL1 deck source;
  the reconstructed `slide_plan.md` skeletons keep the parallel `image:` directives for a future Path-B.
- ✅ **31/31 placed** — `01-aws-console` filled (AWS Console Home screenshot); topic_01 rebuilt to 18 images.
- ✅ **Visual review** (new `review-slides` skill — LibreOffice → per-slide PNG) across all 8 image-bearing
  decks: **0 leftover placeholders**, gen images artefact-free. Three of Claude's diagrams rendered too
  small (wide-short in the deck's image zone) and were reshaped: `deployment-models` → 2×2 grid,
  `service-model-spectrum` → vertical stack, `multi-az-rds` → vertical stack. topic_01 + topic_11 rebuilt.
  All other image slides (AWS reuse + remaining diagrams + gen) render legibly and well-composed.

## The reproducibility principle (why every image is a committed topic asset)
A topic deck is built **from** its `slide_plan.md` by the umbrella `build_topic_deck.py`. The build must
be a **pure function of committed source** — so regenerating a deck never loses images. That already holds
for two of the three routes; the third (AWS reuse) is the gap this checklist closes:

| Route | Source of truth (committed) | Placed on rebuild? |
|---|---|---|
| 📐 **diagram** | `topic_NN/diagrams/<ref>.json` (+ rendered `.drawio`/`.png`) | ✅ auto (draw-diagram, in-pipeline) |
| 🎨 **gen** | `topic_NN/images/` (generate-once, committed) | ✅ auto (image-gen, cached) |
| ☁️ **reuse (AWS)** | `topic_NN/images/` (extracted AWS slide asset) | ⚠️ **only once the builder places a stored `reuse` file** — see Open decision 1 |

**Asset convention (per topic):**
- `topic_NN/diagrams/` — editable diagram source (`.json` spec + `.drawio`) and its rendered `.png`.
- `topic_NN/images/` — all raster assets: `gen` images + extracted AWS `reuse` images, human-named `NN-slug.png`.

Everything committed → a deck rebuild repopulates every slide from disk. No post-build hand-pasting survives regen.

## Legend
📐 diagram (draw-diagram) · 🎨 gen (image-gen / Nano Banana) · ☁️ reuse (AWS Academy slide — instructor decks,
gitignored/local). AWS deck families: **ACF** = Cloud Foundations · **ACA** = Cloud Architecting · **502** =
ICTCLD502 bespoke HA decks. Status: ☐ open · ☑ filled.

---

## Topic 01 — Intro to Cloud (18)
| # | Slide | Route | Target asset | Source / pin | Status |
|---|---|---|---|---|---|
| 1 | What is cloud computing? | 🎨 gen | `images/01-what-is-cloud.png` | conceptual opener | ☐ |
| 2 | Cloud computing defined | 🎨 gen | `images/01-cloud-defined.png` | cloud / data-centre concept | ☐ |
| 3 | Infrastructure as software | 🎨 gen | `images/01-infrastructure-as-hardware.png` | physical racks illustration | ☐ |
| 4 | Traditional computing model | 📐 diagram | `diagrams/traditional-computing-model` | on-prem stack | ☐ |
| 5 | Cloud computing model | 📐 diagram | `diagrams/cloud-computing-model` | cloud stack | ☐ |
| 6 | Cloud deployment models | 📐 diagram | `diagrams/deployment-models` | public/private/hybrid | ☐ |
| 7 | Cloud service models | 📐 diagram | `diagrams/service-model-spectrum` | IaaS/PaaS/SaaS control-vs-effort | ☐ |
| 8 | Availability Zones | 📐 diagram | `diagrams/availability-zones` | Region→AZ boxes (AWS alt: ACF M03) | ☐ |
| 9 | AWS categories of services | ☁️ reuse | `images/01-aws-service-categories.png` | **ACF M01** | ☐ |
| 10 | Compute | 🎨 gen | `images/01-icon-compute.png` | category icon | ☐ |
| 11 | Storage | 🎨 gen | `images/01-icon-storage.png` | category icon | ☐ |
| 12 | Database | 🎨 gen | `images/01-icon-database.png` | category icon | ☐ |
| 13 | Networking & content delivery | 🎨 gen | `images/01-icon-networking.png` | category icon | ☐ |
| 14 | AWS Management Console (activity) | ☁️ reuse | `images/01-aws-console.png` | live console screenshot | ☐ |
| 15 | Well-Architected Framework | ☁️ reuse | `images/01-well-architected-pillars.png` | **ACF M09** (6 pillars) | ☐ |
| 16 | How do you pay for AWS? | ☁️ reuse | `images/01-aws-pricing-philosophy.png` | **ACF M02** | ☐ |
| 17 | Pay less when you reserve | ☁️ reuse | `images/01-reserved-instance-options.png` | **ACF M02** | ☐ |
| 18 | AWS Pricing Calculator | ☁️ reuse | `images/01-pricing-calculator.png` | **ACF M02 S20** / live capture | ☐ |

## Topic 03 — Building the evidence (1)
| # | Slide | Route | Target asset | Source / pin | Status |
|---|---|---|---|---|---|
| 19 | AWS Pricing Calculator | ☁️ reuse | `images/03-pricing-calculator.png` | same as #18 (**ACF M02 S20**) | ☐ |

## Topic 06 — Build foundations (3)
| # | Slide | Route | Target asset | Source / pin | Status |
|---|---|---|---|---|---|
| 20 | Cloud arch: reqs→design→build | ☁️ reuse | `images/06-aws-arch-reqs-design-build.png` | **ACA M02 S08** (alt: diagram) | ☐ |
| 21 | IAM components | ☁️ reuse | `images/06-iam-components.png` | **ACF M04 S18** / ACA M03 (alt: diagram) | ☐ |
| 22 | Shared responsibility model | ☁️ reuse | `images/06-shared-responsibility.png` | **ACF M04 S05** | ☐ |

## Topic 07 — Network & security base (3)
| # | Slide | Route | Target asset | Source / pin | Status |
|---|---|---|---|---|---|
| 23 | IP address / CIDR | ☁️ reuse | `images/07-ip-cidr.png` | **ACF M05 S6/S8** (alt: diagram) | ☐ |
| 24 | VPC anatomy (subnets·IGW·NAT·routes) | 📐 diagram | `diagrams/vpc-anatomy` | draw-diagram; AWS alt **ACA M07 S16** | ☐ |
| 25 | Route 53 DNS resolution flow | ☁️ reuse | `images/07-route53-dns-flow.png` | **ACF M05 S50** (alt: diagram) | ☐ |

## Topic 08 — Compute & elasticity (2)
| # | Slide | Route | Target asset | Source / pin | Status |
|---|---|---|---|---|---|
| 26 | ALB → target group → instances | 📐 diagram | `diagrams/alb-target-instances` | draw-diagram; AWS alt ACA M10 | ☐ |
| 27 | Auto Scaling group (horizontal) | ☁️ reuse | `images/08-asg-horizontal-scaling.png` | **ACA M10 S22** (alt: diagram) | ☐ |

## Topic 09 — Operability & justification (1)
| # | Slide | Route | Target asset | Source / pin | Status |
|---|---|---|---|---|---|
| 28 | CloudWatch metrics/alarms/dashboards | ☁️ reuse | `images/09-cloudwatch.png` | **ACA M10 S9–12** (screenshots) | ☐ |

## Topic 11 — HA concepts (1)
| # | Slide | Route | Target asset | Source / pin | Status |
|---|---|---|---|---|---|
| 29 | Multi-AZ RDS (primary + standby) | 📐 diagram | `diagrams/multi-az-rds` | scenario arch; AWS alt **502 T3 / ACA M10 S44** | ☐ |

## Topic 12 — HA design (2)
| # | Slide | Route | Target asset | Source / pin | Status |
|---|---|---|---|---|---|
| 30 | Identify the single points of failure | 📐 diagram | `diagrams/identify-spofs` | author fresh, LMS-accurate (**502 T2 S10**) | ☐ |
| 31 | Cross-AZ HA architecture | 📐 diagram | `diagrams/cross-az-ha-architecture` | ALB+ASG+Multi-AZ RDS; AWS alt **ACA M10 S41** | ☐ |

---

## Tally
| Route | Count | Who / how |
|---|---|---|
| ☁️ reuse (AWS) | 14 | Extract from the AWS Academy `.pptx` (local, gitignored) — needs the decks on this machine |
| 📐 diagram | 10 | Claude authors the draw-diagram spec → rendered + placed in-pipeline |
| 🎨 gen | 7 | Claude generates via image-gen → committed + placed in-pipeline |

Topics **02, 04, 05, 10, 13, 14** have **no flagged images** (see Open decision 3).

## Open decisions
1. **Builder placement of `reuse` assets.** Extend `deck_images.resolve_image` so `reuse <file>` places a
   committed `topic_NN/images/<file>` when present (else the current labelled placeholder). This is what
   makes AWS images survive a deck rebuild. *(Small, backward-compatible engine change — umbrella.)*
2. **AWS extraction is blocked until the AWS Academy decks are on this machine** (`original-materials/`,
   gitignored). With them present, Claude can extract the pinned slides/media programmatically.
3. **Scope:** all 14 decks are currently image-free and ~220 slides are `image: none`. If polished decks are
   wanted (opener/section hero per topic), that's an *additional* `gen` pass beyond these 31 — opt-in.
4. **Reuse-vs-diagram on architecture items** (24, 26, 29, 30, 31 recommended as diagrams; 20/21/25/27 could
   go either way) — confirm per item as we fill.
5. **CL1 build-path fork (blocking the real deck build).** The 14 CL1 decks are built by the old per-topic
   scripts (`scripts/s1_cl1/build_s1_cl1_topicNN_deck.py`), which hold the real slide content; the
   `slide_plan.md` files are reconstructed skeletons (no briefs / table data). So `build_topic_deck.py`
   builds a structurally-correct deck **with the images but without the real content**. Two paths:
   **A** — add image placement to the per-topic scripts (fast, keeps content, perpetuates deprecated scripts);
   **B** — flesh the 14 slide plans with the real content, then build via the generic builder (converges CL1
   with CL2/CL3; a sizeable content-recovery job). *The image assets + wiring are ready for either.*
