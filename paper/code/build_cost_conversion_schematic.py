"""
Build the cost-conversion schematic for paper/IMPOSSIBILITY-OUTLINE.md §1.5.

A 2D schematic in the cost-pair (μ, α) plane orienting the reader to the
mult/add conversion economy before §3 lays out the canon and §6 closes the
impossibility:

  - Achievable region (above the continuous actual frontier).
  - Hypothetical δ = 0 frontier as a dashed lower curve, separating from the
    actual near the regime boundary.
  - Hatched δ-gap between actual and hypothetical: the irreducible transaction
    cost, visible *as a gap*, not as a step that reads as a discount.
  - Below-frontier region greyed with "FFT-style methods do not reach here"
    — the impossibility punchline made visual, not verbal.
  - Named canon thresholds on the frontier (Morgenstern, AFW, Winograd).
  - Conversion strategies as bidirectional arrows tangent to the frontier.
  - Regime separator as a dashed diagonal crossing the gap.
  - Bridge equivalence (§6.2) as a double-headed vertical arrow spanning the
    δ-gap, with ⟺ language: descent past T(P) ⟺ δ = 0 at the boundary.

This is the Bridge-side picture for §1.5 / §6.2. Lemma B (per-operation
drift) and Separation (δ = 0 outside C_FFT) are not visualized here — see
figures/delta_phase_plot.png at §6.5 for the closure-class story.
"""

import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


# Palette (consistent with build_delta_phase_plot.py)
INK = "#17202a"
ANNOT_GREY = "#555"
GRID = "0.92"
FRONTIER_COLOR = "#17202a"
ACHIEVABLE_FILL = "#e8e0d0"
ACHIEVABLE_EDGE = "#8c7a5a"
UNACHIEVABLE_FILL = "#ececec"
UNACHIEVABLE_EDGE = "#777"
DELTA_COLOR = "#b03a2e"        # witness red
DELTA_FILL = "#fcd8d4"
THRESHOLD_COLOR = "#255c7e"    # blue
REGIME_COLOR = "#2e7d55"       # green
STRATEGY_COLOR = "#7d6608"     # mustard

# Axes
MU_MIN, MU_MAX = 0.0, 10.0
ALPHA_MIN, ALPHA_MAX = 0.0, 10.0


def frontier_actual(x):
    """Continuous concave actual frontier."""
    return 8.5 - 0.5 * x - 0.05 * x ** 2


# Regime boundary and δ-gap shape
MU_BOUNDARY = 5.0
DELTA_HEIGHT = 1.4
DELTA_SIGMA = 1.4


def frontier_hypothetical(x):
    """Hypothetical δ = 0 frontier — coincides with actual far from the
    boundary, lower by a Gaussian bump of peak height δ at μ_b."""
    bump = DELTA_HEIGHT * np.exp(-((x - MU_BOUNDARY) / DELTA_SIGMA) ** 2)
    return frontier_actual(x) - bump


def build_figure():
    fig, ax = plt.subplots(figsize=(11.0, 7.2))

    x_full = np.linspace(MU_MIN, MU_MAX, 300)
    y_actual = frontier_actual(x_full)
    y_hypo = frontier_hypothetical(x_full)

    # ----- Achievable region (above actual frontier) -----
    ach_x = np.concatenate([x_full, [MU_MAX, MU_MIN]])
    ach_y = np.concatenate([y_actual, [ALPHA_MAX, ALPHA_MAX]])
    ax.fill(ach_x, ach_y, color=ACHIEVABLE_FILL, edgecolor="none",
            alpha=0.85, zorder=1)

    # ----- Below-frontier (everywhere below actual): greyed unachievable -----
    sub_x = np.concatenate([x_full, [MU_MAX, MU_MIN]])
    sub_y = np.concatenate([y_actual, [ALPHA_MIN, ALPHA_MIN]])
    ax.fill(sub_x, sub_y, color=UNACHIEVABLE_FILL, edgecolor="none",
            alpha=0.6, zorder=0)

    # ----- δ-gap (hatched) between actual and hypothetical -----
    ax.fill_between(x_full, y_hypo, y_actual,
                    color=DELTA_FILL, edgecolor=DELTA_COLOR,
                    hatch="///", linewidth=0.0, alpha=0.85, zorder=2)

    # ----- Frontiers -----
    ax.plot(x_full, y_actual, color=FRONTIER_COLOR, linewidth=2.6, zorder=5)
    ax.plot(x_full, y_hypo, color=DELTA_COLOR, linewidth=1.5,
            linestyle="--", zorder=4)

    # ----- Regime vocabulary ribbon (§1.4 anchor) -----
    ax.text(MU_BOUNDARY - 0.20, 9.55, "$\\leftarrow$  bounded coefficients",
            fontsize=9, color=ANNOT_GREY, ha="right", va="center",
            style="italic", zorder=3)
    ax.text(MU_BOUNDARY + 0.20, 9.55, "unbounded coefficients  $\\rightarrow$",
            fontsize=9, color=ANNOT_GREY, ha="left", va="center",
            style="italic", zorder=3)
    ax.text(MU_BOUNDARY, 9.55, "·",
            fontsize=14, color=ANNOT_GREY, ha="center", va="center",
            fontweight="bold", zorder=3)

    # ----- Named canon markers on the actual frontier -----
    # AFW moved off the boundary so the δ-arrow isn't conflated with any one
    # canon point (per agent feedback).
    canon_points = [
        (1.6, "Morgenstern", "left", 0.20, 0.30),
        (3.8, "AFW", "right", -0.20, 0.35),
        (8.0, "Winograd", "left", 0.20, 0.40),
    ]
    for cx, name, ha, off_x, off_y in canon_points:
        cy = frontier_actual(cx)
        ax.plot([cx], [cy], "o", color=THRESHOLD_COLOR, markersize=11,
                markeredgecolor=INK, markeredgewidth=1.0, zorder=8)
        ax.text(cx + off_x, cy + off_y, name,
                color=THRESHOLD_COLOR, fontsize=10, fontweight="bold",
                ha=ha, va="bottom", zorder=9)

    # T(P) collective label
    ax.text(7.4, frontier_actual(7.4) + 1.4,
            r"$T(P)$  thresholds (canon)",
            fontsize=10.5, color=THRESHOLD_COLOR, ha="center", va="bottom",
            fontweight="bold", style="italic", zorder=9)

    # ----- Conversion strategy arrows -----
    sx = 2.9
    sy = frontier_actual(sx)
    slope = -0.5 - 0.1 * sx
    fwd_dx = 1.05
    fwd_dy = fwd_dx * slope
    ax.annotate("", xy=(sx + fwd_dx, sy + fwd_dy), xytext=(sx, sy),
                arrowprops=dict(arrowstyle="-|>", color=STRATEGY_COLOR,
                                lw=1.6, mutation_scale=18), zorder=6)
    ax.annotate("", xy=(sx - fwd_dx, sy - fwd_dy), xytext=(sx, sy),
                arrowprops=dict(arrowstyle="-|>", color=STRATEGY_COLOR,
                                lw=1.6, mutation_scale=18), zorder=6)
    ax.text(sx, sy + 0.65,
            "conversion strategies\n" r"(trade $\alpha \leftrightarrow \mu$)",
            fontsize=10, color=STRATEGY_COLOR, fontweight="bold",
            ha="center", va="bottom", zorder=7)

    # ----- Bridge equivalence: double-headed vertical arrow at μ_b -----
    bridge_y_top = frontier_actual(MU_BOUNDARY)
    bridge_y_bot = frontier_hypothetical(MU_BOUNDARY)
    ax.annotate(
        "",
        xy=(MU_BOUNDARY, bridge_y_bot),
        xytext=(MU_BOUNDARY, bridge_y_top),
        arrowprops=dict(arrowstyle="<|-|>", color=DELTA_COLOR,
                        lw=2.2, mutation_scale=20),
        zorder=7,
    )
    ax.text(MU_BOUNDARY + 0.18, (bridge_y_top + bridge_y_bot) / 2,
            r"$\delta$",
            color=DELTA_COLOR, fontsize=22, fontweight="bold",
            ha="left", va="center", zorder=8)
    ax.annotate(
        "Bridge claim (§6.2):\n"
        r"descent past $T(P)$  $\Longleftrightarrow$  $\delta = 0$ at boundary",
        xy=(MU_BOUNDARY + 0.05, (bridge_y_top + bridge_y_bot) / 2),
        xytext=(7.1, 7.5),
        fontsize=9.5, color=DELTA_COLOR, ha="left", va="center",
        fontweight="bold", zorder=8,
        arrowprops=dict(arrowstyle="->", color=DELTA_COLOR, lw=0.9,
                        connectionstyle="arc3,rad=0.15"),
    )

    # ----- Region labels -----
    ax.text(2.5, 9.3, "ACHIEVABLE",
            fontsize=15, color=ACHIEVABLE_EDGE,
            ha="center", va="center", fontweight="bold",
            alpha=0.95, zorder=2)

    ax.text(7.3, 1.0,
            "FFT-style methods do not\nreach below the frontier",
            fontsize=10, color=UNACHIEVABLE_EDGE,
            ha="center", va="center", style="italic",
            alpha=0.95, zorder=2)

    # ----- Frontier label -----
    ax.annotate(
        "actual frontier",
        xy=(0.6, frontier_actual(0.6)),
        xytext=(0.05, frontier_actual(0.6) - 1.5),
        fontsize=10, color=INK, ha="left", va="top",
        fontweight="bold", zorder=7,
        arrowprops=dict(arrowstyle="->", color=INK, lw=0.7),
    )

    # ----- Counterfactual frontier label -----
    h_label_x = MU_BOUNDARY - 2.7
    h_label_y = frontier_hypothetical(h_label_x)
    ax.annotate(
        "counterfactual $\\delta = 0$ frontier\n(unreachable)",
        xy=(h_label_x, h_label_y),
        xytext=(0.1, 4.4),
        fontsize=9, color=DELTA_COLOR, ha="left", va="top",
        style="italic", fontweight="bold", zorder=7,
        arrowprops=dict(arrowstyle="->", color=DELTA_COLOR, lw=0.7),
    )

    # ----- Axes -----
    ax.set_xlim(MU_MIN, MU_MAX)
    ax.set_ylim(ALPHA_MIN, ALPHA_MAX)
    ax.set_xlabel(
        r"multiplicative cost $\mu$    ($\longrightarrow$ more multiplications)",
        fontsize=11,
    )
    ax.set_ylabel(
        r"additive cost $\alpha$    ($\uparrow$ more additions)",
        fontsize=11,
    )
    ax.grid(True, color=GRID, linewidth=0.5, zorder=0)
    ax.set_axisbelow(True)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.tick_params(length=0)

    # ----- Title and caption -----
    fig.suptitle(
        "The mult/add conversion economy",
        fontsize=14.5, fontweight="bold", y=0.97,
    )

    caption = (
        r"Schematic of the cost-pair ($\mu$, $\alpha$) plane for FFT-style methods. "
        r"Methods sit on the actual frontier (solid black); conversion strategies "
        r"move along it. The counterfactual $\delta = 0$ frontier (dashed red) "
        r"lies below it near the bounded/unbounded coefficient boundary (§1.4); "
        r"the hatched gap of height $\delta$ is the irreducible transaction cost. "
        r"Canon thresholds (Morgenstern, AFW, Winograd) sit on the actual frontier. "
        r"The Bridge claim (§6.2) is the equivalence between threshold improvement "
        r"and zeroing $\delta$ at the boundary. Bridge-side picture only; "
        r"Separation (§6.4) and Native drift (§6.5) live in "
        r"figures/delta_phase_plot.png."
    )
    fig.text(0.5, 0.015, caption, ha="center", fontsize=8.8, color="#444",
             style="italic", wrap=True)

    plt.tight_layout(rect=[0, 0.07, 1, 0.95])
    return fig


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(os.path.dirname(here))
    figures_dir = os.path.join(repo_root, "figures")
    os.makedirs(figures_dir, exist_ok=True)
    output_path = os.path.join(figures_dir, "cost_conversion_schematic.png")

    fig = build_figure()
    fig.savefig(output_path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)

    print(output_path)


if __name__ == "__main__":
    main()
