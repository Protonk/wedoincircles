# COMPUTE-POINTED-TOWARD-ENEMY

A meta-note on the discipline of *actually running the compute* rather than
architecting around it. Outside the triad; closer kin to Sir Nighteye than
to Lemillion, Creati, or Aizawa.

---

## Nezu (COMPUTE) — executive

**Slogan.** *I am a being that learned how to process. When I tell you
what happens next, I have already played it through.*

**Quirk.** High Specs. The principal of UA: a small creature with an
outsized mind that runs probabilistic projections faster than anyone
around him. The important detail is narrower than "he's smart" — Nezu does
not speculate. He builds the computation and runs it. When he pronounces
an outcome, it is because he has played it through, not because of
intuition or prophecy.

**Discipline.** *Point the compute at the enemy.* No architectural
statement stands as a settled commitment until a compute has been aimed at
the specific problem and executed. The failure mode this discipline
exists to prevent is **architecture-on-the-fly**: increasingly specific
plausible-sounding extensions stacking up without any of them cashed
against arithmetic. An LLM in dialogue is unusually prone to this; it
produces confident language that survives because nothing checks it.

**Domain — things that can be computed against a named target.**

- Symbolic verification of factorizations, identities, series expansions.
- Numerical verification of an asymptotic claim across many orders of
  magnitude.
- Direct computation of heights, norms, minimal polynomials, Mahler
  measures in concrete number fields.
- Explicit next-order coefficients (not estimates).
- Any claim "X equals Y up to explicit correction R of order Z": R is
  written down.

Out of scope — not because illegitimate, but because these are *not
compute* in Nezu's sense:

- Plausibility arguments from structure alone.
- Dimensional reasoning ending in a guessed constant.
- "A theorem would say that..." / "my bet is..." / "almost certainly..."
- Sir Nighteye's foresight. That is upstream — it identifies where the
  compute should be pointed, not what the compute finds.

**Characteristic tools.** Sage at arbitrary precision; `QQbar` for
algebraic-number fieldwork; `CyclotomicField` and trace fields; resultants
/ norms / minimal polynomials; Mahler-measure computation over roots;
Taylor series with explicit remainders; `full_simplify` after trig
substitution; numerical bootstrap of next-order terms for cross-checking
symbolic coefficients.

---

## Why the triad doesn't cover this

PERMEATE saturates — saturation is production, not verification. A
saturation table can confirm that the first few rows hold no surprises; it
does not check whether the architectural claim *about* the table is
mathematically correct.

CREATI writes closed forms — writing is not running. A closed form is an
object; computing its value at a specific instance, expanding it
asymptotically, or matching it against another object is a separate act.

BIND erases shared vocabulary — erasure is discipline over what is
admitted. It does not verify that what is admitted is right.

The triad produces mathematical material subject to three production
disciplines. Nezu runs the material and finds out whether it holds.

---

## The failure mode this memo exists to name

*Architecture-on-the-fly.* Plausible-sounding extensions stacking up
without being checked. Characteristic signs:

- "A theorem would say..." / "my bet is..." / "this almost certainly..."
- Progressively more specific commitments without corresponding compute.
- Increasing confidence of voice without corresponding verification.
- The tell: if asked for the next-order coefficient *right now*, you
  could not produce it.

The remedy is pointing compute once the specification is sharp enough that a script can run.

---

## Provenance

Written after a session in which architecture drifted for several
exchanges — each Q&A level more specific than the last, none verified —
the exchange demanded: *stop asking me, compute.* Two computes were
then pointed at concrete targets and ran to completion:

- [memos/STRIP-H1-HURWITZ-CLOSURE.md](memos/STRIP-H1-HURWITZ-CLOSURE.md).
  Positive verification: the architecture's bilinear-form identification
  held at leading order, and a classical identification fell out of the
  compute (the radial-graph lift is the circumscribed regular `n`-gon)
  that the architecture had not predicted.
- [memos/LIOUVILLE-SCALE-TEST.md](memos/LIOUVILLE-SCALE-TEST.md).
  Negative verification: the architectural hope that cyclotomic-unit
  cancellation might rescue the naive Liouville endgame died on scale,
  universally, for every `n >= 3`.

Both outcomes are the discipline working. The positive one confirms a
sketch; the negative one closes a branch cleanly. Neither is available if
the compute is not pointed. The memo exists so the next time architecture
starts drifting for more than three exchanges, someone invokes Nezu.
