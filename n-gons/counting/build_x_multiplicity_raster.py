"""
Cumulative vertex-density raster for the outside-out corner sweep.

Previous version: a dot scatter of M_N cluster multiplicities, with marker
size encoding count.  That was a dot plot with an area encoding, not a
raster.

New version: a true 2D heatmap (log color).  For each row N ∈ [3, 40] we
compute the kernel density of all vertex x-coordinates belonging to
polygons of order n ≤ N — the same underlying point cloud as M_N, but
rendered as a cumulative density rather than a clustered multiplicity.
The observable changes: multiplicity-at-clusters → density-in-x-space.
Backbone columns (x ∈ {-2, -1, 0, +1}) accumulate mass linearly in N;
interior x positions pick up at-most-one vertex per polygon so the
accumulation is slow, and the dynamic range compresses onto a log scale.
"""

import os
import math

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import numpy as np


N_MIN = 3
N_MAX = 40

X_MIN = -2.25
X_MAX = 1.25
NX = 700

SIGMA_BINS = 1.3          # Gaussian smoothing in x, in bin units
LOG_FLOOR = 0.04          # display floor for log color scale


def vertex_x(n, k):
    return (1.0 / math.cos(math.pi / n)) * math.cos((2 * k + 1) * math.pi / n)


def gaussian_smooth_x(array, sigma):
    """1D Gaussian convolution along the last (x) axis, per-row."""
    radius = int(np.ceil(3.0 * sigma))
    idx = np.arange(-radius, radius + 1)
    ker = np.exp(-(idx ** 2) / (2.0 * sigma ** 2))
    ker /= ker.sum()
    result = np.empty_like(array)
    for i in range(array.shape[0]):
        result[i] = np.convolve(array[i], ker, mode="same")
    return result


def build_raster():
    x_edges = np.linspace(X_MIN, X_MAX, NX + 1)
    n_rows = N_MAX - N_MIN + 1
    raster = np.zeros((n_rows, NX))
    cumulative = np.zeros(NX)
    for i, N in enumerate(range(N_MIN, N_MAX + 1)):
        xs_for_N = np.array([vertex_x(N, k) for k in range(N)])
        hist, _ = np.histogram(xs_for_N, bins=x_edges)
        cumulative = cumulative + hist
        raster[i] = cumulative
    return raster, x_edges


def plot(outpath):
    raster, x_edges = build_raster()
    smoothed = gaussian_smooth_x(raster, SIGMA_BINS)
    display = np.where(smoothed > LOG_FLOOR, smoothed, LOG_FLOOR)

    y_edges = np.arange(N_MIN - 0.5, N_MAX + 1.5, 1.0)

    fig, ax = plt.subplots(figsize=(13, 8.5))

    mesh = ax.pcolormesh(
        x_edges, y_edges, display,
        norm=LogNorm(vmin=LOG_FLOOR, vmax=float(smoothed.max())),
        cmap="inferno", shading="auto",
    )

    # Backbone guides in pale warm yellow, drawn on top with light alpha
    for gx in (-2.0, -1.0, 0.0, 1.0):
        ax.axvline(gx, color="#ffe28a", ls=":", lw=0.9, alpha=0.45, zorder=3)
    # Tested-empty guides in pale orange
    for gx in (-0.5, 0.5):
        ax.axvline(gx, color="#ff9a55", ls="--", lw=0.9, alpha=0.40, zorder=3)

    ax.set_xlim(X_MIN, X_MAX)
    ax.set_ylim(N_MIN - 0.5, N_MAX + 0.5)
    ax.set_xlabel(r"vertex $x$-coordinate", fontsize=12)
    ax.set_ylabel(r"polygon order  $N$    (cumulative through $n \leq N$)", fontsize=12)

    tick_spec = [
        (-2.0, r"$-2$",      "#c4923f"),
        (-1.0, r"$-1$",      "#c4923f"),
        (-0.5, r"$-1/2$",    "#c9662a"),
        ( 0.0, r"$0$",       "#c4923f"),
        ( 0.5, r"$+1/2$",    "#c9662a"),
        ( 1.0, r"$+1$",      "#c4923f"),
    ]
    ax.set_xticks([p for p, _, _ in tick_spec])
    ax.set_xticklabels([lbl for _, lbl, _ in tick_spec])
    for tick_label, (_, _, color) in zip(ax.get_xticklabels(), tick_spec):
        tick_label.set_color(color)
        tick_label.set_fontweight("bold")
    ax.set_yticks(list(range(5, N_MAX + 1, 5)))

    ax.tick_params(colors="0.25")
    for spine in ax.spines.values():
        spine.set_color("0.4")

    cbar = fig.colorbar(mesh, ax=ax, pad=0.01, fraction=0.035)
    cbar.set_label(r"cumulative vertex density    (log scale)",
                   fontsize=11, color="0.25")
    cbar.ax.tick_params(labelsize=9, colors="0.25")

    fig.suptitle(
        r"Cumulative vertex-density raster of the outside-out sweep  "
        r"(semantic: density, not cluster multiplicity)",
        fontsize=14, fontweight="bold", y=0.995,
    )
    fig.text(
        0.5, 0.955,
        r"row $N$ = kernel density on $x$ of all vertices from polygons $n \leq N$;   "
        r"bright columns: backbone accumulation;   "
        r"dark columns at $x = \pm 1/2$: tested-empty",
        ha="center", fontsize=10.5, color="0.3", style="italic",
    )
    fig.text(
        0.5, 0.015,
        r"yellow dotted guides: backbone $x \in \{-2,-1,0,+1\}$;   "
        r"orange dashed guides: $x = \pm 1/2$;   "
        r"kernel $\sigma \approx %.1f$ bins;   inferno log colormap" % SIGMA_BINS,
        ha="center", fontsize=9.5, color="0.35", style="italic",
    )

    plt.tight_layout(rect=[0.0, 0.035, 1.0, 0.935])
    plt.savefig(outpath, dpi=170, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "..", "figures"))
    os.makedirs(figdir, exist_ok=True)
    out = os.path.join(figdir, "counting_x_multiplicity_raster.png")
    plot(out)
    print(f"wrote {out}")
