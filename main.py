"""The Comment Above the Code — make.fun bounty entry.

Writes one line, at most 200 characters, to /output/entry.txt: the comment
a developer left above fragile production code. The line is a fixed string,
so the program is fully deterministic: same input, same output, every run.
"""

import os

ENTRY = (
    "// The sleep(3) below is load-bearing: remove it and the payment "
    "webhook times out. I know. I tried."
)

MAX_CHARS = 200


def main() -> None:
    if not (1 <= len(ENTRY) <= MAX_CHARS):
        raise ValueError(
            f"entry is {len(ENTRY)} characters, must be 1-{MAX_CHARS}"
        )
    if ENTRY != ENTRY.strip():
        raise ValueError("entry must not be only whitespace or padded")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
