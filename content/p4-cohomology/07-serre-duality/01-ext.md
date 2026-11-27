---
title: Ext groups and Ext sheaves
nodes: []
sources: [Har77, Vak25, GW23, Stacks]
reads_with: [Har77:III.6, Vak25:ch30]
requires: [P1.9, P2.3, P2.6, P2.7, P3.5, P3.6, P4.2]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Ext groups and Ext sheaves

### Statement

Let $(X, \mathcal{O}_X)$ be a ringed space. The category $\mathsf{Mod}(\mathcal{O}_X)$ is abelian (Theorem P2.6.3) and has enough injectives (Theorem P2.7.2). For an $\mathcal{O}_X$-module $\mathcal{F}$, the functors $\operatorname{Hom}_X(\mathcal{F}, -) \colon \mathsf{Mod}(\mathcal{O}_X) \to \mathsf{Ab}$ and $\mathcal{H}om_X(\mathcal{F}, -) \colon \mathsf{Mod}(\mathcal{O}_X) \to \mathsf{Mod}(\mathcal{O}_X)$ are left exact by Theorem P2.6.13.

**Definition P4.7.1 (Ext groups and Ext sheaves).** The *Ext groups* $\operatorname{Ext}^i_X(\mathcal{F}, -)$ are the right derived functors of $\operatorname{Hom}_X(\mathcal{F}, -)$, and the *Ext sheaves* $\mathcal{E}xt^i_X(\mathcal{F}, -)$ are the right derived functors of $\mathcal{H}om_X(\mathcal{F}, -)$. So for an injective resolution $\mathcal{G} \to \mathcal{I}^\bullet$ in $\mathsf{Mod}(\mathcal{O}_X)$,
$$\operatorname{Ext}^i_X(\mathcal{F}, \mathcal{G}) = H^i(\operatorname{Hom}_X(\mathcal{F}, \mathcal{I}^\bullet)), \qquad \mathcal{E}xt^i_X(\mathcal{F}, \mathcal{G}) = \mathcal{H}^i(\mathcal{H}om_X(\mathcal{F}, \mathcal{I}^\bullet)).$$

**Proposition P4.7.2 (first properties).** Let $\mathcal{F}$, $\mathcal{G}$ be $\mathcal{O}_X$-modules.

1. $\operatorname{Ext}^0_X = \operatorname{Hom}_X$ and $\mathcal{E}xt^0_X = \mathcal{H}om_X$. Also $\operatorname{Ext}^i_X(\mathcal{O}_X, \mathcal{G}) = H^i(X, \mathcal{G})$, and $\mathcal{E}xt^i_X(\mathcal{O}_X, \mathcal{G}) = 0$ for $i > 0$.
2. For $U \subseteq X$ open, $\mathcal{E}xt^i_X(\mathcal{F}, \mathcal{G})|_U = \mathcal{E}xt^i_U(\mathcal{F}|_U, \mathcal{G}|_U)$.
3. A short exact sequence $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$ gives a long exact sequence, natural in the sequence,
$$0 \to \operatorname{Hom}(\mathcal{F}'', \mathcal{G}) \to \operatorname{Hom}(\mathcal{F}, \mathcal{G}) \to \operatorname{Hom}(\mathcal{F}', \mathcal{G}) \to \operatorname{Ext}^1(\mathcal{F}'', \mathcal{G}) \to \operatorname{Ext}^1(\mathcal{F}, \mathcal{G}) \to \cdots,$$
and the same holds for the Ext sheaves. A short exact sequence in the second variable gives the long exact sequence of derived functors.
4. Let $\mathcal{E}$ be locally free of finite rank, with dual $\mathcal{E}^\vee = \mathcal{H}om(\mathcal{E}, \mathcal{O}_X)$. Then
$$\operatorname{Ext}^i_X(\mathcal{F} \otimes \mathcal{E}, \mathcal{G}) \cong \operatorname{Ext}^i_X(\mathcal{F}, \mathcal{E}^\vee \otimes \mathcal{G}), \qquad \mathcal{E}xt^i_X(\mathcal{F} \otimes \mathcal{E}, \mathcal{G}) \cong \mathcal{E}xt^i_X(\mathcal{F}, \mathcal{G}) \otimes \mathcal{E}^\vee.$$
In particular $\operatorname{Ext}^i_X(\mathcal{E}, \mathcal{G}) \cong H^i(X, \mathcal{E}^\vee \otimes \mathcal{G})$, and $\mathcal{E}xt^i_X(\mathcal{E}, \mathcal{G}) = 0$ for $i > 0$.

Lean: not in Lean as stated.

**Proposition P4.7.3 (locally free resolutions).** Let $\mathcal{L}_\bullet \to \mathcal{F} \to 0$ be a resolution of $\mathcal{F}$ by locally free $\mathcal{O}_X$-modules of finite rank. Then for every $\mathcal{G}$ and every $i$,
$$\mathcal{E}xt^i_X(\mathcal{F}, \mathcal{G}) \cong \mathcal{H}^i(\mathcal{H}om_X(\mathcal{L}_\bullet, \mathcal{G})).$$
If $X$ is a Noetherian scheme and $\mathcal{F}$, $\mathcal{G}$ are coherent, then $\mathcal{E}xt^i_X(\mathcal{F}, \mathcal{G})$ is coherent, and for every $x \in X$
$$\mathcal{E}xt^i_X(\mathcal{F}, \mathcal{G})_x \cong \operatorname{Ext}^i_{\mathcal{O}_{X,x}}(\mathcal{F}_x, \mathcal{G}_x).$$
For $X = \operatorname{Spec} A$ with $A$ Noetherian and finitely generated $A$-modules $M$, $N$, $\mathcal{E}xt^i_X(\widetilde{M}, \widetilde{N}) = \operatorname{Ext}^i_A(M, N)^\sim$.

Lean: not in Lean as stated.

The groups and the sheaves are related by a spectral sequence $H^p(X, \mathcal{E}xt^q(\mathcal{F}, \mathcal{G})) \Rightarrow \operatorname{Ext}^{p+q}(\mathcal{F}, \mathcal{G})$, which Chapter 8 uses. On a projective scheme a high twist kills all the terms with $p > 0$:

**Proposition P4.7.4 (Ext after a high twist).** Let $X$ be projective over a Noetherian ring $A$, with a very ample sheaf $\mathcal{O}_X(1)$, and let $\mathcal{F}$, $\mathcal{G}$ be coherent. For every $i \geq 0$ there is $q_0$ such that for all $q \geq q_0$
$$\operatorname{Ext}^i_X(\mathcal{F}, \mathcal{G}(q)) \cong \Gamma\big(X, \mathcal{E}xt^i_X(\mathcal{F}, \mathcal{G})(q)\big).$$

Lean: not in Lean as stated.

### Proof in words

All the statements come from three facts about an injective $\mathcal{O}_X$-module $\mathcal{I}$: its restriction to an open set is injective, the functors $\operatorname{Hom}(-, \mathcal{I})$ and $\mathcal{H}om(-, \mathcal{I})$ are exact, and $\mathcal{E}^\vee \otimes \mathcal{I}$ is again injective for a locally free $\mathcal{E}$ of finite rank. The first gives the locality of Ext sheaves, the second the long exact sequence in the first variable, and the third the twisting formulas. A locally free resolution computes the Ext sheaves because both sides are universal $\delta$-functors in $\mathcal{G}$, and on a Noetherian affine scheme such a resolution is a free resolution of modules, which makes the Ext sheaves coherent and computes their stalks. On a projective scheme, a coherent sheaf is a quotient of a sum of copies of $\mathcal{O}(-a)$, whose Ext groups after a twist are cohomology groups of $\mathcal{G}(q + a)$, which vanish for $q$ large by Serre's theorem. Dimension shifting along such presentations proves Proposition P4.7.4.

### Examples

**Example P4.7.5 (a point on a curve).** Let $X$ be a smooth curve over a field $k$, $p \in X$ a closed point and $k(p)$ its skyscraper sheaf, with $0 \to \mathcal{O}_X(-p) \to \mathcal{O}_X \to k(p) \to 0$. This is a locally free resolution, so by Proposition P4.7.3, $\mathcal{E}xt^i(k(p), \mathcal{O}_X)$ is the cohomology of $\mathcal{O}_X \to \mathcal{H}om(\mathcal{O}_X(-p), \mathcal{O}_X) = \mathcal{O}_X(p)$:
$$\mathcal{H}om(k(p), \mathcal{O}_X) = 0, \qquad \mathcal{E}xt^1(k(p), \mathcal{O}_X) = \mathcal{O}_X(p)/\mathcal{O}_X \cong k(p), \qquad \mathcal{E}xt^i(k(p), \mathcal{O}_X) = 0 \text{ for } i \geq 2.$$
The stalk at $p$ is $\operatorname{Ext}^1_{\mathcal{O}_{X,p}}(k(p), \mathcal{O}_{X,p}) = k(p)$, computed from $0 \to \mathcal{O}_{X,p} \xrightarrow{t} \mathcal{O}_{X,p} \to k(p) \to 0$ for a uniformizer $t$.

**Example P4.7.6 (groups and sheaves on the projective line).** Let $X = \mathbb{P}^1_k$, $p = [1 : 0]$, $\mathcal{F} = k(p)$, $\mathcal{G} = \mathcal{O}_X$. By part 3 of Proposition P4.7.2 applied to $0 \to \mathcal{O}(-1) \to \mathcal{O} \to k(p) \to 0$ and by part 4,
$$0 \to \operatorname{Hom}(k(p), \mathcal{O}) \to H^0(\mathcal{O}) \to H^0(\mathcal{O}(1)) \to \operatorname{Ext}^1(k(p), \mathcal{O}) \to H^1(\mathcal{O}) = 0.$$
The middle map is multiplication by the equation $x_1$ of $p$, from $k$ to the $2$-dimensional space $k x_0 \oplus k x_1$, so $\operatorname{Hom}(k(p), \mathcal{O}) = 0$ and $\operatorname{Ext}^1(k(p), \mathcal{O}) \cong k$. This agrees with $\Gamma(X, \mathcal{E}xt^1(k(p), \mathcal{O})) = \Gamma(k(p)) = k$ from Example P4.7.5, as Proposition P4.7.4 predicts, here already for $q = 0$.

**Example P4.7.7 (extensions on the projective line).** By part 4 of Proposition P4.7.2 and Theorem P4.2.1, $\operatorname{Ext}^1_{\mathbb{P}^1}(\mathcal{O}, \mathcal{O}(-2)) = H^1(\mathbb{P}^1, \mathcal{O}(-2)) \cong k$. The nonzero class is the Euler sequence $0 \to \mathcal{O}(-2) \to \mathcal{O}(-1)^2 \to \mathcal{O} \to 0$ of Theorem P3.12.20, with $\Omega_{\mathbb{P}^1} \cong \mathcal{O}(-2)$, which does not split since $H^0(\mathcal{O}(-1)^2) = 0$ while $H^0(\mathcal{O}) \neq 0$. Proposition P2.3.34 identifies $\operatorname{Ext}^1$ with extensions in any abelian category with enough injectives, so up to scaling this is the only nonsplit extension of $\mathcal{O}$ by $\mathcal{O}(-2)$.

### Proof

*Three facts on injectives.* Let $\mathcal{I}$ be an injective $\mathcal{O}_X$-module.

(a) For $U \subseteq X$ open, $\mathcal{I}|_U$ is injective by part 3 of Theorem P2.7.3.

(b) The functor $\operatorname{Hom}_X(-, \mathcal{I})$ is exact, by the definition of an injective object. The functor $\mathcal{H}om_X(-, \mathcal{I})$ is exact: by part 4 of Theorem P2.6.13 it is left exact as a contravariant functor, and for $\mathcal{F}' \subseteq \mathcal{F}$ and $U$ open, $\mathcal{H}om(\mathcal{F}, \mathcal{I})(U) = \operatorname{Hom}_U(\mathcal{F}|_U, \mathcal{I}|_U) \to \operatorname{Hom}_U(\mathcal{F}'|_U, \mathcal{I}|_U)$ is surjective by (a). So $\mathcal{H}om(\mathcal{F}, \mathcal{I}) \to \mathcal{H}om(\mathcal{F}', \mathcal{I})$ is surjective on sections over every open, hence surjective.

(c) For $\mathcal{E}$ locally free of finite rank, $\mathcal{H}om(\mathcal{E}, \mathcal{H}) \cong \mathcal{E}^\vee \otimes \mathcal{H}$ for every $\mathcal{H}$, since this holds for $\mathcal{E} = \mathcal{O}^m$ and the map is defined globally. So by part 3 of Theorem P2.6.13, $\operatorname{Hom}(\mathcal{F}, \mathcal{E}^\vee \otimes \mathcal{I}) \cong \operatorname{Hom}(\mathcal{F} \otimes \mathcal{E}, \mathcal{I})$, naturally in $\mathcal{F}$. The functor $- \otimes \mathcal{E}$ is exact, since $\mathcal{E}$ is locally free, and $\operatorname{Hom}(-, \mathcal{I})$ is exact, so $\operatorname{Hom}(-, \mathcal{E}^\vee \otimes \mathcal{I})$ is exact and $\mathcal{E}^\vee \otimes \mathcal{I}$ is injective.

*Proposition P4.7.2.* (1) Derived functors of a left exact functor agree with it in degree $0$. Since $\operatorname{Hom}_X(\mathcal{O}_X, -) = \Gamma(X, -)$, its derived functors are $H^i(X, -)$, computed in $\mathsf{Mod}(\mathcal{O}_X)$ (part 4 of Theorem P2.7.11). Since $\mathcal{H}om_X(\mathcal{O}_X, -)$ is the identity functor, which is exact, its higher derived functors vanish.

(2) Let $\mathcal{G} \to \mathcal{I}^\bullet$ be an injective resolution. By (a) its restriction to $U$ is an injective resolution of $\mathcal{G}|_U$, and $\mathcal{H}om_X(\mathcal{F}, \mathcal{I}^\bullet)|_U = \mathcal{H}om_U(\mathcal{F}|_U, \mathcal{I}^\bullet|_U)$. Restriction to $U$ is exact, so it commutes with taking cohomology sheaves.

(3) Let $\mathcal{G} \to \mathcal{I}^\bullet$ be an injective resolution. By (b), $0 \to \operatorname{Hom}(\mathcal{F}'', \mathcal{I}^\bullet) \to \operatorname{Hom}(\mathcal{F}, \mathcal{I}^\bullet) \to \operatorname{Hom}(\mathcal{F}', \mathcal{I}^\bullet) \to 0$ is a short exact sequence of complexes, and Theorem P2.3.5 gives the long exact sequence. The same argument with $\mathcal{H}om$ gives the sheaf version. The last claim is Theorem P2.3.15.

(4) Let $\mathcal{G} \to \mathcal{I}^\bullet$ be an injective resolution. Since $\mathcal{E}^\vee$ is locally free, $\mathcal{E}^\vee \otimes \mathcal{G} \to \mathcal{E}^\vee \otimes \mathcal{I}^\bullet$ is exact, and by (c) it is an injective resolution. By (c) again, $\operatorname{Hom}(\mathcal{F}, \mathcal{E}^\vee \otimes \mathcal{I}^\bullet) \cong \operatorname{Hom}(\mathcal{F} \otimes \mathcal{E}, \mathcal{I}^\bullet)$, and taking cohomology gives the first isomorphism. For the second, by part 3 of Theorem P2.6.13 and (c),
$$\mathcal{H}om(\mathcal{F} \otimes \mathcal{E}, \mathcal{I}^\bullet) \cong \mathcal{H}om(\mathcal{F}, \mathcal{H}om(\mathcal{E}, \mathcal{I}^\bullet)) \cong \mathcal{H}om(\mathcal{F}, \mathcal{E}^\vee \otimes \mathcal{I}^\bullet) \cong \mathcal{H}om(\mathcal{F}, \mathcal{I}^\bullet) \otimes \mathcal{E}^\vee,$$
the last because $\mathcal{E}^\vee$ is locally free of finite rank, and the cohomology sheaves of the outer terms are the two sides, since $- \otimes \mathcal{E}^\vee$ is exact. For $\mathcal{F} = \mathcal{O}_X$ part 1 gives the special cases. $\square$

*Proposition P4.7.3.* For fixed $i$, let $T^i(\mathcal{G}) = \mathcal{H}^i(\mathcal{H}om(\mathcal{L}_\bullet, \mathcal{G}))$. Since each $\mathcal{L}_j$ is locally free, $\mathcal{H}om(\mathcal{L}_j, -) = \mathcal{L}_j^\vee \otimes -$ is exact, so a short exact sequence in $\mathcal{G}$ gives a short exact sequence of complexes and a long exact sequence of the $T^i$. So $(T^i)$ is a $\delta$-functor. Since $\mathcal{H}om(-, \mathcal{G})$ is left exact, $T^0(\mathcal{G}) = \ker(\mathcal{H}om(\mathcal{L}_0, \mathcal{G}) \to \mathcal{H}om(\mathcal{L}_1, \mathcal{G})) = \mathcal{H}om(\mathcal{F}, \mathcal{G})$. If $\mathcal{G} = \mathcal{I}$ is injective, $\mathcal{H}om(-, \mathcal{I})$ is exact by (b), so $\mathcal{H}om(\mathcal{L}_\bullet, \mathcal{I})$ is exact in positive degrees and $T^i(\mathcal{I}) = 0$ for $i > 0$. So $(T^i)$ is effaceable, and by Corollary P2.3.23 it is isomorphic to $(\mathcal{E}xt^i(\mathcal{F}, -))$.

Now let $X$ be a Noetherian scheme and $\mathcal{F}$, $\mathcal{G}$ coherent. The claims are local by part 2 of Proposition P4.7.2, so let $X = \operatorname{Spec} A$ with $A$ Noetherian, $\mathcal{F} = \widetilde{M}$, $\mathcal{G} = \widetilde{N}$ with $M$, $N$ finitely generated. Choose a resolution $L_\bullet \to M$ by finitely generated free $A$-modules. Then $\widetilde{L}_\bullet \to \widetilde{M}$ is a resolution by free sheaves of finite rank, since $M \mapsto \widetilde{M}$ is exact (Proposition P3.5.1), and $\mathcal{H}om(\widetilde{L}_j, \widetilde{N}) = \operatorname{Hom}_A(L_j, N)^\sim$ since $L_j$ is free of finite rank. So
$$\mathcal{E}xt^i(\widetilde{M}, \widetilde{N}) = \mathcal{H}^i(\operatorname{Hom}_A(L_\bullet, N)^\sim) = \operatorname{Ext}^i_A(M, N)^\sim,$$
again by exactness of $\sim$. This is coherent, since $\operatorname{Ext}^i_A(M, N)$ is a subquotient of the finitely generated module $\operatorname{Hom}_A(L_i, N) \cong N^{b_i}$. For $x \in X$ corresponding to a prime $\mathfrak{p}$, localization is exact and $\operatorname{Hom}_A(L_j, N)_\mathfrak{p} = \operatorname{Hom}_{A_\mathfrak{p}}((L_j)_\mathfrak{p}, N_\mathfrak{p})$, so the stalk is the cohomology of $\operatorname{Hom}_{A_\mathfrak{p}}((L_\bullet)_\mathfrak{p}, N_\mathfrak{p})$, where $(L_\bullet)_\mathfrak{p}$ is a free resolution of $M_\mathfrak{p}$. This is $\operatorname{Ext}^i_{A_\mathfrak{p}}(M_\mathfrak{p}, N_\mathfrak{p})$. $\square$

*Proposition P4.7.4.* For $i = 0$ this holds for every $q$: $\operatorname{Hom}(\mathcal{F}, \mathcal{G}(q)) = \Gamma(\mathcal{H}om(\mathcal{F}, \mathcal{G}(q)))$ by part 1 of Theorem P2.6.13, and $\mathcal{H}om(\mathcal{F}, \mathcal{G}(q)) = \mathcal{H}om(\mathcal{F}, \mathcal{G})(q)$ by (c). Let $i \geq 1$ and assume the claim for $i - 1$ and all pairs of coherent sheaves. By Theorem P3.6.23 there are $a$ and $m$ with $\mathcal{F}(a)$ generated by $m$ global sections, which gives an exact sequence
$$0 \to \mathcal{R} \to \mathcal{E} \to \mathcal{F} \to 0, \qquad \mathcal{E} = \mathcal{O}_X(-a)^{\oplus m},$$
with $\mathcal{R}$ coherent. By part 4 of Proposition P4.7.2, $\operatorname{Ext}^j(\mathcal{E}, \mathcal{G}(q)) = H^j(X, \mathcal{G}(q + a))^{\oplus m}$, which is $0$ for $j > 0$ and $q \geq q_1$ by part 2 of Theorem P4.2.7, and $\mathcal{E}xt^j(\mathcal{E}, \mathcal{G}) = 0$ for $j > 0$.

If $i \geq 2$, part 3 of Proposition P4.7.2 gives isomorphisms $\operatorname{Ext}^{i-1}(\mathcal{R}, \mathcal{G}(q)) \cong \operatorname{Ext}^i(\mathcal{F}, \mathcal{G}(q))$ for $q \geq q_1$ and $\mathcal{E}xt^{i-1}(\mathcal{R}, \mathcal{G}) \cong \mathcal{E}xt^i(\mathcal{F}, \mathcal{G})$, and the claim for $\mathcal{F}$ in degree $i$ follows from the claim for $\mathcal{R}$ in degree $i - 1$.

If $i = 1$, there are exact sequences
$$\operatorname{Hom}(\mathcal{E}, \mathcal{G}(q)) \to \operatorname{Hom}(\mathcal{R}, \mathcal{G}(q)) \to \operatorname{Ext}^1(\mathcal{F}, \mathcal{G}(q)) \to 0 \quad (q \geq q_1),$$
$$\mathcal{H}om(\mathcal{E}, \mathcal{G}) \xrightarrow{\ \alpha\ } \mathcal{H}om(\mathcal{R}, \mathcal{G}) \to \mathcal{E}xt^1(\mathcal{F}, \mathcal{G}) \to 0.$$
The sheaves in the second sequence are coherent by Proposition P4.7.3. Twist it by $q$, which is exact, and let $\mathcal{K} = \ker \alpha$ and $\mathcal{B} = \operatorname{im} \alpha$, both coherent. By part 2 of Theorem P4.2.7 there is $q_2 \geq q_1$ with $H^1(\mathcal{K}(q)) = H^1(\mathcal{B}(q)) = 0$ for $q \geq q_2$. Then $\Gamma$ is exact on $0 \to \mathcal{K}(q) \to \mathcal{H}om(\mathcal{E}, \mathcal{G})(q) \to \mathcal{B}(q) \to 0$ and on $0 \to \mathcal{B}(q) \to \mathcal{H}om(\mathcal{R}, \mathcal{G})(q) \to \mathcal{E}xt^1(\mathcal{F}, \mathcal{G})(q) \to 0$, so
$$\Gamma(\mathcal{H}om(\mathcal{E}, \mathcal{G})(q)) \to \Gamma(\mathcal{H}om(\mathcal{R}, \mathcal{G})(q)) \to \Gamma(\mathcal{E}xt^1(\mathcal{F}, \mathcal{G})(q)) \to 0$$
is exact. Its first two terms are those of the first sequence by the case $i = 0$, compatibly with the maps. So the cokernels agree, and $\operatorname{Ext}^1(\mathcal{F}, \mathcal{G}(q)) \cong \Gamma(\mathcal{E}xt^1(\mathcal{F}, \mathcal{G})(q))$ for $q \geq q_2$. $\square$

### Exercises

1. (A) Show that $\operatorname{Ext}^i_X(\mathcal{F}, \mathcal{G})$ is a $\Gamma(X, \mathcal{O}_X)$-module, and that the isomorphisms of Proposition P4.7.2 are linear.
2. (A) On $X = \mathbb{P}^1_k$, compute $\operatorname{Ext}^i(\mathcal{O}(a), \mathcal{O}(b))$ for all $a$, $b$, $i$.
3. (B) Let $X = \operatorname{Spec} k[x, y]$ and $\mathcal{F} = k(0)$, the skyscraper at the origin. Use the Koszul resolution (Lemma P1.9.20) to show that $\mathcal{E}xt^i(k(0), \mathcal{O}_X)$ is $k(0)$ for $i = 2$ and $0$ otherwise.
4. (B) Let $Z \subseteq X$ be a closed subscheme of a Noetherian scheme, with ideal $\mathcal{I}$. Show that $\mathcal{H}om_X(\mathcal{O}_Z, \mathcal{G})$ is the subsheaf of sections of $\mathcal{G}$ killed by $\mathcal{I}$, and that $\mathcal{E}xt^i_X(\mathcal{O}_Z, \mathcal{G})$ is supported on $Z$.
5. (B) Show by an example on $\mathbb{P}^1_k$ that Proposition P4.7.4 fails for $q$ small: find coherent $\mathcal{F}$, $\mathcal{G}$ with $\operatorname{Ext}^1(\mathcal{F}, \mathcal{G}) \neq \Gamma(\mathcal{E}xt^1(\mathcal{F}, \mathcal{G}))$.
6. (C) Let $A$ be a Noetherian local ring, $M$ a finitely generated module, and $X = \operatorname{Spec} A$. Show that $\operatorname{Ext}^i_X(\widetilde{M}, \widetilde{N}) = \operatorname{Ext}^i_A(M, N)$ for every $A$-module $N$. (Use that $\operatorname{Hom}_X(\widetilde{M}, -) = \operatorname{Hom}_A(M, \Gamma(X, -))$ on quasi-coherent sheaves, that $\widetilde{I}$ is flasque for an injective $A$-module $I$, and compare both sides as $\delta$-functors on quasi-coherent sheaves.)

### Lean

Mathlib has Ext groups in abelian categories (`CategoryTheory.Abelian.Ext`) and the abelian category of sheaves of modules over a scheme (`AlgebraicGeometry.Scheme.Modules`). Ext sheaves and the comparisons above are not in Mathlib. The handbook adds no `MinimalModel` node here.

### Notes and history

Ext groups of sheaves were introduced by Grothendieck in the Tôhoku paper of 1957, *Sur quelques points d'algèbre homologique*, as derived functors in an abelian category with enough injectives. Serre's paper *Faisceaux algébriques cohérents* already used the twisting argument of Proposition P4.7.4. The presentation follows Hartshorne III.6. The literature state is theorem. In the minimal model program, Ext sheaves into the canonical sheaf appear as the cohomology sheaves of the dual of a coherent sheaf, and the dualizing sheaf of Section 7.3 is itself an Ext sheaf.
