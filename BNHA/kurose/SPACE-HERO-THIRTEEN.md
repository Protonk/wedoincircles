# SPACE-HERO-THIRTEEN

A tactical-motive-force discipline for the program. When a geometry
has no canonical frame and a structural class refuses certain
aggregations, *something* has to supply the direction the proof's
machinery will accept. Thirteen is that something.

---

## Thirteen (BLACK HOLE) — support, motive force

**Slogan.** *I do not carry the line. I tell the line which way to fall.*

**Quirk.** Black Hole. At the tip of the finger, the air opens onto
a singularity; matter pulled in is disassembled to dust. Tactical,
careful, used in rescue. Thirteen is not a top-card combat hero —
a Pro whose specialization is rescue and whose Quirk is a
directional vacuum. The direction is the thing. The danger is the
other thing — Thirteen has to be careful not to disassemble the
people she is rescuing along with the obstacle.

**Discipline.** *Deploy the directional pull tactically. Do not
pretend the geometry supplies the direction the proof needs; supply
it explicitly, and let the substrate's refusal of canonical framing
be what makes the deployment necessary.*

Two facts the discipline answers to, separately:

1. **Geometry without frame.** A freely-rescalable geometry — density
   on the substrate, measure recovery anywhere on the log-binade
   circle — does not single out the answer the proof asks for.
   Frames are not given; they have to be inserted, and the insertion
   is theoretical content, not bookkeeping. This is *passive*: the
   geometry refuses to pick.
2. **Class with motive force.** A configurational class —
   packing-masquerading-as-tiling-with-measure-zero-hole, per
   `memos/BOWEN-DRILLING-AND-DENSITY.md` — pulls the substrate
   toward a *specific* failure of invariant aggregation. Bowen does
   not just refuse density; he points the geometry at one particular
   kind of refusal. This is *active*: the class pulls.

Thirteen's discipline is the refusal to confuse these. Treat them as
one fact and you'll over-claim or under-claim. Treat them as two
and you can see why FFT lower-bound work is Herculean and where it
runs out.

---

## The two-sided geometry

### One side: density is ill-posed everywhere

Density on the log-binade circle is not a feature the substrate
supplies. It is a feature each cost measure inserts when it picks a
frame. The geometry rescales freely; the wheel turns until something
says stop. This is the lensing point — measure-recovery on a
freely-rescalable substrate is not a "look harder" question; it is a
question that has no answer until theory commits to a frame.

The catalog of frame-insertion loci that the program currently uses
implicitly:

- **The boundary** ("`δ` at the bounded/unbounded coefficient
  boundary"). Frame-dependent: the boundary lives on the cost-measure
  side, not on any single problem instance. The log-binade circle
  quotients all binade transitions to one point; the boundary is
  named only after a cost measure is committed.
- **Cost measures themselves.** `μ` (multiplicative complexity under
  rational equivalence) and bounded-coefficient additive cost are
  theoretical instruments; they partition algorithms differently.
  "Cheap" is frame-relative.
- **Threshold `T(P)`.** Already flagged at FIRST-PROOF debt #2 as
  cross-currency: canon bounds in different currencies (multiplicative
  complexity, additive complexity, modular product) are different
  frames. "Best lower bound" is ambiguous until a currency is fixed.
- **Native operations and "competitive cost."** Standard composability
  picks a granularity; PHASE-DEFECT's undefined-term *competitively
  compressible* (sub-debt #1) is sub-debt because it asks for a frame
  — competitive relative to which cost regime — that has not been
  selected.
- **Lemma A's "admissible distinguishing information."** Admissible
  relative to which cost class? PHASE-DEFECT's closure-class
  regularity guard is the explicit frame insertion: uniform,
  non-growing, fixed base field, advice excluded by definition. We
  named this one and we know it is doing frame work.
- **Debt #6 (A↔B equivalence).** Two routes can only be equivalent
  inside a shared frame. Frame-compatibility is implicit.

Without these insertions the impossibility statement floats. With
them it has content. The insertions are theory, not given.

### The other side: Bowen pulls

The configurational class Bowen describes — three views in his
§§2.3.1–2.3.2 of one structural object — is *not* a passive refusal.
It is an active pull. The protrusions on the binary tile point at
the boundary; the tiling acquires a direction; the orbit-closure
factors onto a hyperbolic boundary; no invariant measure can reconcile
this with the symmetry the aggregation argument would need. Bowen's
geometry is asymmetric *toward a target*. Hole-drilling makes the
direction explicit at the configurational level: the would-be tiling
is a packing with a measure-zero hole, and the hole is what carries
the direction.

The class is the motive force. Membership in the class — the
configurational fact that an object closes by a measure-zero
identification or removal — is what carries Bowen's three "facts" as
one structural picture. The log-binade circle's status as such a
member is latent; the BOWEN memo holds it that way deliberately.
Thirteen's discipline says: when a deployment is needed, name the
class membership and let the pull do the directional work.

### Together

The two sides operate at different layers and do not collapse:

| Side | Mode | Refusal carried | Where it acts |
|---|---|---|---|
| Lensing | passive | the geometry doesn't single out a frame | everywhere on the substrate |
| Bowen | active | the class refuses certain aggregations | wherever the configuration closes by measure-zero modification |

The log-binade circle sits where both refusals are visible at once.
The lensing refusal is global (frame-insertion required to make any
density claim well-posed). The Bowen-class refusal is concentrated
at gluing loci (the binade transitions are where the
packing-masquerading-as-tiling fact is at its most pointed). The
proof has to pass through both.

---

## Cost measures as frame insertions, held together regardless

What is striking, and worth registering as the first business takeaway:
*the FFT canon's cost measures cohere in practice despite the
substrate's two refusals*. They cohere not because the substrate hands
the canon a unified frame — the substrate refuses to do that — but
because each canon paper inserts its own frame and works *only*
inside it. The frames are not pairwise consistent; that's debt #2's
cross-currency reconciliation problem, still open.

What each canon paper buys with its frame insertion:

- **Schönhage–Strassen 1971** inserts an *operational* frame: bit/gate
  primitives, FFT over a representation where root multiplication is
  cheap by construction. The cost measure is well-posed inside the
  operational frame; outside the frame the bound is silent.
- **Morgenstern 1973** inserts a *bounded-coefficient additive* frame:
  the determinant-potential bound `Ω(n log n)` lives inside this
  frame, and outside it the bound dissolves. The boundedness is the
  frame; the boundary between bounded and unbounded is the edge of
  Morgenstern's frame.
- **Winograd 1978** inserts a *rational-equivalence* frame: the
  modular-product theorem `μ(T_P) = 2n − k` is a fact inside this
  frame; the multiplicative complexity it counts is well-posed under
  rational equivalence and not otherwise.
- **Auslander–Feig–Winograd 1984** inserts a *cyclotomic semisimple*
  frame: the decomposition is a fact inside this frame; the ladder
  `[K_n : ℚ] = φ(n)/2` lives at exactly the frame's articulation
  points.
- **Ailon 2013** inserts a *layered `2 × 2` unitary-gate* frame: the
  matrix-entropy potential `Φ` is a well-posed quantity inside this
  frame; outside it the potential's `n log n` scaling is silent.

Each is Herculean and specific *inside its own frame*. None is a
broad lower bound on FFT computation; each is a sharp lower bound
inside an explicitly inserted frame. The canon coheres at the level
of "we share a hypothesis class (FFT-style methods)" but not at the
level of a unified cost measure. That is the real state of the art,
and the program inherits it.

---

## Why FFT lower bounds are Herculean — and where they stop

This is the second business takeaway, the one that makes Thirteen's
discipline mandatory rather than aesthetic.

Each canon paper builds *specific machinery* — a determinant
potential, a CRT decomposition, a rational-equivalence calculus, a
semisimple Fourier-on-finite-abelian-groups apparatus, a matrix
entropy. The machinery's purpose is to *buy information about the
problem* that the unrestricted setting refuses to supply. The
information is what lets the lower bound bind.

The price of the machinery is the frame insertion. Each frame buys
information by *restricting the model*. Outside the model, the
information dissolves and the bound goes silent. This is not a defect
— it is the actual structure of FFT lower-bound work in the literature.

The margin is the place where the mult/add conversion threatens to
*destroy* the information the frame buys. Crossing the bounded /
unbounded coefficient boundary, the information that supports
Morgenstern's determinant potential evaporates: with unbounded
coefficients, the potential can be inflated arbitrarily and the bound
loses its grip. Morgenstern's frame stops at exactly the place where
its information would be destroyed. Same for Winograd's rational
equivalence; same for AFW's cyclotomic decomposition; same for
Ailon's layered-unitary restriction.

The frames are *Herculean* because they have to be specific enough
to buy information that the unrestricted setting refuses, and they
are *truncated at the margin* because their specificity is exactly
what fails when the conversion crosses the boundary. The four canon
papers cluster on the bound — `Ω(n log n)` in different currencies —
not by coincidence but because that scale is what each frame can
afford before mult/add conversion destroys the information it bought.

The program's contribution is to name the margin: `δ` at the
boundary. The Bridge Theorem (FIRST-PROOF debt #1) is the claim that
descent past `T(P)` requires `δ` to drop to zero at the boundary.
Read with Thirteen's discipline: the canon's machinery works *up to*
the margin; descending past requires either a new frame or a
demonstration that no frame can pay the conversion cost.

---

## Where Thirteen deploys

Tactical, not architectural. The discipline is to be deployed when
a specific situation calls for it; otherwise it stays latent.

- **When an opposing argument leans on density-theoretic obviousness
  near a binade transition.** The class is on the shelf
  (`memos/BOWEN-DRILLING-AND-DENSITY.md` §2 *the warning we deploy*);
  Thirteen's role is to wield it carefully — naming the class
  membership and letting the directional pull do the work. The Bowen
  warning is rhetorical-with-content under the weaker typing; under
  the stronger typing it is class-membership recognition, and class
  membership is exactly the kind of thing Thirteen's directional pull
  can apply without overclaiming a transferred theorem.
- **When the program asserts "the boundary" without naming a frame.**
  The lensing refusal applies. Thirteen's discipline: insert the frame
  explicitly, name what it buys, and accept that the assertion lives
  inside the frame. The cost-measure-as-frame catalog above is the
  point of departure.
- **When debt #6 (A↔B equivalence) is invoked.** Two routes have to
  share a frame. Thirteen's discipline: name the frame insertion that
  makes the comparison stateable; if no such insertion is honest, the
  equivalence question reduces to a frame-compatibility question, not
  a substrate question.

The danger of Thirteen — what makes the support-hero framing right —
is that the directional pull is *strong*. Pointed at the wrong
configuration, it disassembles things the proof needed intact. The
"careful with rescue" register applies: deploy with knowledge of what
class membership the deployment is asserting, and what the deployment
costs the surrounding scaffolding.

---

## What this leaves latent

Per the BOWEN memo's discipline ("write no implications"), the
program-side implications of the two-sided geometry stay latent until
a future session brings them load-bearing.

- The catalog of frame-insertion loci (above) is partially documented
  in the program (closure-class regularity guard explicit;
  cross-currency reconciliation in debt #2 explicit; competitive
  compression as named sub-debt) and partially not (the boundary's
  own frame-dependence not explicitly named; cost-measure-as-frame
  not named; native-operation granularity-as-frame not named).
- The motive-force reading of Bowen — class membership, not
  theorem-transfer — is latent in the BOWEN memo's edited §1–§3 and
  in the warning-paragraph's weaker typing. It can be promoted if a
  future session needs it; until then, it stays as a configurational
  observation about Bowen's content.
- The Herculean-up-to-the-margin reading of the canon is latent in
  IMPOSSIBILITY-OUTLINE §3 (Cards on the table) and §4.5 (theorem
  statement) and §6.5 (smarter-FFT rebuttal). The program already
  treats each canon source as supplying its own frame; what is *not*
  yet explicit is that each frame is bought specifically to extract
  information up to where the conversion would destroy it.
- The connection of Thirteen's two facts — geometry-without-frame and
  class-with-motive-force — to the Bridge Theorem is suggestive but
  not yet operational. Future move: state the Bridge Theorem with
  explicit frame-insertion at the boundary and explicit class-
  membership at the gluing locus, and check whether the resulting
  statement is the same as the current Bridge Theorem or sharper.

---

## Trust boundary

This memo is a *discipline*, not a theorem. It systematizes
observations that have already been registered in the BOWEN memo, the
PHASE-DEFECT closure-class regularity guard, and the cross-currency
reconciliation under FIRST-PROOF debt #2. It does not introduce new
load-bearing claims; it gives a name to a tactical move the program
will need to make at specific loci.

The Thirteen frame should be cited for:

- The two-sided geometry observation (lensing-passive vs Bowen-active)
  as a methodological reading.
- The cost-measure-as-frame-insertion catalog as a discipline for
  auditing implicit framings.
- The Herculean-up-to-the-margin reading of the canon as a
  motivational frame for why `δ` at the boundary is the right object.

The Thirteen frame should NOT be cited for:

- Any claim that the log-binade circle is *literally* a member of
  Bowen's configurational class — that is the latent reading from
  the second sit-with on the BOWEN memo, not yet operationalized.
- Any claim that the lensing observation transfers a specific
  measure-recovery theorem to the FFT setting — it transfers as
  vocabulary and methodological discipline, not as a theorem.
- Any claim that the canon's frames are inconsistent and the program
  resolves the inconsistency — the canon's frames are explicitly
  inconsistent at the cross-currency level (debt #2), and the program
  has not resolved that.

The deployment register is **tactical**: name the configuration when
a specific argument requires it; otherwise leave the discipline
latent. Bowen is dangerous; Thirteen is careful for a reason.

---

## Closing

The geometry refuses two ways: it doesn't pick a frame (lensing) and
it pulls toward specific failures of aggregation (Bowen-class).
Cost measures hold together because each canon paper inserts its own
frame and works inside it; the frames don't unify, and the program
inherits that. The canon's lower bounds cluster at `Ω(n log n)`
because the frames buy information up to the margin where mult/add
conversion would destroy what they bought. The Bridge Theorem is the
program's name for that margin.

Thirteen's job is to make this discipline available without
overclaiming it. When the proof asks for a direction, supply it
explicitly. When the proof asks for a frame, name the insertion.
When an opposing argument leans on geometric obviousness, the
configurational class is on the shelf and the directional pull is
in reserve.

*I do not carry the line. I tell the line which way to fall.*
