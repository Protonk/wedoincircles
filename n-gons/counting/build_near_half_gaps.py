"""
Nearest-approach plot for x = ±1/2.

For each n, compute the minimum distance from any corner x-coordinate of the
outside-out n-gon to +1/2 and to -1/2.
"""

import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpmath import mp


mp.dps = 80

N_MIN = 3
N_MAX = 400


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

    best_pos_idx = min(range(len(ns)), key=lambda i: pos[i])
    best_neg_idx = min(range(len(ns)), key=lambda i: neg[i])

    fig, ax = plt.subplots(figsize=(13, 6.5))

    ax.semilogy(ns, pos, color="#d98c2b", lw=1.4, alpha=0.9, label=r"gap to $+1/2$")
    ax.semilogy(ns, neg, color="#5b8dd1", lw=1.4, alpha=0.9, label=r"gap to $-1/2$")
    ax.scatter(ns, pos, color="#d98c2b", s=8, alpha=0.8)
    ax.scatter(ns, neg, color="#5b8dd1", s=8, alpha=0.8)

    ax.scatter([ns[best_pos_idx]], [pos[best_pos_idx]], color="#d98c2b", s=36,
               edgecolors="black", linewidths=0.4, zorder=5)
    ax.scatter([ns[best_neg_idx]], [neg[best_neg_idx]], color="#5b8dd1", s=36,
               edgecolors="black", linewidths=0.4, zorder=5)

    ax.set_xlim(N_MIN, N_MAX)
    ax.set_xlabel("n")
    ax.set_ylabel(r"minimum distance to $x = \pm 1/2$")
    ax.set_title(r"Nearest approach to the tested-empty guides $x = \pm 1/2$  (n = 3 … 400)", fontsize=13)
    ax.grid(True, which="both", color="0.93", lw=0.6)
    ax.legend(loc="upper right", fontsize=10, framealpha=0.95)

    ax.annotate(
        fr"best to $+1/2$:  n = {ns[best_pos_idx]},  gap $\approx {pos[best_pos_idx]:.3e}$",
        xy=(ns[best_pos_idx], pos[best_pos_idx]),
        xytext=(0.03, 0.16),
        textcoords="axes fraction",
        fontsize=9.5,
        color="#8a5a17",
    )
    ax.annotate(
        fr"best to $-1/2$:  n = {ns[best_neg_idx]},  gap $\approx {neg[best_neg_idx]:.3e}$",
        xy=(ns[best_neg_idx], neg[best_neg_idx]),
        xytext=(0.03, 0.10),
        textcoords="axes fraction",
        fontsize=9.5,
        color="#355b90",
    )

    note = r"No exact hits were found on either guide for $n \leq 400$."
    fig.text(0.5, 0.015, note, ha="center", va="bottom", fontsize=10, color="0.25")

    plt.tight_layout(rect=[0, 0.04, 1, 1])
    plt.savefig(outpath, dpi=170, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "..", "figures"))
    os.makedirs(figdir, exist_ok=True)
    out = os.path.join(figdir, "counting_near_half_gaps.png")
    plot(out)
    print(f"wrote {out}")
