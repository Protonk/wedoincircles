"""
Small-case walkthrough at n = 7.

Closes the "Candidate artifact" line in `memos/COUNTING-APPARATUS.md` §(D):
a single figure showing three small-case measures around n = 7 at n ∈ [5, 9],
with the closure-failure at n = 7 visibly marked.

The three cost measures are:

    (1) Ruler-and-compass cost. Finite (= tower depth log₂(φ(2n)/2)) if
        cos(π/n) is constructible, ∞ otherwise. This is the half-angle /
        node-side layer. Constructible iff 2n is in the Gauss-Wantzel set:
        2n = 2^a · (product of distinct Fermat
        primes), each Fermat prime to power 1. In the plotted window
        n ∈ [5, 9]:
          constructible:     n ∈ {5, 6, 8}
          non-constructible: n ∈ {7, 9}     ← closure failures

    (2) Trace-side algebraic depth. 2cos(2π/n) has degree φ(n)/2 over ℚ,
        and x_{n,1} = 2cos(2π/n) - 1 shows the outside-out row already
        lives in the same trace field ℚ(cos(2π/n)). At fixed target
        precision the cost is poly(φ(n)/2); use the degree itself as the
        arithmetic-depth proxy. The jump from degree 2 (at n = 5) / 1
        (at n = 6) to degree 3 (at n = 7) is the first cubic on the
        trace side.

    (3) Counting-apparatus observable. |M_n| = length of the outside-out
        counting word for the sweep n' = 3..n, computed via
        counting_utils.multiplicity_word(n). Step increment
        |M_n| − |M_{n−1}| exposes the per-polygon contribution.

The figure has three stacked panels with shared x-axis n ∈ [5, 9].
Non-constructible n are shaded pink; a vertical guide at n = 7 marks
the first non-constructible / first cubic trace field.
"""

import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
from counting_utils import multiplicity_word  # noqa: E402


# --- Gauss-Wantzel constructibility ---------------------------------------

FERMAT_PRIMES = (3, 5, 17, 257, 65537)


def _factor_odd(m):
    """Dict of (odd prime → exponent) for the odd integer m."""
    factors = {}
    d = 3
    while d * d <= m:
        while m % d == 0:
            factors[d] = factors.get(d, 0) + 1
            m //= d
        d += 2
    if m > 1:
        factors[m] = factors.get(m, 0) + 1
    return factors


def is_constructible_2n(n):
    """True iff 2n = 2^a · (product of distinct Fermat primes)."""
    m = 2 * n
    while m % 2 == 0:
        m //= 2
    if m == 1:
        return True
    factors = _factor_odd(m)
    for p, e in factors.items():
        if p not in FERMAT_PRIMES or e != 1:
            return False
    return True


# --- algebraic depth ------------------------------------------------------

def euler_phi(m):
    result = m
    temp = m
    p = 2
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result -= result // p
        p += 1
    if temp > 1:
        result -= result // temp
    return result


def trace_degree(n):
    """Degree of 2cos(2π/n) over ℚ = φ(n) / 2 for n ≥ 3."""
    return euler_phi(n) // 2


def tower_depth_if_pow2(deg):
    """log₂(deg) if deg is a positive power of two, else None."""
    if deg <= 0 or (deg & (deg - 1)) != 0:
        return None
    return deg.bit_length() - 1


# --- data assembly --------------------------------------------------------

N_MIN = 5
N_MAX = 9


def gather_data():
    rows = []
    prev_len = len(multiplicity_word(N_MIN - 1)[0])
    for n in range(N_MIN, N_MAX + 1):
        counts = multiplicity_word(n)[0]
        length = len(counts)
        deg = trace_degree(n)
        half_angle_deg = euler_phi(2 * n) // 2
        constructible = is_constructible_2n(n)
        tower = tower_depth_if_pow2(half_angle_deg) if constructible else None
        rows.append({
            "n": n,
            "two_n": 2 * n,
            "phi_2n": euler_phi(2 * n),
            "phi_n": euler_phi(n),
            "trace_deg": deg,
            "constructible": constructible,
            "tower_depth": tower,
            "M_len": length,
            "M_step": length - prev_len,
        })
        prev_len = length
    return rows


def write_tsv(rows, outpath):
    cols = ["n", "two_n", "phi_2n", "phi_n", "trace_deg", "constructible",
            "tower_depth", "M_len", "M_step"]
    with open(outpath, "w") as f:
        f.write("\t".join(cols) + "\n")
        for r in rows:
            vals = []
            for c in cols:
                v = r[c]
                if v is None:
                    vals.append("inf")
                elif isinstance(v, bool):
                    vals.append("T" if v else "F")
                else:
                    vals.append(str(v))
            f.write("\t".join(vals) + "\n")


# --- figure ---------------------------------------------------------------

def plot_three_panels(rows, outpath):
    ns = np.array([r["n"] for r in rows])
    degs = np.array([r["trace_deg"] for r in rows])
    lens = np.array([r["M_len"] for r in rows])
    steps = np.array([r["M_step"] for r in rows])
    constr = np.array([r["constructible"] for r in rows])

    non_c_ns = ns[~constr]

    fig, (ax1, ax2, ax3) = plt.subplots(
        3, 1, figsize=(11, 11), sharex=True,
        gridspec_kw={"hspace": 0.22},
    )

    def decorate(ax):
        for nc in non_c_ns:
            ax.axvspan(nc - 0.4, nc + 0.4, color="#f6d7d7", alpha=0.45,
                       zorder=0)
        ax.axvline(7, color="#b03030", lw=1.3, alpha=0.55, zorder=1)
        ax.grid(True, color="0.92", lw=0.4, axis="y")

    # --- panel 1: RC cost ---
    decorate(ax1)
    for r in rows:
        if r["constructible"]:
            ax1.plot([r["n"]], [r["tower_depth"]], marker="o", ms=12,
                     color="#2c7a2c", markeredgecolor="black",
                     markeredgewidth=0.7, zorder=5)
            ax1.annotate(f"depth {r['tower_depth']}",
                         xy=(r["n"], r["tower_depth"]),
                         xytext=(0, 12), textcoords="offset points",
                         ha="center", fontsize=9, color="#2c7a2c")
        else:
            ax1.plot([r["n"]], [2.4], marker="^", ms=11,
                     color="#b03030", markeredgecolor="black",
                     markeredgewidth=0.6, zorder=5)
            ax1.annotate(r"$\infty$",
                         xy=(r["n"], 2.4), xytext=(0, 12),
                         textcoords="offset points",
                         ha="center", va="center", fontsize=16,
                         color="#b03030", zorder=6)

    ax1.set_ylim(-0.5, 3.2)
    ax1.set_ylabel(r"$\log_2(\varphi(2n)/2)$  or  $\infty$", fontsize=11)
    ax1.set_title(
        "node side:   tower depth if constructible",
        fontsize=11.5, loc="left",
    )
    ax1.set_yticks([0, 1, 2, 3])

    # --- panel 2: trace-field degree ---
    decorate(ax2)
    ax2.vlines(ns, 0, degs, color="#2c5d8f", lw=2.2, zorder=5)
    ax2.plot(ns, degs, marker="o", ms=11, color="#2c5d8f", lw=0,
             markeredgecolor="black", markeredgewidth=0.7, zorder=6)
    for n, d in zip(ns, degs):
        ax2.annotate(f"{d}", xy=(n, d), xytext=(0, 9),
                     textcoords="offset points", ha="center", fontsize=9,
                     color="#2c5d8f")

    ax2.set_ylim(0, max(degs) + 1.5)
    ax2.set_ylabel(r"$\varphi(n)/2$", fontsize=11)
    ax2.set_title(
        r"trace side:   degree of $2\cos(2\pi/n)=x_{n,1}+1$ over $\mathbb{Q}$",
        fontsize=11.5, loc="left",
    )
    ax2.set_yticks(range(0, max(degs) + 2))

    # --- panel 3: counting ledger ---
    decorate(ax3)
    bar_container = ax3.bar(ns, lens, width=0.55, color="#d28a2e", alpha=0.78,
                            edgecolor="black", linewidth=0.6, zorder=5,
                            label=r"$|M_n|$  (counting word length)")
    for n, L in zip(ns, lens):
        ax3.annotate(f"{L}", xy=(n, L), xytext=(0, 4),
                     textcoords="offset points", ha="center", fontsize=9,
                     color="#7a4f1c")

    ax3b = ax3.twinx()
    step_line, = ax3b.plot(ns, steps, marker="s", ms=9, color="#7a2c7a",
                           lw=1.4, zorder=7,
                           label=r"step increment $|M_n| - |M_{n-1}|$")
    for n, s in zip(ns, steps):
        ax3b.annotate(f"+{s}", xy=(n, s), xytext=(7, -2),
                      textcoords="offset points", fontsize=8.5,
                      color="#7a2c7a")
    ax3b.set_ylabel("step increment", color="#7a2c7a", fontsize=10)
    ax3b.tick_params(axis="y", colors="#7a2c7a")
    ax3b.set_ylim(0, max(steps) + 2)

    ax3.set_ylabel(r"$|M_n|$", fontsize=11)
    ax3.set_title(
        "counting apparatus:   outside-out word length, step increment",
        fontsize=11.5, loc="left",
    )
    ax3.set_xlabel(r"polygon order  $n$", fontsize=12)
    ax3.set_xticks(ns)
    # color tick labels red at non-constructible n so the closure-failure set
    # is legible even without the pink shading.
    for tick, n_val in zip(ax3.get_xticklabels(), ns):
        if n_val in set(non_c_ns.tolist()):
            tick.set_color("#b03030")
            tick.set_fontweight("bold")

    lines = [bar_container, step_line]
    labels = [l.get_label() for l in lines]
    ax3.legend(lines, labels, loc="upper left", framealpha=0.95, fontsize=9)

    fig.suptitle(
        r"Three small-case measures around $n = 7$,   $n \in [5, 9]$",
        fontsize=14, fontweight="bold", y=0.995,
    )
    fig.text(
        0.5, 0.010,
        r"pink bands / red ticks mark Gauss–Wantzel non-constructible $n$"
        r"  —   $n = 7$ is first cubic on the trace side, first non-constructible on the node side",
        ha="center", fontsize=10, color="0.35", style="italic",
    )

    plt.tight_layout(rect=[0.0, 0.035, 1.0, 0.965])
    plt.savefig(outpath, dpi=170)
    plt.close(fig)


# --- entry point ----------------------------------------------------------

def main():
    figdir = os.path.normpath(os.path.join(HERE, "..", "..", "figures"))
    os.makedirs(figdir, exist_ok=True)

    rows = gather_data()

    # print the table
    header = (f"{'n':>3}  {'2n':>3}  {'φ(2n)':>6}  {'φ(n)':>5}  {'tr':>4}  "
              f"{'constr?':>8}  {'tower':>5}  {'|M_n|':>5}  {'Δ|M_n|':>7}")
    print(header)
    print("-" * len(header))
    for r in rows:
        tower_str = "∞" if r["tower_depth"] is None else str(r["tower_depth"])
        print(f"{r['n']:>3}  {r['two_n']:>3}  {r['phi_2n']:>6}  "
              f"{r['phi_n']:>5}  {r['trace_deg']:>4}  "
              f"{'yes' if r['constructible'] else 'NO':>8}  "
              f"{tower_str:>5}  {r['M_len']:>5}  "
              f"{r['M_step']:>+7}")

    tsv_path = os.path.join(HERE, "case_seven_table.tsv")
    write_tsv(rows, tsv_path)
    print(f"\nwrote {tsv_path}")

    fig_path = os.path.join(figdir, "case_seven_three_costs.png")
    plot_three_panels(rows, fig_path)
    print(f"wrote {fig_path}")


if __name__ == "__main__":
    main()
