"""Tests for helpers.yat_brand — the brand constants."""
import pathlib
import re
import sys

sys.path.insert(0, str(next(
    d for d in pathlib.Path(__file__).resolve().parents
    if (d / "helpers" / "__init__.py").exists()
)))

from helpers import yat_brand  # noqa: E402

HEX = ("TEAL", "TERRACOTTA", "OCHRE", "CREAM", "CHARCOAL", "GREY", "STONE", "WHITE")


def test_palette_values_are_six_digit_hex():
    for name in HEX:
        value = getattr(yat_brand, name)
        assert re.fullmatch(r"[0-9A-F]{6}", value), f"{name}={value!r} not 6-digit RGB hex"


def test_known_palette_anchors():
    assert yat_brand.TEAL == "1F5A5C"
    assert yat_brand.WHITE == "FFFFFF"


def test_font_and_strings_present():
    assert yat_brand.FONT
    assert "fictional organisation" in yat_brand.DISCLOSURE
    assert yat_brand.ADDRESS.startswith("YAT College")
