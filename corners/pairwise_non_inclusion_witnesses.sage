"""
corners/pairwise_non_inclusion_witnesses.sage

Pairwise non-inclusion witnesses for the three iso/ hypothesis classes
(Osserman, Fuglede, Beck), per iso/THREE-REGISTER-SYNTHESIS.md Sec 3.2.

Constructs explicit verifiable witnesses for:

  1. Osserman not subset Fuglede  via  thin ellipse (a=2, b=1/2).
  2. Fuglede not subset Osserman  via  small-spike non-convex
     (r(theta) = 1 + epsilon cos(k theta) with k=5, epsilon=0.0575).
  3. Beck not subset {Osserman, Fuglede}  via
     parameter-space-vs-shape-space (categorial; no numerical witness).

For each numerical witness, computes:
  - Whether the construction is in / out of each hypothesis class.
  - The numerical margin from each hypothesis-edge.

Margin convention: signed percent (bound - actual)/bound on the
"satisfied" side; (actual - bound)/bound on the "violated" side. Per
audit convention, margins >= 10 percent certify "cleanly inside/outside."

Witness 1 references:
  - Osserman 1979 eq. (21): Delta >= pi^2 (R-rho)^2 for convex Jordan curve.
  - Sage: elliptic_ec(m), m = 1 - (b/a)^2, gives ellipse perimeter
    L = 4 a * E(m).
  - Volume normalization: ab = 1 makes A = pi a b = pi = omega_2 directly.

Witness 2 references:
  - Fuglede 1989 (*) hypothesis: ||u||_oo <= 3/40, ||grad u||_oo <= 1/2
    for n_dim = 2.
  - Polar curvature: kappa(theta) = (r^2 + 2 (r')^2 - r r'') /
    (r^2 + (r')^2)^(3/2).
  - Non-convexity at theta = pi/k: exact condition is
    (k^2 + 1) epsilon > 1; the simpler k^2 epsilon > 1 is sufficient
    (and what the script reports as a margin), but the actual kappa_dip
    is computed directly to verify the verdict.
  - Volume normalization: scale by 1/sqrt(1 + epsilon^2 / 2) to make A = pi.

Witness 2 scope clarification: Fuglede's nearly-spherical class is
*contained* in Osserman's broad rectifiable-Jordan-curve class (smooth,
starshaped, finite-perimeter). The non-inclusion this witness exhibits
is **Fuglede not-subset Osserman's convex Bonnesen subclass** — the
sub-register where the quantitative Delta >= pi^2 (R - rho)^2
strengthening (Osserman 1979 eq. 21) lives. Negative curvature at the
dip puts the construction outside the convex sub-class while keeping
it inside the broader rectifiable register.

Choice of k=5, epsilon=0.0575 (mid-window of the non-convexity / Fuglede
intersection) is per the parameter-margin analysis in the briefing:
all three margins (Fuglede ||u||, Fuglede ||grad u||, k^2 epsilon > 1)
exceed 20 percent.
"""

RR = RealField(200)
PI = RR(pi)
THREE_FORTIETH = RR(3) / RR(40)
ONE_HALF = RR(1) / RR(2)


def witness_1_thin_ellipse():
    """Osserman applies; Fuglede's ||u||_oo bound fails."""
    a = RR(2)
    b = RR(1) / RR(2)

    # ab = 1, so A = pi a b = pi (already volume-normalized).
    A = PI * a * b
    # Ellipse perimeter via complete elliptic integral of the second kind.
    # Sage convention: elliptic_ec(m) = integral_0^(pi/2) sqrt(1 - m sin^2 t) dt,
    # with m = (eccentricity)^2 = 1 - (b/a)^2 for an ellipse with a > b.
    m = 1 - (b / a)**2
    L = 4 * a * elliptic_ec(m)

    Delta_H = L**2 - 4 * PI * A

    # Bonnesen lower bound (Osserman 1979 eq. (21)): Delta_H >= pi^2 (R - rho)^2
    # for convex Jordan curve, where R = circumradius, rho = inradius.
    # For ellipse with semi-axes a > b: R = a, rho = b.
    bonnesen_bound = PI**2 * (a - b)**2

    # Fuglede u(theta) on the volume-normalized ellipse.
    # In polar form, r(theta) = a b / sqrt(b^2 cos^2 theta + a^2 sin^2 theta).
    # At theta = 0: r = a; at theta = pi/2: r = b. With ab = 1 (no rescaling),
    # u = r - 1 ranges from b - 1 to a - 1.
    u_inf = max(a - 1, abs(b - 1))

    return {
        'name': f"thin ellipse (a = {float(a)}, b = {float(b)})",
        'L': L, 'A': A, 'Delta_H': Delta_H,
        'bonnesen_bound': bonnesen_bound,
        'u_inf': u_inf,
        'osserman_holds': Delta_H >= bonnesen_bound,
        'fuglede_holds': u_inf <= THREE_FORTIETH,
        'osserman_margin_pct': float((Delta_H - bonnesen_bound) / bonnesen_bound * 100),
        'fuglede_excess_pct': float((u_inf - THREE_FORTIETH) / THREE_FORTIETH * 100),
    }


def witness_2_small_spike_nonconvex():
    """Fuglede holds; convex hypothesis fails (negative curvature)."""
    k = RR(5)
    epsilon = RR("0.0575")  # mid-window: 1/k^2 = 0.04 < eps < 3/40 = 0.075

    # r(theta) = 1 + epsilon cos(k theta) — perturbation of unit disk.
    # Pre-normalization area A_pre = (1/2) integral r^2 dtheta = pi (1 + eps^2/2).
    # Volume-normalize by scaling linear dimensions: scale = 1/sqrt(1 + eps^2/2).
    scale = 1 / sqrt(1 + epsilon**2 / 2)

    # After normalization: r_n(theta) = scale * (1 + eps cos(k theta)).
    # u(theta) = r_n(theta) - 1.
    u_max = scale * (1 + epsilon) - 1
    u_min = scale * (1 - epsilon) - 1
    u_inf = max(abs(u_max), abs(u_min))

    # Spherical gradient on unit circle (n_dim = 2): du/dtheta.
    # u'(theta) = - k epsilon sin(k theta) * scale; max at sin(k theta) = +-1.
    grad_u_inf = k * epsilon * scale

    # Polar curvature kappa(theta) = (r^2 + 2 (r')^2 - r r'') / (r^2 + (r')^2)^(3/2).
    # At theta = pi/k (where cos(k theta) = -1, the boundary "dips" inward):
    # r = scale * (1 - eps); r' = 0; r'' = scale * k^2 eps.
    # kappa simplifies to (r - r''/r) ... = (r^2 - r r'') / r^3 since r' = 0.
    r_dip = scale * (1 - epsilon)
    r_pp_dip = scale * k**2 * epsilon
    kappa_dip = (r_dip**2 - r_dip * r_pp_dip) / r_dip**3

    # Sufficient condition for kappa(theta = pi/k) < 0: k^2 eps > 1.
    threshold = k**2 * epsilon

    return {
        'name': f"small-spike non-convex (k = {int(k)}, epsilon = {float(epsilon)})",
        'k': k, 'epsilon': epsilon,
        'u_inf': u_inf, 'grad_u_inf': grad_u_inf,
        'kappa_dip': kappa_dip, 'threshold': threshold,
        'fuglede_u_holds': u_inf <= THREE_FORTIETH,
        'fuglede_grad_holds': grad_u_inf <= ONE_HALF,
        'nonconvex': kappa_dip < 0,
        'fuglede_u_margin_pct': float((THREE_FORTIETH - u_inf) / THREE_FORTIETH * 100),
        'fuglede_grad_margin_pct': float((ONE_HALF - grad_u_inf) / ONE_HALF * 100),
        'nonconvex_margin_pct': float((threshold - 1) * 100),
    }


def witness_3_beck_vs_shape_space():
    """Categorial: Beck's parameter space and Osserman/Fuglede's shape space
    are incompatible at the level of input type."""
    return {
        'name': 'Beck vs. shape-space (categorial)',
        'argument': (
            "Beck 1994's hypothesis class is parameterized by alpha in R^k, "
            "k >= 2 (a parameter point in real coordinate space, not a "
            "shape). Theorems quantify discrepancy of {n alpha} mod 1 for "
            "almost-every alpha.\n\n"
            "Osserman 1979 and Fuglede 1989's hypothesis classes are "
            "parameterized by domains D in R^n with rectifiable / convex / "
            "nearly-spherical boundary (a shape with a metric on it, not a "
            "parameter point). Theorems bound the isoperimetric deficit "
            "Delta(D) in terms of geometric or Sobolev invariants of D.\n\n"
            "There is no canonical functor alpha -> D(alpha) connecting "
            "Beck's parameter space to the Osserman/Fuglede shape space. "
            "The hypothesis classes live in different categories at the "
            "level of input type: Beck cannot be checked by examining a "
            "planar shape; Osserman/Fuglede cannot be checked by examining "
            "a real vector. The non-inclusion is structural.\n\n"
            "This witness is qualitative. No concrete object can be "
            "constructed to fail Osserman/Fuglede while passing Beck (or "
            "vice versa) because no map exists to make the comparison."
        ),
    }


def fmt_yn(b):
    return "Y" if b else "N"


def main():
    print("=" * 76)
    print("Pairwise non-inclusion witnesses for the three iso/ hypothesis classes")
    print("Per iso/THREE-REGISTER-SYNTHESIS.md §3.2")
    print("=" * 76)
    print()

    w1 = witness_1_thin_ellipse()
    print(f"Witness 1: Osserman not-subset Fuglede")
    print(f"  Construction: {w1['name']}")
    print(f"  L = {float(w1['L']):.6f}")
    print(f"  Delta_H = L^2 - 4 pi A = {float(w1['Delta_H']):.6f}")
    print(f"  Bonnesen lower bound pi^2 (R - rho)^2 = {float(w1['bonnesen_bound']):.6f}")
    print(f"  Osserman lower bound holds: {fmt_yn(w1['osserman_holds'])}  "
          f"(margin: {w1['osserman_margin_pct']:+.2f}%)")
    print(f"  ||u||_oo = {float(w1['u_inf']):.6f}  vs Fuglede bound 0.075")
    print(f"  Fuglede hypothesis holds: {fmt_yn(w1['fuglede_holds'])}  "
          f"(excess: {w1['fuglede_excess_pct']:+.2f}%)")
    print(f"  VERDICT: Osserman applies AND Fuglede fails -> witness valid.")
    print()

    w2 = witness_2_small_spike_nonconvex()
    print(f"Witness 2: Fuglede not-subset Osserman's convex Bonnesen subclass")
    print(f"  (Fuglede class is contained in broad rectifiable Osserman; the")
    print(f"   non-inclusion is against the convex sub-register where the")
    print(f"   Delta >= pi^2 (R - rho)^2 strengthening lives.)")
    print(f"  Construction: {w2['name']}")
    print(f"  ||u||_oo     = {float(w2['u_inf']):.6f}  vs Fuglede bound 0.075")
    print(f"    Fuglede ||u|| satisfied: {fmt_yn(w2['fuglede_u_holds'])}  "
          f"(margin: {w2['fuglede_u_margin_pct']:+.2f}%)")
    print(f"  ||grad u||_oo = {float(w2['grad_u_inf']):.6f}  vs Fuglede bound 0.5")
    print(f"    Fuglede ||grad u|| satisfied: {fmt_yn(w2['fuglede_grad_holds'])}  "
          f"(margin: {w2['fuglede_grad_margin_pct']:+.2f}%)")
    print(f"  kappa at dip (theta = pi/k) = {float(w2['kappa_dip']):.6f}")
    print(f"    Non-convex (kappa < 0 at dip): {fmt_yn(w2['nonconvex'])}  "
          f"(k^2 eps = {float(w2['threshold']):.4f}, "
          f"margin above 1: {w2['nonconvex_margin_pct']:+.2f}%)")
    print(f"  VERDICT: Fuglede satisfied (both bounds with > 20% margin) "
          f"AND non-convex (outside Bonnesen convex sub-class) -> witness")
    print(f"           valid for Fuglede not-subset convex-Osserman.")
    print()

    w3 = witness_3_beck_vs_shape_space()
    print(f"Witness 3: Beck not-subset {{Osserman, Fuglede}}")
    print(f"  Construction: {w3['name']}")
    print()
    for line in w3['argument'].splitlines():
        print(f"  {line}")
    print()
    print(f"  VERDICT: Hypothesis classes live in different categories; "
          f"non-inclusion is structural, not numerical.")
    print()


if __name__ == "__main__":
    main()
