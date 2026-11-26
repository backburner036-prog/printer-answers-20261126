"""Entry for make.fun bounty "The Printer Finally Answers".

One line in the office printer's own voice: the thump, the paper jam,
the cryptic error code — and the comeback lands on the last words:
the human hits the machine and calls it troubleshooting.
"""

from pathlib import Path

TEXT = "THUMP. Paper jam. Error 51: I need a human — preferably one who doesn't hit me and call it troubleshooting."

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=240):
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    # One-line bounty: the joke must stay a single line, so any newline
    # (e.g. from an accidental edit) is rejected here, not at the judge.
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    return size


def check_single_line(text):
    # Helper: the entry must read as one breath — beats separated by
    # full stops, never a second sentence that explains the joke.
    assert text.count(".") >= 2, "entry needs its beats in one line"
    assert text == text.strip(), "no leading/trailing whitespace"
    return True


def save_line(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    check_len(TEXT)
    check_single_line(TEXT)
    save_line(OUT, TEXT)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == TEXT, "round-trip mismatch"
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()
