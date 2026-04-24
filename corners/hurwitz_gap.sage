"""
Hurwitz isoperimetric gap for the inscribed regular n-gon.

Closes step 1 of `memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md`
§"Proposed order of work":
    - closed-form Fourier coefficients of the regular n-gon's
      arc-length parametrization,
    - Hurwitz identity (Parseval) closure check against the elementary
      isoperimetric gap,
    - rate comparison against the Archimedean leading term 4π⁴/(3n²),
    - per-frequency-band decomposition of the gap.

Background.
For a simple closed curve γ: [0, L] → ℂ parametrized by arc length, with
complex Fourier series γ(s) = Σ c_m e^{2πi m s / L}, the Hurwitz
isoperimetric identity is
    L² − 4π A = 4π² Σ_{m ∈ ℤ} m(m−1) |c_m|²,
with equality iff c_m = 0 for every m ∉ {0, 1}. The equality case is
the circle; the isoperimetric gap L² − 4π A measures distance-from-circle
in Fourier-Parseval norm.

For the inscribed regular n-gon in the unit circle, the tangent on
edge k is T_k = ω^k · i e^{πi/n} where ω = e^{2πi/n}. A geometric-sum
calculation gives
    c_m = 0        unless  m ≡ 1 (mod n),
    c_m = L_n² / (4π² m²)    for m = 1 + j·n,  j ∈ ℤ,
where L_n = 2n sin(π/n) is the polygon's perimeter.

Sanity identity (closed form):
    Δ_n  :=  L_n² − 4π A_n  =  L_n² · [1 − (π/n) cot(π/n)].
Asymptote: Δ_n = 4π⁴/(3n²) + O(1/n⁴).

Produces three figures:
    figures/hurwitz_gap_rate.png
    figures/hurwitz_gap_frequency_decomposition.png
    figures/hurwitz_gap_coefficients.png
"""

import os
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


# --- closed-form primitives ---------------------------------------------

def L_n(n):
    """Perimeter of the inscribed regular n-gon in the unit circle."""
    return 2.0 * n * math.sin(math.pi / n)


def A_n(n):
    """Area of the inscribed regular n-gon in the unit circle."""
    return 0.5 * n * math.sin(2.0 * math.pi / n)


def delta_elementary(n):
    """Isoperimetric gap Δ_n = L_n² − 4π A_n from elementary geometry."""
    return L_n(n) ** 2 - 4.0 * math.pi * A_n(n)


def delta_closed_form(n):
    """Δ_n = L_n² · [1 − (π/n) cot(π/n)], equal to the elementary form."""
    return L_n(n) ** 2 * (1.0 - (math.pi / n) / math.tan(math.pi / n))


def c_m(n, m):
    """Fourier coefficient c_m of the arc-length parametrization of the
    inscribed regular n-gon in the unit circle. Zero unless m ≡ 1 (mod n);
    for m = 1 + j·n, equal to L_n² / (4π² m²)."""
    if m == 0 or (m - 1) % n != 0:
        return 0.0
    return L_n(n) ** 2 / (4.0 * math.pi ** 2 * m * m)


# --- Parseval / Hurwitz checks ------------------------------------------

def parseval_norm(n, jmax=400):
    """Truncated Σ m² |c_m|² summed over m = 1 + j·n, |j| ≤ jmax.
    Should equal (L_n / (2π))² in the limit."""
    total = 0.0
    for j in range(-jmax, jmax + 1):
        m = 1 + j * n
        cm = c_m(n, m)
        total += m * m * cm * cm
    return total


def parseval_norm_target(n):
    """(L_n / (2π))²."""
    return (L_n(n) / (2.0 * math.pi)) ** 2


def delta_parseval(n, jmax=400):
    """Truncated 4π² Σ m(m−1) |c_m|² over m = 1 + j·n, |j| ≤ jmax, j ≠ 0."""
    total = 0.0
    for j in range(-jmax, jmax + 1):
        if j == 0:
            continue
        m = 1 + j * n
        cm = c_m(n, m)
        total += m * (m - 1) * cm * cm
    return 4.0 * math.pi ** 2 * total


def delta_by_band(n, jmax):
    """Contribution to Δ_n from each band |j| = 1, 2, …, jmax (summed over ±j)."""
    bands = {}
    for j in range(1, jmax + 1):
        band_total = 0.0
        for sign in (1, -1):
            m = 1 + sign * j * n
            cm = c_m(n, m)
            band_total += m * (m - 1) * cm * cm
        bands[j] = 4.0 * math.pi ** 2 * band_total
    return bands


# --- figure 1: rate -----------------------------------------------------

def plot_rate(outpath):
    ns = np.arange(3, 101)
    elem = np.array([delta_elementary(int(n)) for n in ns])
    pars = np.array([delta_parseval(int(n), jmax=400) for n in ns])
    leading = 4.0 * math.pi ** 4 / (3.0 * ns.astype(float) ** 2)

    residual = np.abs(elem - pars) / np.abs(elem)
    residual = np.where(residual > 0, residual, 1e-17)

    fig, (ax, axr) = plt.subplots(
        2, 1, figsize=(11.5, 8.5),
        gridspec_kw={"height_ratios": [3.0, 1.0], "hspace": 0.09},
        sharex=True,
    )

    # --- main panel --------------------------------------------------------
    ax.loglog(ns, leading, ls="--", lw=2.0, color="0.4", zorder=1,
              label=r"$4\pi^4 / (3 n^2)$   —   Archimedean leading term")
    ax.loglog(ns, elem, marker="o", ms=7, lw=0, color="#2c5d8f",
              markeredgecolor="black", markeredgewidth=0.35, zorder=3,
              label=r"$\Delta_n = L_n^2 - 4\pi A_n$   —   elementary")
    ax.loglog(ns, pars, marker="+", ms=13, mew=1.7, lw=0, color="#c0392b",
              zorder=4,
              label=r"$4\pi^2 \sum_m m(m-1)\,|c_m^{(n)}|^2$   —   Parseval, $|j| \leq 400$")

    ax.set_ylabel(r"$\Delta_n$", fontsize=13)
    ax.grid(True, which="major", color="0.92", lw=0.55)
    ax.grid(True, which="minor", color="0.97", lw=0.35)
    ax.legend(loc="lower left", framealpha=0.94,
              edgecolor="0.8", fontsize=10.5,
              title="series", title_fontsize=11)
    ax.tick_params(labelbottom=False)
    ax.set_xlim(ns.min(), ns.max())

    # --- residual panel ----------------------------------------------------
    axr.semilogx(ns, residual, color="#6c3483", lw=1.3, zorder=3)
    axr.scatter(ns, residual, color="#6c3483", s=16, zorder=4,
                edgecolors="black", linewidths=0.3)
    axr.set_xlabel(r"polygon order   $n$", fontsize=13)
    axr.set_ylabel("relative\nresidual", fontsize=10.5)
    axr.grid(True, which="major", color="0.92", lw=0.55)
    axr.grid(True, which="minor", color="0.97", lw=0.35)
    axr.set_xlim(ns.min(), ns.max())
    axr.ticklabel_format(style="sci", axis="y", scilimits=(0, 0))

    floor_val = residual[-1]
    axr.axhline(floor_val, ls=":", lw=1.0, color="0.5", alpha=0.8, zorder=2)
    axr.annotate(
        fr"asymptote $\approx {floor_val:.2e}$:   $|j| > 400$ truncation tail",
        xy=(90, floor_val), xytext=(0.04, 0.70),
        textcoords="axes fraction",
        fontsize=10, color="#4a2a57",
        arrowprops=dict(arrowstyle="->", color="#4a2a57", lw=0.8, alpha=0.75),
    )

    # --- titles ------------------------------------------------------------
    fig.suptitle(
        r"Hurwitz isoperimetric gap:   $\Delta_n = L_n^{\,2} - 4\pi A_n$   "
        r"for the inscribed regular $n$-gon",
        fontsize=14, fontweight="bold", y=0.995,
    )
    fig.text(
        0.5, 0.945,
        r"elementary geometry, Parseval Fourier, and the Archimedean leading term "
        r"$4\pi^{4}/(3n^{2})$ agree on the $1/n^{2}$ rate",
        ha="center", fontsize=10.5, color="0.3", style="italic",
    )
    fig.text(
        0.5, 0.018,
        r"Parseval closure check: elementary and truncated Fourier agree to the $|j| = 400$ tail   "
        r"($\sim 1.55 \times 10^{-3}$ relative, monotone in $n$)",
        ha="center", fontsize=9.5, color="0.35", style="italic",
    )

    plt.tight_layout(rect=[0.0, 0.04, 1.0, 0.93])
    plt.savefig(outpath, dpi=170, bbox_inches="tight")
    plt.close(fig)


# --- figure 2: frequency decomposition ----------------------------------

def plot_frequency_decomposition(outpath, jmax=6):
    ns = np.arange(3, 101)
    totals = np.array([delta_parseval(int(n), jmax=400) for n in ns])

    bands = {}
    for j in range(1, jmax + 1):
        bands[j] = np.array([delta_by_band(int(n), jmax)[j] for n in ns])
    tail = totals - sum(bands[j] for j in range(1, jmax + 1))

    fig, ax = plt.subplots(figsize=(11, 7))

    bottom = np.zeros_like(ns, dtype=float)
    cmap = plt.get_cmap("viridis")
    for j in range(1, jmax + 1):
        fraction = bands[j] / totals
        ax.fill_between(ns, bottom, bottom + fraction,
                        color=cmap((j - 1) / max(jmax - 1, 1)),
                        alpha=0.88, label=r"$|j| = %d$  ($m = 1 \pm %dn$)" % (j, j))
        bottom = bottom + fraction
    # residual tail (j > jmax)
    tail_fraction = tail / totals
    ax.fill_between(ns, bottom, bottom + tail_fraction,
                    color="0.75", alpha=0.55, label=r"$|j| > %d$  (tail)" % jmax)

    ax.set_xlabel(r"$n$", fontsize=12)
    ax.set_ylabel(r"fraction of $\Delta_n$ carried by band", fontsize=12)
    ax.set_title(
        "Hurwitz gap by frequency band:\n"
        r"contribution of $m \in \{1 \pm j n\}$ to $\Delta_n$, stacked over $|j| = 1, \ldots, %d$" % jmax,
        fontsize=12,
    )
    ax.set_ylim(0, 1.02)
    ax.set_xlim(ns.min(), ns.max())
    ax.grid(True, color="0.9", lw=0.4)
    ax.legend(loc="center right", framealpha=0.95, title="band index",
              title_fontsize=10, fontsize=9)

    plt.tight_layout()
    plt.savefig(outpath, dpi=170)
    plt.close(fig)


# --- figure 3: coefficient decay ----------------------------------------

def plot_coefficients(outpath):
    sample_ns = [3, 7, 12, 30]
    fig, ax = plt.subplots(figsize=(11, 7))

    cmap = plt.get_cmap("viridis")
    for i, n in enumerate(sample_ns):
        color = cmap(i / max(len(sample_ns) - 1, 1))

        # admissible positive m: m = 1 + j·n for j = 0, 1, …
        js = list(range(0, 25))
        ms_pos = [1 + j * n for j in js if 1 + j * n > 0]
        abs_cms = [abs(c_m(n, m)) for m in ms_pos]
        ax.loglog(ms_pos, abs_cms, marker="o", ms=6, lw=1.3, color=color,
                  label=f"n = {n}")

        # envelope  L_n² / (4π² m²)  plotted as dotted guide
        ms_env = np.array(ms_pos)
        env = L_n(n) ** 2 / (4.0 * math.pi ** 2 * ms_env ** 2)
        ax.loglog(ms_env, env, ls=":", color=color, lw=0.9, alpha=0.5)

    ax.set_xlabel(r"$m$  (admissible frequencies: $m \equiv 1\ (\mathrm{mod}\ n)$, $m > 0$)",
                  fontsize=12)
    ax.set_ylabel(r"$|c_m^{(n)}|$", fontsize=12)
    ax.set_title(
        "Fourier coefficient decay along the admissible lattice\n"
        r"$|c_m^{(n)}| = L_n^2 / (4\pi^2 m^2)$  for  $m \in 1 + n\mathbb{Z}$,"
        r"  zero off that lattice",
        fontsize=12,
    )
    ax.grid(True, which="both", color="0.9", lw=0.4)
    ax.legend(loc="upper right", framealpha=0.95, title="polygon order",
              title_fontsize=10, fontsize=10)

    plt.tight_layout()
    plt.savefig(outpath, dpi=170)
    plt.close(fig)


# --- entry point --------------------------------------------------------

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "figures"))
    os.makedirs(figdir, exist_ok=True)

    # --- Parseval norm sanity (Σ m² |c_m|² =? (L_n/(2π))²) ---
    print("Parseval norm check: Σ m² |c_m|²  vs  (L_n/(2π))²")
    for n in (3, 5, 7, 10, 30, 100):
        lhs = parseval_norm(n, jmax=400)
        rhs = parseval_norm_target(n)
        rel = abs(lhs - rhs) / rhs
        print(f"  n={n:>4}: lhs={lhs:.14f}  rhs={rhs:.14f}  rel.diff={rel:.2e}")

    # --- Hurwitz identity closure (elementary vs closed-form vs Parseval) ---
    print("\nHurwitz identity: elementary vs closed-form vs Parseval-truncated")
    for n in (3, 5, 7, 10, 30, 100):
        elem = delta_elementary(n)
        clos = delta_closed_form(n)
        pars = delta_parseval(n, jmax=400)
        print(f"  n={n:>4}: elem={elem:.12e}  closed={clos:.12e}  "
              f"parseval={pars:.12e}  rel(elem vs parseval)={abs(elem-pars)/elem:.2e}")

    # --- figures ---
    rate_path = os.path.join(figdir, "hurwitz_gap_rate.png")
    freq_path = os.path.join(figdir, "hurwitz_gap_frequency_decomposition.png")
    coef_path = os.path.join(figdir, "hurwitz_gap_coefficients.png")

    plot_rate(rate_path)
    print(f"\nwrote {rate_path}")
    plot_frequency_decomposition(freq_path)
    print(f"wrote {freq_path}")
    plot_coefficients(coef_path)
    print(f"wrote {coef_path}")


if __name__ == "__main__":
    main()
