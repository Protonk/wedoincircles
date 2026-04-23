# FORTNOW-KOLMOGOROV-BRIEF

Source-extraction memo on **Lance Fortnow, "Kolmogorov Complexity"** (prepared from notes taken by Amy Gale at the Kaikoura workshop, January 2000; 14 pages, 9 sections, 4 references). The notes cover plain Kolmogorov complexity `C`, prefix-free complexity `K`, time-bounded versions `C^t` and `CD^t`, Kraft's inequality, the universal semicomputable measure, and size-of-set bounds via hashing.

Proofs in the notes are mostly sketches. §7 is attributed there to Buhrman–Fortnow–Laplante 2001 and Buhrman–Laplante–Miltersen 2000; §8.3 is attributed to Sipser 1983.

## Main payloads

- **§6** — Kraft's inequality Σ 2^{-|x|} ≤ 1 for prefix-free `A`, the universal semicomputable measure `μ(x) = 2^{-K(x)}`, the dominance fact that any semicomputable sub-probability measure is bounded by a constant times `μ`, and **Theorem 6.3**: `T_worst(n) = O(T_average(n))` under `μ`.
- **§7** — time-bounded `C^t` vs. distinguishing variant `CD^t`; Theorem 7.2 links polynomial `C ≤ CD` to unique-SAT search.
- **§8** — for `A ∈ P`, `CD^p(x) ≤ 2 log |A ∩ Σ^n| + c log n` (Theorem 8.1), with a `log^c n`-approximation for a δ-fraction (Theorem 8.2), and Sipser's hashing-based `log |A∩Σ^n| + c log n` for most advice strings (Theorem 8.3). Valiant–Vazirani follows.

---

## §1. Introduction — plain Kolmogorov complexity `C`

**Definition 1.1.** For fixed alphabet `Σ = {0,1}` and partial computable `f : Σ* → Σ*`,

```
C_f(x) = min{|p| : f(p) = x}   if x ∈ ran f,   else ∞.
```

A description of `x` relative to `f` is any `τ` with `f(τ) = x`. Care is needed against Berry-style paradoxes: `f` is required to be *computable* (not necessarily total).

**Universal UTM.** There is a universal Turing machine `U` and a corresponding universal partial computable `g` (defined by `g(0^{|p|} 1 p y) = U(p, y)`) such that **Claim 1.1**: for every partial computable `f`, there is a constant `c` (in fact `c = 2|p| + 1` where `p` encodes `f`) with

```
C_g(x) ≤ C_f(x) + c     for all x.
```

Define `C(x) := C_g(x)`, well-defined up to an additive constant. Extend to conditional `C(x|y) = min{|p| : g(p, y) = x}`; `C(x|ε) ≡ C(x)`.

**Basic properties.**

1. `C(x) ≤ |x| + c`  (the identity description).
2. `C(xx) ≤ C(x) + c`.
3. For any partial computable `h`, `C(h(x)) ≤ C(x) + c_h`, where `c_h` is the length of a description of `h`.
4. `C(x|y) ≤ C(x) + c`.

**Pairing.** `⟨x, y⟩` is the concatenation `xy` with a self-delimiting marker on `|x|`. A naive concatenation `p q` fails because we cannot find the boundary; encoding `|p|` in self-delimited form (e.g., by "local doubling": `1010` → `1100110001`, with `01` as end marker) gives

```
C(⟨x,y⟩) ≤ C(x) + C(y) + 2 log C(x) + c.
```

Iterating the self-delimiting trick on `log C(x)` itself gives the "log-star" family of refinements,

```
C(⟨x,y⟩) ≤ C(x) + C(y) + log C(x) + 2 log log C(x) + c,
C(⟨x,y⟩) ≤ C(x) + C(y) + log C(x) + log log C(x) + 2 log log log C(x) + c,
⋮
```

**Theorem 1.2 (Incompressibility).** `(∀n)(∃x ∈ Σ^n)(C(x) ≥ n)`. Such `x` are called **Kolmogorov-random**.

*Proof.* Pigeonhole. There are `2^n − 1` programs of length `< n` but `2^n` strings of length `n`, so not every length-`n` string can have a description shorter than `n`. ∎

---

## §2. Some applications

Fortnow reframes classical theorems via incompressibility as **alternative proofs**.

**Theorem 2.1.** *There are infinitely many primes.*

*Proof.* Suppose `p_1, …, p_k` enumerates all primes. Take Kolmogorov-random `m` of length `n`. Write `m = p_1^{e_1} ⋯ p_k^{e_k}`. Each `|e_i| ≤ log m`, so `|⟨e_1,…,e_k⟩| ≤ 2k log log m`. Since `m ≤ 2^{n+1}`, `C(m) ≤ 2k log(n+1) + c`. For `n` large, this contradicts `C(m) ≥ n`. ∎

An effective refinement: for `m` Kolmogorov-random with `p_i` the largest prime dividing `m`,

```
C(m) ≤ C(⟨i, m/p_i⟩) ≤ 2 log|i| + |i| + |m/p_i|,
```

giving `log p_i ≤ log i + 2 log log i`, hence `p_i ≤ i (log i)^2`.

**Theorem 2.2.** *Most strings are near-random.* For all `k` and `n`,

```
|{x ∈ Σ^n : C(x) ≥ |x| − k}| ≥ 2^n (1 − 2^{−k}).
```

*Proof.* At most `2^{n−k} − 1 < 2^{n−k}` programs of length `< n − k`. ∎

**Immune sets.** Let `A = {x : C(x) ≥ |x|/2}`.

**Theorem 2.3.** *If `B` is a computably enumerable subset of `A`, then `B` is finite.*

*Proof.* Suppose `B` is c.e. and infinite. Define `h(n) =` first element enumerated into `B` with length `≥ n`. Then `h` is total and computable (dovetailing), and `h(n) ∈ A`, so `C(h(n)) ≥ |h(n)|/2 ≥ n/2`. But `C(h(n)) ≤ C(n) + c ≤ log n + c`. For large `n`, `n/2 > log n + c`, contradiction. ∎

**Gödel-style application.** In a sound proof system, let `B = {x : there is a proof that x is random}`. Then `B` is c.e. and `B ⊆ A`, so Theorem 2.3 implies that `B` is finite. Thus only finitely many strings can be proved random in that system.

---

## §3. Runs in random strings

**Cut-and-paste, upper bound on runs of zeros.** If `x = u 0^{2 log n} v` for some `u, v` and `x` has length `n`,

```
C(x) ≤ |u| + |v| + log|u| + 2 log log|u| + c ≤ n − 2 log n + log n + 2 log log n + c.
```

Hence `C(x) ≤ n − log n + 2 log log n + c`, contradicting `C(x) = n` for large `x`. So random strings have *no* runs of `2 log n` zeros.

**More surprisingly, random strings must have relatively long runs.** Break `x` into `2n / log n` segments of length `log √n = (log n)/2`. If no run of `(log n)/2` zeros, each segment is one of `√n − 1` possibilities (exclude `0^{log √n}`). Total number of such `x` is at most

```
(√n − 1)^{2n / log n} ≈ 2^n · e^{−2√n / log n},
```

a shrinking fraction of `2^n`. Enumerable, so `C(x) ≤ n − Ω(√n / log n)`, contradicting randomness.

**Theorem 3.1 (size-of-set via complexity).**

- If `A` is finite, `(∀y ∈ Σ*)(∃x ∈ A)(C(x|y) ≥ log|A|)`.
- If `B ⊆ Σ* × Σ*` is an infinite c.e. set with `B_y = {x : ⟨x,y⟩ ∈ B}` finite for every `y`, then
  ```
  (∀x, y : x ∈ B_y)(C(x|y) ≤ log|B_y| + c).
  ```

*Proof sketch.* First item: counting. Second item: enumerate `B_y` in some order `x_1, …, x_{|B_y|}`; describe `x` by `B`'s generator program, `y`, and the index `i ≤ |B_y|`. ∎

Specialization to permutations: let `B_n` be the set of permutations of `{1,…,n}` encoded as strings. Then `(∃x ∈ B_n)(C(x|n) ≥ log|B_n| = log(n!) = n log n - O(n))` and `(∀x ∈ B_n)(C(x|n) ≤ log|B_n| + c)`.

---

## §4. Symmetry of information

From §1's pairing bound: `C(⟨x,y⟩) ≤ C(y|x) + C(x) + O(log n)`, where `n = max{|x|, |y|}`. The reverse direction is essentially tight:

**Theorem 4.1.** `C(y|x) + C(x) ≤ C(⟨x,y⟩) + O(log n)`.

*Proof sketch.* Let `A = {⟨u,v⟩ : C(⟨u,v⟩) ≤ C(⟨x,y⟩)}` and `A_u = {v : ⟨u,v⟩ ∈ A}`. `A` is finite and recursively enumerable given `⟨x,y⟩`. Take `e ∈ ℕ` with `2^{e+1} > |A_x| ≥ 2^e`. Then

```
C(y|x) ≤ log|A_x| + O(1) = e + O(1).
```

Let `B = {u : |A_u| ≥ 2^e}`. Then `|B| ≤ |A|/2^e ≤ 2^{C(⟨x,y⟩)} / 2^e`. Since `x ∈ B`,

```
C(x) ≤ |e| + log(2^{C(⟨x,y⟩)}/2^e) + 2 log|e| ≤ C(⟨x,y⟩) − e + O(log n).
```

Adding gives `C(x) + C(y|x) ≤ C(⟨x,y⟩) + O(log n)`. ∎

Define the information content of `y` in `x` by `I(x:y) = C(y) − C(y|x)`.

**Corollary 4.2.** `I(x:y) = I(y:x) ± O(log n)`.

---

## §5. Prefix-free complexity `K`

**Definition 5.1.** `A ⊆ Σ*` is **prefix-free** if no `x ≠ y` in `A` has `x` a prefix of `y`. `f` is prefix-free if `dom f` is prefix-free.

**Definition 5.2.** A **prefix-free machine** is a Turing machine with an input tape, work tapes, and output tape. The input head reads left-to-right only; at each step the machine either (1) reads and advances, (2) halts with output, or (3) diverges. `M` accepts `f` if `f(x) = y` implies `M` reads exactly `x`, outputs `y`, halts; and `f(x)` undefined implies `M` does not halt on `x`.

**Theorem 5.1.** *Every prefix-free partial computable function is accepted by a prefix-free machine, and there is a universal prefix-free machine.*

*Proof sketch.* Given `f` prefix-free and partial computable, and input `z`: before reading any more, simulate `f` on all `y` with `z` as a prefix until `f(y)` halts (if it does). If `y = z`, output `f(y)`; if `y ≠ z`, read the next bit of input. The universal version uses `0^{|p|} 1 p x` with `p` the program for `f`. ∎

Define `K(x) := C_h(x)` where `h` is the universal prefix-free partial computable function.

**Consequences.**

- **Theorem 5.2.** `K(⟨x,y⟩) ≤ K(x) + K(y) + c`. *(No `log` factor: by prefix-freeness, `p` is the unique initial segment of `pq` on which the machine halts.)*
- **Theorem 5.3.** `(∀n)(∃x ∈ Σ^n)(K(x) ≥ n)`. *(Same counting argument.)*
- **Upper bound loss.** No longer `K(x) ≤ |x| + c`; instead `K(x) ≤ 2 log|x| + |x| + c`, and iterated `K(x) ≤ log|x| + 2 log log|x| + |x| + c`, etc.
- **Lower bound on the upper bound.** `(∀c)(∃x)(K(x) ≥ |x| + log|x| + c)`.

---

## §6. Kraft's inequality and the universal measure

**Theorem 6.1 (Kraft's Inequality).** *If `A ⊆ Σ*` is prefix-free, then*

```
    Σ     2^{-|x|}  ≤  1.
  x ∈ A
```

*Proof.* For each `x ∈ A`, let `R_x ⊆ [0,1]` be the dyadic interval whose binary expansion starts `0.x…`. Then `|R_x| = 2^{-|x|}`, and `R_x ∩ R_y = ∅` whenever `x ≠ y` both lie in a prefix-free set. Sum of disjoint subsets of `[0,1]` is `≤ 1`. ∎

**The universal semicomputable measure.** Define `μ(x) := 2^{-K(x)}`. Then `μ : Σ* → [0,1]` and `Σ_x μ(x) ≤ 1` by Kraft's inequality. Shorter descriptions have heavier weight.

`μ` is **semicomputable**: there is a computable `f(x, k)`, nondecreasing in `k`, with `lim_{k→∞} f(x,k) = μ(x)`. (Enumerate descriptions of `x` in increasing length; never decrease the weight.) `μ` is universal for the semicomputable measures in the following sense:

**Fact 6.2 (universal dominance).** *Let `τ : Σ* → [0,1]` be any semicomputable function with `Σ_x τ(x) ≤ 1`. Then there is a constant `c` such that `τ(x) ≤ c · μ(x)` for all `x`.*

**Theorem 6.3 (worst-case = average-case under `μ`).** *Let `T(x)` be the running time of some algorithm on input `x`. Set*

```
T_w(n) = max_{x ∈ Σ^n} T(x),
T_ave(n) = (Σ_{x ∈ Σ^n} μ(x) T(x)) / (Σ_{x ∈ Σ^n} μ(x)).
```

*Then `T_w(n) = O(T_ave(n))`.*

*Proof sketch.* Let `μ(n) := Σ_{x ∈ Σ^n} μ(x)`. Fortnow defines a distribution `μ'` that places all of `μ(n)` on the lexicographically first length-`n` string attaining `T_w(n)`. Universal dominance for `μ` gives `μ'(x) ≤ c μ(x)`, from which `μ(n) T_w(n) ≤ c Σ_{x ∈ Σ^n} μ(x) T(x)` and hence `T_w(n) = O(T_ave(n))`. ∎

---

## §7. Time-bounded Kolmogorov complexity

*(Fortnow attributes §7 to Buhrman–Fortnow–Laplante 2001 and Buhrman–Laplante–Miltersen 2000.)*

**Definition.** For a time function `t`,

```
C^t_f(x|y) = min{|p| : f(p, y) = x using time ≤ t(|x| + |y|)}.
```

Convention: `∞` if no such `p`.

**Fact 7.1 (universality with `log`-slowdown).** *There is a computable `g` such that for every computable `f` and every time-constructible `t` there is a constant `c` with `C^{t log t}_g(x|y) ≤ C^t_f(x|y) + c`.* Define `C^t(x|y) := C^t_g(x|y)`.

**Distinguishing variant.** A program `p` **distinguishes** `x` (given `y`) if `f(p, y, x) = 1`, `f(p, y, z) = 0` for all `z ≠ x`, and every `f(p, y, z)` uses time `≤ t(|y| + |z|)`.

```
CD^t_f(x|y) = min{|p| : p distinguishes x given y at time bound t}.
```

**No-time-bound case.** `C(x|y) ≤ CD(x|y) + O(1)`: given a distinguishing program `p`, search for the first `z` with `f(p,y,z) = 1`; by the uniqueness clause, `z = x`.

**Polynomial-time case.** The search step costs exponential time. The forward direction remains:

```
(∀ poly p)(∃ poly q)(CD^q(x|y) ≤ C^p(x|y) + c).
```

*(Given a generating program, a distinguishing program just generates and compares.)*

The reverse direction is the hard one.

**Theorem 7.2.** *The statement*

```
(∀ poly p)(∃ poly q)(C^q(x|y) ≤ CD^p(x|y) + c log|x|)
```

*is equivalent to*

> *"There is a polynomial-time computable function `f` such that for all formulas `φ` with exactly one satisfying assignment, `f(φ)` outputs that assignment."*

*The existence of such an `f` is thought to be very unlikely; indeed, it is thought to be only slightly weaker than `P = NP`.*

---

## §8. Sizes of sets

From Theorem 3.1: if `A` is c.e., `(∀x ∈ A ∩ Σ^n)(C(x|n) ≤ log|A ∩ Σ^n| + O(1))`. In general enumeration can take a long time; the time-bounded version requires `CD`, not `C`.

**Theorem 8.1.** *For `A ∈ P`, there exist a polynomial `p` and constant `c` such that*

```
(∀x ∈ A ∩ Σ^n)(CD^p(x) ≤ 2 log|A ∩ Σ^n| + c log n).
```

**Sharpness remarks.** Fortnow says the exact sharpness of the `2 log` term is unknown. He records a relativized lower bound of the same `2 log` form for suitable `A ∈ P^B`, so the theorem is tight as far as current relativizing techniques go. He also notes that if `P = NP`, then polynomial-time `C` and `CD` essentially coincide and one gets a `log|A ∩ Σ^n| + c` bound.

**Theorem 8.2.** *For `A ∈ P` and `δ < 1`, there are a polynomial `p` and constant `c` such that for a `δ`-fraction of the strings in `A ∩ Σ^n`,*

```
CD^p(x) ≤ log|A ∩ Σ^n| + log^c n.
```

**Hashing sketch for 8.1.** Fortnow motivates the proof by asking for a hash `h : Σ^n → Σ^{2 log n}` that is injective on `A`; if such an `h` is available, an element of `A` can be distinguished by its hash value. The actual lemma stated in the notes is: if `{x_1, …, x_d} ⊆ {1, …, 2^n}`, then there is a prime `p ≤ 4 d n^2` such that `x_i ≠ x_j mod p` for `i ≠ j`; take `h_p(x) = x mod p`. The method is non-uniform.

**Theorem 8.3 (Sipser [4]).** *For `A ∈ P`, there are a polynomial `q` and constant `c` such that, for all `n` and most strings `r` of length `q(n)`,*

```
(∀x ∈ A ∩ Σ^n)(CD^q(x | r) ≤ log|A ∩ Σ^n| + c log n).
```

**Valiant–Vazirani.** *There is a randomized polynomial-time reduction `φ ↦ ψ` such that: if `φ` is unsatisfiable then `ψ` is; if `φ` is satisfiable then `ψ` has exactly one satisfying assignment with probability `≥ 1/|φ|^k`.*

*Proof sketch (Fortnow).* Let `A` be the satisfying assignments of `φ`. Pick `r` and a `CD` program `p` at random. With probability `≥ 1/|φ|^k`, `p` is a `CD` program for some satisfying assignment of `φ`. Let `ψ` encode whether `p` and `r` accept some satisfying assignment of `φ`. If `p` is such a `CD` program, then `ψ` has exactly one solution. ∎

---

## §9. P-printable sets

**Definition.** `A ⊆ Σ*` is **P-printable** if there is a poly-time `f : ℕ → 2^{Σ*}` with `f(n) = A ∩ Σ^n`. P-printable implies sparse (polynomially many elements of length `≤ n`); whether all sparse sets in `P` are P-printable is open (Fortnow: "thought not to hold").

**Characterization.** For `k ≥ 1`, let `B_k = {x : C^{n^k}(x) ≤ k log|x|}`. Each `B_k` is P-printable (enumerate all programs of length `≤ k log n`, run each for `n^k` steps).

**Theorem 9.1.** *For all `A` in `P`, `A` is P-printable iff `A ⊆ B_k` for some `k`.*

*Proof sketch.* `(⇐)` clear. `(⇒)`: if `A` is P-printable, the runtime to print `A ∩ Σ^n` is bounded by `n^k` for some `k`; each `x = x_j` with `j ≤ n^k` is describable by its bit-position in `k log n` bits in polynomial time. ∎

---

## §10. Notes and references

Fortnow recommends Li & Vitányi [3] as the standard reference and says the material in §7 comes from [1] and [2].

**References (as Fortnow gives them):**

1. H. Buhrman, L. Fortnow, S. Laplante. "Resource-bounded Kolmogorov complexity revisited." *SIAM Journal on Computing*, 2001. *(To appear at the time of Fortnow's notes.)*
2. H. Buhrman, S. Laplante, P. Miltersen. "New bounds for the language compression problem." *Proceedings of the 15th IEEE Conference on Computational Complexity*, pages 126–130. IEEE Computer Society, Los Alamitos, 2000.
3. M. Li and P. Vitányi. *An Introduction to Kolmogorov Complexity and Its Applications.* Graduate Texts in Computer Science, Springer, New York, second edition, 1997.
4. M. Sipser. "A complexity theoretic approach to randomness." *Proceedings of the 15th ACM Symposium on the Theory of Computing*, pages 330–335. ACM, New York, 1983.
