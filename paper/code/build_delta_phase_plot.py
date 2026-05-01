"""
Build the delta-algebra phase plot for paper/OUTLINE.md §6.

A 2D phase diagram in delta-algebra space. Two axes:
    x: amortization rate alpha       (delta_k ~ k^(-alpha) under composition)
    y: asymptotic floor delta_infty  (lim inf delta — irreducible per-comp fee)

The figure visualizes three distinct claims about the projection:

  - FFT canon: claims free descent at floor = 0 — the entire bottom edge.
    Marked as a continuous strip, not a corner.
  - Lemma B (program's claim, with Coase 1937 as methodological precedent
    for the existence-vs-algebra distinction): no finite composition zeros
    the floor. The bottom edge is foreclosed; the program's working floor
    delta_min sits above it.
  - Debt #2: the *exact* location of delta_min — what amortization, bypass,
    additivity allow — is open. Drawn as a horizontal band straddling
    the working-floor line.

Above the band: a single IMPOSSIBILITY region (the program's claim is
universal across the upper half-plane, not split into mechanisms — one
proof, one mechanism, one shaded region).

Honesty notes (kept in caption):
  - delta_min is not Coase output; Coase establishes existence (delta > 0).
    The uniform lower bound is a *consequence* the program needs to
    establish via Lemma B + Bridge Theorem.
  - The (alpha, floor) projection is from a higher-dimensional algebra
    space (additivity, bypass-resistance, representation-dependence).
"""

import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch, Rectangle


# Palette
COASE_COLOR = "#255c7e"      # blue — program's working floor (Lemma B)
FREE_COLOR = "#2e7d55"       # green — FFT canon's claimed territory
IMP_COLOR = "#b03a2e"        # witness red — impossibility
DEBT_COLOR = "#b8860b"       # mustard — debt #2 / boundary uncertainty
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

# Program's working floor (Lemma B consequence; not a Coase axiom)
DELTA_MIN = 0.12

# Debt #2 band: horizontal extent around the working-floor line
DEBT_BAND_HALF = 0.045


def build_figure():
    fig, ax = plt.subplots(figsize=(11.5, 7.2))

    # ----- 1. Backdrop: shade everything above the working floor as
    # IMPOSSIBILITY (one region, one mechanism). -----
    ax.add_patch(Rectangle(
        (ALPHA_MIN, DELTA_MIN), ALPHA_MAX - ALPHA_MIN,
        FLOOR_MAX - DELTA_MIN,
        facecolor=IMP_FILL, edgecolor="none", zorder=0,
    ))

    # ----- 2. Foreclosed strip (between FFT canon's edge and working floor):
    # hatched blue, "Lemma B forecloses descent through here" -----
    ax.add_patch(Rectangle(
        (ALPHA_MIN, FLOOR_MIN), ALPHA_MAX - ALPHA_MIN, DELTA_MIN,
        facecolor=COASE_FILL, edgecolor=COASE_COLOR,
        hatch="///", linewidth=0.0, zorder=1,
    ))

    # ----- 3. FFT canon's territory: the entire bottom edge (floor = 0).
    # The canon's claim is descent succeeds there; foreclosed by Lemma B. -----
    canon_height = 0.022
    ax.add_patch(Rectangle(
        (ALPHA_MIN, FLOOR_MIN), ALPHA_MAX - ALPHA_MIN, canon_height,
        facecolor=FREE_FILL, edgecolor=FREE_COLOR, linewidth=1.4, zorder=2,
    ))

    # ----- 4. Debt #2 band: horizontal, straddling the working-floor line.
    # The open question is where delta_min actually sits, not where a
    # mechanism-boundary lives inside the impossibility region. -----
    ax.add_patch(Rectangle(
        (ALPHA_MIN, DELTA_MIN - DEBT_BAND_HALF),
        ALPHA_MAX - ALPHA_MIN, 2 * DEBT_BAND_HALF,
        facecolor=DEBT_FILL, edgecolor=DEBT_COLOR,
        hatch="xxx", linewidth=0.0, alpha=0.85, zorder=3,
    ))

    # ----- 5. Working-floor line (program's claim) -----
    ax.axhline(DELTA_MIN, color=COASE_COLOR, linewidth=2.4,
               linestyle="-", zorder=4)
    ax.text(
        0.05, DELTA_MIN + DEBT_BAND_HALF + 0.020,
        r"program's working floor $\delta_{\min}$  (Lemma B + Bridge consequence)",
        color=COASE_COLOR, fontsize=10.5, ha="left", va="bottom",
        fontweight="bold", zorder=6,
    )

    # ----- 6. Single IMPOSSIBILITY region label -----
    ax.text(
        ALPHA_MAX / 2, 0.62,
        "IMPOSSIBILITY",
        fontsize=22, color=IMP_COLOR, ha="center", va="center",
        fontweight="bold", alpha=0.85, zorder=4,
    )
    ax.text(
        ALPHA_MAX / 2, 0.54,
        "(program's claim, universal over the upper half-plane)",
        fontsize=10.5, color=IMP_COLOR, ha="center", va="center",
        style="italic", alpha=0.85, zorder=4,
    )

    # ----- 7. FFT canon: marked as a *territory* (the bottom edge), not a
    # point. The star anchors the (alpha → ∞) limit but the claim covers
    # the entire edge. -----
    fft_x, fft_y = ALPHA_MAX - 0.18, canon_height / 2
    ax.plot([fft_x], [fft_y], marker="*", markersize=26,
            color=FREE_COLOR, markeredgecolor=INK, markeredgewidth=1.0,
            zorder=8)
    ax.annotate(
        "FFT canon's claimed territory:\n"
        r"the entire bottom edge (floor $= 0$)" "\n"
        "★ marks the $\\alpha \\to \\infty$ limit",
        xy=(1.6, canon_height),
        xytext=(1.4, 0.92),
        fontsize=10, color=FREE_COLOR, ha="center", va="center",
        fontweight="bold", zorder=9,
        arrowprops=dict(arrowstyle="->", color=FREE_COLOR, lw=0.8,
                        connectionstyle="arc3,rad=-0.15"),
    )

    # ----- 8. Debt #2 annotation — pinned to the band, not a region inside
    # the impossibility shading. -----
    ax.annotate(
        r"debt #2: where does $\delta_{\min}$ actually sit?" "\n"
        "open under amortization, bypass,\n"
        "additivity, representation-dependence",
        xy=(2.4, DELTA_MIN),
        xytext=(2.45, 0.32),
        fontsize=9.5, color=DEBT_COLOR, ha="left", va="center",
        fontweight="bold", zorder=9,
        arrowprops=dict(arrowstyle="->", color=DEBT_COLOR, lw=0.9),
    )

    # ----- 9. Lemma B arrow: from the impossibility region down through
    # the foreclosed strip, terminating at the FFT canon's edge. The arrow
    # *is* the descent route the proof rules out; the label says exactly
    # what Lemma B says. -----
    ax.annotate(
        "",
        xy=(0.85, canon_height + 0.005),
        xytext=(0.85, 0.55),
        arrowprops=dict(
            arrowstyle="-|>", color=ANNOT_GREY, lw=1.4,
            linestyle="--",
        ),
        zorder=6,
    )
    ax.text(
        0.97, 0.34,
        "Lemma B blocks this\n"
        "descent route:\n"
        "no finite composition\n"
        "zeros the floor",
        fontsize=9.5, color=ANNOT_GREY, ha="left", va="center",
        style="italic", fontweight="bold", zorder=7,
    )

    # ----- 10. (Coase methodological-precedent line moved to caption.) -----

    # ----- 11. Axis setup -----
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

    # ----- 12. Title and caption -----
    fig.suptitle(
        r"The $\delta$-algebra phase plot",
        fontsize=14.5, fontweight="bold", y=0.97,
    )

    caption = (
        r"Two axes project a higher-dimensional $\delta$-algebra space "
        "(additivity, amortization, bypass-resistance, representation-dependence). "
        r"Three distinct claims about the projection: (i) FFT canon claims free "
        r"descent on the entire bottom edge (floor $= 0$); (ii) Lemma B + Bridge "
        r"forecloses that edge, leaving a working floor $\delta_{\min} > 0$; "
        r"(iii) debt #2 asks where $\delta_{\min}$ sits exactly — open under "
        "amortization, bypass, additivity. One mechanism, one impossibility region. "
        r"Coase 1937 is methodological precedent for the existence-vs-algebra "
        r"distinction; it establishes $\delta > 0$, not the uniform bound."
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
