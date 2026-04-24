import math
import os
from fractions import Fraction

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


N_MAX = 18
WITNESS = Fraction(2, 5)
WITNESS_MULTIPLES = [5, 10, 15]
COMPARISON = Fraction(1, 3)
COMPARISON_MULTIPLES = [3, 6, 9, 12, 15, 18]
X_MIN = WITNESS - Fraction(1, 2 * WITNESS.denominator)
X_MAX = WITNESS + Fraction(1, 2 * WITNESS.denominator)
X_PAD = 0.004

INK = "#242424"
MUTED = "#7d8791"
GRID = "#e8e2d7"
ARC_BG = "#bcc4cb"
ARC_MAIN = "#a05ab5"
ARC_DARK = "#5f2d7e"
GUNMETAL = "#35424f"
GUNMETAL_LIGHT = "#6f7c88"
STEM = "#9aa3ad"
STEM_DARK = "#47525f"
ACCENT = "#d1495b"


def linspace(start, stop, count):
    if count <= 1:
        return [start]
    step = (stop - start) / (count - 1)
    return [start + i * step for i in range(count)]


def reduced_rationals(max_denominator):
    rationals = []
    for q in range(2, max_denominator + 1):
        for p in range(1, q):
            frac = Fraction(p, q)
            if frac.denominator == q:
                rationals.append(frac)
    return sorted(set(rationals))


def strip_arc(n, k, samples=120):
    center = k / n
    half_width = 1 / (2 * n)
    xs = linspace(center - half_width, center + half_width, samples)
    ys = []
    for x in xs:
        dt = 2 * math.pi * (x - center)
        ys.append(1 / math.cos(dt) - 1)
    return xs, ys


def plot_strip_arcs(ax):
    witness_x = float(WITNESS)
    comparison_x = float(COMPARISON)

    for n in range(3, N_MAX + 1):
        for k in range(1, n):
            xs, ys = strip_arc(n, k, samples=80)
            is_witness_arc = n in WITNESS_MULTIPLES and k == WITNESS.numerator * (n // WITNESS.denominator)
            is_comparison_arc = n in COMPARISON_MULTIPLES and k == COMPARISON.numerator * (n // COMPARISON.denominator)
            if is_witness_arc or is_comparison_arc:
                continue
            ax.plot(xs, ys, color=ARC_BG, lw=0.45, alpha=0.19, zorder=1)

    for n in COMPARISON_MULTIPLES:
        k = COMPARISON.numerator * (n // COMPARISON.denominator)
        xs, ys = strip_arc(n, k, samples=180)
        lw = 1.75 if n == COMPARISON.denominator else 1.05
        alpha = 0.82 if n == COMPARISON.denominator else 0.52
        ax.plot(xs, ys, color=GUNMETAL_LIGHT, lw=lw, alpha=alpha, zorder=3)
        ax.plot([comparison_x], [0], "o", color=GUNMETAL, ms=5.2,
                markeredgecolor="white", markeredgewidth=0.7, zorder=6)

    for n in WITNESS_MULTIPLES:
        k = WITNESS.numerator * (n // WITNESS.denominator)
        xs, ys = strip_arc(n, k, samples=180)
        lw = 2.0 if n == WITNESS.denominator else 1.55
        alpha = 0.96 if n == WITNESS.denominator else 0.8
        ax.plot(xs, ys, color=ARC_MAIN, lw=lw, alpha=alpha, zorder=4)
        ax.plot([witness_x], [0], "o", color=ARC_DARK, ms=5.5,
                markeredgecolor="white", markeredgewidth=0.7, zorder=6)

        y_peak = 1 / math.cos(math.pi / n) - 1
        ax.text(
            witness_x + 0.012,
            min(y_peak + 0.006, 0.255),
            f"n={n}",
            fontsize=8.4,
            color=ARC_DARK,
            ha="left",
            va="bottom",
            zorder=7,
        )

    ax.axhline(0, color=INK, lw=1.6, zorder=5)
    ax.axvline(comparison_x, color=GUNMETAL, lw=1.0, ls="--", alpha=0.65, zorder=3)
    ax.text(
        comparison_x,
        0.272,
        r"$x=1/3$",
        ha="center",
        va="bottom",
        color=GUNMETAL,
        fontsize=10.2,
        zorder=8,
    )
    ax.axvline(witness_x, color=ACCENT, lw=1.1, ls="--", alpha=0.75, zorder=3)
    ax.text(
        witness_x,
        0.272,
        r"$x=2/5$",
        ha="center",
        va="bottom",
        color=ACCENT,
        fontsize=10.5,
        zorder=8,
    )

    ax.set_ylim(-0.012, 0.30)
    ax.set_ylabel("strip height", color=INK)
    ax.set_title("(a) zoomed strip arcs: all contact happens at floor points x = k/n", loc="left", fontsize=12.5)


def plot_multiplicity(ax, rationals):
    xs = [float(frac) for frac in rationals]
    hs = [N_MAX // frac.denominator for frac in rationals]

    ax.vlines(xs, [0] * len(xs), hs, color=STEM, lw=0.75, alpha=0.72, zorder=2)
    ax.scatter(xs, hs, s=10, color=STEM_DARK, alpha=0.72, zorder=3)

    wx = float(WITNESS)
    wh = N_MAX // WITNESS.denominator
    cx = float(COMPARISON)
    ch = N_MAX // COMPARISON.denominator

    ax.vlines([cx], [0], [ch], color=GUNMETAL, lw=2.25, zorder=5)
    ax.scatter([cx], [ch], s=50, color=GUNMETAL,
               edgecolor="white", linewidth=0.8, zorder=6)
    ax.text(
        cx + 0.006,
        ch + 0.24,
        r"$\lfloor 18/3 \rfloor=6$ hits",
        color=GUNMETAL,
        fontsize=10,
        ha="left",
        va="bottom",
    )

    ax.vlines([wx], [0], [wh], color=ARC_DARK, lw=2.4, zorder=5)
    ax.scatter([wx], [wh], s=54, color=ARC_DARK,
               edgecolor="white", linewidth=0.8, zorder=6)
    ax.text(
        wx + 0.018,
        wh + 0.22,
        r"$\lfloor 18/5 \rfloor=3$ hits",
        color=ARC_DARK,
        fontsize=10,
        ha="left",
        va="bottom",
    )

    ax.set_ylim(0, max(hs) + 1.1)
    ax.set_ylabel("floor hits\nthrough N=18", color=INK)
    ax.set_title("(b) collapse the same window to floor-hit multiplicities", loc="left", fontsize=12.5)


def plot_normalized(ax, rationals):
    xs = [float(frac) for frac in rationals]
    hs = [1 / frac.denominator for frac in rationals]

    ax.vlines(xs, [0] * len(xs), hs, color=STEM, lw=0.75, alpha=0.7, zorder=2)
    ax.scatter(xs, hs, s=10, color=STEM_DARK, alpha=0.7, zorder=3)

    wx = float(WITNESS)
    wh = 1 / WITNESS.denominator
    cx = float(COMPARISON)
    ch = 1 / COMPARISON.denominator

    ax.vlines([cx], [0], [ch], color=GUNMETAL, lw=2.25, zorder=5)
    ax.scatter([cx], [ch], s=50, color=GUNMETAL,
               edgecolor="white", linewidth=0.8, zorder=6)
    ax.text(
        cx + 0.006,
        ch + 0.018,
        r"height $1/3$",
        color=GUNMETAL,
        fontsize=10,
        ha="left",
        va="bottom",
    )

    ax.vlines([wx], [0], [wh], color=ARC_DARK, lw=2.4, zorder=5)
    ax.scatter([wx], [wh], s=54, color=ARC_DARK,
               edgecolor="white", linewidth=0.8, zorder=6)
    ax.text(
        wx + 0.018,
        wh + 0.018,
        r"height $1/5$",
        color=ARC_DARK,
        fontsize=10,
        ha="left",
        va="bottom",
    )

    ax.set_ylim(0, 0.56)
    ax.set_ylabel("normalized\nheight 1/q", color=INK)
    ax.set_title("(c) normalize the same support by denominator", loc="left", fontsize=12.5)


def style_axis(ax, show_xlabel=False):
    ax.set_xlim(float(X_MIN) - X_PAD, float(X_MAX) + X_PAD)
    ax.grid(True, axis="y", color=GRID, lw=0.8, alpha=0.75)
    ax.grid(True, axis="x", color=GRID, lw=0.55, alpha=0.42)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#555555")
    ax.spines["bottom"].set_color("#555555")
    ax.tick_params(colors=INK, labelsize=9)
    ax.set_xticks([float(X_MIN), 1 / 3, float(WITNESS), float(X_MAX)])
    ax.set_xticklabels(["3/10", "1/3", "2/5", "1/2"])
    if show_xlabel:
        ax.set_xlabel("angle fraction x on the strip floor (zoomed window)", color=INK, labelpad=8)
    else:
        ax.tick_params(labelbottom=False)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "figures"))
    os.makedirs(figdir, exist_ok=True)

    rationals = reduced_rationals(N_MAX)

    fig = plt.figure(figsize=(12.5, 9.0))
    gs = GridSpec(
        3,
        1,
        figure=fig,
        height_ratios=[1.45, 1.05, 1.0],
        hspace=0.31,
        top=0.86,
        bottom=0.105,
        left=0.09,
        right=0.95,
    )

    ax_strip = fig.add_subplot(gs[0, 0])
    ax_count = fig.add_subplot(gs[1, 0], sharex=ax_strip)
    ax_norm = fig.add_subplot(gs[2, 0], sharex=ax_strip)

    plot_strip_arcs(ax_strip)
    plot_multiplicity(ax_count, rationals)
    plot_normalized(ax_norm, rationals)

    style_axis(ax_strip)
    style_axis(ax_count)
    style_axis(ax_norm, show_xlabel=True)

    fig.suptitle(
        "Local strip-floor denominator trace near x = 2/5",
        fontsize=17,
        color=INK,
        y=0.955,
    )
    fig.text(
        0.5,
        0.905,
        r"If $k/n=p/q$ in lowest terms, then $q \mid n$; through $N$, the floor multiplicity is $\lfloor N/q \rfloor$.",
        ha="center",
        va="center",
        fontsize=11.5,
        color="#404040",
    )
    fig.text(
        0.5,
        0.035,
        "Zoom window is one n = 5 strip period, [3/10, 1/2]. Compare q = 3 at x = 1/3 with q = 5 at x = 2/5.",
        ha="center",
        va="center",
        fontsize=9.5,
        color=MUTED,
    )

    outpath = os.path.join(figdir, "strip_floor_denominator_trace.png")
    plt.savefig(outpath, dpi=170, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {outpath}")


if __name__ == "__main__":
    main()
