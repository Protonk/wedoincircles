"""
Hurwitz isoperimetric gap for the circumscribed regular n-gon, paired
with the inscribed companion at corners/hurwitz_gap.sage.

Closes the optional follow-on to steps 1-2 of
`memos/KRAFT-HERMITE-LINDEMANN-AITCHISON.md` §"Proposed order of work":
the inscribed-side script does the sin-side calculation; this script
does the tan-side calculation and exposes the Archimedean squeeze
(both gaps -> 4 pi^4 / (3 n^2)) in a single comparison figure.

Background.
The circumscribed regular n-gon to the unit circle has its incircle on
the unit circle and edges tangent to it. Its perimeter and area are

    L_n^circ = 2 n tan(pi / n),
    A_n^circ = n tan(pi / n).

The isoperimetric gap closes to the same bracket factor as the inscribed
side:

    Delta_n^circ = (L_n^circ)^2 - 4 pi A_n^circ
                 = (L_n^circ)^2 . [1 - (pi/n) cot(pi/n)].

The ratio of the two gaps is

    Delta_n^circ / Delta_n^insc = (L_n^circ / L_n^insc)^2 = sec^2(pi/n),

which approaches 1 as n -> infty. Both sides therefore converge to the
common Archimedean leading term 4 pi^4 / (3 n^2); the regular n-gon
sits between them in a polynomial-rate squeeze. This is the Dido /
Archimedes pairing the inscribed-side script alone could not show.

For the arc-length Fourier coefficients of the circumscribed n-gon,
the support pattern is the same as inscribed (m == 1 mod n). The
magnitudes satisfy

    |c_m^circ| = L_n^insc . L_n^circ / (4 pi^2 m^2)
               = sec(pi/n) . |c_m^insc|,

so the Parseval norm target lifts from (L_n^insc/(2 pi))^2 to
(L_n^circ/(2 pi))^2 correctly. The first-band concentration ratio
B_1(n) / Delta_n -> 6/pi^2 inherits unchanged: paired-band terms scale
by the same sec^2(pi/n) factor as the gap, so the inscribed-side
constants of corners/HURWITZ-FIRST-BAND-CONCENTRATION.md transfer
verbatim to the circumscribed side.

Produces one figure:
    figures/hurwitz_gap_archimedean_squeeze.png
"""

import os
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


# --- inscribed primitives (mirrors corners/hurwitz_gap.sage) ----------

def L_n_insc(n):
    """Perimeter of the inscribed regular n-gon in the unit circle."""
    return 2.0 * n * math.sin(math.pi / n)


def A_n_insc(n):
    """Area of the inscribed regular n-gon in the unit circle."""
    return 0.5 * n * math.sin(2.0 * math.pi / n)


def delta_elementary_insc(n):
    return L_n_insc(n) ** 2 - 4.0 * math.pi * A_n_insc(n)


# --- circumscribed primitives -----------------------------------------

def L_n_circ(n):
    """Perimeter of the circumscribed regular n-gon (incircle = unit)."""
    return 2.0 * n * math.tan(math.pi / n)


def A_n_circ(n):
    """Area of the circumscribed regular n-gon (incircle = unit)."""
    return n * math.tan(math.pi / n)


def delta_elementary_circ(n):
    """Δ_n^circ = (L_n^circ)^2 - 4 pi A_n^circ from elementary geometry."""
    return L_n_circ(n) ** 2 - 4.0 * math.pi * A_n_circ(n)


def delta_closed_form_circ(n):
    """Δ_n^circ = (L_n^circ)^2 . [1 - (pi/n) cot(pi/n)]; equal to elementary."""
    return L_n_circ(n) ** 2 * (1.0 - (math.pi / n) / math.tan(math.pi / n))


def c_m_circ(n, m):
    """Magnitude of arc-length Fourier coefficient c_m for the
    circumscribed regular n-gon. Zero unless m == 1 (mod n); for
    m = 1 + j n, equal to L_n^insc . L_n^circ / (4 pi^2 m^2)."""
    if m == 0 or (m - 1) % n != 0:
        return 0.0
    return L_n_insc(n) * L_n_circ(n) / (4.0 * math.pi ** 2 * m * m)


# --- Parseval / Hurwitz checks (circumscribed side) -------------------

def parseval_norm_circ(n, jmax=400):
    """Truncated Σ m^2 |c_m^circ|^2; converges to (L_n^circ/(2 pi))^2."""
    total = 0.0
    for j in range(-jmax, jmax + 1):
        m = 1 + j * n
        cm = c_m_circ(n, m)
        total += m * m * cm * cm
    return total


def parseval_norm_target_circ(n):
    """(L_n^circ / (2 pi))^2."""
    return (L_n_circ(n) / (2.0 * math.pi)) ** 2


def delta_parseval_circ(n, jmax=400):
    """Truncated 4 pi^2 Σ m(m-1) |c_m^circ|^2 over m = 1 + j n, j != 0."""
    total = 0.0
    for j in range(-jmax, jmax + 1):
        if j == 0:
            continue
        m = 1 + j * n
        cm = c_m_circ(n, m)
        total += m * (m - 1) * cm * cm
    return 4.0 * math.pi ** 2 * total


# --- figure: Archimedean squeeze ---------------------------------------

def plot_archimedean_squeeze(outpath):
    ns = np.arange(3, 101)
    elem_insc = np.array([delta_elementary_insc(int(n)) for n in ns])
    elem_circ = np.array([delta_elementary_circ(int(n)) for n in ns])
    pars_circ = np.array([delta_parseval_circ(int(n), jmax=400) for n in ns])
    leading = 4.0 * math.pi ** 4 / (3.0 * ns.astype(float) ** 2)

    ratio = elem_circ / elem_insc            # = sec^2(pi/n)
    ratio_target = 1.0 / np.cos(math.pi / ns) ** 2
    ratio_residual = np.abs(ratio - ratio_target) / ratio_target
    ratio_residual = np.where(ratio_residual > 0, ratio_residual, 1e-17)

    fig, (ax, axr) = plt.subplots(
        2, 1, figsize=(11.5, 8.5),
        gridspec_kw={"height_ratios": [3.0, 1.0], "hspace": 0.09},
        sharex=True,
    )

    # --- main panel: both gaps + leading term ----------------------------
    ax.loglog(ns, leading, ls="--", lw=2.0, color="0.4", zorder=1,
              label=r"$4\pi^4 / (3 n^2)$   —   Archimedean leading term")
    ax.loglog(ns, elem_insc, marker="o", ms=7, lw=0, color="#2c5d8f",
              markeredgecolor="black", markeredgewidth=0.35, zorder=3,
              label=r"$\Delta_n^{\mathrm{insc}} = (L_n^{\mathrm{insc}})^2 - 4\pi A_n^{\mathrm{insc}}$")
    ax.loglog(ns, elem_circ, marker="^", ms=8, lw=0, color="#c0392b",
              markeredgecolor="black", markeredgewidth=0.35, zorder=4,
              label=r"$\Delta_n^{\mathrm{circ}} = (L_n^{\mathrm{circ}})^2 - 4\pi A_n^{\mathrm{circ}}$")
    ax.loglog(ns, pars_circ, marker="+", ms=11, mew=1.5, lw=0, color="#7d3c98",
              zorder=5,
              label=r"$4\pi^2 \sum m(m{-}1)|c_m^{\mathrm{circ}}|^2$   —   Parseval, $|j| \leq 400$")

    ax.set_ylabel(r"$\Delta_n$", fontsize=13)
    ax.grid(True, which="major", color="0.92", lw=0.55)
    ax.grid(True, which="minor", color="0.97", lw=0.35)
    ax.legend(loc="lower left", framealpha=0.94,
              edgecolor="0.8", fontsize=10.5,
              title="series", title_fontsize=11)
    ax.tick_params(labelbottom=False)
    ax.set_xlim(ns.min(), ns.max())

    # --- residual panel: ratio vs sec^2(pi/n) ----------------------------
    axr.loglog(ns, ratio_residual, color="#6c3483", lw=1.3, zorder=3)
    axr.scatter(ns, ratio_residual, color="#6c3483", s=16, zorder=4,
                edgecolors="black", linewidths=0.3)
    axr.set_xlabel(r"polygon order   $n$", fontsize=13)
    axr.set_ylabel(r"$|\Delta^{\mathrm{circ}}/\Delta^{\mathrm{insc}}$" "\n"
                   r"$- \sec^2(\pi/n)| \,/\, \sec^2(\pi/n)$", fontsize=9)
    axr.grid(True, which="major", color="0.92", lw=0.55)
    axr.grid(True, which="minor", color="0.97", lw=0.35)
    axr.set_xlim(ns.min(), ns.max())

    # --- titles ----------------------------------------------------------
    fig.suptitle(
        r"Archimedean squeeze:   $\Delta_n^{\mathrm{insc}}$,  $\Delta_n^{\mathrm{circ}}$,  "
        r"and the common leading term $4\pi^4/(3n^2)$",
        fontsize=14, fontweight="bold", y=0.995,
    )
    fig.text(
        0.5, 0.945,
        r"both gaps $\to 4\pi^4/(3n^2)$ at the same rate;   "
        r"$\Delta_n^{\mathrm{circ}}/\Delta_n^{\mathrm{insc}} = \sec^2(\pi/n) \to 1$",
        ha="center", fontsize=10.5, color="0.3", style="italic",
    )
    fig.text(
        0.5, 0.018,
        r"residual panel: $\Delta^{\mathrm{circ}}/\Delta^{\mathrm{insc}}$ matches "
        r"$\sec^2(\pi/n)$ to floating-point;   "
        r"Parseval check on the circumscribed side mirrors the inscribed-side closure.",
        ha="center", fontsize=9.5, color="0.35", style="italic",
    )

    plt.tight_layout(rect=[0.0, 0.04, 1.0, 0.93])
    plt.savefig(outpath, dpi=170, bbox_inches="tight")
    plt.close(fig)


# --- entry point ------------------------------------------------------

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "figures"))
    os.makedirs(figdir, exist_ok=True)

    # --- Parseval norm sanity (circumscribed side) ---
    print("Circumscribed Parseval norm: Σ m^2 |c_m^circ|^2  vs  (L_n^circ/(2 pi))^2")
    for n in (3, 5, 7, 10, 30, 100):
        lhs = parseval_norm_circ(n, jmax=400)
        rhs = parseval_norm_target_circ(n)
        rel = abs(lhs - rhs) / rhs
        print(f"  n={n:>4}: lhs={lhs:.14f}  rhs={rhs:.14f}  rel.diff={rel:.2e}")

    # --- Hurwitz identity closure (circumscribed side) ---
    print("\nCircumscribed Hurwitz: elementary vs closed-form vs Parseval-truncated")
    for n in (3, 5, 7, 10, 30, 100):
        elem = delta_elementary_circ(n)
        clos = delta_closed_form_circ(n)
        pars = delta_parseval_circ(n, jmax=400)
        rel = abs(elem - pars) / elem
        print(f"  n={n:>4}: elem={elem:.12e}  closed={clos:.12e}  "
              f"parseval={pars:.12e}  rel(elem vs parseval)={rel:.2e}")

    # --- Archimedean squeeze: Δ^circ / Δ^insc = sec^2(pi/n) ---
    print("\nArchimedean squeeze ratio: Δ^circ/Δ^insc  vs  sec^2(pi/n)")
    for n in (3, 5, 7, 10, 30, 100):
        ratio = delta_elementary_circ(n) / delta_elementary_insc(n)
        target = 1.0 / math.cos(math.pi / n) ** 2
        rel = abs(ratio - target) / target
        print(f"  n={n:>4}: ratio={ratio:.12f}  sec^2(pi/n)={target:.12f}  "
              f"rel.diff={rel:.2e}")

    # --- figure ---
    sq_path = os.path.join(figdir, "hurwitz_gap_archimedean_squeeze.png")
    plot_archimedean_squeeze(sq_path)
    print(f"\nwrote {sq_path}")


if __name__ == "__main__":
    main()
