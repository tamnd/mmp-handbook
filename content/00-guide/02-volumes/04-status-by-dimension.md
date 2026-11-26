---
title: The status table by dimension
nodes: [MM861R2D6G, MM3A98X8YR, MMH0CM56AA, MM5ECX1RGZ, MMTJ3YNHTG, MMBTDMD2XP, MMP51FQ005, MMY4HT1Q8M, MMPTP8SV13, MMDZBZY2BV, MMWK2DDDPC, MMGSDKRGR6]
sources: [KM98, Kol92, KMM87, Sho04, Fuj04, Mor25, BCHM10, Fuj11, OAI26, AxiomMMP]
reads_with: []
requires: []
level: guide
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The status table by dimension

The table gives the state in the literature of the main steps of the program, in November 2026. "Theorem" means a refereed proof. "Open" means an open conjecture. "Claimed" means a recent claim that no referee has checked. "Partial" means that special cases are theorems and the general case is open; the volume in brackets gives the details.

| Setting | Flips exist | Termination | Minimal models | Abundance | Cone theorem | ACC for mld |
|---|---|---|---|---|---|---|
| surfaces | not needed (no small contractions) | theorem | theorem | theorem | theorem | theorem (Alexeev) |
| 3-folds, characteristic 0 | theorem (Mori, Shokurov) | theorem (Shokurov, Kawamata) | theorem | theorem (Miyaoka, Kawamata) | theorem | open |
| 3-folds, $p > 5$ | theorem (Vol. 11) | partial (Vol. 11) | theorem (Vol. 11) | partial (Vol. 11) | partial (Vol. 11) | open |
| 3-folds, $p = 5$ | partial (Vol. 11) | partial (Vol. 11) | partial (Vol. 11) | partial (Vol. 11) | partial (Vol. 11) | open |
| 3-folds, $p = 2, 3$ | partial (Vol. 11) | partial (Vol. 11) | partial (Vol. 11) | partial (Vol. 11) | partial (Vol. 11) | open |
| 4-folds, characteristic 0 | theorem (BCHM for klt; Birkar and Hacon-Xu for lc) | partial; the lc case with rational boundary is claimed | partial (Vol. 10) | open | theorem | open |
| 5-folds, characteristic 0 | theorem | partial | partial (Vol. 10) | open | theorem | open |
| all dimensions, characteristic 0 | theorem | open | open in general; theorem for klt pairs with big boundary (BCHM) | open | theorem (klt: Kawamata, Shokurov; lc: Ambro, Fujino) | open |

Some notes on the rows.

- Termination in dimension 4 is a theorem for terminal 4-folds (Kawamata, Matsuda and Matsuki, KMM87), for canonical 4-folds (Fujino, Fuj04) and for lc 4-folds with $K + \Delta$ pseudo-effective (Moraga, Mor25). Termination for every lc 4-fold with rational boundary is claimed by the OpenAI problem family 056 (OAI26), with a Lean formalization in AxiomMath/MMP (AxiomMMP). No person has reviewed the claim or the code, so the handbook marks it claimed and never uses it as a hypothesis.
- The ACC for log canonical thresholds is a theorem in all dimensions (Hacon, McKernan and Xu). The column gives the ACC for minimal log discrepancies, which is open from dimension 3 on. With the lower semicontinuity of mlds, it implies termination (Shokurov, Sho04).
- The rows for characteristic $p$ are only a pointer in this edition. Volume 11 gives each cell with its references.

The handbook writes this table by hand in this edition. A later builder writes each cell from the records of the map (`records/status.json`), with the Lean status of the node next to the literature state. These are the nodes of the table and their Lean statements:

Node: MM861R2D6G · Lean: `MinimalModel.SurfaceMMP`

Node: MMDZBZY2BV · Lean: `MinimalModel.ConeTheoremKlt`

Node: MMP51FQ005 · Lean: `MinimalModel.KltFlips`

Node: MMTJ3YNHTG · Lean: `MinimalModel.Termination`

Node: MMBTDMD2XP · Lean: `MinimalModel.TerminationLc4Rational`

Node: MMY4HT1Q8M · Lean: `MinimalModel.MinimalModelConj`

Node: MMPTP8SV13 · Lean: `MinimalModel.Abundance`

Node: MMWK2DDDPC · Lean: `MinimalModel.ACCMld`

The nodes for the 3-fold results (flips, termination and abundance in dimension 3) and for the ACC for lct are on the map, and their Lean statements are not written yet:

Node: MM3A98X8YR

Node: MMH0CM56AA

Node: MM5ECX1RGZ

Node: MMGSDKRGR6
