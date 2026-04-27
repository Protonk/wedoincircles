# COASE-FRICTION-AND-SPECIALISTS

Source-extraction memo on Ronald H. Coase, "The Nature of the Firm,"
*Economica* New Series Vol. 4 No. 16 (Nov. 1937), pp. 386–405
([sources/Coase-1937.pdf](sources/Coase-1937.pdf), JSTOR scan, 24 PDF
pages including front matter).

**Why this brief exists.** [paper/IMPOSSIBILITY-OUTLINE.md](paper/IMPOSSIBILITY-OUTLINE.md)
§1.5 and [paper/FIRST-PROOF.md](paper/FIRST-PROOF.md) Setup adopt
**transaction cost** as the irreducible-fee object Lemma B blocks from
zeroing. The vocabulary is Coase's. FIRST-PROOF debt #2 lists the
algebra of `δ` (additivity, amortization, scale-behavior,
representation-dependence, bypass-resistance) as open sub-questions.
Coase 1937 is the methodological precedent for this distinction — *the
existence of friction is one claim, the algebra of friction is
another* — and supplies the specific bypass-resistance language ("may
be reduced but it will not be eliminated by the emergence of
specialists") the program inherits at §6.

**What was read.** Pages 386–396 of the original (first 12 pages of
the PDF including JSTOR cover and Section I + the opening of Section
II), covering Coase's setup, the price-mechanism-vs-firm distinction,
the existence-of-friction claim, the marginal condition for firm
size, the heterogeneity-of-transactions remark, and the firm-size
summary statement. Pages 397–405 (the dynamic-equilibrium and
employer-employee discussion) were not read; nothing in the brief
depends on them.

**Confidence level.** High on the brief's four extractions (existence,
specialists, marginal condition, shape determines size) — each is a
direct Coase quotation with page anchor. Medium on the program-side
mapping to FIRST-PROOF debt #2: the analogy is strong but is the
brief's inference, not Coase's framing.

**Trust boundary up front.** Coase is a 1937 economics paper read here
for *vocabulary and methodological precedent*, not for content
transferred to the FFT impossibility theorem. The mathematical content
of our paper does not depend on Coase having proved anything; it
depends on Coase having *named* and *typed* the cost / friction object
the way the FFT-impossibility argument needs it named and typed.

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
From this alone, you can argue that *some* coordination structure
beyond the price mechanism (firms) must exist — but you cannot derive
how big firms are or where their boundaries fall. Mapping: from
`δ > 0` alone (Lemma B in its simplest form), you can argue that
*some* finite-composition route to descent is blocked — but you
cannot derive the full impossibility region.

### 1.2 Specialists do not eliminate friction (p. 390)

> *"This cost may be reduced but it will not be eliminated by the
> emergence of specialists who will sell this information."*

**For the program.** This is Coase's *bypass-resistance* result.
Third-party intermediaries (specialists) can reduce friction but
cannot zero it. The cost is *substrate*, not *agent*. Reduction is
possible; elimination is not. Mapping: FIRST-PROOF debt #2's
"bypass-resistance under advice" — the question of whether advice /
amortization / specialization can route around `δ` — has Coase 1937 as
methodological precedent. The Coasean answer is: reduce yes,
eliminate no. The program's analog is the question of whether Lemma B
needs strengthening to cover advice-augmented regimes.

### 1.3 Marginal condition (p. 395)

> *"A firm will tend to expand until the costs of organising an extra
> transaction within the firm become equal to the costs of carrying
> out the same transaction by means of an exchange on the open market
> or the costs of organising in another firm."*

**For the program.** This is a *derivative* statement: firm size is
fixed where two marginal-cost curves meet. Coase explicitly needs the
*shape* of the cost function — not just its sign. Existence of
friction (the sign) is insufficient to determine the boundary; the
algebra (the derivative) is required. Mapping: FIRST-PROOF debt #2's
question of whether `δ` is "asymptotic? per-size? per-precision?" —
all questions about how `δ` scales — is exactly the algebra-of-friction
question Coase answers via marginal-cost analysis for the firm-size
problem. We do not yet have the analog answer for `δ`; debt #2 names
the open sub-questions.

### 1.4 Shape determines firm size (p. 396)

> *"Other things being equal, therefore, a firm will tend to be larger:
> (a) the less the costs of organising and the slower these costs rise
> with an increase in the transactions organised. (b) the less likely
> the entrepreneur is to make mistakes and the smaller the increase in
> mistakes with an increase in the transactions organised."*

**For the program.** Same friction-existence, different rate-of-rise
in the cost function → different firm boundaries. The algebra is what
distinguishes outcomes. Coase reads firm size off the cost function's
*derivative*, not its *value*. Mapping: the program's *impossibility
region* — the set of (problem, threshold) pairs at which FFT-style
descent fails — is similarly a function of `δ`'s algebra, not just
`δ > 0`. The brief reads Lemma B's current statement (no finite
composition zeros `δ`) as the analog of Coase's existence claim
(friction > 0); the full impossibility region is the analog of his
firm-boundary determination, and is open until the algebra of `δ` is
specified.

### 1.5 Heterogeneity of transactions (p. 396)

> *"Up to now it has been assumed that the exchange transactions which
> take place through the price mechanism are homogeneous. In fact,
> nothing could be more diverse than the actual transactions which
> take place in our modern world. This would seem to imply that the
> costs of carrying out exchange transactions through the price
> mechanism will vary considerably as will also the costs of
> organising these transactions within the firm."*

**For the program.** Friction is *not a single number*; it is a
function of transaction type. Mapping: FIRST-PROOF debt #2's
"representation-dependence" sub-question — whether `δ` depends on the
representation of the underlying compute problem — has Coase's
heterogeneity remark as methodological precedent. The Coasean answer
is: yes, friction varies across transaction types, and this
heterogeneity is what makes the firm-boundary problem non-trivial.
The program's parallel: `δ` likely varies across coefficient regimes,
problem instances, and conversion strategies, and this variation is
what makes the impossibility region non-trivial.

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

The program's use of Coase is at the methodological-vocabulary level;
none of the unchecked content is load-bearing.

---

## 3. What we infer for the program

The Coase-to-FFT mapping is the brief's contribution; Coase did not
write it.

| FIRST-PROOF debt #2 sub-question | Coase precedent | Coasean answer |
|---|---|---|
| Existence of `δ` | p. 390, "cost of using the price mechanism" | Friction exists. |
| Bypass-resistance under advice | p. 390, "specialists" remark | Reduce yes, eliminate no. |
| Additivity across compositions | p. 391, long-term vs short-term contracts | Sub-additive when bundled. |
| Amortization across uses | p. 394–395, diminishing returns to entrepreneur | Friction-per-transaction varies with scale. |
| Scale-behavior / asymptotics | p. 395 marginal condition; p. 396 (a) | Determines boundary via derivative. |
| Representation-dependence | p. 396 heterogeneity remark | Friction varies across transaction types. |
| Sign vs shape | p. 390 (sign) vs p. 396 (shape) | Shape, not sign, determines outcomes. |

Coase does not transfer to the FFT impossibility theorem at the
content level. He transfers at three levels:

1. **Vocabulary**: "transaction cost," "irreducible fee,"
   "frictionless ideal vs reality with friction" — all Coasean. The
   program adopts this naming consistently at §1.5.
2. **Typing**: friction is a non-zero scalar with an algebra (not a
   binary "exists / does not"). The algebra has named sub-questions
   (additivity, amortization, scale-behavior, etc.). FIRST-PROOF
   debt #2 inherits this typing.
3. **Methodological discipline**: existence claims and algebraic
   claims are separately stateable, separately provable, and
   separately load-bearing. Lemma B in its current form is an
   existence-side claim about `δ`. The full impossibility region is
   an algebra-side claim about `δ`. The program does not need to
   close the algebra to state Lemma B; it needs to close the algebra
   to state the impossibility region.

---

## 4. Trust Boundary

### This brief should be cited for

- the four direct quotations at pp. 390, 395, 396 (existence,
  specialists, marginal, shape-determines-size);
- the heterogeneity remark at p. 396;
- Coase's distinction between the existence of friction and its
  algebra as a methodological precedent;
- the mapping table at §3 above (each row is a defensible analogy,
  not a transferred theorem).

### This brief should NOT be cited for

- any FFT-impossibility content — Coase contains none;
- any computational-complexity content — Coase contains none;
- the claim that Coase's algebra-of-friction analysis transfers
  *as a theorem* to the program — it transfers as *vocabulary and
  methodological precedent*, not as proof material;
- pp. 397–405 of the original — not read here;
- empirical economics claims — not the program's domain.

### Provenance tag for the program

**Methodological-framework anchor (§1).** Coase 1937 supplies the
transaction-cost vocabulary, the typing of friction as a positive
scalar with an algebra, and the discipline of separating existence
claims from algebraic claims. None of these is a content transfer; all
of them are language and method. Cited at
[paper/IMPOSSIBILITY-OUTLINE.md](paper/IMPOSSIBILITY-OUTLINE.md)
§1.1, §1.5, §6.5, and (potentially) §Conclusion.

---

## Closing Sentence

This brief extracts four pages of Coase 1937 (pp. 390, 395, 396) for
the methodological-framework precedent the FFT impossibility paper
inherits at §1: that friction is a non-zero scalar, that its algebra
(not just its sign) determines outcomes, that specialist
intermediation can reduce but not eliminate it, and that
heterogeneity across transaction types is part of the algebra. The
mapping to FIRST-PROOF debt #2 is the brief's inferential
contribution; Coase did not write it. The brief is vocabulary-and-
method import, not proof material.
