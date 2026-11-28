---
title: The generalized program and its claims
nodes: [MMQMD68H79, MMSH2N59E3, MMDQRR7TZB, MME79K17YJ]
sources: [BZ16, BCHM10, Bir12, HX13, Mor25, OAI26]
reads_with: []
requires: ["9", "10", "16.1"]
level: research
kind: survey
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The generalized program and its claims

### Statement

The generalized program runs the minimal model program for $K_X + B + M$ in place of $K_X + B$. A step is an extremal contraction for a $(K_X + B + M)$-negative ray, followed by a flip when the contraction is small. The cone theorem and the contraction theorem hold for glc generalized pairs in the form needed, by reduction to pairs. The existence of flips is the first question that needs new work, because the nef part does not live on $X$.

**Theorem 16.1.9 (generalized flips with NQC, Hacon and Liu).** Let $(X, B + \mathbf{M})$ be a $\mathbb{Q}$-factorial gklt generalized pair with NQC nef part, projective over $Z$, and $X \to W$ a flipping contraction of a $(K_X + B + \mathbf{M}_X)$-negative extremal ray. Then the flip exists.

Lean: not yet in Lean.

This is Hacon-Liu, arXiv:2105.13590, as spec 01.2 gives it: flips exist for klt NQC generalized pairs. For usual pairs ($\mathbf{M} = 0$) flips exist in the lc case by refereed work.

**Theorem 16.1.10 (existence of lc flips, Birkar; Hacon and Xu).** Let $(X, \Delta)$ be a projective lc pair and $f \colon X \to Z$ a flipping contraction. Then the flip of $f$ exists.

Node: MMDQRR7TZB · Lean: `MinimalModel.LcFlips`

**Remark 16.1.11 (claim C5: lc generalized flips, Hu and Liu).** Flips exist for all lc generalized pairs, with no NQC hypothesis and no $\mathbb{Q}$-factorial hypothesis. For lc generalized pairs, the existence of minimal models is equivalent to the termination of the program with scaling.

Node: MMQMD68H79

Lean: not yet in Lean.

This is statement S27, claimed by Hu and Liu (arXiv:2603.03817). It is unrefereed and claimed.

**Remark 16.1.12 (claim C17: finite generation fails, Liu and Wang).** There is a projective klt generalized pair whose generalized lc ring $\bigoplus_m H^0(X, \lfloor m(K_X + B + \mathbf{M}_X) \rfloor)$ is not finitely generated.

This is claimed in arXiv:2608.03258, which says that it is "mostly AI-generated, human-verified". The records give it no node. If the claim holds, the analogue of the finite generation theorem of BCHM fails for generalized pairs, and the generalized program cannot end with a canonical model in the usual way.

**Conjecture 16.1.13 (generalized abundance, Lazić and Peternell).** Let $(X, \Delta)$ be a projective klt pair with $\Delta$ a $\mathbb{Q}$-divisor and $K_X + \Delta$ pseudo-effective. Let $L$ be a nef Cartier divisor such that $K_X + \Delta + L$ is nef. Then $K_X + \Delta + L$ is numerically equivalent to a semiample $\mathbb{Q}$-divisor.

Node: MMSH2N59E3 · Lean: `MinimalModel.GeneralizedAbundance`

This is statement S45. It is open for $\dim X \ge 3$. It is the shadow of generalized pairs in the abundance problem: $(X, \Delta + L)$ is a generalized pair with $X' = X$ and nef part $L$, and with $L = 0$ the conjecture is abundance up to numerical equivalence. OpenAI family 036 claims it (claim C6), with no Lean. It is claimed there and open in the records.

### Proof in words

**Flips with NQC.** The records of the project give the theorem of Hacon and Liu as a statement only; they do not describe its proof, and nobody has read the paper for the project. What the definitions show is where the NQC condition enters. A nef part that is a nonnegative combination of nef $\mathbb{Q}$-divisors can be perturbed by small rational amounts and still be nef, so the questions about it become questions about rational data. A real nef class on an irrational boundary ray of the nef cone, as in the example on $E \times E$ of Section 16.1.1, has no such perturbation inside its ray.

**Termination.** For NQC generalized pairs, Chen and Tsakanikas (arXiv:2011.02236) extend Moraga's termination of pseudo-effective lc 4-fold flips (Mor25) to generalized pairs, as spec 01.2 records. The statement for usual pairs is S21.

Node: MME79K17YJ · Lean: `MinimalModel.TerminationPseffLc4`

**The claim C5.** The records give the shape of C5 only through target O-R1-8 of route R1: the statement, and the equivalence "minimal models if and only if termination with scaling" as a reduction node, with mathematical difficulty 3 and formal difficulty 4. The records do not describe the inner steps of the proof.

**The claim C17.** Target O-R1-7 is the explicit example of Liu and Wang and the computation of its generalized lc ring, of mathematical difficulty 2 and formal difficulty 3. A counterexample of this kind is the best case for route R1: it is finite, and a check of it is a check of the whole claim.

### Examples

**Example 16.1.14 (the nef part decides the step).** Let $Y = \mathrm{Bl}_p \mathbb{P}^2$, with $H$ the pullback of a line, $E$ the exceptional curve and $F = H - E$ the class of a fibre of $Y \to \mathbb{P}^1$. Take $B = 0$ and the nef part $\mathbf{M}$ that descends to $Y$ with $\mathbf{M}_Y = aF$, $a \ge 0$. Then $K_Y = -3H + E$ and
$$K_Y + \mathbf{M}_Y = (a - 3) H + (1 - a) E, \qquad (K_Y + \mathbf{M}_Y) \cdot E = a - 1, \qquad (K_Y + \mathbf{M}_Y) \cdot F = -2.$$
The cone of curves of $Y$ has the two rays $[E]$ and $[F]$. For $a < 1$ both rays are negative, and the program may contract $E$. The result is the generalized pair $(\mathbb{P}^2, 0 + \mathbf{M})$ with $\mathbf{M}_{\mathbb{P}^2} = aH$, which still remembers the model $Y$: its generalized discrepancy along $E$ is $1 - a$, from $B_Y = (a - 1)E$. Then $K + \mathbf{M}_{\mathbb{P}^2} = (a - 3)H$ is anti-ample, and the program ends with a Mori fibre space over a point. For $a > 1$ the ray $[E]$ is positive, so the only step is the Mori fibre space $Y \to \mathbb{P}^1$. The same variety and the same boundary give different programs for different nef parts.

**Example 16.1.15 (the glc bound in the last example).** In the last example, $(\mathbb{P}^2, 0 + \mathbf{M})$ is glc if and only if $a - 1 \le 1$, that is $a \le 2$, and gklt if and only if $a < 2$. For $a = 3$ this is the example after the lemma of Section 16.1.1. So contracting $E$ for $a \ge 2$ would leave the class of glc generalized pairs, but this never happens in the program: for $a > 1$ the curve $E$ is $(K + \mathbf{M})$-positive and the program does not contract it. This is the generalized form of the fact that a step of the program keeps a pair lc.

### Lean

On 2026-11-28 the library mmp-lean states S26 (`MinimalModel.LcFlips`), S21 (`MinimalModel.TerminationPseffLc4`) and S45 (`MinimalModel.GeneralizedAbundance`, in `MinimalModel/Statements/Abundance.lean`) as definitions of type `Prop`, with no proof. A `git grep` of the library finds no declaration `GeneralizedLcFlips`: spec 06.2 lists S27 with vocabulary "missing (generalized pairs)" and plans it at milestone S3. The theorem of Hacon and Liu and the claim C17 have no Lean statement.

### Notes and history

**Status of the records on 2026-11-28.**

| Claim | Source | Statement | Record | Status |
|---|---|---|---|---|
| C5 | Hu-Liu, arXiv:2603.03817 | S27 | `claims/arXiv-2603-03817.yaml` | fresh |
| C6 | OpenAI family 036 | S45 | `claims/openai-math.yaml` | fresh |
| C13 | BFMT; Hu-K. Liu-Shen | S47 | `claims/arXiv-2508-19215.yaml`, `claims/arXiv-2611-12744.yaml` | fresh |
| C17 | Liu-Wang, arXiv:2608.03258 | none | `claims/arXiv-2608-03258.yaml` | fresh |

Each record says: "Nobody has read the claim for the project yet." No part of any of them is checked.

**References.** BZ16 for the definitions; Hacon-Liu, arXiv:2105.13590, for NQC generalized flips; Chen-Tsakanikas, arXiv:2011.02236; Mor25; Bir12 and HX13 for lc flips; BCHM10; OAI26 for the OpenAI release, of which family 036 is a part.

**Questions for a reader.**

- Does the claim C5 use the NQC flips of Hacon and Liu as an input, or does it give a new proof of them?
- Is the example of C17 NQC? If it is, the failure of finite generation is not explained by irrational nef classes.
- Which statements of the generalized program would C5 and C17, taken together, leave open?
