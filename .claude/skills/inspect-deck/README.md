# inspect-deck · v1.0.0 (updated 2026-06-14)

## Purpose
Check a slide deck's on-disk size and find **exactly what's bloating it** before committing it.
Teaching decks are git-tracked (the instructor-to-instructor channel), so they must stay small;
this catches a heavy deck and names the culprit so it can be trimmed before it lands.

## Prerequisites
- `python3` on PATH — **standard library only** (no venv, no `pip install`).
- Shared script in `.claude/skills/scripts/`: **`inspect_deck.py`**.
- A target **Office/zip file** to inspect (`.pptx`, `.docx`, `.xlsx`, or any zip).

## Inputs & outputs
- **In:** the deck/Office file (and optional `--warn-mb`, `--top`).
- **Out:** a report — on-disk + uncompressed size, largest internal entries (usually
  `ppt/media/imageNN.*`), embedded media grouped by type, and `OK`/`WARNING`. **Exit 0** within
  the guideline, **1** over (so it works as a pre-commit gate).

## How it works
```bash
python3 .claude/skills/scripts/inspect_deck.py <deck.pptx> [--warn-mb 25] [--top 15]
```
Unzips the Office file, tallies entry sizes, and gates on `--warn-mb` (default 25 MB). If it
WARNs, trim (PowerPoint → Compress Pictures @150 ppi / drop the named object) and re-run until OK.
Don't guess the cause — the report names it, and it varies deck to deck.

## Version history
- **v1.0.0 (2026-06-14)** — initial documented version.
