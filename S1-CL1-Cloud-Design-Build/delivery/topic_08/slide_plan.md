# Topic 08 The workload tier — compute & elasticity — Slide plan
> **Covers:** Topic 08 — see coverage.md
> **STATUS: RECONSTRUCTED** from the built deck (The workload tier — compute & elasticity); structure + image sources + per-component Teaches are authoritative, slide briefs were not recoverable from the deck.

## Depth ceiling
As built — see coverage.md for the AT depth ceiling.

## Teaching source
As built (see coverage.md header).

## AWS pin table
As pinned in the build (AWS refs carried on each slide's type tag where applicable).

## Slides

### Opener
- [BESPOKE] Filling the network
  image: none

### C1 — Compute (EC2 + EBS)
- Teaches: [ICTCLD401 PC 2.3] · [ICTCLD401 PC 2.4] · [ICTCLD401 PC 2.6] · [ICTCLD401 KE 5] · [ICTCLD401 KE 6] · [ICTCLD401 KE 6] · [ICTCLD401 PE 2]
- [BESPOKE] What a server is — and a virtual one
  image: none
- [AWS ACF M06 S10] Amazon EC2
  image: none
- [AWS ACF M06 S11–S26] Launching an instance — the key choices
  image: none
- [AWS ACF M06 S22] Storage on the instance — EBS (block)
  image: none
- [BESPOKE] The compute you'll build
  image: none
- [DEMO] Launch an EC2 instance
  image: none
- [EX] Launch the Ledgerline server
  image: none
- [TAKEAWAYS] Section 1 · Compute
  image: none

### C2 — Elasticity (ALB + Auto Scaling)
- Teaches: [ICTCLD401 PC 3.1] · [ICTCLD401 PC 3.2] · [ICTCLD401 KE 5, 6]
- [AWS ACA M10 S19] Load balancing & scaling
  image: none
- [AWS ACA M07 / M10] The Application Load Balancer
  image: reuse AWS — load balancer → target group → instances
- [AWS ACA M10 S20–S24] Auto Scaling groups
  image: reuse AWS — horizontal scaling with an ASG (ACA M10 S22)
- [BESPOKE] The elasticity you'll build
  image: none
- [DEMO] Create an Auto Scaling policy
  image: none
- [EX] Behind the ALB + ASG — then test scaling
  image: none
- [TAKEAWAYS] Section 2 · Elasticity
  image: none
- [TAKEAWAYS] Topic 8a · Key takeaways
  image: none

### C3 — Managed database (RDS)
- Teaches: [ICTCLD401 PC 2.5] · [ICTCLD401 PC 2.6] · [ICTCLD401 KE 6] · [ICTCLD401 KE 5]
- [BESPOKE] The data tier
  image: none
- [BESPOKE] Databases, and who runs them
  image: none
- [AWS ACF M08 S6–S10] Self-hosted vs managed — EC2 vs RDS
  image: none
- [AWS ACF M08 S8–S29] Amazon RDS
  image: none
- [BESPOKE] The database you'll build
  image: none
- [DEMO] Provision an RDS database
  image: none
- [EX] Provision the Ledgerline database
  image: none
- [TAKEAWAYS] Section 1 · Managed database
  image: none

### C4 — Object & archive storage (S3 + Glacier)
- Teaches: [ICTCLD401 KE 6] · [ICTCLD401 KE 5] · [ICTCLD401 PE 2]
- [AWS ACF M07 S7] Block vs object vs archive
  image: none
- [AWS ACF M07 S22–S34] Amazon S3
  image: none
- [AWS ACF M07 S44–S50] Lifecycle to Glacier — retention
  image: none
- [BESPOKE] The storage you'll build
  image: none
- [DEMO] S3 buckets, versioning & lifecycle
  image: none
- [EX] Create the buckets per the design
  image: none
- [TAKEAWAYS] Section 2 · Object & archive storage
  image: none
- [TAKEAWAYS] Topic 8 · Key takeaways
  image: none

### Close
- [BESPOKE] Next: Topic 8b — the data tier
  image: none
- [BESPOKE] Next: Topic 9 — operability & justification
  image: none

## Build notes
- Reconstructed from `scripts/s1_cl1/build_s1_cl1_topic08*_deck.py`. The deck (.pptx) remains the artefact of record; this plan is the validated source going forward.

## Changelog
- 2026-06-24 — reconstructed from the built deck to the slide-plan format standard.
