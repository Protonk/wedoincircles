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

- `SIX-LENS-SYNTHESIS.md` — third-register cross-source synthesis on
  top of the briefs: six lenses (Avila–Jitomirskaya, Berthé–Reutenauer,
  Lefèvre–Muller, Marklof–Strömbergsson, Beck, K-H-L-A consumption
  interface) on the continued-fraction convergent substrate. Analog of
  `fft/FOUR-FRAMEWORK-SYNTHESIS.md` and `iso/THREE-REGISTER-SYNTHESIS.md`.
- `CONTINUED-FRACTIONS-CROSSWALK.md` — index meta-document on
  continued-fraction convergents as the recurring primitive across the
  six lenses. Pre-work to the synthesis.
- Source-extraction briefs:
  - `10-MARTINIS-BRIEF.md` — Avila–Jitomirskaya almost-Mathieu;
    `β(α) = limsup (ln q_{n+1}) / q_n` Liouville/Diophantine cut.
  - `3DT-BRIEF.md` — Three-Distance Theorem (Berthé–Reutenauer
    combinatorial; Lefèvre–Muller algorithmic; Marklof–Strömbergsson
    lattice-geometric).
- `BETA-PI-LW-AUDIT.md` — L-W-safety audit on the `β(π) = 0` chain via
  Mahler 1953 / Hata 1993 / Salikhov 2008 plus classical CF algebra.

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
