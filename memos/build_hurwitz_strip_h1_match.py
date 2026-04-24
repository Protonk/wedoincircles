"""
Build the Hurwitz / strip-H1 comparison figure.

The figure visualizes the statement from memos/STRIP-TISSUE-FOURIER.md:

    Delta_n = 4 pi^4/(3 n^2) - 16 pi^6/(45 n^4) + O(n^-6),
    ||y_n'||_2^2 = 4 pi^4/(3 n^2) + 4 pi^6/(3 n^4) + O(n^-6).

So the Hurwitz gap and strip H1 seminorm have the same second-order
Archimedean constant, but they are not the same observable. Their
difference has leading term 76 pi^6/(45 n^4).
"""

import math
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


N_MIN = 3
N_MAX = 100

INK = "#17202a"
HURWITZ_BLUE = "#255c7e"
STRIP_GREEN = "#2e7d55"
GUIDE_GRAY = "0.35"
DIFF_RED = "#b03a2e"
GRID = "0.90"


def perimeter(n):
    return 2.0 * n * math.sin(math.pi / n)


def area(n):
    return 0.5 * n * math.sin(2.0 * math.pi / n)


def hurwitz_delta(n):
    l_n = perimeter(n)
    return l_n * l_n - 4.0 * math.pi * area(n)


def strip_h1(n):
    return (4.0 * math.pi * n / 3.0) * math.tan(math.pi / n) ** 3


def leading(n):
    return 4.0 * math.pi ** 4 / (3.0 * n * n)


def scaled_difference_limit():
    return 76.0 * math.pi ** 6 / 45.0


def compute_rows():
    ns = np.arange(N_MIN, N_MAX + 1, dtype=float)
    delta = np.array([hurwitz_delta(int(n)) for n in ns])
    h1 = np.array([strip_h1(int(n)) for n in ns])
    lead = np.array([leading(float(n)) for n in ns])
    scaled_diff = ns ** 4 * (h1 - delta)
    return ns, delta, h1, lead, scaled_diff


def draw_rate_panel(ax, ns, delta, h1, lead):
    ax.loglog(ns, lead, color=GUIDE_GRAY, lw=2.0, ls="--",
              label=r"shared guide $4\pi^4/(3n^2)$")
    ax.loglog(ns, delta, marker="o", ms=5.0, lw=1.2,
              color=HURWITZ_BLUE, markeredgecolor="white",
              markeredgewidth=0.45, label=r"Hurwitz gap $\Delta_n$")
    ax.loglog(ns, h1, marker="s", ms=4.7, lw=1.2,
              color=STRIP_GREEN, markeredgecolor="white",
              markeredgewidth=0.45, label=r"strip seminorm $\|y_n'\|_2^2$")

    ax.set_title("(a) same leading rate, different substrates", fontsize=12,
                 loc="left")
    ax.set_ylabel("observable value")
    ax.grid(True, which="major", color=GRID, lw=0.55)
    ax.grid(True, which="minor", color="0.95", lw=0.35)
    ax.legend(loc="lower left", fontsize=9.5, framealpha=0.95)


def draw_ratio_panel(ax, ns, delta, h1, lead):
    ax.axhline(1.0, color=GUIDE_GRAY, lw=1.3, ls="--", zorder=1)
    ax.plot(ns, delta / lead, color=HURWITZ_BLUE, lw=1.9,
            marker="o", ms=3.8, markeredgecolor="white",
            markeredgewidth=0.35, label=r"$\Delta_n$ / leading")
    ax.plot(ns, h1 / lead, color=STRIP_GREEN, lw=1.9,
            marker="s", ms=3.5, markeredgecolor="white",
            markeredgewidth=0.35, label=r"$\|y_n'\|_2^2$ / leading")

    ax.annotate(
        "Hurwitz approaches from below",
        xy=(34, (delta / lead)[31]),
        xytext=(17, 0.87),
        arrowprops=dict(arrowstyle="->", color=HURWITZ_BLUE, lw=0.8),
        fontsize=9.2,
        color=HURWITZ_BLUE,
    )
    ax.annotate(
        "strip H1 approaches from above",
        xy=(30, (h1 / lead)[27]),
        xytext=(42, 1.17),
        arrowprops=dict(arrowstyle="->", color=STRIP_GREEN, lw=0.8),
        fontsize=9.2,
        color=STRIP_GREEN,
    )

    ax.set_title("(b) second-order match", fontsize=12, loc="left")
    ax.set_xlabel("polygon order n")
    ax.set_ylabel("ratio to shared leading term")
    ax.set_xlim(N_MIN, N_MAX)
    ax.set_ylim(0.70, 1.36)
    ax.grid(True, color=GRID, lw=0.55)
    ax.legend(loc="upper right", fontsize=9, framealpha=0.95)


def draw_difference_panel(ax, ns, scaled_diff):
    target = scaled_difference_limit()
    ax.axhline(target, color=GUIDE_GRAY, lw=1.8, ls="--",
               label=r"$76\pi^6/45$")
    ax.plot(ns, scaled_diff, color=DIFF_RED, lw=2.0,
            marker="o", ms=4.0, markeredgecolor="white",
            markeredgewidth=0.35,
            label=r"$n^4(\|y_n'\|_2^2-\Delta_n)$")

    ax.annotate(
        r"limit $76\pi^6/45 = %.2f$" % target,
        xy=(72, target),
        xytext=(39, target + 250),
        arrowprops=dict(arrowstyle="->", color=DIFF_RED, lw=0.85),
        fontsize=9.4,
        color=DIFF_RED,
    )

    ax.set_title("(c) not an identity: next term separates them",
                 fontsize=12, loc="left")
    ax.set_xlabel("polygon order n")
    ax.set_ylabel(r"$n^4(\|y_n'\|_2^2-\Delta_n)$")
    ax.set_xlim(N_MIN, N_MAX)
    ax.set_ylim(1450, 4600)
    ax.grid(True, color=GRID, lw=0.55)
    ax.legend(loc="upper right", fontsize=9, framealpha=0.95)


def plot(outpath):
    ns, delta, h1, lead, scaled_diff = compute_rows()

    fig = plt.figure(figsize=(14.5, 10.2))
    gs = fig.add_gridspec(2, 2, height_ratios=[1.25, 1.0], hspace=0.28,
                          wspace=0.20)
    ax_rate = fig.add_subplot(gs[0, :])
    ax_ratio = fig.add_subplot(gs[1, 0])
    ax_diff = fig.add_subplot(gs[1, 1])

    draw_rate_panel(ax_rate, ns, delta, h1, lead)
    draw_ratio_panel(ax_ratio, ns, delta, h1, lead)
    draw_difference_panel(ax_diff, ns, scaled_diff)

    fig.suptitle(
        "Hurwitz gap and strip H1 seminorm: same Archimedean jet, different observables",
        fontsize=15,
        fontweight="bold",
        y=0.982,
    )
    fig.text(
        0.5,
        0.942,
        r"Arc-length lattice $1+n\mathbb{Z}$ and strip lattice $n\mathbb{Z}$ "
        r"both produce $4\pi^4/(3n^2)$, but separate at order $n^{-4}$.",
        ha="center",
        va="center",
        fontsize=10.5,
        color="0.30",
    )
    fig.text(
        0.5,
        0.018,
        r"Definitions: $\Delta_n=L_n^2-4\pi A_n$ with "
        r"$L_n=2n\sin(\pi/n)$, $A_n=(n/2)\sin(2\pi/n)$; "
        r"$\|y_n'\|_2^2=(4\pi n/3)\tan^3(\pi/n)$.",
        ha="center",
        fontsize=9.2,
        color="0.35",
        style="italic",
    )

    plt.savefig(outpath, dpi=170, bbox_inches="tight")
    plt.close(fig)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "figures"))
    os.makedirs(figdir, exist_ok=True)
    outpath = os.path.join(figdir, "hurwitz_strip_h1_match.png")

    for n in (3, 10, 30, 100):
        d = hurwitz_delta(n)
        h = strip_h1(n)
        l = leading(n)
        print(
            f"n={n:3d}: Delta/lead={d/l:.12f}  "
            f"H1/lead={h/l:.12f}  n^4 diff={n**4 * (h-d):.12f}"
        )
    print(f"scaled-difference limit = {scaled_difference_limit():.12f}")

    plot(outpath)
    print(f"wrote {outpath}")


if __name__ == "__main__":
    main()
