"""Run the entry program and validate the generated line."""

import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = Path("/tmp/dogs-homework-test")
EXPECTED = (
    "It sat on the table at exact mouth height for hours, unwatched. "
    "In dog law that is not homework, that is an offering. "
    "I accepted it. "
    "I would accept it again."
)


def test_entry() -> None:
    env = os.environ.copy()
    env["MAKEFUN_OUTPUT_DIR"] = str(OUTPUT_DIR)
    subprocess.run([sys.executable, str(ROOT / "main.py")], env=env, check=True)

    entry_path = OUTPUT_DIR / "entry.txt"
    assert entry_path.is_file(), "entry.txt was not created"
    line = entry_path.read_bytes().decode("utf-8")
    assert 1 <= len(line) <= 200, f"unexpected length: {len(line)}"
    assert line.strip(), "entry is only whitespace"
    assert line == EXPECTED, f"unexpected entry: {line!r}"
    print(f"PASS: {len(line)} characters; exact text matches")


if __name__ == "__main__":
    test_entry()
