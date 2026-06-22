# validate-scenario-plan · v1.0.0 (2026-06-22)

## Purpose
Prove a scenario's **scenario plan** satisfies its **assessment contract** — the machine condition for
run-sheet **Gate 6→7**. The consolidated assessment plan ends in an `SR-*` register (everything the world
must provide); this confirms the scenario plan binds a concrete element to every one of them, and that no
element points at an `SR-*` that does not exist.

## Prerequisites
- **Python 3** on PATH — standard library only.
- Shared script `.claude/skills/scripts/validate_scenario_plan.py`.
- The scenario plan `scenario-plans/<SEMESTER>.md` + the consolidated `assessment-plans/<SEMESTER>.md`.

## Inputs & outputs
- **In:** `--semester <S>` (defaults both paths; override with `--plan` / `--consolidated`).
- **Out:** PASS, or FORMAT issues + `UNCOVERED` / `PHANTOM` cross-check discrepancies. **Exit 0** when the
  format is valid and every `SR-*` is satisfied with no phantom.

## How it works
Lints the scenario plan against `docs/scenario-plan-format.md` (sections, header binding, per-element
`Satisfies:` fields, SE-NN ids), then reads the `SR-*` register from the consolidated assessment plan and
the elements' `Satisfies:` lines and compares them as sets, both directions.

## Version history
- **v1.0.0 (2026-06-22)** — initial version. Built for run-sheet Gate 6; proven on S1.
