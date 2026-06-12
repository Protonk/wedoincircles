# FLOOR-FORMULA-CONTRACT

Reader contract for `δ_min(P) = (5π − 1) · Δ_{n_P}` in `paper/FFT-CLASS-IMPOSSIBILITY-PAPER.md`. Governs the abstract, §1, Proposition F's home, and the coda. Binding on the refactor's staging pass (PAPER-REFACTOR-PLAN S1/S2) and on all later prose.

## Status derivation (why the contract reads as it does)

The formula's epistemic status is a four-link chain, each link with a different strength:

1. **In-construction inequality — proved, unconditionally.** On the constructed boundary object, `δ_Z(z) ≥ |Δ_{n_P} − 5π · Δ_{n_P}| = (5π − 1) · Δ_{n_P}` at substrate-side points is arithmetic of the rescaled-spread form (`measure/ENDPOINT-COMMITMENT.md`). No hypothesis needed. But it is a theorem *about the constructed object*.
2. **The constant is route-committed, not canonical.** `r_rc = 5π` is the worked overhead of the chained Sobolev → geometric conversion route (`iso/THREE-REGISTER-SYNTHESIS.md` Claim 1), committed as the morphism normalization (`measure/CURRENCY-MORPHISMS.md`). The direct constant `4π` is provably best on its side; the chained constant is best *known*, not proved optimal. A better chain would move the value. **The floor's positivity is invariant under any positive rescaling; only its value is normalization-dependent.**
3. **Operational meaning is conditional.** Reading `δ_Z` as "cost an algorithm actually pays" rides on the committed operational cost-norm (a definitional choice) plus inputs (H1) and (H2). Without them the inequality is geometry of the object, not a statement about computation.
4. **Coordinate-invariance is open.** Whether all reasonable δ-coordinates yield the same floor region is the cross-chart invariance question (SCAFFOLD ledger #15), explicitly absorbed into the recursion-theoretic horizon. The paper's own position: the result holds on the committed coordinate; the invariant lift is future work.

## Classification (the question's three options, answered)

The *inequality* is a **conditional theorem in a committed coordinate** — not a bare theorem (link 3), not a conjecture (link 1 is proved). The *geometric reading* — "the cost of trading the circle's algebra against the polygon's geometry is the discretization's isoperimetric deficit" — is a **named identification**: call it **the Deficit Identification**, with status stated wherever it appears at full strength. Two registers, never blurred:

- the inequality: "Theorem, on the committed cost coordinate, conditional on (H1)/(H2) for its operational reading."
- the identification: "a structural identification the construction makes precise; exact on the committed coordinate, with coordinate-invariance open."

## Site-by-site register

| Site | Register | Form |
|---|---|---|
| Abstract | one sentence, fully fenced | formula + "on the committed cost coordinate" + "conditional on two named inputs" |
| §1 (informal statement) | labeled informal | "Theorem (informal)" with the conditionality sentence adjacent; the Deficit Identification named, with its status clause in the same breath |
| §5 (Proposition F) | the citable statement | full conditioning as already written (currency-by-currency under (H2); per-currency values awaiting rescaling forms) |
| §8 (coda) | the emblem | may be lyrical; must not upgrade — "the identification the construction makes precise," not "the fact we proved" |

The formula appears at these four sites and **nowhere else** (PAPER-REFACTOR-PLAN C2 budget).

## Allowed phrasings (use these or equivalents no stronger)

- "On the committed cost coordinate, any FFT-style method achieving `T(P)` pays `δ ≥ (5π − 1) · Δ_{n_P}`; the operational reading is conditional on inputs (H1) and (H2)."
- "The floor's positivity is robust to the choice of morphism normalization; its value is that of the best known conversion route."
- "The Deficit Identification: the construction prices the mult/add conversion at size `n` by the isoperimetric deficit of the regular `n`-gon — exactly, on the committed coordinate."
- "Strict descent below `T(P)` would require this floor to vanish; it is positive for every `n ≥ 3`."
- (coda register) "The frontier sits where the polygon falls short of the circle — on the coordinate this paper commits to and audits."

## Forbidden overclaims

- ✗ "We prove that any FFT algorithm must pay `(5π − 1) · Δ_n`" — unqualified; drops links 3 and 4.
- ✗ "The complexity of the FFT is geometric" as established fact — the identification is coordinate-relative until cross-chart invariance lands.
- ✗ Any phrasing treating `5π` as canonical or optimal — it is the committed normalization from the best known route.
- ✗ Stating the formula without the word "coordinate" or an equivalent fence anywhere in the same passage.
- ✗ Letting the abstract or §1 imply the floor is currency-by-currency *quantitatively* — per-currency values await the rescaling forms; only positivity is currency-uniform.

## Forbidden underclaims

- ✗ "We conjecture δ_min = (5π − 1) · Δ_{n_P}" — the in-construction inequality is proved; calling it a conjecture wastes link 1.
- ✗ Burying the formula in a remark — the geometric bet is committed (refactor plan, risk 1); the contract fences it, it does not hide it.

## Upgrade triggers (loosen the contract if and only if)

1. (H1) and (H2) land → drop "conditional on two named inputs"; keep the coordinate fence.
2. Per-currency rescaling forms land → currency-by-currency quantitative phrasing permitted.
3. A cross-chart invariance result (any non-trivial class of coordinates) → the Deficit Identification may be stated as coordinate-robust over that class, named.
4. A better chained route than `5π` → the value updates everywhere from one constant; the contract's structure is unchanged (this is why the contract never lets the *value* carry rhetorical weight the *positivity* should carry).
