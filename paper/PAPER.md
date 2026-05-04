# FFT paper

# §Intro

## §Intro.1. The claim
We prove an impossibility theorem: FFT-style methods, defined by closure under the canon's native operations under a uniform-charge cost model, cannot improve past their existing lower-bound thresholds on cyclotomic-DFT and adjacent compute-cost problems. 

The thresholds in question are heterogeneous — Morgenstern's `Ω(n log n)` bounded-coefficient additive bound, Winograd's modular-product `μ(T_P) = 2n − k`, AFW's multiplicative-complexity threshold under rational equivalence. 

The impossibility lands at each one in its own currency.

## §Intro.2. The frame
The cost framework imports Coase 1937's transaction-cost vocabulary, generalized from economic-coordination friction to measure-theoretic non-nesting overhead. 

Each conversion across the bounded/unbounded coefficient boundary carries an irreducible cost `δ`; the thresholds are *located by* — not held above — that friction. 

§3.6.2 demonstrates currency-stratification on both sides: canon source non-transfer algorithm-side, witnessed by Morgenstern↔Ailon's forced shift from determinant to entropy potential at the normalized FFT; and non-nesting measure-theoretic readings substrate-side, witnessed by the planar isoperimetric gap's rate, constant, and almost-every registers.

Lower bounds are not numbers; they are measurements made in particular coordinate systems.

## §Intro.3. Proof ingredients

The local substrate fact is Theorem K, a σ-algebra coarsening result on the integer-indexed lattice: `f₁ = φ(n)/2`, `f₂ = L_n`, and `f₃ = Δ_n` are unrecoverable from Farey coordinates. The cost-side object is T4b, a currency-universal boundary object `(Z, ℱ, ν, δ)` that carries the algorithm-side currencies and the substrate-side iso registers in one coordinate system.

The theorem is conditional on a cost-form of effective Hermite–Lindemann at `n = 1`, the variable-precision canon re-read under the §1.2 guard, and a rigorous form of the type-gap at `f_{ca}`.

Figure [figures/native_f_closure_mismatch.png](figures/native_f_closure_mismatch.png) shows flat affine closure against the unbounded `φ(n)/2` cyclotomic ladder.

# §1. Cost, conversion, and defect

## §1.1. The accounting stack

The accounting stack has four nested objects: cost model, cost currencies, conversion strategies, and transaction cost `δ`. The cost model governs what is charged; the currencies say what is being counted; the conversion is the adaptive family of strategies trading one currency for another; `δ` is the cost attached to that conversion. The same `δ` typing ranges over algorithm-side currencies (`(μ, α)`) and substrate-side currencies (§5.2's iso/-register triple).

## §1.2. Cost model

We work in a uniform-charge / logarithmic-measure cost model in the Cook–Reckhow 1973 / Slot–van Emde Boas 1984 sense. Bit growth is charged. Advice strings, oracle constants, and table-per-size shortcuts are admissible only when their construction and storage are charged inside the method at the same granularity (§4.2.1). Variable precision is handled by re-reading Morgenstern, Winograd, AFW, and Ailon under the same guard (§6.5).

## §1.3. Cost currencies

The two algorithm-side cost currencies are multiplicative cost `μ` and additive cost `α`. They are currencies inside the §1.2 cost model: measures of what is being counted.

### §1.3.1. Multiplicative cost

The cost-bearing primitives are multiplications; the complexity measure `μ` counts them under bilinear / rational-equivalence accounting. Schönhage–Strassen 1971, Winograd 1978, and Auslander–Feig–Winograd 1984 each give `μ` structure on cyclotomic-DFT and adjacent computations; the full presentation is §3.

### §1.3.2. Additive cost

The cost-bearing primitives are additions; the complexity measure `α` counts them, sensitive to the coefficient regime. Morgenstern 1973's `Ω(n log n)` bounded-coefficient additive lower bound is the structure-bearing result, presented at §3.3. Ailon 2013 is the adjacent normalized-FFT comparison and the clearest in-canon witness for currency-stratification: in a layered `2 × 2` unitary-gate model, matrix entropy gives the same `Ω(n log n)` scale without determinant growth — Morgenstern's determinant method does not reach the normalized FFT (whose determinant has modulus 1), and entropy is needed in its place. §3.6.2 develops this as the content claim that currency-stratification is forced.

## §1.4. Coefficient regimes

Bounded versus unbounded coefficients. The regime is a parameter of every cost measure on either side, and many bounds — Morgenstern's notably — depend on which regime is in force. The bounded/unbounded coefficient boundary is the measure-theoretic state space where `δ` is evaluated at §6.2 / §6.3.

## §1.5. Conversion as adaptive strategy family

The mult/add conversion is the family of strategies FFT-style algorithms use to trade multiplicative cost for additive cost or vice versa. Methods select a strategy adaptively from problem data: Gauss 1805's `4 × 3` versus `3 × 4` factorization of the Pallas computation is the pre-1882 worked example (Goldstine 1977, §4.12–13). The conversion is an adaptive strategy family closed under composition, not a single partial function.

Adaptive currency-choice relocates where `δ` appears; it does not make the conversion frictionless.

## §1.6. Transaction cost `δ`

The conversion has a transaction cost. Following Coase 1937, we keep two questions separate: whether the cost is non-zero (`δ > 0`) and what algebra that cost obeys.

Amortization across repeated uses and asymptotics in size and precision both couple, via the Lindemann–Weierstrass envelope, to effective Hermite–Lindemann at `n = 1` (§6.5). Representation-dependence under change of coordinates is handled by the adaptive-family reading of §1.5; bypass-resistance under specialist intermediation is handled by the regularity guard of §1.2. Additivity under composition is represented by the cocycle composition law of §6.5. The floor extension from at-threshold to past-threshold is the bridge between `δ > 0` at `T(P)` and the implication claim past `T(P)`.

The framework hosts more than the §1.3 `(μ, α)` currency pair. `δ` is the transaction cost between *any two non-nesting measure-theoretic readings of one quantity*. The algorithm-side instance is the bounded/unbounded coefficient conversion. The substrate-side instance is §5.2's iso/-register triple — three non-nesting measure-theoretic readings of the planar isoperimetric gap (rate, constant, almost-every), with `5π ≈ 15.7×` worked-instance overhead between rate and constant on the chained Sobolev → geometric route, and a categorial type-gap to almost-every (`iso/THREE-REGISTER-SYNTHESIS.md` Claim 1).

## §1.7. Candidate cocycle realization

The concrete coordinate for `δ` is `{Δ_k}` cocycle compression: the failure-to-agree of cocycle-product factors across butterfly refinements and primitive modes, measured pointwise. The formal composition law is the cocycle composition law of §6.5; the faithfulness conditions are the T4b package at §6.3.

## §1.8. Threshold interface `T(P)`

For a problem `P`, the threshold `T(P)` is the lower-bound frontier supplied by the three sources — Morgenstern's `Ω(n log n)` additive on bounded coefficients, AFW's multiplicative-complexity threshold under rational equivalence, Winograd's modular-product `μ(T_P) = 2n − k`, each in its own currency. Descent past `T(P)` means trading a higher cost-bearing bound for a lower one by reorganizing the computation. The endpoint commitment of §6.2 ties such descent to `δ → 0` at the bounded/unbounded coefficient boundary, which in the cocycle coordinate reads as competitive `{Δ_k}` compression.

Figure: [figures/cost_conversion_schematic.png](figures/cost_conversion_schematic.png) — the cost-pair `(μ, α)` plane with the three thresholds (Morgenstern, AFW, Winograd) marked, the counterfactual `δ = 0` frontier, the hatched `δ`-gap between them, and the endpoint implication at the bounded/unbounded coefficient boundary.

# §2. The conversion

The FFT is the conversion of multiplication and addition on the circle. The mult/add conversion is the family of strategies FFT-style methods use to trade multiplicative cost for additive cost on the cyclotomic substrate, with roots of unity indexed by the integer lattice `L = {(k, n) : 1 ≤ k < n, n ≥ 3}`.

It is adaptive: methods select strategies from problem data, and the class is closed under composition (§1.5, §4.2.3).

The five sources expose the conversion in different cost coordinates: Schönhage–Strassen builds it operationally; Morgenstern measures it from the additive side under bounded coefficients; Winograd factors it through the CRT modular product; Auslander–Feig–Winograd decomposes it through cyclotomic semisimple structure; Ailon measures it through matrix entropy on a restricted unitary-gate model.

The failure is two halves of one boundary fact: existence (`δ > 0` at `T(P)`) and implication (`δ → 0` past `T(P)`), joined by the floor-extension step of §6.2.

The heterogeneity across the three lower bounds is what failure looks like algorithm-side: each source picks up a piece of cost-coordinate space and none transfers across the boundary cleanly (§3.6.2).

Morgenstern's determinant potential cannot reach the normalized FFT, and matrix entropy is forced in its place at Ailon 2013 (§3.2).

The substrate side carries its own failure shape: §5.2's three iso registers (rate, constant, almost-every) are non-nesting measure-theoretic readings of the planar isoperimetric gap, with `5π` worked overhead between rate and constant and a categorial type-gap to almost-every.

The reduction map `R: L → F` from the integer-indexed lattice to the Farey set induces σ-algebra coarsening on `L`; the substrate observables `f₁ = φ(n)/2`, `f₂ = L_n`, `f₃ = Δ_n` do not factor through `R` (proved in companion form at §5.6).

K certifies that the substrate has structure the conversion has to respect; the impossibility theorem (§6.6) composes K with the cost-algebra apparatus to say no FFT-style method can drive `δ → 0` past `T(P)`.

# §3. Cards on the table

## §3.1. The canon together

Five sources from 1971 through 2013 carry the FFT lower-bound apparatus used here. Morgenstern 1973, Winograd 1978, and Auslander–Feig–Winograd 1984 supply the three threshold entries. Schönhage–Strassen 1971 and Ailon 2013 supply cost-model methodology: the former gives the operational uniform-charge bit/gate baseline; the latter shows how a change of model forces a change of potential.

Within §1's framing, the three lower bounds occupy distinct cost-coordinate cells — Morgenstern at bounded-coefficient additive cost, Winograd at unbounded multiplicative cost on polynomial-quotient rings, Auslander–Feig–Winograd at unbounded multiplicative cost on cyclotomic decomposition — and they exhaust the cells the impossibility theorem of §4 takes as its scope. §4.4 makes the threshold definition formal.

```
+------------------------------+----------------------------------------+------------------------------------------------------------+---------------------------------------------+
| Source                       | Setting                                | Result + mechanism                                         | Where the mechanism unbinds                 |
+------------------------------+----------------------------------------+------------------------------------------------------------+---------------------------------------------+
| Morgenstern 1973             | bounded coefficients (|c_i| ≤ c for    | Ω(n log n) additive cost via determinant potential: the    | unbounded coefficients (potential unbinds   |
|                              | some constant c); linear-circuit /     | DFT matrix has determinant |det| = n^(n/2), and a bounded  | when gate growth is no longer constant);    |
|                              | additive accounting                    | gate grows the running determinant by at most a constant   | multiplicative cost (potential measures     |
|                              |                                        | factor                                                     | volume, not bilinear multiplications); the  |
|                              |                                        |                                                            | normalized FFT (determinant has modulus 1)  |
+------------------------------+----------------------------------------+------------------------------------------------------------+---------------------------------------------+
| Winograd 1978                | unbounded rational-equivalence;        | exact bilinear multiplicative complexity μ(T_P) = 2n − k   | additive cost (bilinear ledger blind to     |
|                              | bilinear multiplicative accounting on  | for degree-n polynomial with k irreducible factors over    | additions); bounded coefficients (rational  |
|                              | polynomial-quotient rings              | the base field, via CRT decomposition: polynomial          | equivalence permits unbounded scalar        |
|                              |                                        | multiplication mod T_P reduces factor-by-factor over       | substitutions); content outside             |
|                              |                                        | residue rings, with the bound from counting essential      | polynomial-quotient ring structure          |
|                              |                                        | bilinear multiplications per factor                        |                                             |
+------------------------------+----------------------------------------+------------------------------------------------------------+---------------------------------------------+
| Auslander–Feig–Winograd 1984 | unbounded rational-equivalence;        | factor-by-factor multiplicative complexity via cyclotomic  | additive cost; bounded coefficients;        |
|                              | bilinear multiplicative accounting on  | decomposition ℚ[G] = ∏_(d | |G|) ℚ(ζ_d) (one cyclotomic    | content outside the rational-equivalence    |
|                              | finite-abelian-group DFTs              | factor per divisor d of |G|), with μ computed per factor   | equivalence relation (linear-rational       |
|                              |                                        | under rational equivalence                                 | substitutions are free)                     |
+------------------------------+----------------------------------------+------------------------------------------------------------+---------------------------------------------+
```

> **Table 1: The three FFT lower bounds.** Each row presents one bound's setting, result and mechanism, and the regions where the mechanism unbinds.

## §3.2. The cost-model methodology: Schönhage–Strassen 1971 and Ailon 2013

Two papers, four decades apart, establish how the FFT lower-bound apparatus counts. Schönhage–Strassen 1971 sets the operational uniform model: bit and gate primitives charged at logarithmic-measure granularity, recursive composability, root-of-unity arithmetic in the ring `Z/F_n Z` (where `F_n = 2^{2^n} + 1` is a Fermat number and `2` is a primitive `2^{n+1}`-th root of unity, so root multiplication reduces to a cyclic shift). The headline result is constructive — integer multiplication in `O(N log N log log N)` bit operations via recursive FFT decomposition — and it is upper-bound only; Schönhage–Strassen is not a lower-bound theorem. It supplies the cost-model the lower-bound apparatus counts inside.

Ailon 2013 supplies the sensitivity. In a restricted layered model — `n` live coordinates, each gate a `2 × 2` unitary mixing of two coordinates — Ailon proves that any circuit computing the normalized Fourier transform requires at least `(1/2) n log_2 n` gates — the same `Ω(n log n)` scale as Morgenstern, on a different cost coordinate. The mechanism is the matrix-entropy potential `Φ(M) = −∑_{p,q} |M(p,q)|² log_2 |M(p,q)|²`: `Φ(Id) = 0`, `Φ(F) = n log_2 n` for the normalized Fourier matrix, and one native `2 × 2` unitary gate raises `Φ` by at most 2. Morgenstern's determinant potential measures volume growth; the normalized FFT has determinant of modulus 1; the determinant potential cannot see it. The Morgenstern↔Ailon comparison is the field-internal witness that non-transfer between cost currencies is structural, not a missing proof.

## §3.3. Morgenstern 1973

Morgenstern's bounded-coefficient additive lower bound: any linear circuit computing the `n`-point DFT under coefficients bounded by a constant `c` requires `Ω(n log n)` additions. The mechanism is a determinant-potential argument — the DFT matrix has determinant of magnitude `n^{n/2}` (Vandermonde-style), and in the bounded-coefficient model each gate grows the running determinant by at most a constant factor, so reaching the full determinant requires `Ω(n log n)` gates. The bounded-coefficient regime is essential: without it the determinant potential does not bind, as the §3.2 normalized FFT case witnesses (modulus 1, matrix-entropy forced in its place). The result fills the additive `α` slot on the bounded side of §1.4.

## §3.4. Winograd 1978

Winograd's modular-product theorem: for a degree-`n` polynomial `T_P` with `k` irreducible factors over the base field, the bilinear multiplicative complexity of multiplication mod `T_P` is exactly `μ(T_P) = 2n − k`. The mechanism is CRT decomposition — polynomial multiplication mod `T_P` reduces to factor-by-factor multiplication in the residue rings, and the lower bound follows by counting essential bilinear multiplications inside each factor. The result fills the multiplicative `μ` slot on the unbounded rational-equivalence side of §1.4; the CRT-cyclotomic factor ledger is what §3.5's Auslander–Feig–Winograd extends from polynomial-quotient rings to the full cyclotomic-DFT class.

## §3.5. Auslander–Feig–Winograd 1984

Auslander–Feig–Winograd's semisimple cyclotomic decomposition of finite-abelian DFTs: the group ring `ℚ[G]` of a finite abelian group `G` decomposes by CRT into a product of cyclotomic fields `ℚ(ζ_d)` (one per divisor `d` of `|G|`), and the DFT factors accordingly. Multiplicative complexity is computed factor-by-factor under rational equivalence — bilinear and linear-rational substitutions are free, only essential nonrational multiplications count. The result extends Winograd's modular-product accounting (§3.4) from polynomial-quotient rings to the full semisimple algebra structure of finite-abelian-group DFTs, filling the multiplicative `μ` slot on the unbounded cyclotomic side of §1.4.

## §3.6. Common cost / conversion structure

The three lower bounds of §3.3–§3.5 share the same cost / conversion stack while occupying different cost-coordinate cells.

## §3.6.1. Translation into the §1 stack

The three lower bounds have distinct coordinates in §1's stack: cost model and guard, currency, regime, conversion role, and `δ` status.

Morgenstern 1973 lives in a bounded-coefficient linear-composition setting; its currency is additive `α`; its regime sits on the bounded side of §1.4 (the determinant potential binds only there); its conversion role is to supply the additive floor against which conversion is measured; its `δ` status is no transfer to unbounded coefficients. Winograd 1978 lives in bilinear / rational-equivalence accounting; currency is multiplicative `μ`; regime is unbounded rational-equivalence; conversion role is the CRT modular-product ledger; `δ` status is no transfer to bounded coefficients or to additive cost. Auslander–Feig–Winograd 1984 sits at rational-equivalence cyclotomic decomposition; currency is multiplicative `μ`; regime is unbounded cyclotomic; conversion role is factor-by-factor multiplicative accounting via CRT decomposition; `δ` status is no transfer to bounded coefficients or to additive cost.

The §1.2 uniform-charge / logarithmic-measure guard supplies the common charging frame. Where a source does not itself formulate variable-precision charging, §6.5 re-reads it under that guard.

## §3.6.2. What's structurally shared

The shared structure is the stack: charged operations, cost currencies, a coefficient-regime boundary, strategy-family composition, and an unpaid transaction cost at the boundary. Two of the three lower bounds sit on the multiplicative side (Winograd modular product, Auslander–Feig–Winograd cyclotomic); Morgenstern is the additive-side floor, and the only one whose lower bound requires bounded coefficients. None of the three transfers a bound across another's coefficient regime or cost currency. Every such transfer is exactly what §1.6 calls `δ`, and §6 must prove that native FFT-style methods cannot make that payment vanish.

`T(P)` is structurally plural: a frontier with currency-specific entries — Auslander–Feig–Winograd multiplicative on unbounded, Morgenstern's `Ω(n log n)` additive on bounded, Winograd's modular-product `μ(T_P) = 2n − k`. Improving past `T(P)` means improving past one entry in its own currency.

The algorithm-side argument is correspondingly currency-stratified: the endpoint commitment, the T4b boundary object, and the candidate transport must land in every cell of `T(P)`. `δ` is conceptually single but realizes in a chosen cost-norm; the three-cell currency plurality forces a `δ`-tuple.

Theorem K (§5.6) is currency-blind: a σ-algebra fact on the integer-indexed lattice, indifferent to cost-counting and equally applicable across algorithm-side currencies (§1.3) and substrate-side iso/ registers (§5.2). The substrate side carries its own currency-stratification: the three iso/ registers (rate, constant, almost-every) are non-nesting measure-theoretic readings of the planar isoperimetric gap, with `5π ≈ 15.7×` worked-instance overhead between rate and constant ([iso/THREE-REGISTER-SYNTHESIS.md](iso/THREE-REGISTER-SYNTHESIS.md) Claim 1) and a categorial type-gap to almost-every.

§3.2 supplies the in-canon witness for non-transfer: Morgenstern's determinant potential cannot reach the normalized FFT, and Ailon's matrix-entropy potential is forced in its place. Translation across the three threshold currencies is not free.

# §4. Main theorem

## §4.1. Scope

The theorem concerns lower-bound methods built from the FFT canon's native operations under the cost model of §1.2. It does not range over all possible lower-bound methods.

## §4.2. FFT-style methods

An FFT-style method is a uniformly described strategy family whose per-size methods are finite compositions of the native operations of §4.2.2, possibly with adaptive choices, charged under §4.2.1, and closed under composition.

## §4.2.1. Model and regularity guard

An in-scope method is charged in the uniform-charge / logarithmic-measure sense of §1.2.

Operation cost, stored precision, coefficient size, precomputed tables, and size-dependent constants must be paid for at the same granularity.

Advice strings, oracle constants, table-per-size shortcuts, and growing hidden state are outside the class unless their construction and storage costs are explicitly charged inside the method.

## §4.2.2. Standard composability of the canon
The native operations are those each source contributes to the FFT-style toolkit, with each entry traced to its §3 lineage: recursive FFT decomposition (Schönhage–Strassen 1971, §3.2), CRT / tensor factorization (Winograd 1978, §3.4; AFW 1984, §3.5), linear-composition closure (all four sources; cf. §3.6.1), cyclotomic factor accounting (AFW 1984, §3.5), and coefficient-regime bookkeeping (Morgenstern 1973, §3.3).

The class is closed under finite composition of these operations when the §4.2.1 guard is respected.

## §4.2.3. The class defined

The proof in §6.6 classifies finite compositions of those operations.

## §4.3. Cyclotomic-DFT and adjacent

The problem class contains cyclotomic DFTs and compute-cost problems sharing §1's cost / conversion structure. Adjacent problems may differ in inputs, but not in the currencies, coefficient regimes, and conversion boundary the lower bounds inhabit.

## §4.4. Existing thresholds

`T(P)` is the lower-bound frontier on problem `P` the impossibility theorem of §4.5 is stated against. Three sources supply its entries, each at a distinct cost-coordinate cell in §1's framing — Morgenstern 1973 at bounded-coefficient additive cost (§3.3), Winograd 1978 at unbounded multiplicative cost on polynomial-quotient rings (§3.4), Auslander–Feig–Winograd 1984 at unbounded multiplicative cost on cyclotomic-decomposed group DFTs (§3.5).

These three define `T(P)`. The impossibility theorem of §4.5 applies to bounds at these three cells; FFT lower-bound results at coordinates outside §1's admitted framing — for example, Ailon 2013's `(1/2) n log_2 n` in a restricted layered unitary-gate model, presented at §3.2 as cost-model methodology — are outside the theorem's scope by construction.

The plurality of `T(P)` across these three distinct cost currencies is handled by the currency-universal limit `Z` of §6.3.

## §4.5. The theorem

For every FFT-style method `M` (§4.2) and every problem `P` (§4.3), `M` does not prove a lower bound on `P` improving past the existing threshold `T(P)` of §4.4.

## §4.6. A worked adversary

Let `M_FR` be the *Farey-regularized recursive FFT*: at each butterfly stage, `M_FR` attempts to coarsen its cyclotomic index by passing `(k, n)` through the reduction map `R: (k, n) ↦ (k/g, n/g)` (with `g = gcd(k, n)`) to read on the Farey side, then composes the residual through every adaptive escape FFT-style closure permits.

The method is native: recursive decomposition, linear composition, cyclotomic factor accounting, and adaptive choice from problem data, all under §4.2.1's regularity guard. Farey reduction is the natural regularization move on cyclotomic indices, and gcd-equivalence-class amortization would absorb residue if it were compatible with the threshold data.

The mult-add trade fails at the cost-algebra obstruction (§6.3, §6.4): §3.6.2's currency-stratification makes cross-currency conversion read on `δ`, and `δ` does not vanish at the bounded/unbounded coefficient boundary.

The remaining escape routes fail at the same boundary object. Farey recoding strips off `f₁, f₂, f₃`, which do not factor through `R` by Theorem K (§5.6). Cross-register iso conversion runs into §5.2's non-nesting and the `5π` worked overhead between rate and constant. Precomputed tables and advice are outside the class unless charged at the same granularity by §4.2.1, with the per-sample cost form supplied by effective Hermite–Lindemann at `n = 1` (§6.5).

Thus `M_FR` exhibits the same four channels the proof classifies in §6.6: Farey recoding, cross-register iso conversion, cross-currency mult-add trading, and size-dependent tables/advice.

# §5. Substrate facts

## §5.1. Rotation-orbit Diophantine kinematics

The substrate here lives on `T = ℝ/ℤ`, not on `L`. Irrationality of `π` places the orbit `{kπ mod 1}` in Weyl's equidistribution regime against Haar measure; finite irrationality measure for `π` (audited L-W-safe at [rotations/BETA-PI-LW-AUDIT.md](rotations/BETA-PI-LW-AUDIT.md), with Mahler 1953 the cheapest witness via `μ(π) < 42`) further gives the Avila–Jitomirskaya parameter `β(π) = 0` (where `β(α) := limsup_{n→∞} (ln q_{n+1}) / q_n` over the continued-fraction denominators of `α`), the stronger discrepancy-side classification.

What the substrate gives is Haar-mean access for continuous and Riemann-integrable test functions, plus the `β(π) = 0` Diophantine classification. The data lives on `T`, and transcription to a scalar `L`-observable is not immediate.

## §5.2. Non-nesting isoperimetric registers

The planar isoperimetric gap `Δ = L² − 4πA` admits three measure-theoretic readings on non-nesting hypothesis classes: *rate* (asymptotic decay along a parametric family of convex curves approaching a disk), *constant* (pointwise sharp inequality on a single convex curve, Bonnesen-strengthening per Osserman 1979 / Bonnesen 1924 — the annulus-width form `Δ ≥ 4π · d²` the §5.2 derivation routes through; convex restriction keeps substrate-side content pre-1882 in the L-W-envelope sense, avoiding the post-1882 Jordan curve theorem), and *almost-every* (full-measure under a distribution on parameter space, Khintchine / Beck 1994 tradition).

Worked-instance witnesses for non-nesting: the thin ellipse `(a = 2, b = 1/2)` and the small-spike `r(θ) = 1 + ε cos(5θ)` give the two pairwise non-inclusions on curve-shape space; Beck's class lives on `α`-parameter space and is type-incompatible with both. Worked-instance overhead between rate and constant: `5π ≈ 15.7×` weaker than Bonnesen direct on the chained Sobolev → geometric route, with no single extremal function realizing all three sharpnesses simultaneously ([iso/THREE-REGISTER-SYNTHESIS.md](iso/THREE-REGISTER-SYNTHESIS.md) Claim 1).

The three readings are currencies in §1.6's transaction-cost sense, with the non-nesting plus the worked overhead supplying a substrate-side `δ > 0` instance.

## §5.3. Closed-form polygon arithmetic

Hurwitz Fourier expansion on the sparse lattice `m ≡ 1 mod n` fixes three closed-form values for the inscribed regular `n`-gon: the polygon perimeter `L_n = 2n sin(π/n)`, the isoperimetric gap rate `Δ_n = 4π⁴/(3n²) + O(1/n⁴)`, and the first-band concentration constant `6/π² = 1/ζ(2)`. The first-band concentration follows from the `ζ(2)`-tail comparison `B_j(n) ≤ B_1(n)/j²`: the leading Fourier mode carries at least `6/π² ≈ 60.8%` of `Δ_n` ([corners/HURWITZ-FIRST-BAND-CONCENTRATION.md](corners/HURWITZ-FIRST-BAND-CONCENTRATION.md) §1).

Figures: [figures/archimedean_triptych.png](figures/archimedean_triptych.png) sets up the inside-out / outside-out / strip substrate; [figures/hurwitz_gap_rate.png](figures/hurwitz_gap_rate.png) closes the Hurwitz identity at the `4π⁴/(3n²)` Archimedean rate (three series collapse to one line over seven decades); [figures/hurwitz_gap_frequency_decomposition.png](figures/hurwitz_gap_frequency_decomposition.png) shows the first-band concentration `B_1(n) ≥ (6/π²) Δ_n` directly as a stacked-area chart over `n`.

## §5.4. Cyclotomic-ladder unboundedness against affine flatness

The maximal real subfield `K_n^+ = ℚ(ζ_n + ζ_n^{−1})` has degree `[K_n^+ : ℚ] = φ(n)/2` over `ℚ`, which grows unbounded with `n`. Affine closure over `ℚ` is flat.

Figure: [figures/pseudo_chebyshev_arithmetic_ladder.png](figures/pseudo_chebyshev_arithmetic_ladder.png) — degrees of `cos(π/n)` over `ℚ` as a stem chart, constructible nodes filled and non-constructible open, with `n = 7` highlighted as the first cubic and first non-constructible node.

## §5.5. The admissibility envelope

The L-W envelope governs substrate-side reasoning: tools are admitted by *content* not by *calendar*, with each post-1882 import requiring a per-instance audit that the proof depends on pre-1882 content (per [memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md)). Within the envelope, no admissible method extracts additional descent information beyond what the substrate already supplies.

The operative measure-theoretic fact is the Lebesgue null/full dichotomy on `ℝ`: the algebraics are null and the transcendentals are full. Finer distinctions among transcendentals — irrationality measure, transcendence type, Diophantine class — trigger per-instance content-not-calendar audits; §5.1's `β(π) = 0` import is the leading example, with Mahler 1953's `μ(π) < 42` the cheapest L-W-safe witness.

## §5.6. Theorem K — substrate-side σ-algebra coarsening

F-side coordinates strip exactly the substrate observables an adversary would need to read its threshold position.

**Theorem K.** *Let `L = {(k, n) ∈ ℤ² : 1 ≤ k < n, n ≥ 3}` and `F = {(p, q) ∈ ℤ² : 1 ≤ p < q, gcd(p, q) = 1}` carry their atomic σ-algebras, and let `R : L → F`, `R(k, n) = (k/g, n/g)` with `g = gcd(k, n)`, be the reduction map. Then `R⁻¹(2^F) ⊂ 2^L` is exactly the σ-algebra of fiber-constant subsets, and the three substrate observables `f₁(k, n) = φ(n)/2` (cyclotomic-ladder degree), `f₂(k, n) = L_n = 2n sin(π/n)` (polygon perimeter; equivalently the Hurwitz first Fourier coefficient via `c_1^{(n)} = L_n²/(4π²)`), and `f₃(k, n) = Δ_n = L_n²(1 − (π/n) cot(π/n))` (isoperimetric gap rate) are not fiber-constant — hence not `R⁻¹(2^F)`-measurable, equivalently they do not factor through `R`.*

Proof at [measure/FOR-BREAKFAST.md](measure/FOR-BREAKFAST.md) §K.0–§K.4. The three observables are non-fiber-constant on the witness pairs `f₁(1, 5) = 2 ≠ 4 = f₁(3, 15)`, `f₂(1, 3) = 3√3 ≠ 6 = f₂(2, 6)`, and `f₃(1, 3) ≈ 10.68 ≠ 3.35 ≈ f₃(2, 6)`. An apparatus restricted to F-side data — denominator-rank, Thomae-height, Stern-Brocot depth, Minkowski `?`-derivative, or any other function on `F` lifted by `R*` — cannot recover `f₁`, `f₂`, `f₃`.

**Kernel partition.** The direct K2 instances are §5.2 rate via `f₃`, §5.2 constant plus §5.3 Hurwitz Fourier on the sparse lattice `m ≡ 1 mod n` via `f₂` (equivalently `c_1^{(n)} = L_n²/(4π²)`), and §5.4 cyclotomic ladder via `f₁`. The non-direct faces sit before K2: §5.1's rotation-orbit kinematics live on `T = ℝ/ℤ` rather than on `L`; §5.5's L-W null/full Lebesgue dichotomy is fiber-constant on `L` under literal reading, with finer cyclotomic-depth content collapsing back to §5.4's `f₁`. The almost-every register of §5.2 requires a parameter family before it transcribes to a scalar `L`-observable.

**Cyclotomic-rigidity support.** *T1 (off-backbone empty contour):* `sec(π/n) cos((2k+1)π/n) ≠ ±1/2` for all `n ≥ 3`, `0 ≤ k < n`. The proof squares, traces from `K_n` to `ℚ`, applies the Ramanujan-sum reduction `4 c_n(2k+1) = μ(n) − 3 φ(n)`, and excludes by `φ(h)`. Niven's rationality theorem does not directly apply: T1 is the rationality of a ratio of two cyclotomic cosines, not of a single one.

# §6. The measure of the conversion

## §6.1. Descent in the cost framework

Descent in §1's framework means trading a higher cost-bearing complexity bound for a lower one by reorganizing the computation. Lower-bound improvement *is* successful descent; §6 asks whether descent past `T(P)` is reachable by FFT-style methods.

Because `T(P)` has distinct cost currencies, the endpoint commitment, T4b, and the candidate transport are asserted currency-by-currency over the algorithm-side currencies (`μ`, `α`). The substrate-side iso/ currencies of §5.2 enter as `δ > 0` facts through T4b.

## §6.2. Endpoint commitment

For descent past `T(P)` to succeed, the algorithm must drive `δ` at the bounded/unbounded coefficient boundary toward zero. In the cocycle coordinate of §1.7 this is competitive compression of the per-sample `{Δ_k}` cost object.

At `T(P)`, any FFT-style method pays `δ ≥ δ_min(P) > 0` at the bounded/unbounded coefficient boundary, currency-by-currency. Strict improvement past `T(P)` requires `δ → 0`. The floor extends past threshold because T4b.4 reads the rate-to-constant overhead as a positive `δ`-floor proportional to the relevant polygon gap `Δ_n`; the exact normalization, including the worked `(5π - 1) · Δ_n` instance, belongs to T4b.3/T4b.4 rather than to the endpoint commitment.

## §6.3. T4b — decompressed boundary package

T4b is a package of seven named statements. Together they construct a currency-universal measurable object, define the `δ` coordinate, and make the obstruction visible to FFT-style closure. The decomposition keeps existence, normalization, iso-register detection, algorithm-side faithfulness, and closure-class measurability separate.

### §6.3.0. T4b.0 — currency diagram

Let `D_T` be the small measurable diagram whose algorithm-side nodes are `C_Mor` (Morgenstern bounded-additive), `C_Win` (Winograd modular-product multiplicative), and `C_AFW` (AFW cyclotomic-multiplicative), and whose substrate-side nodes are `N_rate`, `N_const`, and `N_aae` from §5.2. Bookkeeping nodes record coefficient regime, precision, rational-equivalence quotienting, and table/advice state when those data are needed to make a morphism's domain explicit.

Morphisms in `D_T` state what information is preserved, what cost coordinate is rescaled, and where comparison is partial or type-blocked. The substrate morphism `f_{rc} : N_rate → N_const` carries the worked `5π` rescaling from the chained Sobolev → geometric route; `f_{ca} : N_const → N_aae` is not a finite-rescaling morphism but the type-gap witness. Algorithm-side morphisms distinguish bounded additive, unbounded multiplicative, rational-equivalence, and restricted unitary-entropy coordinates rather than identifying them.

### §6.3.1. T4b.1 — existence of `Z`

The diagram `D_T` has a currency-universal measurable envelope `(Z, ℱ, ν)` with structure maps to every node. Concretely, `Z` is the product/equalizer envelope of the node spaces, with compatibility imposed only along admissible finite-rescaling morphisms. The σ-algebra `ℱ` is generated by the structure maps. The measure `ν` is a proof-carrier measure sufficient for measurability of the registered coordinates; no probability interpretation is used unless a later register supplies one.

Partial morphisms and type gaps are represented by absent or non-finite comparison paths. The construction therefore does not force a finite conversion where the source facts only give non-transfer.

### §6.3.2. T4b.2 — measurable currency encoding

The algorithm-side currencies `(μ, α)` and the substrate-side iso registers have measurable coordinates on `Z`. The §5 scalar substrate observables `f₁ = φ(n)/2`, `f₂ = L_n`, and `f₃ = Δ_n` lift measurably to `Z` at the substrate nodes where they are defined.

This clause does not say that `f₁`, `f₂`, and `f₃` factor through the scalar `δ`. Theorem K says the opposite kind of thing about Farey-side recoding: those observables are not recoverable from `F`. What T4b.2 supplies is a place where the observables and their loss can be spoken about in the same measurable apparatus.

### §6.3.3. T4b.3 — `δ` coordinate and normalization

For each node `i` with a cost observable `κ_i`, and for each admissible finite-rescaling path `i → j` with rescaling factor `r_{ij}^{(κ)}`, define the path defect

`d_{ij}((x_i)_i) = |κ_j(x_j) - r_{ij}^{(κ)} · κ_i(x_i)|`.

The `δ` coordinate is the max, or the finite-method supremum, of these path defects over the comparison family available to the method. Paths through type gaps are not included as finite comparisons; they are obstructions to forming such a path. When a single scalar `δ : Z → ℝ_{≥0}` is named, it is after choosing the operational cost norm of §6.5; before that choice, the same construction is read currency-by-currency as a `δ`-tuple.

### §6.3.4. T4b.4 — iso-register detection

The iso-register structure of §5.2 contributes a positive `δ` floor. At `n`-gon `Z`-points, the finite comparison `f_{rc} : N_rate → N_const` carries `r_{rc}^{(κ)} = 5π`. In the normalization where the direct rate-side and constant-side polygon readings are both expressed in `Δ_n` units, the worked instance contributes

`d_{rc} = (5π - 1) · Δ_n > 0`.

Changing normalization changes the displayed scalar but not the positive proportional floor. The almost-every register remains separate: the `f_{ca}` type-gap is not a large finite constant but the non-availability of a finite-rescaling path.

### §6.3.5. T4b.5 — algorithm-side currency faithfulness

Algorithm-side non-transfer is measurable in `Z` and registers as positive `δ` obstruction. Morgenstern's determinant potential binds bounded-coefficient additive cost; it does not transfer to the normalized FFT, whose determinant has modulus `1`, where Ailon's entropy potential is forced instead. Winograd and AFW supply unbounded rational-equivalence multiplicative ledgers; those ledgers do not transfer to bounded additive cost without crossing the coefficient-regime boundary.

Thus "same scale" is not "same currency." The Morgenstern↔Ailon comparison and the Winograd/AFW rational-equivalence ledgers mark unavailable, partial, or positive-cost morphisms in `D_T`, and T4b.3 reads those failures as nonzero `δ` in the chosen operational norm.

### §6.3.6. T4b.6 — closure-class measurability

FFT-style method membership is measurable against `(Z, ℱ, ν, δ)`. The description space is the space of uniformly described finite strategy families generated by the native operations of §4.2.2, with adaptive choices from problem data allowed only under the §4.2.1 regularity guard. Finite composition and guarded adaptive choice preserve measurability of the associated `Z`-coordinates.

The four escape channels of §4.6 are therefore visible to the T4b package: Farey recoding, cross-register iso conversion, cross-currency mult/add trading, and size-dependent tables/advice. Tables, oracle constants, advice strings, and hidden state remain outside the class unless their construction and storage are charged at the same granularity.

The universality of `Z` supplies the cross-currency reconciliation the lower-bound apparatus does not perform internally; T4b.2-T4b.6 state the separate faithfulness conditions needed for the contradiction in §6.6.

## §6.4. Substrate-side facts as faithfulness witnesses

Theorem K (§5.6) supplies the T4b.2 witness: an apparatus restricted to F-side coordinates cannot recover `f₁`, `f₂`, or `f₃`. Thus Farey recoding can be measured inside `Z`, but the lost scalar observables are not reconstructed from Farey data.

The iso-register facts of §5.2 supply T4b.4. The `5π` rescaling of `f_{rc}` reads on `δ` at `n`-gon `Z`-points as a positive floor, with `(5π - 1) · Δ_n` in the normalization of §6.3.4. The type-gap to almost-every remains a non-finite comparison, not an additional finite constant.

The algorithm-side non-transfer of §3.6.2 supplies T4b.5. Morgenstern↔Ailon non-transfer supplies the determinant/entropy obstruction, while Winograd and AFW supply the rational-equivalence multiplicative cells that do not identify with bounded additive cost.

The admissibility envelope of §5.5 and the regularity guard of §4.2.1 supply T4b.6. Size-dependent tables, advice, oracle constants, and hidden state are outside the class unless paid at the same granularity, with per-sample cost `≥ c · p` from effective Hermite–Lindemann at `n = 1` (§6.5).

## §6.5. Inputs T4b consumes

The cost-algebra apparatus has three inputs.

First, the operational cost-norm is cocycle compressibility: `δ` is the failure-to-agree of cocycle-product factors across butterfly refinements and primitive modes, measured pointwise.

Second, amortization at the boundary reduces to effective Hermite–Lindemann at `n = 1` via the L-W envelope route. Per-instance specialization, table precomputation, and asymptotic averaging cannot lower the per-instance floor without defeating that input.

The needed cost form is: with `ε(m) = log₂(1 + m) − m` on machine-dyadic `m = k/2^p` at variable precision `p`, any scheme `S` producing `ε(m)` to precision `2^{-p}` has total cost `cost_total(S, m, p) ≥ c · p` in the uniform-charge total-cost model.

Third, character reflection with phase-lift conservativity carries the per-sample obstruction on `ε(m)` to a closure-class statement on `δ`. This transport uses the variable-precision cost model and the effective H-L `n = 1` cost form above.

Figure: [figures/delta_phase_plot.png](figures/delta_phase_plot.png) — the closure-class picture in algebraic-phase space (amortization rate, asymptotic floor), with the native mult/add closure region separated from the `floor = 0` region by the working floor `δ_min`.

## §6.6. Conditional impossibility

Suppose `M` is an FFT-style method proving a lower bound on `P` strictly improving past `T(P)`. By §6.2, this descent implies `δ → 0` at the bounded/unbounded coefficient boundary. By T4b.0-T4b.3, the relevant currencies are represented in `(Z, ℱ, ν)` and the attempted descent has a `δ` reading in the chosen operational norm. By T4b.6, closure-class membership and the escape-channel classification are measurable in the same apparatus.

The T4b package routes every FFT-style escape through one of the obstructions in §6.4. Farey recoding loses `f₁`, `f₂`, and `f₃` because they are not recoverable on `F` (T4b.2 plus Theorem K); cross-register iso conversion retains the `5π` overhead and the type-gap (T4b.4); cross-currency mult/add trading retains Morgenstern↔Ailon and bounded/unbounded non-transfer (T4b.5); tables and advice leave the class unless charged at the same granularity (T4b.6 plus §6.5). Each case contradicts `δ → 0`.

Finite compositions of the native operations in §4.2.2 stay inside those cases. Therefore, conditional on the effective Hermite–Lindemann `n = 1` cost form, the variable-precision canon re-read, and the rigorous type-gap at `f_{ca}`, no FFT-style strengthening past current thresholds is reachable on this substrate.

A method improving past `T(P)` would need a cross-currency or cross-regime transfer mechanism not generated by the canon's native operations. Such a method is outside the FFT-style class of §4.2.

# §7. The circle

The conversion lives on the circle: the cyclotomic substrate, the integer lattice indexing roots of unity, and the planar isoperimetric gap used on the substrate side. The five canon sources measure that circle structure in five cost coordinates — three lower bounds (Morgenstern, Winograd, Auslander–Feig–Winograd) and two cost-model anchors (Schönhage–Strassen, Ailon).

Figure [figures/native_f_closure_mismatch.png](figures/native_f_closure_mismatch.png) records the closure-depth contrast: flat affine closure against the unbounded `φ(n)/2` cyclotomic ladder.

Schönhage–Strassen's operational baseline and Ailon's restricted-model sensitivity are the cost-model side of that same structure.

| Source | Circle-side content |
|---|---|
| **Schönhage–Strassen 1971** | Schönhage–Strassen 1971 measures integer multiplication through the cyclotomic substrate. The construction works in `Z/F_n Z` for Fermat number `F_n = 2^{2^n} + 1`, where `2` is a primitive `2^{n+1}`-th root of unity — the circle's roots of unity made arithmetically cheap. Root multiplication reduces to cyclic shift; the recursive composability of the FFT decomposition is the cyclic group's structure showing up in the operational cost ledger. The `O(N log N log log N)` upper bound is what integer multiplication costs when counted through this cyclotomic lens — the circle's recursive symmetry together with the bit-counting overhead of finite-precision arithmetic. Integer multiplication, counted operationally on this substrate, takes the shape the substrate gives it; the cost-model makes the cheap shifts visible because the substrate makes them cheap. |
| **Ailon 2013** | Ailon 2013 measures the normalized Fourier transform through unitary entropy. The model is layered `2 × 2` unitary gates, each mixing two of `n` live coordinates — the circle's symmetry group acting infinitesimally on the data vector. The matrix-entropy potential `Φ(M) = −∑ \|M(p,q)\|² log_2 \|M(p,q)\|²` measures the information-theoretic spread of `M`'s amplitudes; `Φ(Id) = 0`, `Φ(F) = n log_2 n` for the normalized Fourier matrix, and one native gate raises `Φ` by at most `2`. The `(1/2) n log_2 n` lower bound is what the circle costs when the cost-model is unitary entropy. The normalized FFT is unitary by construction (`\|det\| = 1`); information spread is what unitary structure has to give, and the entropy potential registers it. Ailon witnesses, on the canon's own ground, that each cost-model picks up a different aspect of the circle's geometry — the cost-model and the potential are entangled with what the circle has to show. |

> **Table 2: The cost-model methodology on the circle.** The operational upper bound and the restricted-model lower bound expose different cost coordinates on the same cyclotomic substrate.

The lower-bound apparatus reads cost-of-`P` through heterogeneous measures: Morgenstern's `Ω(n log n)` bit-counting on bounded coefficients; Winograd's modular-product / CRT ledger `μ(T_P) = 2n − k` on bilinear-rational; AFW's multiplicative-complexity / cyclotomic-rational-equivalence ledger.

The Morgenstern↔Ailon pair (per Table 2 above, with Ailon's circle reading paired against Morgenstern's bounded-side determinant) is the most explicit currency-stratification demonstration: same problem class (FFT), same scale (`Ω(n log n)`), two restricted models with two forced potentials — determinant on the unnormalized side, entropy on the normalized side (since determinant has modulus 1 there).

The lower-bound currencies are plural because the circle's structure is multi-coordinate. T4b reconciles that plurality with Theorem K's substrate-side coarsening by placing the currencies in one limit object `Z`.

**Algebraic-side companion (NATIVE-F closure-mismatch).** The closure-mismatch *theorem target* at [memos/NATIVE-F-MINIMAL-DEFINITION.md](memos/NATIVE-F-MINIMAL-DEFINITION.md) §No-Go Theorem asserts that no closure-depth-preserving functor `F: C_log → C_circle` satisfying axioms A1–A4 exists between the log-side and circle-side closure systems.

Closure generators: `Aff` log-side (the affine class whose native-operation realization is `Aff⁺(ℝ)`); `{K_n}_{n ≥ 3}` circle-side, where `K_n = ℚ(cos(2π/n))` is the maximal real subfield of `ℚ(ζ_n)` (sometimes written `K_n^+`).

NATIVE-F is algebraic-side companion material. It records the integer-vs-continuum asymmetry through functors between small observable categories, while Theorem K records it through σ-algebra coarsening.

# §Conclusion

Figure [figures/counting_psi_stratification.png](figures/counting_psi_stratification.png) — the ψ(n)-stratified outside-out sweep-x-support over `n ∈ [3, 40]` — localizes the algebraic-depth discontinuity at `n = 7` (Bravais ψ = 2 backbone versus first cubic ψ = 6). The same anchor appears in [figures/native_f_closure_mismatch.png](figures/native_f_closure_mismatch.png); the operational-observable register and the algebraic closure-depth contrast record the same discontinuity in different cost coordinates.

The theorem is intensional in three coordinates: the FFT-style class fixed at §4.2, the operational cost-norm of §6.5, and the cocycle realization of `δ` from §1.7. The extensional lift asks whether the same impossibility holds for behaviorally equivalent algorithms, alternative operational norms, and other reasonable δ-algebras.

Those extension questions are Rice-flavored. The extensional class is in each case an index set whose membership question reduces to halting; deciding it would require an oracle for behavioral equivalence to a member of the relevant class.

Non-FFT methods raise the parallel question: whether a different syntactic class can cross the `n = 7` discontinuity. NATIVE-F is the algebraic-side place where such an alternate vector field is considered.

# References

## FFT canon

- **Schönhage, A., and Strassen, V., 1971** — operational uniform model with recursive FFT composability.
- **Morgenstern, J., 1973** — bounded-coefficient additive lower bound for Fourier computation.
- **Winograd, S., 1978** — modular-product theorem `μ(T_P) = 2n - k` and CRT factor ledger.
- **Auslander, L., Feig, E., and Winograd, S., 1984** — cyclotomic decomposition under rational equivalence.
- **Ailon, N., 2013** — normalized Fourier lower bound in a layered `2 × 2` unitary-gate model via matrix entropy.
- **Goldstine, H. H., 1977** — *A History of Numerical Analysis from the 16th Through the 19th Century*, §4.12-13; Gauss 1805 interpolation and the Pallas factorization example.

## Cost Framework

- **Coase, R. H., 1937** — "The Nature of the Firm," *Economica* New Series Vol. 4 No. 16, pp. 386-405.
- **Cook, S. A., and Reckhow, R. A., 1973** — RAM charging-granularity vocabulary.
- **Slot, C., and van Emde Boas, P., 1984; van Emde Boas, P., 1988/1990** — Invariance Thesis / First Machine Class charging framework.

## Algebraic And Substrate Sources

- **Heideman, M. T., Johnson, D. H., and Burrus, C. S., 1985, §5** — eigenspace decomposition under `σ_{-1}`.
- **Gauss, C. F., 1801** — *Disquisitiones Arithmeticae*; cyclotomic ladder and constructible polygon sufficiency.
- **Wantzel, P.-L., 1837** — necessity in the Gauss-Wantzel constructibility criterion.
- **Niven, I., 1956** — rational-cosine theorem.
- **Bamberg, J., Cairns, G., and Kilminster, D., 2003** — crystallographic restriction `ψ` function.

## Measure And Diophantine Sources

- **Avila, A., and Jitomirskaya, S., 2009** — "The Ten Martini Problem"; exponential-rate Diophantine parameter `β(α)`.
- **Berthé, V., and Reutenauer, C.** — three-distance theorem via three-interval exchanges.
- **Ferenczi, S., and Zamboni, L.** — Lyndon-word characterization in the three-distance context.
- **Lefèvre, V., Muller, J.-M., and Tisserand, A., 1998** — compressed-orbit pseudocode for table-maker's-dilemma filtering.
- **Marklof, J., and Strömbergsson, A.** — lattice formulation of the three-distance theorem on `Γ\SL(2, ℝ)`.
- **Osserman, R., 1979** — Bonnesen-strengthening inequality.
- **Fuglede, B., 1989, Theorem 1.2** — stability bound for nearly spherical domains.
- **Beck, J., 1994** — Fourier / second-moment / Borel-Cantelli discrepancy machinery.
- **Bonnesen, T., 1921; 1924** — isoperimetric strengthening forms.
- **Hurwitz, A., 1902** — Fourier-isoperimetric identity.
- **Lindemann, F., 1882** — L-W boundary; transcendence of `π`.
- **Roth, K. F., 1954** — discrepancy lower bound.
- **Roth, K. F., 1955** — rational approximations to algebraic numbers.
- **Fortnow, L., 2000** — Kolmogorov complexity tools.
- **Aitchison, J., 1959** — density-side Fourier / Poisson expansion.
- **Kuipers, L., and Niederreiter, H., 1974** — Erdős-Turán / Erdős-Turán-Koksma discrepancy sums.

## Proof-Template Sources

- **Bowen, L. P., 2002** — *Density in Hyperbolic Spaces*, Ph.D. dissertation, University of Texas at Austin.
- **Gosper, R. W., 1972** — continued-fraction arithmetic machine.
