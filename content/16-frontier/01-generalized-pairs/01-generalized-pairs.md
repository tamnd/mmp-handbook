---
title: Generalized pairs and the canonical bundle formula
nodes: [MMRXDSNJQ7]
sources: [BZ16, KM98, Bea96, Laz04]
reads_with: []
requires: ["1.3", "4.1", "9"]
level: research
kind: survey
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Generalized pairs and the canonical bundle formula

### Statement

In this chapter $k$ is an algebraically closed field of characteristic 0. A *b-divisor* $\mathbf{M}$ on a normal variety $X$ is a choice of an $\mathbb{R}$-divisor $\mathbf{M}_Y$ on each normal variety $Y$ with a proper birational morphism $Y \to X$, compatible under push-forward: if $Y' \to Y$ is a morphism over $X$, then $\mathbf{M}_{Y'}$ pushes forward to $\mathbf{M}_Y$. The divisor $\mathbf{M}_Y$ is the *trace* of $\mathbf{M}$ on $Y$. The b-divisor *descends* to $Y$ if $\mathbf{M}_Y$ is $\mathbb{R}$-Cartier and $\mathbf{M}_{Y'}$ is its pullback for every higher $Y'$.

**Definition 16.1.1 (generalized pair, after Birkar and Zhang).** A *generalized pair* $(X, B + \mathbf{M})$ over a variety $Z$ is a normal variety $X$ with a projective morphism $X \to Z$, an effective $\mathbb{R}$-divisor $B$ on $X$, and a b-divisor $\mathbf{M}$ on $X$ that descends to some model $f \colon X' \to X$ with $\mathbf{M}_{X'}$ nef over $Z$, such that $K_X + B + \mathbf{M}_X$ is $\mathbb{R}$-Cartier. The divisor $B$ is the *boundary part* and $\mathbf{M}$ the *nef part*. The pair is *NQC* if $\mathbf{M}_{X'}$ is a combination with nonnegative real coefficients of $\mathbb{Q}$-Cartier divisors that are nef over $Z$.

With $\mathbf{M} = 0$ a generalized pair is a pair. In practice one writes $(X, B + M)$ with $M = \mathbf{M}_X$, and keeps the model $X'$ and the nef divisor $M' = \mathbf{M}_{X'}$ in the data. The model can always be replaced by a higher one, with the pullback of $M'$.

**Definition 16.1.2 (generalized discrepancy).** Let $(X, B + \mathbf{M})$ be a generalized pair, and $g \colon Y \to X$ a proper birational morphism from a normal variety to which $\mathbf{M}$ descends. Define $B_Y$ by
$$K_Y + B_Y + \mathbf{M}_Y = g^*(K_X + B + \mathbf{M}_X), \qquad g_* B_Y = B,$$
with $K_Y$ and $K_X$ given by the same rational top form. For a prime divisor $D$ on $Y$ the *generalized discrepancy* is $a(D, X, B + \mathbf{M}) = -\operatorname{mult}_D B_Y$. The generalized pair is *generalized lc* (glc) if $a(D, X, B + \mathbf{M}) \ge -1$ for every prime divisor $D$ over $X$, and *generalized klt* (gklt) if $a > -1$ for every such $D$.

The value does not depend on $Y$: on a higher model $Y'$ the trace $\mathbf{M}_{Y'}$ is the pullback of $\mathbf{M}_Y$, so $B_{Y'}$ is the crepant transform of $B_Y$, as in Volume 4, Chapter 1.

**Lemma 16.1.3 (a glc pair has an lc boundary part).** Let $(X, B + \mathbf{M})$ be a glc generalized pair such that $K_X + B$ is $\mathbb{R}$-Cartier. Then $(X, B)$ is lc. If the generalized pair is gklt, then $(X, B)$ is klt.

Lean: not yet in Lean.

*Proof.* The divisor $M = \mathbf{M}_X = (K_X + B + M) - (K_X + B)$ is $\mathbb{R}$-Cartier. Let $g \colon Y \to X$ be a model to which $\mathbf{M}$ descends, and put $E = g^* M - \mathbf{M}_Y$. Then $g_* E = 0$, so $E$ is $g$-exceptional, and $-E = \mathbf{M}_Y - g^* M$ is nef over $X$. By the negativity lemma (KM98, Lemma 3.39), $E \ge 0$. Write $K_Y + B'_Y = g^*(K_X + B)$. Subtracting from the defining equation of $B_Y$ gives $B_Y + \mathbf{M}_Y - B'_Y = g^* M$, so $B'_Y = B_Y - E \le B_Y$. Hence $\operatorname{mult}_D B'_Y \le \operatorname{mult}_D B_Y \le 1$ for every prime divisor $D$ on $Y$, with strict inequality in the gklt case. Every divisor over $X$ lies on such a model $Y$, so $a(D, X, B) \ge a(D, X, B + \mathbf{M}) \ge -1$. $\square$

The converse fails: the nef part can make the generalized pair worse than $(X, B)$. Let $g \colon Y \to \mathbb{P}^2$ be the blow-up of a point with exceptional curve $E$, $H$ the pullback of a line, and $\mathbf{M}$ the b-divisor that descends to $Y$ with $\mathbf{M}_Y = 3(H - E)$, which is nef. Then $\mathbf{M}_{\mathbb{P}^2} = 3H$, and $K_Y = g^* K_{\mathbb{P}^2} + E$ gives $B_Y = 3E - E = 2E$. So $a(E, \mathbb{P}^2, 0 + \mathbf{M}) = -2$, and the generalized pair is not glc, while $(\mathbb{P}^2, 0)$ is smooth.

The first source of generalized pairs is the canonical bundle formula. Let $f \colon X \to C$ be a relatively minimal elliptic fibration of a smooth projective surface onto a smooth projective curve of genus $g$. For a point $P \in C$ let
$$b_P = 1 - \operatorname{lct}(X, f^* P),$$
computed over a neighbourhood of $P$, and let $B_C = \sum_P b_P P$, the *discriminant part*. Let $j \colon C \to \mathbb{P}^1$ be the $j$-invariant of the fibres, and $\mathbf{M}$ the *moduli part*, the b-divisor that descends to $C$ with $12 \mathbf{M}_C \sim_{\mathbb{Q}} j^* \mathcal{O}_{\mathbb{P}^1}(1)$.

**Theorem 16.1.4 (Kodaira's canonical bundle formula).** If $f$ has no multiple fibre, then
$$K_X \sim_{\mathbb{Q}} f^*(K_C + B_C + \mathbf{M}_C),$$
and $(C, B_C + \mathbf{M})$ is a gklt generalized pair. The values of $b_P$ for the fibre types of Kodaira are:

| Fibre | $I_n$ ($n \ge 0$) | $II$ | $III$ | $IV$ | $I_n^*$ ($n \ge 0$) | $IV^*$ | $III^*$ | $II^*$ | $m I_n$ |
|---|---|---|---|---|---|---|---|---|---|
| $b_P$ | $0$ | $\frac16$ | $\frac14$ | $\frac13$ | $\frac12$ | $\frac23$ | $\frac34$ | $\frac56$ | $1 - \frac1m$ |
| $e(F_P)$ | $n$ | $2$ | $3$ | $4$ | $n + 6$ | $8$ | $9$ | $10$ | $n$ |
| pole of $j$ | $n$ | $0$ | $0$ | $0$ | $n$ | $0$ | $0$ | $0$ | $n$ |

Lean: not yet in Lean.

With multiple fibres $m_i F_i$ the formula holds with the coefficient $1 - \frac{1}{m_i}$ at the image point, as the last column gives. For an lc-trivial fibration of any relative dimension the moduli part is a b-nef b-divisor, and the base carries a generalized pair in the same way.

**Remark 16.1.5 (claim C13: b-semiampleness).** The b-semiampleness conjecture of Prokhorov and Shokurov says that the moduli part of an lc-trivial fibration is b-semiample: some multiple descends to a model and is base point free there. Two preprints claim it: BFMT, arXiv:2508.19215, and Hu, K. Liu and Shen, arXiv:2611.12744. It is claimed, not proved; as a refereed result it is open.

Node: MMRXDSNJQ7

Lean: not yet in Lean.

For an elliptic fibration the conjecture is visible: $12 \mathbf{M}_C$ is the pullback of $\mathcal{O}(1)$ by $j$.

### Proof in words

**The formula for an elliptic surface.** On a relatively minimal elliptic surface, $K_X$ is numerically trivial on the fibres, so $K_X = f^*L$ up to the multiple fibres, for a divisor $L$ on $C$. Two inputs fix $L$. The coefficient at $P$ is the log canonical threshold: $(X, f^*P)$ fails to be lc exactly in the amount by which the fibre is worse than a reduced normal crossing fibre, and the table above is the list of these thresholds (a cusp has threshold $\frac56$; a fibre with a component of multiplicity $m$ has threshold $\frac1m$ at a general point of that component). The degree comes from the Euler number. For a fibre that is not multiple, a check of the table gives
$$12 b_P + \operatorname{ord}_P(\text{pole of } j) = e(F_P).$$
Summing over $P$ and using $\sum_P e(F_P) = e(X) = 12 \chi(\mathcal{O}_X)$ (Noether's formula with $K_X^2 = 0$, Bea96) gives
$$12 \deg(B_C + \mathbf{M}_C) = \sum_P 12 b_P + \deg j = 12 \chi(\mathcal{O}_X),$$
so $\deg(K_C + B_C + \mathbf{M}_C) = 2g - 2 + \chi(\mathcal{O}_X)$, which is Kodaira's value of $\deg L$. The formula itself, as a $\mathbb{Q}$-linear equivalence and not only an equality of degrees, is Kodaira's theorem; the local form of the moduli part is the period map of the family.

**The generalized pair on $C$.** All the $b_P$ of the table are less than 1, and $\mathbf{M}_C$ has degree $\frac{1}{12} \deg j \ge 0$, so it is nef. On a curve the generalized discrepancies are the numbers $-b_P$. So $(C, B_C + \mathbf{M})$ is gklt. To read it as a pair one would need an effective divisor in the class of $\mathbf{M}_C$, chosen with care. The generalized pair keeps $\mathbf{M}_C$ as a nef class instead. In higher relative dimension the moduli part need not descend to the base, only to a higher model, and this is why the nef part sits on a model $X'$ in the definition.

### Examples

**Example 16.1.6 (a rational elliptic surface with twelve nodal fibres).** Let $X$ be the blow-up of $\mathbb{P}^2$ at the nine base points of a general pencil of plane cubics, and $f \colon X \to \mathbb{P}^1$ the map to the pencil. Then $K_X = -F$ for a fibre $F$, and $\chi(\mathcal{O}_X) = 1$, so $e(X) = 12$. A general pencil has twelve singular members, each a nodal cubic, of type $I_1$. So $b_P = 0$ for all $P$, $B_C = 0$, and $\deg j = 12$, so $\deg \mathbf{M}_C = 1$. The formula reads
$$\deg(K_{\mathbb{P}^1} + B_C + \mathbf{M}_C) = -2 + 0 + 1 = -1,$$
and indeed $K_X = -F = f^* \mathcal{O}(-1)$. The generalized pair $(\mathbb{P}^1, 0 + \mathbf{M})$ has $K + B + M$ of degree $-1$, as it must for a surface with $\kappa(X) = -\infty$.

**Example 16.1.7 (a fibration with constant $j$).** Let $X \to \mathbb{P}^1$ be the relatively minimal elliptic surface of the Weierstrass equation $y^2 = x^3 + t$, with $t$ the affine coordinate of $\mathbb{P}^1$. As a rational elliptic surface it has $a_4 = 0$ and $a_6$ of degree 6, here $a_6 = t s^5$ in homogeneous coordinates $[t : s]$. The discriminant is $27 a_6^2$, of order 2 at $t = 0$ and of order 10 at $s = 0$. By Tate's algorithm the fibre at $t = 0$ is of type $II$ and the fibre at infinity of type $II^*$, and all other fibres are smooth. The $j$-invariant is $0$ everywhere, so $\mathbf{M}_C \sim_{\mathbb{Q}} 0$, and
$$B_C = \tfrac16 [0] + \tfrac56 [\infty], \qquad \deg(K_{\mathbb{P}^1} + B_C + \mathbf{M}_C) = -2 + \tfrac16 + \tfrac56 + 0 = -1.$$
The Euler numbers are $2 + 10 = 12$, as Noether's formula asks. Here the whole positivity sits in the boundary part. The two examples have the same $\deg(K_C + B_C + \mathbf{M}_C)$ and opposite splittings between the boundary part and the nef part: this is the reason the canonical bundle formula needs both parts.

**Example 16.1.8 (a nef part that is not NQC).** Let $E$ be an elliptic curve with no complex multiplication and $X = E \times E$. Then $N^1(X)_{\mathbb{R}}$ has dimension 3, the intersection form has signature $(1, 2)$, and the nef cone is the round cone $\{x : x^2 \ge 0, \, x \cdot h \ge 0\}$ for an ample $h$ (Theorem 1.3.25; Laz04, Chapter 1). Its boundary is a circle of rays, and all but countably many of them contain no rational class. Let $M$ be a nonzero class on such an irrational boundary ray, for instance the class of Example 1.3.27 with coordinates $(1, 2, \sqrt 2)$. Then $(X, 0 + M)$, with $X' = X$, is a generalized pair: it is glc, since $X$ is smooth and $B = 0$. It is not NQC. A sum $\sum r_i N_i$ of nef $\mathbb{Q}$-Cartier classes with $r_i > 0$ that lies on an extremal ray of the nef cone has every $N_i$ on that ray, and the ray has no rational point. The NQC condition excludes exactly this kind of nef part.

### Lean

The library mmp-lean has no b-divisors and no generalized pairs on 2026-11-28. Spec 06.2 lists the statement S47 (`BSemiampleness`, the claim C13) with vocabulary "missing (b-divisors)" and plans it at milestone S4. The lemma and the canonical bundle formula of this section are not stated in Lean.

### Notes and history

The definition is Birkar-Zhang (BZ16), where the objects are called generalized polarized pairs; the name generalized pair is now usual. The NQC condition appears in the work of Han and Li on the ACC for generalized pairs, and it is the hypothesis under which most of the generalized program is proved (Section 16.1.2). The negativity lemma is KM98, Lemma 3.39. The fibre types and the canonical bundle formula of an elliptic surface are Kodaira's; see Bea96 for elliptic surfaces and Noether's formula.

**Status of the records on 2026-11-28.** The claim C13 has two records, `claims/arXiv-2508-19215.yaml` (node S47) and `claims/arXiv-2611-12744.yaml`. Both have status fresh and say: "Nobody has read the claim for the project yet." Spec 01.3 describes them as strong human papers whose referee status is not checked. Route R9 has the target O-R9-3, b-semiampleness for Kähler morphisms of relative dimension 1, of mathematical difficulty 2.

**Questions for a reader.**

- Which form of the b-semiampleness conjecture do the two preprints of C13 prove: for lc-trivial fibrations with a klt general fibre, or with an lc one?
- Does b-semiampleness of the moduli part follow, in relative dimension 1, from the $j$-map argument of this section alone, with no Hodge theory?
