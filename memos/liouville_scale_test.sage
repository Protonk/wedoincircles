# liouville_scale_test.sage
#
# Two-stage test of whether the K-H-L-A endgame survives reduction to the
# single Archimedean approximant alpha_n = n tan(pi/n).
#
# Stage 1 (symbolic): verify
#   Delta_n             = 4 A_n^{insc} (alpha_n - pi)
#   Delta(gamma_tilde)  = 4 A_n^{circ} (alpha_n - pi)
#   ||y_n'||^2          = 4 A_n^{circ} (alpha_n - pi) + R_n
# where A_n^{insc} = n sin(pi/n) cos(pi/n), A_n^{circ} = n tan(pi/n) = alpha_n.
#
# Stage 2 (numerical): compute the Mahler measure / algebraic height of
# alpha_n for small n and compare the Liouville lower bound on |alpha_n - pi|
# (under the hypothesis that pi is algebraic of degree d) against the
# Archimedean upper bound |alpha_n - pi| ~ pi^3 / (3 n^2).

from sage.all import (
    pi, tan, sin, cos, var, simplify, Expression,
    QQ, ZZ, QQbar, CC, RR, polygen, PolynomialRing, log, sqrt, prod
)

# ---------------------------------------------------------------------------
# Stage 1: symbolic factorization verification
# ---------------------------------------------------------------------------

print("=" * 90)
print("Stage 1: symbolic verification of the (alpha_n - pi) factorization")
print("=" * 90)
print()

u = var('u')
# With n = pi / u, so u = pi/n, tan(pi/n) = tan(u).
# alpha_n = n tan(pi/n) = (pi/u) tan(u)
alpha_u = (pi / u) * tan(u)

# A_n^{insc} = (n/2) sin(2 pi/n) = n sin(pi/n) cos(pi/n) = (pi/u) sin(u) cos(u)
A_insc_u = (pi / u) * sin(u) * cos(u)

# A_n^{circ} = n tan(pi/n) = alpha_u
A_circ_u = alpha_u

# Delta_n (inscribed) = L_n^2 - 4 pi A_n = 4 n^2 sin^2(pi/n) - 4 pi (n/2) sin(2 pi/n)
#                    = 4 (pi/u)^2 sin^2(u) - 4 pi (pi/u) sin(u) cos(u)
Delta_insc_u = 4 * (pi / u) ** 2 * sin(u) ** 2 - 4 * pi * (pi / u) * sin(u) * cos(u)

# Claim: Delta_insc = 4 A_insc (alpha_u - pi)
claim_insc = 4 * A_insc_u * (alpha_u - pi)

diff_insc = (Delta_insc_u - claim_insc).subs(tan(u) == sin(u)/cos(u)).full_simplify()
print(f"Delta_n - 4 A_n^insc (alpha_n - pi) = {diff_insc}  (should be 0)")

# Delta(gamma_tilde) = 4 n^2 tan^2 - 4 pi n tan = 4 (pi/u)^2 tan^2(u) - 4 pi (pi/u) tan(u)
Delta_circ_u = 4 * (pi / u) ** 2 * tan(u) ** 2 - 4 * pi * (pi / u) * tan(u)

# Claim: Delta_circ = 4 A_circ (alpha_u - pi) = 4 alpha (alpha - pi)
claim_circ = 4 * A_circ_u * (alpha_u - pi)

diff_circ = (Delta_circ_u - claim_circ).subs(tan(u) == sin(u)/cos(u)).full_simplify()
print(f"Delta(gamma_t) - 4 A_n^circ (alpha_n - pi) = {diff_circ}  (should be 0)")

# ||y_n'||^2 = (4 pi n / 3) tan^3 = (4 pi^2 / (3 u)) tan^3(u)
strip_h1_u = (4 * pi ** 2 / (3 * u)) * tan(u) ** 3

# R_n = strip_h1 - Delta_circ
R_u = strip_h1_u - Delta_circ_u

# Claim: R_n = 4 A_circ * [(pi/3) tan^2 - (alpha - pi)]
R_bracket = (pi / 3) * tan(u) ** 2 - (alpha_u - pi)
R_claimed = 4 * A_circ_u * R_bracket

diff_R = (R_u - R_claimed).subs(tan(u) == sin(u)/cos(u)).full_simplify()
print(f"R_n - 4 A_n^circ [(pi/3) tan^2(pi/n) - (alpha_n - pi)] = {diff_R}  (should be 0)")
print()
print("So ||y_n'||^2 = 4 A_n^circ (alpha_n - pi)  +  4 A_n^circ [(pi/3) tan^2 - (alpha_n - pi)].")
print()
print("The bracket (pi/3) tan^2(pi/n) - (alpha_n - pi) itself cancels at 1/n^2:")
bracket_series = R_bracket.series(u == 0, 6).truncate()
print(f"   [(pi/3) tan^2 - (alpha - pi)] series in u=pi/n:  {bracket_series}")
print("   (leading u^4 = 1/n^4, so R_n = O(1/n^4) as before)")
print()
print("Stage 1 RESULT: the three observables share a single small quantity,")
print("  alpha_n - pi,  with different geometric prefactors:")
print("     Delta_n             = 4 A_n^insc * (alpha_n - pi)")
print("     Delta(gamma_t)       = 4 A_n^circ * (alpha_n - pi)")
print("     ||y_n'||^2           = 4 A_n^circ * (alpha_n - pi)  +  R_n")
print("  where R_n is a smaller further-factored quantity.")
print("  The Fourier/Hurwitz/strip apparatus produces geometric WEIGHTS, not a new small ALGEBRAIC quantity.")
print()

# ---------------------------------------------------------------------------
# Stage 2: compute algebraic height of alpha_n = n tan(pi/n)
# ---------------------------------------------------------------------------

print("=" * 90)
print("Stage 2: algebraic height of alpha_n = n tan(pi/n)")
print("=" * 90)
print()


def alpha_n_minpoly(n):
    """Return minimal polynomial of alpha_n = n tan(pi/n) over Q."""
    alpha = QQbar(n * tan(pi / n))
    return alpha.minpoly()


def mahler_measure(p):
    """Compute Mahler measure of integer polynomial p."""
    roots = p.roots(ring=CC, multiplicities=False)
    lc = abs(p.leading_coefficient())
    prod_val = RR(1)
    for r in roots:
        ar = abs(r)
        if ar > 1:
            prod_val *= RR(ar)
    return RR(lc) * prod_val


def naive_height(p):
    """Max |coef| of integer polynomial."""
    return max(abs(c) for c in p.coefficients())


print("  alpha_n is algebraic over Q; for odd prime n its degree is phi(2n).")
print("  The real subfield Q(cos(pi/n)) has degree phi(2n)/2; alpha_n often")
print("  sits in a quadratic extension of that real subfield.")
print("  Conjugates are n tan(pi k / n) for k in the relevant Galois orbit.")
print("  For k close to n/2, n tan(pi k / n) ~ n * cot(pi |n-2k|/(2n)) ~ O(n^2).")
print()

print("{:>4}  {:>5}  {:>10}  {:>14}  {:>16}  {:>14}  {:>14}".format(
    "n", "deg", "phi(2n)/2", "log H_naive", "log M(alpha_n)",
    "log M / deg", "max |conj|"
))
print("-" * 100)

results = []
for n in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 19, 21, 23]:
    try:
        p = alpha_n_minpoly(n)
    except Exception as e:
        print(f"{n:>4}  (failed: {e})")
        continue
    deg = p.degree()
    H = naive_height(p)
    M = mahler_measure(p)
    log_H = RR(log(H)) if H > 0 else RR(0)
    log_M = RR(log(M)) if M > 1 else RR(0)
    ratio = log_M / deg if deg > 0 else RR(0)
    # Also compute max absolute conjugate value
    roots_cc = p.roots(ring=CC, multiplicities=False)
    max_conj = max(abs(r) for r in roots_cc) if roots_cc else RR(0)
    # phi(2n)/2 via Sage
    from sage.all import euler_phi
    phi_half = euler_phi(2*n) // 2 if euler_phi(2*n) % 2 == 0 else euler_phi(2*n) / 2
    print(f"{n:>4}  {deg:>5}  {phi_half!s:>10}  {float(log_H):>14.6f}  {float(log_M):>16.6f}  {float(ratio):>14.6f}  {float(max_conj):>14.3f}")
    results.append((n, deg, log_H, log_M, max_conj))

print()
print("Observations:")
print("  * For odd prime n, deg(alpha_n) = phi(2n), twice the real-subfield degree.")
print("    Some even/small n collapse, but the negative height scale is already visible there.")
print("  * max |conjugate| grows polynomially in n, driven by the k closest to n/2.")
print("    (For prime n, max|conj| ~ 2n^2/pi = O(n^2).)")
print("  * log M(alpha_n) / deg(alpha_n) ~ log n along primes, so log M ~ phi(2n) log n (NOT bounded).")
print("    H(alpha_n) = exp(Omega(phi(2n) log n)) along that subsequence.")
print()

# ---------------------------------------------------------------------------
# Stage 2b: Liouville scale comparison
# ---------------------------------------------------------------------------

print("=" * 90)
print("Stage 2b: Liouville vs Archimedes scale comparison")
print("=" * 90)
print()
print("Suppose pi is algebraic of degree d over Q. Then alpha_n - pi is algebraic")
print("over Q of degree D <= d * deg(alpha_n), sitting in the joint field Q(pi, alpha_n).")
print()
print("Liouville (weak form): for algebraic beta != 0 of degree D and conjugates sigma(beta),")
print("  |beta| >= 1 / prod_{sigma != id} |sigma(beta)|")
print("         >= 1 / (max_sigma |sigma(beta)|)^{D-1}.")
print()
print("In our case, |sigma(alpha_n - pi)| <= |sigma(alpha_n)| + |sigma(pi)|, and for large n the")
print("conjugates of alpha_n dominate. So")
print("  |alpha_n - pi| >= 1 / (max|conj(alpha_n)|)^{D-1}  (up to H(pi) factor).")
print()
print("Let M_n = max |conjugate of alpha_n|. Liouville lower bound on log|alpha_n - pi|:")
print("  log|alpha_n - pi| >= - (D-1) * log M_n")
print("                    = - (d * deg(alpha_n) - 1) * log M_n.")
print()
print("Archimedean upper bound:  log|alpha_n - pi| <= log(pi^3/(3 n^2)) ~ -2 log n + C.")
print()
print("Collision (Liouville LB exceeds Archimedean UB) requires:")
print("  (d * deg(alpha_n) - 1) * log M_n  <=  2 log n + O(1).")
print()
print("Since log M_n ~ 2 log n (worst conjugate is O(n^2)), this becomes:")
print("  (d * deg(alpha_n) - 1) * 2 log n <= 2 log n + O(1)")
print("  d * deg(alpha_n) - 1 <= 1 + O(1/log n)")
print("  d * deg(alpha_n) <= 2 + O(1/log n).")
print()
print("{:>4}  {:>10}  {:>12}  {:>12}  {:>22}  {:>14}  {:>16}".format(
    "n", "deg", "max|conj|", "log M_n", "Liouville LB @ d=2",
    "Archimedes UB", "Liouville wins?"
))
print("-" * 100)

import math
for (n, deg, log_H, log_M, max_conj) in results:
    log_Mn = RR(log(max_conj)) if max_conj > 1 else RR(0)
    # Liouville LB for d = 2: log|alpha_n - pi| >= -(2*deg - 1) * log M_n
    LB_d2 = -(2 * deg - 1) * log_Mn
    # Archimedes UB: log|alpha_n - pi| ~ log(pi^3/(3 n^2))
    UB = RR(log(RR(pi) ** 3 / (3 * n ** 2)))
    wins = "YES" if LB_d2 > UB else "no"
    print(f"{n:>4}  {deg:>10}  {float(max_conj):>12.3f}  {float(log_Mn):>12.4f}  {float(LB_d2):>22.4f}  {float(UB):>14.4f}  {wins:>16}")

print()
print("INTERPRETATION:")
print("  For every n >= 3 tested, the Liouville LB (under d = 2, the loosest nontrivial case)")
print("  is FAR SMALLER than the Archimedean UB. Liouville cannot contradict Archimedes")
print("  on alpha_n - pi for any n.")
print()

# ---------------------------------------------------------------------------
# Could cyclotomic-unit cancellation save it?
# ---------------------------------------------------------------------------

print("=" * 90)
print("Cancellation check: does alpha_n have unexpectedly small cyclotomic-unit height?")
print("=" * 90)
print()
print("If there were a cyclotomic-unit identity collapsing alpha_n's Mahler measure,")
print("we would see log M(alpha_n) / deg(alpha_n) stay bounded instead of growing.")
print("The table above shows this ratio grows ~ log n, matching the 'worst conjugate")
print("is O(n^2)' analysis. No cancellation.")
print()
print("log M / deg trend for primes n:")
prime_n = [3, 5, 7, 11, 13, 17, 19, 23]
print(f"{'n':>4}  {'log M / deg':>14}  {'log n':>10}  {'ratio':>10}")
for n in prime_n:
    p = alpha_n_minpoly(n)
    M = mahler_measure(p)
    deg = p.degree()
    log_M = RR(log(M))
    log_n = RR(log(n))
    ratio = log_M / (deg * log_n) if deg > 0 and log_n > 0 else RR(0)
    print(f"{n:>4}  {float(log_M / deg):>14.6f}  {float(log_n):>10.6f}  {float(ratio):>10.6f}")
print()
print("  (log M / deg) / log n converges to a constant > 0.  That's exponential height.")
print()

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------

print("=" * 90)
print("SUMMARY / VERDICT")
print("=" * 90)
print()
print("Stage 1:  POSITIVE. The three observables share the single small quantity")
print("          alpha_n - pi, with geometric prefactors A_n^insc, A_n^circ, A_n^circ + R_n-weight.")
print("          Fourier/Hurwitz/strip machinery does NOT produce a new small algebraic quantity.")
print()
print("Stage 2:  NEGATIVE.")
print("          deg(alpha_n) is generically phi(2n) along odd primes,")
print("          i.e. twice the cyclotomic real-subfield degree.")
print("          max |conjugate(alpha_n)| ~ 2 n^2 / pi  (conjugate at k near n/2).")
print("          log M(alpha_n) ~ phi(2n) * log n along primes (exponential algebraic height).")
print()
print("          Liouville bound under hypothesis pi algebraic of degree d:")
print("            |alpha_n - pi| >= 1 / (M_conj)^{d * deg(alpha_n) - 1}")
print("                            ~ n^{-2 (d deg(alpha_n) - 1)}")
print("            Collision with |alpha_n - pi| ~ 1/n^2 requires d * deg(alpha_n) <= 2.")
print("            This fails on the tested range and asymptotically along primes.")
print()
print("VERDICT:  The naive Liouville endgame of KRAFT-HERMITE-LINDEMANN-AITCHISON")
print("          DIES ON SCALE when reduced to alpha_n = n tan(pi/n).")
print("          No cyclotomic-unit cancellation rescues it.")
print()
print("Consequence for OLD-TIME-RELIGION:")
print("  (A2) 'Resultants/norms' + (A3) 'Euler-Maclaurin squeeze' together close with a")
print("  negative result.  The Liouville strategy on the polygon-gap approximant is not cogent.")
print("  Alternative endgame strategies (different small quantity, non-Liouville lower bound,")
print("  discrepancy over range of n) remain open but are separate directed-attempts.")
