---
title: The program volumes
nodes: []
sources: [KM98, BCHM10, Kol92, Mat02, Fuj11]
reads_with: []
requires: []
level: guide
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The program volumes

| | Volume | Level | Pages | Needs |
|---|---|---|---|---|
| 0 | How to read this handbook | guide | 60 | none |
| 1 | Divisors, curves and cones | background | 220 | the P volumes |
| 2 | The MMP for surfaces | core | 380 | 1 |
| 3 | The toric MMP | core | 300 | 1, 2 |
| 4 | Singularities of pairs | core | 420 | 1, 2, 3 |
| 5 | Vanishing theorems and multiplier ideals | core | 210 | 1, 4 |
| 6 | Rational curves and bend-and-break | core | 200 | 1, 2 |
| 7 | Cone and contraction theorems | core | 360 | 4, 5, 6 |
| 8 | Flips, flops and the 3-fold MMP | core | 460 | 3, 4, 7 |
| 9 | BCHM: existence of minimal models | advanced | 440 | 5, 7, 8 |
| 10 | Abundance, termination and the Sarkisov program | advanced | 400 | 9 |
| 11 | The MMP in positive and mixed characteristic | advanced | 380 | 2, 4, 7, 8 |
| 12 | Boundedness, complements and BAB | advanced | 420 | 9, 10 |
| 13 | Moduli of stable varieties | research | 400 | 4, 9, 12 |
| 14 | K-stability and K-moduli of Fano varieties | research | 440 | 4, 7, 12, 13 |
| 15 | The MMP for foliations | research | 360 | 4, 7, 8 |
| 16 | The 2026 frontier: generalized pairs, Kähler spaces, 4-folds | research | 320 | 9, 10, 12 |
| 17 | Open problems | research | 120 | all |

Each program volume lists in its `volume.yaml` the prerequisite chapters it needs. For example, Volume 1 needs P3 Ch. 8 to 12, P4 Ch. 1 to 6 and P7 Ch. 1 to 7.

Some program volumes overlap P7 and P8. The rule that splits the material is this. The P volume gives the absolute case and the smooth case, with full proofs. The program volume gives the relative case, the singular case and the case of pairs, and cites the P volume for the rest. So Volume 1 cites Kleiman's criterion from P7 and proves the relative version.

Volumes 16 and 17 are dated reports. They are written again at each milestone of the project.

### Exercises

1. (A) Use the table to list every volume that Volume 9 needs, directly or through other volumes.
