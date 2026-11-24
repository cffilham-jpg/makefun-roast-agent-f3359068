"""Write the roast entry to entry.txt.

The entry is one short line roasting the entrant's own AI agent. It is
written exactly as-is, with no trailing newline, to entry.txt inside the
directory named by MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
import unicodedata

ENTRY = "My agent hallucinated a function, imported it, called it, and then apologized to the error message."


def validate(text):
    """Return True only if text is a valid single-line entry.

    A valid entry is a string of 1-200 characters, on one line, not only
    whitespace, with no leading or trailing whitespace, and free of
    Unicode control, format, line-separator and paragraph-separator
    characters.
    """
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= 200:
        return False
    if not text.strip():
        return False
    if text != text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    for ch in text:
        if unicodedata.category(ch) in ("Cc", "Cf", "Zl", "Zp"):
            return False
    return True


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    if not validate(ENTRY):
        raise SystemExit("entry failed validation")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
