# Topic 12 HA design — Slide plan
> **Covers:** Topic 12 — see coverage.md
> **STATUS: RECONSTRUCTED** from the built deck (HA design); structure + image sources + per-component Teaches are authoritative, slide briefs were not recoverable from the deck.

## Depth ceiling
As built — see coverage.md for the AT depth ceiling.

## Teaching source
As built (see coverage.md header).

## AWS pin table
As pinned in the build (AWS refs carried on each slide's type tag where applicable).

## Slides

### Opener
- [BESPOKE] Now you design it
  image: none

### C1 — Review the baseline & find its SPOFs
- Teaches: [ICTCLD502 PC 2.1] · [ICTCLD502 PC 2.2] · [ICTCLD502 PC 2.3] · [ICTCLD502 PC 2.4] · [ICTCLD502 PC 2.5] · [ICTCLD502 KE 4, 8]
- [BESPOKE] Review the architecture
  image: none
- [BESPOKE] Identify the single points of failure
  image: reuse Identify-SPoFs network diagram (ICTCLD502 · Design HA S10)
- [BESPOKE] Estimate the recovery objectives
  image: none
- [EX] Review the Accounting baseline
  image: none
- [TAKEAWAYS] Section 1 · Review & SPOFs
  image: none

### C2 — Design the HA-equivalent
- Teaches: [ICTCLD502 PC 3.1] · [ICTCLD502 PC 3.2] · [ICTCLD502 PC 3.3] · [ICTCLD502 PC 3.4] · [ICTCLD502 KE 4, 8]
- [BESPOKE] Design redundancy — remove the SPoFs
  image: none
- [AWS ACA M10 S41] The cross-AZ HA architecture
  image: reuse Cross-AZ HA architecture — ALB + ASG + Multi-AZ RDS (ACA M10 S41)
- [BESPOKE] Remove each SPOF — the mapping
  image: none
- [BESPOKE] Re-estimate the recovery objectives
  image: none
- [EX] Design the HA-equivalent for Accounting
  image: none
- [TAKEAWAYS] Section 2 · Design
  image: none

### C3 — Document the design & plan the work
- Teaches: [ICTCLD502 PC 2.5] · [ICTCLD502 PC 3.5] · [ICTCLD502 KE 4, 8]
- [BESPOKE] What an HA design documents
  image: none
- [BESPOKE] Draw the HA topology
  image: none
- [BESPOKE] Plan the implementation & simulation
  image: none
- [EX] Produce your HA design document
  image: none
- [TAKEAWAYS] Section 3 · Document & plan
  image: none
- [TAKEAWAYS] Topic 12 · Key takeaways
  image: none

### Close
- [BESPOKE] Next: Topic 13 — HA implementation & simulation
  image: none

## Build notes
- Reconstructed from `scripts/s1_cl1/build_s1_cl1_topic12*_deck.py`. The deck (.pptx) remains the artefact of record; this plan is the validated source going forward.

## Changelog
- 2026-06-24 — reconstructed from the built deck to the slide-plan format standard.
