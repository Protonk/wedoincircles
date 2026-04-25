"""Verify GPT-5's closed-form conjecture for Δ|M_n|.

Conjecture:
    odd n:         Δ|M_n| = (n - 1) / 2
    n ≡ 0 mod 4:   Δ|M_n| = (n - 4) / 2
    n ≡ 2 mod 4:   Δ|M_n| = (n - 6) / 2        (with n = 6 flagged special)

Computes |M_n| directly via counting_utils.multiplicity_word for n in
[3, N_MAX] and reports any mismatch.
"""

import os

from counting_utils import multiplicity_word


N_MAX = 40


def predicted_increment(n):
    if n % 2 == 1:
        return (n - 1) // 2
    if n % 4 == 0:
        return (n - 4) // 2
    return (n - 6) // 2


def main():
    lengths = {}
    for n in range(3, N_MAX + 1):
        counts, _ = multiplicity_word(n)
        lengths[n] = len(counts)

    rows = []
    mismatches = []
    for n in range(4, N_MAX + 1):
        actual = lengths[n] - lengths[n - 1]
        predicted = predicted_increment(n)
        residue = ("odd" if n % 2 else "0 mod 4" if n % 4 == 0 else "2 mod 4")
        match = "OK" if actual == predicted else "MISS"
        rows.append((n, residue, lengths[n], actual, predicted, match))
        if actual != predicted:
            mismatches.append((n, residue, actual, predicted))

    width = 78
    print("n  residue   |M_n|  Δ|M_n|  predicted  status")
    print("-" * width)
    for n, residue, length, actual, predicted, match in rows:
        print(f"{n:>2}  {residue:<8}  {length:>4}     {actual:>3}        {predicted:>3}    {match}")

    print()
    if not mismatches:
        print(f"All increments n=4..{N_MAX} match the closed-form formula.")
    else:
        print(f"Mismatches at n in {[m[0] for m in mismatches]}:")
        for n, residue, actual, predicted in mismatches:
            print(f"  n={n} ({residue}): actual={actual}, predicted={predicted}")


if __name__ == "__main__":
    main()
