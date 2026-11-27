---
title: Local cohomology
nodes: []
sources: [Har77, Vak25, GW23, Stacks]
reads_with: [Har77:III.2, Har77:III.3]
requires: [P1.5, P1.6, P2.2, P2.3, P2.7, P3.5, P3.6, P4.1, P4.2, P4.7]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Local cohomology

### Statement

Let $X$ be a topological space and $Z \subseteq X$ a closed subset with complement $U = X \setminus Z$. For a sheaf of abelian groups $\mathcal{F}$ on $X$, a section $s \in \mathcal{F}(X)$ has *support in $Z$* if $s_x = 0$ for every $x \in U$, that is, if $s|_U = 0$.

**Definition P4.8.1 (sections with support and local cohomology).**

1. Let $\Gamma_Z(X, \mathcal{F}) \subseteq \Gamma(X, \mathcal{F})$ be the subgroup of sections with support in $Z$, and let $\mathcal{H}^0_Z(\mathcal{F}) \subseteq \mathcal{F}$ be the subsheaf $V \mapsto \Gamma_{Z \cap V}(V, \mathcal{F}|_V)$. Both functors are left exact. The *cohomology of $\mathcal{F}$ with supports in $Z$* is $H^i_Z(X, \mathcal{F})$, the $i$-th right derived functor of $\Gamma_Z(X, -)$ on $\mathsf{Ab}(X)$, and the *local cohomology sheaves* $\mathcal{H}^i_Z(\mathcal{F})$ are the right derived functors of $\mathcal{H}^0_Z$.
2. Let $A$ be a ring, $I \subseteq A$ an ideal and $M$ an $A$-module. Let $\Gamma_I(M) = \{m \in M : I^n m = 0 \text{ for some } n\}$, the *$I$-power torsion* of $M$. It is a left exact functor of $M$, and its right derived functors on $\mathsf{Mod}_A$, which has enough injectives by Theorem P2.2.35, are the *local cohomology modules* $H^i_I(M)$. For a local ring $(A, \mathfrak{m})$, the modules $H^i_\mathfrak{m}(M)$ are the local cohomology of $M$.

For $f = (f_1, \dots, f_r)$ in $A$, the *local Čech complex* $L^\bullet(f, M)$ is the augmented Čech complex of Definition P4.1.1 moved up by one degree:
$$0 \to M \to \prod_{i} M_{f_i} \to \prod_{i < j} M_{f_i f_j} \to \cdots \to M_{f_1 \cdots f_r} \to 0,$$
with $L^0 = M$ and $L^p = \check{C}^{p-1}(f, M)$ for $1 \leq p \leq r$.

**Proposition P4.8.2 (the excision sequence).** Let $Z \subseteq X$ be closed, $U = X \setminus Z$, and $\mathcal{F}$ a sheaf of abelian groups on $X$.

1. There is a long exact sequence, natural in $\mathcal{F}$,
$$0 \to \Gamma_Z(X, \mathcal{F}) \to \Gamma(X, \mathcal{F}) \to \Gamma(U, \mathcal{F}) \to H^1_Z(X, \mathcal{F}) \to H^1(X, \mathcal{F}) \to H^1(U, \mathcal{F}) \to H^2_Z(X, \mathcal{F}) \to \cdots.$$
2. If $\mathcal{F}$ is flasque, then $H^i_Z(X, \mathcal{F}) = 0$ for $i > 0$. So for an $\mathcal{O}_X$-module the groups $H^i_Z(X, \mathcal{F})$ can be computed by an injective resolution in $\mathsf{Mod}(\mathcal{O}_X)$, and they are $\Gamma(X, \mathcal{O}_X)$-modules.
3. (Excision) If $V \subseteq X$ is open and contains $Z$, then restriction gives isomorphisms $H^i_Z(X, \mathcal{F}) \cong H^i_Z(V, \mathcal{F}|_V)$ for all $i$.

Lean: not in Mathlib.

**Lemma P4.8.3 (injective modules over a Noetherian ring).** Let $A$ be Noetherian, $J$ an injective $A$-module, $I$ an ideal and $f \in A$.

1. $J_f$ is an injective $A_f$-module and an injective $A$-module.
2. $\Gamma_I(J)$ is an injective $A$-module.
3. The localization map $J \to J_f$ is surjective.

Lean: Mathlib has injective modules (`Module.Injective`) and Baer's criterion (`Module.Baer.injective`). The lemma is not in Mathlib.

**Theorem P4.8.4 (local cohomology of modules).** Let $A$ be a Noetherian ring, $I = (f_1, \dots, f_r)$ an ideal and $M$ an $A$-module.

1. (Čech complex) There are isomorphisms $H^i_I(M) \cong H^i(L^\bullet(f, M))$, natural in $M$ and compatible with the connecting maps.
2. (Ext) $H^i_I(M) \cong \varinjlim_n \operatorname{Ext}^i_A(A/I^n, M)$, the colimit over the maps induced by the surjections $A/I^{n+1} \to A/I^n$.
3. $H^i_I$ depends only on $\sqrt{I}$. Every element of $H^i_I(M)$ is killed by a power of $I$. $H^i_I(M) = 0$ for $i > r$, and $H^i_I(M) = 0$ for $i > 0$ if $M$ is $I$-power torsion. The functors $H^i_I$ commute with direct sums.
4. (Change of rings) Let $A \to B$ be a homomorphism of Noetherian rings and $N$ a $B$-module. Then $H^i_I(N)$, computed over $A$, is isomorphic to $H^i_{IB}(N)$, computed over $B$.
5. (Flat base change) If $A \to B$ is flat with $B$ Noetherian, then $H^i_I(M) \otimes_A B \cong H^i_{IB}(M \otimes_A B)$. If $\sqrt{I} = \mathfrak{m}$ is a maximal ideal, then $H^i_I(M) = H^i_I(M)_\mathfrak{m} \cong H^i_{\mathfrak{m}A_\mathfrak{m}}(M_\mathfrak{m})$, and for finitely generated $M$, $H^i_\mathfrak{m}(M) \cong H^i_{\hat{\mathfrak{m}}}(\hat{M})$ over the completion $\hat{A}$ of $A_\mathfrak{m}$.
6. (Comparison with sheaves) Let $X = \operatorname{Spec} A$, $Z = V(I)$ and $U = X \setminus Z = D(f_1) \cup \cdots \cup D(f_r)$. Then $H^i_Z(X, \widetilde{M}) \cong H^i_I(M)$, there is an exact sequence
$$0 \to \Gamma_I(M) \to M \to \Gamma(U, \widetilde{M}) \to H^1_I(M) \to 0,$$
and $H^i(U, \widetilde{M}) \cong H^{i+1}_I(M)$ for every $i \geq 1$.

Lean: Mathlib `localCohomology` defines $H^i_I$ as the colimit of $\operatorname{Ext}^i(A/J, -)$ over the ideals $J$ with the same radical as powers of $I$, which is the form of part 2. The Čech description and the comparison with sheaves are not in Mathlib.

**Proposition P4.8.5 (local cohomology sheaves).** Let $X$ be a Noetherian scheme, $Z \subseteq X$ a closed subscheme with ideal sheaf $\mathcal{I}$, and $\mathcal{F}$ a quasi-coherent $\mathcal{O}_X$-module.

1. For any sheaf $\mathcal{F}$ on any space, $\mathcal{H}^i_Z(\mathcal{F})$ is the sheaf associated to the presheaf $V \mapsto H^i_{Z \cap V}(V, \mathcal{F}|_V)$.
2. $\mathcal{H}^i_Z(\mathcal{F})$ is quasi-coherent. On an affine open $V = \operatorname{Spec} A$ with $\mathcal{F}|_V = \widetilde{M}$ and $\mathcal{I}|_V = \widetilde{I}$, it is $H^i_I(M)^\sim$, and $\Gamma(V, \mathcal{H}^i_Z(\mathcal{F})) = H^i_{Z \cap V}(V, \mathcal{F})$.
3. If $\mathcal{F}$ is coherent, then $\mathcal{H}^i_Z(\mathcal{F}) \cong \varinjlim_n \mathcal{E}xt^i_X(\mathcal{O}_X/\mathcal{I}^n, \mathcal{F})$.

Lean: not in Mathlib.

**Proposition P4.8.6 (cones and twists).** Let $S$ be a graded ring with $S_0 = A$ Noetherian, generated as an $A$-algebra by $x_0, \dots, x_n \in S_1$. Let $X = \operatorname{Proj} S$, $\mathfrak{m} = S_+ = (x_0, \dots, x_n)$, $M$ a graded $S$-module and $\mathcal{F} = \widetilde{M}$. Then the modules $H^i_\mathfrak{m}(M)$ are graded, there is an exact sequence of graded modules
$$0 \to H^0_\mathfrak{m}(M) \to M \to \bigoplus_{n \in \mathbb{Z}} \Gamma(X, \mathcal{F}(n)) \to H^1_\mathfrak{m}(M) \to 0,$$
and $H^{i+1}_\mathfrak{m}(M) \cong \bigoplus_{n \in \mathbb{Z}} H^i(X, \mathcal{F}(n))$ for every $i \geq 1$, with $H^i(X, \mathcal{F}(n))$ in degree $n$.

Lean: not in Mathlib.

### Proof in words

A section with support in $Z$ is a section on $X$ that dies on $U$. So for a flasque sheaf the sequence $0 \to \Gamma_Z(X, \mathcal{F}) \to \Gamma(X, \mathcal{F}) \to \Gamma(U, \mathcal{F}) \to 0$ is exact, and applied to an injective resolution it gives the excision sequence. For modules, $\Gamma_I(M)$ is the kernel of $M \to \prod M_{f_i}$, the first map of the local Čech complex. The cohomology of the local Čech complex is a $\delta$-functor, since localization is exact. It vanishes on injective modules, because over a Noetherian ring an injective module stays injective when it is localized or when its $I$-torsion is taken, and it maps onto its localizations. So it is the derived functor of $\Gamma_I$, and every other description follows: the colimit of the Ext groups is a second effaceable $\delta$-functor with the same $H^0$, and on $\operatorname{Spec} A$ the local Čech complex in degrees $\geq 1$ is the Čech complex of the punctured open set $U$. On a cone, the Čech complex of $M$ for the coordinates splits by degree into the Čech complexes of the twists $\mathcal{F}(n)$ on $\operatorname{Proj} S$.

### Examples

**Example P4.8.7 (the affine line).** Let $A = k[x]$ and $I = (x)$. The local Čech complex is $k[x] \to k[x, x^{-1}]$. So $H^0_{(x)}(A) = 0$ and
$$H^1_{(x)}(A) = k[x, x^{-1}]/k[x] = \bigoplus_{a \geq 1} k \, x^{-a},$$
which is not finitely generated, and every element of it is killed by a power of $x$, as part 3 of Theorem P4.8.4 predicts. Multiplication by $x$ sends $x^{-1}$ to $0$ and $x^{-a}$ to $x^{-a+1}$ for $a \geq 2$. So the socle $\{\xi : x\xi = 0\}$ is the line $k x^{-1}$. Section 8.3 identifies this module with the injective hull of $k$. Part 2 of Theorem P4.8.4 sees the same module as $\varinjlim_n \operatorname{Ext}^1(A/x^n, A) = \varinjlim_n A/x^n$, with the maps $A/x^n \to A/x^{n+1}$ given by multiplication by $x$, and $A/x^n$ corresponds to the span of $x^{-1}, \dots, x^{-n}$.

**Example P4.8.8 (the plane and the projective line).** Let $S = k[x, y]$ and $\mathfrak{m} = (x, y)$. The local Čech complex is
$$0 \to S \to S_x \times S_y \to S_{xy} \to 0.$$
Its cohomology is $H^0_\mathfrak{m}(S) = H^1_\mathfrak{m}(S) = 0$ and
$$H^2_\mathfrak{m}(S) = k[x^{\pm 1}, y^{\pm 1}]/(k[x^{\pm 1}, y] + k[x, y^{\pm 1}]) = \bigoplus_{a, b \geq 1} k \, x^{-a} y^{-b}.$$
By part 6 of Theorem P4.8.4, $\Gamma(U, \mathcal{O}) = S$ and $H^1(U, \mathcal{O}_U) \cong H^2_\mathfrak{m}(S)$ on the punctured plane $U$, as in Example P4.1.5. By Proposition P4.8.6 with $X = \mathbb{P}^1_k$, the degree $n$ part of $H^2_\mathfrak{m}(S)$ is $H^1(\mathbb{P}^1, \mathcal{O}(n))$. The monomials $x^{-a}y^{-b}$ with $a, b \geq 1$ and $-a - b = n$ number $-n - 1$ for $n \leq -2$ and none otherwise, which is $\dim H^1(\mathbb{P}^1, \mathcal{O}(n))$ by Theorem P4.2.1.

**Example P4.8.9 (support along a line).** Let $A = k[x, y]$, $I = (x)$, $X = \mathbb{A}^2_k$ and $Z = V(x)$, the line $x = 0$. The local Čech complex is $A \to A_x$, so $H^1_I(A) = A_x/A = \bigoplus_{a \geq 1} x^{-a} k[y]$ and $H^i_I(A) = 0$ for $i \neq 1$. By Proposition P4.8.5, $\mathcal{H}^1_Z(\mathcal{O}_X)$ is the quasi-coherent sheaf associated to this module. It is supported on $Z$, it is not coherent, and its restriction to an open set $D(g)$ is $(A_{xg}/A_g)^\sim$. At a closed point $p \in Z$ with maximal ideal $\mathfrak{n}$, its stalk is $H^1_{(x)}(A_\mathfrak{n})$, while the local cohomology at the point is $H^2_\mathfrak{n}(A_\mathfrak{n})$, which is nonzero by Example P4.8.8 and part 5 of Theorem P4.8.4. The two kinds of local cohomology differ: the first measures $Z$ near $p$, the second only the point.

### Proof

*Proposition P4.8.2.* Part 1. Let $\mathcal{F} \to \mathcal{I}^\bullet$ be an injective resolution in $\mathsf{Ab}(X)$. Each $\mathcal{I}^p$ is flasque by part 1 of Theorem P2.7.11, so $\Gamma(X, \mathcal{I}^p) \to \Gamma(U, \mathcal{I}^p)$ is surjective, and its kernel is $\Gamma_Z(X, \mathcal{I}^p)$ by definition. This gives a short exact sequence of complexes
$$0 \to \Gamma_Z(X, \mathcal{I}^\bullet) \to \Gamma(X, \mathcal{I}^\bullet) \to \Gamma(U, \mathcal{I}^\bullet|_U) \to 0.$$
The cohomology of the first is $H^i_Z(X, \mathcal{F})$, of the second $H^i(X, \mathcal{F})$, and of the third $H^i(U, \mathcal{F})$, since $\mathcal{I}^\bullet|_U$ is an injective resolution of $\mathcal{F}|_U$ (part 3 of Theorem P2.7.3). The long exact sequence of Theorem P2.3.5 is the excision sequence. A map of sheaves extends to a map of injective resolutions, unique up to homotopy, so the sequence is natural.

Part 2. If $\mathcal{F}$ is flasque, then $H^i(X, \mathcal{F}) = H^i(U, \mathcal{F}) = 0$ for $i > 0$ by part 2 of Theorem P2.7.11, since $\mathcal{F}|_U$ is flasque too, and $\Gamma(X, \mathcal{F}) \to \Gamma(U, \mathcal{F})$ is surjective. The excision sequence gives $H^i_Z(X, \mathcal{F}) = 0$ for $i > 0$. An injective $\mathcal{O}_X$-module is flasque (Theorem P2.7.11), so an injective resolution in $\mathsf{Mod}(\mathcal{O}_X)$ is a resolution by $\Gamma_Z$-acyclic objects and computes $H^i_Z(X, \mathcal{F})$ by Theorem P2.3.25. The terms $\Gamma_Z(X, \mathcal{I}^p)$ are then $\Gamma(X, \mathcal{O}_X)$-modules.

Part 3. For any sheaf $\mathcal{G}$, restriction $\Gamma_Z(X, \mathcal{G}) \to \Gamma_Z(V, \mathcal{G}|_V)$ is bijective. It is injective, since a section with support in $Z$ that vanishes on $V$ vanishes on $V \cup U = X$. It is surjective, since a section $t$ on $V$ with support in $Z$ and the section $0$ on $U$ agree on $V \cap U$, and glue to a section on $X$ with support in $Z$. Applied to an injective resolution of $\mathcal{F}$, whose restriction to $V$ is an injective resolution of $\mathcal{F}|_V$, this gives the isomorphism.

*Lemma P4.8.3.* Part 1. Every ideal of $A_f$ is $\mathfrak{a}_f$ for an ideal $\mathfrak{a}$ of $A$, which is finitely presented since $A$ is Noetherian. So $\operatorname{Hom}_{A_f}(\mathfrak{a}_f, J_f) = \operatorname{Hom}_A(\mathfrak{a}, J)_f$, and the surjection $\operatorname{Hom}_A(A, J) \to \operatorname{Hom}_A(\mathfrak{a}, J)$ stays surjective after localization. By Baer's criterion (Theorem P2.2.33), $J_f$ is an injective $A_f$-module. For an $A$-module $N$, $\operatorname{Hom}_A(N, J_f) = \operatorname{Hom}_{A_f}(N_f, J_f)$, which is exact in $N$ since localization is exact. So $J_f$ is an injective $A$-module.

Part 2. Let $\mathfrak{a}$ be an ideal and $\varphi \colon \mathfrak{a} \to \Gamma_I(J)$ a homomorphism. The ideal $\mathfrak{a}$ is finitely generated, so $I^n \varphi(\mathfrak{a}) = 0$ for some $n$. By the Artin-Rees lemma (Lemma P1.5.33) there is $c$ with $I^{c} \cap \mathfrak{a} \subseteq I^n \mathfrak{a}$, so $\varphi$ vanishes on $I^c \cap \mathfrak{a}$. So $\varphi$ and the zero map on $I^c$ define a homomorphism $\mathfrak{a} + I^c \to J$. Since $J$ is injective, it extends to $\psi \colon A \to J$. Then $I^c \psi(1) = \psi(I^c) = 0$, so $\psi(1) \in \Gamma_I(J)$, and $a \mapsto a\psi(1)$ extends $\varphi$ to $A \to \Gamma_I(J)$. By Baer's criterion, $\Gamma_I(J)$ is injective.

Part 3. The ideals $\operatorname{Ann}(f^s)$ increase with $s$ and so are constant for $s \geq s_0$. Let $y/f^n \in J_f$. Define $\varphi \colon (f^{n + s_0}) \to J$ by $\varphi(a f^{n + s_0}) = a f^{s_0} y$. It is well defined: if $a f^{n + s_0} = 0$, then $a \in \operatorname{Ann}(f^{n+s_0}) = \operatorname{Ann}(f^{s_0})$, so $a f^{s_0} = 0$. Since $J$ is injective, $\varphi$ extends to $A$; let $z = \varphi(1)$. Then $f^{n + s_0} z = f^{s_0} y$, so $z/1 = y/f^n$ in $J_f$.

*Theorem P4.8.4.* Part 1. The kernel of $M \to \prod M_{f_i}$ is the set of $m$ with $f_i^{s} m = 0$ for all $i$ and some $s$, which is $\Gamma_I(M)$, since $(f_1^s, \dots, f_r^s) \supseteq I^{rs}$. Localization is exact, so a short exact sequence of modules gives a short exact sequence of local Čech complexes, and $H^i(L^\bullet(f, -))$ is a $\delta$-functor by Theorem P2.3.5. By Corollary P2.3.23 it is enough to prove that $H^i(L^\bullet(f, J)) = 0$ for $i > 0$ and every injective $J$.

Induct on $r$. For $r = 0$ the complex is $J$ in degree $0$. For $r \geq 1$, let $f' = (f_1, \dots, f_{r-1})$ and $I' = (f')$. A $p$-element subset of $\{1, \dots, r\}$ either omits $r$ or is a $(p-1)$-element subset of $\{1, \dots, r-1\}$ with $r$ added, which gives a short exact sequence of complexes
$$0 \to L^{\bullet - 1}(f', M_{f_r}) \to L^\bullet(f, M) \to L^\bullet(f', M) \to 0.$$
Its connecting map $H^p(L^\bullet(f', M)) \to H^p(L^\bullet(f', M_{f_r}))$ is, up to sign, induced by localization. For $M = J$, the module $J_{f_r}$ is injective by part 1 of Lemma P4.8.3, so by induction both outer complexes are exact in positive degrees. The long exact sequence gives $H^p(L^\bullet(f, J)) = 0$ for $p \geq 2$, and
$$H^1(L^\bullet(f, J)) = \operatorname{coker}(\Gamma_{I'}(J) \to \Gamma_{I'}(J_{f_r})).$$
Now $\Gamma_{I'}(J_{f_r}) = \Gamma_{I'}(J)_{f_r}$: if $y/f_r^n$ is killed by $I'^c$, then $f_r^t g y = 0$ for each of the finitely many generators $g$ of $I'^c$ and some $t$, so $f_r^t y \in \Gamma_{I'}(J)$ and $y/f_r^n = f_r^t y/f_r^{n+t}$. The module $\Gamma_{I'}(J)$ is injective by part 2 of Lemma P4.8.3, so it maps onto its localization by part 3. So $H^1(L^\bullet(f, J)) = 0$.

Part 2. $\operatorname{Hom}_A(A/I^n, M) = \{m : I^n m = 0\}$, and the colimit of these subgroups is $\Gamma_I(M)$. Filtered colimits of abelian groups are exact, so $\varinjlim_n \operatorname{Ext}^i_A(A/I^n, -)$ is a $\delta$-functor. It vanishes on injectives in positive degrees. By Corollary P2.3.23 it is $H^i_I$.

Part 3. If $\sqrt{I} = \sqrt{I'}$, then each contains a power of the other, since both are finitely generated, so $\Gamma_I = \Gamma_{I'}$ and their derived functors agree. The module $\operatorname{Ext}^i_A(A/I^n, M)$ is killed by $I^n$, so each element of the colimit in part 2 is killed by a power of $I$. The complex $L^\bullet(f, M)$ has length $r$. If $M$ is $I$-power torsion, then $M_{f_i} = 0$ for every $i$ and $L^\bullet(f, M) = M$ in degree $0$. Localization commutes with direct sums, so the local Čech complex does too.

Part 4. Let $g_i$ be the image of $f_i$ in $B$. As complexes of abelian groups $L^\bullet(f, N) = L^\bullet(g, N)$, since $N_{f_i} = N_{g_i}$. By part 1 over $A$ and over $B$ (applied to $IB = (g_1, \dots, g_r)$), both local cohomologies are its cohomology.

Part 5. $L^\bullet(f, M) \otimes_A B = L^\bullet(f, M \otimes_A B)$, and tensoring with a flat module commutes with taking cohomology. If $\sqrt{I} = \mathfrak{m}$, every element $\xi$ of $H^i_I(M)$ is killed by some $\mathfrak{m}^n$. For $s \notin \mathfrak{m}$, the image of $s$ in the local ring $A/\mathfrak{m}^n$ is a unit, so there is $t$ with $st - 1 \in \mathfrak{m}^n$, and $t$ inverts $s$ on the submodule killed by $\mathfrak{m}^n$. So $s$ acts bijectively on $H^i_I(M)$, which means $H^i_I(M) = H^i_I(M)_\mathfrak{m}$, and the flat base change $A \to A_\mathfrak{m}$ gives the second claim. For the completion, $\hat{A}$ is flat over $A_\mathfrak{m}$ and $\hat{M} = M \otimes_A \hat{A}$ for finitely generated $M$ (Theorems P1.6.13 and P1.6.18). A module $N$ killed by $\mathfrak{m}^n$ satisfies $N \otimes_A \hat{A} = N \otimes_{A/\mathfrak{m}^n} \hat{A}/\mathfrak{m}^n \hat{A} = N$, and $H^i_\mathfrak{m}(M)$ is the union of such submodules, so $H^i_\mathfrak{m}(M) \otimes_A \hat{A} = H^i_\mathfrak{m}(M)$.

Part 6. The functors $M \mapsto H^i_Z(X, \widetilde{M})$ form a $\delta$-functor on $\mathsf{Mod}_A$, since $M \mapsto \widetilde{M}$ is exact (Proposition P3.5.1). In degree $0$, a section $m \in M$ has support $V(\operatorname{Ann}(m))$, since $m_\mathfrak{p} = 0$ exactly when $\operatorname{Ann}(m) \not\subseteq \mathfrak{p}$. This support lies in $V(I)$ if and only if $I \subseteq \sqrt{\operatorname{Ann}(m)}$, that is, if and only if $I^n m = 0$ for some $n$. So $\Gamma_Z(X, \widetilde{M}) = \Gamma_I(M)$.

The open set $U$ is covered by the affine open sets $D(f_i)$, whose intersections $D(f_{i_0} \cdots f_{i_p})$ are affine. By Corollary P4.1.9 the Čech complex $\check{C}^\bullet(f, M)$ computes $H^p(U, \widetilde{M})$. So $L^\bullet(f, M)$ in degrees $\geq 1$ computes $H^{p}(U, \widetilde{M})$ in degree $p + 1$, and its degree $0$ map is the restriction $M \to \Gamma(U, \widetilde{M})$. Hence $H^1(L^\bullet(f, M)) = \operatorname{coker}(M \to \Gamma(U, \widetilde{M}))$ and $H^{p+1}(L^\bullet(f, M)) = H^p(U, \widetilde{M})$ for $p \geq 1$. By part 1 this gives the exact sequence and the isomorphisms $H^i(U, \widetilde{M}) \cong H^{i+1}_I(M)$.

It remains to compare with $H^i_Z(X, \widetilde{M})$. By Serre's vanishing theorem (Theorem P4.1.8), $H^i(X, \widetilde{M}) = 0$ for $i > 0$, so the excision sequence of Proposition P4.8.2 gives $H^1_Z(X, \widetilde{M}) = \operatorname{coker}(M \to \Gamma(U, \widetilde{M}))$ and $H^{i+1}_Z(X, \widetilde{M}) \cong H^i(U, \widetilde{M})$ for $i \geq 1$. For an injective module $J$ the right sides are the cohomology of $L^\bullet(f, J)$ in positive degrees, which vanishes by part 1. So $H^i_Z(X, \widetilde{-})$ is an effaceable $\delta$-functor with $H^0 = \Gamma_I$, and it is $H^i_I$ by Corollary P2.3.23.

*Proposition P4.8.5.* Part 1. Let $\mathcal{F} \to \mathcal{I}^\bullet$ be an injective resolution. Then $\mathcal{H}^i_Z(\mathcal{F})$ is the $i$-th cohomology sheaf of the complex of sheaves $\mathcal{H}^0_Z(\mathcal{I}^\bullet)$, which is the sheaf associated to the presheaf of cohomology groups $V \mapsto H^i(\Gamma_{Z \cap V}(V, \mathcal{I}^\bullet|_V))$. Since $\mathcal{I}^\bullet|_V$ is an injective resolution of $\mathcal{F}|_V$ (Theorem P2.7.3), these groups are $H^i_{Z \cap V}(V, \mathcal{F}|_V)$.

Part 2. On $V = \operatorname{Spec} A$, the presheaf of part 1 takes the value $H^i_I(M)$ on $V$ by part 6 of Theorem P4.8.4, and the value $H^i_{IA_g}(M_g) = H^i_I(M)_g$ on a basic open set $D(g)$ by parts 5 and 6 of the theorem, compatibly with restriction. So on the basis of basic open sets of $V$ the presheaf agrees with $H^i_I(M)^\sim$, which is already a sheaf, and the associated sheaf is $H^i_I(M)^\sim$. Its sections on $V$ are $H^i_I(M) = H^i_{Z \cap V}(V, \mathcal{F})$.

Part 3. On $V = \operatorname{Spec} A$ as in part 2, with $M$ finitely generated, $\mathcal{E}xt^i_X(\mathcal{O}_X/\mathcal{I}^n, \mathcal{F})|_V = \operatorname{Ext}^i_A(A/I^n, M)^\sim$ by Proposition P4.7.3. The functor $M \mapsto \widetilde{M}$ commutes with filtered colimits, so the colimit is $(\varinjlim_n \operatorname{Ext}^i_A(A/I^n, M))^\sim = H^i_I(M)^\sim$ by part 2 of Theorem P4.8.4. The maps $\mathcal{E}xt^i_X(\mathcal{O}_X/\mathcal{I}^n, \mathcal{F}) \to \mathcal{H}^i_Z(\mathcal{F})$ are defined globally, by the inclusions $\mathcal{H}om(\mathcal{O}_X/\mathcal{I}^n, -) \subseteq \mathcal{H}^0_Z$ and universality, and they are isomorphisms on every affine open set.

*Proposition P4.8.6.* Every localization $M_{x_{i_0} \cdots x_{i_p}}$ is graded, and the maps of $L^\bullet(x, M)$ preserve degrees, so the local cohomology is graded. For $p \geq 0$, the degree $n$ part of $M_{x_{i_0} \cdots x_{i_p}}$ is $M(n)_{(x_{i_0} \cdots x_{i_p})}$, the degree $0$ part of the localization of $M(n)$. By Proposition P3.6.11, parts 1 and 4, this is $\Gamma(D_+(x_{i_0} \cdots x_{i_p}), \mathcal{F}(n))$, compatibly with the restriction maps. So the degree $n$ part of $L^\bullet(x, M)$ in degrees $\geq 1$ is the Čech complex of $\mathcal{F}(n)$ for the cover of $X$ by the affine open sets $D_+(x_i)$, whose intersections are affine. Since $X$ is separated, Corollary P4.1.9 identifies its cohomology with $H^p(X, \mathcal{F}(n))$. The degree $0$ map $M_n \to \Gamma(X, \mathcal{F}(n))$ is the natural map. Part 1 of Theorem P4.8.4 gives the claims, exactly as in the proof of part 6.

### Exercises

1. (A) Let $A = \mathbb{Z}$ and $p$ a prime. Show that $H^1_{(p)}(\mathbb{Z}) = \mathbb{Z}[1/p]/\mathbb{Z}$, that $H^0_{(p)}(\mathbb{Z}) = 0$, and that $H^i_{(p)}(\mathbb{Z}/p^n) = 0$ for $i > 0$.
2. (A) Show that the functors $H^i_I$ commute with filtered colimits of modules over a Noetherian ring.
3. (B) Let $A = k[x, y]/(xy)$ and $\mathfrak{m} = (x, y)$. Compute $H^i_\mathfrak{m}(A)$ for all $i$, using the sequence $0 \to A \to k[x] \times k[y] \to k \to 0$, and show that $H^1_\mathfrak{m}(A) \neq 0$.
4. (B) In Example P4.8.9, show that $\mathcal{H}^1_Z(\mathcal{O}_X)$ is not coherent, and compute its stalk at the generic point of $Z$.
5. (B) Let $X = \mathbb{P}^n_k$ and let $S = k[x_0, \dots, x_n]$. Use Proposition P4.8.6 and Theorem P4.2.1 to show that $H^i_\mathfrak{m}(S) = 0$ for $i \leq n$ and to compute the Hilbert function of $H^{n+1}_\mathfrak{m}(S)$.
6. (C) Let $Z \subseteq X$ be closed. Show that $\mathcal{H}^0_Z$ of an injective sheaf is flasque, and deduce a spectral sequence $E_2^{p,q} = H^p(X, \mathcal{H}^q_Z(\mathcal{F})) \Rightarrow H^{p+q}_Z(X, \mathcal{F})$ from the Grothendieck spectral sequence (Theorem P2.4.25) for $\Gamma_Z(X, -) = \Gamma(X, -) \circ \mathcal{H}^0_Z$.

### Lean

Mathlib defines local cohomology of modules over a commutative ring as the colimit of Ext modules (`localCohomology`), with a comparison for ideals with the same radical. Cohomology with supports on a space, the Čech description and the local cohomology sheaves are not in Mathlib. The handbook adds no `MinimalModel` node here.

### Notes and history

Local cohomology was introduced by Grothendieck in his Harvard seminar of 1961, written up by Hartshorne as *Local cohomology* (Lecture Notes in Mathematics 41, 1967), and developed further in SGA 2. Lemma P4.8.3 is the form of Hartshorne III.3.3 and III.3.4 that is needed here, and parts 1, 2 and 6 of Theorem P4.8.4 are among the exercises of Hartshorne III.2 to III.4. The literature state is theorem. In the minimal model program, the excision sequence on a punctured neighbourhood of a point is the tool that compares a singularity with its link, and Proposition P4.8.6 computes the local cohomology of a cone from the cohomology of its base, which is how the singularities of cones in Volume 4 are tested.
