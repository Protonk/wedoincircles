"""
corners/hurwitz_shell_masses.sage

Numerical table of Hurwitz first-band concentration shell masses for
inscribed regular n-gons. Verifies the dyadic-shell estimate proven in
corners/HURWITZ-FIRST-BAND-CONCENTRATION.md Step 4:

    sum_{2^r <= j < 2^(r+1)} B_j(n)  <=  2^(-r) B_1(n).

Closed form (Step 1 of the same memo):

    B_j(n) = (L_n^4 / (2 pi^2))
             * j^2 n^2 (j^2 n^2 + 3) / (j^2 n^2 - 1)^3,
    L_n = 2 n sin(pi / n).

For each n, tabulates:
    - S_r(n) = sum_{2^r <= j < 2^(r+1)} B_j(n)
    - bound  = 2^(-r) B_1(n)
    - ratio  = S_r / bound        (proof says <= 1)
    - decay  = S_r / S_(r-1)      (-> 1/2 as r -> infty, universal in n)

Asymptotic of the ratio (n-dependent, not 1/2):

    S_r(n) / (2^(-r) B_1(n))  ->  (n^2 - 1)^3 / (2 n^4 (n^2 + 3))
    as r -> infty for fixed n.

This limit -> 1/2 only as n -> infty; for fixed n it is smaller. Sample
limits: n=3 -> 0.2634, n=5 -> 0.3950, n=40 -> 0.4981.

Sanity checks:
    - r = 0: S_0 = B_1, bound = B_1, ratio = 1.
    - cumulative sum across r should match Delta_n = L_n^2 - 4 pi A_n
      (residual is the tail beyond r = R_max).
    - The B_1(n) / Delta_n values printed in the per-n header are
      *exact* (closed-form numerator and denominator at 200-bit
      precision). They differ from the existing table in
      HURWITZ-FIRST-BAND-CONCENTRATION at ~ 1.5e-5 because that table
      was generated with a truncated direct sum in the denominator,
      not the exact Delta_n.
"""

RR = RealField(200)
PI = RR(pi)


def L(n):
    return 2 * RR(n) * sin(PI / RR(n))


def A(n):
    # = (n/2) sin(2 pi / n) using sin(2x) = 2 sin x cos x
    return RR(n) * sin(PI / RR(n)) * cos(PI / RR(n))


def Delta(n):
    return L(n)**2 - 4 * PI * A(n)


def B(j, n):
    """Paired-band mass B_j(n) from HURWITZ-FIRST-BAND-CONCENTRATION Step 1."""
    Ln = L(n)
    j2n2 = (RR(j) * RR(n))**2
    return (Ln**4 / (2 * PI**2)) * j2n2 * (j2n2 + 3) / (j2n2 - 1)**3


def shell_sum(r, n):
    """S_r(n) = sum over j in [2^r, 2^(r+1)) of B_j(n)."""
    lo = 2**r
    hi = 2**(r + 1)
    return sum(B(j, n) for j in range(lo, hi))


def main():
    print("Hurwitz first-band concentration: dyadic-shell mass table")
    print("Verifies HURWITZ-FIRST-BAND-CONCENTRATION Step 4 numerically.")
    print("Bound: S_r(n) <= (1/2)^r * B_1(n).")
    print("Asymptotic in r (fixed n): S_r / bound -> (n^2-1)^3 / (2 n^4 (n^2+3)).")
    print("Decay S_r / S_(r-1) -> 1/2 universally as r -> infty.")
    print()

    R_max = 5
    for n in [3, 5, 7, 10, 40]:
        B1 = B(1, n)
        D = Delta(n)
        print(f"n = {n}")
        print(f"  Delta_n           = {float(D):.6e}")
        print(f"  B_1(n)            = {float(B1):.6e}")
        print(f"  B_1(n) / Delta_n  = {float(B1 / D):.10f}")
        print()
        header = (
            f"  {'r':>2}  {'shell range':>14}  {'S_r(n)':>14}  "
            f"{'bound':>14}  {'ratio':>10}  {'decay':>9}"
        )
        print(header)
        print("  " + "-" * (len(header) - 2))

        prev_S = None
        cumulative = RR(0)
        for r in range(R_max + 1):
            S = shell_sum(r, n)
            bound = B1 / RR(2)**r
            ratio = S / bound
            shell_lo = 2**r
            shell_hi = 2**(r + 1) - 1
            shell_range = f"[{shell_lo}, {shell_hi}]"
            if prev_S is not None:
                decay = float(S / prev_S)
                decay_str = f"{decay:>9.6f}"
            else:
                decay_str = f"{'-':>9}"
            print(
                f"  {r:>2}  {shell_range:>14}  {float(S):>14.6e}  "
                f"{float(bound):>14.6e}  {float(ratio):>10.6f}  "
                f"{decay_str}"
            )
            prev_S = S
            cumulative += S

        residual = D - cumulative
        residual_frac = residual / D
        print(
            f"  cumulative S_0..S_{R_max}: {float(cumulative):.6e}  "
            f"(tail residual: {float(residual):.3e}, "
            f"fraction {float(residual_frac):.3e} of Delta_n)"
        )
        print()


if __name__ == "__main__":
    main()
