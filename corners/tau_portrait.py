"""
τ(n) portrait — the circle-side residue.

Closes the τ-stem-plot bullet in `memos/COUNTING-APPARATUS.md` §(C)
"What's missing for the portrait."

τ is the circle-side residue (analog of Landfall's ε(m) on the log side):

    τ(n) = 2·cos(2π/n) − round(2·cos(2π/n))    ∈ [−1/2, 1/2]

Facts visible in the portrait:

  - Zeros at n ∈ {1, 2, 3, 4, 6} — the Niven / crystallographic set.
    (2·cos(2π/n) is integer exactly on this set.)
  - For n ∉ {1, 2, 3, 4, 6}, τ is algebraic of degree φ(n)/2 over ℚ.
    (Not φ(2n)/2 — that is the degree of cos(π/n), a different object
    hosted at `corners/PSEUDO-CHEBYSHEV-NODES.md`.)
  - Positive bulge: 2·cos(2π/n) crosses 3/2 at n ≈ 8.69, so the rounding
    direction flips between n = 8 and n = 9. τ > 0 only at n ∈ {7, 8}.
  - Large-n decay: 2·cos(2π/n) = 2 − 4π²/n² + O(1/n⁴), so for n ≥ 9,
    τ(n) = −4π²/n² + O(1/n⁴).  Same Taylor-tail 1/n² rate as the Hurwitz
    isoperimetric gap at `corners/hurwitz_gap.sage`.

Two panels: stem plot on linear y (the portrait proper); |τ(n)| on
log-log with the 4π²/n² asymptote overlaid.
"""

import math
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np


# --- primitives -----------------------------------------------------------

NIVEN_ZEROS = {1, 2, 3, 4, 6}
N_MIN = 3
N_MAX = 60


def euler_phi(m):
    if m <= 0:
        return 0
    result = m
    temp = m
    p = 2
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result -= result // p
        p += 1
    if temp > 1:
        result -= result // temp
    return result


def algebraic_degree(n):
    """Degree of 2·cos(2π/n) over ℚ:  1 on the Niven set, else φ(n)/2."""
    if n in NIVEN_ZEROS:
        return 1
    return euler_phi(n) // 2


def tau(n):
    if n in NIVEN_ZEROS:
        return 0.0
    v = 2.0 * math.cos(2.0 * math.pi / n)
    return v - round(v)


# --- color scheme ---------------------------------------------------------

DEGREE_COLORS = {
    1: "#2c7a2c",  # green — Niven zeros
    2: "#2c5d8f",  # navy
    3: "#d1495b",  # orange-red — first cubic at n = 7
    4: "#168e4f",  # teal
    5: "#7a2c7a",  # purple
    6: "#d4a017",  # gold
}
HIGH_DEG_COLOR = "#888888"  # gray — deg ≥ 7


def degree_color(deg):
    return DEGREE_COLORS.get(deg, HIGH_DEG_COLOR)


# --- data -----------------------------------------------------------------

def compute_data():
    rows = []
    for n in range(N_MIN, N_MAX + 1):
        rows.append({
            "n": n,
            "tau": tau(n),
            "degree": algebraic_degree(n),
        })
    return rows


def _ns_by_degree(rows, deg):
    return [r["n"] for r in rows if r["degree"] == deg]


# --- plot -----------------------------------------------------------------

def plot_portrait(rows, outpath):
    ns = np.array([r["n"] for r in rows])
    taus = np.array([r["tau"] for r in rows])
    degs = np.array([r["degree"] for r in rows])

    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(14, 9),
        gridspec_kw={"height_ratios": [1.7, 1], "hspace": 0.30},
    )

    # --- panel 1: stem plot ---

    ax1.axhline(0, color="0.4", lw=0.9, zorder=1)
    ax1.axhline(0.5, color="0.75", lw=0.8, ls="--", zorder=1)
    ax1.axhline(-0.5, color="0.75", lw=0.8, ls="--", zorder=1)

    for r in rows:
        n = r["n"]
        t = r["tau"]
        d = r["degree"]
        color = degree_color(d)

        if n in NIVEN_ZEROS:
            ax1.plot([n], [0], marker="*", ms=18, color=color,
                     markeredgecolor="black", markeredgewidth=0.7,
                     zorder=7)
        else:
            ax1.vlines(n, 0, t, color=color, lw=1.7, zorder=4, alpha=0.9)
            ax1.plot([n], [t], marker="o", ms=6.5, color=color,
                     markeredgecolor="black", markeredgewidth=0.45,
                     zorder=5)

    ax1.annotate(
        "Niven zeros\n(crystallographic set $\\{3, 4, 6\\}$)",
        xy=(4.5, 0.015), xytext=(6.5, 0.33),
        fontsize=9, color="#2c7a2c",
        arrowprops=dict(arrowstyle="->", color="#2c7a2c", lw=0.8),
    )
    ax1.annotate(
        "positive bulge:  $n \\in \\{7, 8\\}$",
        xy=(7.5, 0.34), xytext=(16, 0.45),
        fontsize=9.5, color="#b03030",
        arrowprops=dict(arrowstyle="->", color="#b03030", lw=0.8),
    )
    ax1.annotate(
        "sign flip at $n = 9$\n$2\\cos(2\\pi/n)$ crosses $3/2$",
        xy=(9, -0.45), xytext=(16, -0.28),
        fontsize=9, color="#b03030",
        arrowprops=dict(arrowstyle="->", color="#b03030", lw=0.8),
    )
    ax1.annotate(
        r"$\tau(n) \to 0^-$  at rate  $-4\pi^2/n^2$",
        xy=(58, -0.015), xytext=(44, -0.22),
        fontsize=9.5, color="0.25",
        arrowprops=dict(arrowstyle="->", color="0.35", lw=0.8),
    )

    ax1.set_xlim(N_MIN - 0.8, N_MAX + 0.8)
    ax1.set_ylim(-0.60, 0.60)
    ax1.set_ylabel(r"$\tau(n) = 2\cos(2\pi/n) - \mathrm{round}(\cdot)$",
                   fontsize=11)
    ax1.set_title("circle-side residue at integer $n$, colored by algebraic degree",
                  fontsize=11.5, loc="left")
    ax1.grid(True, axis="x", color="0.96", lw=0.4)
    ax1.tick_params(labelbottom=False)

    legend_items = [
        Patch(facecolor=DEGREE_COLORS[1],  label=r"deg 1  —  Niven zeros $\{3, 4, 6\}$"),
        Patch(facecolor=DEGREE_COLORS[2],  label=r"deg 2  —  $n \in \{5, 8, 10, 12\}$"),
        Patch(facecolor=DEGREE_COLORS[3],  label=r"deg 3  —  $n \in \{7, 9, 14, 18\}$   [first cubic]"),
        Patch(facecolor=DEGREE_COLORS[4],  label=r"deg 4  —  $n \in \{15, 16, 20, 24, 30\}$"),
        Patch(facecolor=DEGREE_COLORS[5],  label=r"deg 5  —  $n \in \{11, 22, 25, 33\}$"),
        Patch(facecolor=DEGREE_COLORS[6],  label=r"deg 6  —  $n \in \{13, 21, 26, 28, 36\}$"),
        Patch(facecolor=HIGH_DEG_COLOR,    label=r"deg $\geq 7$  (higher-degree tail)"),
    ]
    ax1.legend(handles=legend_items, loc="lower right", framealpha=0.95,
               fontsize=8.5, title=r"algebraic degree  $\varphi(n)/2$",
               title_fontsize=9, ncol=2)

    # --- panel 2: |τ(n)| log-log decay ---

    nonzero_mask = np.array([r["n"] not in NIVEN_ZEROS for r in rows])
    ns_nz = ns[nonzero_mask]
    abs_taus_nz = np.abs(taus[nonzero_mask])
    degs_nz = degs[nonzero_mask]

    n_dense = np.linspace(max(5, N_MIN), N_MAX, 300)
    ref = 4.0 * math.pi ** 2 / n_dense ** 2
    ax2.loglog(n_dense, ref, ls="--", color="0.3", lw=1.3,
               label=r"$4\pi^2 / n^2$   (Taylor-tail asymptote)")

    for n, at, d in zip(ns_nz, abs_taus_nz, degs_nz):
        ax2.loglog([n], [at], marker="o", ms=6.5,
                   color=degree_color(d),
                   markeredgecolor="black", markeredgewidth=0.45,
                   zorder=5)

    ax2.set_xlabel(r"polygon order  $n$", fontsize=12)
    ax2.set_ylabel(r"$|\tau(n)|$", fontsize=11)
    ax2.set_title(r"$|\tau(n)|$ on log–log: approach to the Taylor-tail asymptote $4\pi^2/n^2$",
                  fontsize=11.5, loc="left")
    ax2.grid(True, which="both", color="0.93", lw=0.4)
    ax2.legend(loc="lower left", framealpha=0.95, fontsize=9)
    ax2.set_xlim(4, N_MAX + 2)

    # --- overall titles ---

    fig.suptitle(
        r"$\tau(n)$ portrait:  the circle-side residue,  $n \in [3, 60]$",
        fontsize=14, fontweight="bold", y=0.995,
    )
    fig.text(
        0.5, 0.010,
        r"analog of Landfall's  $\varepsilon(m)$;  zeros at the crystallographic set;"
        r"  large-$n$ decay at the same $1/n^2$ Taylor rate as the Hurwitz isoperimetric gap",
        ha="center", fontsize=9.5, color="0.35", style="italic",
    )

    plt.tight_layout(rect=[0.0, 0.030, 1.0, 0.965])
    plt.savefig(outpath, dpi=170)
    plt.close(fig)


# --- entry point ----------------------------------------------------------

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "figures"))
    os.makedirs(figdir, exist_ok=True)

    rows = compute_data()

    # Print the distinctive initial values
    print(f"{'n':>4}  {'deg':>4}  {'tau(n)':>13}")
    print("-" * 27)
    for r in rows[:15]:
        print(f"{r['n']:>4}  {r['degree']:>4}  {r['tau']:>+13.6f}")
    print("  ...")
    for r in rows[-5:]:
        print(f"{r['n']:>4}  {r['degree']:>4}  {r['tau']:>+13.6f}")

    outpath = os.path.join(figdir, "tau_portrait.png")
    plot_portrait(rows, outpath)
    print(f"\nwrote {outpath}")


if __name__ == "__main__":
    main()
