# BOWEN-DRILLING-AND-DENSITY

Source-extraction memo on Lewis P. Bowen, *Density in Hyperbolic
Spaces*, Ph.D. dissertation, University of Texas at Austin, 2002
([sources/Bowen2002-drilling.pdf](sources/Bowen2002-drilling.pdf), 7
PDF pages covering pp. 43–49 of the dissertation: §2.3.1 "Penrose's
binary tilings" and §2.3.2 "A different tiling without an invariant
measure").

**Why this brief exists.** Landfall §6 already inherits Bowen 2002
§2.3.1 for the no-`PSL(2,ℝ)`-invariant-measure result on binary
tilings, and the program inherits that inheritance via
[fft/LANDFALL-PROOF-TEMPLATES.md](fft/LANDFALL-PROOF-TEMPLATES.md) Template 2.
Beyond what Landfall lifts, §2.3.1 contains a separate observation
the user surfaced — a *hole-drilling instability* lemma that says the
density of a tiling becomes ill-defined under arbitrarily small
perturbations. This observation is methodologically resonant with
[fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md)'s log-binade-clock
construction, where the gluing point that closes the binade
`[1, 2)` to a circle is exactly the next binade's `0` — a measure-zero
locus where density-theoretic structure could plausibly break in a
Bowen-style way. The brief surfaces the hole-drilling content for
program use and audits §2.3.2's alternative construction as
methodological context. Citation lifted from Landfall's References:
*Bowen, L. P. Density in Hyperbolic Spaces. Ph.D. dissertation,
University of Texas at Austin, 2002.*

**What was read.** Pages 43–49 of the dissertation, covering §2.3.1
(Penrose's binary tilings; the no-invariant-measure proof; the
hole-drilling observation; the optimal-density-≠-1 conclusion) and
§2.3.2 (alternative tiling without invariant measure, via free-group
action on a noncompact surface covered by `H²`). Pages 1–42 (Chapter
1, §1.2.2 strip model setup, §2.1 tiling-space lifts, etc., used by
Landfall) and pp. 50+ (later chapters) were not read here. Landfall's
existing citations to §1.2.2 (strip model with `W = ln 2`) and
§2.1 (eq. 2.5, natural tiling-space lift when an invariant measure
exists) are not independently audited in this brief.

**Confidence level.** High on the brief's three direct extractions
from §2.3.1 (no-invariant-measure proof; hole-drilling observation;
optimal-density bound) and on §2.3.2's structural shape — each is
either a direct quotation or a near-paraphrase with page anchor.
Medium on the program-side analogy between Bowen's hole-drilling and
the log-binade-clock gluing: the analogy is suggestive but is not a
content transfer; it is the brief's inference, not Bowen's framing.

**Trust boundary up front.** Bowen 2002 is a 2002 hyperbolic-geometry
dissertation read here for *vocabulary, methodological precedent,
and one specific observation* (hole-drilling density instability),
not for content directly transferred to the FFT impossibility theorem.
The mathematical content of the program does not depend on any
Bowen result holding for the log-binade circle; it depends on
Bowen having *named* and *proved* the hole-drilling instability in
the hyperbolic-tiling setting, where the program borrows the
vocabulary and uses the geometric kinship as a tactical resource for
aggregation-route rebuttals (per
[fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md) Track-A's closure-class
regularity guard and the C2 tactical reach in
[fft/LANDFALL-PROOF-TEMPLATES.md](fft/LANDFALL-PROOF-TEMPLATES.md) Template 2).

---

## 1. The no-invariant-measure result (§2.3.1, pp. 43–44)

This is the inheritance Landfall §6 already extracts; restated here
to anchor the brief. Sections §1 and §2 below are extracts from
Bowen's same §2.3.1; §3 extracts from §2.3.2. In Bowen's own
argument the three appear as one sustained geometric picture — the
no-invariant-measure result, the hole-drilling instability, and the
alternative free-group construction share a single setup and
mutually constrain each other in `H²`. The textual divisions here
are for the program's purposes, not Bowen's.

> *"the natural action of the isometry group `G` of `H²` (namely
> `G = PSL₂(ℝ)`) on the boundary `Δ` of `H²` ... assume there is a
> measure `µ` on `Δ` invariant under `G`. Any hyperbolic element
> `g_h ∈ G` has 2 fixed points in `Δ`, `p₁, p₂`, and moves all other
> points towards one and away from the other. From its invariance
> under `g_h`, `µ({p₁, p₂}) = 1`. Then considering that any elliptic
> element `g_e ∈ G` has no fixed points in `Δ`, and `µ` must also be
> invariant under `g_e`, we get a contradiction. So there are no
> probability measures on `Δ` invariant under `G`."* (p. 43)

The argument lifts from `Δ` (the boundary at infinity of `H²`) to
the binary-tiling space `Θ_β` via a continuous equivariant function
`f : Θ_β → Δ`, which "takes each tiling to the point 'pointed to'
by the protrusion on each body in the tiling" (p. 43). If a
`G`-invariant measure `µ` existed on `Θ_β`, the pushforward `µ_f`
would be a `G`-invariant measure on `Δ` — contradiction.

**For the program.** This is the Landfall §6 ⇒
[fft/LANDFALL-PROOF-TEMPLATES.md](fft/LANDFALL-PROOF-TEMPLATES.md) Template 2 inheritance:
representation-relocation rebuttals presupposing equivariant
aggregation across a representation cannot be supported by an
invariant measure in the binary-tiling setting. Already in the
program; not new.

## 2. The hole-drilling observation (§2.3.1, pp. 45–46)

The substantive new content for this brief, continuing §2.3.1's
setup from §1 above. In Bowen's text the hole-drilling observation
and the no-invariant-measure result appear within a single
discussion of the same binary tile `β`; the two sit together rather
than separately. Bowen constructs `β̄` from three abutting copies
of the binary tile `β`, drills a small hole, and obtains a body
`β̄_0` whose packings of the plane are "precisely the complements
of the disk packings of Böröczky discussed above" (p. 45). The
observation:

> *"the meaningfulness of the density of the tiling of Figure 2.3 is
> unstable under arbitrarily small perturbations (drilling
> arbitrarily small holes). Notice that when we drill these small
> holes we turn the tiling into a mere packing, forcing us to give up
> the 'simplicity' of the tiling, as a global object with seemingly
> obvious density, and leaving us to find some meaningful way to
> assign a density to the resulting packing."* (p. 45)

And the structural lesson:

> *"the difficulty in assigning a density to a packing, for instance
> congruent copies of a single body `β`, can derive from the
> complexity of the set of rigid motions of `β` that define the
> packing. And in this sense a tiling is no simpler; treating it as
> a global object with an 'obvious' density simply avoids coming to
> grips with the essential nature of the assignment of density for
> packings."* (p. 45)

> *"the phenomenon whereby the 'optimal' density can be less (even
> far less) than 1 for a body which can tile space, can be understood
> as related to the instability of the meaningfulness of the density
> of the tilings under removal of small holes in the tiles. This
> suggest that even for tilings one needs to keep track of the
> individuality of the tiles."* (p. 46)

Bowen also reports (citing [8]) that for every `ε > 0` there exists
a body `β` that admits a tiling of `H^n` but with optimal density
`D(β) < ε` (p. 44).

**For the program.** This is the disquieting observation. Three
program-side readings, none yet a transferred theorem:

*Reading A — measure-theoretic foundations.* The log-binade clock
`L = ℝ_{>0}/2^ℤ` is constructed by gluing `[1, 2)` to itself at the
`)`. The gluing point — `1`, identified with `0` of the next binade
— is a measure-zero locus where the construction closes. Bowen's
hole-drilling observation says density-theoretic structure on a
tiling is *unstable* under measure-zero perturbations of exactly the
hole-drilling shape. The log-binade circle is structurally a closed-up
strip with built-in gluing loci at every binade transition. Whether
Bowen's *theorem* transfers depends on geometric kinship (Bowen's
strip is `H²`; ours is 1D quotient), but the *vocabulary and
methodological warning* transfers: density and equidistribution
arguments on the log-binade circle should be audited at gluing loci
before being treated as substrate-level.

*Reading B — tactical resource for aggregation rebuttals.* If a
candidate aggregation attack on the FFT impossibility presents in a
binary-tiling-embeddable geometry — anything `PSL(2, ℝ)`-shaped,
horocyclic-strip, or dyadic-tower-shaped — the hole-drilling
observation strengthens the no-invariant-measure result of §1: not
only is there no invariant measure, but density on the would-be
tiling is *itself* structurally unstable. C2's tactical reach (per
[fft/LANDFALL-PROOF-TEMPLATES.md](fft/LANDFALL-PROOF-TEMPLATES.md) Template 2)
acquires this additional content when the attack's geometry is
Bowen-embeddable.

*Reading C — methodological discipline.* "Treating it as a global
object with an 'obvious' density simply avoids coming to grips with
the essential nature of the assignment of density for packings"
(p. 45). Translation to the program: vocabulary like "competitive
compression," "density of orbit equidistribution," and "no measurable
function separates regimes" should be specified at the level where
the substrate's measure-theoretic structure is honest, not at a
level where a "global density" is asserted by construction. This is
the program-side echo of Landfall's "the floor does not stabilize
that way" (cited from Landfall's §2.1/2.3.1 reading of Bowen).

**The warning we deploy, re-typed under the measure-theoretic discipline.**
Bowen's hole-drilling observation does not transfer to the
log-binade circle as a theorem — sub-check (α) of new test 2
confirms that the gluing locus lands on a horocycle
tile-*boundary* in the strip embedding (Landfall §1.2.2), while
Bowen's drilling acts on tile-*interiors*; the locus-types differ
and the mechanism does not carry. What does carry, under
[BNHA/hakamada/MEASURE-TWICE.md](BNHA/hakamada/MEASURE-TWICE.md)'s
measure-theoretic discipline, is *methodological character*. Bowen
explicitly demonstrates that density is the contested
measure-theoretic invariant on his substrate, and the hole-drilling
is his mechanism for naming the contestation. His own phrase —
*"the essential nature of the assignment of density for packings"*
(p. 45) — is what Best Jeanist now names structurally as
*measure-theoretic character*: density on Bowen's substrate is
multifarious because the rigid-motion group is rich enough to
preclude any single invariant probability measure, and the
hole-drilling exposes the contestation that was already there. We
deploy Bowen as the substrate-side methodological precedent for
the All-for-One refusal made measure-theoretically: density on his
substrate is multifarious; `T(P)` on ours is multifarious for
analogous structural reasons (no native functor `F` per
`memos/NATIVE-F-MINIMAL-DEFINITION.md`); both reflect substrate
structure too rich for object-level unification. Bowen supplies
at least one concrete worked instance of the contestation
(p. 44, `D(β) < ε` for any `ε > 0`, where the apparently obvious
density-1 was misleading by an arbitrary factor). The deployment
register upgrades from rhetorical-with-content to *load-bearing
methodological precedent*: when the program defends the All-for-One
refusal in measure-theoretic terms, Bowen has done structurally
analogous work in his own setting, and the citation carries that
load. Mechanism doesn't transfer; methodological character does.

## 3. Alternative construction without an invariant measure (§2.3.2, pp. 47–49)

Bowen presents a second construction in §2.3.2 that reaches the
same structural impossibility as §2.3.1's main result via a
different group action — the free group `F_2` rather than
`PSL₂(ℝ)` — and on a different geometric carrier (a noncompact
surface `S` covered by `H²` rather than the binary tiling space
itself). Read alongside §1 and §2, §2.3.2 is not a separate
theorem so much as a sister realization of the same configurational
fact under a different geometric light. The construction: octagonal
tile `τ`; X-tile formed by two copies; X-tiles glue to form a
noncompact surface `S` homeomorphic to "the boundary of a regular
neighborhood of the standard Cayley graph for the free group on
two generators embedded in `R³`", covered by `H²`; free group `F_2`
acts isometrically on `S` and lifts to `H²`. The conclusion is the
same — no invariant measure on the orbit closure of the lifted
tiling — and Bowen reaches it via two distinct routes:

- **Route 1 (push-forward).** Walking the protrusions gives a map
  from the space of tilings of `S` by `X` to the ideal boundary of
  `S`, commuting with `F_2`. The ideal boundary admits no `F_2`-
  invariant probability measure; by push-forward, neither does the
  tiling space.
- **Route 2 (stabilizer).** Suppose an equivariant map `φ` to `Δ`
  exists. The stabilizer of the tiling is noncyclic (contains the
  fundamental group of `S`); by Fuchsian-group theory, noncyclic
  groups don't fix points at infinity. Contradiction.

**For the program.** Methodological precedent only: the
no-invariant-measure pattern is not unique to the Penrose binary
tilings of §2.3.1 — it generalizes to other tilings whose orbit
closure factors onto a hyperbolic boundary. The program does not
need this generality (Landfall's §6 inheritance is on Penrose binary
tilings specifically), but if a future attack on the impossibility
presents in a non-binary-tiling but `H²`-embeddable geometry,
§2.3.2's two-route argument is on the shelf.

The §2.3.2 generalization is paged at pp. 47–49 of the PDF and
audited at the structural level only; the brief does not
independently verify the Fuchsian-group step or the homeomorphism
between `S` and the regular-neighborhood-of-Cayley-graph object.

---

## What Bowen states without our independent check

- Bowen cites [8] for the modification giving `D(β) < ε` for every
  `ε > 0` (p. 44). The brief does not chase the citation; the
  modification is reported as Bowen's attribution.
- The Böröczky disk-packing result that the §2.3.1 hole-drilling
  argument relates to (p. 45) is cited but not independently audited.
  Not load-bearing for the brief; the program uses the hole-drilling
  *observation*, not its specific connection to Böröczky.
- The §2.3.2 homeomorphism `S ≅` boundary-of-regular-neighborhood-of-
  Cayley-graph and the Fuchsian-group statement that noncyclic
  groups don't fix ideal points are reported as Bowen's; not
  independently audited.

The program's use of Bowen 2002 is at the methodological-vocabulary
plus tactical-resource level; none of the unchecked content is
load-bearing.

---

## What we infer for the program

The Bowen-to-FFT mapping is the brief's contribution; Bowen did not
write it.

| Bowen content | Program use | Status |
|---|---|---|
| §2.3.1 no-invariant-measure on binary tilings | LANDFALL-PROOF-TEMPLATES Template 2; aggregation rebuttal | Inherited via Landfall §6 |
| §2.3.1 hole-drilling instability | PHASE-DEFECT disquiet at log-binade gluing; C2 tactical strengthening | New; analogy not theorem |
| §2.3.1 `D(β) < ε` for `ε > 0` (citing [8]) | Methodological warning: tilings in `H^n` can have arbitrarily small optimal density | Background only |
| §2.3.2 alternative construction (free-group action on `S`) | Reserve for non-Penrose-tiling attacks | Methodological precedent |

Bowen 2002 transfers to the FFT impossibility theorem at three levels,
matching the COASE methodological-import shape:

1. **Vocabulary**: "tiling vs packing," "density unstable under
   small perturbations," "drilling holes," "no invariant measure on
   the orbit closure." All Bowen's. The program adopts this language
   at the disquiet-paragraph level and in C2 tactical reaches.
2. **Typing**: density on a tiled space is not a single number; it
   is a structure that depends on whether you have full coverage or
   arbitrarily-small-hole coverage, and on which invariant measure
   sees the tiling. Density on the log-binade circle inherits this
   typing as a methodological discipline; whether the typing has
   theorem-level content for the FFT impossibility is open.
3. **Methodological discipline**: "treating a tiling as a global
   object with an 'obvious' density simply avoids coming to grips
   with the essential nature of the assignment of density for
   packings" (p. 45). Translates: don't assert substrate-level
   measure-theoretic claims on the log-binade circle without
   auditing what happens at the gluing point. PHASE-DEFECT's Track A
   closure-class regularity guard and C2 tactical reach inherit this
   discipline.

---

## Trust Boundary

### This brief should be cited for

- the four direct quotations from §2.3.1 at pp. 43–46 (no-invariant-
  measure proof; hole-drilling observation; tile-vs-packing
  instability lesson; `D(β) ≠ 1` consequence);
- §2.3.2's two-route construction at pp. 47–49 (push-forward route;
  stabilizer/Fuchsian-group route);
- Bowen's distinction between *tiling as global object with obvious
  density* vs *packing whose density depends on the rigid-motion set
  defining it* as a methodological precedent;
- the table at §"What we infer for the program" above (each row is a
  defensible analogy or inheritance, not a transferred theorem).

### This brief should NOT be cited for

- any direct theorem about the log-binade circle — Bowen contains
  none; the geometric kinship is suggestive, not transferred;
- any FFT-impossibility content — Bowen contains none;
- any computational-complexity content — Bowen contains none;
- the claim that Bowen's hole-drilling instability transfers *as a
  theorem* to the program's measure-theoretic foundation —
  it transfers as *vocabulary, methodological warning, and tactical
  resource*, not as proof material;
- pp. 1–42 and pp. 50+ of the dissertation — not read here. Landfall's
  §1.2.2 strip-model and §2.1 tiling-space-lift citations live in
  unread pages and are not independently audited;
- the Böröczky disk-packing literature — referenced in passing on
  p. 45, not load-bearing here.

### Provenance tag for the program

**Methodological-warning anchor and tactical resource (PHASE-DEFECT,
LANDFALL-PROOF-TEMPLATES Template 2).** Bowen 2002 §2.3.1 supplies the
hole-drilling vocabulary, the typing of density as substrate-
unstable under measure-zero perturbations, and the tactical reach
that any binary-tiling-embeddable aggregation attack inherits both
the no-invariant-measure result *and* the density-instability
strengthening. None of these is a content transfer; all are language
and method. Cited at
[fft/PHASE-DEFECT.md](fft/PHASE-DEFECT.md) (disquiet paragraph and
Track A closure-class regularity guard, when the prose pass earns
the citation) and
[fft/LANDFALL-PROOF-TEMPLATES.md](fft/LANDFALL-PROOF-TEMPLATES.md) Template 2
(C2 tactical reach).

---

## Closing Sentence

This brief extracts seven pages of Bowen 2002 (pp. 43–49) for the
methodological-warning and tactical-resource content the FFT
impossibility paper inherits beyond what Landfall §6 already lifts:
that a tiling's density is unstable under arbitrarily small hole-
drilling, that no invariant measure on the binary-tiling space
exists by a direct boundary-of-`H²` argument, and that the same
no-invariant-measure pattern generalizes to other `H²`-embeddable
constructions. The mapping to PHASE-DEFECT's log-binade-clock
disquiet and to the C2 tactical reach is the brief's inferential
contribution; Bowen did not write it. The brief is vocabulary-
warning-and-tactical-resource import, not proof material.
