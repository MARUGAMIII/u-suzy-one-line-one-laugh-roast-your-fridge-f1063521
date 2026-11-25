#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge -- make.fun entry.

Writes a single roast of the entrant's fridge to /output/entry.txt
(or $OUTPUT_DIR/entry.txt when set, for local testing).

The joke: the fridge's late-night hum is the setup -- every owner
knows that low buzz at 3 a.m. -- and the turn is that the hum is
the fridge calling the leftovers to gossip about its owner. The
payoff lands in the last few words: "apparently I'm why nothing in
here stays fresh" blames the owner for the food going off, which is
the fridge's own job. Specific detail (the 3 a.m. hum), one line,
plain ASCII, no setup that needs a second sentence.

Python standard library only. Deterministic: the same line every run.
"""

import os

# Words anchoring the line to a fridge itself (its hum, its leftovers,
# what it keeps) -- the judge brief's first criterion. The entry must
# name at least one.
FRIDGE_KEYWORDS = ("fridge", "hum", "leftovers", "fresh")

ENTRY = (
    "My fridge hums at 3 a.m. like it's calling the leftovers to gossip "
    "about me, and apparently I'm why nothing in here stays fresh."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry length {len(text)} out of range 1-200")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text.isascii():
        raise SystemExit("entry must be plain ASCII")
    lowered = text.lower()
    if not any(word in lowered for word in FRIDGE_KEYWORDS):
        raise SystemExit(
            "entry must name a fridge concept "
            "(fridge, hum, leftovers or fresh)"
        )
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
