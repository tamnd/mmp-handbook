---
title: The sheaves O_X(D)
nodes: []
sources: [Vak25, Har77, GW20, Stacks]
reads_with: [Vak25:ch14, Har77:II.6, GW20:ch11]
requires: [P1.8, P1.11, P3.5, P3.6]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The sheaves O_X(D)

### Statement

In this section $X$ is a normal integral Noetherian scheme with function field $K$. Write $\mathcal{K}$ for the constant sheaf $K$ on $X$, the quasi-coherent sheaf of Example P3.5.5. For an open $U$ and $D \in \operatorname{Div}(X)$, write $D|_U$ for the image of $D$ in $\operatorname{Div}(U)$ (Theorem P3.8.13).

**Definition P3.8.27 (the sheaf of a divisor).** For $D \in \operatorname{Div}(X)$ let $\mathcal{O}_X(D) \subseteq \mathcal{K}$ be the subsheaf with
$$
\mathcal{O}_X(D)(U) = \{ f \in K^* : (\operatorname{div}(f) + D)|_U \geq 0 \} \cup \{0\}
$$
for $U \neq \emptyset$. A divisor $D$ is *locally principal* at $x \in X$ if there are an open $U \ni x$ and $f \in K^*$ with $D|_U = \operatorname{div}(f)|_U$.

A *$\mathbb{Q}$-divisor* is an element $D = \sum_i a_i D_i$ of $\operatorname{Div}(X) \otimes \mathbb{Q}$, with distinct prime divisors $D_i$ and $a_i \in \mathbb{Q}$. Its *round down* is $\lfloor D \rfloor = \sum_i \lfloor a_i \rfloor D_i$, and $\mathcal{O}_X(D) = \mathcal{O}_X(\lfloor D \rfloor)$.

Lean: not in Lean as stated.

**Proposition P3.8.28 (first properties).** Let $D, D' \in \operatorname{Div}(X)$.

1. $\mathcal{O}_X(D)$ is a sheaf of $\mathcal{O}_X$-modules. For an affine open $U = \operatorname{Spec} A$, $\mathcal{O}_X(D)|_U = \widetilde{A(D|_U)}$, with $A(D|_U)$ the divisorial fractional ideal of Theorem P1.11.24. So $\mathcal{O}_X(D)$ is coherent.
2. $\mathcal{O}_X(0) = \mathcal{O}_X$. If $D \leq D'$, then $\mathcal{O}_X(D) \subseteq \mathcal{O}_X(D')$. Multiplication in $K$ maps $\mathcal{O}_X(D) \otimes \mathcal{O}_X(D')$ to $\mathcal{O}_X(D + D')$. In particular $\mathcal{O}_X(-D)$ is an ideal sheaf for $D \geq 0$.
3. For $g \in K^*$, multiplication by $g$ is an isomorphism $\mathcal{O}_X(D) \to \mathcal{O}_X(D - \operatorname{div}(g))$. So $\mathcal{O}_X(D) \cong \mathcal{O}_X(D')$ if $D \sim D'$.
4. Conversely, every isomorphism $\mathcal{O}_X(D) \to \mathcal{O}_X(D')$ of $\mathcal{O}_X$-modules is multiplication by some $g \in K^*$ with $D' = D - \operatorname{div}(g)$. So $\mathcal{O}_X(D) \cong \mathcal{O}_X(D')$ if and only if $D \sim D'$.
5. If $Z \subseteq X$ is closed of codimension at least $2$ and $U \subseteq X$ is open, the restriction $\mathcal{O}_X(D)(U) \to \mathcal{O}_X(D)(U \setminus Z)$ is bijective.
6. $\mathcal{O}_X(D)$ is invertible near $x$ if and only if $D$ is locally principal at $x$.

Lean: not in Lean as stated.

**Theorem P3.8.29 (sections and linear systems).** Let $D \in \operatorname{Div}(X)$.

1. $\Gamma(X, \mathcal{O}_X(D)) = \{ f \in K^* : \operatorname{div}(f) + D \geq 0 \} \cup \{0\}$.
2. The map $f \mapsto \operatorname{div}(f) + D$ induces a bijection from $(\Gamma(X, \mathcal{O}_X(D)) \setminus \{0\})/\mathcal{O}_X(X)^*$ to the set $|D|$ of effective divisors linearly equivalent to $D$, the *complete linear system* of $D$.
3. If $X$ is a scheme over a field $k$ with $\mathcal{O}_X(X)^* = k^*$, for example $X = \mathbb{P}^n_k$, then $|D|$ is the set of $k$-points of the projective space of lines in $\Gamma(X, \mathcal{O}_X(D))$.

Lean: not in Lean as stated.

**Proposition P3.8.30 (divisors on projective space).** Let $H = V_+(x_0) \subseteq \mathbb{P}^n_k$ and $d \in \mathbb{Z}$. The map $F \mapsto F/x_0^d$ on homogeneous elements of degree $d$ of the localizations $S_{x_i}$ defines an isomorphism $\mathcal{O}_{\mathbb{P}^n}(d) \to \mathcal{O}_{\mathbb{P}^n}(dH)$. So $\Gamma(\mathbb{P}^n_k, \mathcal{O}(dH)) = \{F/x_0^d : F \in S_d\}$, and for $d \geq 0$, $|dH|$ is the set of hypersurfaces of degree $d$, counted with multiplicity.

Lean: not in Lean as stated.

### Proof in words

The sheaf $\mathcal{O}_X(D)$ consists of the rational functions whose poles are bounded by $D$. The condition is checked divisor by divisor, so the sheaf is the global form of the divisorial ideals of P1 Ch. 11, and it does not see closed sets of codimension two. Changing $D$ by a principal divisor changes the sheaf by multiplication with a function, and every isomorphism has this form because a homomorphism between two subsheaves of $\mathcal{K}$ of rank one is determined at the generic point. A global section $f$ gives an effective divisor $\operatorname{div}(f) + D$, and two sections give the same divisor exactly when their ratio is a unit, which is the projectivization of the space of sections.

### Examples

**Example P3.8.31 (the projective line).** On $\mathbb{P}^1_k$ let $D = d \cdot \infty$ with $d \geq 0$. A function $f \in k(t)$ lies in $\Gamma(\mathcal{O}(D))$ if and only if it has no poles on $\mathbb{A}^1_k$, so $f \in k[t]$ by Proposition P3.8.4, and $\operatorname{ord}_\infty(f) \geq -d$, so $\deg f \leq d$. So $\Gamma(\mathbb{P}^1_k, \mathcal{O}(d \cdot \infty)) = \{f \in k[t] : \deg f \leq d\}$, of dimension $d + 1$, which matches $\Gamma(\mathcal{O}(d))$ via Proposition P3.8.30. The linear system $|D|$ is the set of effective divisors of degree $d$ on $\mathbb{P}^1_k$.

**Example P3.8.32 (a sheaf that is not invertible).** On the quadric cone $X = \operatorname{Spec} A$, $A = k[x, y, z]/(xy - z^2)$, let $L = V(x, z)$ and $M = V(y, z)$. By Example P3.8.8, $\operatorname{div}(x) = 2L$ and $\operatorname{div}(z) = L + M$. Then $\mathcal{O}_X(-L)$ is the ideal sheaf of $L$, the sheaf of the prime $(x, z)$, which needs two generators at the vertex. By part 3 of Proposition P3.8.28, $\mathcal{O}_X(L) = x^{-1} \mathcal{O}_X(L - \operatorname{div}(x)) = x^{-1} \mathcal{O}_X(-L)$, with sections $A + A \cdot (z/x)$. Neither sheaf is invertible at the vertex, since $L$ is not locally principal there (Example P1.8.22). The sheaf $\mathcal{O}_X(2L) = x^{-1} \mathcal{O}_X$ is invertible. The product of the sections of $\mathcal{O}_X(L)$ with themselves is $x^{-2}(x, z)^2 = x^{-1} \mathfrak{m}$, with $\mathfrak{m} = (x, y, z)$, a proper subsheaf of $\mathcal{O}_X(2L)$, as in Example P1.11.26.

**Example P3.8.33 (sections on a surface with a curve removed).** Let $X = \mathbb{A}^2_k$ and $D = V(x)$. Then $\Gamma(\mathcal{O}_X(mD)) = x^{-m} k[x, y]$ for $m \geq 0$, and $\bigcup_m \Gamma(\mathcal{O}_X(mD)) = k[x, x^{-1}, y] = \mathcal{O}(X \setminus D)$. For the origin $P$, which is not a divisor, no sheaf $\mathcal{O}_X(D)$ has poles at $P$ alone: $\Gamma(X \setminus P, \mathcal{O}_X) = \Gamma(X, \mathcal{O}_X)$ by part 5 of Proposition P3.8.28 with $D = 0$.

**Example P3.8.34 (round down).** On $\mathbb{A}^1_k$ let $D = \frac{1}{2} [0] - \frac{1}{3} [1]$. Then $\lfloor D \rfloor = -[1]$, and $\Gamma(\mathcal{O}(D)) = (t - 1) k[t]$. The round down does not commute with addition: $\lfloor D \rfloor + \lfloor D \rfloor = -2[1]$, while $\lfloor 2D \rfloor = [0] - [1]$. This is why the sheaves $\mathcal{O}_X(mD)$ for a $\mathbb{Q}$-divisor $D$ are computed one $m$ at a time.

### Proof

*Proof of Proposition P3.8.28.* (1) For $f \in \mathcal{O}_X(D)(U)$ and $a \in \mathcal{O}_X(U)$, $\operatorname{div}(af) + D = \operatorname{div}(a) + \operatorname{div}(f) + D$, and $\operatorname{div}(a)|_U \geq 0$ by part 4 of Proposition P3.8.2. The sum of two elements is in $\mathcal{O}_X(D)(U)$, as $\operatorname{ord}_E(f + g) \geq \min(\operatorname{ord}_E(f), \operatorname{ord}_E(g))$ for every prime divisor $E$ (Proposition P3.8.2, part 2). So the sections form an $\mathcal{O}_X(U)$-submodule of $K$. The conditions are compatible with restriction, and the sheaf property holds because a prime divisor meeting $U = \bigcup U_i$ meets some $U_i$, and the condition at that divisor can be checked on $U_i$, as the order is computed in the same local ring. For $U = \operatorname{Spec} A$ and $g \in A$, the sections over $D(g)$ are the $f$ with $v_\mathfrak{p}(f) + n_\mathfrak{p} \geq 0$ for the height one primes $\mathfrak{p}$ not containing $g$, which is $A(D|_U)_g$, by the description of the localizations of $A(D|_U)$ at height one primes in Theorem P1.11.24 and Krull's theorem (Theorem P1.8.2) for $A_g$. So $\mathcal{O}_X(D)|_U$ is the sheaf associated with the $A$-module $A(D|_U)$, which is finitely generated, as it is a fractional ideal of the Noetherian domain $A$ (Theorem P1.11.24). By Proposition P3.5.22, $\mathcal{O}_X(D)$ is coherent.

(2) $\mathcal{O}_X(0)(U) = \mathcal{O}_X(U)$ by Proposition P3.8.4. The inclusion for $D \leq D'$ and the product statement follow from $\operatorname{div}(fg) + D + D' = (\operatorname{div}(f) + D) + (\operatorname{div}(g) + D')$. For $D \geq 0$, $\mathcal{O}_X(-D) \subseteq \mathcal{O}_X(0) = \mathcal{O}_X$.

(3) $\operatorname{div}(gf) + D - \operatorname{div}(g) = \operatorname{div}(f) + D$, so $f \mapsto gf$ maps $\mathcal{O}_X(D)(U)$ onto $\mathcal{O}_X(D - \operatorname{div}(g))(U)$, with inverse multiplication by $g^{-1}$.

(4) Let $\varphi \colon \mathcal{O}_X(D) \to \mathcal{O}_X(D')$ be an isomorphism. Choose a nonempty affine open $U = \operatorname{Spec} A$ and a nonzero $s \in \mathcal{O}_X(D)(U)$, which exists as $A(D|_U)$ is a nonzero fractional ideal. Put $g = \varphi(s)/s \in K^*$; note $\varphi(s) \neq 0$, as $\varphi$ is injective. Let $W \subseteq U$ be a nonempty affine open and $f \in \mathcal{O}_X(D)(W)$ nonzero. As $K$ is the fraction field of $\mathcal{O}_X(W)$, write $f/s = a/b$ with $a, b \in \mathcal{O}_X(W)$, $b \neq 0$. Then $bf = as|_W$ in $\mathcal{O}_X(D)(W)$, and $\mathcal{O}_X$-linearity gives $b \varphi(f) = a \varphi(s)|_W = a g s = b g f$, so $\varphi(f) = gf$. Let $V$ be any nonempty open and $f \in \mathcal{O}_X(D)(V)$. As $X$ is irreducible, $V \cap U$ contains a nonempty affine open $W$, and $\varphi(f)|_W = gf|_W$. The restriction maps of $\mathcal{K}$ between nonempty opens are the identity of $K$, so $\varphi(f) = gf$. So $\varphi$ is multiplication by $g$, and $\mathcal{O}_X(D') = g \mathcal{O}_X(D) = \mathcal{O}_X(D - \operatorname{div}(g))$ by part 3. Two divisors with the same sheaf are equal: for a prime divisor $E$ with coefficients $n$ in $D$ and $n'$ in $D'$, on an affine open meeting $E$ the localizations at the height one prime of $E$ are $t^{-n} A_\mathfrak{p}$ and $t^{-n'} A_\mathfrak{p}$ by Theorem P1.11.24, so $n = n'$. So $D' = D - \operatorname{div}(g)$.

(5) The prime divisors meeting $U$ are the prime divisors meeting $U \setminus Z$, since a prime divisor $E$ with $E \cap U \subseteq Z$ has $E \cap U$ of codimension $1$ in $U$ inside $Z \cap U$, of codimension at least $2$ in $U$. So both sets of sections are defined by the same conditions in $K$, and restriction is the identity of $K$ on them.

(6) If $D|_U = \operatorname{div}(f)|_U$, then $\mathcal{O}_X(D)|_U = f^{-1} \mathcal{O}_U$ by parts 2 and 3 applied on $U$, which is free of rank one. Conversely, let $\mathcal{O}_X(D)|_U \cong \mathcal{O}_U$ for an affine open $U = \operatorname{Spec} A \ni x$, so that $A(D|_U) = sA$ for some $s \in K^*$. Then $\mathcal{O}_X(D)|_U = \mathcal{O}_U(-\operatorname{div}(s)|_U)$ by part 3, and by the last argument of part 4, $D|_U = -\operatorname{div}(s)|_U = \operatorname{div}(s^{-1})|_U$. $\square$

*Proof of Theorem P3.8.29.* (1) This is the definition with $U = X$.

(2) The divisor $\operatorname{div}(f) + D$ is effective and linearly equivalent to $D$. Every effective $E \sim D$ is $D + \operatorname{div}(f)$ for some $f \in K^*$, and then $f \in \Gamma(X, \mathcal{O}_X(D))$. Finally $\operatorname{div}(f) + D = \operatorname{div}(f') + D$ if and only if $\operatorname{div}(f/f') = 0$, that is $f/f' \in \mathcal{O}_X(X)^*$ by Proposition P3.8.11.

(3) If $\mathcal{O}_X(X)^* = k^*$, the classes in part 2 are the nonzero vectors of the $k$-vector space $\Gamma(X, \mathcal{O}_X(D))$ up to a scalar. For $X = \mathbb{P}^n_k$, $\mathcal{O}_X(X) = k$ by Theorem P3.6.12 with $m = 0$. $\square$

*Proof of Proposition P3.8.30.* On $U_i = D_+(x_i)$, $H|_{U_i} = \operatorname{div}(x_0/x_i)|_{U_i}$, since $x_0/x_i$ is a coordinate on $U_i \cong \mathbb{A}^n_k$ for $i \neq 0$ and a unit for $i = 0$. So $\mathcal{O}(dH)|_{U_i} = (x_i/x_0)^d \mathcal{O}_{U_i}$, by part 6 of the proof above. The sections of $\mathcal{O}(d)$ over $U_i$ are $x_i^d \cdot S_{(x_i)}$, and $F \mapsto F/x_0^d$ maps $x_i^d \cdot g$, $g \in S_{(x_i)}$, to $(x_i/x_0)^d g$. So the map is an isomorphism over each $U_i$, and the maps agree on overlaps, as they are all given by the same formula in $K$. The global sections of $\mathcal{O}(d)$ are $S_d$ by Theorem P3.6.12, which gives the description of $\Gamma(\mathcal{O}(dH))$. For $d \geq 0$ and $F \in S_d$ nonzero, $\operatorname{div}(F/x_0^d) + dH = \sum_i a_i D_{F_i}$ for $F = c \prod F_i^{a_i}$, by Theorem P3.8.20, which is the hypersurface $V_+(F)$ with multiplicities. $\square$

### Exercises

1. (A) On $\mathbb{P}^1_k$ compute $\Gamma(\mathcal{O}(D))$ for $D = 2[0] - [\infty]$ and for $D = [0] + [1] - 3[\infty]$. Show that $\dim_k \Gamma(\mathbb{P}^1_k, \mathcal{O}(D)) = \max(0, \deg D + 1)$ for every $D$ supported at $k$-points.
2. (A) On the quadric cone of Example P3.8.32, show that $\Gamma(\mathcal{O}_X(L))$ is generated as an $A$-module by $1$ and $z/x$, and that $z/x = y/z$ in $K$.
3. (A) On $\mathbb{A}^2_k$, show that $\mathcal{O}_X(D) \cong \mathcal{O}_X$ for every divisor $D$, and find the generator of $\mathcal{O}_X(D)$ for $D = 2V(x) - V(y - x^2)$.
4. (B) Let $X$ be the quadric cone. Show that $\mathcal{O}_X(L) \otimes \mathcal{O}_X(L) \to \mathcal{O}_X(2L)$ is not surjective, and that its image is $x^{-1} \mathfrak{m}^\sim$. Show that $\mathcal{O}_X(L)$ is isomorphic to its dual $\mathcal{H}om(\mathcal{O}_X(L), \mathcal{O}_X)$, by identifying the dual with $\mathcal{O}_X(-L)$.
5. (B) Let $D$ be locally principal and $E$ any divisor. Show that $\mathcal{O}_X(D) \otimes \mathcal{O}_X(E) \to \mathcal{O}_X(D + E)$ is an isomorphism.
6. (B) Let $X = \mathbb{P}^1 \times \mathbb{P}^1$ and $D$ a divisor of bidegree $(a, b)$ with $a, b \geq 0$. Show that $\Gamma(X, \mathcal{O}_X(D))$ is isomorphic to the space of bihomogeneous polynomials of bidegree $(a, b)$, of dimension $(a + 1)(b + 1)$.
7. (C) Let $\mathcal{F} \subseteq \mathcal{K}$ be a coherent subsheaf with $\mathcal{F} \neq 0$ such that $\mathcal{F}(U) \to \mathcal{F}(U \setminus Z)$ is bijective for every open $U$ and every closed $Z$ of codimension at least $2$. Show that $\mathcal{F} = \mathcal{O}_X(D)$ for a unique divisor $D$. Use Theorem P1.11.24 on affine opens.

### Lean

Mathlib has no sheaf $\mathcal{O}_X(D)$ of a Weil divisor, no divisorial sheaves and no linear systems of Weil divisors. The twisting sheaves $\mathcal{O}(d)$ of projective space are also not in Mathlib, so Proposition P3.8.30 is not in Lean as stated. For rings, divisorial fractional ideals are not in Mathlib either. The handbook adds no `MinimalModel` node here.

### Notes and history

The sheaf $\mathcal{O}_X(D)$ is the sheaf form of the Riemann-Roch spaces $L(D)$ of a curve, the spaces of functions with poles bounded by $D$. On a normal variety these are exactly the reflexive sheaves of rank one, by Exercise 7 and Theorem P1.11.24. Hartshorne, Section II.6, defines $\mathcal{O}_X(D)$ only for Cartier divisors and treats reflexive sheaves later, while Vakil and Görtz-Wedhorn define it for Weil divisors as here. The literature state is theorem. In the minimal model program the canonical sheaf of a normal variety is $\mathcal{O}_X(K_X)$, the sheaves $\mathcal{O}_X(mK_X)$ define the canonical ring $\bigoplus_{m \geq 0} \Gamma(X, \mathcal{O}_X(mK_X))$, and part 5 of Proposition P3.8.28 is the reason why a flip, an isomorphism in codimension one, does not change this ring.
