---
title: The theorem on formal functions
nodes: []
sources: [Har77, Vak25, GW23, Stacks]
reads_with: [Har77:III.11, Vak25:ch28]
requires: [P1.5, P1.6, P2.7, P3.11, P4.1, P4.2, P4.4, P4.5]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The theorem on formal functions

### Statement

Throughout, $Y$ is a Noetherian scheme, $f \colon X \to Y$ is projective with $X \subseteq \mathbb{P}^r_Y$, $\mathcal{F}$ is a coherent sheaf on $X$, and $y \in Y$ is a point with maximal ideal $\mathfrak{m} \subseteq \mathcal{O}_{Y, y}$. For $n \geq 1$ let
$$X_n = X \times_Y \operatorname{Spec} \mathcal{O}_{Y, y}/\mathfrak{m}^n, \qquad \mathcal{F}_n = \mathcal{F}|_{X_n},$$
the pullback of $\mathcal{F}$ to $X_n$. So $X_1 = X_y$ is the fibre, and $X_n$ is a closed subscheme of $X_{n+1}$ with the same underlying space. The maps $\mathcal{F} \to \mathcal{F}_n$ induce maps $(R^q f_* \mathcal{F})_y \to H^q(X_n, \mathcal{F}_n)$, compatible with $n$. The source is a finitely generated $\mathcal{O}_{Y,y}$-module by Theorem P4.4.8, and $\mathfrak{m}^n$ acts as zero on the target, so they induce a map
$$\theta^q \colon (R^q f_* \mathcal{F})^\wedge_y \to \varprojlim_n H^q(X_n, \mathcal{F}_n)$$
from the $\mathfrak{m}$-adic completion of the stalk.

**Theorem P4.6.1 (theorem on formal functions).** For every $q \geq 0$ the map $\theta^q$ is an isomorphism.

Lean: not in Lean as stated.

**Corollary P4.6.2 (vanishing above the fibre dimension).** If $\dim X_y \leq d$ for every $y \in Y$, then $R^q f_* \mathcal{F} = 0$ for every $q > d$ and every coherent $\mathcal{F}$.

Lean: not in Lean as stated.

**Corollary P4.6.3 (formal functions in degree zero).** The map $\theta^0 \colon (f_* \mathcal{O}_X)^\wedge_y \to \varprojlim_n H^0(X_n, \mathcal{O}_{X_n})$ is an isomorphism of rings.

Lean: not in Lean as stated.

The name comes from Zariski, for whom $\varprojlim_n H^0(X_n, \mathcal{O}_{X_n})$ was the ring of *formal functions* along the fibre, functions defined on an infinitesimal neighbourhood of $X_y$ of every order. Corollary P4.6.3 says that every formal function along the fibre comes from a formal function on the base at $y$, an element of $(f_* \mathcal{O}_X)^\wedge_y$.

### Proof in words

After base change to the local ring at $y$, which is flat, the stalk is the module $M = H^q(X, \mathcal{F})$ over a local ring $(A, \mathfrak{m})$, and the question is how $M/\mathfrak{m}^n M$ compares with $H^q(X, \mathcal{F}/\mathfrak{m}^n \mathcal{F})$. The long exact sequence of $0 \to \mathfrak{m}^n \mathcal{F} \to \mathcal{F} \to \mathcal{F}/\mathfrak{m}^n \mathcal{F} \to 0$ sandwiches $H^q(\mathcal{F}/\mathfrak{m}^n \mathcal{F})$ between $M/R_n$, for the image $R_n$ of $H^q(\mathfrak{m}^n \mathcal{F})$, and a submodule $Q_n$ of $H^{q+1}(\mathfrak{m}^n \mathcal{F})$. The key observation is that all the modules $H^q(\mathfrak{m}^n \mathcal{F})$ together form one finitely generated module over the Rees algebra $\bigoplus_n \mathfrak{m}^n$, because they are the cohomology of a coherent sheaf on a projective scheme over that algebra. Finite generation then makes $(R_n)$ a stable $\mathfrak{m}$-filtration, so that $\varprojlim M/R_n$ is the completion $\hat{M}$, and it forces the transition maps of $(Q_n)$ to vanish in long enough steps, so that $(Q_n)$ disappears in the limit. This is the Artin-Rees argument, run on cohomology.

### Examples

**Example P4.6.4 (the blow-up of a point of the plane).** Let $Y = \mathbb{A}^2_k = \operatorname{Spec} k[x, y]$, $\pi \colon X \to Y$ the blow-up of the origin $0$ with exceptional curve $E \cong \mathbb{P}^1_k$ (Theorem P3.11.17), and $\mathfrak{m} = (x, y)$. Then $\mathfrak{m} \mathcal{O}_X = \mathcal{I}_E$ is the ideal sheaf of $E$, so $X_n$ is the subscheme $n E$ defined by $\mathcal{I}_E^n$. In the chart $\operatorname{Spec} k[x, v]$ with $y = x v$, $\mathcal{I}_E = (x)$, and in the chart $\operatorname{Spec} k[y, u]$ with $x = y u$, $\mathcal{I}_E = (y)$. So $\mathcal{I}_E^k / \mathcal{I}_E^{k+1}$ is a line bundle on $E$, and the images of the $k + 1$ monomials of degree $k$ in $x, y$ are independent global sections of it. So it is $\mathcal{O}_E(k)$, and there are exact sequences
$$0 \to \mathcal{O}_E(k) \to \mathcal{O}_{X_{k+1}} \to \mathcal{O}_{X_k} \to 0.$$
Since $H^1(E, \mathcal{O}_E(k)) = 0$ for $k \geq 0$ by Theorem P4.2.1, induction on $n$ gives $H^1(X_n, \mathcal{O}_{X_n}) = 0$ for all $n$. By Theorem P4.6.1, $(R^1 \pi_* \mathcal{O}_X)^\wedge_0 = 0$, so $(R^1 \pi_* \mathcal{O}_X)_0 = 0$. Away from $0$, $\pi$ is an isomorphism. So $R^1 \pi_* \mathcal{O}_X = 0$, which agrees with Proposition P4.4.16 for $m = 0$. In degree $0$, the limit of the $H^0(X_n, \mathcal{O}_{X_n})$ is built from $H^0(\mathcal{O}_E(k)) = k[x, y]_k$, and it is $k[[x, y]]$, the completion of $\pi_* \mathcal{O}_X = \mathcal{O}_Y$ at $0$.

**Example P4.6.5 (the cone over a plane cubic).** Let $E = V_+(F) \subseteq \mathbb{P}^2_k$ be a smooth cubic, $Y = \operatorname{Spec} k[x, y, z]/(F)$ the affine cone over $E$ with vertex $0$, and $\pi \colon X \to Y$ the blow-up of $0$. As in Example P4.6.4, $\mathfrak{m} \mathcal{O}_X = \mathcal{I}_E$ for the exceptional curve, which is a copy of $E$, and $\mathcal{I}_E^k/\mathcal{I}_E^{k+1} \cong \mathcal{O}_E(k)$: the blow-up is the total space of the line bundle $\mathcal{O}_E(-1)$, with $E$ as its zero section, whose conormal bundle is $\mathcal{O}_E(1)$. From $0 \to \mathcal{O}_{\mathbb{P}^2}(k - 3) \to \mathcal{O}_{\mathbb{P}^2}(k) \to \mathcal{O}_E(k) \to 0$ and Theorem P4.2.1, $H^1(E, \mathcal{O}_E(k)) \cong H^2(\mathbb{P}^2, \mathcal{O}(k - 3))$ for $k \geq 0$, which is $k$ for $k = 0$ and $0$ for $k \geq 1$. The sequences $0 \to \mathcal{O}_E(n) \to \mathcal{O}_{X_{n+1}} \to \mathcal{O}_{X_n} \to 0$ and $H^2 = 0$ on the curve $E$ give isomorphisms $H^1(X_{n+1}, \mathcal{O}) \cong H^1(X_n, \mathcal{O})$ for $n \geq 1$, and $H^1(X_1, \mathcal{O}) = H^1(E, \mathcal{O}_E) = k$. By Theorem P4.6.1, $(R^1 \pi_* \mathcal{O}_X)^\wedge_0 \cong k$. Since $\pi$ is an isomorphism away from $0$, $R^1 \pi_* \mathcal{O}_X$ is the skyscraper sheaf $k$ at the vertex. So the cone over an elliptic curve has a singularity that is not rational, in the sense of P8. The same computation for a smooth plane curve of degree $d$ is Exercise 5.

**Example P4.6.6 (the completion is needed).** For the identity $f \colon \mathbb{A}^1_k \to \mathbb{A}^1_k$ and $y = 0$, $X_n = \operatorname{Spec} k[t]/(t^n)$ and $\varprojlim_n H^0(X_n, \mathcal{O}_{X_n}) = k[[t]]$, while $(f_* \mathcal{O})_0 = k[t]_{(t)}$. The formal functions are the formal power series, and Theorem P4.6.1 can only compare them with the completion of the stalk. For $f \colon \mathbb{P}^1_Y \to Y$ the same happens: $H^0(X_n, \mathcal{O}_{X_n}) = \mathcal{O}_{Y,y}/\mathfrak{m}^n$ by Theorem P4.2.1, with limit $\widehat{\mathcal{O}}_{Y,y}$.

### Proof

*Theorem P4.6.1.* Let $A = \mathcal{O}_{Y, y}$. By part 1 of Corollary P4.5.2, $(R^q f_* \mathcal{F})_y = H^q(X_A, \mathcal{F})$ for $X_A = X \times_Y \operatorname{Spec} A$, which is projective over $A$, and each $X_n$ is the closed subscheme of $X_A$ defined by $\mathfrak{m}^n$. Pushing forward along the closed immersion $X_n \to X_A$, which does not change cohomology by Corollary P4.4.3, $H^q(X_n, \mathcal{F}_n) = H^q(X_A, \mathcal{F}/\mathfrak{m}^n \mathcal{F})$. So replace $Y$ by $\operatorname{Spec} A$ and $X$ by $X_A$. Now $A$ is a Noetherian local ring, and $M = H^q(X, \mathcal{F})$ is a finitely generated $A$-module by Theorem P4.2.7.

*Step 1: the Rees algebra.* Let $S = \bigoplus_{d \geq 0} \mathfrak{m}^d t^d \subseteq A[t]$ be the Rees algebra of $\mathfrak{m}$ (Definition P3.11.1). It is generated over $A$ by $\mathfrak{m} t$, so it is a finitely generated $A$-algebra and Noetherian. The sheaf $\mathcal{G} = \bigoplus_{d \geq 0} \mathfrak{m}^d \mathcal{F}$ is a quasi-coherent module over $\mathcal{O}_X \otimes_A S$, with $a t^k$ acting as multiplication by $a$ from $\mathfrak{m}^d \mathcal{F}$ to $\mathfrak{m}^{d+k} \mathcal{F}$. On an affine open $U \subseteq X$, $\mathcal{G}(U)$ is generated over $\mathcal{O}_X(U) \otimes_A S$ by $\mathcal{F}(U)$ in degree $0$, hence by finitely many elements. By Theorem P3.5.35, $\mathcal{G}$ is the pushforward of a coherent sheaf $\widetilde{\mathcal{G}}$ along the affine morphism $p \colon X_S = X \times_A \operatorname{Spec} S \to X$. Now $X_S \subseteq \mathbb{P}^r_S$ is projective over the Noetherian ring $S$, so by Corollary P4.4.3, Proposition P4.1.18 and Theorem P4.2.7,
$$\bigoplus_{d \geq 0} H^q(X, \mathfrak{m}^d \mathcal{F}) = H^q(X, \mathcal{G}) = H^q(X_S, \widetilde{\mathcal{G}})$$
is a finitely generated graded $S$-module, for every $q$. Here $a t^k$ acts on cohomology through multiplication by $a$.

*Step 2: the exact sequences.* For $n \geq 1$ the long exact sequence of $0 \to \mathfrak{m}^n \mathcal{F} \to \mathcal{F} \to \mathcal{F}/\mathfrak{m}^n \mathcal{F} \to 0$ gives an exact sequence
$$0 \to M/R_n \to H^q(X, \mathcal{F}/\mathfrak{m}^n \mathcal{F}) \to Q_n \to 0,$$
where $R_n$ is the image of $H^q(X, \mathfrak{m}^n \mathcal{F}) \to M$ and $Q_n$ is the kernel of $H^{q+1}(X, \mathfrak{m}^n \mathcal{F}) \to H^{q+1}(X, \mathcal{F})$. The inclusions $\mathfrak{m}^{n+1} \mathcal{F} \subseteq \mathfrak{m}^n \mathcal{F}$ make these sequences into an exact sequence of inverse systems, and the transition maps of $(M/R_n)$ are surjective.

*Step 3: $(R_n)$ is a stable filtration.* The module $\bigoplus_n R_n t^n \subseteq M[t]$ is the image of the $S$-linear map $\bigoplus_n H^q(X, \mathfrak{m}^n \mathcal{F}) \to M[t]$, so it is a finitely generated $S$-module, generated by homogeneous elements of degrees at most some $c$. For $n \geq c$ this gives $R_n = \sum_{j \leq c} \mathfrak{m}^{n-j} R_j$, and so $R_{n+1} = \mathfrak{m} R_n$. Also $\mathfrak{m} R_n \subseteq R_{n+1}$ for all $n$, and $R_0 = M$. So $(R_n)$ is a stable $\mathfrak{m}$-filtration (Definition P1.6.4), and by Lemma P1.6.5, $\varprojlim_n M/R_n = \hat{M}$, compatibly with the maps from $M$.

*Step 4: $(Q_n)$ vanishes in the limit.* The module $\bigoplus_n Q_n t^n$ is the kernel of the $S$-linear map $\bigoplus_n H^{q+1}(X, \mathfrak{m}^n \mathcal{F}) \to H^{q+1}(X, \mathcal{F})[t]$, so it is a submodule of a finitely generated module over the Noetherian ring $S$, and it is generated by homogeneous elements $g_i \in Q_{j_i}$ with $j_i \leq c$, after enlarging $c$. Each $Q_n$ is a quotient of $H^q(X, \mathcal{F}/\mathfrak{m}^n \mathcal{F})$, on which $\mathfrak{m}^n$ acts as zero, so $\mathfrak{m}^n Q_n = 0$. For $N \geq n$ let $\tau \colon Q_N \to Q_n$ be the transition map. If $g \in Q_j$ with $j \leq n$ and $a \in \mathfrak{m}^{N - j}$, then $\tau(a t^{N-j} g) = a t^{n-j} g$, since both are induced by multiplication by $a$ from $\mathfrak{m}^j \mathcal{F}$ to $\mathfrak{m}^n \mathcal{F}$. Now let $n \geq c$ and $N = 2n$. Every element of $Q_{2n}$ is a sum of terms $a t^{2n - j} g_i$ with $j = j_i$ and $a \in \mathfrak{m}^{2n - j} = \mathfrak{m}^n \mathfrak{m}^{n - j}$. Writing $a = \sum b_l c_l$ with $b_l \in \mathfrak{m}^n$ and $c_l \in \mathfrak{m}^{n-j}$,
$$\tau(a t^{2n-j} g_i) = \sum_l b_l \cdot (c_l t^{n-j} g_i) = 0,$$
since $b_l \in \mathfrak{m}^n$ kills $Q_n$. So $Q_{2n} \to Q_n$ is zero for $n \geq c$. If $(x_n) \in \varprojlim Q_n$, then $x_n = \tau(x_{2n}) = 0$ for $n \geq c$, and $x_n = \tau(x_c) = 0$ for $n < c$. So $\varprojlim Q_n = 0$.

*Step 5.* By Lemma P1.6.2 applied to the sequences of Step 2,
$$0 \to \varprojlim M/R_n \to \varprojlim H^q(X, \mathcal{F}/\mathfrak{m}^n \mathcal{F}) \to \varprojlim Q_n = 0$$
is exact. With Step 3, the natural map $\hat{M} \to \varprojlim H^q(X_n, \mathcal{F}_n)$ is an isomorphism, and this map is $\theta^q$. $\square$

*Corollary P4.6.2.* Let $y \in Y$. Each $X_n$ has the underlying space of $X_y$, a Noetherian space of dimension at most $d$. The cohomology of an $\mathcal{O}$-module agrees with the cohomology of the underlying sheaf of abelian groups (Section P2.7), so $H^q(X_n, \mathcal{F}_n) = 0$ for $q > d$ by Theorem P2.7.13. By Theorem P4.6.1 the completion of the finitely generated $\mathcal{O}_{Y,y}$-module $N = (R^q f_* \mathcal{F})_y$ is $0$. By Theorem P1.6.13, $\hat{N} = N \otimes \widehat{\mathcal{O}}_{Y,y}$, and the completion is faithfully flat by Theorem P1.6.18, so $N = 0$. This holds at every $y$. $\square$

*Corollary P4.6.3.* The case $q = 0$, $\mathcal{F} = \mathcal{O}_X$ of Theorem P4.6.1. The maps $(f_* \mathcal{O}_X)_y \to H^0(X_n, \mathcal{O}_{X_n})$ are ring homomorphisms, so the limit map is one. $\square$

### Exercises

1. (A) For $f \colon \mathbb{P}^r_Y \to Y$ and $\mathcal{F} = \mathcal{O}(m)$, verify Theorem P4.6.1 directly from Theorem P4.2.1 over the rings $\mathcal{O}_{Y,y}/\mathfrak{m}^n$.
2. (A) Let $j \colon \mathbb{A}^2_k \setminus \{0\} \to \mathbb{A}^2_k$ be the inclusion. Show that the fibre over $0$ is empty while $(R^1 j_* \mathcal{O})_0 \neq 0$ (Example P4.4.5), and explain which hypothesis of Theorem P4.6.1 fails.
3. (A) Let $\pi \colon X \to \mathbb{A}^3_k$ be the blow-up of the origin, with exceptional divisor $E \cong \mathbb{P}^2_k$ and $\mathcal{I}_E^k/\mathcal{I}_E^{k+1} \cong \mathcal{O}_E(k)$. Show that $R^1 \pi_* \mathcal{O}_X = R^2 \pi_* \mathcal{O}_X = 0$.
4. (B) In Example P4.6.4, show that $\mathcal{I}_E^k \mathcal{O}_X(2E)/\mathcal{I}_E^{k+1} \mathcal{O}_X(2E) \cong \mathcal{O}_E(k - 2)$, and use Theorem P4.6.1 to show that $R^1 \pi_* \mathcal{O}_X(2E)$ has length $1$, in agreement with Proposition P4.4.16.
5. (B) Let $C = V_+(F) \subseteq \mathbb{P}^2_k$ be a smooth curve of degree $d$ and $\pi \colon X \to Y$ the blow-up of the vertex of the affine cone over $C$. Show that $R^1 \pi_* \mathcal{O}_X$ is supported at the vertex, with length $\sum_{k \geq 0} h^1(C, \mathcal{O}_C(k)) = \sum_{j=0}^{d-3} \binom{j + 2}{2}$. Deduce that the vertex is a rational singularity in the sense of P8 only for $d \leq 2$.
6. (C) Let $f \colon X \to Y$ be projective, $Y$ Noetherian, $\mathcal{F}$ coherent, and $d = \dim X_y$. Use Theorem P4.6.1 and the right exactness of $H^d$ on the schemes $X_n$, whose dimension is $d$, to show that $(R^d f_* \mathcal{F})_y \otimes k(y) \to H^d(X_y, \mathcal{F}_y)$ is surjective, without assuming $\mathcal{F}$ flat over $Y$. Compare with Exercise 6 of Section 5.1.

### Lean

The completion of a Noetherian local ring, the Rees algebra and the Artin-Rees lemma are in Mathlib (`AdicCompletion`, `Ideal.exists_pow_inf_eq_pow_smul` for Artin-Rees). The cohomology of coherent sheaves and the theorem on formal functions are not. The handbook adds no `MinimalModel` node here.

### Notes and history

Zariski proved the theorem on formal functions in 1951, in *Theory and applications of holomorphic functions on algebraic varieties over arbitrary ground fields*, for $q = 0$, to prove his connectedness theorem. Grothendieck extended it to all $q$ and to proper morphisms in EGA III.4.1.5. The proof here, by the Rees algebra, is Hartshorne's proof of III.11.1, with the Artin-Rees step made explicit. The literature state is theorem. In the minimal model program, Theorem P4.6.1 is how $R^i f_* \mathcal{O}_X$ is computed for a resolution of a singularity or a contraction, as in Examples P4.6.4 and P4.6.5, and Corollary P4.6.2 bounds the higher direct images of a contraction by the dimension of its exceptional fibres.
