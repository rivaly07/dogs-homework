"""Assemble the complete excuse from named parts."""

from .setup import SETUP_PARTS
from .verdict import CLOSING_LINES, DOG_LAW_TWIST


def compose() -> str:
    """Return the dog's one-line excuse."""
    parts = (*SETUP_PARTS, DOG_LAW_TWIST, *CLOSING_LINES)
    return " ".join(parts)
