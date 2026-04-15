import os
import math

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Mapping:
#   radial:  r in [1, sec(pi/3)=2] -> y = r - 1 in [0, 1]
#   angular: theta in [0, 2pi]     -> x = theta/(2pi) in [0, 1]
#
# n-gon edge k: r = sec(theta - 2*pi*k/n)
#   spans theta in [(2k-1)*pi/n, (2k+1)*pi/n]
#
# n-cir (circumscribed circle of n-gon): y = sec(pi/n) - 1

NS = range(3, 9)
COLORS = {
    3: "#d1495b",
    4: "#2e86ab",
    5: "#168e4f",
    6: "#f4a261",
    7: "#9b59b6",
    8: "#1abc9c",
}


def linspace(start, stop, count):
    if count <= 1:
        return [start]
    step = (stop - start) / (count - 1)
    return [start + i * step for i in range(count)]


def plot(outpath):
    fig, ax = plt.subplots(figsize=(11, 5))

    for n in NS:
        color = COLORS[n]
        y_n = 1.0 / math.cos(math.pi / n) - 1.0
        for k in range(n):
            alpha = 2 * math.pi * k / n
            theta_lo = alpha - math.pi / n
            theta_hi = alpha + math.pi / n
            theta = linspace(theta_lo, theta_hi, 300)
            x = [((t / (2 * math.pi)) % 1.0) for t in theta]
            y = [(1.0 / math.cos(t - alpha)) - 1.0 for t in theta]

            start = 0
            for i in range(len(x) - 1):
                if abs(x[i + 1] - x[i]) > 0.5:
                    if i + 1 - start > 1:
                        ax.plot(x[start:i + 1], y[start:i + 1], color=color, lw=1.4, alpha=0.85)
                    start = i + 1
            if len(x) - start > 1:
                ax.plot(x[start:], y[start:], color=color, lw=1.4, alpha=0.85)
        ax.axhline(y_n, color=color, lw=1.3, linestyle="--", zorder=4, alpha=0.7)
        ax.text(1.01, y_n, f"n={n}  y={y_n:.3f}", fontsize=8.5, va="center", color=color)

    ax.axhline(0, color="black", lw=2.0, zorder=5)
    ax.text(0.01, 0.012, "incircle  (n → ∞)", fontsize=9, va="bottom", color="black")

    ax.set_xlim(0, 1)
    ax.set_ylim(-0.04, 1.08)
    ax.set_xlabel("angle  (0 = 1, wraps at both sides)", fontsize=10)
    ax.set_ylabel("radius  (incircle = 0,  3-cir = 1)", fontsize=10)
    ax.set_title("Archimedean strip  |  n = 3 … 8", fontsize=12)
    ax.axvline(0, color="gray", lw=0.8, ls=":")
    ax.axvline(1, color="gray", lw=0.8, ls=":")
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_xticklabels(["0", "¼", "½", "¾", "1"])

    plt.tight_layout()
    plt.savefig(outpath, dpi=160, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    figdir = os.path.normpath(os.path.join(here, "..", "figures"))
    os.makedirs(figdir, exist_ok=True)
    out = os.path.join(figdir, "archimedean_strip.png")
    plot(out)
    print(f"wrote {out}")
