# LINDEMANN-BRIEF

A source-extraction memo on Lindemann's 1882 transcendence of π, its Weierstrass-1885 generalization (Lindemann–Weierstrass), and the relationship to the program's compute-cost ambition at `memos/COUNTING-APPARATUS.md`.

The brief has a second, harder job: to identify exactly when invoking Lindemann–Weierstrass in our arguments is safe, when it is programmatically weak, and when it is strictly circular. The program aims at a theorem that would *uphold* Lindemann–Weierstrass for the specific constants e and π, so using Lindemann–Weierstrass as a tool — rather than as a background fact — has to be done carefully.

**Confidence level of this read.** High on the classical statements (Hermite 1873, Lindemann 1882, Weierstrass 1885, Schanuel conjecture) — these are standard textbook material, cross-checked against multiple sources. Medium on the circularity analysis — that is the brief's own contribution and is open to refinement as the program's compute-cost argument takes shape.

---

## The theorem, precisely

**Lindemann–Weierstrass, Form A.** If α₁, …, αₙ are distinct algebraic numbers, then e^{α₁}, …, e^{αₙ} are linearly independent over the algebraic closure ℚ̄ of ℚ.

**Form B (equivalent).** If β₁, …, βₙ are algebraic numbers that are linearly independent over ℚ, then e^{β₁}, …, e^{βₙ} are algebraically independent over ℚ.

**Baker's version (equivalent).** For algebraic β₁, …, βₙ and distinct algebraic α₁, …, αₙ,
β₁ e^{α₁} + ⋯ + βₙ e^{αₙ} = 0 iff all βᵢ = 0.

## How the classical corollaries drop out

**e transcendental** (Hermite 1873, subsumed into Lindemann–Weierstrass). From Form A with α₁ = 0, α₂ = 1 distinct algebraic: 1 and e are ℚ̄-linearly independent, hence e ∉ ℚ̄.

**π transcendental** (Lindemann 1882). Suppose π algebraic. Then iπ is algebraic and nonzero. By Form B applied to the ℚ-linearly-independent set {iπ}, e^{iπ} is transcendental. But e^{iπ} = −1 is rational. Contradiction.

**Others.** e^α transcendental for every algebraic α ≠ 0; sin α, cos α, tan α transcendental for algebraic α ≠ 0; log α transcendental for algebraic α ≠ 0, 1. Each via Form A or Form B on an appropriate set.

## What Lindemann–Weierstrass does not settle

It establishes transcendence of e and π **individually**. It does **not** establish their algebraic independence over ℚ. Whether a non-trivial polynomial P(x, y) ∈ ℚ[x, y] exists with P(e, π) = 0 is an open problem. Stronger: it is not even known whether e + π is irrational.

**Schanuel's conjecture** (Stephen Schanuel, 1960s): if α₁, …, αₙ are complex numbers linearly independent over ℚ, then at least n of α₁, …, αₙ, e^{α₁}, …, e^{αₙ} are algebraically independent over ℚ.

Schanuel implies algebraic independence of e and π as a special case. Take α₁ = 1, α₂ = iπ — linearly independent over ℚ (since π is irrational by Lambert 1761). Schanuel gives: at least 2 of {1, iπ, e, e^{iπ} = −1} are algebraically independent over ℚ. Since 1 and −1 are rational, the two independent ones must be iπ and e. Hence e and π are algebraically independent.

**The logical geography**, bottom to top:

- **Proven (Lindemann–Weierstrass, 1885):** e, π each transcendental.
- **Open (our target):** e, π algebraically independent over ℚ — equivalently, no non-trivial P(x,y) ∈ ℚ[x,y] with P(e,π) = 0.
- **Open (Schanuel, conjectured):** the general algebraic-independence statement of which our target is a special case.

The program's ambition sits in the middle open region — strictly stronger than Lindemann–Weierstrass, strictly weaker than Schanuel.

---

## The circularity risk

The program's target theorem (computational-impossibility route to algebraic independence of e and π) would imply:

1. Algebraic independence of e and π (tautologically).
2. e, π each transcendental (corollary of 1 — if either were algebraic, a relation with the other would exist).
3. Hence, Lindemann–Weierstrass for these two specific constants.

So the target *upholds* Lindemann–Weierstrass in that restricted sense. This is the framing that makes the circularity question live.

**When invoking L–W is clean.**

*Use as background fact, motivation, sanity check, or weakly-implied benchmark.* E.g., "Lindemann established π transcendental; our quantitative compute-cost result should refine this qualitative fact into an explicit cost lower bound." No circularity: L–W has its own proof (Hermite's method, 1873–1882), independent of our argument.

*Use as a strictly weaker lemma.* Our target is strictly stronger than L–W for these constants. Using L–W as an intermediate step is valid — it is using a known weaker theorem to reach an unknown stronger one. Not circular.

**When invoking L–W is programmatically weak.**

*Aesthetic / narrative concern.* If L–W does most of the visible work in the argument and the compute-cost machinery is decorative, the paper's claim collapses from "new independence result for e and π" to "quantitative version of a known qualitative result." Not formally circular, but the program's novelty evaporates. Watch for this in drafts: count how much of the argument's force depends on invoking π transcendental vs. on the compute-cost construction.

**When invoking L–W is strictly circular.**

*Claiming L–W as an output.* If the paper says "our compute-cost theorem gives a new proof of Lindemann–Weierstrass (for e and π) as a corollary," then invoking L–W in the proof of the compute-cost theorem is formally circular. Avoid any phrasing that sells L–W as a downstream deliverable.

*Essential use of post-L–W transcendence results where their own proofs go through L–W.* Gelfond–Schneider (1934), Baker's theorem (1966), and Nesterenko (1996) all live downstream of L–W in transcendence theory. Using them "essentially" in our argument inherits L–W's role. If used, invoke only the statement, never the proof; and check whether the statement itself is needed for the compute-cost story or whether a strictly pre-L–W substitute exists.

---

## Pre-Lindemann tools (safe to use)

Classical results independent of Lindemann–Weierstrass, available to the program without circularity risk:

- **Lambert 1761**: π is irrational.
- **Euler (18th century)**: e is irrational.
- **Gauss–Wantzel (1796, 1837)**: the regular n-gon is ruler-and-compass constructible iff n = 2^a × (product of distinct Fermat primes). Directly load-bearing for `corners/PSEUDO-CHEBYSHEV-NODES.md` §Constructibility and for `memos/COUNTING-APPARATUS.md` item (A) compute-model choice.
- **Wantzel 1837**: constructible numbers form a tower of degree-2 extensions of ℚ, hence are algebraic of degree 2^k. The ruler-and-compass depth bound.
- **Cyclotomic polynomial theory** (Gauss): Φ_n(x) has degree φ(n); 2cos(2π/n) has minimal polynomial of degree φ(n)/2 over ℚ for n ≥ 3. Load-bearing for `COUNTING-APPARATUS.md` item (C) τ-portrait.
- **Galois theory of cyclotomic extensions** (Gauss, Galois): Gal(ℚ(ζₙ)/ℚ) ≅ (ℤ/nℤ)*. Structural spine of the τ algebraic-depth catalog.

Everything the program does at finite algebraic depth — the counting apparatus, the pseudo-Chebyshev algebraic-degree growth, the τ zero-set classification, the n = 7 small-case walkthrough at `COUNTING-APPARATUS.md` item (D) — lives in this pre-Lindemann regime.

## Post-Lindemann tools (use with explicit care)

- **Gelfond–Schneider (1934)**: if α, β algebraic with α ≠ 0, 1 and β irrational, then α^β transcendental. Gives transcendence of 2^√2, e^π (via Hilbert's 7th), others. Proof technique is distinct from L–W but often chains with it. Treat as L–W-adjacent — flag any essential use.
- **Baker's theorem (1966)**: linear forms in logarithms of algebraic numbers, with effective bounds. Used in `memos/BIDDER-AND-SON.md` §"Open question" for the son's-nine-constants closure question. Baker's proof technique builds on L–W-style Hermite interpolation; its dependence on L–W proper is partial but material.
- **Nesterenko (1996)**: π and e^π are algebraically independent (proved, not conjectural). Descends from Gelfond–Schneider; does not settle algebraic independence of e and π, which remains open.

None of the above settle algebraic independence of e and π. That's still Schanuel territory.

---

## What the program can state without invoking Lindemann

The sharpest pre-L–W statement the program can aim for, based on current material:

> In a fixed compute model (e.g., algebraic-arithmetic over ℚ or an algebraic straight-line program model), computing 2cos(2π/n) to algebraic-depth φ(n)/2 requires Ω(g(n)) primitive operations, for an explicit g(n) tied to the counting apparatus's |M_N| growth at resolution N.

This is a compute-cost lower bound over the algebraic regime. It does not invoke transcendence of π or of any e^α. It provides the Inscription §§1/4 hardening that `BNHA/triad/Creati/INSCRIPTION-PAPER-PLAN.md` currently softens.

Extending that statement to π itself — "computing π to precision ε requires Ω(h(ε)) operations" — probably requires a transcendence-or-adjacent input somewhere. That extension is the place where L–W-safety needs to be checked line by line, and the extension should state the dependency explicitly rather than silently invoking L–W.

The strongest form of the program's ambition — "no non-trivial algebraic relation between e and π, from a compute-cost obstruction" — is where the circularity risk becomes acute. Any proof of that statement has to be pre-L–W at the core, with L–W entering only as a sanity check at the boundaries.

---

## Historical notes

- **Hermite 1873**: "Sur la fonction exponentielle." First transcendence result: e transcendental. The proof method (now called Hermite's method, using integral representations of e^x) is the ancestor of all classical transcendence proofs.
- **Lindemann 1882**: "Über die Zahl π." π transcendental, via Hermite's method extended. This settled the 2400-year-old squaring-the-circle problem — Wantzel 1837 had shown constructible numbers must be algebraic of degree 2^k, so π's transcendence implies non-constructibility of a square with area π.
- **Weierstrass 1885**: Generalized Lindemann's argument to what is now the Lindemann–Weierstrass theorem.
- **Schanuel 1960s**: Conjectured the stronger algebraic-independence statement.

**"Known since antiquity" caveat.** The squaring-the-circle impossibility was *conjectured* since antiquity; it was *proved* by Lindemann in 1882 (with Wantzel's 1837 constructibility framework). The program's framing of the classical result should acknowledge this: pre-Lindemann, the problem was open, not closed.

## Standard references

- Baker, A. *Transcendental Number Theory* (Cambridge, 1975). Classical textbook.
- Murty, M. R. & Rath, P. *Transcendental Numbers* (Springer, 2014). Modern treatment with proofs.
- Mayer, S. "The Transcendence of π" (2006). Accessible self-contained write-up.
- Conrad, K. "Transcendence of e." Expository notes.
- Wikipedia: *Lindemann–Weierstrass theorem*, *Schanuel's conjecture*. Serviceable for statements; use textbooks for proofs.

---

## What this brief is not

- **Not a proof.** The brief summarizes statements and guides their use. See references for proofs.
- **Not a commitment to using L–W.** It names when L–W is safe and when it isn't; the commitment is made case-by-case.
- **Not a full transcendence-theory reference.** It covers only what's load-bearing for the program's compute-cost ambition.

---

## Exit criteria

This brief freezes when each step in the program's compute-cost argument can be tagged with one of the following:

- **Pre-L–W**: uses only Lambert / Euler / Gauss–Wantzel / cyclotomic / Galois tools. Clean.
- **L–W as background**: invokes π transcendental (or e transcendental) as a known fact, but not essentially — the argument's force is elsewhere. Clean.
- **L–W essential**: the argument depends on L–W in a load-bearing way. Flag. Check whether a pre-L–W substitute exists.
- **Circular**: the argument purports to derive L–W (or a consequence the target implies) while invoking L–W as a step. Refactor.

Promotion: once the Inscription §§1/4 hardening in `BNHA/triad/Creati/INSCRIPTION-PAPER-PLAN.md` is drafted and each step is L–W-tagged, the content of this brief's §"The circularity risk" migrates into a methodology appendix of that paper-plan, and this brief reduces to a pointer.
