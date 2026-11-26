---
title: Fujita freeness and effective non-vanishing
nodes: [MMXQBHJKWR, MMRG60YPYS]
sources: [Ajit26, Laz04]
reads_with: []
requires: ["10", "12"]
level: research
kind: survey
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Fujita freeness and effective non-vanishing

### Statement

**Conjecture 17.4.5 (Fujita freeness).** Let $X$ be a smooth projective variety and $L$ an ample line bundle. Then $K_X + mL$ is base point free for each $m \ge \dim X + 1$.

Node: MMXQBHJKWR · Lean: `MinimalModel.FujitaFreeness`

This is statement S56. It is open in general and known in dimension at most 5.

**Remark 17.4.6 (Claim C14: effective non-vanishing fails in dimension 4).** The Ambro-Kawamata effective non-vanishing conjecture is false in dimension 4, with the example of Ajit as the witness.

Node: MMRG60YPYS · Lean: `MinimalModel.NotEffectiveNonVanishing4`

This is statement S57. The node states the negation of the conjecture. Spec 06.2.2 gives it the class refuted: the literature disproves the conjecture. Spec 06.2.1 keeps the class claimed until a referee accepts the counterexample, so the node has the kind claim. This report follows the records: the conjecture is refuted in dimension 4 by a claimed counterexample, and the counterexample is not refereed.

### Proof in words

**Fujita freeness, by dimension.** Spec 01.9 says that freeness is known for $n \le 5$ [S]. The records give no source for each dimension. Very ampleness, the second conjecture of Fujita, is open [S]. Laz04 treats the conjectures of Fujita.

The claims of 2026 attack the general case in two ways. OpenAI family 038 claims the full conjecture, $m \ge n + 1$ (claim C8). Han (arXiv:2609.01574) claims a linear bound: $K_X + mL$ is free for $m \ge \lceil C_0 n \rceil$ with $C_0 \approx 1.77629$ (row T10-12 of spec 07). Target O-R1-3 states the bound of Han as "$K + 2nL$ is free". An earlier claim of the full conjecture, Chan (arXiv:2411.07129), has a gap that Helmke found [P]. Spec 01.13 counts this gap among the claims of the autumn of 2026 that have already failed or changed.

**Effective non-vanishing, by dimension.** Kawamata proved the conjecture for $\nu(D) \le 2$ [P]. In dimension 4, Ajit (arXiv:2610.09270) claims counterexamples. Spec 01.9 says that the conjecture is false in dimension at least 4, and that only $\nu(D) = 3$ is open [P]. The records do not say which dimensions this open case covers.

The first example of Ajit, as spec 01.9 and target O-R1-1 give it:

- $E$ is the Fermat cubic curve, and $\rho$ is an automorphism of order 3 of $E^4$;
- $X = E^4 / \langle \rho \rangle$ is terminal, with 81 singular points of type $\frac{1}{3}(1, 1, 1, 1)$;
- $3K_X \sim 0$;
- $D$ is an ample Cartier divisor with $D^4 = 72$ and $h^0(mD) = 3(m^4 - 1)$.

At $m = 1$ the formula gives $h^0(D) = 0$. Since $3K_X \sim 0$, the divisor $D - K_X$ is numerically equivalent to $D$, so it is ample too. So $D$ is an ample Cartier divisor on a terminal 4-fold with $D - K_X$ ample and no section. The formula also agrees with Riemann-Roch in its top term: $\chi(mD) = \frac{D^4}{24} m^4 + \dots = 3m^4 + \dots$. The records do not give the other terms.

### Examples

**First test cases.**

- Fujita freeness in general: O-R6-4 (difficulty 3). The questions Q5.10 and Q5.11 of Han, and a better constant $C_0$: O-R6-3 (difficulty 2 and 1). The real analysis and the multiplicity inequality behind $C_0$: O-R1-3 (difficulty 2, formal check 2).
- Fujita very ampleness: O-R6-5 (difficulty 4).
- Effective non-vanishing for $\nu(D) = 3$, first for klt 3-folds with $D$ big: O-R6-1 (difficulty 2).
- The questions of Ajit (O-R6-2, difficulty 2 each): a terminal $X$ with ample $D$, $D - K_X$ ample, $H^0(D) = 0$ and $R(X, D)$ with rational singularities; a klt Fano variety with a nef Cartier $D$ and $H^0(D) = 0$; $H^0(kD) = 0$ for $1 \le k < N$. O-R6-2 is a backup for Target T (Section 3.3).

**The check of C14.** Target O-R1-1 is the first target of the project, because spec 04.2 calls it "a disproof that is finite, new and certain". The part to check is the full first example: the action on $E^4$, the 81 fixed points, $3K_X \sim 0$, $D^4 = 72$ and $h^0(mD) = 3(m^4 - 1)$. The mathematics is a check (difficulty 1). The formal check has difficulty 2: finite arithmetic over $\mathbb{F}_3^4$ and $\mathbb{Z}[\omega]$, plus Riemann-Roch on an abelian 4-fold as a named hypothesis. Lab experiment E3 computes the intersection numbers, the values of $h^0$ by Riemann-Roch or by a count of monomials, and the singularities of each example. Lab experiment E4 searches the weighted hypersurfaces and complete intersections of dimension 3 for the first question of O-R6-2. On 2026-11-26 the lab has no run of E3 or E4.

Milestone S1 (2027-02-28) asks for the check of Ajit (S57, E3) and the letter to the author.

### Lean

On 2026-11-26 the library states S56 as `MinimalModel.FujitaFreeness` in `MinimalModel/Statements/Effective.lean`. It takes a smooth projective variety, a canonical divisor $K$ and an ample Cartier divisor $L$, and asks that $K + mL$ be free for each $m \ge \dim X + 1$. The docstring says that the class stays open until experts accept a proof. The statement has no proof.

`MinimalModel.NotEffectiveNonVanishing4` (S57) is not in `records/lean.json`. The module note of `Effective.lean` says that S57 needs abelian varieties, which are not in `Basic.lean` yet. The node plans the statement for milestone S1. The first nodes of the check are `claim-ajit-env` (the map has it as S57), `ajit-fermat-quotient` (the group, the fixed points and the local types) and `ajit-h0-formula` ($h^0(mD) = 3(m^4 - 1)$ from the invariant part of $H^0$ on $E^4$). Only `claim-ajit-env` is a node on 2026-11-26.

### Notes and history

**Claims of 2025 and 2026.**

| Claim | What it claims | Record | Status |
|---|---|---|---|
| C8, OpenAI 038 | Fujita freeness for $m \ge n + 1$ | `claims/openai-math.yaml` | fresh; no Lean |
| C8, Han | a linear bound, $C_0 \approx 1.77629$ | `claims/arXiv-2609-01574.yaml` | fresh; unrefereed |
| C14, Ajit | counterexamples to effective non-vanishing in dimension at least 4 | `claims/arXiv-2610-09270.yaml`, `papers/Ajit26.yaml` | fresh; v2 of 2026-10-14; "explicit and checkable; read by Totaro" [R] |

Chan (arXiv:2411.07129) is a claim of 2024, so it has no record. Each record says: "Nobody has read the claim for the project yet."

**Routes.** Route R1 (weight 0.20) has O-R1-1 and O-R1-3. Route R6 (weight 0.10) has O-R6-1 to O-R6-5, with the first nodes `env-statement` and `fujita-free-statement`. The lab has E3 and E4.

**References.** Ajit26 (arXiv:2610.09270); Laz04; arXiv:2609.01574 (Han); arXiv:2411.07129 (Chan). The paper record of Ajit26 points to Volume 10.

**Questions for a reader.**

- Which sources prove Fujita freeness in dimensions 3, 4 and 5? The records give the tag [S] only.
- Is the open case $\nu(D) = 3$ of effective non-vanishing open in dimension 4 only, or in every dimension at least 4?
- Does the bound $\lceil C_0 n \rceil$ of Han agree with the form $K + 2nL$ of target O-R1-3?
