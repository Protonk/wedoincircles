# AGENTS

## Repo character

This is a math-research writing repo. Most work is reading papers, promoting notes into reusable internal references, tightening theorem statements, and keeping the document graph coherent.

Default verification is documentary rather than executable:

- check theorem wording,
- check scope honesty,
- check path and pointer integrity,
- and check whether a note belongs in `sources/`, `memos/`, or `triad/`.

## Triad rule

Program-law and discipline constraints belong in `triad/`, not buried inside source consolidations or paper briefs.

- `CREATI` owns form, closed construction, and identity-level structure.
- `PERMEATE` owns saturation, preparation, and first-witness localization.
- `BIND` owns Erasure, vocabulary hygiene, and primitive-only restatement.

If a note is really making a rule about how the program is allowed to think, it belongs in `triad/`.

## Link hygiene

When moving or renaming a document, sweep the repo for stale paths in the same turn.

This repo has already seen structural moves such as:

- `inspo/` -> `triad/`
- promoted notes moving from `sources/` -> `memos/`

Assume path drift is a live risk. Fix links immediately rather than leaving quiet breakage behind.
