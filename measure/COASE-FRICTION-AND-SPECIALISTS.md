# COASE-FRICTION-AND-SPECIALISTS

Source-extraction memo on Ronald H. Coase, "The Nature of the Firm,"
*Economica* New Series Vol. 4 No. 16 (Nov. 1937), pp. 386–405
([sources/Coase-1937.pdf](sources/Coase-1937.pdf), JSTOR scan, 24 PDF
pages including front matter).

**Why this memo lives in `measure/`.** The brief was originally
shelved as a methodological-precedent note in `memos/`. It has been
moved here because what Coase actually supplies is a **substrate-side
posture**: the assertion that friction is a structural feature of the
world and that its algebra is empirical, plural, and locally
refinable. That posture is what lets the program assert an
impossibility region without overclaiming the algebra of `δ` as
canonical. The posture sits alongside the rest of the substrate-side
typing in `measure/`:

- [measure/SUBSTRATE-OBSTRUCTIONS.md](measure/SUBSTRATE-OBSTRUCTIONS.md)
  types the five substrate-side measure-theoretic refusals (Haar /
  three isoperimetric registers / `ζ(2)`-tail / counting-invariant /
  L-W envelope null/full).
- [measure/THE-FIRST-BRIDGE.md](measure/THE-FIRST-BRIDGE.md) names the
  bridge the program owes between `δ` as an algorithm-side coordinate
  and the substrate-side closure boundary.
- [measure/ALGEBRA-OF-DELTA.md](measure/ALGEBRA-OF-DELTA.md) is the
  Varian-style local formalization on top of the present memo: it
  picks coordinates on the substrate-side discontinuity and explores
  their algebra.

This memo is the **posture-anchor**. It is not vocabulary import; it
is the legitimization of a structural-fact-with-plural-coordinates
methodology inside a mathematical impossibility theorem.

**What was read.** Pages 386–396 of the original (first 12 pages of
the PDF including JSTOR cover and Section I + the opening of Section
II), covering Coase's setup, the price-mechanism-vs-firm distinction,
the existence-of-friction claim, the marginal condition for firm
size, the heterogeneity-of-transactions remark, and the firm-size
summary statement. Pages 397–405 (the dynamic-equilibrium and
employer-employee discussion) were not read; nothing in this memo
depends on them.

**Confidence level.** High on the four extractions in §1 — each is a
direct Coase quotation with page anchor. Medium on the program-side
posture mapping in §3: the lineage from Coase through Williamson /
Hart-Moore / Varian into the present paper is real and well-known in
economics, but its application to a mathematical impossibility theorem
is the program's own move, not Coase's framing.

**Trust boundary up front.** Coase is a 1937 economics paper read
here for *posture*, not for content transferred to the FFT
impossibility theorem. The mathematical content of the paper does not
depend on Coase having proved anything; it depends on Coase having
*named* the substrate / coordinate split the way the FFT-impossibility
argument needs it named.

---

## 1. What Coase proves

Coase argues that firms exist because **using the price mechanism has
a cost** — and derives, as a methodological consequence, that the
*size* of firms is determined by the *algebra* of that cost. Two
distinct claims, one nested in the other.

### 1.1 Existence of friction (p. 390)

> *"The main reason why it is profitable to establish a firm would
> seem to be that there is a cost of using the price mechanism. The
> most obvious cost of 'organising' production through the price
> mechanism is that of discovering what the relevant prices are."*

**For the program.** This is the bare-existence claim. Friction > 0.
Coase asserts it as a structural fact about market exchange — not as
a theorem he proves, but as a feature of the world the rest of the
paper is forced to respect. Mapping: the program's analog is the
substrate-side discontinuity at the bounded/unbounded coefficient
boundary. `δ > 0` at the boundary is the algorithm-side reading of
this substrate-side fact; Lemma B is its existence-side bookkeeping.

### 1.2 Specialists do not eliminate friction (p. 390)

> *"This cost may be reduced but it will not be eliminated by the
> emergence of specialists who will sell this information."*

**For the program.** Coase's *bypass-resistance* result.
Third-party intermediaries (specialists) can reduce friction but
cannot zero it. The cost is *substrate*, not *agent*. Reduction is
possible; elimination is not. Mapping: the program's analog is the
"smarter-FFT rebuttal" of [paper/IMPOSSIBILITY-OUTLINE.md](paper/IMPOSSIBILITY-OUTLINE.md)
§6.6 — a smarter FFT-style method does not answer the impossibility
because the friction is on the substrate, not on the algorithm. The
Coasean answer is *reduce yes, eliminate no*; the program's analog
is *redistribute or amortize yes, zero no*.

### 1.3 Marginal condition (p. 395)

> *"A firm will tend to expand until the costs of organising an extra
> transaction within the firm become equal to the costs of carrying
> out the same transaction by means of an exchange on the open market
> or the costs of organising in another firm."*

**For the program.** A *derivative* statement: firm size is fixed
where two marginal-cost curves meet. Coase explicitly needs the
*shape* of the cost function — not just its sign. Existence of
friction (the sign) is insufficient to determine the boundary; the
algebra (the derivative) is required. Mapping: the algorithm-side
shape of the impossibility region requires an algebra of `δ` (where
`δ` scales, how it amortizes, how it depends on representation). The
algebra is what locates the *boundary* of the impossibility region in
algorithm-side coordinates; it does not constitute the substrate-side
discontinuity itself.

### 1.4 Shape determines firm size (p. 396)

> *"Other things being equal, therefore, a firm will tend to be larger:
> (a) the less the costs of organising and the slower these costs rise
> with an increase in the transactions organised. (b) the less likely
> the entrepreneur is to make mistakes and the smaller the increase in
> mistakes with an increase in the transactions organised."*

**For the program.** Same friction-existence, different rate-of-rise
in the cost function → different firm boundaries. The algebra
distinguishes outcomes. Coase reads firm size off the cost function's
*derivative*, not its *value*. Mapping: the impossibility region's
shape is read off `δ`'s algebra; different reasonable algebras give
different shapes. None is canonical. This is the structural feature
the lineage Coase → Williamson → Hart-Moore → Varian has lived with
for nine decades, and the program inherits it.

### 1.5 Heterogeneity of transactions (p. 396)

> *"Up to now it has been assumed that the exchange transactions which
> take place through the price mechanism are homogeneous. In fact,
> nothing could be more diverse than the actual transactions which
> take place in our modern world. This would seem to imply that the
> costs of carrying out exchange transactions through the price
> mechanism will vary considerably as will also the costs of
> organising these transactions within the firm."*

**For the program.** Friction is *not a single number*; it is a
function of transaction type. Mapping: `δ` likely varies across
coefficient regimes, problem instances, and conversion strategies,
and this variation is what makes the impossibility region non-trivial.
Heterogeneity is an algebra-side question; the substrate-side
discontinuity persists across all transaction types.

---

## 2. What Coase states without our independent check

- The historical and bibliographic claims about prior work (Marshall
  on organisation as a fourth factor of production, J. B. Clark on
  the entrepreneur, Knight on managers, Robbins on the firm-as-related-to-network-of-prices)
  are not independently checked. The brief reports them as Coase's
  attributions.
- The economics-domain empirical claims (the Lancashire cotton
  industry's vertical-integration practices, sales-tax effects on
  firm formation) are not independently checked. The brief does not
  use them.
- The Knight 1933 quote (p. 394, "the relation between efficiency and
  size") is reproduced from Coase's footnote attribution.

The program's use of Coase is at the methodological-posture level;
none of the unchecked content is load-bearing.

---

## 3. The posture, and why it transfers

The mapping below is the brief's contribution; Coase did not write
it.

### 3.1 What Coase did, structurally

Coase noticed a fact the existing economics couldn't name: trade
through any coordination mechanism carries a non-zero, irreducible
fee. He didn't derive this; he listed examples (price discovery,
contracting, enforcement) and let the reader feel the universal that
connects them. The algebra grew on top — Williamson on asset
specificity, Hart-Moore on incomplete contracts, Grossman-Hart on
residual control rights, mechanism design more broadly. These took
roughly four decades of contact with specific institutions to build.
Each formalization captures a different shadow of the original
observation. None subsumes the others.

The standard reading among economists by now is that there is no
canonical "algebra of transaction costs"; there are multiple useful
formalizations, each tuned to a domain, each empirically calibrated
through engagement with specific contracts and industries. The
substrate-side fact is that friction exists; the algebras are local
charts.

### 3.2 The substrate / coordinate split

The split this memo identifies in Coase, and inherits for the
program, is:

| Layer | What it does | Coase precedent | Program analog |
|---|---|---|---|
| **Substrate-side fact** | Asserts a structural feature of the world that any reasonable formalism must respect. | Friction exists in market exchange (p. 390). | Algebraic-arithmetic discontinuity at the bounded/unbounded coefficient boundary, witnessed five ways at [measure/SUBSTRATE-OBSTRUCTIONS.md](measure/SUBSTRATE-OBSTRUCTIONS.md). |
| **Coordinate** | Picks a quantitative handle on the substrate-side fact. The handle is one of many; alternatives are equally legitimate. | Transaction cost as a positive scalar with an algebra (the Williamson / Hart-Moore / Varian tradition). | `δ` as a transaction-cost coordinate on the substrate-side discontinuity. The cocycle realization at [fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md) is one candidate; others are open. |
| **Algebra of the coordinate** | Specifies how the coordinate composes, scales, amortizes, depends on representation. | Williamson's TCE, Hart-Moore on incomplete contracts, Varian's microfoundations. Plural; not canonical. | [measure/ALGEBRA-OF-DELTA.md](measure/ALGEBRA-OF-DELTA.md)'s seven sub-questions. Plural; one choice among many. |
| **Result shape** | What the formalism enables you to say. | Firm boundaries, vertical integration thresholds, ownership rights. | The impossibility region's shape — which problems / thresholds sit unreachable. |

The substrate-side fact is the manifold. The coordinates chart it.
Different reasonable charts give different *parameterizations* of the
same fact. The substrate-side fact survives reformalization; the
chart does not.

### 3.3 Why this transfers

Most mathematical impossibilities don't rest on empirically-anchored
primitives — Galois insolvability, Hilbert's 10th, FLT-style results
all start from formal definitions and derive consequences without
empirical grounding. Physics has empirical impossibilities (no
perpetual motion, no superluminal information) but doesn't usually
frame them as theorems. The program is doing both: a theorem-shaped
result with a substrate-shaped primitive.

The closest precedents in CS are *random oracle model* arguments and
the *unique games conjecture* — both structural assertions defended
by track record rather than derivation, used as load-bearing
primitives in many impossibility proofs. Both leave a permanent
asterisk on the results that depend on them, but the results are
real. The program's `δ` is structurally analogous, with two
distinguishing features: `δ` is more transparently substrate-grounded
than ROM or UGC, because Coase is *explicitly* the methodological
anchor and the substrate-side witnesses are catalogued at
[measure/SUBSTRATE-OBSTRUCTIONS.md](measure/SUBSTRATE-OBSTRUCTIONS.md);
and the program has at least one proved structural reading of the
substrate-side discontinuity in the form of FOR-BREAKFAST K
([measure/FOR-BREAKFAST.md](measure/FOR-BREAKFAST.md) §The kernel),
a σ-algebra coarsening theorem with transport failure for three
concrete L-observables (cyclotomic-ladder degree, polygon perimeter,
Hurwitz isoperimetric gap). That distinguishes the δ situation
moderately from ROM/UGC's purely-track-record posture: the
substrate-side fact is not only empirically witnessed but also has
one formally-proved structural facet.

The posture is what transfers. It is what lets the paper say:
*there's a discontinuity at the boundary, the existing thresholds
sit on it, FFT-style methods cannot cross because the discontinuity
is a feature of the algebraic-arithmetic substrate.* That assertion
is not a theorem in the conventional sense. It is a Coase-style
structural claim about computation, with the algebra of `δ` as the
local chart that lets the impossibility region come into focus.

### 3.4 What this is NOT

- It is **not** a claim that the algebra of `δ` is canonical. Different
  reasonable algebras would give different impossibility-region
  shapes; all chart the same substrate-side discontinuity.
- It is **not** a claim that all reasonable `δ`-algebras yield the
  *same* impossibility region at `T(P)`. The Coase posture supports
  upstream-ness of the substrate boundary relative to any chosen
  coordinate (different shapes, same discontinuity); cross-chart
  invariance of the resulting impossibility region is a separate
  invariance theorem (T6 in
  [measure/FOR-BREAKFAST.md](measure/FOR-BREAKFAST.md) §K.6's
  notation), not entailed by the posture alone.
- It is **not** a claim that Coase derived something we are using as
  proof material. Coase asserted a structural feature of the world; he
  did not prove it.
- It is **not** vocabulary import. Vocabulary follows from the
  posture — you cannot name `δ` "the transaction cost" without first
  deciding the substrate-side discontinuity is the load-bearing
  object.
- It is **not** a claim that the impossibility theorem reduces to a
  Coase analogy. The proof skeleton (Bridge + Separation + Native
  drift) is mathematical content. Coase supplies the legitimacy of the
  framing in which that skeleton is the right shape.

---

## 4. Trust Boundary

### This memo should be cited for

- the four direct quotations at pp. 390, 395, 396 (existence,
  specialists, marginal, shape-determines-size);
- the heterogeneity remark at p. 396;
- Coase's substrate-side / coordinate-side posture as a methodological
  precedent for the program's claim that `δ` is a coordinate on a
  substrate-side discontinuity;
- the lineage Coase → Williamson / Hart-Moore / Varian as the
  standard pattern of substrate-fact + plural-coordinate work;
- the legitimacy of asserting an impossibility region whose precise
  shape is coordinate-relative but whose substrate-side discontinuity
  is not.

### This memo should NOT be cited for

- any FFT-impossibility content — Coase contains none;
- any computational-complexity content — Coase contains none;
- the claim that Coase's algebra-of-friction analysis transfers
  *as a theorem* to the program — it transfers as *posture*, not
  as proof material;
- the claim that any specific algebra of `δ` is canonical — Coase's
  own work, and the lineage that grew on top of it, treats the
  algebra as plural and locally refinable;
- the claim that all reasonable `δ`-algebras yield the same
  impossibility region at `T(P)` — that is a separate invariance
  theorem (T6) not delivered by the posture transfer;
- pp. 397–405 of the original — not read here;
- empirical economics claims — not the program's domain.

### Provenance tag for the program

**Substrate-side posture anchor.** Coase 1937 supplies the
substrate-side / coordinate-side split, the typing of friction as a
positive scalar with an algebra, the discipline of separating
existence claims from algebraic claims, and the structural claim that
the friction is on the substrate rather than on the agent. None of
these is content transfer; all are posture. Cited at
[paper/IMPOSSIBILITY-OUTLINE.md](paper/IMPOSSIBILITY-OUTLINE.md)
§1.6, §6.6, and (potentially) §Conclusion as the methodological
anchor.

---

## Closing Sentence

This memo extracts four pages of Coase 1937 (pp. 390, 395, 396) for
the substrate-side posture the FFT impossibility paper inherits at
§1: that friction exists as a structural feature of the world, that
its algebra is empirical and plural, that specialist intermediation
can reduce but not eliminate it, and that heterogeneity across
transaction types is part of the algebra. The lineage Coase →
Williamson / Hart-Moore / Varian is the standard pattern of taking a
substrate-side observation and building plural local algebras on top
of it. The program's adoption of `δ` as a coordinate on a
substrate-side discontinuity, with its algebra deferred to
[measure/ALGEBRA-OF-DELTA.md](measure/ALGEBRA-OF-DELTA.md), is the
mathematical-complexity instance of that pattern. The brief is
posture import, not proof material.
