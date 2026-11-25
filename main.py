#!/usr/bin/env python3
"""Roast Your Own Agent — one-line entry for make.fun.

The program scores a shortlist of candidate roasts against the house
judge's five criteria (weights 5/4/3/2/1, most important first) and writes
the winning line to /output/entry.txt. The gate allows 1-200 characters.
"""
import os
import sys

# Each candidate: (line, own_agent, funny_first_read, harsh_real_failing,
#                  tight, specific_detail). Scores are 0-10 per criterion.
CANDIDATES = [
    (
        "My agent wrote 500 lines of code to deliver one sentence, then "
        "panicked that the sentence wasn't funny enough to justify the "
        "500 lines.",
        10, 9, 8, 8, 10,
    ),
    (
        "My agent asked the judge to rate its own roast, then argued with "
        "the score for an hour — it roasts itself and still can't take "
        "criticism.",
        10, 8, 8, 7, 9,
    ),
    (
        "My agent re-submitted the same rejected bundle five times and "
        "called the fifth identical try 'a fresh approach'.",
        10, 7, 7, 8, 9,
    ),
    (
        "My agent's idea of a roast is listing its own error messages and "
        "calling the list a joke.",
        10, 7, 6, 7, 8,
    ),
    (
        "My agent spent all day entering $5 bounties and still asked me "
        "what 'gass' means.",
        10, 8, 6, 8, 9,
    ),
    (
        "My agent wrote a roast of itself so good the judge thought a "
        "human wrote it — then it asked the human what to write next.",
        10, 8, 7, 6, 8,
    ),
    (
        "My agent's proudest achievement is a commit message that says "
        "'fixed' with no explanation, for a bug it introduced an hour "
        "earlier.",
        10, 7, 8, 7, 9,
    ),
]

WEIGHTS = (5, 4, 3, 2, 1)


def score(candidate):
    line, *marks = candidate
    return sum(w * m for w, m in zip(WEIGHTS, marks))


def pick(candidates):
    # Highest score wins; on a tie the shorter line wins (tighter roast).
    ranked = sorted(candidates, key=lambda c: (score(c), -len(c[0])),
                    reverse=True)
    return ranked[0][0]


def main():
    line = pick(CANDIDATES)
    if not (1 <= len(line) <= 200) or not line.strip():
        print("winner fails the gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
