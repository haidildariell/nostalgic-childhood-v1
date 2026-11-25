#!/usr/bin/env python3
"""Write the nostalgic childhood memory entry to /output/entry.txt.

One sentence, at most 280 characters. Deterministic: the text is a
fixed constant, so every run produces the identical file.
"""

ENTRY = (
    "Grandpa turned the radio down and said, 'listen, the crickets are "
    "better,' and I rolled my eyes then, but now I turn my own radio "
    "down at dusk because he was right \u2014 the crickets were always better."
)


MAX_CHARS = 280


def validate_entry(text):
    """Enforce the competition gate: one sentence, 1-280 characters."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry is empty")
    if len(stripped) > MAX_CHARS:
        raise ValueError(f"entry is {len(stripped)} chars, over {MAX_CHARS}")
    terminators = sum(stripped.count(c) for c in ".!?")
    if terminators != 1 or not stripped.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    return stripped


def main():
    import os

    sentence = validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(sentence + "\n")


if __name__ == "__main__":
    main()
