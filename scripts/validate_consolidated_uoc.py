#!/usr/bin/env python3
"""Validate that consolidated_uoc.md references every PC/FS/PE/KE/AC from each
source UoC exactly once.

Builds the expected inventory by parsing each source .md file:
- PCs: numbered "X.Y" entries inside the Elements and Performance Criteria table
- FSs: skill-name keys in the Foundation Skills table
- PEs/KEs/ACs: top-level bullet items under each section heading

Then parses consolidated_uoc.md for every reference tag of the form
[UNIT SECTION numbering] and reports any item that is missing, duplicated,
or unexpected.
"""

import re
import sys
from collections import Counter
from pathlib import Path

CLUSTER_DIR = Path("/Users/timbaird/Documents/Kangan/diploma-cloud-cyber/S1-CL1-Cloud-Design-Build")
UOC_DIR = CLUSTER_DIR / "assessments" / "units_of_competency"
CONSOLIDATED = CLUSTER_DIR / "consolidated_uoc.md"

UNITS = ["ICTCLD401", "ICTCLD502", "ICTICT517"]


def parse_pcs(md_text: str) -> list[str]:
    """Extract PC numbers (e.g. '1.2') from the Elements and Performance Criteria table."""
    # Find the section between "# Elements and Performance Criteria" and the next "# "
    m = re.search(r"# Elements and Performance Criteria\n(.*?)(?=\n# )", md_text, re.DOTALL)
    if not m:
        return []
    section = m.group(1)
    # PCs in source are split by <br> within table cells, each prefixed "X.Y "
    return re.findall(r"\b(\d+\.\d+)\s+", section)


def parse_fs(md_text: str) -> list[str]:
    """Extract Foundation Skill names from the Foundation Skills table."""
    m = re.search(r"# Foundation Skills\n(.*?)(?=\n# )", md_text, re.DOTALL)
    if not m:
        return []
    section = m.group(1)
    names = []
    for line in section.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        # Skip the header row and separator row
        if re.match(r"\|\s*(SKILL|Skill)\s*\|", line):
            continue
        if re.match(r"\|\s*-+\s*\|", line):
            continue
        # Skip the legend row that starts with "Elements describe" etc.
        # Foundation Skills table doesn't have a legend row but be safe
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) >= 2 and cells[0] and not cells[0].lower().startswith("skill"):
            names.append(cells[0])
    return names


def parse_section_bullets(md_text: str, heading: str) -> int:
    """Count assessable bullets under a heading (PE, KE, AC).

    Normally counts top-level bullets ('- ' with no leading whitespace).
    Special case: if the section has exactly one top-level bullet and that
    bullet ends with ':' (it's a parent like '- For one organisation:'
    with nested children), count the immediate sub-bullets ('  - ') instead.
    This handles ICTICT517 PE.
    """
    pattern = rf"# {re.escape(heading)}\n(.*?)(?=\n# )"
    m = re.search(pattern, md_text, re.DOTALL)
    if not m:
        sections = re.findall(rf"# {re.escape(heading)}\n(.*?)(?=\n# |\Z)", md_text, re.DOTALL)
        if not sections:
            return 0
        section = sections[-1]
    else:
        section = m.group(1)

    lines = section.splitlines()
    top_level = [line for line in lines if re.match(r"^- ", line)]

    if len(top_level) == 1 and top_level[0].rstrip().endswith(":"):
        # Parent-only top-level bullet; count immediate sub-bullets
        sub = [line for line in lines if re.match(r"^  - ", line)]
        return len(sub)

    return len(top_level)


def build_inventory() -> set[str]:
    """Build the expected set of reference tags from the source UoCs."""
    expected = set()
    for unit in UNITS:
        md = (UOC_DIR / f"{unit}_Complete_R1.md").read_text(encoding="utf-8")
        for pc in parse_pcs(md):
            expected.add(f"{unit} PC {pc}")
        for fs in parse_fs(md):
            expected.add(f"{unit} FS {fs}")
        for n in range(1, parse_section_bullets(md, "Performance Evidence") + 1):
            expected.add(f"{unit} PE {n}")
        for n in range(1, parse_section_bullets(md, "Knowledge Evidence") + 1):
            expected.add(f"{unit} KE {n}")
        for n in range(1, parse_section_bullets(md, "Assessment Conditions") + 1):
            expected.add(f"{unit} AC {n}")
        # AC also includes the trailing assessor-requirements paragraph
        # which we numbered as the last AC item (e.g. AC 5 for 401, AC 9 for
        # 502, AC 6 for 517). Add one extra per unit to account for that.
        last_ac = parse_section_bullets(md, "Assessment Conditions") + 1
        expected.add(f"{unit} AC {last_ac}")
    return expected


def extract_refs(text: str) -> list[str]:
    """Pull every reference tag from the consolidated doc.

    Skips backtick-wrapped tags (those are documentation examples in the
    preamble, not real references).
    """
    # Strip inline code spans (single-backtick content) before extracting
    cleaned = re.sub(r"`[^`]*`", "", text)
    return re.findall(r"\[(ICT\w+|BSB\w+|VU\d+) (PC|FS|PE|KE|AC) ([^\]]+)\]", cleaned)


def main():
    expected = build_inventory()
    consolidated = CONSOLIDATED.read_text(encoding="utf-8")
    raw_refs = extract_refs(consolidated)
    found = [f"{u} {s} {n}" for u, s, n in raw_refs]
    counts = Counter(found)

    found_set = set(found)
    missing = sorted(expected - found_set)
    unexpected = sorted(found_set - expected)
    duplicated = sorted([(ref, c) for ref, c in counts.items() if c > 1])

    print(f"Expected items:   {len(expected)}")
    print(f"Found references: {len(found)} ({len(found_set)} unique)")
    print()

    if missing:
        print(f"MISSING ({len(missing)}):")
        for ref in missing:
            print(f"  - {ref}")
        print()

    if unexpected:
        print(f"UNEXPECTED ({len(unexpected)}):")
        for ref in unexpected:
            print(f"  - {ref}  (count={counts[ref]})")
        print()

    if duplicated:
        print(f"DUPLICATED ({len(duplicated)}):")
        for ref, c in duplicated:
            print(f"  - {ref}  ({c} times)")
        print()

    if not missing and not unexpected and not duplicated:
        print("RESULT: PASS — every expected item appears exactly once, nothing extra.")
        sys.exit(0)
    else:
        print("RESULT: FAIL")
        sys.exit(1)


if __name__ == "__main__":
    main()
