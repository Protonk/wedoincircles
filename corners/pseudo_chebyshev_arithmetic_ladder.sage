"""
Arithmetic ladder for the pseudo-Chebyshev node sequence.

For node(n) = cos(pi/n), the algebraic degree over Q is phi(2n)/2.
The same node is straightedge-and-compass constructible exactly when the
regular 2n-gon is Gauss-Wantzel constructible. This script plots both
readouts on one n-axis.
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from sage.all import euler_phi, factor, RDF


N_MIN = 2
N_MAX = 40
FERMAT_PRIMES = {3, 5, 17, 257, 65537}


def degree(n):
    """Degree of cos(pi/n) over Q for n >= 2."""
    return int(euler_phi(2 * n) // 2)


def is_gauss_wantzel_order(m):
    """True iff a regular m-gon is constructible."""
    odd_part = int(m)
    while odd_part % 2 == 0:
        odd_part //= 2
    for p, exp in factor(odd_part):
        if int(p) not in FERMAT_PRIMES or int(exp) != 1:
            return False
    return True


def is_constructible_node(n):
    """node(n) is constructible iff the regular 2n-gon is constructible."""
    return is_gauss_wantzel_order(2 * n)


def plot(outpath):
    ns = list(range(N_MIN, N_MAX + 1))
    degs = [degree(n) for n in ns]
    constructible = [is_constructible_node(n) for n in ns]

    fig, ax = plt.subplots(figsize=(15, 7.2))

    for n, d, ok in zip(ns, degs, constructible):
        stem_color = "#386f80" if ok else "#b84b5c"
        ax.vlines(n, 0, d, color=stem_color, lw=1.8, alpha=0.48, zorder=2)
        if ok:
            ax.plot(
                [n], [d],
                marker="o", ms=8.5,
                markerfacecolor="#2d8392",
                markeredgecolor="black",
                markeredgewidth=0.65,
                zorder=4,
            )
        else:
            ax.plot(
                [n], [d],
                marker="o", ms=8.5,
                markerfacecolor="white",
                markeredgecolor="#b4263b",
                markeredgewidth=1.8,
                zorder=5,
            )

    # Degree tiers that occur early enough to be readable.
    for y, label in [
        (1, "rational"),
        (2, "quadratic"),
        (3, "cubic"),
        (4, "quartic"),
        (5, "quintic"),
        (6, "sextic"),
        (8, "degree 8"),
        (10, "degree 10"),
        (12, "degree 12"),
    ]:
        ax.axhline(y, color="0.88", lw=0.8, zorder=1)
        ax.text(
            N_MAX + 0.65, y, label,
            fontsize=8.5, color="0.36", va="center",
        )

    # The first arithmetic break.
    n0 = 7
    d0 = degree(n0)
    ax.axvspan(6.55, 7.45, color="#f3c3ca", alpha=0.23, zorder=0)
    ax.annotate(
        "n = 7: first cubic\nand first nonconstructible node",
        xy=(n0, d0),
        xytext=(10.0, 7.5),
        fontsize=10,
        color="#742336",
        arrowprops=dict(arrowstyle="->", color="#742336", lw=1.0),
        bbox=dict(boxstyle="round,pad=0.35", fc="white", ec="#e0a2ad", lw=0.8),
        zorder=8,
    )

    # Labels for the first few exact classes and selected later returns.
    for n in [2, 3, 4, 5, 6, 8, 10, 12, 15, 16, 17, 20, 24, 30]:
        d = degree(n)
        ax.annotate(
            str(n),
            xy=(n, d),
            xytext=(0, 8),
            textcoords="offset points",
            ha="center",
            fontsize=7.5,
            color="#244c55" if is_constructible_node(n) else "#9b2638",
            zorder=7,
        )

    ax.plot(
        [], [], marker="o", ms=8.5, linestyle="None",
        markerfacecolor="#2d8392", markeredgecolor="black",
        label="constructible node",
    )
    ax.plot(
        [], [], marker="o", ms=8.5, linestyle="None",
        markerfacecolor="white", markeredgecolor="#b4263b", markeredgewidth=1.8,
        label="nonconstructible node",
    )

    ax.set_title(
        "Arithmetic ladder for pseudo-Chebyshev nodes",
        fontsize=15,
    )
    ax.set_xlabel("n")
    ax.set_ylabel(r"degree of $\cos(\pi/n)$ over $\mathbb{Q}$:  $\varphi(2n)/2$")
    ax.set_xlim(N_MIN - 0.8, N_MAX + 4.1)
    ax.set_ylim(0, max(degs) + 2.0)
    ax.set_xticks(range(2, N_MAX + 1, 2))
    ax.set_yticks(sorted(set(degs)))
    ax.grid(axis="x", color="0.93", lw=0.5)
    ax.legend(loc="upper left", framealpha=0.95)

    ax.text(
        0.99, 0.03,
        "Filled markers are exactly the n for which the regular 2n-gon is Gauss-Wantzel constructible.",
        transform=ax.transAxes,
        ha="right",
        va="bottom",
        fontsize=9,
        color="0.28",
    )

    plt.tight_layout()
    plt.savefig(outpath, dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "figures"))
    os.makedirs(figdir, exist_ok=True)
    out = os.path.join(figdir, "pseudo_chebyshev_arithmetic_ladder.png")
    plot(out)
    print(f"wrote {out}")
