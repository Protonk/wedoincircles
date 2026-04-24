"""
Nearest-approach plot for x = ±1/2.

For each n, compute the minimum distance from any corner x-coordinate of the
outside-out n-gon to +1/2 and to -1/2.

The two series decay at different rates for an arithmetic reason:
- +1/2 aligns exactly with the internal cosine when 3(2k+1) = n and 2k+1 is odd,
  i.e., when n ≡ 3 (mod 6). On that subsequence the gap collapses to the sec
  correction (sec(π/n) − 1)/2 ≈ π²/(4n²).
- -1/2 would require 3(2k+1) = 2n with 2k+1 odd, which is parity-impossible.
  The best alignment misses by angular π/(3n), giving gap ≈ π√3/(6n) ~ 1/n.

These two envelopes are drawn as reference lines.

Exact non-attainment is expected to be algebraic rather than transcendence-
theoretic. The equation x_{n,k} = ±1/2 becomes
    2 cos((2k+1)π/n) ∓ cos(π/n) = 0,
equivalently a ℚ-linear relation with coefficient pattern (2, 2, ∓1, ∓1)
among four primitive 2n-th roots of unity. The natural proof route is
Conway–Jones-style classification of vanishing sums of roots of unity plus a
decomposition lemma for non-primitive relations. That proof is not written in
this repo yet, but the expected mechanism is cyclotomic algebra.
"""

import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from mpmath import mp


mp.dps = 80

N_MIN = 3
N_MAX = 400

COLOR_POS = "#d98c2b"          # orange — gap to +1/2 (generic)
COLOR_POS_SPECIAL = "#8a4e10"  # darker orange — n ≡ 3 (mod 6), exact-cos aligned
COLOR_NEG = "#5b8dd1"          # blue — gap to -1/2
COLOR_REF_N2 = "#4a4a4a"       # dotted — π²/(4n²) floor
COLOR_REF_N = "#8a8a8a"        # dashed — π√3/(6n) envelope


def polygon_corner_xs(n):
    radius = 1 / mp.cos(mp.pi / n)
    return [radius * mp.cos((2 * k + 1) * mp.pi / n) for k in range(n)]


def half_gap_data():
    ns = list(range(N_MIN, N_MAX + 1))
    pos = []
    neg = []
    for n in ns:
        xs = polygon_corner_xs(n)
        pos.append(float(min(abs(x - mp.mpf("0.5")) for x in xs)))
        neg.append(float(min(abs(x + mp.mpf("0.5")) for x in xs)))
    return ns, pos, neg


def plot(outpath):
    ns, pos, neg = half_gap_data()

    ns_arr = np.array(ns)
    pos_arr = np.array(pos)
    neg_arr = np.array(neg)

    special_mask = (ns_arr % 6 == 3)

    best_pos_idx = int(np.argmin(pos_arr))
    best_neg_idx = int(np.argmin(neg_arr))

    fig, ax = plt.subplots(figsize=(13, 7))

    # --- reference envelopes ---------------------------------------------
    n_grid = np.linspace(N_MIN, N_MAX, 600)
    ref_n2 = (np.pi ** 2) / (4.0 * n_grid ** 2)
    ref_n1 = (np.pi * np.sqrt(3)) / (6.0 * n_grid)
    ax.plot(n_grid, ref_n1, ls="--", color=COLOR_REF_N, lw=1.1, alpha=0.85,
            zorder=1, label=r"$\pi\sqrt{3}\,/\,(6n)$  — generic $1/n$ envelope")
    ax.plot(n_grid, ref_n2, ls=":", color=COLOR_REF_N2, lw=1.3, alpha=0.9,
            zorder=1, label=r"$\pi^{2}/(4n^{2})$  — exact-cos $1/n^{2}$ floor")

    # --- scatter: generic orange, special orange, blue -------------------
    ax.scatter(ns_arr[~special_mask], pos_arr[~special_mask],
               color=COLOR_POS, s=12, alpha=0.7, zorder=3,
               label=r"gap to $+1/2$")
    ax.scatter(ns_arr[special_mask], pos_arr[special_mask],
               color=COLOR_POS_SPECIAL, s=30, marker="D",
               edgecolors="black", linewidths=0.35, alpha=0.95, zorder=4,
               label=r"$n \equiv 3\ (\mathrm{mod}\ 6)$  — exact-cos aligned")
    ax.scatter(ns_arr, neg_arr,
               color=COLOR_NEG, s=12, alpha=0.75, zorder=3,
               label=r"gap to $-1/2$")

    # --- best-point stars ------------------------------------------------
    ax.scatter([ns[best_pos_idx]], [pos[best_pos_idx]],
               marker="*", s=260, color="#ffd700",
               edgecolors="black", linewidths=0.8, zorder=6)
    ax.scatter([ns[best_neg_idx]], [neg[best_neg_idx]],
               marker="*", s=260, color="#ffd700",
               edgecolors="black", linewidths=0.8, zorder=6)

    ax.annotate(
        fr"best to $+1/2$: $n = {ns[best_pos_idx]}$,  gap $\approx {pos[best_pos_idx]:.2e}$",
        xy=(ns[best_pos_idx], pos[best_pos_idx]),
        xytext=(0.46, 0.12), textcoords="axes fraction",
        fontsize=10, color="#5a3a0a",
        arrowprops=dict(arrowstyle="->", color="#5a3a0a", lw=0.8, alpha=0.75),
    )
    ax.annotate(
        fr"best to $-1/2$: $n = {ns[best_neg_idx]}$,  gap $\approx {neg[best_neg_idx]:.2e}$",
        xy=(ns[best_neg_idx], neg[best_neg_idx]),
        xytext=(0.46, 0.36), textcoords="axes fraction",
        fontsize=10, color="#1f3d6b",
        arrowprops=dict(arrowstyle="->", color="#1f3d6b", lw=0.8, alpha=0.75),
    )

    # --- axes ------------------------------------------------------------
    ax.set_yscale("log")
    ax.set_xlim(N_MIN - 2, N_MAX + 5)
    ax.set_ylim(5e-6, 2.5)
    ax.set_xlabel(r"polygon order  $n$", fontsize=12)
    ax.set_ylabel(r"minimum gap to $x = \pm 1/2$", fontsize=12)
    ax.grid(True, which="major", color="0.93", lw=0.6)
    ax.grid(True, which="minor", color="0.97", lw=0.4)

    # --- legend ----------------------------------------------------------
    # Custom ordering: data series first, then arithmetic subsequence, then refs.
    handles, labels = ax.get_legend_handles_labels()
    # Reorder: we want [gap +1/2, ≡3 mod 6, gap -1/2, 1/n ref, 1/n² ref]
    wanted = [
        r"gap to $+1/2$",
        r"$n \equiv 3\ (\mathrm{mod}\ 6)$  — exact-cos aligned",
        r"gap to $-1/2$",
        r"$\pi\sqrt{3}\,/\,(6n)$  — generic $1/n$ envelope",
        r"$\pi^{2}/(4n^{2})$  — exact-cos $1/n^{2}$ floor",
    ]
    ordered = [handles[labels.index(w)] for w in wanted if w in labels]
    ordered_labels = [w for w in wanted if w in labels]
    ax.legend(ordered, ordered_labels,
              loc="upper right", framealpha=0.94,
              edgecolor="0.8", fontsize=9.5, ncol=1,
              title=r"series & asymptotics", title_fontsize=10)

    # --- titles ----------------------------------------------------------
    fig.suptitle(
        r"Nearest approach of outside-out vertices to  $x = \pm 1/2$",
        fontsize=14.5, fontweight="bold", y=0.995,
    )
    fig.text(
        0.5, 0.955,
        r"$n \in [3, 400]$    |    "
        r"orange $+1/2$ series: $1/n^2$ subsequence at $n \equiv 3\ (\mathrm{mod}\ 6)$;    "
        r"blue $-1/2$ series: no exact-cos alignment (parity-forbidden)",
        ha="center", fontsize=10, color="0.3", style="italic",
    )
    fig.text(
        0.5, 0.020,
        r"no exact hit was found for any $n \leq 400$;   "
        r"expected global non-attainment proof: cyclotomic vanishing-sum classification, not transcendence",
        ha="center", fontsize=9.5, color="0.35", style="italic",
    )

    plt.tight_layout(rect=[0.0, 0.035, 1.0, 0.93])
    plt.savefig(outpath, dpi=170, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "..", "figures"))
    os.makedirs(figdir, exist_ok=True)
    out = os.path.join(figdir, "counting_near_half_gaps.png")
    plot(out)
    print(f"wrote {out}")
