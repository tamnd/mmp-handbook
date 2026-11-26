---
title: The statements and their status
nodes: [MMTJ3YNHTG, MMBTDMD2XP, MMY4HT1Q8M, MMPTP8SV13, MMWK2DDDPC, MMGSDKRGR6, MM861R2D6G, MMDZBZY2BV]
sources: [KM98, BCHM10, Sho04, Mor25, OAI26, AxiomMMP]
reads_with: []
requires: ["0"]
level: research
kind: survey
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The statements and their status

### Statement

**Remark 17.7.1 (The status table by dimension).** The table gives the state of the main steps of the program on 2026-11-26. Each cell gives the literature state first. The brackets give the statement of the map and its Lean status, where the map has a node.

| Setting | Flips exist | Termination | Minimal models | Abundance | Cone theorem | ACC for mld |
|---|---|---|---|---|---|---|
| surfaces | not needed | theorem (S12, stated) | theorem (S12, stated) | theorem (S14, unstated) | theorem (S11, stated) | theorem (Alexeev, rated [U]; no node) |
| 3-folds, characteristic 0 | theorem (S15, stated) | theorem (S16, stated) | theorem (S18, stated) | theorem (S17, unstated) | theorem (S04, stated) | open (S49, open) |
| 3-folds, $p > 5$ | theorem (S58, unstated) | theorem (S58, unstated) | theorem (S58, unstated) | partial; $\nu = 1$ and the lc case for $p > 42$ claimed (C9; no node) | theorem (S58, unstated) | the records do not say |
| 3-folds, $p = 5$ | theorem (S58, unstated) | theorem (S58, unstated) | theorem (S58, unstated) | partial; $\nu = 1$ claimed (C9; no node) | theorem (S58, unstated) | the records do not say |
| 3-folds, $p = 2, 3$ | partial; open (O-R7-2; no node) | partial; open (O-R7-2; no node) | partial; open (O-R7-2; no node) | the records do not say | the records do not say | the records do not say |
| 4-folds, characteristic 0 | theorem (S30 and S26, stated) | partial (S21, stated); lc with rational boundary claimed (S22, claimed) | partial (S33, open); see Section 2.1 | partial; open for $\kappa \le 0$ (S40, open) | theorem (S04 and S05, stated) | open (S49, open) |
| 5-folds, characteristic 0 | theorem (S30 and S26, stated) | partial; big case claimed (S24, claimed) | partial; $\kappa \ge 0$ known (S33, open) | open (S40, open) | theorem (S04 and S05, stated) | open (S49, open) |
| all dimensions, characteristic 0 | theorem (S30 and S26, stated); lc generalized pairs claimed (S27, claimed) | open (S20, open); big case claimed (S25, claimed) | open (S33, open); klt with big boundary a theorem (S31, unstated) | open (S40, open); big case a theorem (S42, stated) | theorem (S04 and S05, stated) | open (S49, open); ACC for lct a theorem (S48, stated) |

The table follows the form of Volume 0, Section 2.4, and the rows and columns of spec 11.6. Chapters 1 to 6 give the sources of each cell. The cells for characteristic $p$ come from Chapter 5. The records give the lc 3-fold program for $p \ge 5$ as one statement, S58, so the five cells of S58 in each row share one node.

**Remark 17.7.2 (The open, conjectural and claimed statements of the map).** Of the 60 statements of the map, 40 have the literature class theorem, 14 have the class conjecture and 6 have the class claimed. These are the 20 statements that are not theorems.

| S | Lean name | Class | Lean status | Section |
|---|---|---|---|---|
| S20 | `Termination` | conjecture | open | 1.1 |
| S22 | `TerminationLc4Rational` | claimed | claimed (stated) | 1.2 |
| S24 | `TerminationBigLe5` | claimed | claimed (stated) | 1.2 |
| S25 | `TerminationBig` | claimed | claimed (stated) | 1.2 |
| S27 | `GeneralizedLcFlips` | claimed | claimed (no statement) | 1.2 |
| S33 | `MinimalModelConj` | conjecture | open | 2.1 |
| S38 | `StrongSarkisov` | conjecture | unstated | 1.3 |
| S40 | `Abundance` | conjecture | open | 2.2 |
| S41 | `NonVanishing` | conjecture | open | 2.1 |
| S45 | `GeneralizedAbundance` | conjecture | unstated | 2.3 |
| S46 | `IitakaConj` | conjecture | unstated | 2.3 |
| S47 | `BSemiampleness` | claimed | claimed (no statement) | 2.3 |
| S49 | `ACCMld` | conjecture | open | 3.1 |
| S50 | `LSCMld` | conjecture | open | 3.2 |
| S51 | `MldBound` | conjecture | open | 3.2 |
| S52 | `HanLiuEncACC` | conjecture | unstated | 3.3 |
| S54 | `IndexConj` | conjecture | unstated | 4.1 |
| S55 | `ConeConj` | conjecture | unstated | 4.1 |
| S56 | `FujitaFreeness` | conjecture | open | 4.2 |
| S57 | `NotEffectiveNonVanishing4` | claimed | claimed (no statement) | 4.2 |

Each Lean name has the prefix `MinimalModel.`. The Lean status counts of all 60 statements are: 22 stated, 8 open, 6 claimed and 24 unstated. No statement is faithful, proved, proved-mod or proved-ext.

### Proof in words

**How a status is computed.** The status of a node is not written by hand (spec 08.3). The builder of the map reads the node and the Lean record `records/lean.json`, and it gives the status by these rules.

- A node with no Lean statement in the record is unstated.
- A node of the class conjecture with a Lean statement is open.
- A node of the class theorem with a Lean statement is stated.
- A node with a Lean proof that has no `sorry` is proved, or proved-mod if the proof has named nodes as hypotheses.
- Faithful needs the fidelity battery F1 to F7 (spec 06.3). On 2026-11-26 the record `records/fidelity.json` is empty, so no statement is faithful.

The builder of the handbook gives the status claimed to each node of the class claimed, also when the node has no Lean statement. So S27, S47 and S57 show the status claimed with no Lean statement behind them. The table above marks them "no statement". A reviewer must decide if the builder must show them as unstated.

**The literature state and the Lean status are two different things.** The literature state says what the mathematics knows. The Lean status says what the library states and proves. A theorem of the literature can be unstated in Lean, as S17, abundance for 3-folds, is. An open conjecture can have a Lean statement, as S20 has. The status table needs both, because route R2 and route R3 can change the Lean status of a cell before the literature state changes.

**Where the records disagree.** The report found these conflicts in the records. It follows the more careful record in each case, and it marks the conflict in the section.

- Minimal models in dimension 4. The docstring of `MinimalModel.MinimalModelConj` and the table of spec 01.1 do not give the same open range (Section 2.1).
- The LSC in dimension 3. Spec 03, Conjecture 3.17, and Volume 1 differ from the table of spec 01.1 (Section 3.2).
- The ACC for mlds. Volume 1, Section 1.5, says open in dimension 4 and higher. The records say open from dimension 3 on (Section 3.1).
- The LSC in Lean. `MinimalModel.LSCMld` quantifies over closed points. The node quantifies over the points of the scheme (Section 3.2).
- Lc abundance for 3-folds with $p > 42$. Spec 01.1 and spec 01.4 give it as proved. The claim record C9 keeps it as a claim (Section 5.1).

### Examples

How to read a cell: termination for 4-folds in characteristic 0. The cell says "partial (S21, stated); lc with rational boundary claimed (S22, claimed)". The literature has a refereed proof for lc 4-folds with $K + \Delta$ pseudo-effective (Mor25), and the library states it as `MinimalModel.TerminationPseffLc4`. The case of every lc 4-fold with rational boundary is claimed by OpenAI 056 and by AxiomMath/MMP, and the library states it as `MinimalModel.TerminationLc4Rational` with the class claimed. The audit of Section 7.3 decides if S22 can move to proved-ext. The cell does not change before the audit passes, whatever the bridge build says (spec 06.6).

How to read a cell with no node: the 3-fold program for $p = 2, 3$. The cell names target O-R7-2 of route R7, but no node. A later report gives the cell a node when the stater role writes one.

### Lean

The Lean record on 2026-11-26 is from the library mmp-lean at commit 6e779d01, built on 2026-11-26 with Lean 4.35.0 and Mathlib v4.35.0. These are the Lean statements of the main cells of the table:

Node: MM861R2D6G · Lean: `MinimalModel.SurfaceMMP`

Node: MMDZBZY2BV · Lean: `MinimalModel.ConeTheoremKlt`

Node: MMTJ3YNHTG · Lean: `MinimalModel.Termination`

Node: MMBTDMD2XP · Lean: `MinimalModel.TerminationLc4Rational`

Node: MMY4HT1Q8M · Lean: `MinimalModel.MinimalModelConj`

Node: MMPTP8SV13 · Lean: `MinimalModel.Abundance`

Node: MMWK2DDDPC · Lean: `MinimalModel.ACCMld`

Node: MMGSDKRGR6 · Lean: `MinimalModel.ACCLct`

S20, S33, S40 and S49 are open conjectures. S22 is claimed. The other three are theorems of the literature that the library states and does not prove.

### Notes and history

**Changes since the last report.** This is the first report, so it has no changes to give. The next report is due at milestone S1 (2027-02-28). It must give the change of each cell and of each count.

**Routes.** All routes change cells of the table. Section 7.4 gives the routes and their weights.

**References.** KM98 and BCHM10 for the program; Sho04 for the reduction of termination; Mor25 for pseudo-effective lc 4-folds; OAI26 and AxiomMMP for claim C1. Volume 0, Section 2.4, has the hand-written form of the table.

**Questions for a reader.**

- Must the builder show a claimed node with no Lean statement as unstated?
- Which cells must the next report split, for example the cell of abundance in dimension 4 by the Kodaira dimension?
- Which record must the project correct for each conflict in the list above?
