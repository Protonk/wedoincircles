# PROVENANCE-AND-TRANSFERABILITY

INHERIT-discipline synthesis on the FFT-complexity chain. Applies
[BNHA/ONE-FOR-ALL.md](BNHA/ONE-FOR-ALL.md)'s two-clause obligation —
provenance backward + transferability forward — to the program's use
of the FFT-complexity literature.

This memo is the program-side counterpart to
[fft/FOUR-FRAMEWORK-SYNTHESIS.md](fft/FOUR-FRAMEWORK-SYNTHESIS.md).
The four-framework synthesis is the *cross-source comparison*: four
papers in seven-axiom space, pairwise non-composability, the program's
fifth-coordinate identification. This memo records what the program
*does* with that synthesis: what it inherits with audit, what it has
imported into program-internal apparatus, and what it owes to
successors.

This is a third-register memo per [CONTRIBUTING.md](CONTRIBUTING.md):
load-bearing, expected to hold up under scrutiny. Where a statement
is not directly attested by one of the cited memos, it is labelled
explicitly.

---

## 1. Provenance backward

The chain runs Gauss 1805 → Cooley–Tukey 1965 → modern complexity
literature (AFW 1984, Morgenstern 1973, Winograd 1978,
Schönhage–Strassen 1971). The historiographical audit lives in
[fft/HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF.md](fft/HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF.md);
it documents the inheritance chain with explicit transmission failures
(Hansen 1835 non-citation, the British 19th-century line, the
1866–1965 quiet century) and explicit direct continuities (Lagrange →
Gauss via Göttingen library borrowing 1795–1798).

Per-source role and trust boundary:

- **Auslander–Feig–Winograd 1984**
  ([fft/AUSLANDER-FEIG-WINOGRAD-1984-BRIEF.md](fft/AUSLANDER-FEIG-WINOGRAD-1984-BRIEF.md)):
  rational-equivalence-preserving, semisimple cyclotomic decomposition,
  multiplicative complexity under rational equivalence. Imported as
  *structural decomposition*, not as cost model — AFW's
  rational-equivalence quotient is not certification-cost preserving.
- **Morgenstern 1973**
  ([fft/MORGENSTERN-1973-BRIEF.md](fft/MORGENSTERN-1973-BRIEF.md)):
  bounded-coefficient determinant-growth lower bound. Imported as
  *boundedness mechanism* — the structural reason coefficient-bounded
  hypotheses prevent volume-growth absorption is the lever the program
  needs at axiom 2 in different form.
- **Winograd 1978**
  ([fft/WINOGRAD-1978-BRIEF.md](fft/WINOGRAD-1978-BRIEF.md)):
  modular-product theorem `mu(T_P) = 2n - k`, CRT/cyclotomic factor
  ledger. Imported as *cyclotomic factor accounting*, not as
  certification-preserving lower bound — Winograd permits free
  constants and field choice in a way the program's regime forbids.
- **Schönhage–Strassen 1971**
  ([fft/SCHOENHAGE-STRASSEN-1971-BRIEF.md](fft/SCHOENHAGE-STRASSEN-1971-BRIEF.md)):
  operational uniform bit-complexity / Boolean-circuit, FFT over
  representations where root multiplication is cheap. Imported as
  *uniform operational template* — the program's certification-
  preserving regime is closest to Schönhage–Strassen's stance on
  axioms 3, 4, 7.

Audit verdicts on the chain follow the L-W-safety content criterion
([memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md) §"Audit
criterion: content, not calendar"): a candidate's first-proof date is
not the end of the audit; what matters is whether the proof technique
routes through transcendence theory. None of the four FFT-complexity
briefs depends on Lindemann–Weierstrass; the chain is L-W-safe in
content even though all four papers are post-1882 in calendar.

---

## 2. What the program uses

Four tools the program has imported and integrated.

### 2.1 Ledger lattice apparatus

P-axis (positional granularity P0–P3 + orbit) × A-axis (algebraic
certification A0–A3); semantic vs. cost lattices distinct.
`V_cert` at `(P3, A2)`; `O_cert` at `(orbit, A3)`; `F2` at `(P2, A0)`;
row-degree at `(P1, A1)`. Lives in
[memos/LEDGER-PIVOT-SEARCH.md](memos/LEDGER-PIVOT-SEARCH.md)
§"Ledger lattice".

The lattice is program-internal apparatus; its *construction* is
program-side, but its *calibration* is against AFW's
rational-equivalence quotient (which determined what the lattice must
not silently quotient) and Morgenstern's coordinate-sensitive counting
(which determined what the A-axis must keep cost-bearing).

### 2.2 Certification-preserving regime + seven open axioms

The fifth coordinate the program commits to: algebraic-arithmetic
over `Q` with seven axioms specified as open:

1. algebraic constants as advice versus paid adjunctions;
2. coefficient height-boundedness;
3. binary additions versus arbitrary linear combinations;
4. precomputed DFT-like matrices/linear transforms free versus paid;
5. field adjunctions paid by degree, height, or both;
6. root isolation paid by precision, certification depth, or both;
7. uniformity in `N` versus nonuniform advice.

Lives in [memos/LEDGER-PIVOT-SEARCH.md](memos/LEDGER-PIVOT-SEARCH.md)
§"Certification-preserving model: open axioms". The regime's
distinguishing commitments per
[fft/FOUR-FRAMEWORK-SYNTHESIS.md](fft/FOUR-FRAMEWORK-SYNTHESIS.md)
§"Verdict": closest to Schönhage–Strassen on axioms 3, 4, 7; adds
paid algebraic constants at axiom 1, paid algebraic height at
axiom 2, paid adjunctions by degree at axiom 5, paid root isolation
by precision and certification depth at axiom 6.

### 2.3 Fifth-coordinate identification + bridge as construction

Pairwise non-composability is structural at named axiom splits
([fft/FOUR-FRAMEWORK-SYNTHESIS.md](fft/FOUR-FRAMEWORK-SYNTHESIS.md)
§"Non-Composability Is Structural"). The program's certification-
preserving regime is a fifth axiom-coordinate, distinct from each of
the four neighboring frameworks. **Bridge work is construction, not
import**: existing frameworks supply tools and constraints; no
neighbor supplies the theorem.

The (task, model, ledger) triple commits the program: T1 (enumerate
corner positions to precision `10^-k`) or T3 (distinguish pairs
`(n, k)` whose round-trace agrees but actual trace differs at
precision `epsilon`) + certification-preserving algebraic-arithmetic
over `Q` + `V_cert` at `(P3, A2)`. The matching claim asserts that no
strictly lighter ledger serves a tight primitive-op lower bound on
T1 or T3 in the model.

Tasks live in [memos/COUNTING-APPARATUS.md](memos/COUNTING-APPARATUS.md)
§(B); the matching claim in
[memos/LEDGER-PIVOT-SEARCH.md](memos/LEDGER-PIVOT-SEARCH.md)
§"Task-ledger admissibility".

### 2.4 Closure-asymmetry forced `K_n`

The eigenspace identification proven in
[fft/HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF.md](fft/HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF.md)
§5 shows `K_n = Q(cos(2 pi / n))` is the unique multiplicatively-
closed half of the Galois involution decomposition of `Q(zeta_n)`:

```text
Q(zeta_n) = K_n  ⊕  K_n · 2 i sin(2 pi / n).
```

`E_{-1}` is a 1-dimensional `K_n`-module but **not** a subfield. The
program's algebraic-side commitment to `K_n` is therefore *forced by
closure*, not aesthetic. Uplifted to
[memos/NATIVE-F-MINIMAL-DEFINITION.md](memos/NATIVE-F-MINIMAL-DEFINITION.md)
§"Why `K_n` (forced by closure)" as structural justification for the
closure-mismatch theorem's algebraic-side ladder.

This connects two branches: the FFT-complexity import (where `K_n`
appears as the algebraic substrate the bridge construction builds
over) and the closure-mismatch theorem (where `K_n` appears as the
closure-generator family). Same field, two roles, one structural
justification.

---

## 3. Transferability forward

Per ONE-FOR-ALL.md, the program owes successors *transferable tools*.
What this folder hands forward.

### 3.1 The articulated bridge-construction agenda

A successor working on a primitive-op lower bound for cyclotomic-
complexity-shaped tasks has, on file:

- The seven open axioms, each with disjunctions specified
  (LEDGER-PIVOT-SEARCH §"Certification-preserving model").
- The fifth-coordinate position relative to four neighboring
  frameworks (FOUR-FRAMEWORK-SYNTHESIS §"Verdict").
- The (task, model, ledger) triple as the deliverable shape
  (COUNTING-APPARATUS §(B), LEDGER-PIVOT-SEARCH §"Task-ledger
  admissibility").
- The matching claim as the proof object.
- The construction agenda's four parts — define the certification-
  preserving machine, operationalize the algebraic ledger, import
  boundedness as theorem (not slogan), uniformize the cost
  accounting — in FOUR-FRAMEWORK-SYNTHESIS §"Construction Required".

A successor does not start from "is there a lower bound somewhere
nearby"; they start from "here is the specific axiom-coordinate, here
are its commitments, here is what construction is needed."

### 3.2 The trust boundaries on each imported tool

Each brief carries a "should be cited for / should NOT be cited for"
section. Successors who use the same imports inherit those boundaries
explicitly. This prevents the same tool from being silently used for
something its source brief specifically rules out — e.g., AFW's
rational-equivalence framework being cited for a certification-cost
claim it does not support.

### 3.3 The synthesis as auditable record

FOUR-FRAMEWORK-SYNTHESIS is itself a transferable artifact: the
axiom-by-axiom matrix, the pairwise non-composability table with
named splits, the construction agenda. A successor who disagrees with
the program's coordinate placement can audit the synthesis cell by
cell against the four briefs, and dispute or refine specific cells
without dispute spreading to the whole synthesis.

### 3.4 The closure-asymmetry observation

The `K_n`-forced-by-closure result is small but lifts the program's
algebraic-side commitment from convention to structural fact.
Successors building on `K_n` as the algebraic substrate inherit the
justification for that choice without re-deriving it. Successors
working in `Q(zeta_n)` instead inherit the explicit fact that they
have chosen a strictly larger object than closure forces.

---

## 4. What stays open

The transferability is honest about what hasn't closed.

- **Axiom consistency.** Whether the seven open axioms close
  consistently under the program's commitments (paid adjunctions,
  paid height, paid root isolation, etc.) is not yet argued. Some
  pair of commitments might be mutually exclusive.
- **Matching argument.** The matching claim survives the calibration
  on below-matching-as-coarse-but-valid (three-regime structure
  intact), but the matching-at-coordinate claim is not yet ironclad.
  Stress-test stands open.
- **Fifth-coordinate construction.** The synthesis identifies the
  coordinate as distinct from the four neighbors; the construction
  itself is not done. This is the bet inside the quarantine that
  [BNHA/VILLAINS-ANSWERED.md](BNHA/VILLAINS-ANSWERED.md) §#5 makes
  explicit.
- **Closure-asymmetry-to-compute-cost translation.** `K_n` is forced
  by closure on the algebraic side; whether forced-by-closure
  translates into a primitive-op cost the certification-preserving
  model registers is a separate question.

These are the items a successor inherits as *work*, not as solved.

---

## Cross-references

- [fft/FOUR-FRAMEWORK-SYNTHESIS.md](fft/FOUR-FRAMEWORK-SYNTHESIS.md) —
  cross-source synthesis (load-bearing).
- [fft/FFT-CYCLOTOMIC-COMPLEXITY.md](fft/FFT-CYCLOTOMIC-COMPLEXITY.md) —
  coordination memo (directed-read agenda; predates the synthesis).
- [fft/HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF.md](fft/HEIDEMAN-JOHNSON-BURRUS-1985-BRIEF.md) —
  historiographical audit (Gauss 1805 → Cooley–Tukey 1965).
- [memos/LEDGER-PIVOT-SEARCH.md](memos/LEDGER-PIVOT-SEARCH.md) —
  lattice apparatus, certification-preserving regime, matching claim.
- [memos/COUNTING-APPARATUS.md](memos/COUNTING-APPARATUS.md) —
  T1/T2/T3 task definitions, model menu.
- [memos/NATIVE-F-MINIMAL-DEFINITION.md](memos/NATIVE-F-MINIMAL-DEFINITION.md) —
  closure-mismatch theorem, `K_n` forced-by-closure justification.
- [memos/OLD-TIME-RELIGION.md](memos/OLD-TIME-RELIGION.md) —
  L-W-safety audit criterion (content, not calendar).
- [BNHA/VILLAINS-ANSWERED.md](BNHA/VILLAINS-ANSWERED.md) §#5 —
  narrative-register summary of the program's commitments arising
  from this work.
- [BNHA/ONE-FOR-ALL.md](BNHA/ONE-FOR-ALL.md) — INHERIT discipline
  framing (provenance + transferability).
