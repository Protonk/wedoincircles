# FFT-COMPLEXITY-FOUR-FRAMEWORK-SYNTHESIS

Cross-source synthesis on the four FFT-complexity frameworks extracted in:

- [memos/AUSLANDER-FEIG-WINOGRAD-1984-BRIEF.md](memos/AUSLANDER-FEIG-WINOGRAD-1984-BRIEF.md)
- [memos/MORGENSTERN-1973-BRIEF.md](memos/MORGENSTERN-1973-BRIEF.md)
- [memos/WINOGRAD-1978-BRIEF.md](memos/WINOGRAD-1978-BRIEF.md)
- [memos/SCHOENHAGE-STRASSEN-1971-BRIEF.md](memos/SCHOENHAGE-STRASSEN-1971-BRIEF.md)

This is a third-register synthesis in the sense of
[CONTRIBUTING.md](CONTRIBUTING.md): it is intended as load-bearing
program architecture, not a provisional search note. The claims below
are bounded by the four source-extraction briefs. Where a statement is
not a theorem of one of the papers, it is labelled as a program-side
construction requirement.

The comparison uses the seven open parameters from
[memos/LEDGER-PIVOT-SEARCH.md](memos/LEDGER-PIVOT-SEARCH.md)
section "Certification-preserving model: open axioms":

1. algebraic constants as advice versus paid adjunctions;
2. coefficient height-boundedness;
3. binary additions versus arbitrary linear combinations;
4. precomputed DFT-like matrices or linear transforms as free versus paid;
5. field adjunctions paid by degree, height, or both;
6. root isolation paid by precision, certification depth, or both;
7. uniformity in `N` versus nonuniform advice.

## Verdict

The four papers do not occupy one framework at different strengths.
They occupy four distinct coordinates in the seven-axiom space.

The program's desired certification-preserving algebraic-arithmetic
regime is a fifth coordinate. It is closest in spirit to
Schoenhage-Strassen's operational and uniform stance, but it must add
three things that Schoenhage-Strassen does not supply:

- paid algebraic height in axiom 2;
- paid field adjunctions by degree, with height accounted through
  axiom 2, in axiom 5;
- root isolation paid by both numerical precision and certification
  depth in axiom 6.

Therefore the bridge work in
[memos/FFT-CYCLOTOMIC-COMPLEXITY.md](memos/FFT-CYCLOTOMIC-COMPLEXITY.md)
is construction, not import. The existing literature supplies
ingredients, obstructions, and model templates; no briefed paper already
lives at the program's coordinate.

## Coordinate Notation

For compactness, each framework is recorded as:

```text
(A1, A2, A3, A4, A5, A6, A7)
```

where `Ai` is the commitment made on open axiom `i`.

These coordinates are semantic/cost coordinates, not moral rankings.
A framework can be powerful precisely because it quotients data that the
program must retain.

## Witness Index

The tables below rely on the following source-level witnesses, each
recorded in the corresponding source-extraction brief.

| Tag | Witness | Proof technique / role |
| --- | --- | --- |
| AFW-1 | For every finite abelian group `G`, `F(G)` is rationally equivalent to a semisimple cyclotomic linear system, and `p(M)` counts essential nonrational multiplication/division steps. | p-primary decomposition, Vandermonde blocks, CRT, tensor products of semisimple algebras, and the Auslander-Winograd semilinear-system theorem. Establishes the AFW coordinate on A1, A3, A4, A5, and A7. |
| AFW-2 | AFW does not count additions, rational preprocessing/postprocessing, bit complexity, numerical precision, height of algebraic constants, or construction of cyclotomic constants. | Model definition: multiplicative complexity after rational-equivalence quotient. Establishes the AFW coordinate on A2, A3, A5, and A6. |
| MOR-1 | A bounded-coefficient linear algorithm adjoins `h = lambda f + mu g` with `|lambda|, |mu| <= c`, and satisfies `m+ > log A(F) / log(2c)`. For the DFT and `c = 1`, this gives `m+ > (n/2) log_2 n`. | Determinant / volume-growth argument using multilinearity and the coefficient bound. Establishes Morgenstern's A2/A3 commitments and the lower-bound mechanism. |
| MOR-2 | The theorem applies to each fixed coefficient matrix `F`; coefficients may be arbitrary complex numbers subject to the modulus bound, with no field-adjunction, root-isolation, bit, or uniform-code accounting. | Fixed-matrix linear-circuit framework. Establishes Morgenstern's A1, A4, A5, A6, and A7 commitments. |
| WIN-1 | For multiplication modulo a degree-`n` polynomial `P`, the imported modular-product theorem is `mu(T_P) = 2n - k`, where `k` is the number of distinct irreducible factors of `P`; multiplication by fixed field elements is not counted. | Bilinear multiplicative complexity plus CRT factorization. Establishes Winograd's A1, A3, and A5 commitments. |
| WIN-2 | The DFT algorithms are built from cyclic convolution, Rader/Good decompositions, CRT recombinations, permutations, and sometimes extension fields that split more factors and reduce multiplication count. | Constructive change-of-form algorithmics. Establishes Winograd's A4 and A7 limitations and the non-certification-preserving use of field choice. |
| SS-1 | Two `N`-digit integers are multiplied in `O(N log N log log N)` on multitape Turing machines and Boolean networks; primitives are head movements or two-input gates. | Recursive FFT construction with explicit operational cost. Establishes Schoenhage-Strassen's A3, A4, and A7 commitments. |
| SS-2 | In `Z_{F_n}`, the element `2` is a primitive `2^(n+1)`-th root of unity, so twiddle multiplication is cyclic shift; the complex method instead uses fixed-point precision. | Representation engineering: make the algebraic root operation operationally cheap, or pay fixed-point precision. Establishes Schoenhage-Strassen's A1, A2, A4, A5, and A6 commitments. |

## The Five Coordinates

| Framework | Axiom coordinate | Establishing witnesses |
| --- | --- | --- |
| AFW 1984 | `(free fixed complex/cyclotomic constants; no height bound; additions and rational linear transforms free, essential nonrational multiplication/division counted; rational pre/post transforms free; field adjunction not a paid primitive; no root isolation or precision cost; nonuniform fixed finite system)` | AFW brief, "Main Payload" and section 1: `F(G)` is rationally equivalent to a semisimple cyclotomic linear system; `p(M)` counts essential nonrational multiplication/division; rational row/column changes preserve `p(M)`. AFW brief, section 2: additions, rational preprocessing/postprocessing, bit complexity, precision, constant height, and constructing cyclotomic constants are not counted. |
| Morgenstern 1973 | `(bounded complex scalar advice; modulus-bounded coefficients, not algebraic height; binary bounded linear additions counted; fixed target matrix not one primitive but no uniform description charged; no field-adjunction operation; no root-isolation operation; nonuniform fixed matrix/size)` | Morgenstern brief, section 1: each counted step is `h = lambda f + mu g` with `|lambda|, |mu| <= c`; `m+ > log A(F) / log(2c)`; for the DFT, `m+ > (n/2) log_2 n` at `c = 1`. Morgenstern brief, section 3: arbitrary complex coefficients of bounded modulus are permitted, not constructed. |
| Winograd 1978 | `(chosen-field constants free; no height or modulus bound; multiplicative complexity over a field, with fixed scalar multiplications/additions not the lower-bound currency; CRT/permutation/change-of-form data permitted; field extensions not paid and may reduce count; no root isolation or precision cost; nonuniform algorithm family/no Kraft charge)` | Winograd brief, "Main Payload" and section 1: the modular-product theorem `mu(T_P) = 2n - k` for multiplication modulo a degree-`n` polynomial `P`, with `k` distinct irreducible factors; multiplication by fixed field elements is not counted; CRT recombination supplies the algorithms. Winograd brief, section 2: extension of the coefficient field can split more factors and reduce multiplication count. |
| Schoenhage-Strassen 1971 | `(no arbitrary algebraic advice in the operational model; bit-length/precision charged rather than algebraic height; primitive cost is TM head movement or two-input gate; FFT work paid except representation-level shifts/wiring; no abstract field-adjunction primitive; numerical precision paid in the complex method and exact finite-ring arithmetic in the Fermat method, but no certification-depth isolation ledger; uniform recursive algorithm in input size)` | Schoenhage-Strassen brief, "Main Payload" and section 1: multiplication of two `N`-digit integers in `O(N log N log log N)` on multitape Turing machines and Boolean networks; effort is head movements or gate count. Section 2: in `Z_{F_n}`, `2` is a primitive `2^(n+1)`-th root of unity and twiddle multiplication becomes cyclic shift; complex method uses fixed-point precision. Section 4 and Hazard 3: the algorithm is uniform in `N`. |
| Program certification-preserving regime | `(algebraic constants must be constructed by paid adjunctions; algebraic coefficient height is bounded and paid; primitive arithmetic is binary, arbitrary linear transforms are decomposed and paid; precomputed DFT-like matrices and linear transforms are paid by description/application; field adjunctions are paid at least by degree, with height paid through A2; root isolation is paid by both precision and certification depth; uniform in N, ideally with self-delimiting/Kraft-compatible compiler)` | Program-side construction target, not an existing theorem. It is the working default named in `LEDGER-PIVOT-SEARCH`: paid adjunctions, bounded constants, binary additions, paid linear transforms, paid adjunctions by degree, paid root isolation by precision, and uniformity in `N`. |

The last row is not imported from any source. It is the coordinate the
program must build if `V_cert` is to remain cost-bearing rather than
semantic-only.

## Axiom-by-Axiom Witness Matrix

| Axiom | AFW 1984 | Morgenstern 1973 | Winograd 1978 | Schoenhage-Strassen 1971 | Program coordinate |
| --- | --- | --- | --- | --- | --- |
| A1 constants | Free fixed complex/cyclotomic constants. Witness: semilinear systems over `C`; DFT entries and cyclotomic fields are structural data. | Free bounded complex coefficients. Witness: `lambda, mu in C`, `|lambda|, |mu| <= c`. | Free constants from chosen field. Witness: multiplication by fixed elements of `G` is not counted. | Operational constants only. Witness: root `2` in `Z_{F_n}` is represented as a shift; complex roots require fixed-point approximation. | Paid algebraic constants; no arbitrary algebraic advice. |
| A2 coefficient size | Not controlled. Witness: AFW brief lists height and precision as uncounted. | Modulus-bounded, not height-bounded. Witness: determinant proof needs `|lambda|, |mu| <= c`. | Not controlled. Witness: field extension and fixed scalars are allowed without height charge. | Bit-length/precision charged. Witness: TM/gate model and fixed-point complex method; Fermat-ring elements have represented size. | Algebraic height is bounded and charged. |
| A3 addition primitive | Additions and rational linear transforms free. Witness: `p(M)` counts essential nonrational multiplication/division only. | Binary bounded linear additions counted. Witness: each new form has two parents. | Multiplications are the lower-bound currency; additions and fixed scalar recombinations are not the protected cost. Witness: modular-product complexity. | Head movements/gates are primitive; arbitrary linear combinations are not primitive. Witness: operational model definitions. | Binary arithmetic primitives; arbitrary linear maps decomposed and paid. |
| A4 precomputed transforms | Rational pre/post transforms free. Witness: rational equivalence preserves `p(M)`. | Full matrix not one primitive, but fixed matrix/circuit family is nonuniform and description-free. Witness: theorem applies to fixed `F`. | Permutations, CRT recombinations, and fixed constants are algorithmic change-of-form data. Witness: Rader/Good/CRT constructions. | FFT transforms are paid operationally, except shifts/wiring made cheap by representation. Witness: Fermat cyclic-shift trick. | Precomputed matrices/transforms paid. |
| A5 field adjunction | Not paid. Witness: cyclotomic fields and semisimple algebras are decomposition objects, not constructed constants. | Not modeled. Witness: arbitrary complex coefficients simply available under modulus bound. | Not paid. Witness: enlarging the field can reduce counted multiplications. | No abstract adjunction primitive. Witness: chosen rings are implemented by bit operations. | Paid by degree, with height controlled by A2. |
| A6 root isolation | Not present. Witness: exact semilinear algebra over `C`. | Not present. Witness: exact linear algebra over `C`. | Not present. Witness: exact algebra over a chosen field. | Precision paid in complex method; finite-ring method exact; no certification-depth isolation. Witness: fixed-point FFT and Fermat-ring FFT. | Paid by precision and certification depth. |
| A7 uniformity | Nonuniform fixed finite system. Witness: fixed `F(G)` and no compiler/Kraft accounting. | Nonuniform fixed matrix. Witness: theorem applied separately to each DFT size. | Nonuniform family/no prefix-free accounting. Witness: constructive tables and field choices, but no uniform code charge. | Uniform in `N`. Witness: recursive algorithm handles arbitrary input size. | Uniform in `N`, with Kraft-compatible description as an additional target. |

## Non-Composability Is Structural

The frameworks fail to compose at named axiom splits. The failure is
not that one paper is "weaker" than another. The problem is that each
paper protects a different invariant.

| Pair | Blocking split | Status | Reason |
| --- | --- | --- | --- |
| AFW 1984 / Morgenstern 1973 | A2, A3, A4 | Incompatible as stated | AFW freely uses rational equivalence and free rational linear transforms. Morgenstern's determinant argument is coordinate-sensitive and depends on bounded binary linear additions. A rational change of basis can move determinant growth into coefficients, exactly the channel Morgenstern bounds. |
| AFW 1984 / Winograd 1978 | A4, plus theorem scope | Translatable inside algebraic multiplicative complexity, not certification-cost preserving | Winograd supplies modular-product/CRT multiplicative structure; AFW supplies semilinear rational-equivalence structure. They are adjacent algebraically. But the translation preserves multiplication counts only after quotienting additions, heights, precision, and positional data. |
| AFW 1984 / Schoenhage-Strassen 1971 | A3, A4, A7 | Incompatible as stated; translatable only by paying transforms operationally | AFW's rational equivalence forgets the coordinate representation. Schoenhage-Strassen's cheap root multiplication depends on exact bit positions in the Fermat-ring representation. A rational change of basis destroys the shift/wiring witness unless the change itself is implemented and charged. |
| Morgenstern 1973 / Winograd 1978 | A2, A3, A5 | Incompatible as stated | Morgenstern counts bounded binary linear additions over `C`; Winograd counts multiplications in bilinear modular products over a freely chosen field. Field extension and fixed scalar freedom can change the object Morgenstern would have to bound. |
| Morgenstern 1973 / Schoenhage-Strassen 1971 | A2, A3, A7 | Translatable with cost | Both are coordinate-sensitive and operational in spirit. The currencies differ: bounded linear additions versus head movements/gates/bit operations. A bridge would need a theorem translating bit-operation implementations into bounded-coefficient linear steps, or conversely bounding the bit cost of bounded-linear circuits. |
| Winograd 1978 / Schoenhage-Strassen 1971 | A1, A2, A5, A7 | Translatable with cost | Schoenhage-Strassen uses FFT/CRT ideas adjacent to Winograd, but it adds an operational cost model. Winograd's free constants and field extensions must be represented as bit operations or ring operations before the cost comparison is meaningful. |

The split that matters most for the program is A4: whether linear
change-of-form is free. AFW and Winograd become powerful by allowing
algebraic changes of form that are harmless for multiplicative
complexity. `V_cert` and the counting tasks care about cellwise
certification and positional data. For them, a change of basis is not
neutral unless the transformed certificates are recovered and charged.

The second load-bearing split is A2/A3: whether large constants or
unbounded linear combinations can absorb the algebraic content. This is
Morgenstern's positive lesson. The bounded-coefficient hypothesis is not
a cosmetic restriction; it is the step in the determinant proof that
prevents volume growth from being hidden in coefficients.

The third split is A7: whether a fixed-size construction is allowed to
carry uncharged advice. The Kraft side of the program cannot use a
per-size family without paying for the family description.

## Relation To The Program Coordinate

The program coordinate is closest to Schoenhage-Strassen on A3, A4, and
A7:

- primitive cost is operational rather than purely algebraic;
- arbitrary linear transforms are not one free primitive;
- the model should be uniform in input size.

But Schoenhage-Strassen is not the program coordinate. It does not pay
algebraic height, does not define paid algebraic adjunctions, does not
track root isolation by certification depth, and proves an upper bound
for integer multiplication rather than a lower bound for T1/T3 or
`V_cert`.

Morgenstern supplies the strongest existing witness for why A2/A3 must
be certification-preserving. Its determinant argument shows that a
linear lower bound survives when coefficients are bounded and collapses
when they are not. But it is not a certificate-production model: it has
no paid adjunctions, no root isolation, no height ledger, no uniform
compiler, and no task reduction to T1/T3.

Winograd supplies the clean cyclotomic factor ledger. The witness is
`mu(T_P) = 2n - k`, with `P = u^N - 1` giving the cyclotomic factors
`Phi_d` and the count `2N - d(N)` in the multiplication-counting
convention. But Winograd's framework is too permissive on constants and
field choice to be imported as a certification-cost lower bound.

AFW supplies the strongest structural decomposition: finite-abelian DFTs
reduce, up to rational equivalence, to semisimple cyclotomic algebra
systems whose multiplicative complexity is computable. But AFW's
rational-equivalence quotient is exactly what makes it dangerous for
`V_cert`: it can preserve multiplicative complexity while discarding the
cellwise and positional information the program wants to charge.

## Construction Required

The bridge plan cannot be "cite AFW/Winograd/Morgenstern/Schoenhage-
Strassen and transfer the theorem." It must construct a fifth model.

The construction has four parts.

1. **Define the certification-preserving machine.** Specify the seven
   axioms as actual rules: no arbitrary algebraic advice; paid
   adjunctions; algebraic height bounds; binary primitives; paid
   precomputed transforms; field extensions paid by degree; root
   isolation paid by precision and certification depth; uniform
   self-delimiting compilation across `N`.

2. **Operationalize the algebraic ledger.** Convert the Winograd/AFW
   cyclotomic decomposition into objects the program's tasks demand:
   real trace-field certificates, cellwise value data, height witnesses,
   and isolating intervals. This is where `V_cert` enters. Rational
   equivalence is not allowed to erase these data unless recovering them
   is explicitly paid.

3. **Import boundedness as a theorem, not a slogan.** Morgenstern shows
   that bounded coefficients protect determinant growth in linear DFT
   circuits. The program needs either a direct analogue for
   certification-producing algebraic arithmetic, or a reduction from
   T1/T3 plus `V_cert` to a bounded-linear problem in which Morgenstern's
   determinant mechanism applies without circularity.

4. **Uniformize the cost accounting.** Schoenhage-Strassen shows what a
   uniform operational FFT construction looks like. The program needs a
   uniform compiler for its certificate-producing algorithms, ideally
   compatible with Kraft accounting. AFW and Winograd do not provide this;
   Morgenstern does not provide this; Schoenhage-Strassen provides the
   operational template but not the certificate lower bound.

## Source Inputs To The Construction

| Source | What it contributes | What it cannot supply |
| --- | --- | --- |
| AFW 1984 | Semisimple cyclotomic decomposition of finite-abelian DFTs; computable multiplicative complexity under rational equivalence. | Certification-cost model; paid constants; real-subfield `K_n` result; positional/cellwise preservation; uniform Kraft accounting. |
| Morgenstern 1973 | Bounded-coefficient determinant lower-bound mechanism; precise reason unbounded coefficients collapse additive lower bounds. | Algebraic-height accounting; adjunction cost; root isolation; nonlinear/certificate lower bound; uniformity. |
| Winograd 1978 | Modular-product theorem `mu(T_P) = 2n - k`; CRT/cyclotomic factor ledger; cyclic-convolution-to-DFT construction. | Certification-preserving constants; paid field extensions; additive/bit lower bound; uniform Kraft accounting. |
| Schoenhage-Strassen 1971 | Operational uniform model; bit/gate primitives; FFT over a representation where root multiplication is cheap by construction. | Lower bound; algebraic certificate ledger; paid adjunctions; height and certification-depth root isolation. |

## Load-Bearing Claim

The program's compute-cost branch should no longer be described as
"transporting FFT complexity to the circle side" without qualification.
The precise claim is:

> Existing FFT-complexity papers supply four incompatible or only
> cost-translatable coordinates in the seven-axiom space. The circle-side
> certification-preserving model is a fifth coordinate. The bridge work is
> to build that fifth coordinate by combining AFW/Winograd cyclotomic
> structure, Morgenstern boundedness, and Schoenhage-Strassen operational
> uniformity, while paying the algebraic certification costs that all four
> papers omit or quotient.

This is why the bridge is construction rather than import.

## Trust Boundary

This memo may be cited for the five-coordinate comparison, the named
axiom splits, and the construction agenda above.

It should not be cited as proving:

- a lower bound for T1/T3;
- a primitive-operation lower bound for `V_cert`;
- a conversion theorem from AFW or Winograd multiplicative complexity to
  certification-preserving algebraic arithmetic;
- a real-subfield `K_n` version of any of the four FFT results;
- a Kraft theorem for any of the four source frameworks.

Those remain bridge tasks.
