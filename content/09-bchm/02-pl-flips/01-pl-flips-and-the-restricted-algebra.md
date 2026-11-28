---
title: Pl flips and the restricted algebra
nodes: []
sources: [HM07, Cor07, BCHM10, Sho92]
reads_with: [Cor07:2, HM07:5]
requires: [1.1, 3.5, 4.5, 8.1, 8.3]
level: advanced
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Pl flips and the restricted algebra

### Statement

Recall from Definition 8.3.1 that a pl flipping contraction is a small contraction $f \colon X \to Z$ with $\rho(X/Z) = 1$ of a $\mathbb{Q}$-factorial plt pair $(X, S + B)$, $S$ prime and $\lfloor B \rfloor = 0$, with $-(K_X + S + B)$ and $-S$ ample over $Z$. Shokurov's reduction, Theorem 8.3.5, is proved in Volume 8 in every dimension $n \ge 2$: if pl flips exist in dimension $n$ and special termination holds in dimension $n$, then klt flips exist in dimension $n$. This chapter supplies the first hypothesis from finite generation in dimension $n - 1$, and Chapter 3 the second. Throughout, $Z = \operatorname{Spec} A$ is affine, which is no loss, since a flip is constructed locally over $Z$ and is unique (Theorem 8.1.6).

**Definition 9.2.1 (the restricted algebra of a divisor).** Let $X$ be a normal variety projective over $Z = \operatorname{Spec} A$, $S$ a normal prime divisor of $X$ and $D$ a Weil divisor on $X$ whose multiples $mD$ are Cartier near the generic point of every curve of $S$ and with $S \not\subseteq \operatorname{Supp} D$. The *restricted algebra* of $D$ is the graded $A$-algebra
$$\operatorname{res}_S R(X, D) = \bigoplus_{m \ge 0} \operatorname{im} \big( H^0(X, \mathcal{O}_X(mD)) \to H^0(S, \mathcal{O}_S(mD|_S)) \big),$$
the image of $R(X, D) = R(X/Z, D)(Z)$ under restriction of sections, where $D|_S$ is the restriction of $D$ as a $\mathbb{Q}$-divisor on $S$ and a section is restricted as a rational function with poles bounded by $mD$. For $D = S$ this is the algebra $R_S$ of Definition 8.3.3 when $mS$ is Cartier.

**Lemma 9.2.2 (pl flips and restricted algebras).** Let $f \colon X \to Z$ be a pl flipping contraction of $(X, S + B)$ with $Z$ affine, and let $k \ge 1$ be an integer with $k(K_X + S + B)$ Cartier.

1. $K_X + S + B \sim_{\mathbb{Q}} aS + f^* L$ for a rational number $a > 0$ and a $\mathbb{Q}$-Cartier divisor $L$ on $Z$, and the pl flip exists if and only if $R(X/Z, S)$, equivalently $R_S$, equivalently $R(X/Z, k(K_X + S + B))$, is finitely generated.
2. If the pl flip exists, then $\operatorname{res}_S R(X, k(K_X + S + B))$ is a finitely generated $A$-algebra.
3. Conversely, if $\operatorname{res}_S R(X, k(K_X + S + B))$ is finitely generated, then the pl flip exists.

Lean: not yet in Lean.

**Corollary 9.2.3 (klt flips from the induction).** Let $n \ge 2$. If Theorem 9.1.4 holds in dimension $n$ and special termination holds for sequences of flips of $n$-dimensional $\mathbb{Q}$-factorial dlt pairs, then the flip of every flipping contraction of an $n$-dimensional $\mathbb{Q}$-factorial klt pair exists.

Lean: not yet in Lean.

### Proof in words

A pl flip is the flip of the divisor $S$, because $K_X + S + B$ and $S$ are both negative on the one contracted ray and so are proportional up to a pullback from $Z$. The flip of a divisor exists exactly when its divisorial algebra is finitely generated, and for the divisor $S$ itself finite generation can be checked after cutting down to $S$, which is Theorem 8.3.4. If the flip exists the algebra of $K_X + S + B$ is finitely generated, and so is its image on $S$; this is the easy direction. The converse needs a version of Theorem 8.3.4 for a section of $k(K_X + S + B)$ that vanishes on $S$, and is cited.

The corollary is Theorem 8.3.5 with its first hypothesis renamed.

### Examples

**Example 9.2.4 (the toric 4-fold pl flip).** Let $N = \mathbb{Z}^4$ with basis $e_1, \dots, e_4$ and $u_i = e_i$ for $i \le 4$, $u_5 = e_1 + e_2 + e_3 - e_4$, so that $u_1 + u_2 + u_3 - u_4 - u_5 = 0$. Let $\sigma = \operatorname{Cone}(u_1, \dots, u_5)$ and $Z = U_\sigma$. The fan $\Sigma^-$ with the three maximal cones obtained from $\{u_1, \dots, u_5\}$ by omitting one of $u_1, u_2, u_3$, and the fan $\Sigma^+$ with the two maximal cones obtained by omitting one of $u_4, u_5$, are the two simplicial subdivisions of $\sigma$ with no new rays (Theorem 3.5.20); each of the five maximal cones is spanned by a basis of $N$, so $X^\pm = X_{\Sigma^\pm}$ are smooth. The relation vector $r = (1, 1, 1, -1, -1)$ is the class of a torus-invariant curve $C^-$ of $X^-$, with $D_i \cdot C^- = r_i$, so $K_{X^-} \cdot C^- = -\sum r_i = -1$. The exceptional locus of $X^- \to Z$ is $V(\operatorname{Cone}(u_4, u_5)) \cong \mathbb{P}^2$, that of $X^+ \to Z$ is $V(\operatorname{Cone}(u_1, u_2, u_3)) \cong \mathbb{P}^1$, and $X^+$ is the flip of $X^-$.

Take $S = D_4$ and $B = 0$. Then $(X^-, S)$ is plt, as $X^-$ and $S$ are smooth, $S \cdot C^- = -1$ and $(K_{X^-} + S) \cdot C^- = -2$, so $f^- \colon X^- \to Z$ is a pl flipping contraction, and part 1 of Lemma 9.2.2 holds with $a = 2$. The 3-fold $S$ is the toric variety of the star of $u_4$ in $N / \mathbb{Z} e_4$, with rays $\bar e_1, \bar e_2, \bar e_3$ and $\bar u_5 = \bar e_1 + \bar e_2 + \bar e_3$: it is the blow-up $S = \operatorname{Bl}_0 \mathbb{A}^3$, with exceptional divisor $E = D_5|_S \cong \mathbb{P}^2$. On $X^+$ the star of $u_4$ is the single cone $\operatorname{Cone}(e_1, e_2, e_3, e_4)$ and $S^+ \cong \mathbb{A}^3$. So the pl flip restricts on $S$ to the blow-down $\operatorname{Bl}_0 \mathbb{A}^3 \to \mathbb{A}^3$.

The algebras are computed with characters. Write $m = (a, b, c, d) \in M$ in the dual basis, so that $\langle m, u_i \rangle$ is $a, b, c, d$ for $i = 1, \dots, 4$ and $a + b + c - d$ for $i = 5$. A basis of $H^0(X^-, \mathcal{O}(jD_4))$ is given by the characters with
$$a, b, c \ge 0, \qquad d \ge -j, \qquad a + b + c \ge d,$$
and those with $d \ge -j + 1$ span the subspace $H^0(\mathcal{O}((j-1)D_4))$. So $(R_S)_j$ has the basis of characters with $d = -j$ and $a, b, c \ge 0$, the last inequality being automatic, and $R_S \cong k[x, y, z][\tau]$ with $x, y, z$ of degree $0$ and $\tau$ of degree $1$. It is finitely generated, and $\operatorname{Proj}_{\mathbb{A}^3} R_S = \mathbb{A}^3 = S^+$. The divisor $\operatorname{div} \chi^{(0,0,0,1)} = D_4 - D_5$ shows $D_4|_S \sim E$, and by adjunction $(K_{X^-} + S)|_S = K_S = 2E \sim 2S|_S$, as part 1 of Lemma 9.2.2 predicts. The restricted algebra $\operatorname{res}_S R(X^-, K_{X^-} + S)$ is the Veronese subalgebra of $R_S$ in even degrees, $k[x, y, z][\tau^2]$.

**Example 9.2.5 (the Francia flip).** For the Francia flip, Example 8.3.7 shows that $S = D_1$ is the weighted blow-up of $\mathbb{A}^2$ with weights $(1, 2)$, with exceptional curve $C^-$ with $(C^-)^2 = -\frac12$, $K_S \cdot C^- = -1$, so $K_S = 2C^-$ as $\mathbb{Q}$-divisors, and $S^+ \cong \mathbb{A}^2$. Here $a = 2$ in Lemma 9.2.2, and the restricted algebra of $K_{X^-} + S$ is a graded subalgebra of $\bigoplus_m H^0(S, \mathcal{O}_S(mK_S)) = \bigoplus_m H^0(S, \mathcal{O}_S(2mC^-))$, which is $k[x, y]$ in each degree because $C^-$ is exceptional over $\mathbb{A}^2$. Section 3 shows that the two are equal in all large divisible degrees, which reads Theorem 8.3.9 for the Francia flip as the finite generation of $R(S / \mathbb{A}^2, K_S)$.

### Proof

*Lemma 9.2.2.* Part 1 is Lemma 8.3.2 together with Theorem 8.3.4, and the last equivalence holds because $k(K_X + S + B) \sim_{\mathbb{Q}} kaS + f^* kL$ with $Z$ affine, so that the two algebras have isomorphic Veronese subalgebras, and by Lemma 8.1.5 a divisorial algebra is finitely generated if and only if a Veronese subalgebra is.

For part 2, put $D = k(K_X + S + B)$. The pl flip is the $D$-flip, as $-D$ is ample over $Z$, so by part 3 of Theorem 8.1.6 the algebra $R(X/Z, D)(Z) = R(X, D)$ is a finitely generated $A$-algebra. The restriction map $R(X, D) \to \bigoplus_m H^0(S, \mathcal{O}_S(mD|_S))$ is a homomorphism of graded $A$-algebras, and its image $\operatorname{res}_S R(X, D)$ is a quotient of $R(X, D)$, so it is generated by the images of generators of $R(X, D)$.

For part 3, Cor07, Chapter 2, and HM07, Section 5, prove the converse with the argument of Theorem 8.3.4 applied to the graded algebra $R(X, D)$ and a section of $\mathcal{O}_X(lD)$ vanishing on $S$ that exists by part 1, with the kernel of restriction described as a principal ideal up to a Veronese subalgebra. The details of that argument are not reproduced here, and the statement is cited from those sources.

*Corollary 9.2.3.* Theorem 9.1.4 in dimension $n$ is the first hypothesis of Theorem 8.3.5 and the second is assumed, so Theorem 8.3.5 gives the conclusion.

### Exercises

1. (A) In Example 9.2.4, check that the five maximal cones of $\Sigma^-$ and $\Sigma^+$ are spanned by bases of $N$, and identify the exceptional loci of $X^\pm \to Z$.
2. (A) In Example 9.2.4, compute $D_5 \cdot C^-$ and $(K_{X^-} + D_5) \cdot C^-$, and decide whether $(X^-, D_5) \to Z$ is a pl flipping contraction.
3. (B) In Example 9.2.4, compute $R_S$ for $S = D_1$, if $D_1$ makes $f^-$ a pl flipping contraction, or explain why it does not.
4. (B) Show that the restricted algebra of Definition 9.2.1 depends on $D$ only up to linear equivalence, in the sense that $D' = D + \operatorname{div} \phi$ with $\phi$ a unit near the generic point of $S$ gives an isomorphic graded algebra.
5. (B) Give an example of a finitely generated algebra $R(X, D)$ whose restricted algebra on a smooth divisor $S$ is not the full algebra $R(S, D|_S)$, using a surface $X$ and a curve $S$ on it.
6. (C) Prove part 3 of Lemma 9.2.2 when $k(K_X + S + B) \sim kaS$ over $Z$ with $ka$ an integer, by reducing to Theorem 8.3.4.

### Lean

Nothing in this section is in Lean. The library has `MinimalModel.IsFlip`, `MinimalModel.IsPlt` and the statement `MinimalModel.KltFlips`, but no pl flipping contraction and no restricted algebra.

### Notes and history

Pl flips and the reduction of klt flips to them are due to Shokurov, Sho92 in dimension 3 and Sho04 in general, and the formulation through the restricted algebra is that of Cor07, Chapter 2, which is the reference for the converse direction of Lemma 9.2.2. The idea that the restricted algebra should be an adjoint algebra in one dimension lower is Shokurov's; the theorem that makes it true in every dimension is the extension theorem of HM07, the subject of Section 2. The toric 4-fold flip of Example 9.2.4 is the simplest flip with a flipping locus of dimension $2$, and it shows the general pattern on $S$: the pl flip restricts to the log canonical model of $K_S + \Theta$ over the image of $S$.
