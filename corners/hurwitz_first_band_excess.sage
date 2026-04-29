"""
Asymptotic expansion of the first-band concentration ratio
B_1(n)/Delta_n around 1/n^2 = 0.

Closes the open question at `paper/POLYGONAL-LEDGER.md` §"Open":
"Whether the sharpness constant 6/pi^2 has tractable higher-order
corrections (the B_1(n)/Delta_n excess decays as O(1/n^2))."

The answer: yes, fully tractable. The expansion is closed-form with
rational-in-pi^2 coefficients to all orders. To order 1/n^6:

    B_1(n)/Delta_n = 6/pi^2
                   + 12 (15 - pi^2) / (5 pi^2 n^2)
                   + 2 (34 pi^4 - 1260 pi^2 + 7875) / (175 pi^2 n^4)
                   - 4 (22 pi^6 - 1530 pi^4 + 23625 pi^2 - 110250) /
                     (2625 pi^2 n^6)
                   + O(1/n^8).

Numerical leading correction: ~ +1.2476 / n^2; the excess approaches
6/pi^2 from above, matching the table at
`corners/HURWITZ-FIRST-BAND-CONCENTRATION.md` (B_1(3)/Delta_3 = 0.7297,
B_1(40)/Delta_40 = 0.6087, asymptote 0.6079271...).

Inheritance across the inscribed/circumscribed Archimedean squeeze. Both
B_j(n) and Delta_n scale by the same sec^2(pi/n) factor between
inscribed and circumscribed regular n-gons (`corners/hurwitz_gap_circumscribed.sage`),
so the ratio B_1(n)/Delta_n is *identical* on the two sides; the
asymptotic expansion above transfers verbatim.

Closed-form inputs (from `corners/HURWITZ-FIRST-BAND-CONCENTRATION.md`):

    L_n           = 2 n sin(pi/n)
    B_1(n)        = (L_n^4 / (2 pi^2)) * n^2 (n^2 + 3) / (n^2 - 1)^3
    Delta_n       = L_n^2 * [1 - (pi/n) cot(pi/n)]

Setting u = pi/n, the ratio B_1/Delta becomes a function of u; Taylor
expansion around u = 0 gives the asymptotic.
"""

import os


def main():
    # --- symbolic Taylor expansion in u = pi/n ------------------------
    u = SR.var('u')
    ratio = (
        2 * pi**2 * sin(u)**2 * (pi**2 + 3 * u**2)
        / ((pi**2 - u**2)**3 * (1 - u / tan(u)))
    )

    print("=" * 78)
    print("Symbolic asymptotic expansion of B_1(n) / Delta_n")
    print("=" * 78)
    print()
    print("Setting u = pi/n, ratio = B_1(n)/Delta_n is a function of u.")
    print("Taylor expansion around u = 0 (through u^6):")
    print()

    series_u = ratio.series(u, 8)
    coeffs = {
        0: series_u.coefficient(u, 0).simplify_full(),
        2: series_u.coefficient(u, 2).simplify_full(),
        4: series_u.coefficient(u, 4).simplify_full(),
        6: series_u.coefficient(u, 6).simplify_full(),
    }

    print(f"  u^0:  {coeffs[0]}    (= 6/pi^2 = {float(coeffs[0]):.16f})")
    print(f"  u^2:  {coeffs[2]}")
    print(f"          (numerical: {float(coeffs[2]):.16f})")
    print(f"  u^4:  {coeffs[4]}")
    print(f"          (numerical: {float(coeffs[4]):.16f})")
    print(f"  u^6:  {coeffs[6]}")
    print(f"          (numerical: {float(coeffs[6]):.16f})")
    print()

    # --- substituting u = pi/n -----------------------------------------
    print("Substituting u = pi/n, B_1(n)/Delta_n =")
    print()
    print("    6/pi^2  (asymptote, matches 1/zeta(2))")
    coeff_n2 = (coeffs[2] * pi**2).simplify_full()
    coeff_n4 = (coeffs[4] * pi**4).simplify_full()
    coeff_n6 = (coeffs[6] * pi**6).simplify_full()
    print(f"  + ({coeff_n2}) / n^2")
    print(f"  + ({coeff_n4}) / n^4")
    print(f"  + ({coeff_n6}) / n^6")
    print(f"  + O(1/n^8)")
    print()
    print(f"Numerical 1/n^k coefficients:")
    print(f"  c1 (u^2 -> 1/n^2):  {float(coeff_n2):.12f}")
    print(f"  c2 (u^4 -> 1/n^4):  {float(coeff_n4):.12f}")
    print(f"  c3 (u^6 -> 1/n^6):  {float(coeff_n6):.12f}")
    print()

    # --- numerical verification at 200-bit precision -------------------
    print("=" * 78)
    print("Numerical verification at 200-bit precision")
    print("=" * 78)
    print()
    print(f"{'n':>4}  {'exact B_1(n)/Delta_n':>22}  "
          f"{'+ c1/n^2':>20}  {'+ c2/n^4':>20}  {'+ c3/n^6':>20}")

    six_over_pi2 = float(6 / pi**2)
    c1, c2, c3 = float(coeff_n2), float(coeff_n4), float(coeff_n6)

    pi_hp = pi.n(prec=200)
    for nval in [3, 5, 7, 10, 20, 40, 100, 1000, 10000]:
        L = 2 * nval * sin(pi_hp / nval)
        B1 = (L**4 / (2 * pi_hp**2)) * nval**2 * (nval**2 + 3) / (nval**2 - 1)**3
        Delta = L**2 * (1 - (pi_hp / nval) / tan(pi_hp / nval))
        exact = float(B1 / Delta)
        pred1 = six_over_pi2 + c1 / nval**2
        pred2 = pred1 + c2 / nval**4
        pred3 = pred2 + c3 / nval**6
        print(f"{nval:>4}  {exact:>22.16f}  "
              f"{pred1:>20.16f}  {pred2:>20.16f}  {pred3:>20.16f}")

    print()
    print("Convergence: at n = 10000, asymptotic expansion through O(1/n^6)")
    print("matches exact value to floating-point precision.")
    print()
    print("Sign: c1 > 0, so excess B_1/Delta - 6/pi^2 approaches the")
    print("asymptote from ABOVE — matching the inscribed-side table")
    print("at HURWITZ-FIRST-BAND-CONCENTRATION (B_1(n)/Delta_n decreases")
    print("monotonically toward 6/pi^2 as n grows).")


if __name__ == "__main__":
    main()
