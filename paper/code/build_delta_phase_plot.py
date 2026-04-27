"""
Build the delta-algebra phase plot for paper/IMPOSSIBILITY-OUTLINE.md §6.

A 2D phase diagram in delta-algebra space. Two axes:
    x: amortization rate alpha       (delta_k ~ k^(-alpha) under composition)
    y: asymptotic floor delta_infty  (lim inf delta — Coase's irreducible part)

The figure visualizes the *algebra-vs-existence* distinction Coase 1937 names
methodologically and FIRST-PROOF debt #2 carries forward:

  - The FFT canon lives at (alpha large, floor = 0) — the corner reachable
    only by zeroing the floor. Free descent.
  - The Coase axiom (specialists reduce but do not eliminate, p. 390) is the
    horizontal line floor = delta_min > 0. The program operates above it.
  - Above the line: impossibility — but the *mechanism* differs by region:
      * left of alpha_crit: slow amortization dominates; impossibility at
        small k.
      * right of alpha_crit: fast amortization, but positive floor still
        forces total to grow; impossibility at large k.
  - Debt #2 = where exactly the mechanism boundary sits inside the program's
    domain, drawn here as a band of uncertainty. Lemma B is the existence
    claim that the program's domain stays bounded *away* from the FFT corner.

Honesty notes:
  - The Coase line height (delta_min) is itself a working hypothesis, not a
    proven number. Drawn solid for the program's current stance, with a
    note that its stability under composition / specialization / amortization
    is what FIRST-PROOF debt #2 is asking.
  - The (alpha, floor) parametrization is a 2D *projection* of a higher-
    dimensional algebra space (additivity, bypass, representation). Caption
    flags this.
"""

import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch, Rectangle


# Palette
COASE_COLOR = "#255c7e"      # blue — Coase axiom line
FREE_COLOR = "#2e7d55"       # green — free descent / FFT canon
IMP_COLOR = "#b03a2e"        # witness red — impossibility
DEBT_COLOR = "#b8860b"       # mustard — debt #2 / open
INK = "#17202a"
ANNOT_GREY = "#555"
GRID = "0.92"

# Region fills (lighter palette echoes)
IMP_FILL = "#f5d8d4"
FREE_FILL = "#dcecdf"
DEBT_FILL = "#f4ebcb"
COASE_FILL = "#dde8f0"

# Axes
ALPHA_MIN, ALPHA_MAX = 0.0, 3.2
FLOOR_MIN, FLOOR_MAX = 0.0, 1.0

# Coase axiom: floor must stay above delta_min
DELTA_MIN = 0.10

# Critical alpha (heuristic — debt #2 owns its precise location)
ALPHA_CRIT = 1.4
ALPHA_BAND = 0.45  # half-width of the debt-#2 band


def build_figure():
    fig, ax = plt.subplots(figsize=(11.5, 7.2))

    # ----- 1. Backdrop: shade everything as impossibility (red light) -----
    ax.add_patch(Rectangle(
        (ALPHA_MIN, FLOOR_MIN), ALPHA_MAX - ALPHA_MIN, FLOOR_MAX - FLOOR_MIN,
        facecolor=IMP_FILL, edgecolor="none", zorder=0,
    ))

    # ----- 2. Coase exclusion zone (floor < delta_min): hatched blue -----
    ax.add_patch(Rectangle(
        (ALPHA_MIN, FLOOR_MIN), ALPHA_MAX - ALPHA_MIN, DELTA_MIN,
        facecolor=COASE_FILL, edgecolor=COASE_COLOR,
        hatch="///", linewidth=0.0, zorder=1,
    ))

    # ----- 3. Free-descent strip on floor = 0 (FFT canon, alpha > alpha_crit)
    free_height = 0.018
    ax.add_patch(Rectangle(
        (ALPHA_CRIT + ALPHA_BAND, FLOOR_MIN),
        ALPHA_MAX - (ALPHA_CRIT + ALPHA_BAND), free_height,
        facecolor=FREE_FILL, edgecolor=FREE_COLOR, linewidth=1.2, zorder=2,
    ))

    # ----- 4. Debt-#2 band: where the mechanism boundary sits -----
    # Vertical band at alpha = alpha_crit ± ALPHA_BAND, only above the Coase line
    ax.add_patch(Rectangle(
        (ALPHA_CRIT - ALPHA_BAND, DELTA_MIN),
        2 * ALPHA_BAND, FLOOR_MAX - DELTA_MIN,
        facecolor=DEBT_FILL, edgecolor=DEBT_COLOR,
        hatch="...", linewidth=0.0, alpha=0.7, zorder=2,
    ))

    # ----- 5. Coase axiom line -----
    ax.axhline(DELTA_MIN, color=COASE_COLOR, linewidth=2.2,
               linestyle="-", zorder=4)
    ax.text(
        0.05, DELTA_MIN + 0.020,
        r"Coase axiom: floor $\geq \delta_{\min} > 0$",
        color=COASE_COLOR, fontsize=10.5, ha="left", va="bottom",
        fontweight="bold", zorder=5,
    )

    # ----- 6. Region labels -----
    # Impossibility — left side (slow-amortization mechanism)
    ax.text(
        0.55, 0.86,
        "IMPOSSIBILITY\n" r"(slow-$\alpha$ mechanism)",
        fontsize=12.5, color=IMP_COLOR, ha="center", va="center",
        fontweight="bold", alpha=0.85, zorder=3,
    )
    # Impossibility — right side (floor-dominated mechanism)
    ax.text(
        2.55, 0.86,
        "IMPOSSIBILITY\n" r"(floor-dominated)",
        fontsize=12.5, color=IMP_COLOR, ha="center", va="center",
        fontweight="bold", alpha=0.85, zorder=3,
    )

    # ----- 7. Anchor markers -----
    # FFT canon star at (alpha large, floor = 0). Annotation goes ABOVE
    # the line so it doesn't crowd the Coase exclusion text below.
    fft_x, fft_y = ALPHA_MAX - 0.18, free_height / 2
    ax.plot([fft_x], [fft_y], marker="*", markersize=26,
            color=FREE_COLOR, markeredgecolor=INK, markeredgewidth=1.0,
            zorder=8)
    ax.annotate(
        "FFT canon: free descent\n"
        r"($\alpha \to \infty$, floor $= 0$)",
        xy=(fft_x, fft_y),
        xytext=(2.85, 0.92),
        fontsize=9.5, color=FREE_COLOR, ha="center", va="center",
        fontweight="bold", zorder=9,
        arrowprops=dict(arrowstyle="->", color=FREE_COLOR, lw=0.8,
                        connectionstyle="arc3,rad=-0.15"),
    )

    # Program working hypothesis
    prog_x, prog_y = 1.85, 0.60
    ax.plot([prog_x], [prog_y], marker="o", markersize=14,
            color=IMP_COLOR, markeredgecolor=INK, markeredgewidth=1.2,
            zorder=8)
    ax.annotate(
        "program working\nhypothesis",
        xy=(prog_x + 0.10, prog_y - 0.01),
        xytext=(2.40, 0.62),
        fontsize=9.5, color=IMP_COLOR, ha="left", va="center",
        fontweight="bold", zorder=9,
        arrowprops=dict(arrowstyle="->", color=IMP_COLOR, lw=0.8),
    )

    # Debt #2 marker — question mark inside the band
    ax.text(
        ALPHA_CRIT, 0.32, "?",
        color=DEBT_COLOR, fontsize=56, ha="center", va="center",
        fontweight="bold", zorder=8,
    )
    ax.annotate(
        "debt #2: where exactly does\n"
        "the mechanism boundary sit?\n"
        r"(additivity, amortization, bypass)",
        xy=(ALPHA_CRIT - 0.10, 0.32),
        xytext=(0.30, 0.55),
        fontsize=9.5, color=DEBT_COLOR, ha="left", va="center",
        fontweight="bold", zorder=9,
        arrowprops=dict(arrowstyle="->", color=DEBT_COLOR, lw=0.8),
    )

    # ----- 8. Lemma B annotation -----
    # Lemma B's existence claim: the program domain stays bounded away from
    # the FFT corner. Drawn as a curved dashed arrow from the working
    # hypothesis to the corner, labeled "Lemma B blocks".
    ax.annotate(
        "",
        xy=(fft_x - 0.10, fft_y + 0.020),
        xytext=(prog_x + 0.07, prog_y - 0.08),
        arrowprops=dict(
            arrowstyle="-|>", color=ANNOT_GREY, lw=1.2,
            linestyle="--", connectionstyle="arc3,rad=0.45",
        ),
        zorder=6,
    )
    ax.text(
        2.85, 0.34,
        "Lemma B: no finite\ncomposition zeros the\nfloor — this descent\nroute is blocked",
        fontsize=9.0, color=ANNOT_GREY, ha="center", va="center",
        style="italic", fontweight="bold", zorder=7,
    )

    # ----- 9. Axis setup -----
    ax.set_xlim(ALPHA_MIN, ALPHA_MAX)
    ax.set_ylim(FLOOR_MIN, FLOOR_MAX)
    ax.set_xlabel(
        r"amortization rate $\alpha$    "
        r"($\delta_k \sim k^{-\alpha}$ under composition$\;\longrightarrow$ faster decay)",
        fontsize=11,
    )
    ax.set_ylabel(
        r"asymptotic floor $\delta_\infty$    "
        r"($\uparrow$ irreducible per-composition fee)",
        fontsize=11,
    )
    ax.grid(True, color=GRID, linewidth=0.5, zorder=0)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=9.5)

    # ----- 10. Title and caption -----
    fig.suptitle(
        r"The $\delta$-algebra phase plot",
        fontsize=14.5, fontweight="bold", y=0.97,
    )

    caption = (
        r"Two axes of $\delta$'s algebra: decay rate under composition ($\alpha$) "
        r"and asymptotic floor ($\delta_\infty$). "
        "Both axes are projections of higher-dimensional algebra space "
        "(additivity, amortization, bypass-resistance, representation-dependence). "
        "Coase axiom puts the program above floor $= \\delta_{\\min}$; FFT canon "
        "lives below it, unreachable. Debt #2 is the shape of the mechanism "
        "boundary inside the program's domain — drawn here as a band of uncertainty."
    )
    fig.text(0.5, 0.015, caption, ha="center", fontsize=8.8,
             color="#444", style="italic", wrap=True)

    plt.tight_layout(rect=[0, 0.07, 1, 0.95])
    return fig


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(os.path.dirname(here))
    figures_dir = os.path.join(repo_root, "figures")
    os.makedirs(figures_dir, exist_ok=True)
    output_path = os.path.join(figures_dir, "delta_phase_plot.png")

    fig = build_figure()
    fig.savefig(output_path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)

    print(output_path)


if __name__ == "__main__":
    main()
