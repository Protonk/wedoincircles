# COST-MODEL-UNIFORMITY-BRIEF

Paired source-extraction brief on:

- **Stephen A. Cook and Robert A. Reckhow**, "Time Bounded Random Access Machines," *Journal of Computer and System Sciences* **7** (1973), 354–375. PDF at [sources/Cook-Reckhow-1973-time-bounded-RAM.pdf](sources/Cook-Reckhow-1973-time-bounded-RAM.pdf).
- **Peter van Emde Boas**, "Machine Models and Simulations (Revised Version)," ITLI Prepublication Series for Computation and Complexity Theory CT-88-05, University of Amsterdam, August 1988 (revised draft of the chapter that appeared as ch. 1 of *Handbook of Theoretical Computer Science, Vol. A: Algorithms and Complexity*, J. van Leeuwen, ed., MIT Press, 1990, pp. 1–66). PDF at [sources/vanEmdeBoas-1988-machine-models-simulations.pdf](sources/vanEmdeBoas-1988-machine-models-simulations.pdf).

**Why this brief exists.** [paper/FIRST-PROOF.md](paper/FIRST-PROOF.md) debt #9 (pending) and [memos/EFFECTIVE-HL-N1-COST-FORM.md](memos/EFFECTIVE-HL-N1-COST-FORM.md) commit the program to a *uniform-charge cost model*. That commitment is not program-internal vocabulary: charging-granularity-as-modeling-choice is Cook–Reckhow 1973, and complexity-classes-invariant-under-reasonable-charging is the Slot–van Emde Boas **Invariance Thesis** as surveyed in van Emde Boas 1988/1990. This brief anchors both, calls out one terminology pitfall, and draws the trust boundary.

**What was read.** Cook–Reckhow pp. 354–356 thoroughly (abstract, intro, Table I of instruction times, definition of `l(n)`); proofs of the simulation theorems and the hierarchy theorem skimmed at the level needed to confirm the abstract's claims. Van Emde Boas pp. 1–3 (cover, abstract); body sections on the Invariance Thesis and First Machine Class read selectively; the parallel-machines material (Second Machine Class) noted but not relied on.

**Confidence level.** High on the brief's direct quotations (each has a page anchor). High on the abstract-level claims of both papers. Medium on the program-side mapping, which is the brief's inference. The terminology-pitfall callout below is the brief's contribution; both papers share blame for the confusion only in the sense that "uniform" gets used for two different things.

---

## Main content of each paper

### Cook–Reckhow 1973 — charging granularity (proved)

The paper introduces a Random Access Machine (RAM) abstract model and proves simulation theorems relating it to multitape Turing machines. The load-bearing methodological move is at p. 355:

> "The random access storage is unlimited, and the word length is unlimited, although we propose making a time charge roughly equal to the logarithm of the magnitude of each number placed in storage. This is like charging for the number of words required to store a high precision number on a fixed wordsize machine."

The charge is parameterized by a function `l(n)` (p. 355):

> "Associated with the machine is the function `l(n)` which, roughly speaking, denotes the time required to store the number `n`. The most natural values for `l(n)` are (1) take `l(n)` identically one, and (2) take `l(n)` approximately `log|n|`."

Table I (p. 356) gives execution times of the RAM's primitive instructions, each in terms of `l` of the operand sizes. Definition at p. 356:

> "`l(n) = ⌈log₂|n|⌉` if `|n| ≥ 2`; `1` if `|n| < 2`. We will call this the *logarithmic function*."

Motivation (p. 356):

> "Briefly, the reason for taking `l(n)` logarithmic instead of constant is that each register is allowed to hold arbitrarily large integers."

The simulation results then give: a `T(n)` time-bounded Turing machine simulates on the RAM in `O(T(n) · l(T(n)))` time; a `T(n)` time-bounded RAM simulates on a Turing machine in `T(n)³` if `l` is constant, `T(n)²` if `l` is logarithmic.

### Van Emde Boas 1988/1990 — the Invariance Thesis (surveyed)

The 1988 preprint is the revised draft of the 1990 Handbook of Theoretical Computer Science chapter (confirmed at the title page: "This paper is the revised draft of a chapter in a forthcoming Handbook of Theoretical Computer Science which will be published by North Holland Publ. Cie. in the fall of 1988"). For program purposes, the two are content-equivalent.

The Invariance Thesis is named verbatim in the abstract:

> "In Complexity Theory the use of informal estimates can be justified by appealing to the **Invariance Thesis** which states that all standard models of sequential computing devices are equivalent in the sense that the fundamental complexity classes don't depend on the precise model chosen for their definition."

The chapter organizes machine models into the **First Machine Class** (sequential models satisfying the Invariance Thesis: multitape Turing machines, RAM/RASP under logarithmic time charging, additive-type RAM/RASP under uniform time plus logarithmic space) and the **Second Machine Class** (parallel models satisfying the Parallel Computation Thesis: parallel time = sequential space up to polynomial). Storage Modification Machines are *not* clean members of the First Machine Class under the plausible space measure (van Emde Boas notes their inclusion would require an unnatural logarithmic space measure). Models outside both classes — including non-uniform model families and constructions where the `n → M_n` uniformity map is not assumed — are explicitly noted as "not exhausted" by the two classes.

The thesis itself is cited in the literature as **Slot–van Emde Boas 1984** ("On Tape Versus Core; an Application of Space Efficient Perfect Hash Functions to the Invariance of Space," STOC 1984) for the original formulation; the 1988/1990 chapter is the canonical survey treatment.

---

## What each paper states without our independent check

- Cook–Reckhow's prior-work attributions (Wegbreit, Hartmanis, Stearns, Hopcroft–Ullman simulations) are reported but not independently verified.
- Van Emde Boas's catalogue of First Machine Class members and the specific simulation overhead for each is taken as surveyed; the brief does not re-verify each entry.
- The Slot–van Emde Boas 1984 STOC paper itself is cited via the 1988 chapter; the brief has not separately read the 1984 STOC paper.

The program's use is at the methodological-vocabulary level; none of the unchecked content is load-bearing.

---

## Two flags (load-bearing)

### Terminology pitfall: "uniform" means two different things

Three terminologies cross here, and they don't line up.

- **Cook–Reckhow's *constant* option** (their phrasing, p. 355): take `l(n) = 1`. Each instruction has unit cost regardless of operand size.
- **Van Emde Boas's *uniform measure*** (later survey terminology): the charging convention corresponding to Cook–Reckhow's constant `l(n)` — unit cost per instruction.
- **The program's *uniform-charge cost model*** (debt #9 / EFFECTIVE-HL-N1-COST-FORM): all native operations and all stored bits charged at the same precision granularity.

The program's "uniform-charge" is **not** van Emde Boas's "uniform measure" and **not** Cook–Reckhow's constant `l(n) = 1`. It corresponds to Cook–Reckhow's **logarithmic** choice (`l(n) = ⌈log₂|n|⌉`, named "the *logarithmic function*" at p. 356) — equivalently, van Emde Boas's *logarithmic measure*. The program's "uniform" means *uniform across the storage / operations boundary*, not *uniform across operand sizes*.

Why this matters: under van Emde Boas's "uniform measure" (= Cook–Reckhow's constant `l(n)`), a single instruction manipulates arbitrarily large numbers in unit time — exactly the kind of uncharged advice the program's regularity guard excludes. The program's "uniform-charge" model corresponds instead to the logarithmic measure, where bit-length is paid for.

When citing for the program's cost model, the right phrasing is *charging granularity in the sense of Cook–Reckhow 1973 (logarithmic `l(n)`)* or *the program's uniform-charge model (van Emde Boas's logarithmic measure)*. Avoid bare "uniform" without saying which one.

### Thesis, not theorem

The Invariance Thesis is a *thesis*, not a theorem. Van Emde Boas explicitly frames it as parallel to the Church–Turing thesis: a methodological commitment that justifies informal complexity estimates, validated by the body of simulation results in the surveyed literature, but not provable within complexity theory itself (since it makes a claim about which models count as "reasonable," and "reasonable" is not formalized inside the theory).

The program inherits the Invariance Thesis as **methodological precedent**, the same trust register as Coase 1937 — *vocabulary and discipline, not transferred theorem*. Citing it commits the program to: (a) the First Machine Class — multitape Turing machines, RAM/RASP under logarithmic time, additive RAM/RASP under uniform time plus logarithmic space — simulates internally up to polynomial time and constant-factor space; (b) models outside the First Machine Class fail this invariance, with non-uniform model families a named example; (c) "reasonable" cost models are operationally those that fit the First Machine Class register, with the program's commitment to operate within it. None of (a)–(c) is a theorem the program transfers; they are language and method, validated downstream by van Emde Boas's surveyed simulations rather than proved as part of the thesis itself.

---

## What we infer for the program

The program-to-source mapping is the brief's contribution; neither paper wrote it.

| Program object | Cook–Reckhow / van Emde Boas anchor |
|---|---|
| Uniform-charge cost model | Cook–Reckhow's logarithmic `l(n)` (= van Emde Boas's logarithmic measure); generalized to "all bits and all operations charged at the same precision granularity" |
| Regularity guard ("excluding advice") | Slot–van Emde Boas 1984 / van Emde Boas 1988/1990; non-uniform model families fall outside the First Machine Class. (The "advice-bearing" framing is program-side translation, not source terminology.) |
| Debt #9 commitment | Adopt First Machine Class as the program's hypothesis class; canon's `Ω(n log n)` cluster re-read to confirm thresholds survive logarithmic-cost charging at variable precision |
| "Movement between time and space doesn't change cost class" intuition | The Invariance Thesis itself |

The transfer is at three levels, parallel to the Coase 1937 anchor:

1. **Vocabulary.** "Charging granularity," "uniform charge," "reasonable model," "advice as uncharged information" — Cook–Reckhow and Slot–van Emde Boas. Adopted at debt #9 and EFFECTIVE-HL-N1-COST-FORM.
2. **Typing.** Cost is parameterized by a charging-granularity function `l(n)`; complexity classes are well-defined under any reasonable choice. The program's `cost_total` inherits this typing.
3. **Methodological discipline.** The Invariance Thesis is a *thesis* — informal commitment that justifies later technical work. Debt #9 inherits this register: the cost-model commitment is methodological, not provable; the canon re-read it requires is the technical work.

---

## Trust boundary

### This brief should be cited for

- The two direct quotations from Cook–Reckhow pp. 354 and 355–356 (charging-granularity construct and motivation);
- The Invariance Thesis quotation from van Emde Boas's 1988 abstract;
- The First Machine Class / Second Machine Class organization;
- The mapping table in §"What we infer for the program" above (each row is a defensible analogy, not a transferred theorem);
- The terminology pitfall (uniform-cost RAM ≠ uniform-charge cost model).

### This brief should NOT be cited for

- Any FFT-impossibility content — neither paper contains any;
- Any specific complexity result on cyclotomic DFTs, Morgenstern, AFW, Winograd, Ailon, or the program's `ε` — none of these is in scope of either source;
- The claim that the Invariance Thesis transfers as a theorem — it transfers as methodological precedent;
- The 1984 Slot–van Emde Boas STOC paper at the proof level — the brief has not separately read it.

### Provenance tag for the program

**Cost-model anchor (debt #9).** Cook–Reckhow 1973 supplies the charging-granularity vocabulary (`l(n)`); Slot–van Emde Boas 1984 / van Emde Boas 1988/1990 supplies the Invariance Thesis as the principle that complexity classes are model-independent under reasonable charging. Cited at [paper/FIRST-PROOF.md](paper/FIRST-PROOF.md) debt #9 (pending), [memos/EFFECTIVE-HL-N1-COST-FORM.md](memos/EFFECTIVE-HL-N1-COST-FORM.md) §"Cost-model uniformity," and [fft/LANDFALL-EXTENDED-CAFF-TRANSFER.md](fft/LANDFALL-EXTENDED-CAFF-TRANSFER.md) §"Cost-model uniformity, not table-permissive vs strict." Forward note to [paper/OUTLINE.md](paper/OUTLINE.md) §1 once the prose pass touches the cost-framework setup.

---

## Closing sentence

This brief extracts pp. 354–356 of Cook–Reckhow 1973 and the abstract plus First Machine Class material of van Emde Boas 1988/1990 for the methodological-framework precedent FIRST-PROOF debt #9 inherits: that the First Machine Class is model-independent under reasonable charging (Slot–van Emde Boas Invariance Thesis), that the charging granularity `l(n)` is itself the load-bearing modeling choice (Cook–Reckhow), and that the program's "uniform-charge cost model" is *not* van Emde Boas's "uniform measure" or Cook–Reckhow's constant `l(n)` — it is the *logarithmic* measure / logarithmic `l(n)` reading, with "uniform" naming uniformity across the storage / operations boundary rather than across operand sizes. That three-way terminology distinction is the brief's contribution. The mapping to debt #9 is the brief's inferential work; neither paper wrote it.
