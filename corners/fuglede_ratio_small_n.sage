"""
corners/fuglede_ratio_small_n.sage

Fuglede small-n stability ratio for inscribed regular N-gons.

Computes Delta_F / (||u||^2 + ||grad u||^2) at N in {3, ..., 12} and tests
whether Fuglede 1989 Theorem 1.2 (I.a) lower bound

    Delta_F >= (1/10) (||u||^2 + ||grad u||^2)

holds at small N where the nearly-spherical hypothesis (*) formally fails.

Per `iso/THREE-REGISTER-SYNTHESIS.md` Sec 3.4: namespace-corrected
threshold for the inscribed N-gon family is N >= 8 (gradient bound) or
N >= 7 (uniform bound). Below those, hypothesis (*) fails. The synthesis
flagged "Bridge 1" (per-N direct Parseval computation using existing
Hurwitz coefficient formulas) as cheapest; this script is that bridge.

Setup
-----
Inscribed regular N-gon, vertices on unit circle.
Volume-normalize by k = sqrt(pi / A_N) so the area becomes pi = omega_2.
Then u(theta) = k r(theta) - 1, with r(theta) the (unscaled) boundary
distance at angle theta (cos(pi/N) at edge midpoint, 1 at vertex).
sigma = dtheta / (2 pi) on the unit circle (Fuglede's normalized
surface measure on Sigma).

Closed forms on a single wedge phi in [-pi/N, pi/N], N copies by symmetry:
    u(phi)     = k cos(pi/N) sec(phi) - 1
    du/dphi    = k cos(pi/N) sin(phi) / cos^2(phi)

    integral_{-a}^{a} u(phi)^2 dphi
        = 2 [ k^2 c^2 t  -  2 k c log((1 + s) / c)  +  a ]

    integral_{-a}^{a} (du/dphi)^2 dphi
        = (2/3) k^2 c^2 t^3

with a = pi/N, s = sin(a), c = cos(a), t = tan(a).

Fuglede's dimensionless deficiency:
    Delta_F = L / (2 sqrt(pi A)) - 1 = sqrt(N tan(pi/N) / pi) - 1.

Volume-normalization sanity check (eq. 10 in Fuglede Sec 1):
    <u> + <u^2>/2 = 0.

Ambient-dimension hypothesis (*) for n_dim = 2:
    ||u||_oo  <= 3 / (20 n_dim) = 3/40 = 0.075
    ||grad u||_oo <= 1/2

For the inscribed regular N-gon:
    ||u||_oo      = max(k - 1, 1 - k c)
    ||grad u||_oo = k tan(pi/N)
"""

RR = RealField(200)
PI = RR(pi)
ONE_TENTH = RR(1) / RR(10)
THREE_FORTIETH = RR(3) / RR(40)
ONE_HALF = RR(1) / RR(2)


def fuglede_data(N):
    a = PI / RR(N)
    s = sin(a)
    c = cos(a)
    t = s / c

    A = RR(N) * s * c          # = (N/2) sin(2 pi / N)
    alpha = RR(N) * t          # alpha_N = N tan(pi/N)
    k = sqrt(PI / A)           # volume-normalization scale

    Delta_F = sqrt(alpha / PI) - 1

    u_sq = (RR(N) / PI) * (
        k**2 * c**2 * t
        - 2 * k * c * log((1 + s) / c)
        + a
    )
    grad_u_sq = (RR(N) / (3 * PI)) * k**2 * c**2 * t**3

    u_inf = max(abs(k - 1), abs(k * c - 1))
    grad_u_inf = k * t

    u_mean = (RR(N) / PI) * (k * c * log((1 + s) / c) - a)

    return {
        'N': N,
        'k': k,
        'Delta_F': Delta_F,
        'u_sq': u_sq,
        'grad_u_sq': grad_u_sq,
        'sum_norms': u_sq + grad_u_sq,
        'ratio': Delta_F / (u_sq + grad_u_sq),
        'u_inf': u_inf,
        'grad_u_inf': grad_u_inf,
        'unif_ok': u_inf <= THREE_FORTIETH,
        'grad_ok': grad_u_inf <= ONE_HALF,
        'vol_check': u_mean + u_sq / 2,
    }


def main():
    rows = [fuglede_data(N) for N in range(3, 13)]

    print("Fuglede stability ratio for inscribed regular N-gons")
    print("Theorem 1.2 (I.a) lower bound: Delta_F >= (1/10) (||u||^2 + ||grad u||^2)")
    print("Hypothesis (*) for n_dim = 2: ||u||_oo <= 3/40 = 0.075,  ||grad u||_oo <= 1/2")
    print()

    header = (
        f"{'N':>3} | {'||u||_oo':>10} {'unif':>4} {'||grad u||_oo':>13} {'grad':>4} | "
        f"{'Delta_F':>11} {'||u||^2+||grad u||^2':>20} {'ratio':>10} {'>=1/10':>6}"
    )
    print(header)
    print("-" * len(header))
    for r in rows:
        print(
            f"{r['N']:>3} | "
            f"{float(r['u_inf']):>10.6f} {'Y' if r['unif_ok'] else 'N':>4} "
            f"{float(r['grad_u_inf']):>13.6f} {'Y' if r['grad_ok'] else 'N':>4} | "
            f"{float(r['Delta_F']):>11.5e} {float(r['sum_norms']):>20.5e} "
            f"{float(r['ratio']):>10.6f} "
            f"{'Y' if r['ratio'] >= ONE_TENTH else 'N':>6}"
        )

    print()
    max_vol_err = max(abs(float(r['vol_check'])) for r in rows)
    print(f"Volume-normalization check max |<u> + <u^2>/2| = {max_vol_err:.2e}  (should be 0)")
    print()

    small = [r for r in rows if r['N'] in (3, 4, 5, 6, 7)]
    inf_pair = min(((r['N'], r['ratio']) for r in small), key=lambda p: p[1])
    inf_N, inf_ratio = inf_pair
    print(f"Small-n stability test (N in 3..7, hypothesis (*) formally fails):")
    print(f"  inf ratio  = {float(inf_ratio):.6f}  at N = {inf_N}")
    print(f"  Fuglede's universal 1/10 = {float(ONE_TENTH):.6f}")
    if inf_ratio >= ONE_TENTH:
        margin = float((inf_ratio - ONE_TENTH) / ONE_TENTH * 100)
        print(f"  VERDICT: bound holds at small N. Margin at N = {inf_N}: {margin:.2f}%.")
    else:
        deficit = float((ONE_TENTH - inf_ratio) / ONE_TENTH * 100)
        print(f"  VERDICT: bound FAILS at N = {inf_N}. Deficit: {deficit:.2f}%.")


if __name__ == "__main__":
    main()
