"""
psi-aligned counting table for n = 3 .. 30.

Outputs a TSV with:
- the crystallographic clock psi(n),
- the six-field per-polygon contributions,
- word-length and non-2 increments,
- exact per-polygon corner hits on X in {+1, +1/2, 0, -1/2, -1}.
"""

import csv
import os

from mpmath import mp

from counting_utils import multiplicity_word


N_MIN = 3
N_MAX = 30
HIT_TOL = mp.mpf("1e-40")
CONTOUR_LEVELS = (-1, mp.mpf("-0.5"), 0, mp.mpf("0.5"), 1)


def psi_value(n):
    if n == 1 or n == 2:
        return 0
    total = 0
    remaining = n
    p = 2
    while p * p <= remaining:
        if remaining % p == 0:
            exp = 0
            while remaining % p == 0:
                remaining //= p
                exp += 1
            total += psi_prime_power(p, exp)
        p = 3 if p == 2 else p + 2
    if remaining > 1:
        total += psi_prime_power(remaining, 1)
    return total


def psi_prime_power(p, exp):
    if p == 2:
        if exp == 1:
            return 0
        return 2 ** (exp - 1)
    return (p ** exp) - (p ** (exp - 1))


def leading_one(n):
    return 1 if n % 2 == 1 else 0


def x_minus_one(n):
    return 2 if n % 2 == 0 else 0


def x_zero(n):
    return 2 if (n >= 6 and n % 4 == 2) else 0


def left_field(n):
    if n % 2 == 1:
        return (n - 1) // 4
    if n % 4 == 0:
        return (n - 4) // 4
    return (n - 6) // 4


def right_field(n):
    if n % 2 == 1:
        return (n - 3) // 4
    if n % 4 == 0:
        return (n - 4) // 4
    return (n - 6) // 4


def x_plus_one(_n):
    return 2


def contour_hits(n):
    hits = {level: 0 for level in CONTOUR_LEVELS}
    radius = 1 / mp.cos(mp.pi / n)
    for k in range(n):
        theta = (2 * k + 1) * mp.pi / n
        x = radius * mp.cos(theta)
        for level in CONTOUR_LEVELS:
            if abs(x - level) < HIT_TOL:
                hits[level] += 1
    return hits


def build_rows():
    rows = []
    prev_length = 0
    prev_non2 = 0
    for n in range(N_MIN, N_MAX + 1):
        counts, _ = multiplicity_word(n)
        length = len(counts)
        non2_total = sum(1 for value in counts if value != 2)
        hits = contour_hits(n)
        row = {
            "n": n,
            "psi": psi_value(n),
            "word_length": length,
            "word_length_increment": length - prev_length,
            "non2_total": non2_total,
            "non2_increment": non2_total - prev_non2,
            "leading_1": leading_one(n),
            "x=-1": x_minus_one(n),
            "x=-1/2": hits[mp.mpf("-0.5")],
            "L(n)": left_field(n),
            "x=0": x_zero(n),
            "R(n)": right_field(n),
            "x=+1/2": hits[mp.mpf("0.5")],
            "x=+1": x_plus_one(n),
        }
        rows.append(row)
        prev_length = length
        prev_non2 = non2_total
    return rows


def write_tsv(rows, outpath):
    fieldnames = [
        "n",
        "psi",
        "word_length",
        "word_length_increment",
        "non2_total",
        "non2_increment",
        "leading_1",
        "x=-1",
        "x=-1/2",
        "L(n)",
        "x=0",
        "R(n)",
        "x=+1/2",
        "x=+1",
    ]
    with open(outpath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    rows = build_rows()
    out = os.path.join(here, "psi_counting_table.tsv")
    write_tsv(rows, out)
    print(f"wrote {out}")
