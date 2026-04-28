# rotations

Irrational-rotations and Kronecker-sequence literature import for the
program. Sibling to `fft/` (FFT-complexity import) and `iso/`
(isoperimetric import); all three folders hold imported reads and the
program's syntheses on top of them, in different content domains.

The unifying object across the briefs in this folder is the
**continued-fraction convergents `p_n/q_n` of an irrational `α`** and
the Kronecker sequence `nα mod 1` they organize. Different perspectives
read the same arithmetic substrate: spectral (almost-Mathieu),
combinatorial (three-distance theorem), algorithmic (table-maker's
dilemma), computational (Gosper). The crosswalk memo names the
unification.

Contents:

- `CONTINUED-FRACTIONS-CROSSWALK.md` — meta-document on
  continued-fraction convergents as the recurring primitive across
  four independent memos (this folder's two briefs plus
  Landfall's Gosper finite-closure template and the Lefèvre–Muller pseudocode
  embedded in `3DT-BRIEF.md`).
- Source-extraction briefs:
  - `10-MARTINIS-BRIEF.md` — Avila–Jitomirskaya almost-Mathieu;
    `β(α) = limsup (ln q_{n+1}) / q_n` Liouville/Diophantine cut.
  - `3DT-BRIEF.md` — Three-Distance Theorem (Berthé–Reutenauer
    combinatorial; Lefèvre–Muller algorithmic; Marklof–Strömbergsson
    lattice-geometric).

A cross-source synthesis on top of the briefs is not yet written; it
would be the analog of `fft/FOUR-FRAMEWORK-SYNTHESIS.md` or
`iso/THREE-REGISTER-SYNTHESIS.md`. The crosswalk memo is partial
pre-work toward such a synthesis.

New briefs follow `CONTRIBUTING.md` source-extraction register;
L-W-safety audit per `memos/OLD-TIME-RELIGION.md`; trust boundary
explicit per brief.

Adjacent material kept elsewhere:

- `iso/BECK-1994-BRIEF.md` — probabilistic Diophantine approximation
  on Kronecker sequences. Stays in `iso/` because its primary role
  there is as Thread 3 of the three-thread isoperimetric chain
  (gap-as-discrepancy reading); the rotations/ folder holds the
  explicitly-rotations-themed material that doesn't dual-purpose into
  another register.
- `fft/LANDFALL-PROOF-TEMPLATES.md` Template 3 — Gosper's
  continued-fraction transducer, computational perspective on the same
  CF substrate.
