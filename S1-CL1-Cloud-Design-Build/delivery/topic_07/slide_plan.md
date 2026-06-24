# Topic 07 Network & security base — Slide plan
> **Covers:** Topic 07 — see coverage.md
> **STATUS: RECONSTRUCTED** from the built deck (Network & security base); structure + image sources + per-component Teaches are authoritative, slide briefs were not recoverable from the deck.

## Depth ceiling
As built — see coverage.md for the AT depth ceiling.

## Teaching source
As built (see coverage.md header).

## AWS pin table
As pinned in the build (AWS refs carried on each slide's type tag where applicable).

## Slides

### Opener
- [BESPOKE] Continuing the build
  image: none

### C1 — Virtual network & subnets (VPC)
- Teaches: [ICTCLD401 PC 2.2] · [ICTCLD401 KE 5] · [ICTCLD401 PE 1]
- [AWS ACF M05 S5–S9] Networking, the essentials
  image: reuse AWS — IP address / CIDR (ACF M05 S6 / S8)
- [AWS ACF M05 S11] The VPC — your private network in AWS
  image: none
- [AWS ACA M07 S12–S16] Routing: gateways & route tables
  image: reuse AWS — VPC anatomy: subnets · IGW · NAT · route tables (ACA M07 S16)
- [EX] Public or private?
  image: none
- [BESPOKE] The network you'll build
  image: none
- [TAKEAWAYS] Section 1 · The virtual network
  image: none

### C2 — Controlling traffic (security groups)
- Teaches: [ICTCLD401 KE 9] · [ICTCLD401 PE 1]
- [AWS ACA M07 S23] What a firewall does
  image: none
- [AWS ACF M05 S33–S35] Security groups
  image: none
- [TABLE] The design's security groups
  image: none
- [DEMO] Build a VPC and its security groups
  image: none
- [EX] Build the network fabric
  image: none

### C3 — Name resolution & connectivity (DNS + testing)
- Teaches: [ICTCLD401 PC 2.6] · [ICTCLD401 KE 10] · [ICTCLD401 PE 3]
- [AWS ACF M05 S49–S50] How DNS works — and Route 53
  image: reuse AWS — Route 53 DNS resolution flow (ACF M05 S50)
- [BESPOKE] The design's name & certificate
  image: none
- [AWS ACA M07 S45, S41] Prove it works — test connectivity
  image: none
- [DEMO] Create a DNS record & test reachability
  image: none
- [EX] Configure DNS + test connectivity
  image: none
- [TAKEAWAYS] Section 3 · Names & connectivity
  image: none
- [TAKEAWAYS] Topic 7 · Key takeaways
  image: none

### Close
- [BESPOKE] Next: Topic 8 — the workload tier
  image: none

## Build notes
- Reconstructed from `scripts/s1_cl1/build_s1_cl1_topic07*_deck.py`. The deck (.pptx) remains the artefact of record; this plan is the validated source going forward.

## Changelog
- 2026-06-24 — reconstructed from the built deck to the slide-plan format standard.
