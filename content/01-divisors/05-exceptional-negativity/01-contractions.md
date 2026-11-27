---
title: Contractions and exceptional loci
nodes: []
sources: [KM98, Har77, Deb01]
reads_with: [KM98:ch1, Har77:ch3, Deb01:ch1]
requires: [P3.4, P3.7, P3.11, P4.2, P4.6, 1.1]
level: background
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Contractions and exceptional loci

### Statement

P4 Chapter 6 proves Zariski's main theorem and the Stein factorization for projective morphisms of Noetherian schemes. This section restates them for varieties in the form in which the minimal model program uses them. It adds two facts: the rigidity lemma, which says when a morphism factors through a contraction, and a description of the exceptional locus of a projective birational morphism onto a normal variety. In this chapter $k$ is algebraically closed of characteristic 0, and a variety is an integral separated scheme of finite type over $k$.

**Definition 1.5.1 (contraction).** A *contraction* is a projective morphism $f \colon X \to Y$ of varieties with $f_* \mathcal{O}_X = \mathcal{O}_Y$. This is Definition P4.6.14 for varieties, and Definition 1.1.11 asks in addition that $X$ and $Y$ be normal.

Lean: `MinimalModel.IsContraction` (definition), in the project library: a projective morphism to a normal variety such that $f^\#$ is an isomorphism on every open set.

**Proposition 1.5.2 (first properties of contractions).** Let $f \colon X \to Y$ be a projective morphism of varieties.

1. If $f$ is a contraction, then $f$ is surjective and every fibre $X_y$ is nonempty and connected. If in addition $X$ is normal, then $Y$ is normal.
2. If $f$ is birational and $Y$ is normal, then $f$ is a contraction.
3. If $f$ and $g \colon Y \to Z$ are contractions, then $g \circ f$ is a contraction.
4. Let $X$ and $Y$ be normal and $f$ surjective. Then $f$ is a contraction if and only if $K(Y)$ is algebraically closed in $K(X)$.

Lean: not yet in Lean.

**Theorem 1.5.3 (Stein factorization from a normal variety).** Let $f \colon X \to Y$ be a projective morphism of varieties with $X$ normal. Then $f = g \circ f'$, where $f' \colon X \to Y'$ is a contraction onto a normal variety $Y'$ and $g \colon Y' \to Y$ is finite. For every $y \in Y$ the connected components of $X_y$ are the fibres of $f'$ over the finitely many points of $g^{-1}(y)$. The morphism $f$ is a contraction if and only if $g$ is an isomorphism.

Lean: not yet in Lean.

**Lemma 1.5.4 (rigidity).** Let $f \colon X \to Y$ be a contraction and $g \colon X \to Z$ a morphism to a scheme $Z$. Suppose that $g(X_y)$ is a single point for every point $y \in Y$. Then there is a unique morphism $h \colon Y \to Z$ with $g = h \circ f$.

Lean: not yet in Lean.

The lemma is how the program builds morphisms out of a contraction: a morphism that is constant on the fibres of $f$ descends to $Y$. It is also the tool behind uniqueness statements such as the one in Theorem 1.1.12.

**Definition 1.5.5 (exceptional locus, exceptional divisors).** Let $f \colon X \to Y$ be a projective birational morphism of varieties with $Y$ normal, and let $U \subseteq Y$ be the set of points $y$ with $X_y$ finite. By Corollary P4.6.10, $U$ is open and $f^{-1}(U) \to U$ is an isomorphism.

1. The *exceptional locus* of $f$ is the closed set $\operatorname{Exc}(f) = f^{-1}(Y \setminus U)$, as after Corollary P4.6.10.
2. A prime divisor $P$ of $X$ is *$f$-exceptional* if $\dim f(P) < \dim P$. An $\mathbb{R}$-divisor is *$f$-exceptional* if every component of its support is.
3. The *pushforward* of a prime divisor $P$ is $f_* P = f(P)$ if $P$ is not exceptional and $f_* P = 0$ if it is. It extends linearly to $\mathbb{R}$-divisors, that is, to finite sums $\sum_i b_i P_i$ with $b_i \in \mathbb{R}$.
4. The morphism $f$ is *small* if $\operatorname{Exc}(f)$ has codimension at least 2 in $X$, and *divisorial* if $\operatorname{Exc}(f)$ is a prime divisor.

**Proposition 1.5.6 (the exceptional locus).** Let $f \colon X \to Y$ be as in Definition 1.5.5, $n = \dim X$, and $U$ as there.

1. For $x \in X$ the following are equivalent: (a) $x \notin \operatorname{Exc}(f)$; (b) there is an open $V \ni x$ such that $f(V)$ is open and $f|_V \colon V \to f(V)$ is an isomorphism; (c) $\{x\}$ is an irreducible component of the fibre $X_{f(x)}$.
2. $\operatorname{Exc}(f) \neq X$. Every closed point of $\operatorname{Exc}(f)$ lies on a curve $C \subseteq X$ such that $f(C)$ is a point.
3. $f(\operatorname{Exc}(f)) = Y \setminus U$, and it has codimension at least 2 in $Y$. The map $f_*$ is a bijection from the non-exceptional prime divisors of $X$ to the prime divisors of $Y$. Its inverse is the *strict transform* $f^{-1}_* Q$, the closure of $f^{-1}(Q \cap U)$.
4. A prime divisor $P$ of $X$ is $f$-exceptional if and only if $P \subseteq \operatorname{Exc}(f)$. There are finitely many exceptional prime divisors, and they are the irreducible components of $\operatorname{Exc}(f)$ of dimension $n - 1$.

Lean: not yet in Lean.

So a birational contraction onto a normal variety is an isomorphism off a set of codimension at least 2 in the target, and it is either small, or it has some exceptional divisors. Section 2 shows that for a $\mathbb{Q}$-factorial target it is never small, unless it is an isomorphism.

### Proof in words

The first two parts of the proposition are P4 Chapter 6 itself: Zariski's main theorem gives $f_* \mathcal{O}_X = \mathcal{O}_Y$ for a birational $f$ onto a normal variety, and the connectedness theorem gives connected fibres. For the criterion with function fields, an element of $K(X)$ algebraic over $K(Y)$ becomes integral after multiplication by a function on $Y$, so it is regular on the normal variety $X$, and $f_* \mathcal{O}_X = \mathcal{O}_Y$ puts it in $K(Y)$. The Stein factorization of P4 is $Y' = \operatorname{\mathbf{Spec}}_Y f_* \mathcal{O}_X$, and its rings of sections are rings of functions on open subsets of the normal variety $X$, so $Y'$ is normal.

For rigidity, the map $h$ is forced on points, and it is continuous because $f$ is closed. On functions, $h^\#$ is the composite of $g^\#$ with the inverse of the isomorphism $\mathcal{O}_Y \to f_* \mathcal{O}_X$. The only check is that $h^\#$ is local, and this holds because the fibres are nonempty.

For the exceptional locus, a point $x$ that is isolated in its fibre lies in a connected fibre, so the fibre is $\{x\}$, and Zariski's main theorem says that $f$ is an isomorphism near $x$. The codimension bound comes from the dimension of fibres: over a component $W$ of $Y \setminus U$ the generic fibre has positive dimension, so $f^{-1}(W)$, which lies in the proper closed subset $\operatorname{Exc}(f)$, has dimension at least $\dim W + 1$.

### Examples

**Example 1.5.7 (a product).** Let $Y$ be a variety and $f \colon X = \mathbb{P}^m \times Y \to Y$ the projection. For an affine open $V = \operatorname{Spec} A$ of $Y$, Theorem P4.2.1 gives $H^0(\mathbb{P}^m_A, \mathcal{O}) = A$, so $f_* \mathcal{O}_X = \mathcal{O}_Y$ and $f$ is a contraction. Its fibres are the projective spaces $\mathbb{P}^m \times \{y\}$, connected as Proposition 1.5.2 says. For $Y = \mathbb{P}^1$ and $m = 1$ both projections of $\mathbb{P}^1 \times \mathbb{P}^1$ are contractions, and the fibres of each one are mapped isomorphically by the other, so neither factors through the other: Lemma 1.5.4 does not apply.

**Example 1.5.8 (the blow-up of a point of $\mathbb{A}^n$).** Let $n \geq 2$ and $\pi \colon X = \operatorname{Bl}_0 \mathbb{A}^n \to \mathbb{A}^n$. By Theorem P3.11.4, $X$ is covered by $n$ charts isomorphic to $\mathbb{A}^n$, with $E = \{0\} \times \mathbb{P}^{n-1}$, and by Theorem P3.11.3 $\pi$ is projective, birational, and an isomorphism over $\mathbb{A}^n \setminus \{0\}$. Since $\mathbb{A}^n$ is normal, $\pi$ is a contraction by part 2 of Proposition 1.5.2. Here $U = \mathbb{A}^n \setminus \{0\}$ and $\operatorname{Exc}(\pi) = E$, a prime divisor with $\pi(E) = \{0\}$ of dimension $0 < n - 1$. So $E$ is the only exceptional divisor, $\pi$ is divisorial, $\pi_* E = 0$, and $\pi(\operatorname{Exc}(\pi))$ has codimension $n \geq 2$. For $n = 2$ this is Example P4.6.11.

**Example 1.5.9 (a finite morphism and a Stein factorization).** The morphism $\sigma \colon \mathbb{P}^1 \to \mathbb{P}^1$, $[a : b] \mapsto [a^2 : b^2]$, is finite of degree 2. It is surjective with finite fibres, but it is not a contraction: $\sigma_* \mathcal{O}_{\mathbb{P}^1}$ has rank 2, and the function field extension $k(t) \supseteq k(t^2)$ is algebraic of degree 2, as part 4 of Proposition 1.5.2 predicts. The fibre over $[1 : 1]$ is the two points $[1 : \pm 1]$, not connected. Let $f = \sigma \circ \operatorname{pr}_1 \colon \mathbb{P}^1 \times \mathbb{P}^1 \to \mathbb{P}^1$. By Example 1.5.7, $f_* \mathcal{O} = \sigma_* \mathcal{O}_{\mathbb{P}^1}$, so the Stein factorization of Theorem 1.5.3 is $\mathbb{P}^1 \times \mathbb{P}^1 \xrightarrow{\operatorname{pr}_1} \mathbb{P}^1 \xrightarrow{\sigma} \mathbb{P}^1$, and the fibre of $f$ over $[1 : 1]$ is the disjoint union of the two lines $\{[1 : \pm 1]\} \times \mathbb{P}^1$, as in Example P4.6.18.

**Example 1.5.10 (normality of the target is needed).** Let $\nu \colon \mathbb{A}^1 \to Y$ be the normalization of the nodal cubic of Example P4.6.12. It is projective and birational, and every fibre is finite, so with the set $U$ of Definition 1.5.5 one would get $U = Y$ and $\operatorname{Exc}(\nu) = \emptyset$. But $\nu$ is not an isomorphism, the fibre over the node is two points, and $\nu_* \mathcal{O}_{\mathbb{A}^1} \neq \mathcal{O}_Y$. Definition 1.5.5 asks for a normal target for this reason: without it, Corollary P4.6.10 fails, and the exceptional locus does not see where $f$ fails to be an isomorphism.

**Example 1.5.11 (two contractions from the blow-up of a point of $\mathbb{P}^n$).** Let $n \geq 2$, $p = [1 : 0 : \dots : 0] \in \mathbb{P}^n$, and
$$Y = \{ ([x_0 : \dots : x_n], [u_1 : \dots : u_n]) : x_i u_j = x_j u_i \text{ for } 1 \leq i < j \leq n \} \subseteq \mathbb{P}^n \times \mathbb{P}^{n-1},$$
with projections $\pi \colon Y \to \mathbb{P}^n$ and $q \colon Y \to \mathbb{P}^{n-1}$. On $x_0 \neq 0$ the equations are those of part 2 of Theorem P3.11.4 for the origin of $\mathbb{A}^n$. Where $x_0 = 0$ some $x_i \neq 0$ with $i \geq 1$, and the equations say $[u] = [x_1 : \dots : x_n]$, so $\pi$ is an isomorphism there. So $Y = \operatorname{Bl}_p \mathbb{P}^n$, and $\pi$ is a divisorial contraction with $\operatorname{Exc}(\pi) = E = \{p\} \times \mathbb{P}^{n-1}$, as in Example 1.5.8. Over the open set $u_1 \neq 0$ of $\mathbb{P}^{n-1}$, with $a_j = u_j/u_1$, the equations say $x_j = a_j x_1$ for $j \geq 2$, so $q^{-1}(\{u_1 \neq 0\}) \cong \mathbb{P}^1 \times \mathbb{A}^{n-1}$, with coordinates $[x_0 : x_1]$ and $(a_2, \dots, a_n)$. The same holds on each $u_i \neq 0$, so $q$ is a $\mathbb{P}^1$-bundle, and $q$ is a contraction by Example 1.5.7 applied on each of these open sets. The fibre of $q$ over $[u]$ is the strict transform of the line through $p$ with direction $[u]$, and $q|_E \colon E \to \mathbb{P}^{n-1}$ is an isomorphism. So $q$ is not constant on the fibre $E$ of $\pi$, and $\pi$ is not constant on the fibres of $q$. By Lemma 1.5.4 applied with the roles exchanged, neither morphism can be the composite of the other with a morphism: the projection from $p$ is not defined at $p$, and the blow-up is the graph that resolves it.

### Proof

*Proposition 1.5.2.* (1) Theorem P4.6.7 gives that every fibre is nonempty and connected, so $f$ is surjective. If $X$ is normal and $V \subseteq Y$ is an affine open set, then $\mathcal{O}_Y(V) = \mathcal{O}_X(f^{-1}(V))$, and $f^{-1}(V)$ is nonempty. A rational function on the normal integral scheme $f^{-1}(V)$ that is integral over $\mathcal{O}_X(f^{-1}(V))$ is integral over every local ring $\mathcal{O}_{X, x}$, hence lies in each of them, hence is regular on $f^{-1}(V)$. So $\mathcal{O}_Y(V)$ is integrally closed in $K(X)$, and in particular in its own fraction field $K(Y)$, and $Y$ is normal.

(2) This is Theorem P4.6.8.

(3) The composite of projective morphisms to a quasi-compact scheme is projective (Har77, Exercise II.4.9), and $(g \circ f)_* \mathcal{O}_X = g_* f_* \mathcal{O}_X = g_* \mathcal{O}_Y = \mathcal{O}_Z$.

(4) If $K(Y)$ is algebraically closed in $K(X)$, then $f$ is a contraction by Corollary P4.6.16. Conversely let $f$ be a contraction and $a \in K(X)$ algebraic over $K(Y)$. Let $V = \operatorname{Spec} A$ be a nonempty affine open subset of $Y$, so that $K(Y) = \operatorname{Frac} A$. Then $a^m + c_1 a^{m-1} + \dots + c_m = 0$ for some $c_i \in K(Y)$. Choose $0 \neq d \in A$ with $d c_i \in A$ for all $i$. Then $b = da$ satisfies
$$b^m + (d c_1) b^{m-1} + (d^2 c_2) b^{m-2} + \dots + d^m c_m = 0,$$
a monic equation with coefficients in $A \subseteq \mathcal{O}_X(f^{-1}(V))$. As in part 1, $b$ is regular on the normal variety $f^{-1}(V)$, so $b \in \mathcal{O}_X(f^{-1}(V)) = A$, and $a = b/d \in K(Y)$. $\square$

*Theorem 1.5.3.* By Theorem P4.6.15, $f = g \circ f'$ with $Y' = \operatorname{\mathbf{Spec}}_Y f_* \mathcal{O}_X$, $g$ finite, $f'$ a contraction, and the statement on connected components. The scheme $Y'$ is of finite type and separated over $k$, because $g$ is finite and $Y$ is a variety. For an affine open $V \subseteq Y$, $g^{-1}(V) = \operatorname{Spec} \mathcal{O}_X(f^{-1}(V))$, and this ring is $0$ or a normal domain by the argument of part 1 of Proposition 1.5.2. The morphism $f'$ is surjective by part 1 of Proposition 1.5.2, so $Y'$ is the image of the irreducible space $X$, and it is irreducible. So $Y'$ is a normal variety. If $f$ is a contraction, then $f_* \mathcal{O}_X = \mathcal{O}_Y$ and $g$ is the identity of $Y$. Conversely, if $g$ is an isomorphism, then $f$ is the composite of a contraction and an isomorphism, hence a contraction. $\square$

*Lemma 1.5.4.* By part 1 of Proposition 1.5.2, $f$ is surjective, so each $X_y$ is nonempty. Define $h(y)$ as the point $g(X_y)$. Then $g = h \circ f$ as maps of sets. For a closed set $F \subseteq Z$, a point $y$ lies in $h^{-1}(F)$ if and only if $X_y$ meets $g^{-1}(F)$, because $g$ is constant on $X_y$. So $h^{-1}(F) = f(g^{-1}(F))$, which is closed because $f$ is proper. So $h$ is continuous. For an open $V \subseteq Z$, $f^{-1}(h^{-1}(V)) = g^{-1}(V)$. Let $h^\#_V$ be the composite
$$\mathcal{O}_Z(V) \xrightarrow{g^\#} \mathcal{O}_X(g^{-1}(V)) = (f_* \mathcal{O}_X)(h^{-1}(V)) \xrightarrow{(f^\#)^{-1}} \mathcal{O}_Y(h^{-1}(V)),$$
where $f^\# \colon \mathcal{O}_Y \to f_* \mathcal{O}_X$ is an isomorphism because $f$ is a contraction. These maps are compatible with restriction, so $(h, h^\#)$ is a morphism of ringed spaces with $f^\# \circ h^\# = g^\#$. It is a morphism of locally ringed spaces: let $y \in Y$, $z = h(y)$, and $s$ a section of $\mathcal{O}_Z$ near $z$ with $s(z) = 0$. If $h^\#(s)$ were a unit in $\mathcal{O}_{Y, y}$, it would be invertible on an open $W \ni y$, so $g^\#(s) = f^\# h^\#(s)$ would be invertible on $f^{-1}(W)$. Take $x \in X_y$. Then $g(x) = z$, and $g^\#(s)$ is a unit at $x$, which contradicts $s(z) = 0$ because $g$ is a morphism of locally ringed spaces. So $h$ is a morphism of schemes. If $h'$ is a second one, $h' = h$ on points because $f$ is surjective, and $f^\# \circ h'^\# = g^\# = f^\# \circ h^\#$ with $f^\#$ an isomorphism, so $h'^\# = h^\#$. $\square$

*Proposition 1.5.6.* (1) If $x \notin \operatorname{Exc}(f)$, then $V = f^{-1}(U)$ works in (b) by Corollary P4.6.10. If (b) holds, then $f|_V$ is injective, so $V \cap X_{f(x)} = \{x\}$, and $\{x\}$ is open in $X_{f(x)}$. It is also closed in $X_{f(x)}$, because the closure of $x$ in $V \cap X_{f(x)}$ is $\{x\}$ and its closure in the fibre meets the open set $V \cap X_{f(x)}$ only in $x$; a point of the closure outside $V$ would specialize from $x$, and the specializations of $x$ in the fibre lie over $f(x)$ and are mapped by $f|_V$ to $f(x)$, so they lie in $V$ only if they equal $x$. So $\{x\}$ is a connected component of $X_{f(x)}$, in particular an irreducible component. If (c) holds, $\{x\}$ is closed in the fibre, and it is open, because it is the complement of the union of the other irreducible components: no other component contains $x$, since $\{x\}$ is a maximal irreducible closed subset. By Theorem P4.6.8 the fibre is connected, so it is $\{x\}$, it is finite, and $f(x) \in U$.

(2) The morphism $f$ is birational, so it is an isomorphism over a dense open subset of $Y$, which lies in $U$. So $U \neq \emptyset$ and $\operatorname{Exc}(f) \neq X$. Let $x \in \operatorname{Exc}(f)$ be closed. Then $y = f(x)$ is a closed point, because $f$ is proper, and $\kappa(y) = k$. By Corollary P4.6.10 the fibre $X_y$ has positive dimension at $x$, so an irreducible component $G$ of $(X_y)_{\mathrm{red}}$ through $x$ has dimension $d \geq 1$. It is a closed subvariety of a projective space $\mathbb{P}^N$, since $f$ is projective and $\kappa(y) = k$. If $d \geq 2$, a hyperplane through $x$ that does not contain $G$ meets $G$ in a closed set whose components through $x$ have dimension $d - 1$, by part 2 of Proposition P3.7.5 applied on an affine neighbourhood of $x$ in $G$. Repeating $d - 1$ times gives an irreducible curve $C \ni x$ in $G$, and $f(C) = \{y\}$.

(3) The morphism $f$ is surjective by part 1 of Proposition 1.5.2, so $f(\operatorname{Exc}(f)) = Y \setminus U$. Let $W$ be an irreducible component of $Y \setminus U$, with generic point $\eta$. The closed set $f^{-1}(W)$ has finitely many irreducible components, and the images of those are closed and cover $W$, so some component $G$ satisfies $f(G) = W$. The fibre $X_\eta$ is the union of the generic fibres $G_\eta$ over the components $G$ with $f(G) = W$, and it is not finite because $\eta \notin U$. So some such $G$ has $\dim G_\eta \geq 1$, and Theorem P3.7.6 gives $\dim G = \dim W + \dim G_\eta \geq \dim W + 1$. But $G \subseteq \operatorname{Exc}(f)$, a proper closed subset of $X$ by part 2, so $\dim G \leq n - 1$ and $\dim W \leq n - 2$. For the bijection, let $P$ be a non-exceptional prime divisor. By part 4 below, $P \not\subseteq \operatorname{Exc}(f)$, so $P \cap f^{-1}(U)$ is a dense open subset of $P$ and is mapped isomorphically onto the closed subset $f(P) \cap U$ of $U$. So $f(P)$, which is closed because $f$ is proper, is a prime divisor, and $P$ is the closure of $f^{-1}(f(P) \cap U)$. Conversely, a prime divisor $Q$ of $Y$ is not contained in $Y \setminus U$, which has codimension at least 2, so $f^{-1}(Q \cap U) \cong Q \cap U$ is irreducible of dimension $n - 1$, and its closure $f^{-1}_* Q$ is a prime divisor, not contained in $\operatorname{Exc}(f)$, with $f(f^{-1}_* Q) = Q$.

(4) If $P \subseteq \operatorname{Exc}(f)$, then $f(P) \subseteq Y \setminus U$ has dimension at most $n - 2$ by part 3, so $P$ is exceptional. Conversely let $\dim f(P) < n - 1$, and let $\eta'$ be the generic point of $f(P)$. By Theorem P3.7.6 the generic fibre of $P \to f(P)$ has dimension $n - 1 - \dim f(P) \geq 1$, so $X_{\eta'}$ is not finite and $\eta' \notin U$. Then $f(P) = \overline{\{\eta'\}} \subseteq Y \setminus U$, and $P \subseteq \operatorname{Exc}(f)$. Every exceptional prime divisor is an irreducible closed subset of dimension $n - 1$ of $\operatorname{Exc}(f)$, which has dimension at most $n - 1$ by part 2. So it is an irreducible component of $\operatorname{Exc}(f)$, and there are finitely many. $\square$

### Exercises

1. (A) Let $\pi \colon X \to \mathbb{A}^3$ be the blow-up of the line $L = \{x = y = 0\}$. Using Theorem P3.11.4, describe $U$, $\operatorname{Exc}(\pi)$ and the fibres of $\pi$. Show that $\pi$ is divisorial and that $\pi(\operatorname{Exc}(\pi)) = L$ has codimension 2, as part 3 of Proposition 1.5.6 predicts.
2. (A) Let $f \colon \mathbb{P}^1 \to \mathbb{P}^1$, $[a : b] \mapsto [a^3 : b^3]$. Show that $f$ is not a contraction, find an element of $K(X)$ algebraic over $K(Y)$ but not in $K(Y)$, and describe the Stein factorization of $f \circ \operatorname{pr}_1 \colon \mathbb{P}^1 \times \mathbb{P}^2 \to \mathbb{P}^1$.
3. (B) Let $f \colon X \to Y$ be a contraction of normal varieties with $\dim X = \dim Y$. Show that $f$ is birational. (Use part 4 of Proposition 1.5.2 and Theorem P3.7.6.)
4. (B) Let $f \colon X \to Y$ be a contraction and $g \colon X \to Z$ a finite morphism. Show that $g$ is constant on every fibre of $f$, that $g = h \circ f$, and that $f$ is an isomorphism. (Use Lemma 1.5.4, Corollary P4.6.17 and the definition of a contraction.)
5. (B) Let $f \colon X \to Y$ and $g \colon Y \to Z$ be projective birational morphisms of varieties with $Y$ and $Z$ normal. Show that $\operatorname{Exc}(g \circ f) = \operatorname{Exc}(f) \cup f^{-1}(\operatorname{Exc}(g))$. Check it for the two blow-ups of Example P5.8.6 with $n = 1$.
6. (B) Let $f \colon X \to Y$ be a projective surjective morphism of normal varieties, and let $L$ be the algebraic closure of $K(Y)$ in $K(X)$. Show that $L$ is a finite extension of $K(Y)$ and that the variety $Y'$ of Theorem 1.5.3 is the normalization of $Y$ in $L$: its function field is $L$, and $Y' \to Y$ is finite with $Y'$ normal.

### Lean

The project library has `MinimalModel.IsContraction`, a projective morphism $f$ to a normal variety such that $f^\#$ is an isomorphism on every open set, which is Definition 1.5.1, and `MinimalModel.IsExtremalContraction`, used in the statement of the contraction theorem. Proposition 1.5.2, the Stein factorization and the rigidity lemma are not in Lean. Mathlib has the relative spectrum and the normalization of a quasi-compact and quasi-separated morphism, but not Zariski's main theorem in the form of Corollary P4.6.10.

### Notes and history

Zariski's main theorem is from 1943, the connectedness theorem from 1951, and Stein's factorization is from complex analysis (Stein, 1956), with Grothendieck's algebraic form in EGA III. Hartshorne, Section III.11, is the source of P4 Chapter 6 (Har77). The rigidity lemma is in Kollár-Mori, Chapter 1 (KM98), in a slightly different form, and Debarre, Chapter 1, gives the same statements (Deb01). Kollár and Mori define the exceptional set of a birational morphism as the set of points where it is not a local isomorphism, and part 1 of Proposition 1.5.6 shows that this agrees with Definition 1.5.5 when the target is normal. The literature state is theorem.
