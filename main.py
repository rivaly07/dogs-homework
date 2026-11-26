"""Write the assembled excuse to the configured output directory."""

import os
from pathlib import Path

from excuse.compose import compose


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry = compose()
    (output_dir / "entry.txt").write_text(entry, encoding="utf-8")


if __name__ == "__main__":
    main()
