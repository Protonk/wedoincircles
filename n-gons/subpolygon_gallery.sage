"""
Subpolygon gallery for the designated-wholeness refinement.

Companion to `n-gons/SUBPOLYGON.md`.

Show eight anchored n-gons through their tangency-point sets on the shared
incircle. All ambient tangency points are drawn as open circles. Whole
tangency points are filled. When the whole set has order g >= 3, draw the
regular anchored g-gon circumscribing the same incircle; when g = 2, draw the
surviving diameter; when g = 1, only the anchor survives.
"""

import os
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle as MplCircle
from matplotlib.colors import Normalize


CASES = (
    (7, 360),
    (11, 360),
    (10, 36),
    (9, 12),
    (8, 36),
    (6, 360),
    (8, 360),
    (12, 36),
)


def whole_data(n, dh):
    g = math.gcd(n, dh)
    q = n // g
    positions = [(j * q) % n for j in range(g)]
    return g, q, positions


def point_on_circle(angle, radius=1.0):
    return (radius * math.cos(angle), radius * math.sin(angle))


def polygon_vertices_from_tangencies(g):
    if g < 3:
        return []
    radius = 1.0 / math.cos(math.pi / g)
    return [
        point_on_circle((2 * j + 1) * math.pi / g, radius)
        for j in range(g)
    ]


def draw_subpolygon(ax, g, color):
    if g == 1:
        return
    if g == 2:
        xs = [1.0, -1.0]
        ys = [0.0, 0.0]
        ax.plot(xs, ys, color=color, lw=1.4, zorder=2)
        return

    verts = polygon_vertices_from_tangencies(g)
    verts.append(verts[0])
    xs = [p[0] for p in verts]
    ys = [p[1] for p in verts]
    ax.plot(xs, ys, color=color, lw=1.4, zorder=2)


def panel(ax, n, dh, cmap, norm):
    g, q, whole_positions = whole_data(n, dh)
    color = cmap(norm(g))

    ax.add_patch(MplCircle((0.0, 0.0), 1.0, fill=False, ec="0.65", lw=1.5, zorder=1))
    draw_subpolygon(ax, g, color)

    all_angles = [2.0 * math.pi * k / n for k in range(n)]
    all_points = [point_on_circle(theta) for theta in all_angles]
    ax.scatter(
        [p[0] for p in all_points],
        [p[1] for p in all_points],
        s=26,
        facecolors="white",
        edgecolors="0.25",
        linewidths=0.8,
        zorder=3,
    )

    whole_angles = [2.0 * math.pi * k / n for k in whole_positions]
    whole_points = [point_on_circle(theta) for theta in whole_angles]
    ax.scatter(
        [p[0] for p in whole_points],
        [p[1] for p in whole_points],
        s=48,
        c=[color],
        edgecolors="black",
        linewidths=0.6,
        zorder=4,
    )

    ax.plot([1.0], [0.0], marker="*", color="black", ms=10, zorder=5)

    ax.set_title(f"n = {n}, DH = {dh} | g = {g}, q = {q}", fontsize=10)
    ax.set_aspect("equal")
    ax.set_xlim(-1.45, 1.45)
    ax.set_ylim(-1.45, 1.45)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)


def plot(outpath):
    cmap = plt.get_cmap("viridis")
    norm = Normalize(vmin=1, vmax=max(math.gcd(n, dh) for n, dh in CASES))

    fig, axes = plt.subplots(2, 4, figsize=(14, 7))
    for ax, (n, dh) in zip(axes.flat, CASES):
        panel(ax, n, dh, cmap, norm)

    fig.suptitle(
        "Whole positions as anchored subpolygons on the shared incircle",
        fontsize=14,
        y=0.99,
    )
    plt.tight_layout()
    plt.savefig(outpath, dpi=160)
    plt.close(fig)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "figures"))
    os.makedirs(figdir, exist_ok=True)
    out = os.path.join(figdir, "subpolygon_gallery.png")
    plot(out)
    print(f"wrote {out}")
