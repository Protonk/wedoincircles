# §Intro

## §Intro.1. The claim
We prove an impossibility theorem: FFT-style methods, defined by closure under the canon's native operations under a uniform-charge cost model, cannot improve past their existing lower-bound thresholds on cyclotomic-DFT and adjacent compute-cost problems. 

The thresholds in question are heterogeneous — Morgenstern's `Ω(n log n)` bounded-coefficient additive bound, Winograd's modular-product `μ(T_P) = 2n − k`, AFW's multiplicative-complexity threshold under rational equivalence. 

The impossibility lands at each one in its own currency.

## §Intro.2. The frame
The cost framework imports Coase 1937's transaction-cost vocabulary, generalized from economic-coordination friction to measure-theoretic non-nesting overhead. 

Each conversion across the bounded/unbounded coefficient boundary carries an irreducible cost `δ`; the thresholds are *located by* — not held above — that friction. 

§3.6.2 demonstrates currency-stratification on both sides: 

  Algorithm-side (canon source non-transfer, witnessed constructively by Morgenstern↔Ailon's forced shift from determinant to entropy potential at the normalized FFT) 

  Substrate-side (the planar isoperimetric gap's three non-nesting measure-theoretic readings, with `5π` worked overhead between rate and constant). 

Lower bounds are not numbers; they are measurements made in particular coordinate systems.

## §Intro.3. What's earned, what's committed, what's owed
The proof carries three objects at three evidentiary standards. 

  *Earned*: Theorem K, a σ-algebra coarsening result on the integer-indexed lattice, proved here in companion form — the local, checkable fact certifying that `f₁ = φ(n)/2`, `f₂ = L_n`, `f₃ = Δ_n` are unrecoverable from Farey coordinates; T1's off-backbone empty contour is proved alongside. 
  
  *Committed*: a uniform-charge cost model with regularity guard, an operational cost-norm on the cocycle product, and the `δ`-typing extension to substrate-side iso registers. 
  
  *Owed*: T4b — the currency-universal boundary object whose three faithfulness clauses tie substrate-side facts to algorithm-side cost; the endpoint commitment that ties threshold improvement to `δ → 0`; the floor extension that bridges at-threshold to past-threshold. 

The algebraic-side closure-mismatch reading at §7 (NATIVE-F) is a sibling structural reading on the integer-vs-continuum asymmetry, not load-bearing for the impossibility. 

Frame figure: [figures/native_f_closure_mismatch.png](figures/native_f_closure_mismatch.png) — flat affine closure (left) against the unbounded `φ(n)/2` cyclotomic ladder (right), the closure-depth contrast in one panel; re-referenced at §7.

# §1. Cost, conversion, and defect

## §1.1. The accounting stack

§1 sets the four nested objects this paper measures with: cost model, cost currencies, conversion strategies, and transaction cost `δ`. The cost model governs what is charged; the currencies say what is being counted; the conversion is the adaptive family of strategies trading one currency for another; `δ` is the cost attached to that conversion. `δ` is not a synonym for the mult/add conversion. It is a typed object that ranges across both algorithm-side currencies (`(μ, α)`) and substrate-side ones (§5.2's iso/-register triple); §1.6 names how it ranges and what its algebra owes.

## §1.2. Cost model

We work in a uniform-charge / logarithmic-measure cost model in the Cook–Reckhow 1973 / Slot–van Emde Boas 1984 sense. Bit growth is charged. Advice strings, oracle constants, and table-per-size shortcuts are handled by the regularity guard at §4.2.1 — admissible only when their construction and storage are charged inside the method at the same granularity. "Uniform" in this paper does not mean Cook–Reckhow constant `l(n) = 1` or van Emde Boas uniform measure; it means logarithmic-measure charging in both senses, and the methodological commitment is set here. Compatibility under variable precision — re-reading Morgenstern, Winograd, AFW, and Ailon under this guard — is the substantive remaining work that lands at §6.5.

## §1.3. Cost currencies

The two algorithm-side cost currencies are multiplicative cost `μ` and additive cost `α`. They are currencies inside the §1.2 cost model — measures of what is being counted — not conversion strategies between them. The conversion is named at §1.5; the cost attached to it is named at §1.6.

### §1.3.1. Multiplicative cost

The cost-bearing primitives are multiplications; the complexity measure `μ` counts them under bilinear / rational-equivalence accounting. Schönhage–Strassen 1971, Winograd 1978, and Auslander–Feig–Winograd 1984 each give `μ` structure on cyclotomic-DFT and adjacent computations; the full presentation is §3.

### §1.3.2. Additive cost

The cost-bearing primitives are additions; the complexity measure `α` counts them, sensitive to the coefficient regime. Morgenstern 1973's `Ω(n log n)` bounded-coefficient additive lower bound is the structure-bearing result, presented at §3.3. Ailon 2013 is the adjacent normalized-FFT comparison and the clearest in-canon witness for currency-stratification: in a layered `2 × 2` unitary-gate model, matrix entropy gives the same `Ω(n log n)` scale without determinant growth — Morgenstern's determinant method does not reach the normalized FFT (whose determinant has modulus 1), and entropy is needed in its place. §3.6.2 develops this as the content claim that currency-stratification is forced.

## §1.4. Coefficient regimes

Bounded versus unbounded coefficients. The regime is a parameter of every cost measure on either side, and many bounds — Morgenstern's notably — depend on which regime is in force. The bounded/unbounded coefficient boundary is the measure-theoretic state space where `δ` is evaluated at §6.2 / §6.3.

## §1.5. Conversion as adaptive strategy family

The mult/add conversion is the family of strategies FFT-style algorithms use to trade multiplicative cost for additive cost or vice versa. Methods select a strategy adaptively from problem data: Gauss 1805's `4 × 3` versus `3 × 4` factorization of the Pallas computation is the pre-1882 worked example (Goldstine 1977, §4.12–13). The conversion is an adaptive strategy family closed under composition, not a single partial function.

Adaptivity is the move that looks like it might evade `δ`, and does not. Switching currencies is precisely what `δ` measures, so adaptive currency-choice relocates where `δ` shows up rather than zeroing it. The supporting content is at §3.6.2: currency-stratification is forced, with Morgenstern↔Ailon non-transfer as the in-canon witness.

## §1.6. Transaction cost `δ`

The conversion has a transaction cost. Following Coase 1937, we keep two questions separate: whether the cost is non-zero, and what its algebra is. *Existence* (`δ > 0`) is one claim; *algebra* is the other. Coase's distinction between the existence of friction (p. 390: "there is a cost of using the price mechanism") and its algebra (p. 395 marginal condition; p. 396 the firm-size determination as costs of organising rise with transactions organised) is the precedent the program inherits, and it is the explicit organizing move of this section: existence is what §6.2's endpoint commitment carries; algebra is the open work named at §6.5; the *reduce-yes-eliminate-no* facet returns at §6.6.

The algebra of `δ` runs through six headings, plus a separate at-threshold/past-threshold bridge heading the framework has to answer for. The six algebra headings: *Additivity* under composition has its formal-character skeleton at the cocycle composition law of §6.5 — a partial-yes verdict, with the cross-term collapsing under §1.2's regularity guard. *Amortization* across repeated uses reduces (via the Lindemann–Weierstrass envelope) to effective Hermite–Lindemann at `n = 1`, which is the substrate-side input owed at §6.5; closing it closes the substantive open part of the algebra. *Asymptotics* in size and precision couple to the same reduction. *Representation-dependence* under change of coordinates is closed in spirit under §1.5's adaptive-family reading. *Bypass-resistance* under specialist intermediation is closed under the §1.2 regularity guard. *Multi-route effects* are closed methodologically. The bridge heading — *floor extension from at-threshold to past-threshold* — is not algebra of `δ` per se but the structural bridge between the existence claim *at* `T(P)` and the implication claim *past* `T(P)`; §6.2 names it as the load-bearing step between those two halves.

The framework hosts more than the §1.3 `(μ, α)` currency pair. `δ` is the transaction cost between *any two non-nesting measure-theoretic readings of one quantity*. The algorithm-side instance is the bounded/unbounded coefficient conversion. The substrate-side instance is §5.2's iso/-register triple — three non-nesting measure-theoretic readings of the planar isoperimetric gap (rate, constant, almost-every), with `5π ≈ 15.7×` worked-instance overhead between rate and constant on the chained Sobolev → geometric route, and a categorial type-gap to almost-every (`iso/THREE-REGISTER-SYNTHESIS.md` Claim 1).

## §1.7. Candidate cocycle realization

The paper carries a candidate concrete realization of `δ` from §6 onward: `δ` is the cost of `{Δ_k}` cocycle compression — the failure-to-agree of cocycle-product factors across butterfly refinements and primitive modes, measured pointwise. The formal composition law is the cocycle composition law of §6.5; the faithfulness condition the candidate must satisfy is T4b's keystone proposition at §6.3. This is candidate machinery, declared here to flag the form §6 will commit to; the operational cost-norm commitment is made at §6.5.

## §1.8. Threshold interface `T(P)`

For a problem `P`, the threshold `T(P)` is the lower-bound frontier supplied by the three sources — Morgenstern's `Ω(n log n)` additive on bounded coefficients, AFW's multiplicative-complexity threshold under rational equivalence, Winograd's modular-product `μ(T_P) = 2n − k`, each in its own currency. Descent past `T(P)` means trading a higher cost-bearing bound for a lower one by reorganizing the computation. The endpoint commitment of §6.2 ties descent to a specific cost-coordinate value: descent past `T(P)` *implies* `δ → 0` at the bounded/unbounded coefficient boundary, which in §1.7's candidate cocycle coordinate reads as competitive `{Δ_k}` compression. The implication direction is what §6.2 has to earn; a biconditional is not claimed.

Figure: [figures/cost_conversion_schematic.png](figures/cost_conversion_schematic.png) — the cost-pair `(μ, α)` plane with the three thresholds (Morgenstern, AFW, Winograd) marked, the counterfactual `δ = 0` frontier, the hatched `δ`-gap between them, and the endpoint implication at the bounded/unbounded coefficient boundary. Endpoint-side picture only; the keystone proposition lives at §6.3, the substrate-side faithfulness witnesses at §6.4, the inputs T4b consumes at §6.5, and the algebraic-side companion at §7. Companion at [paper/code/COST-CONVERSION-SCHEMATIC.md](paper/code/COST-CONVERSION-SCHEMATIC.md).

# §2. The conversion

The FFT is the conversion of multiplication and addition on the circle. This paper proves where that conversion fails.

**The conversion.** The mult/add conversion is the family of strategies FFT-style methods use to trade multiplicative cost for additive cost on the circle — cyclotomic substrate, roots of unity, the integer lattice `L = {(k, n) : 1 ≤ k < n, n ≥ 3}` the substrate sits on.

It is adaptive: methods select strategies from problem data, and the class is closed under composition (§1.5, §4.2.3).

The five sources are five windows on the conversion: Schönhage–Strassen builds it operationally; Morgenstern measures it from the additive side under bounded coefficients; Winograd factors it through the CRT modular product; Auslander–Feig–Winograd decomposes it through cyclotomic semisimple structure; Ailon measures it through matrix entropy on a restricted unitary-gate model.

**Where it fails.** At the bounded/unbounded coefficient boundary.

The failure is two halves of one boundary fact: existence (`δ > 0` at `T(P)`) and implication (`δ → 0` past `T(P)`), bridged at §6.2 by §1.6's floor-extension step — the load-bearing move that collapses the halves into two readings of one fact.

The heterogeneity across the three lower bounds is what failure looks like algorithm-side: each source picks up a piece of cost-coordinate space and none transfers across the boundary cleanly (§3.6.2).

Morgenstern's determinant potential cannot reach the normalized FFT, and matrix entropy is forced in its place at Ailon 2013 (§3.2).

The substrate side carries its own failure shape: §5.2's three iso registers (rate, constant, almost-every) are non-nesting measure-theoretic readings of the planar isoperimetric gap, with `5π` worked overhead between rate and constant and a categorial type-gap to almost-every.

The §4.6 chase makes the failure operational: a Farey-regularized recursive FFT tries four routes through the conversion that don't pay `δ` — Farey recoding, cross-register iso conversion, mult-add trading, precomputed tables — and each route slams into a substrate-side door.

**Why we can see the failure.** Theorem K is the local checkable fact.

The reduction map `R: L → F` from the integer-indexed lattice to the Farey set induces σ-algebra coarsening on `L`; the substrate observables `f₁ = φ(n)/2`, `f₂ = L_n`, `f₃ = Δ_n` do not factor through `R` (proved in companion form at §5.6).

K certifies that the substrate has structure the conversion has to respect; the impossibility theorem (§6.6) composes K with the cost-algebra apparatus to say no FFT-style method can drive `δ → 0` past `T(P)`.

The conversion of multiplication and addition on the circle cannot be made friction-free by any FFT-style passage.

The heterogeneity is one structural fact across the three cost-coordinate cells.

# §3. Cards on the table

## §3.1. The canon together

Five sources from 1971 through 2013 carry the FFT lower-bound apparatus we engage with, and they sit in two groups by methodological role rather than five-on-one chronology. Three of them are the lower bounds the program reads as `T(P)`: Morgenstern 1973's `Ω(n log n)` additive floor under bounded coefficients, Winograd 1978's modular-product `μ(T_P) = 2n − k` on polynomial-quotient rings, and Auslander–Feig–Winograd 1984's factor-by-factor multiplicative complexity on cyclotomic-decomposed group DFTs. The other two are cost-model methodology — they establish how the field counts, not what the field's lower bounds are. Schönhage–Strassen 1971 sets the baseline: the operational uniform-charge bit/gate model with recursive composability the lower-bound apparatus counts inside. Ailon 2013 sets the sensitivity: when the cost-model varies (the normalized FFT, restricted unitary-gate layered model), the determinant potential unbinds and matrix entropy is forced in its place — an in-canon witness that currency-stratification is not a coverage gap but a structural feature of how the cost-model interacts with the potential. The pairing is what gives §3.6.2 its content claim.

§3.2 presents the cost-model methodology together (Schönhage–Strassen and Ailon, with their methodological roles bound). §3.3, §3.4, §3.5 present the three lower bounds, one each. §3.6 reads the three together: §3.6.1 translates each lower bound through §1's stack; §3.6.2 lands the structural reading that the three-fold currency-stratification is forced.

The program's content reads what these five sources together can and cannot reach — three lower-bound results admitted inside their stated trust boundaries (set side by side in Table 1 below), plus the cost-model frame within which those results live.

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

> **Table 1: The three FFT lower bounds.** Each row presents one bound's setting, result and mechanism, and the regions where the mechanism unbinds. Reading down column 4 makes the cross-row pattern of forced silences visible — the heterogeneity §3.6.2 develops as content.

## §3.2. The cost-model methodology: Schönhage–Strassen 1971 and Ailon 2013

Two papers, four decades apart, establish how the FFT lower-bound apparatus counts. Schönhage–Strassen 1971 sets the operational uniform model: bit and gate primitives charged at logarithmic-measure granularity, recursive composability, root-of-unity arithmetic in the ring `Z/F_n Z` (where `F_n = 2^{2^n} + 1` is a Fermat number and `2` is a primitive `2^{n+1}`-th root of unity, so root multiplication reduces to a cyclic shift). The headline result is constructive — integer multiplication in `O(N log N log log N)` bit operations via recursive FFT decomposition — and it is upper-bound only; Schönhage–Strassen is not a lower-bound theorem. Its program role is the operational template: the cost-model the lower-bound apparatus counts inside, the model-and-composability anchor §1.2's uniform-charge discipline names as its FFT-side counterpart to Cook–Reckhow / Slot–van Emde Boas RAM-charging vocabulary.

Ailon 2013 supplies the sensitivity. In a restricted layered model — `n` live coordinates, each gate a `2 × 2` unitary mixing of two coordinates — Ailon proves that any circuit computing the normalized Fourier transform requires at least `(1/2) n log_2 n` gates. The mechanism is the matrix-entropy potential `Φ(M) = −∑_{p,q} |M(p,q)|² log_2 |M(p,q)|²`: `Φ(Id) = 0`, `Φ(F) = n log_2 n` for the normalized Fourier matrix, and one native `2 × 2` unitary gate raises `Φ` by at most 2. The result reaches the same `Ω(n log n)` scale as Morgenstern 1973's bounded-coefficient determinant-potential bound, but in a different restricted model with a different cost currency — and the difference is the program's read on Ailon. Morgenstern's determinant potential measures volume growth; the normalized FFT has determinant of modulus 1; the determinant potential cannot see the normalized FFT, and matrix entropy is the replacement potential the cost-model change forces. Two lower-bound currencies, both reaching `Ω(n log n)`, forced into different shapes by what each potential can see — currency-segregation as a structural feature of the potential method, not a coverage gap or absent better proof (per [fft/AILON-2013-UNITARY-FFT-LOWER-BOUND-BRIEF.md](fft/AILON-2013-UNITARY-FFT-LOWER-BOUND-BRIEF.md) §3).

Together the pair bound the cost-model frame from both sides. Schönhage–Strassen is the baseline: this is how the FFT literature counts. Ailon is the sensitivity: change the count, and the potential changes too. Each one alone is incomplete; together they are the methodological grounding the three lower bounds of §3.3–§3.5 inhabit, and the in-canon witness §3.6.2 reads as the forcing of currency-stratification. Ailon's own survey foregrounds the posture the program owes at §6.6: nontrivial broad linear-circuit Fourier lower bounds remain open, and known successful results require strong model restrictions. The Morgenstern↔Ailon pair is the field-internal demonstration that the §3.6.2 non-transfer is forced rather than incidental.

## §3.3. Morgenstern 1973

Morgenstern's bounded-coefficient additive lower bound: any linear circuit computing the `n`-point DFT under coefficients bounded by a constant `c` requires `Ω(n log n)` additions. The mechanism is a determinant-potential argument — the DFT matrix has determinant of magnitude `n^{n/2}` (Vandermonde-style), and in the bounded-coefficient model each gate grows the running determinant by at most a constant factor, so reaching the full determinant requires `Ω(n log n)` gates. The bounded-coefficient regime is essential: without it the determinant potential does not bind, as the §3.2 normalized FFT case witnesses (modulus 1, matrix-entropy forced in its place). The result fills the additive `α` slot on the bounded side of §1.4.

## §3.4. Winograd 1978

Winograd's modular-product theorem: for a degree-`n` polynomial `T_P` with `k` irreducible factors over the base field, the bilinear multiplicative complexity of multiplication mod `T_P` is exactly `μ(T_P) = 2n − k`. The mechanism is CRT decomposition — polynomial multiplication mod `T_P` reduces to factor-by-factor multiplication in the residue rings, and the lower bound follows by counting essential bilinear multiplications inside each factor. The result fills the multiplicative `μ` slot on the unbounded rational-equivalence side of §1.4; the CRT-cyclotomic factor ledger is what §3.5's Auslander–Feig–Winograd extends from polynomial-quotient rings to the full cyclotomic-DFT class.

## §3.5. Auslander–Feig–Winograd 1984

Auslander–Feig–Winograd's semisimple cyclotomic decomposition of finite-abelian DFTs: the group ring `ℚ[G]` of a finite abelian group `G` decomposes by CRT into a product of cyclotomic fields `ℚ(ζ_d)` (one per divisor `d` of `|G|`), and the DFT factors accordingly. Multiplicative complexity is computed factor-by-factor under rational equivalence — bilinear and linear-rational substitutions are free, only essential nonrational multiplications count. The result extends Winograd's modular-product accounting (§3.4) from polynomial-quotient rings to the full semisimple algebra structure of finite-abelian-group DFTs, filling the multiplicative `μ` slot on the unbounded cyclotomic side of §1.4.

## §3.6. Common cost / conversion structure

What do the three lower bounds of §3.3–§3.5 share in §1's cost / conversion framework?

§3.6.1 re-reads them through five coordinates: cost model and guard, currency, regime, conversion role, and `δ` status. §3.6.2 reads the deeper structural fact: the heterogeneity across the three is non-transfer across regime and currency, and the §3.2 cost-model methodology supplies the in-canon witness that this non-transfer is structural.

## §3.6.1. Translation into the §1 stack

We re-read the three lower bounds of §3.3–§3.5 through §1's five coordinates: cost model and guard, currency, regime, conversion role, and `δ` status. The point is to keep theorem content separate from program-side typing.

Morgenstern 1973 lives in a bounded-coefficient linear-composition setting; its currency is additive `α`; its regime sits on the bounded side of §1.4 (the determinant potential binds only there); its conversion role is to supply the additive floor against which conversion is measured; its `δ` status is no transfer to unbounded coefficients. Winograd 1978 lives in bilinear / rational-equivalence accounting; currency is multiplicative `μ`; regime is unbounded rational-equivalence; conversion role is the CRT modular-product ledger; `δ` status is no transfer to bounded coefficients or to additive cost. Auslander–Feig–Winograd 1984 sits at rational-equivalence cyclotomic decomposition; currency is multiplicative `μ`; regime is unbounded cyclotomic; conversion role is factor-by-factor multiplicative accounting via CRT decomposition; `δ` status is no transfer to bounded coefficients or to additive cost.

The §1.2 uniform-charge / logarithmic-measure guard is a program-side requirement placed over this re-read; where a source does not itself formulate variable-precision charging, the variable-precision re-read is the substantive open work landing at §6.5. The cost-model methodology of §3.2 (Schönhage–Strassen for the operational baseline; Ailon for the cost-model-forces-potential sensitivity) is the program-side anchor under which this re-read operates — it is what makes the three lower bounds' regime and currency placements measurable in the same framework.

## §3.6.2. What's structurally shared

The shared structure is the stack: charged operations, cost currencies, a coefficient-regime boundary, strategy-family composition, and an unpaid transaction cost at the boundary. Two of the three lower bounds sit on the multiplicative side (Winograd modular product, Auslander–Feig–Winograd cyclotomic); Morgenstern is the additive-side floor, and the only one whose lower bound requires bounded coefficients. None of the three transfers a bound across another's coefficient regime or cost currency. Every such transfer is exactly what §1.6 calls `δ`, and §6 must prove that native FFT-style methods cannot make that payment vanish.

**Four structural faces of the non-transfer.** (Labeled (i)–(iv) here to keep them distinct from §6.6's (a)–(d) composition.)

(i) `T(P)` is *structurally plural*: a fragmented frontier with currency-specific entries — Auslander–Feig–Winograd multiplicative on unbounded, Morgenstern's `Ω(n log n)` additive on bounded, Winograd's modular-product `μ(T_P) = 2n − k`. "Improving past `T(P)`" means improving past any one entry in its own currency.

(ii) The algorithm-side argument is correspondingly *currency-stratified*: the endpoint commitment, the T4b boundary object, and the candidate transport must each land in every cell of `T(P)`. `δ` is conceptually single but realizes in a chosen cost-norm; the three-cell currency-plurality forces a `δ`-tuple.

(iii) Theorem K (§5.6) is *currency-blind*: a σ-algebra fact on the integer-indexed lattice, indifferent to cost-counting and equally applicable across both algorithm-side currencies (§1.3) and substrate-side iso/ registers (§5.2).

(iv) The substrate side carries its own *currency-stratification at §5.2*: the three iso/ registers (rate, constant, almost-every) are non-nesting measure-theoretic readings of the planar isoperimetric gap, with `5π ≈ 15.7×` worked-instance overhead between rate and constant ([iso/THREE-REGISTER-SYNTHESIS.md](iso/THREE-REGISTER-SYNTHESIS.md) Claim 1) and a categorial type-gap to almost-every. They are currencies in §1.6's transaction-cost sense; non-nesting plus worked overhead *is* a substrate-side `δ > 0` instance by §1.6's definition, with Theorem K's coarsening sitting on top of the register-stratification.

The substrate/algorithm asymmetry is therefore not "substrate uniform vs algorithm plural" but "currency-pluralities on both sides forcing matching commitments on `δ`, with Theorem K supplying the register-blind layer that ties them together."

**The non-transfer is forced, not incidental.** §3.2's cost-model methodology supplies the in-canon witness: when Morgenstern's determinant potential is asked to reach the normalized FFT (whose determinant has modulus 1), it cannot, and Ailon's matrix-entropy potential is forced in its place. Two lower-bound currencies, both reaching `Ω(n log n)`, forced into different shapes by what each potential can see — currency-segregation as a structural feature of the potential method, not a coverage gap. Lower bounds are not numbers; they are measurements made in particular coordinate systems, and translation across the three is not free. §6.6's smarter-FFT rebuttal lands as content on the strength of this.

NATIVE-F's closure-mismatch reading at §7 is a sibling structural rhyme on the integer-vs-continuum asymmetry; parallel to this account, not load-bearing for it.

# §4. Main theorem

## §4.1. Frame
Preview in plain language: an impossibility theorem asserting that FFT-style methods cannot prove lower bounds *improving past* the existing thresholds for cyclotomic-DFT and adjacent compute-cost problems.

The formal version is at §4.5.

## §4.2. FFT-style methods
The hypothesis class.

It is intentionally narrower than "all lower-bound methods": only methods built from the FFT canon's native operations, under the cost model and guard of §1.2, are in scope.

## §4.2.1. Model and regularity guard
An in-scope method is charged in the uniform-charge / logarithmic-measure sense of §1.2.

Operation cost, stored precision, coefficient size, precomputed tables, and size-dependent constants must be paid for at the same granularity.

Advice strings, oracle constants, table-per-size shortcuts, and growing hidden state are outside the class unless their construction and storage costs are explicitly charged inside the method.

## §4.2.2. Standard composability of the canon
The native operations are those each source contributes to the FFT-style toolkit, with each entry traced to its §3 lineage: recursive FFT decomposition (Schönhage–Strassen 1971, §3.2), CRT / tensor factorization (Winograd 1978, §3.4; AFW 1984, §3.5), linear-composition closure (all four sources; cf. §3.6.1), cyclotomic factor accounting (AFW 1984, §3.5), and coefficient-regime bookkeeping (Morgenstern 1973, §3.3).

The list is descriptive of canon, not stipulative — each entry's lineage is on the page. The class is closed under finite composition of these operations when the §4.2.1 guard is respected.

## §4.2.3. The class defined
Formally: an FFT-style method is a uniformly described strategy family whose per-size methods are finite compositions of the native operations of §4.2.2, possibly with adaptive choices, charged under §4.2.1, and closed under composition (per §1.5's reading; see `fft/FFT-SEARCH-PLAN.md` for the Gauss 1805 anchor and the deeper search-theoretic framing).

The class is fixed by §4.2.2's descriptive operation list, not by what §6.6 happens to close — changing §6.6's case structure does not retroactively narrow §4.2. Channel exhaustiveness (debt #11) is therefore a check *over §4.2.2*: do finite compositions of those operations stay inside §6.6's four-channel routing? The check sits in the ledger; the class definition does not move under it.

This is the formal object §4.5 quantifies over.

## §4.3. Cyclotomic-DFT and adjacent
The problem class.

Cyclotomic-DFT specifically — the discrete Fourier transform over cyclotomic fields.

"Adjacent" pinned down: compute-cost problems sharing §1's cost / conversion structure, differing in inputs but not in the cost / conversion framework the bounds inhabit.

## §4.4. Existing thresholds

`T(P)` is the lower-bound frontier on problem `P` the impossibility theorem of §4.5 is stated against. Three sources supply its entries, each at a distinct cost-coordinate cell in §1's framing — Morgenstern 1973 at bounded-coefficient additive cost (§3.3), Winograd 1978 at unbounded multiplicative cost on polynomial-quotient rings (§3.4), Auslander–Feig–Winograd 1984 at unbounded multiplicative cost on cyclotomic-decomposed group DFTs (§3.5).

These three define `T(P)`. The impossibility theorem of §4.5 applies to bounds at these three cells; FFT lower-bound results at coordinates outside §1's admitted framing — for example, Ailon 2013's `(1/2) n log_2 n` in a restricted layered unitary-gate model, presented at §3.2 as cost-model methodology — are outside the theorem's scope by construction.

The plurality of `T(P)` across these three distinct cost currencies demands the impossibility theorem close at each entry. Cross-currency reconciliation across the three is part of §6.3's currency-universal limit Z.

## §4.5. The theorem
Formal propositional statement.

For every FFT-style method `M` (§4.2) and every problem `P` (§4.3), `M` does not prove a lower bound on `P` improving past the existing threshold `T(P)` of §4.4.

Equivalently: no FFT-style strengthening past the current thresholds is reachable on this substrate.

## §4.6. The chase: a worked adversary

To stake the theorem before earning it, we run a specimen FFT-style method against `T(P)` and watch where it breaks.

Let `M_FR` be the *Farey-regularized recursive FFT*: at each butterfly stage, `M_FR` attempts to coarsen its cyclotomic index by passing `(k, n)` through the reduction map `R: (k, n) ↦ (k/g, n/g)` (with `g = gcd(k, n)`) to read on the Farey side, then composes the residual through every adaptive escape FFT-style closure permits.

The specimen is native — recursive decomposition, linear composition, cyclotomic factor accounting, and adaptive choice from problem data, all under §4.2.1's regularity guard — and naively tempting: Farey reduction is the most natural regularization move on cyclotomic indices, and gcd-equivalence-class amortization would let `M_FR` absorb residue if it worked.

**Headline attempt: mult-add trading.** `M_FR` tries to amortize a multiplicative-side residue through Morgenstern's bounded-coefficient additive ledger to escape the AFW cyclotomic-multiplicative threshold — the one-line route through the maze any reader will think of first.

The trade fails at the cost-algebra obstruction (§6.3, §6.4): §3.6.2's currency-stratification (Morgenstern↔Ailon non-transfer per §3.2; the determinant potential doesn't reach the normalized FFT, entropy is forced) makes the cross-currency conversion read on `δ`, and `δ` does not vanish at the bounded/unbounded coefficient boundary.

The substrate content of *why* the conversion costs are bounded below is earned in §5 (specifically §3.6.2 face (iv) plus §5.2's iso non-nesting on the substrate-side iso half).

**Three variants foreshadowed for §5 to dispatch.**

*Farey recoding* (the namesake attempt): `M_FR` passes `(k, n)` through `R` and tries to read its threshold position on the reduced fraction; broken by Theorem K at §5.6 — `f₁, f₂, f₃` do not factor through `R`.

*Cross-register iso conversion*: `M_FR` tries to trade a rate-form bound for a sharp-constant bound; broken by §5.2's non-nesting (`5π` worked overhead between rate and constant, categorial type-gap to almost-every).

*Precomputed tables / advice*: `M_FR` tries to absorb residue with size-dependent shortcuts; broken by §5.5's admissibility envelope plus §4.2.1's regularity guard, with per-sample cost `≥ c · p` from effective Hermite–Lindemann at `n = 1`.

Each variant is a different door, all opening onto the same room — `(Z, ℱ, ν, δ)` — and converging at §6.6 conditional on the keystone proposition (§6.3, debt #1) and on the channel-exhaustiveness commitment over §4.2.2's native operations (debt #11). Under those commitments the four-attempt span is what every FFT-style method's escape factors through.

The adversary is artificial.

Its failure does not commit the proof to a single currency (the algebra of `δ` extends across all three LB currencies and both substrate-side iso registers; debt #13), does not strip optionality from the floor-extension mechanism (debt #2(8)), and does not formalize channel-exhaustiveness (debt #11).

It is narrative scaffolding: a vehicle for the cost-algebra obstruction (§6.3) to be tested on a concrete escape attempt before being lifted to the full FFT-style class at §6.6.

## §4.7. Proof outline

The proof has three parts plus a load-bearing transport, per `paper/PROOF-CHAIN.md`.

The §4.6 chase is the dramatic version; this is the structural one.

**Substrate-side menagerie** (§5). The substrate the §4.6 chase navigates: rotation-orbit Diophantine kinematics under Haar measure (§5.1), non-nesting isoperimetric registers (§5.2), closed-form polygon arithmetic via Hurwitz Fourier expansion (§5.3), cyclotomic-ladder unboundedness against affine flatness (§5.4), the L-W admissibility envelope (§5.5), and Theorem K's σ-algebra coarsening on the integer-indexed lattice `L` (§5.6, *proved here in companion form*; proof at `measure/FOR-BREAKFAST.md` §K.0–§K.4).

The menagerie is the substrate content of the four doors §4.6 staked.

**T4b — the keystone proposition** (§6.3). The single sovereign claim of §6: a currency-universal boundary object `(Z, ℱ, ν, δ)` over the three LB currencies and substrate-side iso registers, with three faithfulness clauses — (i) §5 scalar substrate observables `f₁, f₂, f₃` factor through `δ`; (ii) iso-register currency structure encoded measurably so cross-register conversion costs read on `δ` alongside the algorithm-side `(μ, α)` cost; (iii) closure-class membership reads measurably against `(Z, ℱ, ν, δ)`.

Open and load-bearing (debt #1). Spec at `measure/THE-FIRST-BRIDGE.md`.

**Substrate-side facts as faithfulness witnesses** (§6.4). Theorem K certifies clause (i); §5.2 iso non-nesting plus §3.6.2 currency-stratification certify clause (ii); §5.5 admissibility envelope plus §4.2.1 regularity guard certify clause (iii).

Each substrate-side fact stops reading as a parallel obstruction and starts reading as a piece of T4b's faithfulness contract — and as the door that closes one of §4.6's escape attempts.

**Inputs T4b consumes** (§6.5). The cost-algebra apparatus — operational cost-norm (debt #14), composition law, amortization conjecture, candidate transport via character reflection / phase-lift conservativity at `fft/PHASE-DEFECT.md`, substrate-side input via effective Hermite–Lindemann at `n = 1` (debt #3) — recast as inputs T4b's keystone proposition takes, not as parallel open commitments.

**Conditional impossibility** (§6.6). The endpoint commitment (§6.2) ties threshold improvement to `δ → 0` at the boundary; T4b's faithfulness clauses bite via §6.4's witnesses; the four §4.6 escape doors each close on `(Z, ℱ, ν, δ)`, exhausting the chase.

NATIVE-F's algebraic-side closure-mismatch reading (§7) is named as a sibling structural reading, not load-bearing.

Construction debts: working ledger at end of document (outline-only; not paper content).

# §5. A maze of twisting passages, all alike

## §5.1. Rotation-orbit Diophantine kinematics

The substrate here lives on `T = ℝ/ℤ`, not on `L`. Irrationality of `π` places the orbit `{kπ mod 1}` in Weyl's equidistribution regime against Haar measure; finite irrationality measure for `π` (audited L-W-safe at [rotations/BETA-PI-LW-AUDIT.md](rotations/BETA-PI-LW-AUDIT.md), with Mahler 1953 the cheapest witness via `μ(π) < 42`) further gives the Avila–Jitomirskaya parameter `β(π) = 0` (where `β(α) := limsup_{n→∞} (ln q_{n+1}) / q_n` over the continued-fraction denominators of `α`), the stronger discrepancy-side classification.

What the substrate gives is Haar-mean access for continuous and Riemann-integrable test functions, plus the `β(π) = 0` Diophantine classification — no kinematic feature distinguishing one mult/add trade from another beyond what passes through that mean. §5.6's kernel partition reads §5.1 as a non-direct face: the data lives on `T`, and transcription to a scalar L-observable is open.

## §5.2. Non-nesting isoperimetric registers

The planar isoperimetric gap `Δ = L² − 4πA` admits three measure-theoretic readings on non-nesting hypothesis classes: *rate* (asymptotic decay along a parametric family approaching a disk), *constant* (pointwise sharp inequality on a single curve, Bonnesen-strengthening per Osserman 1979 / Bonnesen 1924 — the annulus-width form `Δ ≥ 4π · d²` the §5.2 derivation routes through), and *almost-every* (full-measure under a distribution on parameter space, Khintchine / Beck 1994 tradition).

Worked-instance witnesses for non-nesting: the thin ellipse `(a = 2, b = 1/2)` and the small-spike `r(θ) = 1 + ε cos(5θ)` give the two pairwise non-inclusions on curve-shape space; Beck's class lives on `α`-parameter space and is type-incompatible with both. Worked-instance overhead between rate and constant: `5π ≈ 15.7×` weaker than Bonnesen direct on the chained Sobolev → geometric route, with no single extremal function realizing all three sharpnesses simultaneously ([iso/THREE-REGISTER-SYNTHESIS.md](iso/THREE-REGISTER-SYNTHESIS.md) Claim 1).

The three readings are currencies in §1.6's transaction-cost sense, with the non-nesting plus the worked overhead supplying a substrate-side `δ > 0` instance per §3.6.2 face (iv). §5.6's kernel partition reads the rate and constant registers as direct K2 instances via `f₃` and `f₂`; the almost-every register is the parameterized measure operation, requiring a parameter family before transcribing to a scalar L-observable. §6.4 picks this up as the substrate-side half of T4b's clause (ii).

## §5.3. Closed-form polygon arithmetic

Hurwitz Fourier expansion on the sparse lattice `m ≡ 1 mod n` fixes three closed-form values for the inscribed regular `n`-gon: the polygon perimeter `L_n = 2n sin(π/n)`, the isoperimetric gap rate `Δ_n = 4π⁴/(3n²) + O(1/n⁴)`, and the first-band concentration constant `6/π² = 1/ζ(2)`. The first-band concentration follows from the `ζ(2)`-tail comparison `B_j(n) ≤ B_1(n)/j²`: the leading Fourier mode carries at least `6/π² ≈ 60.8%` of `Δ_n` ([corners/HURWITZ-FIRST-BAND-CONCENTRATION.md](corners/HURWITZ-FIRST-BAND-CONCENTRATION.md) §1).

§5.6's kernel partition reads the rate via `f₃ = Δ_n` and the perimeter / first-Fourier-coefficient via `f₂ = L_n` (equivalently `c_1^{(n)} = L_n²/(4π²)`). Descent reaches these closed-form values only at threshold; §6.4 carries them through Theorem K's clause-(i) faithfulness witness.

Figures: [figures/archimedean_triptych.png](figures/archimedean_triptych.png) sets up the inside-out / outside-out / strip substrate; [figures/hurwitz_gap_rate.png](figures/hurwitz_gap_rate.png) closes the Hurwitz identity at the `4π⁴/(3n²)` Archimedean rate (three series collapse to one line over seven decades); [figures/hurwitz_gap_frequency_decomposition.png](figures/hurwitz_gap_frequency_decomposition.png) shows the first-band concentration `B_1(n) ≥ (6/π²) Δ_n` directly as a stacked-area chart over `n`.

## §5.4. Cyclotomic-ladder unboundedness against affine flatness

The maximal real subfield `K_n^+ = ℚ(ζ_n + ζ_n^{−1})` has degree `[K_n^+ : ℚ] = φ(n)/2` over `ℚ`, which grows unbounded with `n`. Affine closure over `ℚ` is flat. Native operations cannot bridge the asymmetry: they live in a closure system whose depth is constant against a substrate whose depth is unbounded.

§5.6's kernel partition reads this face as a direct K2 instance via `f₁(k, n) = φ(n)/2`. The integer-vs-continuum asymmetry recorded here is the same asymmetry NATIVE-F (§7) reads through closure-mismatch — sibling structural readings in different formal languages.

Figure: [figures/pseudo_chebyshev_arithmetic_ladder.png](figures/pseudo_chebyshev_arithmetic_ladder.png) — degrees of `cos(π/n)` over `ℚ` as a stem chart, constructible nodes filled and non-constructible open, with `n = 7` highlighted as the first cubic and first non-constructible node.

## §5.5. The admissibility envelope

The L-W envelope governs substrate-side reasoning: tools are admitted by *content* not by *calendar*, with each post-1882 import requiring a per-instance audit that the proof depends on pre-1882 content (per [memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md)). Within the envelope, no admissible method extracts additional descent information beyond what the substrate already supplies.

The operative measure-theoretic fact is the Lebesgue null/full dichotomy on `ℝ`: the algebraics are null and the transcendentals are full. Finer distinctions among transcendentals — irrationality measure, transcendence type, Diophantine class — trigger per-instance content-not-calendar audits; §5.1's `β(π) = 0` import is the leading example, with Mahler 1953's `μ(π) < 42` the cheapest L-W-safe witness.

§5.6's kernel partition reads §5.5 as fiber-constant on `L` under the literal algebraic-vs-transcendental reading, with finer cyclotomic-depth content collapsing back to §5.4's `f₁`. The §6 role is via T4b's clause (iii): composed with §4.2.1's regularity guard and effective Hermite–Lindemann at `n = 1` (§6.5's substrate-side input), it certifies that closure-class membership reads measurably against `(Z, ℱ, ν, δ)` — size-dependent shortcuts are out-of-class unless paid at the same granularity.

## §5.6. Theorem K — substrate-side σ-algebra coarsening

K is clause (i)'s witness for T4b's faithfulness at §6.3 / §6.4 and the door that closes the Farey-recoding case of the §4.6 chase. F-side coordinates strip exactly the substrate observables an adversary would need to read its threshold position.

**Theorem K.** *Let `L = {(k, n) ∈ ℤ² : 1 ≤ k < n, n ≥ 3}` and `F = {(p, q) ∈ ℤ² : 1 ≤ p < q, gcd(p, q) = 1}` carry their atomic σ-algebras, and let `R : L → F`, `R(k, n) = (k/g, n/g)` with `g = gcd(k, n)`, be the reduction map. Then `R⁻¹(2^F) ⊂ 2^L` is exactly the σ-algebra of fiber-constant subsets, and the three substrate observables `f₁(k, n) = φ(n)/2` (cyclotomic-ladder degree), `f₂(k, n) = L_n = 2n sin(π/n)` (polygon perimeter; equivalently the Hurwitz first Fourier coefficient via `c_1^{(n)} = L_n²/(4π²)`), and `f₃(k, n) = Δ_n = L_n²(1 − (π/n) cot(π/n))` (isoperimetric gap rate) are not fiber-constant — hence not `R⁻¹(2^F)`-measurable, equivalently they do not factor through `R`.*

Proof at [measure/FOR-BREAKFAST.md](measure/FOR-BREAKFAST.md) §K.0–§K.4. The three observables are non-fiber-constant on the witness pairs `f₁(1, 5) = 2 ≠ 4 = f₁(3, 15)`, `f₂(1, 3) = 3√3 ≠ 6 = f₂(2, 6)`, and `f₃(1, 3) ≈ 10.68 ≠ 3.35 ≈ f₃(2, 6)`. An apparatus restricted to F-side data — denominator-rank, Thomae-height, Stern-Brocot depth, Minkowski `?`-derivative, or any other function on `F` lifted by `R*` — cannot recover `f₁`, `f₂`, `f₃`.

**Kernel partition.** The five §5 substrate faces interact with K's coarsening in three ways. *Three direct K2 instances*: §5.2 rate via `f₃`; §5.2 constant + §5.3 Hurwitz Fourier on the sparse lattice `m ≡ 1 mod n` via `f₂` (equivalently `c_1^{(n)} = L_n²/(4π²)`); §5.4 cyclotomic ladder via `f₁`. *Two non-direct faces* anchor at pre-K2 level: §5.1's rotation-orbit kinematics live on `T = ℝ/ℤ` rather than on `L`, with the substrate-side reading carried by Weyl equidistribution against Haar (irrationality of `π`) and the stronger `β(π) = 0` classification (finite irrationality measure of `π`, audited L-W-safe at [rotations/BETA-PI-LW-AUDIT.md](rotations/BETA-PI-LW-AUDIT.md)); §5.5's L-W null/full Lebesgue dichotomy is fiber-constant on `L` under literal reading, with finer cyclotomic-depth content collapsing back to §5.4's `f₁` and the L-W safety guard governing substrate-side reasoning ([memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md)). *One measure operation*: §5.2's almost-every register requires a parameter family before it transcribes to a scalar L-observable.

**Cyclotomic-rigidity supports.** *T1 (off-backbone empty contour):* `sec(π/n) cos((2k+1)π/n) ≠ ±1/2` for all `n ≥ 3`, `0 ≤ k < n`. Proved at [measure/FOR-BREAKFAST.md](measure/FOR-BREAKFAST.md) §K.5: squaring + trace from `K_n` to `ℚ` + the Ramanujan-sum reduction `4 c_n(2k+1) = μ(n) − 3 φ(n)` + `φ(h)` exclusion. Niven's rationality theorem does not directly apply — T1 is the rationality of a *ratio* of two cyclotomic cosines, not of a single one — and the trace + Ramanujan route is the clean path. *T2 (thin-sweep all-N at slope `s = 1/√3`):* open. Empirical floor `≈ 4.5 × 10⁻⁸` through `n ≤ 100`; the slope `s = 1/√3` claim is not parallel to T1's path, since adjoining `√3 ∈ ℚ(ζ_{12})` admits real-quadratic intersections with cyclotomic composita that the T1 reduction does not close. *T3 (`x`-support / ψ trace-field compatibility):* open. Odd-Chebyshev factorization `T_{2k+1}(X)/X ∈ ℚ[X²]` reduces the plotted `x`-support to `K_n`-readable form; the uniform statement that `ψ` (the crystallographic-restriction function — minimal Euclidean dimension hosting an `n`-fold lattice rotation, with `ψ(n) = 2` exactly for `n ∈ {1, 2, 3, 4, 6}` and `ψ(7) = 6` as the first non-Bravais case; Bamberg–Cairns–Kilminster 2003) and `[K_n : ℚ]` agree on shared qualitative content is verified case-by-case at low `n`, not yet uniform.

# §6. The measure of the conversion

## §6.1. Descent in the cost framework

Descent in §1's framework means trading a higher cost-bearing complexity bound for a lower one by reorganizing the computation. Lower-bound improvement *is* successful descent; §6 asks whether descent past `T(P)` is reachable by FFT-style methods.

Per §3.6.2's non-transfer, §6 runs currency-by-currency: §6.2's endpoint commitment, §6.3's T4b, and §6.5's candidate transport each land in every cell of `T(P)`. `δ` is conceptually single but realizes in a chosen cost-norm; the cost-algebra commitments are uniform in shape, plural-in-currencies in execution. The currency-by-currency quantifier here is over *algorithm-side* cost currencies (`μ`, `α`). Substrate-side iso/ currencies (§5.2, via §3.6.2's substrate-side currency-stratification face) feed in as facts — substrate-side `δ > 0` instances per §1.6 — not as additional axes §6 quantifies over.

## §6.2. Endpoint commitment

For descent past `T(P)` to succeed, the algorithm must drive `δ` at the bounded/unbounded coefficient boundary toward zero, which in §1.7's candidate cocycle coordinate reads as competitive compression of the per-sample `{Δ_k}` cost object.

The commitment is a non-vanishing transaction-cost lemma at `T(P)`, in two halves. *Existence:* any FFT-style method achieving `T(P)` pays `δ ≥ δ_min(P) > 0` at the bounded/unbounded coefficient boundary, currency-by-currency (Morgenstern bounded-additive, Winograd modular product, AFW cyclotomic-multiplicative). *Implication:* strict improvement past `T(P)` requires `δ → 0`. The two halves are bridged by §1.6's floor-extension question — the at-threshold-to-past-threshold step — which §6.2 names as the load-bearing move that collapses the halves into two readings of one fact. Without that step, the halves are independent claims sharing a label, and the §6.6 contradiction lands at the at-threshold locus only.

This is the Coasean reading the §1.6 framework commits to: the three thresholds are *located* by irreducible friction at the boundary, not held there by an absent better algorithm; the algebra of friction determines whether the floor can be reduced. The implication direction is what the bridge to T4b earns; a biconditional is not claimed.

The endpoint is *stated* at the algorithm-side `(μ, α)` boundary, but §6.3's keystone proposition extends faithfulness to the §5.2 iso/-register currency structure, so `δ → 0` on T4b automatically covers every `δ`-instance T4b's coordinate factors. The substrate-side `δ > 0` fact (§3.6.2 face (iv)) then contradicts that endpoint, supplying the substrate-side currency-stratification half of the §6.6 composition.

## §6.3. T4b — the keystone proposition

The single sovereign claim of §6, and the locus where the §4.6 chase exhausts.

Owed in the form of a currency-universal limit object: a measure space `(Z, ℱ, ν)` (the abstract measure on `Z` is written `ν` to avoid collision with §1.3's multiplicative-cost currency `μ`) together with a `δ`-coordinate `δ : Z → ℝ_{≥0}` (the universal transaction cost), where `Z` is the limit over the three LB currencies — Morgenstern bounded-additive, Winograd modular product, AFW cyclotomic-multiplicative — joined by substrate-side iso registers (rate, constant, almost-every; §5.2) on equal footing. Structure morphisms between currency-specific cost coordinates supply the diagram `Z` is the limit over.

**Faithfulness clauses.** The faithful-measurable-coordinate condition of [measure/THE-FIRST-BRIDGE.md](measure/THE-FIRST-BRIDGE.md) reads as three specific clauses, each with a substrate-side or algorithm-side **witness** — the necessity-side input the clause consumes, cited and expanded at §6.4 — and each closing one of the §4.6 chase doors. The clauses themselves are T4b's open faithfulness requirements; the witnesses are not by themselves proofs of factor-through-`δ`.

- *(i)* The §5 scalar substrate-side observables `f₁ = φ(n)/2`, `f₂ = L_n`, `f₃ = Δ_n` factor through `δ`. **Witness:** Theorem K (§5.6). **Door:** Farey recoding.
- *(ii)* The iso-register currency structure is encoded measurably, so cross-register conversion costs read on `δ` alongside `(μ, α)`. **Witness (substrate-side):** §5.2 iso non-nesting. **Witness (algorithm-side):** §3.6.2 currency-stratification (Morgenstern↔Ailon non-transfer, §3.2). **Doors:** cross-register iso conversion, and mult-add trading.
- *(iii)* Closure-class membership reads measurably against `(Z, ℱ, ν, δ)`. **Witness:** §5.5 admissibility envelope plus §4.2.1 regularity guard. **Door:** precomputed tables / advice.

The Coasean algebra reading: `Z` is the boundary object across all three LB currencies, not one — its universality *is* the cross-currency reconciliation the lower-bound apparatus does not perform internally. Closing T4b in this form closes a substantial chunk of that reconciliation, and the non-vanishing transaction-cost lemma of §6.2 lands at every currency in the limit. T4b is open and load-bearing — the §6 keystone the rest of the chain composes around.

## §6.4. Substrate-side facts as faithfulness witnesses

The §5 menagerie acquires its §6 role here. Each substrate-side fact stops reading as a parallel obstruction and starts reading as a witness for one of T4b's faithfulness clauses; each closes one of the §4.6 chase doors.

**σ-algebra coarsening (Theorem K) → clause (i).** Theorem K (§5.6) certifies that an apparatus restricted to F-side coordinates cannot recover the three direct K2 substrate observables `f₁, f₂, f₃`. T4b's clause (i) requires those observables to factor through `δ`; the Farey-recoding attempt of §4.6 tries to read on `F` via `R`, which strips exactly those observables off the data the method has access to. The door closes: `M_FR` loses the position-reading it needs.

**Iso/-register currency-stratification (§5.2) → clause (ii) substrate-side half.** §5.2 certifies that the planar isoperimetric gap admits three non-nesting measure-theoretic readings (rate, constant, almost-every), with positive worked-instance overhead between rate and constant — `5π ≈ 15.7×` per [iso/THREE-REGISTER-SYNTHESIS.md](iso/THREE-REGISTER-SYNTHESIS.md) Claim 1 — and a categorial type-gap to almost-every. T4b's clause (ii) encodes this measurably, so cross-register conversion costs read on `δ` alongside `(μ, α)`; each conversion is a substrate-side `δ > 0` instance per §1.6 (per §3.6.2 face (iv)). The cross-register iso conversion attempt of §4.6 cannot escape via free conversion between readings.

**Currency-stratification at §3.6.2 → clause (ii) algorithm-side half.** Morgenstern↔Ailon non-transfer (§3.2) demonstrates that no canon source transfers a bound across another's coefficient regime or cost currency: the determinant potential cannot reach the normalized FFT, entropy is forced. T4b's clause (ii) encodes this algorithm-side cross-currency structure measurably; the mult-add trading attempt of §4.6 — the headline chase — fails here.

**Admissibility envelope + regularity guard (§5.5, §4.2.1) → clause (iii).** §5.5's L-W safety operative dichotomy plus §4.2.1's charging discipline jointly require that closure-class membership read measurably against `(Z, ℱ, ν, δ)`. The tables / advice attempt of §4.6 tries to absorb residue with size-dependent shortcuts; clause (iii) reads them as out-of-class unless paid at the same granularity, with per-sample cost `≥ c · p` from effective Hermite–Lindemann at `n = 1` (§6.5).

## §6.5. Inputs T4b consumes

The cost-algebra apparatus that makes T4b realizable. Each item below is an input the keystone proposition consumes, not a parallel open commitment.

**Operational cost-norm.** The composition law on the cost coordinate is at [fft/COCYCLE-COMPOSITION-LAW.md](fft/COCYCLE-COMPOSITION-LAW.md). The program commits to *operational compressibility* as the cost-norm: `δ` is the failure-to-agree of cocycle-product factors across butterfly refinements and primitive modes, measured pointwise. The Coasean reading: this matches "the friction as actually paid" — the right coordinate for the substrate-side discontinuity. Secondary norms (low-rank, factorization, residual-coordinate) remain available as sharper tests if backing is needed; not committed. The cocycle-product law itself is not yet rigorously proved; that piece is part of the algebra-of-`δ` open work named at §1.6.

**Amortization conjecture.** Whether per-instance specialization, table precomputation, or asymptotic averaging can drive per-instance `δ` below its existence-side floor is the conjecture parked at [memos/AMORTIZATION-AT-THE-BOUNDARY.md](memos/AMORTIZATION-AT-THE-BOUNDARY.md), which reduces non-amortization at the boundary to effective Hermite–Lindemann at `n = 1` via the L-W envelope route. The structural payoff is the §1.6 coupling: the algebra-of-`δ` headings *amortization* and *asymptotics* are not independent open work but downstream consequences of the substrate-side input below — closing it closes both. The conjecture is open; conditionally closed by that input.

**Substrate-side input.** The amortization conjecture's load-bearing input is a per-sample cost-form for effective Hermite–Lindemann at `n = 1`. With `ε(m) = log₂(1 + m) − m` on machine-dyadic `m = k/2^p` at variable precision `p`, the cost-form spec asks `cost_total(S, m, p) ≥ c · p` for any scheme `S` producing `ε(m)` to precision `2^{-p}`, against a uniform-charge total-cost model. Spec at [memos/EFFECTIVE-HL-N1-COST-FORM.md](memos/EFFECTIVE-HL-N1-COST-FORM.md). Open; substrate-side delivery owed.

**Candidate transport.** Character reflection barrier with phase-lift conservativity as its analytic-exponential specialization, at [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md). Carries the per-sample cost obstruction on `ε(m)` to a closure-class statement on `δ`. The original Landfall §2 affine-closure template no longer transfers at cost level under extended `C_Aff` ([fft/LANDFALL-EXTENDED-CAFF-TRANSFER.md](fft/LANDFALL-EXTENDED-CAFF-TRANSFER.md)); the live source-side obstruction is Landfall §4 plus effective H–L. The phase-lift conservativity audit at [fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md](fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md) returns *clean-conditional* on (a) variable-precision cost model and (b) effective H–L `n = 1` in cost-norm-compatible form. The first is the §1.2 variable-precision re-read, owed at §6.5; the second is the substrate-side input above, with the cost-norm-compatible qualifier settled by the operational compressibility commitment at the top of this section. The transport has no independent open work — it is the coupling claim from §1.6, and closes when those two conditions land.

Figure: [figures/delta_phase_plot.png](figures/delta_phase_plot.png) — the closure-class picture in algebraic-phase space (amortization rate, asymptotic floor). Above the working-floor line `δ_min`: the IMPOSSIBILITY region (native closure of mult/add primitives). Below the foreclosed strip: the FFT canon's claimed territory at `floor = 0`, targeted as unreachable by finite composition once the bridge closes. The horizontal mustard band straddling the working floor is where `δ_min` actually sits depending on the algebra of `δ`. Companion at [paper/code/COASE-PHASE.md](paper/code/COASE-PHASE.md).

## §6.6. Conditional impossibility

Compose: (a) the substrate-side facts as faithfulness witnesses (§6.4) — Theorem K for clause (i), §5.2 iso non-nesting and §3.6.2 currency-stratification for clause (ii), §5.5 admissibility envelope plus §4.2.1 regularity guard for clause (iii); (b) T4b as the keystone proposition (§6.3) plus the inputs it consumes (§6.5); (c) the endpoint commitment (§6.2). NATIVE-F (§7) is a sibling structural reading and not part of this composition.

Suppose `M` is an FFT-style method proving a lower bound on `P` strictly improving past `T(P)`. By (c), the descent implies `δ → 0` at the bounded/unbounded coefficient boundary — competitive `{Δ_k}` compression in §1.7's candidate cocycle coordinate. By (b), `δ` is faithfully measurable on `(Z, ℱ, ν)`, and closure-class membership factors through it. By (a), each of T4b's faithfulness clauses bites: `M`'s escape attempts — the §4.6 chase generalized from the specimen `M_FR` to the full FFT-style class — factor through one of the §4.6 doors, each of which closes on `(Z, ℱ, ν, δ)`.

Farey recoding factors through clause (i) and contradicts the endpoint because `f₁, f₂, f₃` are not recoverable on `F`; cross-register iso conversion factors through clause (ii)'s substrate-side half and contradicts the endpoint because the `5π` worked overhead and categorial type-gap are encoded into `δ`; cross-currency mult-add trading factors through clause (ii)'s algorithm-side half and contradicts the endpoint because Morgenstern↔Ailon non-transfer is encoded into `δ`; tables / advice factor through clause (iii) and contradict the endpoint because they read as out-of-class unless charged at the same granularity, with per-sample cost `≥ c · p`. The chase exhausts; `(Z, ℱ, ν, δ)` is the room every escape ends in.

The four-case structure is debt #11 closing by enumeration over §4.2.2's descriptive operation list, not by general substrate-factoring lemma. Each native operation routes its finite-composition behavior into one of the four cases; the residual check is that the routing is exhaustive over §4.2.2. The §4.2 descriptive commitment — operation list anchored to §3 sources — is what makes the enumeration land structurally rather than stipulatively. The alternative path-(ii) closure (re-tailor §4.2 around the operations §6.6 blocks) is declined: it would dissolve §Conclusion's syntactic-class meaning and bend the recursion-theoretic horizon the wrong way.

The contradiction rides on §1.6's floor-extension question: without it, the substrate-side floor and the past-`T(P)` endpoint operate on different cost-frontier loci, and the contradiction is at the at-threshold locus only.

Conditional on (b) and (c) closing, and on the §1.2 variable-precision re-read landing, no FFT-style strengthening past current thresholds is reachable on this substrate.

The smarter-FFT rebuttal upgrades from posture to content via §3.6.2: per §3.6.2's currency-stratification, no canon source transfers a bound across another's coefficient regime or cost currency, and no FFT-style passage transfers between substrate-side iso/ registers without paying transaction cost. Every such transfer is exactly `δ`. A smarter FFT-style method improving past `T(P)` would therefore have to invent a *new* cross-currency or cross-regime transfer mechanism. The impossibility theorem says FFT-style closure cannot manufacture such a mechanism from the canon's native operations: the §4.6 chase exhibits the four natural escapes FFT-style closure suggests; §6.4 names the substrate-side fact behind each door; §6.3's keystone composes them onto `(Z, ℱ, ν, δ)`.

The field's own survey aligns with this content claim: Ailon 2013 (§3.2) explicitly foregrounds that nontrivial broad linear-circuit Fourier lower bounds remain open, and known successful results require strong model restrictions — cross-currency or cross-regime transfer mechanisms are not in the literature. *Smarter FFT* therefore collapses to *FFT-style method plus machinery outside the canon's stack*, which by §4.2's class definition puts the alleged method outside the FFT-style class, not inside being smarter.

Coase 1937 supplies the *reduce yes, eliminate no* vocabulary; §3.6.2 supplies the content. The obstruction is structural, not in algorithmic cleverness.

QED for §4 once (b) and (c) are earned and the §1.2 variable-precision re-read lands.

# §7. The circle

We return to the circle — the cyclotomic substrate the conversion lived on, the integer lattice it indexed, the roots of unity it composed against, the planar isoperimetric gap it measured.

The impossibility theorem relocates what the canon was seeing all along.

The five sources are five readings of the circle's structure under five different cost coordinates — three lower bounds (Morgenstern, Winograd, Auslander–Feig–Winograd) and two cost-model anchors (Schönhage–Strassen, Ailon).

**The canon, reread on the circle.** The three lower bounds sit at the limits this substrate permits FFT-style methods to reach. Each canon source measures what its cost coordinate sees; the heterogeneity is the circle showing through.

Frame figure re-reference: [figures/native_f_closure_mismatch.png](figures/native_f_closure_mismatch.png) — the §Intro panel re-read after the impossibility theorem closes; the closure-depth contrast is the structural payoff.

**The cost-model methodology, reread on the circle.** The cost-model methodology of §3.2 — Schönhage–Strassen's operational baseline and Ailon's restricted-model sensitivity — admits a §7 reading the standard presentation does not give. Both papers, read after §6, are circle readings.

| Source | Reread on the circle |
|---|---|
| **Schönhage–Strassen 1971** | Schönhage–Strassen 1971 measures integer multiplication through the cyclotomic substrate. The construction works in `Z/F_n Z` for Fermat number `F_n = 2^{2^n} + 1`, where `2` is a primitive `2^{n+1}`-th root of unity — the circle's roots of unity made arithmetically cheap. Root multiplication reduces to cyclic shift; the recursive composability of the FFT decomposition is the cyclic group's structure showing up in the operational cost ledger. The `O(N log N log log N)` upper bound is what integer multiplication costs when counted through this cyclotomic lens — the circle's recursive symmetry together with the bit-counting overhead of finite-precision arithmetic. Integer multiplication, counted operationally on this substrate, takes the shape the substrate gives it; the cost-model makes the cheap shifts visible because the substrate makes them cheap. |
| **Ailon 2013** | Ailon 2013 measures the normalized Fourier transform through unitary entropy. The model is layered `2 × 2` unitary gates, each mixing two of `n` live coordinates — the circle's symmetry group acting infinitesimally on the data vector. The matrix-entropy potential `Φ(M) = −∑ \|M(p,q)\|² log_2 \|M(p,q)\|²` measures the information-theoretic spread of `M`'s amplitudes; `Φ(Id) = 0`, `Φ(F) = n log_2 n` for the normalized Fourier matrix, and one native gate raises `Φ` by at most `2`. The `(1/2) n log_2 n` lower bound is what the circle costs when the cost-model is unitary entropy. The normalized FFT is unitary by construction (`\|det\| = 1`); information spread is what unitary structure has to give, and the entropy potential registers it. Ailon witnesses, on the canon's own ground, that each cost-model picks up a different aspect of the circle's geometry — the cost-model and the potential are entangled with what the circle has to show. |

> **Table 2: The cost-model methodology, reread on the circle.** After §6's impossibility, what looked like an upper-bound construction and a restricted-model lower bound are two sides of the same circle reading — the canon's own apparatus for measuring what the circle was doing.

**Multi-measure framing of `T(P)`, on the circle.** The lower-bound apparatus reads cost-of-`P` through heterogeneous measures: Morgenstern's `Ω(n log n)` bit-counting on bounded coefficients; Winograd's modular-product / CRT ledger `μ(T_P) = 2n − k` on bilinear-rational; AFW's multiplicative-complexity / cyclotomic-rational-equivalence ledger.

The Morgenstern↔Ailon pair (per Table 2 above, with Ailon's circle reading paired against Morgenstern's bounded-side determinant) is the most explicit currency-stratification demonstration: same problem class (FFT), same scale (`Ω(n log n)`), two restricted models with two forced potentials — determinant on the unnormalized side, entropy on the normalized side (since determinant has modulus 1 there).

The lower-bound currencies are plural because the circle's structure is multi-coordinate; the impossibility theorem is what makes their plurality structurally meaningful.

Cross-currency coherence with the substrate-side reading at Theorem K (§5.6) is the *intended* reconciliation; per debt #9, the reconciliation itself — both the variable-precision re-read and the cross-currency alignment of `T(P)` — is open.

**Algebraic-side companion (NATIVE-F closure-mismatch).** The closure-mismatch *theorem target* at [memos/NATIVE-F-MINIMAL-DEFINITION.md](memos/NATIVE-F-MINIMAL-DEFINITION.md) §No-Go Theorem asserts that no closure-depth-preserving functor `F: C_log → C_circle` satisfying axioms A1–A4 exists between the log-side and circle-side closure systems.

Closure generators: `Aff` log-side (the affine class whose native-operation realization is `Aff⁺(ℝ)`); `{K_n}_{n ≥ 3}` circle-side, where `K_n = ℚ(cos(2π/n))` is the maximal real subfield of `ℚ(ζ_n)` (sometimes written `K_n^+`).

NATIVE-F is the circle's algebraic-side reading — the integer-vs-continuum asymmetry it records is the circle against the line.

Sibling structural reading to Theorem K (substrate-side); both record the same substrate seen through different formal languages.

Currently at proof-sketch status with promotion criteria stated.

**Scope.** The statement is about *functors* between two small observable categories; its operational reading is narrow — it forecloses the subclass of FFT-style descents that exhibit (or implicitly construct) a closure-preserving correspondence between log-side affine apparatus and circle-side cyclotomic ladder.

The companion role is what NATIVE-F's own memo claims for itself ("structural rhyme, not theorem dependency", per `memos/NATIVE-F-MINIMAL-DEFINITION.md` §Methodological note); the present outline aligns with that scope.

**[Construction debt #6: narrowed to companion-grade; promotion to closure-depth definitions remains, but is not required for the main impossibility.]**

# §Conclusion

**Operational-observable echo.** Figure [figures/counting_psi_stratification.png](figures/counting_psi_stratification.png) — the ψ(n)-stratified outside-out sweep-x-support over `n ∈ [3, 40]` — localizes the algebraic-depth discontinuity at `n = 7` (Bravais ψ = 2 backbone vs first cubic ψ = 6). The same `n = 7` first-cubic anchor sits on the algebraic side at [figures/native_f_closure_mismatch.png](figures/native_f_closure_mismatch.png) (§Intro, §7); the operational-observable register and the algebraic-side closure-depth contrast read the same discontinuity through different cost coordinates. The compute-cost branch (`memos/LEDGER-PIVOT-SEARCH.md`, `fft/FOUR-FRAMEWORK-SYNTHESIS.md`) searches for the cost-theorem that converts this stratification into a primitive-op floor.

**Outflow: the recursion-theoretic horizon.** Three debts in the apparatus — #11(iii) channel exhaustiveness, #14 cost-norm uniformity, #15 (T6) cross-chart invariance — ask whether the impossibility lifts from its intensional form to an extensional one. Does T4b's faithfulness for the closure-class indicator extend from the syntactic FFT-style class of §4.2 to the class of algorithms behaviorally equivalent to it? Is the operational compressibility cost-norm right for every behaviorally-equivalent scheme? Do all reasonable δ-algebras yield the same impossibility region at `T(P)`?

Each is the same Rice-flavored question parameterized differently — by the class, by the norm, by the coordinate. The extensional class is in each case an index set whose membership question reduces to halting; closing any of the three would require an oracle deciding behavioral equivalence to a member of the relevant class.

The §4.5 theorem is unconditional on the apparatus's three syntactic commitments — the FFT-style class fixed at §4.2, the operational cost-norm committed at §6.5, the δ-algebra realized at the §1.7 cocycle coordinate — and conditional on the construction-debt ledger closing. When the ledger closes, the impossibility is structural in those three coordinates; the extensional lift to behaviorally-equivalent classes / norms / coordinates is what the recursion-theoretic horizon is.

The paper does not claim the thread cannot be closed. It locates exactly the recursion-theoretic horizon at which extensional closure would have to happen — one horizon viewed from three loci, not three separate threads.

**Sibling outflow: non-FFT methods.** Whether a non-FFT vector field crosses the `n = 7` discontinuity is the sibling question. The trinity ranges over the FFT-style class, the cost-norm, and the δ-algebra coordinate, asking whether each lifts extensionally; the non-FFT question asks whether the syntactic class itself can be replaced. The algebraic-side companion at [memos/NATIVE-F-MINIMAL-DEFINITION.md](memos/NATIVE-F-MINIMAL-DEFINITION.md) is where an alternate vector field is considered. Adjacent open programs — the cost / conversion map at higher resolution (debt #9(c)'s variable-precision canon re-read most centrally) and the K-H-L-A discrepancy strut — run alongside.

Clean handoff, not vague future work.

# Figures

Eight figures, theorem-paired, each with an alt-text-ready companion document. All figures live at `figures/`; build scripts and companion documents per the table below.

| Figure | Build script | Companion document | Section |
|---|---|---|---|
| [figures/native_f_closure_mismatch.png](figures/native_f_closure_mismatch.png) | [memos/build_native_f_closure_mismatch.py](memos/build_native_f_closure_mismatch.py) | [memos/NATIVE-F-MINIMAL-DEFINITION.md](memos/NATIVE-F-MINIMAL-DEFINITION.md) | §Intro, §7 |
| [figures/cost_conversion_schematic.png](figures/cost_conversion_schematic.png) | [paper/code/build_cost_conversion_schematic.py](paper/code/build_cost_conversion_schematic.py) | [paper/code/COST-CONVERSION-SCHEMATIC.md](paper/code/COST-CONVERSION-SCHEMATIC.md) | §1.8 |
| [figures/archimedean_triptych.png](figures/archimedean_triptych.png) | [n-gons/build_archimedean_triptych.py](n-gons/build_archimedean_triptych.py) | [n-gons/ARCHIMEDEAN-STRIP-FLIP.md](n-gons/ARCHIMEDEAN-STRIP-FLIP.md) | §5.3 |
| [figures/hurwitz_gap_rate.png](figures/hurwitz_gap_rate.png) | [corners/hurwitz_gap.sage](corners/hurwitz_gap.sage) | [corners/HURWITZ-GAP.md](corners/HURWITZ-GAP.md) | §5.3 |
| [figures/hurwitz_gap_frequency_decomposition.png](figures/hurwitz_gap_frequency_decomposition.png) | [corners/hurwitz_gap.sage](corners/hurwitz_gap.sage) | [corners/HURWITZ-FIRST-BAND-CONCENTRATION.md](corners/HURWITZ-FIRST-BAND-CONCENTRATION.md) | §5.3 |
| [figures/pseudo_chebyshev_arithmetic_ladder.png](figures/pseudo_chebyshev_arithmetic_ladder.png) | [corners/pseudo_chebyshev_arithmetic_ladder.sage](corners/pseudo_chebyshev_arithmetic_ladder.sage) | [corners/PSEUDO-CHEBYSHEV-NODES.md](corners/PSEUDO-CHEBYSHEV-NODES.md) | §5.4 |
| [figures/delta_phase_plot.png](figures/delta_phase_plot.png) | [paper/code/build_delta_phase_plot.py](paper/code/build_delta_phase_plot.py) | [paper/code/COASE-PHASE.md](paper/code/COASE-PHASE.md) | §6.5 |
| [figures/counting_psi_stratification.png](figures/counting_psi_stratification.png) | [n-gons/counting/build_psi_stratification.py](n-gons/counting/build_psi_stratification.py) | [n-gons/counting/PSI-STRATIFICATION.md](n-gons/counting/PSI-STRATIFICATION.md) | §Conclusion |

All previously named figure-and-table gaps are now in place; further gaps will be identified during the prose pass.

---

# References

> Provenance discipline per `BNHA/ONE-FOR-ALL.md`: every load-bearing tool below names the chain it inherits from, and is staged for the next reader to pick up without reconstructing context. Working entries; bibliographic data refined per pass.

# Primary engagement — the FFT canon (§3, §7)

The five canon papers split into three lower bounds (Morgenstern, Winograd, AFW) and two cost-model methodology papers (Schönhage–Strassen, Ailon), per §3.1.

- **Schönhage, A., and Strassen, V., 1971** — operational uniform model with recursive composability; cited at §1.2 (cost-model setup) and §3.2 (cost-model methodology, baseline side: not a lower-bound source).
- **Morgenstern, J., 1973** — bounded-coefficient additive lower bound; cited at §1, §3.3, §6 (the floor that turns out to be unreachable from below).
- **Winograd, S., 1978** — modular-product theorem `μ(T_P) = 2n − k` and CRT-cyclotomic factor ledger; cited at §1, §3.4.
- **Auslander, L., Feig, E., and Winograd, S., 1984** — cyclotomic decomposition under rational equivalence; cited at §1, §3.5.
- **Ailon, N., 2013** — `Ω(n log n)` lower bound for the normalized Fourier transform in a layered `2 × 2` unitary-gate model, proved by a matrix-entropy potential; cited at §3.2 (cost-model methodology, sensitivity side: in-canon witness for the forcing of currency-stratification per §3.6.2; the survey warning that broad linear-circuit Fourier lower bounds remain open is referenced at §6.6). Source-extraction at `fft/AILON-2013-UNITARY-FFT-LOWER-BOUND-BRIEF.md`.
- **`fft/FFT-COMPLEXITY-ARTICULATION.md`** *(in-program extract)* — proof-template and trust-boundary index for the FFT canon.
- **Goldstine, H. H., 1977** — *A History of Numerical Analysis from the 16th Through the 19th Century*, §4.12–13. Pre-1882 anchor for the FFT-as-adaptive-search reading: Gauss 1805's divide-and-conquer interpolation engine, with the Pallas worked example (`4×3` vs `3×4`) chosen on practical grounds rather than asymptotic ones. Source-extraction at `fft/GOLDSTINE-1977-INTERPOLATION-BRIEF.md`; deeper framing parked at `fft/FFT-SEARCH-PLAN.md`. Cited at §1.5, §4.2, and (potentially) §3 / §7.

# Cost / conversion framework anchor (§1)

- **Coase, R. H., 1937** — "The Nature of the Firm," *Economica* New Series Vol. 4 No. 16 (Nov. 1937), pp. 386–405. PDF at [sources/Coase-1937.pdf](sources/Coase-1937.pdf). Source for the transaction-cost framework adopted at §1.6 and §6: trade through any coordination mechanism carries a non-zero, irreducible fee, and the *algebra* of that fee — additivity across compositions, amortization across repeated uses, scale-behavior, representation-dependence, bypass-resistance under specialist intermediation, and heterogeneity across transaction types — determines what the framework lets one prove. Coase's distinction between the existence of friction (p. 390: "there is a cost of using the price mechanism") and its algebra (p. 395 marginal condition; p. 396 the firm-size determination "(a) the less the costs of organising and the slower these costs rise with an increase in the transactions organised") is the methodological precedent for FIRST-PROOF debt #2 (algebra of `δ` left open with named open sub-questions). Cited at §1.6 (transaction-cost vocabulary and irreducible-fee framing), §6.6 (the *reduce yes, eliminate no* vocabulary for the conditional argument's structural claim, with full algebra of `δ` deferred per debt #2), and (potentially) §Conclusion as the methodological-framework reference.
- **`measure/COASE-FRICTION-AND-SPECIALISTS.md`** *(in-program brief)* — vocabulary memo importing Coase 1937 as the typing surface for `δ`. Articulates the existence/algebra split the program inherits (Coase pp. 390 / 395 / 396) and the methodological precedent for the algebra-of-`δ` open sub-questions. Cited from §1.6 (existence/algebra split as organizing move), §6.2 (located-by-friction reading at `T(P)`), and §6.6 (*reduce yes, eliminate no* closer).
- **Cook, S. A., and Reckhow, R. A., 1973** — RAM charging-granularity vocabulary via the `l(n)` function; cited for logarithmic charging, not for FFT lower-bound content.
- **Slot, C., and van Emde Boas, P., 1984; van Emde Boas, P., 1988/1990** — Invariance Thesis / First Machine Class methodological precedent for model-independent reasonable charging; cited as thesis-level discipline, not theorem transfer.
- **`memos/COST-MODEL-UNIFORMITY-BRIEF.md`** *(in-program extract)* — paired brief on Cook-Reckhow and van Emde Boas; cited for the terminology guard that the program's "uniform-charge" is logarithmic-measure charging, not Cook-Reckhow constant `l(n) = 1` / van Emde Boas uniform measure.

# Algebraic-side material

- **Heideman, M. T., Johnson, D. H., and Burrus, C. S., 1985, §5** — eigenspace decomposition `Q(ζ_n) = K_n ⊕ K_n · 2i sin(2π/n)` under `σ_{−1}`, forcing `K_n` as the multiplicatively-closed half; cited at §1, §6.
- **`memos/NATIVE-F-MINIMAL-DEFINITION.md`** *(in-program companion)* — closure-mismatch *theorem target* (no closure-depth-preserving functor `F: C_log → C_circle` satisfying A1–A4 between log-side and circle-side closure systems; closure generators `Aff` and `{K_n}_{n ≥ 3}`, where `K_n = ℚ(cos(2π/n))`). Currently at proof-sketch status with promotion criteria stated; awaits closure-depth definitions and full promotion (debt #6). Cited at §Intro and §7 as the algebraic-side companion.

# Substrate-side sources (§5)

- **`paper/MEASURE-THEORETIC-OBSTRUCTIONS.md`** *(paper-level pointer)* — routes the paper reader to the measure package and states the trust boundary: substrate-side typing supports Theorem K's σ-algebra coarsening reading at §5.6, not the cost-algebra apparatus (§6.3, §6.5) or the conditional impossibility itself (§6.6).
- **`measure/SUBSTRATE-OBSTRUCTIONS.md`** *(detailed measure catalogue)* — substrate-side measure-theoretic typing of the five §5 angles: Haar measure on `T = ℝ/ℤ` for §5.1; non-nesting of three measure-theoretic registers (rate / constant / almost-every) for §5.2; `ζ(2)`-tail comparison and Hurwitz Fourier expansion for §5.3; ℚ-vector-space dimension as counting-invariant obstruction for §5.4; Lebesgue null/full dichotomy under L-W safety for §5.5. Cited at §5.1–§5.5 as the source-side typing layer.

## Rotation-orbit Diophantine kinematics

- **Avila, A., and Jitomirskaya, S., "The Ten Martini Problem,"** *Annals of Mathematics* 2009 — exponential-rate Diophantine parameter `β(α) = limsup (ln q_{n+1}) / q_n`; places `π` on the Diophantine side.
- **Berthé, V., and Reutenauer, C.** — three-distance theorem combinatorial reading via three-interval exchanges.
- **Ferenczi, S., and Zamboni, L.** — perfectly clustering Lyndon-word characterization used through Berthé–Reutenauer's citation and statement, not as a separately audited source.
- **Lefèvre, V., Muller, J.-M., and Tisserand, A., 1998** — compressed-orbit pseudocode for the table-maker's-dilemma filter.
- **Marklof, J., and Strömbergsson, A.** — lattice formulation of the three-distance theorem on `Γ\SL(2, ℝ)`.

## Non-nesting isoperimetric registers

- **Osserman, R., 1979** — Bonnesen-strengthening inequality `L² − 4πA ≥ π²(R − r)²`.
- **Fuglede, B., 1989, Theorem 1.2** — stability bound for nearly-spherical domains.
- **Beck, J., 1994** — higher-dimensional Fourier + second-moment + Borel–Cantelli machinery as Diophantine substitute.
- **Bonnesen, T., 1921; 1924** — both forms; audit-catalogue same-result-different-constants instance.
- **Hurwitz, A., 1902** — Fourier-isoperimetric identity.

## Closed-form polygon arithmetic

- Hurwitz 1902 (above) — Fourier coefficients on the lattice `1 + nℤ`.
- **Gauss, C. F., *Disquisitiones Arithmeticae*, 1801** — cyclotomic ladder and constructible polygon sufficiency; the algebraic-depth substrate.
- **Wantzel, P.-L., 1837** — necessity side of the Gauss–Wantzel constructibility criterion; supports the `n = 7` first non-constructible anchor.
- **Niven, I., 1956** — rational-cosine theorem; `τ(n)` zero set `{1, 2, 3, 4, 6}`.

## Cyclotomic-ladder unboundedness against affine flatness

- HJB 1985 §5 (above).
- **Bamberg, J., Cairns, G., and Kilminster, D., 2003** — crystallographic restriction `ψ` function; rotation orders compatible with Bravais lattices = `{1, 2, 3, 4, 6}`.

## Admissibility envelope

- **Lindemann, F., 1882** — the L–W boundary; transcendence of `π`.
- **Roth, K. F., 1954** — discrepancy lower bound (transcendence-free in content).
- **Roth, K. F., 1955** — rational approximations to algebraic numbers (distinct paper, same author, adjacent year; transcendence-class theorem).
- **Fortnow, L., 2000** — Kolmogorov complexity tools; universal semicomputable measure `μ(x) = 2^{−K(x)}` and Fact 6.2 universal dominance.
- **Aitchison, J., 1959** — density-side Fourier/Poisson expansion; adjacent K-H-L-A discrepancy-strut material.
- **Kuipers, L., and Niederreiter, H., 1974** — source for the Erdős–Turán / Erdős–Turán–Koksma discrepancy-sum apparatus used by the adjacent K-H-L-A branch.

# Proof-template precedent (§6)

- **`measure/THE-FIRST-BRIDGE.md`** *(in-program bridge memo)* — names the T4b spec: a measure space `(Z, ℱ, ν)` with a `δ`-coordinate satisfying the broadened faithful-measurable-coordinate condition — the §5 scalar substrate-side observables factor through `δ`, the §5.2 iso/-register currency structure is encoded measurably so cross-register conversion costs read on `δ` alongside the algorithm-side `(μ, α)` cost, and closure-class membership reads measurably. Also names the endpoint commitment (debt #5) and is the anchor for the conditional argument's structural premises.
- **`paper/LANDFALL-EXPORT.md`** *(paper-level pointer)* — routes the paper reader to the Landfall inheritance map and states the trust boundary.
- **`fft/LANDFALL-PROOF-TEMPLATES.md`** *(detailed template map)* — original affine-closure template (Landfall §2), no-invariant-measure aggregation (Landfall §6, deploying the source content documented in `memos/BOWEN-DRILLING-AND-DENSITY.md`), finite-closure refusal (Landfall §7 via Gosper). Cited at §6 as the historical template, not as the live cost-level obstruction.
- **`fft/LANDFALL-EXTENDED-CAFF-TRANSFER.md`** *(in-program audit)* — explains why Landfall §2 does not transfer at cost level under extended `C_Aff` and why the source-side obstruction shifts to Landfall §4 plus effective H-L at `n = 1`.
- **`memos/EFFECTIVE-HL-N1-COST-FORM.md`** *(in-program target form)* — states the per-sample lower-bound shape the live source-side obstruction must supply at variable precision.
- **`fft/PHASE-DEFECT.md`** *(in-program candidate machinery)* — phase-defect cocycle `{Δ_k}`, character reflection barrier, and phase-lift conservativity as the candidate transport from source-side `ε` cost obstruction to FFT-side `δ`.
- **Bowen, L. P.** *Density in Hyperbolic Spaces.* Ph.D. dissertation, University of Texas at Austin, 2002. — §2.3.1 no-`PSL(2, ℝ)`-invariant probability measure on the binary tiling space; §2.3.1 hole-drilling instability of density under arbitrarily small perturbations; §2.3.2 alternative no-invariant-measure construction via free-group action on a noncompact `H²`-covered surface. See `memos/BOWEN-DRILLING-AND-DENSITY.md` for the source-extraction brief; citation form lifted from Landfall.
- **Gosper, R. W., 1972** — continued-fraction arithmetic machine; cited as the negative anchor (exact computation in unbounded state, finite closure refused).

---

# Construction-debt ledger

> **Outline-only — not paper content.** Working ledger of construction debts that gate the §4.5 theorem. By the prose pass each debt will have been proven, resolved, or absorbed; this ledger does not survive into the paper. Inline `[Construction debt #N]` flags in §6.2, §6.3, §6.5, §7 reference rows of the table below. Per-citation guardrails (trust boundaries, do-not-re-claim discipline) live at the linked anchor memos rather than in this table; consult those for the citation-by-citation contract.

The fifteen debts of `paper/PROOF-CHAIN.md`, mapped to outline location, status, and anchoring memo.

| # | Name | Outline location | Status | Anchor |
|---|---|---|---|---|
| 1 | T4b — boundary object with `δ`-faithfulness as currency-universal limit | §6.3 | Open; central. Owed in the form of a currency-universal limit `Z` over canon currencies (Morgenstern, Winograd, AFW; debt #9) joined by substrate-side iso registers (rate, constant, almost-every) on equal footing, with `δ` the universal transaction-cost coordinate. The Coasean algebra reading: `Z` is the boundary object across the whole canon, not one currency. Faithfulness: (i) §5 scalar observables `f₁, f₂, f₃` factor through `δ`; (ii) iso-register currency structure encoded measurably so cross-register conversion costs read on `δ` alongside `(μ, α)`; (iii) closure-class membership reads measurably against `(Z, ℱ, ν, δ)`. Couples to debt #5 (the non-vanishing transaction-cost lemma must land at every currency in the limit) and debt #12 (currency-morphism construction supplies the limit's input). Closing #1 in this form closes a substantial chunk of #9. Phase decomposition (1a fix `δ`; 1b construct `Z`; 1c verify faithfulness clauses) at [paper/T4B-DECOMPOSITION.md](paper/T4B-DECOMPOSITION.md). | [measure/THE-FIRST-BRIDGE.md](measure/THE-FIRST-BRIDGE.md), [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md), [paper/T4B-DECOMPOSITION.md](paper/T4B-DECOMPOSITION.md) |
| 2 | Algebra of `δ` — sub-question status, with (4)+(5) reduced to #3 and (8) added as the bridge for #5 | §1.6, §6.5 | **Partially earned.** Per `measure/ALGEBRA-OF-DELTA.md`'s eight-sub-question decomposition: (1) existence, (2) advice-side bypass-resistance, (6) representation-dependence (closed for all four canon frameworks via the COCYCLE-TRANSLATION memos as (b)-conditional out-of-scope), and (7) sign-vs-shape are closed in spirit; (3) additivity has its formal-character composition-law skeleton in hand at `fft/COCYCLE-COMPOSITION-LAW.md` (partial-yes verdict; cross-term collapses under regularity guard); (4) amortization and (5)-strong asymptotics are reduced to **debt #3 (effective H–L `n=1`)** via the L-W-envelope route at `memos/AMORTIZATION-AT-THE-BOUNDARY.md` — the substantive contribution: amortization-failure at the boundary is downstream of #3 landing, not an independent debt; (8) floor extension from at-threshold to past-threshold is the structural bridge between debt #5's existence and implication halves — **discharged at [measure/ENDPOINT-COMMITMENT.md](measure/ENDPOINT-COMMITMENT.md) via substrate-side floor invariance under T(P)-movement**; couples to (3) and #14. **What's still open inside #2:** rigorous proof of the composition law (full FP arithmetic model + regularity-guard exhaustiveness + edge cases like subnormals/overflow); (3)'s super-additive-at-boundary working hypothesis under route-3 morphism semantics (#12). **Closed via discharge:** (8) at `measure/ENDPOINT-COMMITMENT.md`. **Couplings:** #5's route-2 lemma form (`δ ≥ δ_min(P) > 0`) absorbs (5)-strong and consumes (8) as the at-threshold/past-threshold bridge; #1's route-3 limit demands (3) precision for the universal property; #13 substrate-extends the algebra to iso-register friction with defense-in-depth discipline; #14 (committed cost-norm) is the definitional move that gates the whole apparatus. | [fft/COCYCLE-COMPOSITION-LAW.md](fft/COCYCLE-COMPOSITION-LAW.md), [memos/AMORTIZATION-AT-THE-BOUNDARY.md](memos/AMORTIZATION-AT-THE-BOUNDARY.md), [measure/ALGEBRA-OF-DELTA.md](measure/ALGEBRA-OF-DELTA.md), [measure/ENDPOINT-COMMITMENT.md](measure/ENDPOINT-COMMITMENT.md) |
| 3 | Effective H-L `n = 1` cost-form | §6.5 | Open; substrate-side delivery owed. Per-sample bound `cost_total ≥ c · p` against uniform-charge total cost on machine-dyadic `m = k/2^p`. | [memos/EFFECTIVE-HL-N1-COST-FORM.md](memos/EFFECTIVE-HL-N1-COST-FORM.md) |
| 4 | Character-reflection / phase-lift transport — coupling claim, audit clean-conditional | §6.5 | Open. The phase-lift conservativity audit (`fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md`) verdict is **clean-conditional** per AMORTIZATION-AT-THE-BOUNDARY's blocker analysis — the audit itself is done. Carries the per-sample cost obstruction on `ε` to a closure-class statement on `δ`. **No independent open work; #4 is structurally a coupling claim.** **Conditions:** (a) variable-precision cost model — debt #9's variable-precision-canon-re-read part; (b) effective H–L `n=1` in cost-norm-compatible form — debt #3, with the "in cost-norm-compatible form" qualifier settled by #14's committed operational compressibility. Closing #3 + #9's variable-precision part closes #4 automatically. Same coupling pattern as (4)+(5)→#3 in debt #2 and (8)-bridge structure for #5: closing one debt visibly moves another. | [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md), [fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md](fft/PHASE-LIFT-CONSERVATIVITY-AUDIT.md), [fft/LANDFALL-EXTENDED-CAFF-TRANSFER.md](fft/LANDFALL-EXTENDED-CAFF-TRANSFER.md) |
| 5 | Endpoint commitment as non-vanishing transaction-cost lemma at canon thresholds | §6.2 | Closes structurally (modulo #12 + #9(c)). Two halves bridged by debt #2 sub-question (8): **(existence half)** any FFT-style method achieving the canon threshold `T(P)` pays `δ ≥ δ_min(P) > 0` at the bounded/unbounded coefficient boundary; **(implication half)** strict improvement past `T(P)` requires `δ → 0` (or competitive `{Δ_k}` compression in the candidate cocycle coordinate). #2(8)'s floor-extension closes the bridge via substrate-side structural invariance under T(P)-movement; the §6.6 contradiction lands. The Coasean reading the §1.6 framework commits to ([measure/COASE-FRICTION-AND-SPECIALISTS.md](measure/COASE-FRICTION-AND-SPECIALISTS.md)): the canon thresholds are *located* by irreducible friction at the boundary, not held there by an absent better algorithm. Currency-by-currency reading uses morphism rescalings from debt #12. **Discharge:** [measure/ENDPOINT-COMMITMENT.md](measure/ENDPOINT-COMMITMENT.md) — both halves + the bridge proved on T4b's faithful `(Z, ℱ, ν, δ)`. | [measure/THE-FIRST-BRIDGE.md](measure/THE-FIRST-BRIDGE.md) §What The Argument Must Show; [measure/COASE-FRICTION-AND-SPECIALISTS.md](measure/COASE-FRICTION-AND-SPECIALISTS.md); [measure/ENDPOINT-COMMITMENT.md](measure/ENDPOINT-COMMITMENT.md) |
| 6 | NATIVE-F closure-mismatch promotion | §7 | Open; sibling structural reading to K. Forecloses the narrow subclass of FFT-style descents that exhibit a closure-preserving correspondence between log-side and circle-side closure systems; not load-bearing for the §6.6 main composition. Promotion to closure-depth definitions still wanted but not required for §4.5. | [memos/NATIVE-F-MINIMAL-DEFINITION.md](memos/NATIVE-F-MINIMAL-DEFINITION.md) |
| 7 | T2 thin-sweep all-N | §5.6 (cyclotomic-rigidity supports) | Open; proof target. Real-quadratic intersection with cyclotomic composita; not parallel to T1's path. | [n-gons/counting/THICK-SWEEP.md](n-gons/counting/THICK-SWEEP.md) |
| 8 | T3 `x`-support / ψ trace-field compatibility | §5.6 | Open. Uniform statement of odd-Chebyshev `K_n`-readability + ψ-coloring agreement. | [n-gons/counting/PSI-STRATIFICATION.md](n-gons/counting/PSI-STRATIFICATION.md) |
| 9 | Uniform-charge cost model, canon re-read, and `T(P)` currency reconciliation — split into (a) set / (b) absorbed / (c) still owed | §1.2, §6.5, §6.6, §7 | Three components with sharply different status: **(a) Methodological commitment** — uniform-charge cost model, charging discipline, regularity guard. **Set** at §1.2 per `memos/COST-MODEL-UNIFORMITY-BRIEF.md`; closed in spirit. **(b) Cross-currency reconciliation of `T(P)`** — alignment of Morgenstern bounded-additive, Winograd modular product, AFW cyclotomic-multiplicative thresholds in a single cost framework. **Substantially absorbed** by debt #1's route-3 currency-universal limit: `Z`'s universality *is* the reconciliation. Closing #1 + #12 closes most of (b); residual is the explicit currency-by-currency check that the limit construction lands at each entry of `T(P)`. **(c) Variable-precision canon re-read** — re-read Morgenstern, AFW, Winograd, Ailon at variable precision under the uniform-charge guard. **Still owed in full.** Real substantive work; not absorbed by other debts. **Couplings:** (b) closes together with #1 + #12 under route 3; (c) is what gates #4's transport (closing (c) + #3 closes #4). | [memos/COST-MODEL-UNIFORMITY-BRIEF.md](memos/COST-MODEL-UNIFORMITY-BRIEF.md), canon re-reads (Morgenstern, AFW, Winograd, Ailon) |
| 10 | Trust-boundary discipline | §3, §6, References (per-source) | Ongoing. Each canon citation respects [fft/PROVENANCE-AND-TRANSFERABILITY.md](fft/PROVENANCE-AND-TRANSFERABILITY.md)'s stated boundaries; per-source guardrails at the cited memos. | [fft/PROVENANCE-AND-TRANSFERABILITY.md](fft/PROVENANCE-AND-TRANSFERABILITY.md) |
| 11 | Channel exhaustiveness for §6.6 composition (path-(i)-by-enumeration) | §4.2.2, §6.6 | **Committed closure form: path (i) by finite-composition enumeration over §4.2.2.** The §6.6 chase walks four cases against T4b's three faithfulness clauses (Farey recoding → (i); cross-register iso → (ii)-substrate; mult-add trading → (ii)-algorithm; tables/advice → (iii)); the residual check is whether finite compositions of §4.2.2's five descriptive operations stay inside that four-case routing. Open in that residual sense; load-bearing. The class definition is fixed at §4.2.2 descriptively (each operation traced to a §3 canon source) and does *not* move under #11's closure. **Path (ii) declined:** the alternative closure form (re-tailor §4.2 around the operations §6.6 happens to block) would dissolve §Conclusion's syntactic-class meaning and bend the recursion-theoretic horizon the wrong way; not the closure path the paper takes. Provenance: FIRST-PROOF #5 (Lemma A exhaustiveness) was the original home; retired with Lemma A and not transferred. With #6 narrowed to companion-grade, the old negative-space argument has lost the NATIVE-F pillar. **Recursion-theoretic horizon (per §Conclusion outflow):** path (iii) — negative-space covering over candidate non-blocked descents — is forced to range behaviorally and is undecidable in general (Rice's theorem); the §Conclusion outflow recognizes its extensional version as the natural future-research horizon, not as a closable debt. **Discharge:** path-(i) closure verified at [fft/CHANNEL-EXHAUSTIVENESS.md](fft/CHANNEL-EXHAUSTIVENESS.md) — per-operation classification (5 ops × 4 channels) plus composition closure. | this §6.6, §4.2.2; `paper/FIRST-PROOF.md` debt #5 (retired); [fft/CHANNEL-EXHAUSTIVENESS.md](fft/CHANNEL-EXHAUSTIVENESS.md) |
| 12 | Currency-morphism construction for the T4b limit | §6.3 | Open. Inputs to the route-3 currency-universal limit `Z` (debt #1) — the *diagram* whose limit `Z` is. Each canon currency (Morgenstern bounded-additive, Winograd modular product, AFW cyclotomic-multiplicative) and each substrate-side iso register (rate, constant, almost-every) needs to be presented as a measurable cost-coordinate object, with structure morphisms between them: e.g., Morgenstern↔Winograd as the bounded↔unbounded coefficient transfer, Winograd↔AFW as modular product → cyclotomic decomposition, iso-register transitions as the `5π`-overhead Sobolev → geometric chain (per `iso/THREE-REGISTER-SYNTHESIS.md` Claim 1). **Order:** #12 is logically prior to #1 (the diagram precedes the limit); realistically the two close in tandem — sketch diagram, take candidate limit, check faithfulness (i)–(iii), refine, retake. **Route-3 commitment:** #12 only exists because route 3 was committed for #1; routes 1 (cocycle-direct) and 2 (fiber-product) wouldn't generate this debt. **Existing pieces:** Morgenstern↔Ailon morphism worked in-canon at §3.2 (determinant doesn't transfer to normalized FFT; entropy needed) — illustrative negative morphism at one transition; iso-register `5π` Sobolev → geometric overhead worked at `iso/THREE-REGISTER-SYNTHESIS.md` Claim 1, with categorial type-gap to almost-every; substrate observables `f₁, f₂, f₃` constructed via Theorem K with explicit fiber-non-constant witnesses. **Scope guard:** #12 stays narrowly scoped to the diagram of cost-coordinate objects and morphisms. It *uses* #2's cost-norm and composition law; it does not define them. It *consumes* #9's variable-precision canon re-read; it does not perform it. Drift into #2 or #9 territory should be flagged. Depends on debt #9. **Adjacent extensional question (absorbed into §Conclusion outflow by analogy with #15):** are the named structure morphisms (Morgenstern↔Winograd, Winograd↔AFW, iso-register transitions) all the reasonable morphisms in the route-3 diagram, or are there other reasonable morphisms that would change `Z`'s universal property? Diagram-side dual of #15's coordinate question; same Rice flavor (extensional class "all reasonable morphisms" is not syntactically decidable); not separately enumerated in the outflow to keep the trinity clean. The route-3 commitment makes `Z`'s universality a property of *the chosen diagram*; lifting to "the universal limit over all reasonable diagrams" meets the same horizon as #15. | [measure/THE-FIRST-BRIDGE.md](measure/THE-FIRST-BRIDGE.md), [iso/THREE-REGISTER-SYNTHESIS.md](iso/THREE-REGISTER-SYNTHESIS.md), this §3.2 |
| 13 | Substrate-side `δ` generalization — amortized definitional commitment | §1.6 | Open and ongoing (mortgage-style, not discrete proof). Definitional commitment at §1.6: `δ` is the transaction cost between any two non-nesting measure-theoretic readings of one quantity. This extends Coase's economic-coordination friction to measure-theoretic non-nesting overhead — a generalization that is more than a definition (it asserts the algebra of friction transfers across the extension) and more than a theorem (it sets the typing the rest of the paper uses). **Down-payment:** §3.6.2 face (iv) — substrate-side instance with worked overhead (`5π` Sobolev → geometric per `iso/THREE-REGISTER-SYNTHESIS.md` Claim 1) and categorial type-gap to almost-every. **Amortization schedule:** §6.3 T4b clause (ii) treats substrate-side iso-register friction measurably; §6.6 cross-register channel argument uses it for the substrate-side contradiction; debt #1's route-3 limit hosts substrate and algorithm currencies on equal footing; substrate-side Coasean instances accumulate as the paper proceeds. **Defense-in-depth discipline:** no single argument should hinge on the generalization alone — each load-bearing use must be independently defensible from substrate-side or algorithm-side facts, so attacking the definition does not topple the proof. The debt closes asymptotically through usage, not at a discrete moment. **Adjacent extensional question (absorbed into §Conclusion outflow by analogy with #15):** are the three named iso registers (rate, constant, almost-every) all the reasonable measure-theoretic readings of the planar isoperimetric gap, or are there other reasonable readings the substrate-side `δ > 0` instance should account for? Substrate-side dual of #15's coordinate question; same Rice flavor (extensional class "all reasonable measure-theoretic readings" is not syntactically decidable); not separately enumerated in the outflow to keep the trinity clean. The defense-in-depth discipline of the mortgage covers this — no single argument should hinge on the three iso registers being the *only* readings. | this §1.6, §3.6.2 face (iv), §6.3 (ii), §6.6; [measure/COASE-FRICTION-AND-SPECIALISTS.md](measure/COASE-FRICTION-AND-SPECIALISTS.md) |
| 14 | Cost-norm commitment for `δ` (operational compressibility) | §6.5 | **Committed.** `δ` is the operational cost-norm on the cocycle product across an FFT-style scheme `S`'s composition path (per `fft/COCYCLE-COMPOSITION-LAW.md` recommendation): the failure-to-agree of cocycle-product factors across butterfly refinements and primitive modes, measured pointwise. Definitional move, not a theorem. **Coasean reading:** the operational norm matches "the friction as actually paid" — the right coordinate for the substrate-side discontinuity. **What it gates:** #1 (route-3 limit needs `δ` to have a precise algebra), #5 (route-2 lemma needs `δ_min(P)` defined in some norm), #12 (morphism costs need a norm to live in), #4 (transport carries cost in the norm), and #2's remaining work (rigorous composition-law proof must respect the norm). Secondary cost-norms (low-rank, factorization, residual-coordinate) remain available as sharper tests if the operational form needs backing; not committed. **Recursion-theoretic horizon (per §Conclusion outflow):** asking *is the operational norm right for every behaviorally-equivalent scheme?* is a Rice-flavored question (cost-norm uniformity over the extensional class); the outflow absorbs this as a sub-question of the intensional/extensional dichotomy, not a separate debt. | [fft/COCYCLE-COMPOSITION-LAW.md](fft/COCYCLE-COMPOSITION-LAW.md), [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md) |
| 15 | Cross-chart invariance of the impossibility region (T6) | §6.3, §6.5, §Conclusion | **Open and absorbed by the §Conclusion outflow as route 3.** Two forms per `measure/FOR-BREAKFAST.md` §K.6: **weaker T6** (substrate-side discontinuity is upstream of any specific δ-coordinate; the boundary-as-set is coordinate-independent) is held as posture via Coase 1937; **stronger T6** (all reasonable δ-algebras yield the same impossibility region at `T(P)`) is open and load-bearing for the §4.5 structural claim. The apparatus is committed to the cocycle coordinate (route 3 for #1, route 2 for #5, the (8) bridge); without T6, §4.5 reads "impossibility in the cocycle coordinate" rather than "structural impossibility." **Route 3 commitment:** the extensional T6 ("all reasonable coordinates") is Rice-flavored — "reasonable" is not a syntactically decidable class, and cross-coordinate impossibility-region equivalence is undecidable in general by the same mechanism as #11(iii) and #14 cost-norm uniformity. The §Conclusion outflow absorbs T6 as a sub-question of the intensional/extensional dichotomy, parallel to #11(iii) and #14. The §4.5 theorem holds on the syntactic δ-algebra (cocycle realization at `fft/PHASE-DEFECT.md`); lifting to the extensional class meets the recursion-theoretic horizon. **Couplings:** T4b (route 3 for #1) committed to cocycle coordinate; ALGEBRA-OF-DELTA's Coordinate scope and FOR-BREAKFAST §K.6 acknowledge T6 explicitly. Route 3 does not foreclose later upgrades to direct invariance per candidate algebra or finite-list verification if a stronger claim becomes available. | [measure/FOR-BREAKFAST.md](measure/FOR-BREAKFAST.md) §K.6, [measure/ALGEBRA-OF-DELTA.md](measure/ALGEBRA-OF-DELTA.md) Coordinate scope, [measure/COASE-FRICTION-AND-SPECIALISTS.md](measure/COASE-FRICTION-AND-SPECIALISTS.md) |

Earned and not on this list: σ-algebra coarsening (Theorem K, §5.6), Lemma T1 (off-backbone empty contour, [measure/FOR-BREAKFAST.md](measure/FOR-BREAKFAST.md) §K.5), T4a (common indexing domain `L`), the `β(π) = 0` L-W audit at [rotations/BETA-PI-LW-AUDIT.md](rotations/BETA-PI-LW-AUDIT.md). The destination is conditional on (1)–(3) and (5) plus (9)(c)'s variable-precision canon re-read, (11)'s channel exhaustiveness, and (12)'s currency-morphism construction; (4) is a coupling claim that closes automatically when #3 + (9)(c) land; (6) is companion material whose promotion is wanted but not required for §4.5; (7)–(8) and (10) are supports and discipline; (13) is qualitatively different — an ongoing definitional commitment with mortgage-style amortization across the paper rather than a discrete proof obligation, with the discipline being defense-in-depth so no single argument depends on the generalization alone; (14) is a committed definitional move (operational compressibility) that gates #1, #5, #12, #4, and #2's remaining work; (15) is recognized as a recursion-theoretic horizon absorbed by the §Conclusion outflow (parallel to #11(iii) and #14 cost-norm uniformity), not a closable debt within the apparatus. Coupling notes: (1)+(9)(b)+(12) close together under route 3 — `Z`'s universality *is* the reconciliation of (9)(b), and (12) supplies the morphism inputs (1) takes the limit over; (9)(a) is set per §1.2; (9)(c) is the substantive remaining work. (2)'s sub-questions (4)+(5) reduce to debt #3 via the L-W-envelope route at `memos/AMORTIZATION-AT-THE-BOUNDARY.md`; closing #3 closes the substantive open part of #2; (2)'s sub-question (8) bridges #5's two halves.
