---
title: Four-folds in positive characteristic and mixed characteristic
nodes: [MMGSDKRGR6]
sources: [KM98]
reads_with: []
requires: ["11"]
level: research
kind: survey
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Four-folds in positive characteristic and mixed characteristic

### Statement

The map has no node for the problems of this section. The records state them as targets of route R7.

**Conjecture 17.5.4 (The 4-fold program for $p > 5$).** The minimal model program holds for lc $\mathbb{Q}$-factorial 4-fold pairs over a perfect field of characteristic $p > 5$.

The records do not state this conjecture in one sentence. Target O-R7-3 asks for it conditional on log resolutions, stated as a reduction (difficulty 3).

**Conjecture 17.5.5 (ACC for log canonical thresholds of 4-folds in characteristic $p$).** The log canonical thresholds of 4-fold pairs in characteristic $p$ satisfy the ACC.

This is target O-R7-4 (difficulty 4). In characteristic 0 the ACC holds in every dimension.

**Theorem 17.5.6 (ACC for log canonical thresholds).** In characteristic 0, the ACC holds for log canonical thresholds in each dimension, for coefficients in DCC sets.

Node: MMGSDKRGR6 · Lean: `MinimalModel.ACCLct`

**Conjecture 17.5.7 (The arithmetic 3-fold program in residue characteristic 2 and 3).** The minimal model program holds for arithmetic 3-folds with residue characteristics 2 and 3.

This is target O-R7-6 (difficulty 4). It is open.

### Proof in words

**Why 4-folds are hard.** Resolution of singularities is open in characteristic $p$ in dimension at least 4 (spec 01.4). Each proof of the program in dimension 4 must assume log resolutions, or avoid them. Spec 04.8 calls the obstruction for the mathematics "no resolution in dim $\ge 4$, and no vanishing".

**What is known in dimension 4.**

- Hacon and Witaszek (arXiv:2009.02631) give contractions to $\mathbb{Q}$-factorial 4-folds and the semistable 4-fold program for $p > 5$, partly conditional on log resolutions [P].
- Waldron (arXiv:2608.14236) proves a cone theorem for lc $\mathbb{Q}$-factorial 4-fold pairs for $p > 5$, under the log resolution conjecture [P].

The records give no claim of 2025 or 2026 for 4-folds in characteristic $p$.

**Mixed characteristic.**

- Residue characteristic 0 or more than 5: BMPSTWW give the program for arithmetic 3-folds (arXiv:2012.15801, Publ. IHES 138 (2023)) [P]. The records name the authors by these initials only.
- Residue characteristic 5: Xie and Xue (arXiv:2201.08208, a preprint) [P].
- Residue characteristic 2 and 3: Takamatsu and Yoshikawa treat semistable families (arXiv:2012.07324) [P]. The general case is O-R7-6.

**Foliations in characteristic $p$.** Bernasconi (arXiv:2309.13978) shows that the cone theorem, the base point free theorem and the existence of Mori fibre spaces fail for 1-foliated surface pairs with canonical singularities in characteristic $p$ [P]. So the program for foliations (Chapter 6) does not carry over.

**Moduli.** KSBA moduli in characteristic $p$ is target O-R7-7. Spec 01.8 says that the subject was not checked in the session of the report [U] (Section 4.3).

### Examples

The first test case of the 4-fold program is O-R7-3: the reduction "log resolutions give the 4-fold program for $p > 5$", with the results of Waldron and of Hacon and Witaszek as its inputs. The first node is `red-waldron`.

The first test case in mixed characteristic is O-R7-6, with the semistable case of Takamatsu and Yoshikawa as the known instance.

### Lean

The library has no statement of this section on 2026-11-26. The project and its sibling project on singularities (spec 2161) share one hypothesis, `MinimalModel.HasLogResolution` (spec 06.1), and one record in both maps. `MinimalModel.HasLogResolution` is in `records/lean.json`. The first node of R7 is `has-log-resolution`, shared with spec 2161. A Lean statement of O-R7-3 is an implication with `HasLogResolution` as a hypothesis.

`MinimalModel.ACCLct` is stated for a field of characteristic 0 (`CharZero k`). A statement of O-R7-4 needs the field of S58, with `CharP k p` and `PerfectField k` (spec 06.2.3).

### Notes and history

**Claims of 2025 and 2026.** The records hold no claim for 4-folds in characteristic $p$ or for mixed characteristic.

**Routes.** Route R7 (weight 0.05) has O-R7-3, O-R7-4, O-R7-6 and O-R7-7, with the first nodes `has-log-resolution` and `red-waldron`.

**References.** KM98; arXiv:2009.02631 (Hacon and Witaszek); arXiv:2608.14236 (Waldron); arXiv:2012.15801 (BMPSTWW); arXiv:2201.08208 (Xie and Xue); arXiv:2012.07324 (Takamatsu and Yoshikawa); arXiv:2309.13978 (Bernasconi). Volume 11 treats the mixed characteristic program and the counterexamples for 1-foliations.

**Questions for a reader.**

- Which steps of the 4-fold program for $p > 5$ need log resolutions, and which need only the cone theorem of Waldron?
- Does the method of Takamatsu and Yoshikawa for semistable families extend to all arithmetic 3-folds of residue characteristic 2 and 3?
- What is the exact form of the log resolution hypothesis that the two projects share?
