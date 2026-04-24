"""
Build the strip-tissue Fourier figure.

The figure is the visual companion to memos/STRIP-TISSUE-FOURIER.md:

1. The strip tissue y_n(x) for n = 10, with one period highlighted and
   the DC coefficient d_0 = A_below(n) marked.
2. Signed coefficients n^2 d_k compared against (-1)^k/k^2.
3. Pairwise nonzero-mode energy shares, normalized by the exact nonzero
   L2 energy ||y_n||_2^2 - |d_0|^2, compared against the limiting
   1/(zeta(4) k^4) law.
"""

import math
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


N = 10
KMAX = 12

INK = "#17202a"
BLUE = "#255c7e"
ORANGE = "#d98c2b"
RED = "#b03a2e"
GREEN = "#2e7d55"
SHADE = "#f2e7d5"
GRID = "0.90"


def sec(x):
    return 1.0 / math.cos(x)


def a_below(n):
    theta = math.pi / n
    return (n / math.pi) * math.log(sec(theta) + math.tan(theta)) - 1.0


def l2_total(n):
    theta = math.pi / n
    return (n / math.pi) * (
        math.tan(theta) - 2.0 * math.log(sec(theta) + math.tan(theta)) + theta
    )


def nonzero_l2_energy(n):
    d0 = a_below(n)
    return l2_total(n) - d0 * d0


def d_k(n, k):
    if k == 0:
        return a_below(n)

    # The -1 term integrates to zero for k != 0, so the sec term alone is
    # numerically better conditioned and matches the memo's formula.
    upper = math.pi / n

    def integrand(t):
        return sec(t) * math.cos(k * n * t)

    val, _err = quad(integrand, 0.0, upper, epsabs=1e-13, epsrel=1e-13, limit=100)
    return (n / math.pi) * val


def signed_asymptotic(k):
    if k == 0:
        return None
    sign = -1.0 if k % 2 else 1.0
    return sign / float(k * k)


def strip_tissue(n, xs):
    period = 1.0 / n
    phase = np.mod(xs + 0.5 * period, period) - 0.5 * period
    return (1.0 / np.cos(2.0 * math.pi * phase)) - 1.0


def draw_strip_panel(ax, n):
    xs = np.linspace(0.0, 1.0, 4001)
    ys = strip_tissue(n, xs)
    d0 = a_below(n)
    peak = sec(math.pi / n) - 1.0

    x0 = 0.5 - 0.5 / n
    x1 = 0.5 + 0.5 / n
    mask = (xs >= x0) & (xs <= x1)

    ax.axvspan(x0, x1, color=SHADE, alpha=0.85, zorder=0)
    ax.plot(xs, ys, color="0.55", lw=1.0, alpha=0.65, zorder=2)
    ax.plot(xs[mask], ys[mask], color=BLUE, lw=2.7, zorder=4)
    ax.axhline(0.0, color=INK, lw=1.6, zorder=3)
    ax.axhline(d0, color=ORANGE, lw=2.0, ls="--", zorder=5)
    ax.axhline(peak, color="0.45", lw=1.0, ls=":", zorder=3)

    ax.text(
        x1 + 0.012,
        d0,
        r"$d_0=A_{\rm below}=%.5f$" % d0,
        color=ORANGE,
        fontsize=9.5,
        va="center",
        ha="left",
    )
    ax.text(
        x0 + 0.006,
        peak * 0.94,
        "one strip period",
        color=BLUE,
        fontsize=9,
        va="top",
        ha="left",
    )

    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(-0.003, peak * 1.20)
    ax.set_title(r"(a) strip tissue $y_{10}(x)$: area is the DC mode", fontsize=12)
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$y_n(x)$")
    ax.set_xticks([0.0, 0.25, 0.5, 0.75, 1.0])
    ax.set_xticklabels(["0", "1/4", "1/2", "3/4", "1"])
    ax.grid(True, color=GRID, lw=0.55)


def draw_coeff_panel(ax, n, kmax):
    ks = np.arange(-kmax, kmax + 1)
    actual = np.array([n * n * d_k(n, int(k)) for k in ks])
    nonzero_ks = np.array([k for k in ks if k != 0])
    asymptotic = np.array([signed_asymptotic(int(k)) for k in nonzero_ks])

    mask = ks != 0
    ax.axhline(0.0, color=INK, lw=1.0, zorder=1)
    ax.vlines(ks[mask], 0.0, actual[mask], color=BLUE, lw=2.0, alpha=0.90, zorder=2)
    ax.scatter(ks[mask], actual[mask], s=36, color=BLUE, edgecolor="white",
               linewidth=0.45, zorder=3, label=r"$10^2 d_k$")

    ax.vlines([0], 0.0, [actual[ks == 0][0]], color=ORANGE, lw=3.0, zorder=2)
    ax.scatter([0], [actual[ks == 0][0]], s=48, color=ORANGE, edgecolor="white",
               linewidth=0.45, zorder=4, label=r"$10^2 d_0$")

    ax.scatter(nonzero_ks, asymptotic, marker="x", s=54, linewidth=1.6,
               color=RED, zorder=5, label=r"$(-1)^k/k^2$")

    ax.set_xlim(-kmax - 0.75, kmax + 0.75)
    ax.set_ylim(-1.18, max(1.95, float(np.max(actual)) * 1.12))
    ax.set_title(r"(b) signed nonzero modes: $d_k \sim (-1)^k/(k^2 n^2)$",
                 fontsize=12)
    ax.set_xlabel(r"mode index $k$ on lattice $10\mathbb{Z}$")
    ax.set_ylabel(r"scaled coefficient $10^2 d_k$")
    ax.set_xticks(np.arange(-kmax, kmax + 1, 2))
    ax.grid(True, axis="y", color=GRID, lw=0.55)
    ax.legend(loc="upper right", fontsize=9, framealpha=0.95)


def draw_energy_panel(ax, n, kmax):
    pairs = np.arange(1, kmax + 1)
    denom = nonzero_l2_energy(n)
    shares = np.array([2.0 * d_k(n, int(k)) ** 2 / denom for k in pairs])
    zeta4 = math.pi ** 4 / 90.0
    limiting = np.array([1.0 / (zeta4 * k ** 4) for k in pairs])
    first_limit = 90.0 / math.pi ** 4

    ax.bar(pairs, shares, width=0.72, color=GREEN, edgecolor="white",
           linewidth=0.6, alpha=0.88, label="actual pair share")
    ax.plot(pairs, limiting, color=RED, lw=1.4, marker="x", ms=6,
            label=r"limit $1/(\zeta(4)k^4)$")

    ax.annotate(
        r"$90/\pi^4 = %.3f$" % first_limit,
        xy=(1, shares[0]),
        xytext=(2.2, 0.62),
        textcoords="data",
        arrowprops=dict(arrowstyle="->", color=INK, lw=0.8),
        fontsize=10,
        color=INK,
    )

    ax.set_yscale("log")
    ax.set_xlim(0.35, kmax + 0.65)
    ax.set_ylim(1e-5, 1.25)
    ax.set_title(r"(c) nonzero $L^2$ energy: first pair carries almost all mass",
                 fontsize=12)
    ax.set_xlabel(r"mode pair $\pm k$")
    ax.set_ylabel(r"$2|d_k|^2 / \sum_{j\ne0}|d_j|^2$")
    ax.set_xticks(pairs)
    ax.grid(True, which="major", axis="y", color=GRID, lw=0.55)
    ax.grid(True, which="minor", axis="y", color="0.95", lw=0.4)
    ax.legend(loc="upper right", fontsize=9, framealpha=0.95)


def plot(outpath):
    fig = plt.figure(figsize=(15.0, 8.8))
    gs = fig.add_gridspec(2, 2, height_ratios=[1.0, 1.08], hspace=0.36, wspace=0.22)
    ax_strip = fig.add_subplot(gs[0, :])
    ax_coeff = fig.add_subplot(gs[1, 0])
    ax_energy = fig.add_subplot(gs[1, 1])

    draw_strip_panel(ax_strip, N)
    draw_coeff_panel(ax_coeff, N, KMAX)
    draw_energy_panel(ax_energy, N, KMAX)

    fig.suptitle(
        "Strip-tissue Fourier object: DC area, signed modes, and first-pair concentration",
        fontsize=15,
        fontweight="bold",
        y=0.985,
    )
    fig.text(
        0.5,
        0.947,
        r"For $n=10$, the strip lattice is $10\mathbb{Z}$: "
        r"$d_0=A_{\rm below}$, while $d_k$ follows $(-1)^k/(k^2 n^2)$ off DC.",
        ha="center",
        va="center",
        fontsize=10.5,
        color="0.30",
    )
    fig.text(
        0.5,
        0.014,
        r"Panel (c) uses the exact denominator "
        r"$\|y_{10}\|_2^2-|d_0|^2$, not a truncated sum.",
        ha="center",
        fontsize=9.5,
        color="0.35",
        style="italic",
    )

    plt.savefig(outpath, dpi=170, bbox_inches="tight")
    plt.close(fig)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "figures"))
    os.makedirs(figdir, exist_ok=True)
    outpath = os.path.join(figdir, "strip_tissue_fourier.png")

    d0 = a_below(N)
    nonzero = nonzero_l2_energy(N)
    first_share = 2.0 * d_k(N, 1) ** 2 / nonzero
    print(f"n={N}")
    print(f"d_0 = A_below = {d0:.12f}")
    print(f"nonzero L2 energy = {nonzero:.12e}")
    print(f"first-pair share = {first_share:.12f}")
    print(f"first-pair limit = {90.0 / math.pi ** 4:.12f}")

    plot(outpath)
    print(f"wrote {outpath}")


if __name__ == "__main__":
    main()
