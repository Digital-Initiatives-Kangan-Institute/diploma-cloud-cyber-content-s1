# Topic 03 Designing for scalability and the four components — Slide plan
> **Covers:** Topic 03 — see coverage.md
> **Subtitle:** Design the scalability improvements by selecting and improving the four resource tiers
> **STATUS: DRAFT** (authored 2026-07-02).

## Depth ceiling
DESIGN — design the scalability improvements on paper and select/improve the four resource tiers to Ledgerline's business needs; the build is AT3. Scalability = elastic capacity-on-demand, demonstrable by test — not a load forecast. Justify each choice; do not implement, and do not over-provision.

## Teaching source
AWS performance/scalability pillar (elastic capacity, auto scaling, resource selection); bespoke for the four-component allocation framing and the object-storage-in-context contrast.

## AWS pin table
TBD — AWS scalability/architecture modules to be pinned.

## Slides

### Opener
- [BESPOKE] The scalability half of the design
  - Topic 3 continues AT1: you design the scalability improvements for Ledgerline (single-AZ cloud).
  - Structure the design by four resource components — network, compute, database, storage — the same four units the AT2 team later divides the IaC write by.
  - Scalability here means elastic capacity-on-demand, demonstrable by test at AT3 — not a forecast, and not over-provisioning.
  - Design only, to the business needs — the build is AT3.
  image: gen flat vector hero illustration of four cloud resource tiers network compute database storage scaling elastically, blue and gold accents, minimal, no text
  notes:
    Frame the scalability half of AT1's design — structured by the FOUR resource components that also
    become the AT2 team's work-split. Set the depth: design to the business needs, prove-by-test at AT3, no
    over-provisioning.
    • First two bullets: Topic 3 continues AT1 — design the scalability improvements for Ledgerline,
    structured by four components: network, compute, database, storage. These are the same four units the
    AT2 team later divides the IaC write by — flag the seam.
    • Third bullet: scalability here = elastic capacity-on-demand, demonstrable BY TEST at AT3 — not a
    forecast, and not over-provisioning.
    • Fourth bullet (the discipline): design only, to the business needs — the build is AT3.
    Misconception to pre-empt: "scalable = big enough for the busiest day." No — that's over-provisioning
    (paying for idle capacity); scalable means it GROWS and SHRINKS on demand. Different idea entirely.
    Question to pose: "What's the difference between a scalable design and just buying a bigger server?"
    (elastic capacity-on-demand vs fixed spare capacity you pay for whether used or not).
    UoC/AT1 tie: this Topic develops ICTCLD504 PC 2.2 and KE 6; the output is the resource-selection
    sections of the AT1 Solution Design + the object-storage KE-appendix question.

### C1 — The four resource components
- Teaches: [ICTCLD504 PC 2.2]
- Kicker: select and improve each tier to the business needs
- [PRIMER] Scalability = elastic capacity-on-demand
  - Elastic capacity: add resources as load rises, release them as load falls — pay for what you use.
  - The test of a scalable design is a demonstration: it scales on demand (proven at AT3), not a load forecast on paper.
  - Over-provisioning fixed spare capacity is not scalability — it is gold-plating; right-size instead.
  image: none
  notes:
    Open Section 1 with the definition that governs the whole Topic — scalability is elasticity, and it's
    PROVEN by test, not asserted on paper.
    • First bullet: elastic capacity — add resources as load rises, release them as load falls; pay for what
    you use. Both directions matter.
    • Second bullet: the TEST of a scalable design is a demonstration — it scales on demand (proven at AT3),
    not a load forecast on paper. Design so it can be demonstrated.
    • Third bullet: over-provisioning fixed spare capacity is NOT scalability — it's gold-plating;
    right-size instead. The anti-over-engineering rule, made concrete.
    Misconception to pre-empt: "add auto scaling everywhere and you're scalable." No — only some tiers scale
    elastically (compute, storage); scalability is designed per tier to the need, and it must be
    demonstrable.
    Question to pose: "A design with a huge fixed server 'handles any load' — is it scalable?" (No — it's
    over-provisioned; scalable means capacity moves WITH load).
    UoC/AT1 tie: ICTCLD504 PC 2.2 (select & improve resources for scalability) → AT1 Solution Design
    resource-selection sections.
- [BESPOKE] The four resource components
  - Split the design across four tiers: network, compute, database, storage.
  - Compute and storage are the tiers that scale elastically on demand; network and database are selected and configured to support that scale.
  - These are the same four units the AT2 team later divides the IaC write by — a clean seam from design to build.
  image: diagram four-components
  notes:
    Install the FOUR-COMPONENT structure off the diagram — the frame the whole scalability design (and the
    AT2 build) is organised by.
    • First bullet: split the design across four tiers — network, compute, database, storage. Point to each
    on the diagram.
    • Second bullet: compute and storage are the tiers that scale ELASTICALLY on demand; network and
    database are selected and configured to SUPPORT that scale. Not all four scale the same way.
    • Third bullet (the seam): these are the same four units the AT2 team later divides the IaC write by — a
    clean seam from design (now) to build (AT2/AT3). Flag it; it's a deliberate design-to-build hand-off.
    Misconception to pre-empt: "all four tiers scale the same way." No — compute/storage scale elastically;
    network/database are sized and configured to carry that scale. Treating them identically misdesigns the
    tier.
    Question to pose: "Which of the four tiers actually add and remove capacity on demand — and which just
    have to support that?" (compute + storage scale; network + database support).
    UoC/AT1 tie: ICTCLD504 PC 2.2 (select & improve compute/storage/database/network resources) → AT1
    Solution Design; the four components are also the AT2 IaC work-split.
- [BESPOKE] Selecting and improving each tier
  - Network: right-size the path and load-spreading so the tier below can scale out behind it.
  - Compute: move from fixed capacity to a pool that grows and shrinks on demand (auto scaling).
  - Database: select a managed data service that scales reads without a rebuild; keep Ledgerline's accounting data consistent.
  - Storage: select storage that grows on demand rather than a fixed-size volume.
  image: none
  notes:
    Walk each of the four tiers concretely — what "select and improve for scalability" means per tier. This
    is the how-to behind the four-component frame.
    • Network: right-size the path and the load-spreading so the tier below can scale OUT behind it.
    • Compute: move from fixed capacity to a POOL that grows and shrinks on demand (auto scaling) — the
    clearest example of elasticity.
    • Database: select a managed data service that scales READS without a rebuild, while keeping
    Ledgerline's accounting data consistent. (Note the consistency constraint — it's an accounting system.)
    • Storage: select storage that grows on demand rather than a fixed-size volume.
    Misconception to pre-empt: "scale the database by adding write replicas." No — an accounting system
    needs consistency; you scale READS and keep writes consistent, you don't shard the ledger for
    throughput.
    Question to pose: "Compute scales by a pool that grows/shrinks — what's the equivalent move for
    storage?" (grows on demand vs a fixed-size volume).
    UoC/AT1 tie: ICTCLD504 PC 2.2 (select & improve each resource tier to business needs) → AT1 Solution
    Design resource selection.
- [BESPOKE] Justify against the business needs
  - Tie every resource choice to a stated Ledgerline business need — why this tier, why this size.
  - Choose the simplest option that meets the need; note where capacity scales elastically and how it would be demonstrated by test.
  - Do not over-engineer: no tier scaled beyond what a need justifies.
  image: none
  notes:
    The justification discipline — every resource choice ties to a stated business need, and nothing is
    scaled further than a need justifies. This is what turns selections into a defensible design.
    • First bullet: tie every resource choice to a stated Ledgerline business need — why THIS tier, why THIS
    size. No choice without a reason.
    • Second bullet: choose the simplest option that meets the need; note where capacity scales elastically
    and HOW it would be demonstrated by test (the AT3 link).
    • Third bullet: do not over-engineer — no tier scaled beyond what a need justifies.
    Misconception to pre-empt: "more headroom is safer, so scale up." No — unjustified capacity is
    gold-plating and loses marks; the defensible design is the simplest one that meets the need.
    Question to pose: "If I asked 'why is the compute tier sized like that?', what's your answer?" (a named
    business need + how it scales on demand — not 'to be safe').
    UoC/AT1 tie: ICTCLD504 PC 2.2 (select & improve resources ACCORDING TO business needs) → AT1 Solution
    Design resource justification.
- [EX] Design the four tiers for the practice engagement
  - For the practice-vehicle engagement, select and improve the network, compute, database and storage tiers to its business needs.
  - Mark where capacity scales elastically, and justify each choice against a named need.
  timer: ~30 min
  image: none
  notes:
    Facilitation — the Section 1 practice; students select and improve the four tiers for the practice
    engagement, marking where capacity scales elastically and justifying each choice.
    Tell students: "For the practice engagement, select and improve the network, compute, database and
    storage tiers to its business needs. Mark where capacity scales elastically, and justify each choice
    against a named need."
    Steps (put on the board):
    1. Take the four tiers one at a time — network, compute, database, storage.
    2. For each, choose how to select/improve it for scalability to a stated need.
    3. Mark which tiers scale ELASTICALLY on demand, and note how you'd demonstrate it by test.
    Must produce: a four-tier resource design, each choice tied to a named need, elastic tiers marked.
    Timing: ~30 min then discuss. Where they get stuck: they over-provision "to be safe" (push
    right-sizing), and they mark network/database as elastic when those SUPPORT scale rather than scale
    themselves — circulate and correct.
    Share-back prompt: ask one student which tiers they marked elastic, and challenge any that are really
    just "big."
    No-leakage note: the website is the practice vehicle; AT1 assesses resource selection on Ledgerline —
    comparable, not identical.

### C2 — Object storage in context
- Teaches: [ICTCLD504 KE 6]
- Kicker: contrast a stateful system with an object-storage-dependent one
- [PRIMER] Object storage for static web sites
  - Object storage holds whole objects (files) addressed by key — it scales storage on demand and serves static assets directly.
  - It is the natural home for a static web site's content: HTML, images, downloads served without a server.
  - Contextual knowledge here — not a Ledgerline requirement, but the contrast that sharpens what Ledgerline's storage actually needs.
  image: none
  notes:
    Open Section 2 — object storage, taught as CONTEXTUAL knowledge (KE 6). It's not a Ledgerline
    requirement; it's the contrast that sharpens what Ledgerline's storage actually is.
    • First bullet: object storage holds whole objects (files) addressed by key — it scales storage on
    demand and serves static assets directly.
    • Second bullet: it's the natural home for a STATIC web site's content — HTML, images, downloads served
    without a server.
    • Third bullet (the framing): contextual here — not a Ledgerline need, but the contrast that sharpens
    what Ledgerline's storage actually needs. Signal this is a "know it for the KE question" slide.
    Misconception to pre-empt: "so we should put Ledgerline on object storage." No — Ledgerline is a
    transactional, database-backed system; object storage suits STATIC content. The next slide draws the
    contrast.
    Question to pose: "What kind of workload is object storage the natural home for — and is Ledgerline one
    of them?" (static websites; no — Ledgerline is stateful).
    UoC/AT1 tie: ICTCLD504 KE 6 (use of object storage for static web sites) → the object-storage-in-context
    question in the AT1 Part A KE appendix.
- [BESPOKE] Ledgerline vs a static-website workload
  - Ledgerline is a stateful accounting system: transactional, consistent, database-backed — object storage is not its primary store.
  - An object-storage-dependent static-website workload is the opposite: its content lives in object storage and scales with it.
  - Be able to explain how you would provision object storage for such a workload if the need arose.
  image: none
  notes:
    Draw the CONTRAST explicitly — Ledgerline (stateful) versus an object-storage-dependent static-website
    workload. The contrast is the answer to the KE-appendix question.
    • First bullet: Ledgerline is a stateful accounting system — transactional, consistent, database-backed;
    object storage is NOT its primary store.
    • Second bullet: an object-storage-dependent static-website workload is the OPPOSITE — its content lives
    in object storage and scales with it.
    • Third bullet: be able to explain how you would PROVISION object storage for such a workload if the need
    arose (the examinable skill).
    Misconception to pre-empt: "every system should use object storage because it scales." No — fit to the
    workload: static content → object storage; transactional accounting data → a managed database.
    Question to pose: "For a static website you'd reach for object storage — walk me through provisioning it.
    Now why is that the wrong store for Ledgerline's ledger?" (static vs transactional/consistent).
    UoC/AT1 tie: ICTCLD504 KE 6 → AT1 Part A KE appendix (the object-storage-in-context question).
- [EX] Answer the object-storage-in-context question
  - Contrast Ledgerline's storage needs with an object-storage-dependent website workload.
  - Explain how you would provision object storage for the website workload if it were needed.
  timer: ~15 min
  image: none
  notes:
    Facilitation — the Section 2 practice; students answer the object-storage-in-context question in
    writing — a direct rehearsal of the AT1 KE-appendix question.
    Tell students: "Contrast Ledgerline's storage needs with an object-storage-dependent website workload.
    Then explain how you would provision object storage for the website workload if it were needed."
    Steps (put on the board):
    1. State Ledgerline's storage character — stateful, transactional, database-backed.
    2. Contrast the static-website workload — content in object storage, scales with it.
    3. Explain how you'd provision the object storage for that website workload.
    Must produce: a short written answer with the contrast plus a provisioning explanation.
    Timing: ~15 min then discuss. Where they get stuck: they describe object storage generically without the
    CONTRAST, or forget the provisioning step — circulate and check both halves are present.
    Share-back prompt: read one strong answer and ask the room whether it (a) contrasts and (b) provisions.
    No-leakage note: this rehearses the KE-appendix question shape; AT1 asks it for Ledgerline — comparable,
    not identical.
- [TAKEAWAYS] Topic 3 · Key takeaways
  - Scalability = elastic capacity-on-demand, demonstrable by test — not a forecast, not over-provisioning.
  - Design across four resource components: network, compute, database, storage — the AT2 IaC seam.
  - Justify each tier against a Ledgerline business need; right-size, choose the simplest that fits.
  - Object storage suits static-website workloads; Ledgerline is stateful and database-backed — know the contrast.
  image: none

### Close
- [BESPOKE] Next: Topic 4 — document, present & sign-off
  - You've designed the scalability half across the four components; next you document and present the Solution Design for sign-off.
  - Bring these resource selections and their justifications — they are the core of the design.
  image: none

## Build notes
~11 slides. Exercises run on the practice-vehicle engagement (design only). One generated diagram (`diagram four-components` — the four tiers network/compute/database/storage with elastic-scaling indicators on compute and storage); one decorative `gen` image (opener hero).

## Changelog
- 2026-07-02 — authored to full content from coverage.md.
