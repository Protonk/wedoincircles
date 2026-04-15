"""
Leash Plot A: the monotonicity leash condition.

Companion to `corners/LEASH.md`.

Shows the monotonicity leash condition in a single panel,
Marklof–Strömbergsson Figure 3 style:

  - Green half-plane (y ≤ 0): admissible region for the target curve's
    rightmost point. A target whose rightmost point lies here produces
    a monotone right-pane curve (no fold).
  - Dashed horizontal at y = 0: the leash boundary.
  - Three target curves overlaid:
      baseline   c =  0    (unit circle at origin),  rightmost (1,  0)   — on boundary
      safe       c = −0.5  (translated down),        rightmost (1, −0.5) — in green
      fold       c = +0.5  (translated up),          rightmost (1, +0.5) — above boundary

Why this figure: the leash condition is "target curve's rightmost
point has y ≤ 0." The green region makes the condition visual; the
three target curves test it; the rightmost-point markers show where
each target lands relative to the leash.
"""

import os
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle as MplCircle, Rectangle


def plot(outpath):
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))

    # --- frame ---
    xmin, xmax = -1.2, 1.55
    ymin, ymax = -1.6, 1.6
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.set_aspect("equal")

    # --- green half-plane: admissible region y ≤ 0 ---
    ax.add_patch(Rectangle(
        (xmin, ymin), xmax - xmin, -ymin,
        facecolor="#c2e5c2", alpha=0.45,
        edgecolor="none", zorder=0,
    ))

    # --- leash boundary: y = 0, dashed ---
    ax.axhline(0, color="0.3", ls="--", lw=1.1, zorder=2)

    # --- chord family: faint positive-slope rays from origin at a few angles ---
    for n in (3, 5, 10, 30):
        angle = math.pi / n
        # extend to the right edge of the frame or until y exceeds ymax
        x_end = xmax - 0.05
        y_end = x_end * math.tan(angle)
        if y_end > ymax - 0.1:
            y_end = ymax - 0.1
            x_end = y_end / math.tan(angle)
        ax.plot([0, x_end], [0, y_end],
                color="0.55", lw=0.8, alpha=0.5, zorder=1)

    # --- three target curves (color-coded by leash status) ---
    # baseline: c = 0, solid black
    ax.add_patch(MplCircle(
        (0, 0), 1.0,
        fill=False, ec="black", lw=1.6, zorder=3,
    ))
    # safe: c = -0.5, dashed green
    ax.add_patch(MplCircle(
        (0, -0.5), 1.0,
        fill=False, ec="#1f7a1f", lw=1.6, ls="--", zorder=3,
    ))
    # fold: c = +0.5, dashed red
    ax.add_patch(MplCircle(
        (0, 0.5), 1.0,
        fill=False, ec="#b03030", lw=1.6, ls="--", zorder=3,
    ))

    # --- rightmost points, color-coded ---
    rightmost_points = [
        (1.0,  0.0, "black",   "c = 0  (baseline): rightmost on boundary"),
        (1.0, -0.5, "#1f7a1f", "c = −0.5 (safe): rightmost in green"),
        (1.0,  0.5, "#b03030", "c = +0.5 (fold): rightmost above boundary"),
    ]
    for (x, y, color, label) in rightmost_points:
        ax.plot([x], [y], marker="o", color=color, ms=10,
                markeredgecolor="black", markeredgewidth=0.7, zorder=6)
        dy = 10 if y >= 0 else -16
        ax.annotate(f"({x:.0f}, {y:+.1f})",
                    xy=(x, y), xytext=(8, dy),
                    textcoords="offset points", fontsize=9, color=color,
                    zorder=7)

    # --- origin ---
    ax.plot([0], [0], marker="*", color="black", ms=13, zorder=8)
    ax.annotate("origin", xy=(0, 0), xytext=(-28, -14),
                textcoords="offset points", fontsize=9, zorder=8)

    # --- inline labels ---
    # leash boundary
    ax.annotate("leash boundary  y = 0",
                xy=(-1.1, 0), xytext=(0, 4),
                textcoords="offset points", fontsize=9, color="0.3")

    # admissible region
    ax.annotate("admissible region\n(target rightmost at y ≤ 0)",
                xy=(-0.55, -1.15), fontsize=10, color="#1f7a1f",
                ha="center", va="center", zorder=5)

    # chord family
    ax.annotate("chord family\n(positive-slope rays\nfrom origin)",
                xy=(1.1, 1.1), fontsize=9, color="0.45",
                ha="left", va="top")

    # target curve labels near each circle
    ax.annotate("baseline (c = 0)",
                xy=(-1.02, 0.25), fontsize=9, color="black")
    ax.annotate("safe (c = −0.5)",
                xy=(-1.02, -0.35), fontsize=9, color="#1f7a1f")
    ax.annotate("fold (c = +0.5)",
                xy=(-1.02, 0.85), fontsize=9, color="#b03030")

    # --- minimal axis ticks ---
    ax.set_xticks([-1, 0, 1])
    ax.set_yticks([-1, -0.5, 0, 0.5, 1])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(
        "Leash Plot A: the monotonicity leash condition\n"
        "target curve's rightmost point must lie at y ≤ 0 to avoid a fold",
        fontsize=12,
    )
    ax.grid(False)

    plt.tight_layout()
    plt.savefig(outpath, dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "figures"))
    os.makedirs(figdir, exist_ok=True)
    out = os.path.join(figdir, "leash_plot_a.png")
    plot(out)
    print(f"wrote {out}")
