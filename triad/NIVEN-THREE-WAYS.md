# NIVEN-THREE-WAYS

The first concrete test of the triad discipline (BIND, CREATI, PERMEATE) on a theorem whose answer is already known. The point of the exercise is not to prove Niven's theorem — that's done — but to check whether three *routes to it* land cleanly in the three disciplines' primitives, without any leg needing to reach across for foreign vocabulary. If they do, the discipline split is natural for this problem class and the triad can be trusted to do real work on the harder circle-side residue. If one route refuses to sit in its assigned discipline, that refusal names exactly where the disciplines aren't yet sharp enough. For the abstract pattern this test instantiates, see `triad/TRIAD-ABSTRACT-PATTERN.md`.

---

## Why Niven is the right first test

Niven's theorem states that for rational q, cos(qπ) is rational only when cos(qπ) ∈ {0, ±1/2, ±1}. Equivalently: 2cos(2π/n) is an integer only for n ∈ {1, 2, 3, 4, 6}. Equivalently: the circle-side residue τ(n) = 2cos(2π/n) − round(2cos(2π/n)) is zero exactly on the crystallographic set.

This equivalence means Niven's theorem isn't adjacent to the NGON-WHOLENESS program — it **is** the base case of it. τ was defined to measure "how far is the rotation's trace from being an integer." Niven classifies exactly where that distance is zero. Every later statement about τ(n) for n outside {1, 2, 3, 4, 6} is a statement about the non-zero regime of an object whose zero set is determined by Niven.

The theorem has two standard algebraic proofs and an obvious PERMEATE-style attack. Nothing in this document is new mathematics. What's being tested is the triad claim — that the algebraic proofs live natively in two different disciplines, and that the PERMEATE attack exposes exactly what a saturation-first leg can and cannot do on its own.

## The three routes, assigned

### CREATI proof: explicit minimal polynomial

**Primitives used.** 2cos(2π/n) is an algebraic integer (the sum of a primitive n-th root of unity and its conjugate), closed-form via ζ_n + ζ_n^{-1}. Its minimal polynomial over ℚ has degree φ(n)/2 for n ≥ 3 (catalog item 9 in `triad/plus_ultra/Creati/CREATI-THE-CIRCLE.md`). An algebraic integer that is rational must be an integer (standard). An integer x satisfying |x| ≤ 2 is in {-2, -1, 0, 1, 2}.

**Proof.** Suppose 2cos(2π/n) is rational. Since it's an algebraic integer, it's an integer. Since |2cos(2π/n)| ≤ 2, it's in {-2, -1, 0, 1, 2}. Solve 2cos(2π/n) = k for k in each of the five values, reading off n from cos(2π/n) = k/2. k = 2 gives n = 1. k = 1 gives n = 6. k = 0 gives n = 4. k = -1 gives n = 3. k = -2 gives n = 2. No other n satisfies 2cos(2π/n) ∈ ℤ.

**Why this is CREATI-native.** Every object is constructed and catalogued before use. 2cos(2π/n) has its minimal polynomial written down. The degree φ(n)/2 is closed-form on prime factorization. The set {-2, -1, 0, 1, 2} is an enumeration. The five values of n are exhibited one at a time. There is no limiting process, no analytic continuation, no existential step that isn't immediately matched by a construction. The proof terminates when the catalog is exhausted.

**Did it reach across?** No. Every primitive is in the CREATI catalog (items 7, 8, 9) already. The proof can be written without reference to any BIND or PERMEATE primitive.

**Equivalent CREATI route via Chebyshev.** A second CREATI proof, equally native, uses the scaled Chebyshev polynomial

$$
P_q(x) = 2\,T_q(x/2),
$$

which is monic with integer coefficients and degree q. Take $t = (p/q)\pi$ in lowest terms; then

$$
P_q(2\cos t) = 2T_q(\cos t) = 2\cos(qt) = 2\cos(p\pi) = \pm 2.
$$

So $2\cos t$ is a rational root of the monic-ℤ polynomial $P_q(x) - (\pm 2)$. Integer Root Theorem forces it to be an integer; $|2\cos t| \le 2$ forces it into $\{-2, -1, 0, 1, 2\}$. This is the route the Mizar formalization of Niven's theorem takes (proposition 52 onward; see `memos/MIZAR-NIVEN-FOREBODING.md`). Both routes are CREATI-native; they differ only in which monic-ℤ polynomial is named first.

### BIND proof: Galois orbit size

**Primitives used.** The Galois group Gal(ℚ(ζ_n)/ℚ) acts on $\zeta_n + \zeta_n^{-1}$ with orbit of size $\varphi(n)/2$ for $n \ge 3$. Galois conjugates of a rational number are equal to it. Therefore a rational $2\cos(2\pi/n)$ has Galois orbit of size 1.

**Proof.** Since

$$
2\cos(2\pi/n) = \zeta_n + \zeta_n^{-1},
$$

if $2\cos(2\pi/n) \in \mathbb{Q}$, then its Galois orbit has size 1. But for $n \ge 3$ that orbit has size $\varphi(n)/2$, so $\varphi(n)=2$. The solutions to $\varphi(n) = 2$ are $n = 3, 4, 6$. Handle $n = 1, 2$ separately.

**Why this is BIND-native.** Galois theory is a primitive internal to the algebraic-number side. Nothing is imported from a circle or a rotation or a trigonometric identity; $2\cos(2\pi/n)$ is treated as an algebraic number and the proof works at the level of field extensions. The argument never leaves $\mathbb{Q}(\zeta_n)$. There's no trigonometry in the proof — $2\cos(2\pi/n)$ is a name for $\zeta_n + \zeta_n^{-1}$, and the proof operates on the root of unity directly.

**Did it reach across?** Almost no. The one place it comes close is the assertion that 2cos(2π/n) has orbit of size φ(n)/2, which requires knowing that ζ_n has φ(n) conjugates and that complex conjugation halves the orbit. Complex conjugation is a geometric operation on ℂ, which could be read as importing from the circle side. But in practice it's treated as an involution on ℚ(ζ_n) fixing ℝ, which is internal to the field-theoretic primitives. No reach-across of serious weight.

### PERMEATE proof: small-case saturation plus growth

**Primitives used.** A finite tabulation of $2\cos(2\pi/n)$ for small $n$, identifying which values are rational. An asymptotic growth statement saying that for large $n$,

$$
2\cos(2\pi/n)=2-\frac{4\pi^2}{n^2}+O(n^{-4}),
$$

so the tail approaches $2$ from below with a rigid shape. This does not close the proof by itself; it identifies the form of any possible tail counterexample.

**Proof-attempt / attack (not a standalone proof).** Tabulate $2\cos(2\pi/n)$ for $n = 1, 2, \dots, 12$:

| n | 2cos(2π/n) | rational? |
|---|---|---|
| 1 | 2 | yes |
| 2 | −2 | yes |
| 3 | −1 | yes |
| 4 | 0 | yes |
| 5 | (√5 − 1)/2 | no |
| 6 | 1 | yes |
| 7 | ≈ 1.247 | no |
| 8 | √2 | no |
| 9 | ≈ 1.532 | no |
| 10 | (1 + √5)/2 | no |
| 11 | ≈ 1.683 | no |
| 12 | √3 | no |

The rational cases in the saturated range are exactly $\{1, 2, 3, 4, 6\}$. For large $n$ one also has the asymptotic

$$
2\cos(2\pi/n) = 2 - \frac{4\pi^2}{n^2} + O(n^{-4}),
$$

so the tail is monotone up toward $2$ and, from $n \ge 7$ onward, stays strictly between $1$ and $2$. This means the table strongly predicts "no new zeroes of $\tau$ will appear."

What this does **not** do by itself is prove irrationality in the tail. Closeness to $2$ does not bound rational denominators, and the asymptotic alone does not rule out rational nonintegers. To close the tail rigorously one imports a CREATI lemma — either the algebraic-degree fact $\deg = \varphi(n)/2 \ge 2$ for $n \ge 7$, or the algebraic-integer $\Rightarrow$ integer step. So the PERMEATE move here is: saturate the table, narrow the shape of any possible counterexample, then ask CREATI for the tail-closing lemma.

**Why this is PERMEATE-native as an attack.** The move is grounded in the tabulation, and the matching rule is "which $n$ produce integer values of $2\cos(2\pi/n)$." The saturation gives the conjectural zero set immediately, and the asymptotic explains what any tail counterexample would have to look like: a nonintegral rational value in $(1, 2)$ converging to $2$.

**Did it reach across?** Yes, decisively. The tail-closing step is not PERMEATE-native. Strict PERMEATE can saturate the table and motivate the conjecture; it cannot, on saturation alone, prove that no rational noninteger value ever appears in the tail. The rigorous closing step is exactly the point where CREATI has to supply a lemma.

This is the first finding from the test. It's not a failure of the triad; it's a specification. PERMEATE-proper cannot finish Niven on saturation alone. It can generate the right conjecture very cheaply and identify the form of the tail obstruction, but it needs a supplied arithmetic lemma from CREATI to turn that attack into a proof. Two of the three disciplines are self-contained on this problem; the third is productive but not closed.

## What the test shows

Two complete proofs exist here, and the third leg contributes a genuine attack rather than a closed proof. The reach-across is in the expected direction: PERMEATE's tail-closing needs a closed-form arithmetic lemma, which is exactly the kind of complementarity the triad was designed to expose.

The design of the triad — three different productive constraints on what counts as a move — still works here. BIND finishes Niven without arithmetic tabulation. CREATI finishes Niven without analysis. PERMEATE does not finish Niven on tabulation alone, but it does produce the right conjecture, the right small-case table, and the right question to hand off. This is the complementarity lemma at its smallest scale: PERMEATE reaches what CREATI can't (the saturation picture itself, which CREATI would regard as beneath its notice), and CREATI reaches what PERMEATE can't (an infinite tail closed by a closed-form lemma).

The pattern to watch for on the full τ-problem: the same loan structure — PERMEATE tabulates, hits a horizon, CREATI supplies a closed-form tail bound, BIND supplies the domain-internal argument that the tail bound is sharp — is likely to recur. Niven is the case where it happens in one step. Later cases will have more steps, but the shape of the cooperation should be recognizable.

## Consequences for the program

Three small consequences for the doc set.

**`tangencies/WHOLENESS.md`.** The $\tau(n) = 0$ set is $\{1, 2, 3, 4, 6\}$ by Niven's theorem; this is worth stating explicitly in section §C1 (where $\tau$ is defined in the CREATI catalog of `triad/plus_ultra/Creati/CREATI-THE-CIRCLE.md`). What this note adds is not three independent closed proofs, but two independent algebraic proofs plus one saturation-first route that lands on the same set and exposes exactly where the tail has to be closed.

**`triad/plus_ultra/Creati/CREATI-THE-CIRCLE.md`.** The CREATI proof of Niven is literally catalog item 7 + catalog item 9 + the {-2,-1,0,1,2} enumeration. This can be added as a worked example of what a CREATI result looks like at the "closed-form result" admissible shape. Useful as a template.

**`triad/plus_ultra/Eraserhead/BIND-THE-CIRCLE.md`.** The Galois-orbit proof is the cleanest example of a BIND argument that stays entirely inside the algebraic-number-theory primitives without touching τ_c or the continuous-E tool. It's a reminder that BIND has discrete primitives available (Galois theory of cyclotomic fields) and isn't committed to analytic ones. Worth noting as a vocabulary check: when BIND uses Galois theory on ℚ(ζ_n), it's operating in primitives that are native to the circle-side algebraic structure but don't require importing anything from the log side. Erasure holds.

## What this previews about F

The CREATI and BIND proofs both rest on circle-side algebraic structure — cyclotomic minimal polynomials, scaled Chebyshev polynomials, Galois orbits in $\mathbb{Q}(\zeta_n)$. These are facets of one underlying fact: the circle side carries a native $\mathbb{Z}[x]$-closure, generated either by the trace identity

$$
2\cos(nt)=P_n(2\cos t), \qquad P_n(x)=2T_n(x/2),
$$

or by the cyclotomic structure $\zeta_n + \zeta_n^{-1}$.

Landfall §2 (see `memos/LANDFALL-EXPORT.md`) argues that the log-side analog of this closure is Aff⁺(ℝ): the machine's mantissa operations generate affine maps x ↦ ax + b, and composition stays affine. The log side has no native ℤ[x]; its operational closure is capped at degree 1.

So Niven's clean circle-side proof has no log-side analog. The arithmetic restriction (rational ⇒ integer for 2cos at rational angles) is a consequence of the circle's polynomial closure, and the log side lacks the closure that would generate an analogous restriction. PERMEATE Leg 2's predicted n = 7 break sits in the same family: the first integer where the circle-side polynomial structure (via ψ from Bamberg–Cairns–Kilminster) reaches a prime outside the log rep's support — a specific arithmetic witness of the same closure mismatch.

This is preview, not result. A structural F-non-existence statement still requires a precise category-theoretic framing of "native functor" and the acknowledgment that F may still exist as a non-native matching (which is what each leg of the triad is independently testing). What Niven gives us is the cleanest first instance of the closure-mismatch shape on a problem whose answer is already known, together with a visible example of where a saturation-first attack runs out of room and asks an algebraic leg to finish the job.

## What this test does not establish

Whether the triad generalizes past Niven. τ(n) = 0 is a yes/no question; τ(n) for n outside the zero set is a real-valued question with infinite complexity, and the triad might behave differently when asked to produce bounds or structural theorems about non-zero values. The success at Niven is evidence that the disciplines are natively separated for this problem class; it is not evidence that they will finish the full τ question with the same clean complementarity.

What the Niven test does is put the burden of proof in the right place: if someone claims the triad split is artificial for the circle-side program, they now have to explain why it works this cleanly on the program's base case. The default assumption — disciplines aligned with natural proof-styles — gets to stand.
