---
title: Tango curves and Raynaud's counterexample
nodes: []
sources: [Ray78, Tan72, Muk13, EV92, BK05, Har77]
reads_with: [Ray78:1, Tan72:1, EV92:11, Muk13:1]
requires: [P4.2, P4.4, P4.7, P7.8]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Tango curves and Raynaud's counterexample

### Statement

Throughout, $k$ is algebraically closed of characteristic $p > 0$. The *absolute Frobenius* $F \colon X \to X$ of a scheme over $k$ is the identity on the underlying space and $f \mapsto f^p$ on functions. For a line bundle $L$, $F^* L \cong L^p$, and pullback by $F$ gives maps $F^* \colon H^i(X, L) \to H^i(X, L^p)$. On a smooth curve, $F$ is finite and flat of degree $p$.

**Definition P7.11.1 (exact differentials).** Let $C$ be a smooth curve. The sheaf $B_1 \subseteq F_* \Omega_C$ is the image of $d \colon F_* \mathcal{O}_C \to F_* \Omega_C$. It is an $\mathcal{O}_C$-submodule, because $d(f^p g) = f^p dg$, and there is an exact sequence of $\mathcal{O}_C$-modules
$$0 \to \mathcal{O}_C \xrightarrow{F^*} F_* \mathcal{O}_C \xrightarrow{d} B_1 \to 0.$$
A smooth projective curve $C$ is a *Tango curve* if there is a rational function $f$ on $C$ with $df \neq 0$ and $\operatorname{div}(df) = pD$ for an effective divisor $D$ of positive degree.

**Lemma P7.11.2 (the kernel of Frobenius).** Let $C$ be a smooth projective curve and $L$ a line bundle of positive degree. Then the kernel of $F^* \colon H^1(C, L^{-1}) \to H^1(C, L^{-p})$ is isomorphic to $H^0(C, B_1 \otimes L^{-1})$.

Lean: not in Lean as stated.

**Proposition P7.11.3 (Tango).** Let $C$ be a Tango curve with $f$ and $D$ as in Definition P7.11.1. Then $F^* \colon H^1(C, \mathcal{O}_C(-D)) \to H^1(C, \mathcal{O}_C(-pD))$ is not injective, although $\mathcal{O}_C(D)$ is ample.

Lean: not in Lean as stated.

**Theorem P7.11.4 (Raynaud, black box).** Let $C$ be a Tango curve. There is a smooth projective surface $X$ with a morphism $X \to C$ whose fibres are curves, and an ample line bundle $\mathcal{L}$ on $X$ with $H^1(X, \mathcal{L}^{-1}) \neq 0$, equivalently $H^1(X, \omega_X \otimes \mathcal{L}) \neq 0$. Tango curves exist in every characteristic $p$, so Kodaira vanishing fails in every characteristic $p > 0$.

Lean: not in Lean as stated.

### Proof in words

On a curve, Frobenius pulls a class in $H^1$ of a negative line bundle back to a class in $H^1$ of a more negative one. The exact sequence of Definition P7.11.1, twisted by $L^{-1}$, identifies the kernel with the global exact differentials with values in $L^{-1}$, and on a Tango curve the differential $df$ is one. So Frobenius kills a class $\xi \in H^1(C, \mathcal{O}(-D))$.

Raynaud turns the curve into a surface. The class $\xi$ is an extension $0 \to \mathcal{O}_C \to \mathcal{E} \to \mathcal{O}_C(D) \to 0$, nonsplit, whose Frobenius pullback splits. In the ruled surface $P = \mathbb{P}(\mathcal{E})$, the splitting of the pullback gives a curve $C' \subseteq P$ that maps to $C$ purely inseparably of degree $p$, disjoint from the section given by the subbundle $\mathcal{O}_C$. A cyclic cover of $P$ branched along these two curves, of a degree determined by $D$ and $p$, is the surface $X$, and the pullback of a combination of the two curves and a fibre is the line bundle $\mathcal{L}$. The class $\xi$ pulls back to a nonzero class in $H^1(X, \mathcal{L}^{-1})$. This is a black box here.

### Examples

**Example P7.11.5 (a plane Tango curve).** Let $q = p^e \geq 4$ and $C \subseteq \mathbb{P}^2$ the closure of the affine curve $y^q - y = x^{q-1}$. The partial derivative in $y$ is $q y^{q-1} - 1 = -1$, so the affine curve is smooth and the projection to the $x$-line is étale on it. The homogeneous equation $y^q - y z^{q-1} = x^{q-1} z$ meets the line $z = 0$ only at $P_\infty = (1 : 0 : 0)$, where in the chart $x = 1$ the derivative of $y^q - y z^{q-1} - z$ in $z$ is $-1$. So $C$ is a smooth plane curve of degree $q$, irreducible, of genus $g = \frac{(q-1)(q-2)}{2}$. The differential $dx$ is nonzero, since $x$ is a separating function, and it has no zeros on the affine part, where the projection to the $x$-line is étale. So $\operatorname{div}(dx)$ is supported at $P_\infty$, of degree $2g - 2 = q(q - 3)$:
$$\operatorname{div}(dx) = q(q-3) P_\infty = p D, \qquad D = p^{e-1}(q - 3) P_\infty.$$
For $q \geq 4$, $\deg D > 0$, and $C$ is a Tango curve with $f = x$. Proposition P7.11.3 gives a nonzero class in $H^1(C, \mathcal{O}(-D))$ killed by Frobenius.

**Example P7.11.6 (curves satisfy Kodaira vanishing).** On a smooth projective curve $C$ in any characteristic, an ample line bundle $L$ has $H^1(C, \omega_C \otimes L) \cong H^0(C, L^{-1})' = 0$ by Serre duality, Corollary P4.7.21, since $\deg L^{-1} < 0$. So the failure of Kodaira vanishing needs dimension at least $2$, and on a Tango curve the failure is only of the injectivity of Frobenius on $H^1(C, L^{-1})$, which in characteristic $0$ has no analogue. Theorem P7.11.4 converts it into a failure of vanishing on a surface.

**Example P7.11.7 (curves that are not Tango).** If $\operatorname{div}(df) = pD$ with $\deg D > 0$, then $2g - 2 = p \deg D > 0$, so a Tango curve has genus at least $2$, and in fact $2g - 2 \geq p$. The projective line and elliptic curves are not Tango curves. For an elliptic curve $E$, Frobenius on $H^1(E, \mathcal{O}_E)$ is zero exactly when $E$ is supersingular (Har77, Section IV.4). This is a Frobenius kernel for the trivial line bundle, which is not ample, and Section 11.3 returns to it.

### Proof

*Definition P7.11.1.* Let $K = k(C)$ and $t$ a local parameter at a closed point $x$, which is a separating function, so $K = K^p(t)$ has basis $1, t, \dots, t^{p-1}$ over $K^p$, and in the completion $k((t))$ every element is uniquely $\sum_{i=0}^{p-1} b_i t^i$ with $b_i \in k((t^p))$. An element $g = \sum_{i < p} a_i^p t^i$ of $K$, with $a_i \in K$, has $dg = \sum_{i=1}^{p-1} i a_i^p t^{i-1} dt$. If $g$ is regular at $x$, then by uniqueness of the expansion each $a_i^p$ lies in $k[[t^p]] \cap K$, which is regular at $x$ since $\mathcal{O}_{C,x} = K \cap k[[t]]$. So $dg = 0$ forces $g = a_0^p$ with $a_0$ regular at $x$, since $\mathcal{O}_{C,x}$ is normal. Hence the kernel of $d$ is the image of $F^*$, and the sequence is exact.

*Lemma P7.11.2.* Tensor the sequence of Definition P7.11.1 with $L^{-1}$. By the projection formula, $F_* \mathcal{O}_C \otimes L^{-1} = F_*(F^* L^{-1}) = F_*(L^{-p})$, and the sequence becomes
$$0 \to L^{-1} \to F_*(L^{-p}) \to B_1 \otimes L^{-1} \to 0,$$
where the first map is $F^*$. Since $F$ is finite, $H^i(C, F_* L^{-p}) = H^i(C, L^{-p})$ (Corollary P4.4.3), and the first map induces $F^*$ on cohomology. The long exact sequence reads
$$H^0(C, L^{-p}) \to H^0(C, B_1 \otimes L^{-1}) \to H^1(C, L^{-1}) \xrightarrow{F^*} H^1(C, L^{-p}),$$
and $H^0(C, L^{-p}) = 0$ since $\deg L^{-p} < 0$.

*Proposition P7.11.3.* By Lemma P7.11.2 with $L = \mathcal{O}_C(D)$, it is enough to find a nonzero section of $B_1(-D)$. Inside $F_* \Omega_C \otimes \mathcal{O}(-D) = F_*(\Omega_C \otimes F^* \mathcal{O}(-D)) = F_*(\Omega_C(-pD))$, the form $df$ is a global section, since $\operatorname{div}(df) = pD$. It lies in $B_1$ locally at every point $x$: with $t$ a local parameter at $x$, write $f = \sum_{i < p} a_i^p t^i$ with $a_i \in K$ as in the proof of Definition P7.11.1. Since $df = \sum_{i \geq 1} i a_i^p t^{i-1} dt$ is regular at $x$, uniqueness of the expansion in $k((t))$ shows that $a_i^p$ is regular at $x$ for $1 \leq i \leq p - 1$, so $g = \sum_{i = 1}^{p-1} a_i^p t^i$ is regular at $x$ and $dg = df$. So $df$ is a nonzero global section of $B_1 \otimes \mathcal{O}(-D)$, and the class it defines in $H^1(C, \mathcal{O}(-D))$ is nonzero and killed by $F^*$. The divisor $D$ has positive degree, so $\mathcal{O}(D)$ is ample.

*Theorem P7.11.4.* This is Raynaud's theorem (Ray78), and Mukai extends the construction to higher dimension (Muk13); it is a black box here. The existence of Tango curves in every characteristic is Example P7.11.5 for $q \geq 4$, which covers every $p$: take $q = p^e$ with $e$ large enough that $q \geq 4$. The precise branch data of the cyclic cover depend on $p$ and on $D$, and are not reproduced here.

### Exercises

1. (A) Check that $B_1$ is locally free of rank $p - 1$ on a smooth curve, by computing $F_* \mathcal{O}_C$ in a local coordinate.
2. (A) Let $p = 3$. Show that the plane curve $y^3 - y = x^2$ is an elliptic curve with $\operatorname{div}(dx) = 0$, and explain why it is not a Tango curve.
3. (B) Let $C$ be a Tango curve with $D$ as in Definition P7.11.1. Show that $\mathcal{O}_C(pD) \cong \omega_C$, that $\deg D = \frac{2g - 2}{p}$, and that the nonzero class of Proposition P7.11.3 gives a nonsplit extension $0 \to \mathcal{O}_C \to \mathcal{E} \to \mathcal{O}_C(D) \to 0$ whose Frobenius pullback splits.
4. (B) Show that on a smooth projective curve of genus $g$, $\deg F_* \mathcal{O}_C = (p-1)(g-1)$, from $\chi(F_* \mathcal{O}_C) = \chi(\mathcal{O}_C)$ and Riemann-Roch for vector bundles, and deduce $\deg B_1 = (p-1)(g-1)$.
5. (B) Let $C$ be any smooth projective curve and $L$ a line bundle of degree $\geq 1$. Show that $F^* \colon H^1(C, L^{-1}) \to H^1(C, L^{-p})$ is injective when $\deg L > \frac{2g - 2}{p}$, using a degree bound for $H^0(C, B_1 \otimes L^{-1}) \subseteq H^0(C, \Omega_C \otimes L^{-p})$.
6. (C) Read Raynaud's construction (Ray78) and, for the curve of Example P7.11.5 with $p = 2$, $q = 4$, determine the ruled surface $\mathbb{P}(\mathcal{E})$, the curve $C'$ and the degree of the cyclic cover.

### Lean

The project library has no positive characteristic vanishing statements and no Frobenius pullback on cohomology. Mathlib has the Frobenius endomorphism of rings of characteristic $p$, but not on schemes with its action on coherent cohomology. The handbook adds no `MinimalModel` node here.

### Notes and history

Tango studied extensions of line bundles on curves under Frobenius pullback (Tan72), and Raynaud used Tango's curves to construct the first counterexample to Kodaira vanishing in positive characteristic (Ray78). The literature state is theorem. Mukai gave counterexamples in all dimensions at least $2$ and related them to the failure of the Bogomolov and Miyaoka-Yau inequalities (Muk13). Esnault and Viehweg, Lecture 11 (EV92), present Raynaud's example. The statement that Kodaira vanishing fails in every characteristic $p > 0$ is attributed here to Raynaud's construction applied to Example P7.11.5; the details of the branch data for small $p$ were not checked against the paper.
