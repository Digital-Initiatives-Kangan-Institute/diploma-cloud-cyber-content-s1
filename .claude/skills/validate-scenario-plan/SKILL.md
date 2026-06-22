---
name: validate-scenario-plan
version: 1.0.0
updated: 2026-06-22
model: claude-haiku-4-5-20251001
description: >-
  This skill should be used to confirm a scenario plan satisfies its scenario's assessment contract —
  e.g. "validate the scenario plan", "does the scenario cover every SR", "run the scenario cross-check", or
  at run-sheet Gate 6→7. It runs validate_scenario_plan.py: it lints the scenario plan against the format
  standard (required sections, header binding, per-element 'Satisfies:' fields, well-formed SE-NN ids) and
  cross-checks it against the consolidated assessment plan's SR-* register — asserting every SR-* is
  satisfied by at least one scenario element (UNCOVERED → fail) and no element claims a non-existent SR-*
  (PHANTOM → fail). Use it whenever a scenario plan must be confirmed against its SR-* contract.
---

# Validate scenario plan

The scenario plan (`scenario-plans/<SEMESTER>.md`) is the **authored** bridge between the assessment
contract and the in-world world: it maps every `SR-*` in the **consolidated assessment plan**
(`assessment-plans/<SEMESTER>.md`) to the concrete scenario element that provides it (see
`docs/scenario-plan-format.md`). This skill is the machine condition for run-sheet **Gate 6→7**.

## When to use

- After authoring/updating a scenario plan, to confirm it satisfies the whole `SR-*` contract (Gate 6→7).
- Whenever the consolidated assessment plan changed (an `SR-*` was added/removed), to catch a scenario plan
  that no longer covers the contract.
- To detect an element claiming a stale or mistyped `SR-*` (phantom).

## The validator

`validate_scenario_plan.py` (bundled at `.claude/skills/scripts/`) runs two phases:

- **FORMAT** — required sections present + in order; header carries STATUS + Assessment-binding; §2 has an
  element table and per-element `### SE-NN` blocks each with a `Satisfies:` field; SE ids well-formed.
- **CROSS-CHECK** — reads the `SR-*` register from the consolidated assessment plan and the `Satisfies:`
  lines from the scenario plan, then asserts bidirectionally: every register `SR-*` is satisfied by ≥1
  element (**UNCOVERED** otherwise), and every claimed `SR-*` exists in the register (**PHANTOM** otherwise).
  An element satisfying no `SR-*` is reported **info** (allowed world-building).

Stdlib only.

## How to run it

```bash
python3 .claude/skills/scripts/validate_scenario_plan.py --semester S1
```

- `--semester` — defaults the plan to `scenario-plans/<SEMESTER>.md` and the contract to
  `assessment-plans/<SEMESTER>.md` (override with `--plan` / `--consolidated`).

Exit `0` on PASS (format valid AND every `SR-*` satisfied, no phantoms), `1` otherwise. On an UNCOVERED
failure, add or bind a scenario element; on PHANTOM, fix the `Satisfies:` id (or regenerate the consolidated
plan if the register genuinely changed).

## Portability

Self-contained: stdlib-only, in `.claude/skills/scripts/`; needs only the scenario plan + the consolidated
assessment plan.
