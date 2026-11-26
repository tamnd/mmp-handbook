---
title: The program for foliations
nodes: [MMRWTZFN7D]
sources: [KM98]
reads_with: []
requires: ["15"]
level: research
kind: survey
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The program for foliations

### Statement

**Theorem 17.6.1 (The program for algebraically integrable foliations).** The minimal model program holds for algebraically integrable foliations.

Node: MMRWTZFN7D · Lean: `MinimalModel.AlgIntFoliationMMP`

This is statement S60. The records give it the class theorem, after Liu, Meng and Xie (Compositio 161 (2025), arXiv:2404.01559) and CHLMSSX (arXiv:2408.14258, 2504.10737). The records name the authors of the second source by these initials only.

**Conjecture 17.6.2 (The program for general foliations in dimension at least 4).** The minimal model program holds for foliations on varieties of dimension at least 4.

The map has no node for this problem. It is target O-R8-5 (difficulty 5), and it is open.

**Conjecture 17.6.3 (lc foliated flips).** Flips exist for foliated lc pairs.

Spec 11 lists "lc foliated flips" as an open problem of this volume. The records of the project do not say more: they give no statement, no class of foliations, no dimension and no source for this problem. The statement above is the plain reading of the words of spec 11, and a reader must fix it against a source.

### Proof in words

**What is known, by dimension and rank** (spec 01.6):

- **Surfaces.** The program holds for foliations on surfaces (McQuillan, Brunella) [S].
- **3-folds.** The program holds for foliations of rank 1 and rank 2 on 3-folds (Cascini-Spicer, Spicer-Svaldi, and others) [S].
- **Algebraically integrable foliations, each dimension.** These foliations, and the adjoint structures $t K_{\mathcal{F}} + (1 - t) K_X$, have a program in every dimension (S60) [P]. Abundance for klt algebraically integrable adjoint foliated structures holds in dimension at most 3 (Liu and Xu, arXiv:2510.04419, to appear in Math. Ann.) [P].
- **General foliations, dimension at least 4.** Only partial results: a cone theorem for rank 1, the uniqueness of the outputs of the rank 1 program (arXiv:2608.09663), and minimal models for smooth foliations of corank 1 and of general type (Cascini and Spicer, arXiv:2610.16727) [P][S].

Spec 04.9 names the obstruction for the mathematics: there is no cone theorem in general rank.

In characteristic $p$ the program fails for 1-foliated surface pairs (Bernasconi, arXiv:2309.13978; Section 5.2).

### Examples

The survey of Cascini and Spicer (arXiv:2604.09027) lists precise open questions. Spec 04.9 says that some are about surfaces and are small. Route R8 takes four of them as its first test cases:

- O-R8-1: do the notions of foliation singularity agree on normal surfaces? (Q2.3; difficulty 1)
- O-R8-2: is the lc locus of a foliation Zariski open? (Q3.11; difficulty 2)
- O-R8-3: are canonical foliation singularities non-dicritical, for rank 2 on 3-folds? (Q3.23; difficulty 2)
- O-R8-4: Q6.5 for algebraically integrable foliations (difficulty 2). The records do not give the text of Q6.5.

O-R8-1 is a backup for Target T (Section 3.3), as "a surface question". Volume 15 treats the examples of foliations: the Riccati foliation, and a foliation of degree $d$ on $\mathbb{P}^2$ with $K_{\mathcal{F}} = (d - 1)H$ (spec 11).

### Lean

On 2026-11-26, `MinimalModel.AlgIntFoliationMMP` (S60) is not in `records/lean.json`. The node plans it in `MinimalModel/Statements/OtherSettings.lean` for milestone S6. Its vocabulary is missing, so the node has the status unstated, with `needs` edges to the missing definitions (spec 06.2.2, row G1b). Spec 04.9 says that foliations need the tangent sheaf and saturation. The first nodes of route R8 are `foliation-def`, `foliation-canonical-class` and `cs-q23-statement`. None is a node of the map yet.

### Notes and history

**Claims of 2025 and 2026.** The records hold no claim on foliations.

**Routes.** Route R8 (weight 0.05) has O-R8-1 to O-R8-5.

**References.** arXiv:2404.01559 (Liu, Meng and Xie); arXiv:2408.14258 and 2504.10737 (CHLMSSX); arXiv:2510.04419 (Liu and Xu); arXiv:2608.09663; arXiv:2610.16727 and 2604.09027 (Cascini and Spicer); arXiv:2309.13978 (Bernasconi); KM98 for the program of pairs. Volume 15 treats foliations. At ICM 2026, J. V. Pereira spoke on foliations with numerically trivial canonical bundle (spec 01.10, [S]).

**Questions for a reader.**

- What is the exact statement of the problem "lc foliated flips" that spec 11 means, and for which rank and dimension is it open?
- Which known result is the cone theorem for rank 1 in dimension at least 4, and who proves it?
- What is the text of Q6.5 of the survey of Cascini and Spicer?
