---
title: Zariski's connectedness and main theorems
nodes: []
sources: [Har77, Vak25, GW23, Stacks]
reads_with: [Har77:III.11, Vak25:ch29]
requires: [P1.1, P1.2, P1.4, P1.6, P1.11, P3.4, P3.7, P3.11, P4.1, P4.6]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Zariski's connectedness and main theorems

### Statement

As in Section 6.1, $Y$ is Noetherian and $f \colon X \to Y$ is projective with $X \subseteq \mathbb{P}^r_Y$.

**Theorem P4.6.7 (Zariski's connectedness theorem).** If $f_* \mathcal{O}_X = \mathcal{O}_Y$, then every fibre $X_y$ is nonempty and connected.

Lean: not in Lean as stated.

**Theorem P4.6.8 (Zariski's main theorem, connectedness form).** Let $f \colon X \to Y$ be a projective birational morphism of integral schemes, with $Y$ Noetherian and normal. Then $f_* \mathcal{O}_X = \mathcal{O}_Y$, and every fibre of $f$ is nonempty and connected.

Lean: not in Lean as stated.

**Proposition P4.6.9 (finite fibres).** If the fibre $X_y$ is a finite set, then there is an open neighbourhood $V$ of $y$ such that $f^{-1}(V) \to V$ is finite.

Lean: not in Lean as stated.

**Corollary P4.6.10 (Zariski's main theorem, original form).** Let $f \colon X \to Y$ be as in Theorem P4.6.8. Let $U \subseteq Y$ be the set of points $y$ for which $X_y$ is finite. Then $U$ is open, and $f^{-1}(U) \to U$ is an isomorphism. So every fibre of $f$ is either a single point, over $U$, or connected of positive dimension at every point, over $Y \setminus U$.

Lean: not in Lean as stated.

The closed subset $\operatorname{Exc}(f) = f^{-1}(Y \setminus U)$ is the *exceptional locus* of $f$: the set of points of $X$ where $f$ fails to be an isomorphism. Corollary P4.6.10 says that a birational projective morphism onto a normal scheme is an isomorphism exactly where it is quasi-finite, and contracts every fibre it does not keep to a connected positive-dimensional set. This is the shape of every birational contraction in the minimal model program.

### Proof in words

If $f_* \mathcal{O}_X = \mathcal{O}_Y$, the theorem on formal functions identifies the completed local ring $\widehat{\mathcal{O}}_{Y,y}$ with the ring of formal functions along $X_y$. A splitting of $X_y$ into two disjoint closed pieces gives a splitting of every thickening $X_n$, hence a nontrivial idempotent formal function, while a complete local ring has none. For Zariski's main theorem, $f_* \mathcal{O}_X$ is a finite $\mathcal{O}_Y$-algebra inside the function field of $Y$, hence integral over $\mathcal{O}_Y$, and normality of $Y$ forces it to be $\mathcal{O}_Y$. The original form follows by showing that a projective morphism with a finite fibre is finite near that fibre, so that $f$ is finite and birational over $U$, hence an isomorphism there because $Y$ is normal.

### Examples

**Example P4.6.11 (the blow-up of a point).** The blow-up $\pi \colon X \to \mathbb{A}^2_k$ of the origin is projective and birational, and $\mathbb{A}^2_k$ is normal. By Theorem P4.6.8, $\pi_* \mathcal{O}_X = \mathcal{O}_{\mathbb{A}^2}$, which Proposition P4.4.16 checked directly. The fibre over the origin is $E \cong \mathbb{P}^1$, connected, and $U = \mathbb{A}^2 \setminus \{0\}$, over which $\pi$ is an isomorphism. The exceptional locus is $E$. The same holds for the blow-up of the vertex of the cone over a smooth plane curve (Example P4.6.5), since the cone is normal by Exercise 4.

**Example P4.6.12 (normality is needed).** Let $Y = V(y^2 - x^2(x + 1)) \subseteq \mathbb{A}^2_k$ be the nodal cubic, with $\operatorname{char} k \neq 2$, and $\nu \colon X = \mathbb{A}^1_k \to Y$, $t \mapsto (t^2 - 1, t(t^2 - 1))$, its normalization (Section P3.7). Then $\nu$ is finite and birational, hence projective, and the fibre over the node $(0, 0)$ is $\{t = 1, t = -1\}$, two points. So the fibre is not connected, and $\nu_* \mathcal{O}_X \neq \mathcal{O}_Y$: the function $t = y/x$ is integral over $\mathcal{O}_Y$ but not in it. Here $U = Y$, every fibre is finite, and $\nu$ is not an isomorphism. Both conclusions of Theorem P4.6.8 and Corollary P4.6.10 fail, because $Y$ is not normal.

**Example P4.6.13 (a small contraction).** Let $Y = V(xy - zw) \subseteq \mathbb{A}^4_k = \operatorname{Spec} k[x, y, z, w]$, the cone over a smooth quadric surface. Since $xy - zw$ is irreducible and the singular locus $\{0\}$ has codimension $3$, $Y$ is normal by Corollary P1.11.14. Let $X \subseteq Y \times \mathbb{P}^1_k$, with coordinates $[s : t]$ on $\mathbb{P}^1$, be the closed subscheme
$$x t = z s, \qquad w t = y s.$$
On the chart $s \neq 0$, with $t/s = u$, the equations say $z = x u$ and $y = w u$, and then $xy - zw = x w u - x u w = 0$ holds automatically, so this chart is $\operatorname{Spec} k[x, w, u] \cong \mathbb{A}^3$. Symmetrically, the chart $t \neq 0$ is $\operatorname{Spec} k[z, y, v] \cong \mathbb{A}^3$ with $v = s/t$, $x = z v$, $w = y v$. So $X$ is smooth and integral. The projection $f \colon X \to Y$ is projective. Away from $0$, the ratio $[s : t]$ is determined as $[x : z]$ or $[w : y]$, one of which is defined, so $f$ is an isomorphism over $Y \setminus \{0\}$, and $f$ is birational. The fibre over $0$ is all of $\{0\} \times \mathbb{P}^1$. By Theorem P4.6.8, $f_* \mathcal{O}_X = \mathcal{O}_Y$, and by Corollary P4.6.10 the exceptional locus is the curve $C = f^{-1}(0) \cong \mathbb{P}^1$. The exceptional locus has codimension $2$ in the threefold $X$: $f$ is a *small* contraction. It contracts no divisor, unlike the blow-ups of Example P4.6.11. The second small resolution, by the equations $x t = w s$, $z t = y s$, is the other side of the Atiyah flop in Volume 1.

### Proof

*Theorem P4.6.7.* Let $y \in Y$ and $A = \widehat{\mathcal{O}}_{Y,y}$, a complete Noetherian local ring. By Corollary P4.6.3 and the hypothesis, $\varprojlim_n H^0(X_n, \mathcal{O}_{X_n}) \cong A$ as rings. If $X_y$ were empty, every $X_n$ would be empty, the limit would be $0$, and $A = 0$, which is false. Suppose $X_y = Z_1 \sqcup Z_2$ with $Z_1, Z_2$ nonempty, closed and open. Each $X_n$ has the underlying space of $X_y$, so $\mathcal{O}_{X_n} = \mathcal{O}_{X_n}|_{Z_1} \times \mathcal{O}_{X_n}|_{Z_2}$, and the section $e_n$ equal to $1$ on $Z_1$ and $0$ on $Z_2$ is an idempotent of $H^0(X_n, \mathcal{O}_{X_n})$, different from $0$ and $1$ since both $Z_i$ are nonempty. The $e_n$ are compatible, so they define an idempotent $e \in A$ different from $0$ and $1$, since its image in $H^0(X_1, \mathcal{O}_{X_1})$ is $e_1$. But a local ring has no idempotents other than $0$ and $1$: if $e(1 - e) = 0$, one of $e$ and $1 - e$ is a unit, and then the other is $0$. This contradiction shows $X_y$ is connected. $\square$

*Theorem P4.6.8.* The question is local on $Y$, so let $Y = \operatorname{Spec} A$ with $A$ a normal Noetherian domain. Then $B = H^0(X, \mathcal{O}_X)$ is a finitely generated $A$-module by Theorem P4.2.7, and $f_* \mathcal{O}_X = \widetilde{B}$. Since $X$ is integral, $B$ is a domain. Let $K = K(Y) = \operatorname{Frac} A$. There is a dense open $V \subseteq Y$ over which $f$ is an isomorphism, and we can take $V = D(s)$ for some $s \neq 0$ in $A$. Since $X$ is integral, restriction of functions to the dense open $f^{-1}(V)$ is injective, so $B \to H^0(f^{-1}(V), \mathcal{O}_X) = A_s \subseteq K$ is injective, and $A \subseteq B \subseteq K$. Every element of $B$ is integral over $A$, because $B$ is a finitely generated $A$-module (Section P1.4). Since $A$ is integrally closed in $K$, $B = A$. So $f_* \mathcal{O}_X = \mathcal{O}_Y$, and Theorem P4.6.7 gives the connectedness. $\square$

*Proposition P4.6.9.* Replacing $Y$ by an affine open neighbourhood of $y$, let $Y = \operatorname{Spec} A$, so that $X$ is a closed subscheme of $\mathbb{P}^r_A$ defined by a homogeneous ideal $I \subseteq A[T_0, \ldots, T_r]$. The fibre $X_y \subseteq \mathbb{P}^r_{k(y)}$ is finite, say $X_y = \{x_1, \ldots, x_m\}$, and each $x_j$ corresponds to a homogeneous prime $P_j \subseteq k(y)[T_0, \ldots, T_r]$ not containing the irrelevant ideal. If $m = 0$, then $y \notin f(X)$, which is closed by Corollary P3.4.30, and $V = Y \setminus f(X)$ works. Otherwise:

*Step 1: a form avoiding the fibre.* For each pair $i \neq j$ of indices, $P_j \not\subseteq P_i$, since distinct closed points of the finite set $X_y$ give incomparable primes, so there is a homogeneous $h_{ij} \in P_j \setminus P_i$. For $m = 1$ choose a variable $T_l \notin P_1$ and set $G_0 = T_l$. For $m \geq 2$ let $H_i = \prod_{j \neq i} h_{ij}$, homogeneous, in every $P_j$ with $j \neq i$ and, since $P_i$ is prime, not in $P_i$. Raise the $H_i$ to powers $a_i$ so that the $H_i^{a_i}$ have a common degree, and let $G_0 = \sum_i H_i^{a_i}$. Then $G_0 \notin P_i$ for every $i$, since every term but the $i$-th lies in $P_i$. So $V_+(G_0) \cap X_y = \emptyset$.

*Step 2: lifting.* Choose $s \in A \setminus \mathfrak{p}_y$, for the prime $\mathfrak{p}_y$ of $y$, such that the coefficients of $G_0$ lift to $A_s$, and a homogeneous $G \in A_s[T_0, \ldots, T_r]$ lifting $G_0$. Replace $Y$ by $D(s)$. The closed subset $X \cap V_+(G)$ of $X$ has closed image $W = f(X \cap V_+(G)) \subseteq Y$ by Corollary P3.4.30, and $y \notin W$ since $X_y \cap V_+(G) = \emptyset$. Let $V \subseteq Y \setminus W$ be an affine open neighbourhood of $y$.

*Step 3: affine and proper gives finite.* Over $V$, $f^{-1}(V) \subseteq D_+(G)$, and $D_+(G) \cap \mathbb{P}^r_V = \operatorname{Spec} \mathcal{O}(V)[T_0, \ldots, T_r]_{(G)}$ is affine by Theorem P3.6.3. So $f^{-1}(V)$, a closed subscheme of an affine scheme, is affine, say $f^{-1}(V) = \operatorname{Spec} C$. By Theorem P4.2.7, $C = H^0(f^{-1}(V), \mathcal{O})$ is a finitely generated $\mathcal{O}(V)$-module, since $f^{-1}(V)$ is projective over $V$. So $f^{-1}(V) \to V$ is finite. $\square$

*Corollary P4.6.10.* By Proposition P4.6.9, every $y \in U$ has an open neighbourhood $V$ over which $f$ is finite, and then every fibre over $V$ is finite, so $V \subseteq U$ and $U$ is open. Over an affine open $V = \operatorname{Spec} A \subseteq U$ on which $f$ is finite, $f^{-1}(V) = \operatorname{Spec} B$ with $B$ finite over $A$, and $B = A$ by Theorem P4.6.8. So $f^{-1}(V) \to V$ is an isomorphism, and these glue to $f^{-1}(U) \cong U$. For $y \notin U$, $X_y$ is infinite and connected by Theorem P4.6.8. A connected Noetherian scheme of finite type over a field with an isolated point is that point, so every point of $X_y$ lies on a curve in $X_y$: $\dim_x X_y \geq 1$ for every $x \in X_y$. $\square$

### Exercises

1. (A) Let $f \colon X \to Y$ be projective with $f_* \mathcal{O}_X = \mathcal{O}_Y$. Show that $f$ is surjective and that $f$ has geometrically connected fibres over every point $y$ with $k(y)$ algebraically closed.
2. (A) Show that the normalization of the cuspidal cubic $V(y^2 - x^3)$ has connected fibres but is not an isomorphism, and explain why this does not contradict Corollary P4.6.10.
3. (B) In Example P4.6.13, compute the ideal of the fibre $f^{-1}(0)$ in each chart and show that it is the reduced curve $\mathbb{P}^1$. Show that the preimage of the plane $\{x = z = 0\} \subseteq Y$ contains $C$, while the strict transform of the plane $\{x = w = 0\}$ meets $C$ in one point.
4. (B) Show that the affine cone over a smooth plane curve of degree $d$ is normal, using Corollary P1.11.14.
5. (B) Let $X \to \mathbb{A}^2_k$ be the blow-up of the ideal $(x, y^2)$. Show that $X$ is not normal near one point of the exceptional curve, that its normalization is still projective and birational over $\mathbb{A}^2_k$, and that both have connected fibres.
6. (C) Let $f \colon X \to Y$ be projective with $Y$ Noetherian and $f_* \mathcal{O}_X = \mathcal{O}_Y$. Show that every fibre is geometrically connected: $X_y \times_{k(y)} \operatorname{Spec} K$ is connected for every field $K \supseteq k(y)$. (For $K = k(y)(\alpha)$ finite, lift the minimal polynomial of $\alpha$ to a monic $g \in \mathcal{O}_{Y,y}[T]$, base change along the finite flat local extension $\mathcal{O}_{Y,y} \to \mathcal{O}_{Y,y}[T]/(g)$ using Theorem P4.5.1, and apply Theorem P4.6.7. Then pass to arbitrary $K$.)

### Lean

Mathlib has normal domains and integral closure (`IsIntegrallyClosed`), finite and integral ring maps, and the fact that a local ring has only trivial idempotents. The theorems above, which depend on cohomology of coherent sheaves, are not in Mathlib. The handbook adds no `MinimalModel` node here.

### Notes and history

Zariski proved the main theorem in *Foundations of a general theory of birational correspondences* (1943), in the form that a birational correspondence between normal varieties is an isomorphism at a point where it has a finite fibre. He deduced the connectedness theorem in 1951 from the theorem on formal functions, which he proved for the purpose. Grothendieck gave the general forms in EGA III.4.3 and EGA IV.8.12, the latter without projectivity, via quasi-finite morphisms, and Peskine gave an elementary algebraic proof of the quasi-finite form. Hartshorne III.11.4 and its corollaries are the forms used here. The literature state is theorem. In the minimal model program, Theorem P4.6.8 is the reason a birational contraction onto a normal variety is determined by its exceptional locus, and Example P4.6.13 is the basic small contraction, the starting point of flips and flops.
