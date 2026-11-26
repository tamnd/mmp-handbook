---
title: Pullback of divisors
nodes: []
sources: [Vak25, Har77, GW20, Stacks]
reads_with: [Vak25:ch14, Har77:II.6, GW20:ch11]
requires: [P2.6, P3.5, P3.8]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Pullback of divisors

### Statement

Let $f \colon X \to Y$ be a morphism of integral schemes, with generic points $\eta_X$ and $\eta_Y$ and function fields $K(X)$ and $K(Y)$. Put $\xi = f(\eta_X)$. The map on stalks $f^\sharp_{\eta_X} \colon \mathcal{O}_{Y, \xi} \to \mathcal{O}_{X, \eta_X} = K(X)$ is a local homomorphism to a field, so it sends units to nonzero elements. For $g \in \mathcal{O}_{Y, \xi}$ write $f^* g$ for its image in $K(X)$. If $f$ is dominant, then $\xi = \eta_Y$, $\mathcal{O}_{Y, \xi} = K(Y)$, and $f^* \colon K(Y) \to K(X)$ is the field extension of $f$.

**Definition P3.9.26 (pullback of a Cartier divisor).** Let $D = \{(U_i, f_i)\}$ be a Cartier divisor on $Y$ with $\xi \notin \operatorname{Supp} D$. Every $i$ with $f^{-1}(U_i) \neq \emptyset$ has $\xi \in U_i$, since the nonempty open set $f^{-1}(U_i)$ contains $\eta_X$, and $f_i \in \mathcal{O}_{Y, \xi}^*$, since $\xi \notin \operatorname{Supp} D$. The *pullback* of $D$ is
$$
f^* D = \{(f^{-1}(U_i), f^* f_i)\} ,
$$
over the $i$ with $f^{-1}(U_i) \neq \emptyset$. Write $\operatorname{CaDiv}_f(Y)$ for the set of Cartier divisors $D$ with $\xi \notin \operatorname{Supp} D$.

Lean: not in Lean as stated.

**Proposition P3.9.27 (properties of the pullback).** In the situation of Definition P3.9.26:

1. $f^* D$ is a Cartier divisor on $X$ that does not depend on the datum of $D$. The set $\operatorname{CaDiv}_f(Y)$ is a subgroup of $\operatorname{CaDiv}(Y)$, and $f^* \colon \operatorname{CaDiv}_f(Y) \to \operatorname{CaDiv}(X)$ is a homomorphism with $\operatorname{Supp} f^* D \subseteq f^{-1}(\operatorname{Supp} D)$.
2. If $D$ is effective, so is $f^* D$, and $\mathcal{I}_{f^* D} = \mathcal{I}_D \mathcal{O}_X$ is the image of $f^* \mathcal{I}_D \to \mathcal{O}_X$. So the closed subscheme $f^* D$ is the fibre product $D \times_Y X$.
3. For $g \in \mathcal{O}_{Y, \xi}^*$, $\operatorname{div}(g) \in \operatorname{CaDiv}_f(Y)$ and $f^* \operatorname{div}(g) = \operatorname{div}(f^* g)$.
4. $\mathcal{O}_X(f^* D) \cong f^* \mathcal{O}_Y(D)$.
5. If $h \colon Y \to Z$ is a morphism of integral schemes and $D \in \operatorname{CaDiv}_{h \circ f}(Z)$, then $D \in \operatorname{CaDiv}_h(Z)$, $h^* D \in \operatorname{CaDiv}_f(Y)$, and $(h \circ f)^* D = f^*(h^* D)$.
6. If $f$ is dominant, then $\operatorname{CaDiv}_f(Y) = \operatorname{CaDiv}(Y)$, and $f^*$ induces a homomorphism $\operatorname{CaCl}(Y) \to \operatorname{CaCl}(X)$ that corresponds to $f^* \colon \operatorname{Pic}(Y) \to \operatorname{Pic}(X)$ under Theorem P3.9.4.
7. Let $Y$ be normal and Noetherian and $\pi \colon Y \times \mathbb{A}^1 \to Y$ the projection. For every Cartier divisor $D$ on $Y$ the Weil divisor of $\pi^* D$ is $[\pi^* D] = \pi^{-1}[D]$, with the notation of Theorem P3.8.14.

Lean: not in Lean as stated. The pullback of sheaves of modules is `AlgebraicGeometry.Scheme.Modules.pullback`.

**Proposition P3.9.28 (pullback of $\mathbb{Q}$-Cartier divisors).** Let $X$ and $Y$ be normal integral Noetherian schemes, $f \colon X \to Y$ a morphism and $D$ a $\mathbb{Q}$-Cartier Weil divisor on $Y$ with $f(\eta_X) \notin \operatorname{Supp} D$. Let $m \geq 1$ be an integer with $mD$ Cartier, and identify $mD$ with a Cartier divisor by Proposition P3.9.9. Then
$$
f^* D = \tfrac{1}{m} [f^*(mD)] \in \operatorname{Div}(X) \otimes \mathbb{Q}
$$
does not depend on $m$. It is additive, it agrees with $[f^* D]$ when $D$ is Cartier, it is effective when $D$ is, and $D \sim_\mathbb{Q} D'$ implies $f^* D \sim_\mathbb{Q} f^* D'$ when both pullbacks are defined. The same formula defines $f^* \Delta$ for a $\mathbb{Q}$-Cartier $\mathbb{Q}$-divisor $\Delta$ with $f(\eta_X) \notin \operatorname{Supp} \Delta$.

Lean: not in Lean as stated.

**Proposition P3.9.29 (pullback on Dedekind schemes).** Let $X$ and $Y$ be Dedekind schemes, that is, normal integral Noetherian schemes of dimension $1$, and $f \colon X \to Y$ a dominant morphism. Let $y \in Y$ be a closed point with uniformizer $t_y$ of the discrete valuation ring $\mathcal{O}_{Y, y}$. Then $f^{-1}(y)$ is a finite set of closed points, and
$$
f^*[y] = \sum_{x \in f^{-1}(y)} e_x [x], \qquad e_x = \operatorname{ord}_x(f^* t_y) \geq 1 .
$$
The integer $e_x$ is the *ramification index* of $f$ at $x$.

Lean: not in Lean as stated.

### Proof in words

A Cartier divisor is given by local equations, and a local equation can be composed with a morphism. The only danger is that the composite is zero, which happens when the image of the generic point lies on the divisor. When the pullback exists, it commutes with sums, with principal divisors and with the line bundles of Section 9.1, as all three are built from the local equations. A $\mathbb{Q}$-Cartier divisor is pulled back by clearing denominators, pulling back a Cartier multiple, and dividing again. On curves this gives the classical formula in which each point of the fibre counts with its ramification index.

### Examples

**Example P3.9.30 (a map of degree $d$ of the projective line).** Let $f \colon \mathbb{P}^1_k \to \mathbb{P}^1_k$, $[s : t] \mapsto [s^d : t^d]$, with $d \geq 1$. Let $0 = [0 : 1]$, with uniformizer $u = s/t$ on $D_+(t)$. Since $f^* u = u^d$ and $f^{-1}(0) = \{0\}$, Proposition P3.9.29 gives $f^*[0] = d [0]$. The divisor $[0]$ is the hyperplane $V_+(s)$, so $\mathcal{O}([0]) \cong \mathcal{O}(1)$ by Example P3.9.5, and part 4 of Proposition P3.9.27 gives $f^* \mathcal{O}(1) \cong \mathcal{O}(d[0]) \cong \mathcal{O}(d)$. This agrees with the direct computation from the transition function $s/t$ of $\mathcal{O}(1)$, which pulls back to $(s/t)^d$, the transition function of $\mathcal{O}(d)$.

**Example P3.9.31 (the cone $xy = z^2$).** Let $k$ be perfect with $\operatorname{char} k \neq 2$, $X_2 = V(xy - z^2) \subseteq \mathbb{A}^3_k$, and $L = V(x, z)$ and $M = V(y, z)$ as in Example P3.9.21.

1. Let $\pi \colon \mathbb{A}^2_k \to X_2$, $(u, v) \mapsto (u^2, v^2, uv)$. It is finite and surjective, so dominant. Since $2L = \operatorname{div}(x)$ and $\pi^* x = u^2$, Proposition P3.9.28 gives $\pi^* L = \frac{1}{2} \operatorname{div}(u^2) = V(u)$, an integral Cartier divisor, although $L$ is not Cartier. In the same way $\pi^* M = V(v)$, and $\pi^* \operatorname{div}(z) = \operatorname{div}(uv) = V(u) + V(v)$, as additivity requires.
2. Let $i \colon M \to X_2$ be the inclusion of the line $M \cong \mathbb{A}^1_k$, with coordinate $x$. The generic point of $M$ is not on $L$, and $i^* x = x$. So $i^* L = \frac{1}{2} \operatorname{div}(x) = \frac{1}{2} [0]$. The pullback of a Weil divisor that is only $\mathbb{Q}$-Cartier can have fractional coefficients, and the denominator $2$ is the index of $L$.

**Example P3.9.32 (a chart of the blow-up of the plane).** Let $\sigma \colon \mathbb{A}^2_k \to \mathbb{A}^2_k$, $(x, t) \mapsto (x, xt)$, which is birational, so dominant. Let $C = V(y)$ on the target. Since $\sigma^* y = xt$, $\sigma^* C = V(x) + V(t)$. Here $E = V(x) = \sigma^{-1}(0)$ is the exceptional curve of the chart, and $V(t)$ is the strict transform of $C$. For a curve $V(g)$ through the origin with $g$ of order $m$ at the origin, $\sigma^* g = x^m g_1$ with $x \nmid g_1$, and $\sigma^* V(g) = mE + V(g_1)$. Chapter 11 develops this.

**Example P3.9.33 (restriction to a subvariety and moving lemma).** Let $\ell \subseteq \mathbb{P}^2_k$ be the line $V_+(z)$ and $i \colon \ell \to \mathbb{P}^2_k$ the inclusion. For $D = \ell$ the point $i(\eta_\ell)$ is the generic point of $\operatorname{Supp} D$, so $i^* D$ is not defined. The line bundle $i^* \mathcal{O}(\ell) = i^* \mathcal{O}(1) = \mathcal{O}_\ell(1)$ is still defined. The divisor $\ell' = V_+(x)$ satisfies $\ell' \sim \ell$, since $\ell' - \ell = \operatorname{div}(x/z)$, and $i^* \ell'$ is the point $[0 : 1 : 0]$ of $\ell$. Its class in $\operatorname{CaCl}(\ell) = \operatorname{Pic}(\ell)$ is that of $\mathcal{O}_\ell(1)$, as part 4 of Proposition P3.9.27 predicts. So on the level of classes the pullback is always defined, by moving the divisor in its class.

**Example P3.9.34 (a conic and its tangent line).** Let $i \colon \mathbb{P}^1_k \to \mathbb{P}^2_k$, $[s : t] \mapsto [s^2 : st : t^2]$, with image the conic $C = V_+(xz - y^2)$. On $D_+(x)$ the line $T = V_+(z)$ has local equation $z/x$, and $i^*(z/x) = (t/s)^2$. So $i^* T = 2[1 : 0]$, and $T$ is tangent to $C$ at $[1 : 0 : 0]$. The line $S = V_+(y)$ gives $i^*(y/x) = t/s$ near $[1 : 0]$ and $i^*(y/z) = s/t$ near $[0 : 1]$, so $i^* S = [1 : 0] + [0 : 1]$, two transverse intersections. In both cases the degree is $2$, and $i^* \mathcal{O}_{\mathbb{P}^2}(1) \cong \mathcal{O}_{\mathbb{P}^1}(2)$.

### Proof

*Proof of Proposition P3.9.27.* (1) For $i, j$ with $f^{-1}(U_i \cap U_j) \neq \emptyset$, $u = f_i/f_j \in \mathcal{O}_Y(U_i \cap U_j)^*$, so $f^\sharp u \in \mathcal{O}_X(f^{-1}(U_i \cap U_j))^*$. Its germ at $\eta_X$ is the image of the germ of $u$ at $\xi$, that is, $f^* f_i / f^* f_j$. So $f^* f_i / f^* f_j$ is a unit on $f^{-1}(U_i \cap U_j)$, and $f^* D$ is a Cartier datum. If $\{(V_k, g_k)\}$ is an equivalent datum, the same argument applied to the union of the two data shows that the union of the pullbacks is a Cartier datum, so the pullbacks are equivalent. The set $\operatorname{CaDiv}_f(Y)$ contains $0$ and is closed under sums and negatives, since $f_i g_k$ and $f_i^{-1}$ are units at $\xi$ when $f_i$ and $g_k$ are. The pullback of a product of local equations is the product of the pullbacks, so $f^*$ is a homomorphism. If $x \in f^{-1}(U_i)$ and $f(x) \notin \operatorname{Supp} D$, then $f_i \in \mathcal{O}_{Y, f(x)}^*$, so $f_i$ is a unit on an open $V \ni f(x)$, $f^\sharp f_i$ is a unit on $f^{-1}(V)$, and $x \notin \operatorname{Supp} f^* D$.

(2) Let $f_i \in \mathcal{O}_Y(U_i)$. Then $f^* f_i$ is the germ of $f^\sharp f_i \in \mathcal{O}_X(f^{-1}(U_i))$, so $f^* D$ is effective, and its ideal on $f^{-1}(U_i)$ is generated by $f^\sharp f_i$. This is the image of $f^* (f_i \mathcal{O}_{U_i}) \to \mathcal{O}_{f^{-1}(U_i)}$. The closed subscheme defined by $\mathcal{I}_D \mathcal{O}_X$ is $D \times_Y X$, the preimage of the closed subscheme $D$ (Chapter 3, Section 3.3).

(3) $\operatorname{Supp} \operatorname{div}(g)$ is the set of points where $g$ is not a unit of the local ring, which does not contain $\xi$. The pullback of the datum $\{(Y, g)\}$ is $\{(X, f^* g)\}$.

(4) The isomorphisms $\mathcal{O}_{U_i} \to \mathcal{O}_Y(D)|_{U_i}$, $a \mapsto a f_i^{-1}$, of Proposition P3.9.3 exhibit $\mathcal{O}_Y(D)$ as the line bundle glued from the $\mathcal{O}_{U_i}$ along multiplication by $f_j/f_i \in \mathcal{O}_Y(U_i \cap U_j)^*$, since $a f_i^{-1} = (a f_j/f_i) f_j^{-1}$. The pullback $f^* \mathcal{O}_Y(D)$ is glued from the $\mathcal{O}_{f^{-1}(U_i)}$ along multiplication by $f^\sharp(f_j/f_i)$. By the same computation, $\mathcal{O}_X(f^* D)$ is glued from these sheaves along multiplication by $f^* f_j / f^* f_i = f^\sharp(f_j/f_i)$. So the two line bundles are isomorphic.

(5) Put $\zeta = h(\xi)$, the image of $\eta_X$ in $Z$. A local equation $f_i$ of $D$ is a unit at $\zeta = (h \circ f)(\eta_X)$. Since $h(\eta_Y)$ is a generization of $\zeta$, the local ring $\mathcal{O}_{Z, h(\eta_Y)}$ is a localization of $\mathcal{O}_{Z, \zeta}$, and $f_i$ is also a unit there, so $D \in \operatorname{CaDiv}_h(Z)$. The element $h^* f_i$ lies in the image of $\mathcal{O}_{Z, \zeta}^* \to \mathcal{O}_{Y, \xi}$, which consists of units, so $h^* D \in \operatorname{CaDiv}_f(Y)$. The two pullbacks of $f_i$ are images of $f_i$ under the same composite of maps of stalks $\mathcal{O}_{Z, \zeta} \to \mathcal{O}_{Y, \xi} \to K(X)$, so they agree.

(6) If $f$ is dominant, then $\xi = \eta_Y$, which lies in no support, since every element of $K(Y)^*$ is a unit of $\mathcal{O}_{Y, \eta_Y} = K(Y)$. By (3), $f^*$ maps principal divisors to principal divisors, so it induces a map on $\operatorname{CaCl}$. By (4) and Theorem P3.9.4 it corresponds to $f^*$ on $\operatorname{Pic}$.

(7) The projection is dominant, so $\pi^* D$ is defined by (6). Both sides are additive, and both are local on $Y$, so it suffices to treat $D = \operatorname{div}(g)$ on an open $U \subseteq Y$, where $[\pi^* D] = \operatorname{div}(\pi^* g)$ by (3). Let $P$ be a prime divisor of $U$ with discrete valuation ring $R = \mathcal{O}_{Y, P}$ and uniformizer $\varpi$. The prime divisor $\pi^{-1}(P)$ has local ring $R' = R[t]_{\mathfrak{m}_R R[t]}$, and $\mathfrak{m}_R R[t] = \varpi R[t]$ is prime, as $R[t]/\varpi R[t] = \kappa(P)[t]$ is a domain. So $\varpi$ generates the maximal ideal of $R'$, and $\operatorname{ord}_{\pi^{-1}(P)}(g) = \operatorname{ord}_P(g)$ for $g \in K(Y)^*$. By Theorem P3.8.14 every prime divisor of $U \times \mathbb{A}^1$ on which $\pi^* g$ has nonzero order is of this form: a prime divisor $Q$ of $U \times \mathbb{A}^1$ that dominates $U$ has $\mathcal{O}_{Y \times \mathbb{A}^1, Q} \supseteq K(Y)$, and $g$ is a unit there. So $\operatorname{div}(\pi^* g) = \sum_P \operatorname{ord}_P(g) \, \pi^{-1}(P) = \pi^{-1}(\operatorname{div}(g))$. $\square$

*Proof of Proposition P3.9.28.* By Proposition P3.9.9 the Weil divisor of $mD$ has support $\operatorname{Supp} D$, and on a normal scheme the support of a Cartier divisor $C$ is the support of $[C]$: a local equation $h$ near $x$ is a unit at $x$ if and only if $h$ and $h^{-1}$ have no poles near $x$, by Proposition P3.8.4. So $mD \in \operatorname{CaDiv}_f(Y)$. If $mD$ and $m'D$ are Cartier, then $f^*(mm'D) = m' f^*(mD) = m f^*(m'D)$ by part 1 of Proposition P3.9.27, and dividing by $mm'$ gives the independence. Additivity follows by taking a common multiple. For $D$ Cartier take $m = 1$. If $D \geq 0$, then $mD$ is an effective Cartier divisor by Proposition P3.9.9, so $f^*(mD) \geq 0$ by part 2 of Proposition P3.9.27. If $m(D - D') = \operatorname{div}(g)$ with $mD$ and $mD'$ Cartier, then $g$ is a unit at $f(\eta_X)$, since $\operatorname{Supp} \operatorname{div}(g) \subseteq \operatorname{Supp} D \cup \operatorname{Supp} D'$, and parts 1 and 3 of Proposition P3.9.27 give $f^*(mD) - f^*(mD') = \operatorname{div}(f^* g)$. So $m(f^* D - f^* D') = [\operatorname{div}(f^* g)]$ is principal. For a $\mathbb{Q}$-divisor $\Delta$ the same argument applies to the Weil divisors $m\Delta$. $\square$

*Proof of Proposition P3.9.29.* The points of $X$ are $\eta_X$ and the closed points, and $f(\eta_X) = \eta_Y \neq y$. The set $f^{-1}(y)$ is a closed subset that does not contain $\eta_X$, so it is a proper closed subset of the Noetherian scheme $X$ of dimension $1$, and so a finite set of closed points. The function $t_y$ has $\operatorname{ord}_y(t_y) = 1$, and by Lemma P3.8.3 there is an open $U \ni y$ on which $\operatorname{div}(t_y)|_U = [y]|_U$. So $[y]$ is the Cartier divisor $\{(U, t_y), (Y \setminus \{y\}, 1)\}$. Its pullback is $\{(f^{-1}(U), f^* t_y), (X \setminus f^{-1}(y), 1)\}$, whose Weil divisor is $\sum_{x \in f^{-1}(y)} \operatorname{ord}_x(f^* t_y) [x]$. Since $t_y \in \mathfrak{m}_y$ and $f^\sharp_x$ is a local homomorphism, $f^* t_y \in \mathfrak{m}_x$, so $e_x \geq 1$. $\square$

### Exercises

1. (A) Let $k$ be algebraically closed with $\operatorname{char} k \nmid d$. In Example P3.9.30 compute $f^*[1 : 1]$, and show that every point of $f^{-1}([1 : 1])$ has ramification index $1$.
2. (A) In part 1 of Example P3.9.31 compute $\pi^*(aL + bM)$ for integers $a, b$, and the pullback of $\frac{1}{2} L$.
3. (A) In Example P3.9.34 show that the line $V_+(x - 2y + z)$ pulls back to $2[1 : 1]$, and find all lines whose pullback is twice a point.
4. (B) Let $f \colon \mathbb{A}^1_k \to \mathbb{A}^2_k$, $t \mapsto (t, t)$, and $D = \operatorname{div}(x/y)$. Show that $f^* D = 0$, while $f^{-1}(\operatorname{Supp} D)$ is the origin. So the inclusion in part 1 of Proposition P3.9.27 can be strict.
5. (B) Show that the open immersion $\mathbb{A}^1_k \to \mathbb{P}^1_k$ induces the zero map $\operatorname{Pic}(\mathbb{P}^1_k) \to \operatorname{Pic}(\mathbb{A}^1_k)$. Show that for $X$ locally factorial and $U \subseteq X$ a nonempty open subscheme, $\operatorname{Pic}(X) \to \operatorname{Pic}(U)$ is surjective.
6. (B) In the situation of Proposition P3.9.28 assume $f$ is dominant. Show that $f^*$ is a homomorphism from the group of $\mathbb{Q}$-Cartier Weil divisors to $\operatorname{Div}(X) \otimes \mathbb{Q}$, and that its image consists of $\mathbb{Q}$-Cartier $\mathbb{Q}$-divisors.
7. (C) Let $Y$ be an integral scheme, $\pi \colon Y \times \mathbb{A}^1 \to Y$ the projection and $s \colon Y \to Y \times \mathbb{A}^1$ the zero section. Show that $\pi^* \colon \operatorname{Pic}(Y) \to \operatorname{Pic}(Y \times \mathbb{A}^1)$ is injective. For $Y$ normal and Noetherian and $D$ a Cartier divisor on $Y$, show that $s^* \pi^* D = D$.

### Lean

Mathlib defines the pullback of sheaves of modules on schemes, `AlgebraicGeometry.Scheme.Modules.pullback`, and the map on Picard groups of rings `CommRing.Pic.mapRingHom`. There is no Cartier divisor, and so no pullback of divisors. The statements of this section are not in Lean as stated. The handbook adds no `MinimalModel` node here.

### Notes and history

Hartshorne, Section II.6, discusses the pullback of Cartier divisors, and Görtz-Wedhorn, Chapter 11, treat it for schemes that need not be integral. The literature state is theorem. In the minimal model program the pullback of $\mathbb{Q}$-Cartier divisors is used in three ways. The ramification formula $K_X = f^* K_Y + R$ for a finite morphism, of which Proposition P3.9.29 is the case of curves, compares canonical divisors. For a resolution or a blow-up $f \colon X \to Y$, the discrepancies are the coefficients in $K_X = f^* K_Y + \sum a_i E_i$, and this needs $K_Y$ to be $\mathbb{Q}$-Cartier, so that $f^* K_Y$ is defined. The intersection number $D \cdot C$ of a $\mathbb{Q}$-Cartier divisor with a curve is the degree of the pullback to the normalization of $C$, and Example P3.9.31 shows that it can be fractional.
