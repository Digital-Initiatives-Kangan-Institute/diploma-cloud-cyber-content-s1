---
name: inspect-deck
version: 1.0.0
updated: 2026-06-14
model: claude-haiku-4-5-20251001
description: >-
  This skill should be used to check a slide deck's size and find what's driving it before
  committing it — e.g. "check the deck size", "is this pptx too big", "what's making Topic_07 so
  large", "deck bloat / hygiene check", "inspect the deck before I commit it", or after generating
  or editing a teaching deck. It runs a deterministic check (the bundled inspect_deck.py) that
  reports the on-disk size, the largest internal entries, and embedded media grouped by type, and
  fails if the deck exceeds a size guideline. Teaching decks are git-tracked (the instructor-to-
  instructor channel), so keeping them small matters. Use it whenever a deck's size needs checking,
  even if the user does not name the script. Works on any Office/zip file (.pptx, .docx, .xlsx).

---

# Inspect a deck's size before committing

Teaching decks are tracked in git so instructors can share them, which means they need to stay small
enough for plain git. Bloat usually rides in on pasted slides — uncompressed images, an embedded
video, dragged-in masters. This skill shows the on-disk size and exactly which internal objects are
driving it, and gates on a size guideline, so a heavy deck is caught and trimmed before it lands.

## When to use

- After generating or editing a Topic deck, before committing it.
- When a `.pptx` (or any Office file) seems unexpectedly large and you need to find the culprit.
- As a pre-commit hygiene gate for any tracked deck.

## How to run it

```bash
python3 .claude/skills/scripts/inspect_deck.py <deck.pptx> [--warn-mb 25] [--top 15]
```

- `<deck>` — the `.pptx` (or `.docx`/`.xlsx`/any zip) to inspect.
- `--warn-mb` — the size guideline; the check fails (exit 1) if the deck on disk exceeds it. Default
  25 MB.
- `--top` — how many largest internal entries to list. Default 15.

Exit `0` if within the guideline, `1` if over — so it can act as a pre-commit gate.

## Interpreting the result

- **On disk / uncompressed total** — the headline size and how much it expands to.
- **Largest internal entries** — the specific files (usually `ppt/media/imageNN.*`) eating the
  space; this is where to look first.
- **Embedded media by type** — the culprit category at a glance (e.g. several large `.tiff` or
  uncompressed `.png`, or an embedded video/audio).
- **OK / WARNING** — within or over the guideline.

If it WARNs, trim before committing — typically PowerPoint → Compress Pictures (whole deck, 150 ppi,
delete cropped areas), or drop the offending object identified above — then re-run until it reports
OK. Don't assume the cause; the report names it, and it won't be the same object every time.

## Portability

Self-contained and stdlib-only, so the whole `.claude/skills/` folder works in any course repo. It
inspects any Office/zip file, so it is not specific to this project's decks.
