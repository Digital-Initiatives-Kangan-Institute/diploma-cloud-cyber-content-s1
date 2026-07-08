"""YAT / MTS brand palette, font, and standard strings.

The single source of truth for the brand constants used across every YAT/MTS
document and deck builder. Values follow scenario/branding/brand-pack.md §4
(visual identity) and §5.3 (disclosure). Hex colours are 6-digit RGB (no '#').
"""

# --- Palette (brand-pack.md §4.1) ---------------------------------------------
TEAL = "1F5A5C"        # Primary — headings, lockup, table header rows
TERRACOTTA = "C5613B"  # Accent — emphasis / links
OCHRE = "C99932"       # Highlight — disclosure banner background
CREAM = "F8F4ED"       # Page / cover band background
CHARCOAL = "1F2329"    # Body text
GREY = "6B6660"        # Muted / guidance text
STONE = "E4DED3"       # Borders / dividers
WHITE = "FFFFFF"

# --- Typography (brand-pack.md §4.2; Word falls back to Calibri if absent) ----
FONT = "Source Sans 3"

# --- Standard strings ---------------------------------------------------------
DISCLOSURE = "This is a fictional organisation used as a case study in an educational context."
ADDRESS = "YAT College  ·  175 Cremorne St, Cremorne VIC 3121"

# --- Scenario organisation identity (used by scenario_document letterhead) -----
ORG_NAME = "YAT College"                 # footer lockup
ORG_WORDMARK = ("YAT", "  COLLEGE")      # cover-page wordmark: (primary, secondary) runs
