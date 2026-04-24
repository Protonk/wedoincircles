# NEAR-HALF-GAPS

![Near-half gaps](../../figures/counting_near_half_gaps.png)

The near-half-gaps figure at `figures/counting_near_half_gaps.png` (built by `n-gons/counting/build_near_half_gaps.py`) is the quantitative companion to the "tested-empty guides" claim in `PSI-STRATIFICATION.md`. For each polygon order `n ∈ [3, 400]` it plots the minimum distance from any outside-out vertex x-coordinate `x_{n,k} = sec(π/n)·cos((2k+1)π/n)` to the two candidate rational guides at `x = ±1/2`, on semi-log y. No exact hit is found for any `n ≤ 400`. The two best approaches are flagged inline: to `+1/2`, gap ≈ `1.55 × 10⁻⁵` at `n = 399`; to `−1/2`, gap ≈ `2.27 × 10⁻³` at `n = 398`. The orange series is `gap to +1/2`, the blue series is `gap to −1/2`.

The two series decay at visibly different rates, and the mechanism is arithmetic. The angular condition for a vertex to sit exactly at `x = +1/2` is `(2k+1)π/n = π/3`, i.e., `3(2k+1) = n` with `2k+1` odd — solvable iff `n ≡ 3 (mod 6)`. On those n the cosine factor is `1/2` *exactly*, and the whole gap reduces to the sec-correction `(sec(π/n) − 1)/2 ≈ π²/(4n²)`. At `n = 399 = 3·133` the mechanism fires cleanly and the gap collapses to the `1/n²` floor. The corresponding condition for `x = −1/2` is `3(2k+1) = 2n` with `2k+1` odd; the left side is odd and the right side is even, so there is no `(n, k)` at which this holds. The best alignment misses by angular `π/(3n)`, giving absolute gap `≈ (√3/2)·π/(3n) ~ 1/n`. That factor-of-`n` worse rate is what separates the two best-approach numbers by ≈ 100× at `n ≈ 399`.

The sawtooth structure comes from the same mechanism, stratified by `n mod 6` for the orange series and `n mod 3` for the blue series. Orange spikes (downward) mark the `n ≡ 3 (mod 6)` events where the exact-cos alignment kicks in; the envelope between spikes tracks the generic `1/n` angular-deviation behavior. Blue has no exact-cos alignment available and tracks a denser `1/n` sawtooth throughout. The envelope of both series follows an overall `~1/n` trend with the orange series dropping to `~1/n²` on its arithmetic-special subsequence.

The exact-hit question is algebraic, not transcendence-theoretic. Setting `x_{n,k} = ±1/2` gives

$$
2\cos\!\left(\frac{(2k+1)\pi}{n}\right) \mp \cos\!\left(\frac{\pi}{n}\right)=0,
$$

equivalently a `ℚ`-linear relation with coefficient pattern `(2, 2, \mp 1, \mp 1)` among four primitive `2n`-th roots of unity. So the natural proof route is cyclotomic: classify the admissible vanishing sums of roots of unity (Conway–Jones 1976, plus the decomposition of non-primitive relations), then check that this coefficient pattern never occurs. The repo has not yet written that proof down, but the expected mechanism is finite algebraic casework, not transcendence.

Three things the figure makes visible without further prose: (i) the "tested-empty" label in PSI-STRATIFICATION.md is a quantitative, not qualitative, empirical claim — no zero was found across 398 orders, with the closest call at `1.55 × 10⁻⁵`; (ii) the `±1/2` asymmetry is not incidental — there is a structural reason, inside the outside-out anchoring, why `+1/2` admits a `1/n²` approach subsequence while `−1/2` is capped at `1/n`, so a compression scheme that treats the two guides symmetrically throws away arithmetic information; (iii) no n up to 400 gives an exact hit, and the expected proof of global non-attainment is cyclotomic rather than transcendence-theoretic — a Conway–Jones-style classification of the associated vanishing sums of roots of unity should close the no-hit statement algebraically. For program context, see `n-gons/counting/PSI-STRATIFICATION.md` and `n-gons/counting/COUNTING.md` §"Structural Decomposition".
