# THICK-SWEEP

Why a tilted straight-line sweep across the Archimedean strip hits at most one vertex at a time, why a sweep with any positive bandwidth eventually hits more, and how the two facts coexist.

## The strip

Each regular polygon `n = 3, …, N` contributes `n` vertices. In the strip view, vertex `k` of polygon `n` sits at angular coordinate `x = (2k+1)/(2n)` on the interval `[0, 1)` (with `0` and `1` identified), at height `y = sec(π/n) − 1`:

```
(x_{n,k}, y_{n,k}) = ((2k+1)/(2n), sec(π/n) − 1),   k = 0, 1, …, n − 1.
```

All `n` vertices of polygon `n` share the same height; different polygons sit at different heights. As `n` grows the height collapses toward `0` (the incircle) and the vertex count grows.

## The thin sweep

A vertical sweep across the strip is degenerate: every vertical line either misses every vertex or hits exactly one, with the lone exception `x = 1/2` where every odd polygon's middle vertex coincides. Tilting the sweep line by `30°` — slope `s = tan(30°) = 1/√3` — gives the same thing: each tilted line still hits at most one vertex. Counting vertices under any single straight-line sweep gives an all-`1`s sequence with no growth, regardless of how large `N` gets.

This is surprising because the vertices proliferate quadratically as `N → ∞`. The question is why a slanted line never eventually sweeps more than one at a time.

For a line of slope `s`, the function `c(x, y) = y − sx` is constant on each line, so a sweep is just a monotone variation of `c`. Each vertex gets a sweep coordinate:

```
c_{n,k} = (sec(π/n) − 1) − s·(2k+1)/(2n).
```

The thin sweep hits two vertices simultaneously iff `c_{n,k} = c_{n',k'}` for distinct `(n, k), (n', k')`. Rearranging:

```
sec(π/n) − sec(π/n') = s · ((2k+1)/(2n) − (2k'+1)/(2n')).
```

The left side lies in the totally real cyclotomic field `ℚ(cos(π/n), cos(π/n'))`. The right is `s` times a rational. For `s = 1/√3`, the equation forces `√3` to relate to a specific cyclotomic element in a way that fails case by case. Empirically, no exact coincidences appear through `N = 100`; the closest pair sits at `c`-distance `≈ 1.4 × 10⁻⁷`. This algebraic rigidity is what keeps the thin sweep from producing anything but `1`s under any single slope.

## The thick sweep

Give the sweep line a positive bandwidth — a band of width `δ` in the sweep coordinate — and the picture changes immediately. For any slope `s ≥ 0` and any `δ > 0`, there is some `N` for which a band of width `δ` contains two or more vertices. Equivalently: the minimum consecutive gap between `c`-values can be made smaller than any prescribed `δ` by choosing `N` large enough.

The argument is pigeonhole. The total vertex count for polygons `n = 3, …, N` is `P(N) = N(N+1)/2 − 3`. Since `sec(π/n) − 1 ≤ sec(π/3) − 1 = 1` for `n ≥ 3`, and `x ∈ [0, 1)`,

```
c_{n,k} = y_{n,k} − s·x_{n,k} ∈ (−s, 1],
```

an interval of length `L = 1 + s`. Sorting the `P(N)` coordinates as `c_{(1)} ≤ c_{(2)} ≤ … ≤ c_{(P)}`, their `P − 1` consecutive gaps are nonnegative reals summing to at most `L`, so by averaging:

```
min_i (c_{(i+1)} − c_{(i)}) ≤ L / (P(N) − 1) = 2(1 + s) / (N(N+1) − 8).
```

For any `δ > 0`, choose `N` so the right side falls below `δ`. Concretely,

```
N > (−1 + √(1 + 8·(2(1+s)/δ + 8))) / 2,
```

and for small `δ` this simplifies to `N ≳ √(2(1 + s)/δ)`. Some pair of consecutive `c`-values then lies within `δ` of each other, and a band of that width centered between them contains both vertices.

## Sharpness

The pigeonhole bound `L / (P − 1)` is the worst case — perfectly equispaced points. For the actual structured vertex set, gaps shrink considerably faster. At slope `s = 1/√3`:

- `N = 20`:  `P = 207`,  bound `7.7 × 10⁻³`,  empirical min gap `2.9 × 10⁻⁵`
- `N = 50`:  `P = 1272`, bound `1.2 × 10⁻³`,  empirical min gap `1.4 × 10⁻⁷`
- `N = 100`: `P = 5047`, bound `3.1 × 10⁻⁴`,  empirical min gap `4.5 × 10⁻⁸`

![Thin-sweep gap decay](../../figures/counting_thick_sweep_gap_decay.png)

The empirical minimum consecutive gap drops far below the averaging bound. The staircase shape is real: the minimum only changes when a new closest pair appears.

The pigeonhole bound is enough for the existence claim; the actual minimum gap appears to shrink polynomially faster, but the argument doesn't require this.

The two regimes coexist. Vertices get arbitrarily close in the `c`-coordinate as `N` grows, but never coincide. The bandwidth `δ` converts proximity into multiplicity.
