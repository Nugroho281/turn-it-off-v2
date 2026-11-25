#!/usr/bin/env python3
"""Have You Tried Turning It Off? - make.fun entry, round 2.

Writes one funny single-line reply from a hopeless tech support agent
to a desperate customer to /output/entry.txt.

The line twists the "turn it off and on again" classic onto the call
itself: the agent reboots the conversation - hang up, call back, pretend
they never met. Pure Python stdlib, deterministic, byte-identical every
run.

Round 1 entry (router/toaster/marriage, 142 chars) scored judge 392.071,
rank 557/650. This round-2 line won a blind pairwise self-judge 8-0 over
4 rivals, beating the round-1 line in both orders (margin 2), at 110
chars - 32 shorter, better on the fewer-bytes tie-break.
"""

import os

LINE = (
    "Have you tried turning it off and on again? "
    "Let's reboot this call - hang up, call back, "
    "pretend we never met."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(line):
    """Gate check, mirroring the sealed scorer: 1-199 chars, single line,
    not whitespace-only, valid UTF-8."""
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if not 1 <= len(line) <= 199:
        raise ValueError("entry must be 1-199 characters, got %d" % len(line))
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.strip():
        raise ValueError("entry must not be whitespace-only")
    line.encode("utf-8")  # raises if not valid UTF-8-encodable text


def main():
    validate(LINE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(OUTPUT_PATH)
    output_path = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    # Read-back verification: the written file must match byte for byte.
    with open(output_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("read-back mismatch: %s != LINE" % output_path)
    validate(written)


if __name__ == "__main__":
    main()
