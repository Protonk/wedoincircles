import os
import math
from fractions import Fraction

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle

# The un-inverted annulus {1 <= r <= 2}: bend the Archimedean strip the
# natural way, so the strip top (3-cir) lands at the outer boundary r = 2
# and the strip bottom (incircle) lands at the inner boundary r = 1.
#
# n-gon edge k: straight line at distance 1 from origin, tangent to the
#   incircle at angle 2*pi*k/n. Polar form r = sec(theta - 2*pi*k/n),
#   valid on theta in [(2k-1)*pi/n, (2k+1)*pi/n].
# n-gon corners: at angles (2k+1)*pi/n, radius sec(pi/n).
# n-cir (circumscribed circle of the n-gon): full circle at r = sec(pi/n).
#
# As n grows, sec(pi/n) \downarrow 1. The n-cirs converge down onto the
# incircle from outside; each n-gon is squeezed in the annulus
# [1, sec(pi/n)].

NS = range(3, 9)
COLORS = {
    3: "#d1495b",
    4: "#2e86ab",
    5: "#168e4f",
    6: "#f4a261",
    7: "#9b59b6",
    8: "#1abc9c",
}
XLIM = (-2.07, 1.10)
YLIM = (-1.88, 1.88)


def linspace(start, stop, count):
    if count <= 1:
        return [start]
    step = (stop - start) / (count - 1)
    return [start + i * step for i in range(count)]


def visible_upper_corner_rays():
    rays = {}
    for n in NS:
        r_outer = 1.0 / math.cos(math.pi / n)
        for k in range(n):
            angle = Fraction(2 * k + 1, n)
            if angle > 1:
                continue
            x = r_outer * math.cos(math.pi * float(angle))
            y = r_outer * math.sin(math.pi * float(angle))
            if XLIM[0] <= x <= XLIM[1] and YLIM[0] <= y <= YLIM[1]:
                rays[angle] = COLORS[n]
    return sorted(rays.items())


def semicircle_regions():
    regions = []
    prev = Fraction(0, 1)
    for angle, color in visible_upper_corner_rays():
        width = angle - prev
        if width > 0:
            regions.append((width / 2, color, angle))
        prev = angle
    return sorted(regions, key=lambda item: (-item[0], item[2]))


def add_semicircle_area_inset(ax):
    regions = semicircle_regions()
    bar_height = 0.078
    x0 = -1.95
    y0 = -1.78
    total_height = bar_height * len(regions)

    y = y0 + total_height - bar_height
    for area, color, _ in regions:
        width = float(area) / bar_height
        ax.add_patch(
            Rectangle(
                (x0, y),
                width,
                bar_height,
                facecolor=color,
                edgecolor=color,
                alpha=0.72,
                lw=1.0,
                zorder=30,
            )
        )
        y -= bar_height

    x_right = -1.15
    y = -y0 - total_height
    for area, color, _ in regions:
        width = float(area) / bar_height
        ax.add_patch(
            Rectangle(
                (x_right - width, y),
                width,
                bar_height,
                facecolor=color,
                edgecolor=color,
                alpha=0.72,
                lw=1.0,
                zorder=30,
            )
        )
        y += bar_height


def plot(outpath):
    fig, ax = plt.subplots(figsize=(7, 7))
    fig.patch.set_facecolor("#f8f5ef")
    ax.set_facecolor("#f8f5ef")

    for n in NS:
        color = COLORS[n]
        r_outer = 1.0 / math.cos(math.pi / n)  # sec(pi/n)
        verts = [
            (
                r_outer * math.cos((2 * k + 1) * math.pi / n),
                r_outer * math.sin((2 * k + 1) * math.pi / n),
            )
            for k in range(n)
        ]
        ax.add_patch(
            Polygon(
                verts,
                closed=True,
                facecolor=color,
                edgecolor=color,
                lw=2.6,
                alpha=0.72,
                joinstyle="miter",
                zorder=n,
            )
        )

    ax.add_patch(
        Circle(
            (0, 0),
            1.0,
            facecolor="#f8f5ef",
            edgecolor="none",
            zorder=20,
        )
    )
    for n in NS:
        color = COLORS[n]
        r_outer = 1.0 / math.cos(math.pi / n)
        for k in range(n):
            angle = (2 * k + 1) * math.pi / n
            x = r_outer * math.cos(angle)
            y = r_outer * math.sin(angle)
            if not (XLIM[0] <= x <= XLIM[1] and YLIM[0] <= y <= YLIM[1]):
                continue
            ax.plot(
                [math.cos(angle), 0.0],
                [math.sin(angle), 0.0],
                color=color,
                lw=1.8,
                alpha=0.78,
                solid_capstyle="round",
                zorder=21,
            )
    ax.add_patch(
        Circle(
            (0, 0),
            1.0,
            facecolor="none",
            edgecolor=(0.38, 0.38, 0.38, 0.86),
            lw=2.0,
            zorder=22,
        )
    )
    add_semicircle_area_inset(ax)

    ax.set_xlim(*XLIM)
    ax.set_ylim(*YLIM)
    ax.set_aspect("equal")
    ax.axis("off")

    plt.tight_layout()
    plt.savefig(outpath, dpi=160, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "figures"))
    os.makedirs(figdir, exist_ok=True)
    out = os.path.join(figdir, "archimedean_outside_out.png")
    plot(out)
    print(f"wrote {out}")
