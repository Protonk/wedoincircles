"""Verify the psi-vs-trace-degree fracture for candidate ledger #1.

This script supports ``memos/LEDGER-PIVOT-SEARCH.md``.  It checks:

1. Equal psi strata can contain different trace-field degrees phi(n)/2.
2. Under the phrase "psi-stratified sweep-x-support," the two
   value-forgetful ledgers -- psi-stratum support counts (L2) and exact
   support with psi grading (L3) -- behave differently under a
   rational-placeholder relabeling that preserves the collision pattern:
   L2 is invariant; L3 changes because it retains the x-values
   themselves.  The row-psi ledger (L1) trivially ignores x-values by
   definition and is not tested explicitly.

Corner computation uses mpmath at 120 decimal digits of precision, matching
``n-gons/counting/counting_utils.py``.
"""

from __future__ import annotations

from collections import Counter, defaultdict
import argparse

from mpmath import mp


mp.dps = 120

DEFAULT_N_MAX = 60
DEFAULT_SUPPORT_N = 15
CLUSTER_TOL = mp.mpf("1e-40")


def factorization(n: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    remaining = n
    p = 2
    while p * p <= remaining:
        if remaining % p == 0:
            exp = 0
            while remaining % p == 0:
                remaining //= p
                exp += 1
            factors[p] = exp
        p = 3 if p == 2 else p + 2
    if remaining > 1:
        factors[remaining] = 1
    return factors


def euler_phi(n: int) -> int:
    result = n
    for p in factorization(n):
        result -= result // p
    return result


def psi_prime_power(p: int, exp: int) -> int:
    if p == 2:
        return 0 if exp == 1 else 2 ** (exp - 1)
    return p ** exp - p ** (exp - 1)


def psi_value(n: int) -> int:
    if n in {1, 2}:
        return 0
    return sum(psi_prime_power(p, exp) for p, exp in factorization(n).items())


def trace_degree(n: int) -> int:
    if n < 3:
        raise ValueError("trace degree phi(n)/2 is used here only for n >= 3")
    return euler_phi(n) // 2


def psi_support_counts(clusters: list[list[tuple]]) -> Counter[int]:
    counts: Counter[int] = Counter()
    for cluster in clusters:
        for _x, n, _k, _theta in cluster:
            counts[psi_value(n)] += 1
    return counts


def corner_clusters(max_n: int) -> list[list[tuple]]:
    points: list[tuple] = []
    for n in range(3, max_n + 1):
        radius = 1 / mp.cos(mp.pi / n)
        for k in range(n):
            theta = (2 * k + 1) * mp.pi / n
            points.append((radius * mp.cos(theta), n, k, theta))

    points.sort(key=lambda item: item[0])
    clusters: list[list[tuple]] = []
    current: list[tuple] = []
    current_x = None
    for item in points:
        x = item[0]
        if current_x is None or abs(x - current_x) > CLUSTER_TOL:
            if current:
                clusters.append(current)
            current = [item]
            current_x = x
        else:
            current.append(item)
    if current:
        clusters.append(current)
    return clusters


def collision_signature(clusters: list[list[tuple]]) -> tuple[int, ...]:
    return tuple(len(cluster) for cluster in clusters)


def exact_support_signature(clusters: list[list[tuple]]) -> tuple:
    """Tuple of (x, psi) pairs for direct comparison under mpmath."""
    signature: list[tuple] = []
    for cluster in clusters:
        for x, n, _k, _theta in cluster:
            signature.append((x, psi_value(n)))
    return tuple(signature)


def placeholder_clusters(clusters: list[list[tuple]]) -> list[list[tuple]]:
    denominator = len(clusters) + 1
    relabeled: list[list[tuple]] = []
    for idx, cluster in enumerate(clusters, start=1):
        placeholder_x = mp.mpf(idx) / mp.mpf(denominator)
        relabeled.append([(placeholder_x, n, k, theta) for _x, n, k, theta in cluster])
    return relabeled


def named_pair_rows() -> list[tuple[int, int, int, int, int]]:
    pairs = [(7, 15), (11, 35), (16, 40)]
    rows = []
    for a, b in pairs:
        psi_a = psi_value(a)
        psi_b = psi_value(b)
        if psi_a != psi_b:
            raise AssertionError(f"expected shared psi for {(a, b)}, got {psi_a}, {psi_b}")
        rows.append((a, b, psi_a, trace_degree(a), trace_degree(b)))
    return rows


def psi_classes(n_max: int) -> dict[int, list[tuple[int, int]]]:
    classes: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for n in range(3, n_max + 1):
        classes[psi_value(n)].append((n, trace_degree(n)))
    return dict(sorted(classes.items()))


def print_named_pairs() -> None:
    print("Named equal-psi / different-degree pairs")
    print("n_a  n_b  psi  deg_a  deg_b  spread")
    print("-------------------------------------")
    for a, b, psi, deg_a, deg_b in named_pair_rows():
        print(f"{a:>3}  {b:>3}  {psi:>3}  {deg_a:>5}  {deg_b:>5}  {abs(deg_b - deg_a):>6}")
    print()


def print_classes(n_max: int) -> None:
    print(f"Psi equivalence classes through n={n_max} with at least two rows")
    print("psi  spread  rows as n:deg")
    print("---------------------------")
    for psi, rows in psi_classes(n_max).items():
        if len(rows) < 2:
            continue
        degrees = [deg for _n, deg in rows]
        spread = max(degrees) - min(degrees)
        formatted = ", ".join(f"{n}:{deg}" for n, deg in rows)
        print(f"{psi:>3}  {spread:>6}  {formatted}")
    print()


def print_largest_fractures(n_max: int, limit: int = 5) -> None:
    ranked = []
    for psi, rows in psi_classes(n_max).items():
        if len(rows) < 2:
            continue
        degrees = [deg for _n, deg in rows]
        spread = max(degrees) - min(degrees)
        if spread > 0:
            ranked.append((spread, psi, rows))
    ranked.sort(reverse=True)

    print(f"Largest nonzero psi-class degree spreads through n={n_max}")
    print("spread  psi  rows as n:deg")
    print("---------------------------")
    for spread, psi, rows in ranked[:limit]:
        formatted = ", ".join(f"{n}:{deg}" for n, deg in rows)
        print(f"{spread:>6}  {psi:>3}  {formatted}")
    print()


def print_support_relabeling(support_n: int) -> None:
    clusters = corner_clusters(support_n)
    placeholders = placeholder_clusters(clusters)

    original_l2 = psi_support_counts(clusters)
    placeholder_l2 = psi_support_counts(placeholders)
    original_l3 = exact_support_signature(clusters)
    placeholder_l3 = exact_support_signature(placeholders)

    print(f"Support-level placeholder test at N={support_n}")
    print("--------------------------------------")
    print(f"occupied x-cells: {len(clusters)}")
    print(f"total support points (n,k): {sum(len(cluster) for cluster in clusters)}")
    print(f"collision signature preserved: {collision_signature(clusters) == collision_signature(placeholders)}")
    print(f"L2 psi support counts unchanged: {original_l2 == placeholder_l2}")
    print(f"L3 exact support with psi grading changed: {original_l3 != placeholder_l3}")
    print("L2 counts by psi:", ", ".join(f"{psi}:{original_l2[psi]}" for psi in sorted(original_l2)))
    first_cluster = clusters[0]
    first_placeholder = placeholders[0]
    if first_cluster and first_placeholder:
        real_x, real_n, real_k, _theta = first_cluster[0]
        placeholder_x, _n, _k, _theta = first_placeholder[0]
        print(
            "first relabeled point: "
            f"(n={real_n}, k={real_k}, psi={psi_value(real_n)}) "
            f"x≈{mp.nstr(real_x, 6)} -> x={mp.nstr(placeholder_x, 6)}"
        )
    print()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-max", type=int, default=DEFAULT_N_MAX)
    parser.add_argument("--support-n", type=int, default=DEFAULT_SUPPORT_N)
    args = parser.parse_args()

    print_named_pairs()
    print_classes(args.n_max)
    print_largest_fractures(args.n_max)
    print_support_relabeling(args.support_n)


if __name__ == "__main__":
    main()
