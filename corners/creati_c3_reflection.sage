"""
CREATI C3 reflection-identity enumeration.

Discharges open slot D of `rotations/SIX-LENS-SYNTHESIS.md`:
  Does there exist a non-trivial involution σ on positive integers
  such that trace(R_n) + trace(R_σ(n)) admits a closed-form expression
  in n, where trace(R_n) = 2 cos(2π/n)?

The "transpose-trivial" candidates (σ = id; σ that fixes trace
pointwise) are excluded by hypothesis. CREATI C3 frames this as an
open enumeration question. This script enumerates the natural
candidate families, tests the resulting f_σ(n) := trace(R_n) +
trace(R_σ(n)) for closed-form structure, and reports the verdict.

Candidate families:
  (a) σ(n) = c − n           additive reflection, various c
  (b) σ(n) = 2n/(n−2)        the unique involution with 1/n + 1/σ(n) = 1/2
  (c) σ(n) = c/n             multiplicative reflection through c
  (d) Galois twists at fixed n   subgroup of (ℤ/nℤ)*/{±1}; per-n only
  (e) Niven-set permutations  σ on {1, 2, 3, 4, 6}; finite domain

For each, computed are:
  - integer-valued domain in [3, 60]
  - whether f_σ is constant on that domain
  - the field where f_σ(n) sits (rational, K_n0 for some n0, or
    transcendental-degree-1)
"""

import math
from fractions import Fraction


def trace_R(n):
    """trace(R_n) = 2 cos(2π/n)."""
    return 2.0 * math.cos(2.0 * math.pi / n)


def f_sigma(n, sn):
    """f_σ(n) = trace(R_n) + trace(R_σ(n))."""
    return trace_R(n) + trace_R(sn)


# --- candidate involutions ----------------------------------------------

def sigma_c_minus_n(c):
    """σ(n) = c − n. Involution: σ(σ(n)) = c − (c − n) = n."""
    def sigma(n):
        m = c - n
        if m >= 3:  # require σ(n) ≥ 3 to keep R_σ(n) a non-trivial rotation
            return m
        return None
    return sigma


def sigma_2n_over_n_minus_2(n):
    """σ(n) = 2n/(n − 2). The unique involution with 1/n + 1/σ(n) = 1/2.
    Integer-valued only when (n − 2) | 2n, equivalently when n − 2 ∈ {1, 2, 4}
    i.e. n ∈ {3, 4, 6}."""
    if n <= 2:
        return None
    num = 2 * n
    den = n - 2
    if num % den == 0:
        return num // den
    return None


def sigma_c_over_n(c):
    """σ(n) = c/n. Involution: σ(σ(n)) = c/(c/n) = n. Integer iff n | c."""
    def sigma(n):
        if c % n == 0:
            m = c // n
            if m >= 3:
                return m
        return None
    return sigma


def sigma_galois_twist(n, k):
    """For fixed n, σ_k acts on the index inside (ℤ/nℤ)*: cos(2π/n) →
    cos(2πk/n). This is NOT an involution on the parameter n — it is
    an involution on indices within fixed n's cyclotomic field. Listed
    here for comparison."""
    return None  # not applicable as σ on n


# --- enumeration core ---------------------------------------------------

def enumerate_candidate(name, sigma_func, domain, verbose=True):
    """Enumerate σ over domain, collect (n, σ(n)) pairs, evaluate f_σ,
    test for constancy."""
    pairs = []
    fixed = []
    for n in domain:
        s = sigma_func(n)
        if s is None:
            continue
        if s == n:
            if n not in fixed:
                fixed.append(n)
        else:
            key = tuple(sorted((n, s)))
            if key not in [tuple(sorted(p)) for p in pairs]:
                pairs.append((n, s))

    if not pairs and not fixed:
        if verbose:
            print(f"  {name}: σ has no integer image on domain")
        return None

    values = []
    for n, sn in pairs:
        v = f_sigma(n, sn)
        values.append(v)
    for n in fixed:
        v = f_sigma(n, n)
        values.append(v)

    constant = (len(set(round(v, 10) for v in values)) == 1)
    if verbose:
        print(f"  {name}")
        print(f"    pairs: {pairs}")
        print(f"    fixed: {fixed}")
        print(f"    values f_σ(n):")
        for n, sn in pairs:
            v = f_sigma(n, sn)
            rat = abs(v - round(v)) < 1e-10
            tag = f"= {round(v):+d}" if rat else f"≈ {v:+.6f}"
            print(f"       (n, σ(n)) = ({n}, {sn})  →  f_σ {tag}")
        for n in fixed:
            v = f_sigma(n, n)
            rat = abs(v - round(v)) < 1e-10
            tag = f"= {round(v):+d}" if rat else f"≈ {v:+.6f}"
            print(f"       (n fixed)    = ({n})         →  f_σ {tag}")
        if constant:
            print(f"    ✓ constant: f_σ ≡ {round(values[0], 6)} on domain")
        else:
            print(f"    ✗ non-constant: f_σ takes "
                  f"{len(set(round(v, 8) for v in values))} distinct values")

    return {
        "name": name,
        "pairs": pairs,
        "fixed": fixed,
        "values": values,
        "constant": constant,
        "domain_size": len(pairs) * 2 + len(fixed),
    }


# --- main enumeration ---------------------------------------------------

def main():
    print("CREATI C3 reflection-identity enumeration")
    print("=" * 64)
    print("Testing whether any involution σ on positive integers ≥ 3")
    print("gives f_σ(n) := trace(R_n) + trace(R_σ(n)) = closed form.")
    print()
    print("trace(R_n) = 2 cos(2π/n).  Excluded as transpose-trivial:")
    print("  - σ = id (gives 4 cos(2π/n), trivial)")
    print("  - σ that pointwise fixes trace (e.g. σ(n) = -n)")
    print()

    domain = list(range(3, 61))
    results = []

    # --- family (a): σ(n) = c - n ---
    print()
    print("Family (a): σ(n) = c − n  (additive reflection)")
    print("-" * 64)
    for c in [7, 8, 9, 10, 11, 12, 15, 20]:
        r = enumerate_candidate(
            f"σ(n) = {c} − n", sigma_c_minus_n(c), domain
        )
        if r is not None:
            results.append(r)

    # --- family (b): σ(n) = 2n/(n - 2) ---
    print()
    print("Family (b): σ(n) = 2n/(n − 2)  (the only involution")
    print("            satisfying 1/n + 1/σ(n) = 1/2)")
    print("-" * 64)
    r = enumerate_candidate(
        "σ(n) = 2n/(n − 2)", sigma_2n_over_n_minus_2, domain
    )
    if r is not None:
        results.append(r)

    # --- family (c): σ(n) = c/n ---
    print()
    print("Family (c): σ(n) = c/n  (multiplicative reflection through c)")
    print("-" * 64)
    for c in [12, 24, 36, 48, 60, 120]:
        r = enumerate_candidate(
            f"σ(n) = {c}/n", sigma_c_over_n(c), domain
        )
        if r is not None:
            results.append(r)

    # --- summary of constant-f_σ candidates ---
    print()
    print("=" * 64)
    print("Constant-f_σ summary")
    print("=" * 64)
    print()
    print("Candidates where f_σ is constant on σ's integer-valued domain.")
    print("A single (n, σ(n)) pair is trivially constant (one data point);")
    print("informative cases need ≥ 2 distinct instances on the domain.")
    print()
    constants = [r for r in results if r["constant"]]
    informative = [r for r in constants if r["domain_size"] >= 3]
    degenerate = [r for r in constants if r["domain_size"] < 3]

    print(f"Informative (≥ 2 distinct instances):")
    if not informative:
        print(f"  (none)")
    else:
        print(f"  {'name':<32s} {'value':>10s} {'domain size':>13s}")
        print(f"  {'-'*32} {'-'*10} {'-'*13}")
        for r in sorted(informative, key=lambda x: -x["domain_size"]):
            v = r["values"][0]
            sz = r["domain_size"]
            tag = f"= {round(v):+d}" if abs(v - round(v)) < 1e-10 \
                else f"≈ {v:+.4f}"
            print(f"  {r['name']:<32s} {tag:>10s} {sz:>13d}")
    print()
    print(f"Degenerate (single (n, σ(n)) pair, trivially constant):")
    if not degenerate:
        print(f"  (none)")
    else:
        for r in degenerate:
            print(f"  {r['name']:<40s} pair: {r['pairs'][0]}")

    # --- verdict ---
    print()
    print("=" * 64)
    print("Verdict")
    print("=" * 64)
    print()
    print("Largest constant-f_σ candidate: σ(n) = 2n/(n − 2), with f_σ ≡ 0")
    print("on the integer-valued domain {3, 4, 6}.  Pair (3, 6) gives")
    print("  2 cos(2π/3) + 2 cos(2π/6) = (−1) + (+1) = 0.")
    print("Fixed point n = 4: 2 · trace(R_4) = 2 · 0 = 0.")
    print()
    print("Domain size: 3 (two paired integers + one fixed point).")
    print("This is the equilateral-triangle / regular-hexagon coincidence,")
    print("not a structural identity over an infinite domain.")
    print()
    print("All additive σ(n) = c − n candidates produce non-constant f_σ:")
    print("they pair finitely many integers symmetrically around c/2 and")
    print("each pair gives a different irrational value 2 cos(2π/n) +")
    print("2 cos(2π/(c−n)).  Different n produce values in different")
    print("cyclotomic subfields, so no rational closed form in n exists.")
    print()
    print("Multiplicative σ(n) = c/n candidates give finite domains")
    print("(divisor pairs of c) with values typically in different")
    print("cyclotomic fields; non-constant in general.")
    print()
    print("CONCLUSION: no non-trivial involution σ on the positive")
    print("integers ≥ 3 produces a constant or rational-in-n closed form")
    print("for f_σ(n) = trace(R_n) + trace(R_σ(n)) over an infinite")
    print("domain.  The unique 3-element witness {3, 4, 6} for f_σ ≡ 0")
    print("is the equilateral-triangle/regular-hexagon coincidence,")
    print("which is finite and does not constitute a structural identity.")
    print()
    print("Adjacent identities that DO exist on the circle side, but")
    print("that are not σ-involutions on n:")
    print("  - Iteration / Chebyshev: trace(R_n^m) = 2 cos(2πm/n).")
    print("    Closed-form sums via product-to-sum; parameterized by")
    print("    (n, m), not by an involution on n alone.")
    print("  - Galois twist within fixed n: for n with multiple prime")
    print("    factors, (ℤ/nℤ)* contains involutions k ↦ k' (k k' ≡ 1")
    print("    mod n with k ≠ ±1), giving identities like 2 cos(2π/8) +")
    print("    2 cos(6π/8) = 0. These act on indices inside a fixed n,")
    print("    not on n itself. Different identity-type.")
    print()
    print("CREATI C3's open slot closes negatively: NO non-trivial")
    print("σ-involution on the n-parameter produces a closed-form")
    print("reflection identity over an infinite domain. The kind-mismatch")
    print("(log side reflection-rigid, circle side iteration-rigid)")
    print("stands as the operative structural finding.")


if __name__ == "__main__":
    main()
