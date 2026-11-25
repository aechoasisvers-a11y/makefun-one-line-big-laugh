"""One Line, Big Laugh — make.fun entry.

Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
not only white space. This entry is 99 characters.
"""

import os

ENTRY = "I finally got a job that pays me to sleep \u2014 it's called unemployment, and the only benefit is naps."


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(ENTRY)}")
    if not ENTRY.strip():
        raise ValueError("entry must not be only white space")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
