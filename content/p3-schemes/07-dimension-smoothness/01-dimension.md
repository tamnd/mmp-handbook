---
title: The dimension of schemes and of varieties
nodes: []
sources: [Vak25, Har77, GW20, Stacks]
reads_with: [Vak25:ch11, Har77:I.1, GW20:ch5]
requires: [P1.4, P1.5, P1.13, P3.1, P3.2, P3.3]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The dimension of schemes and of varieties

### Statement

**Definition P3.7.1 (dimension and codimension).** Let $X$ be a topological space. The *dimension* $\dim X$ is the supremum of the lengths $n$ of chains $Z_0 \subsetneq Z_1 \subsetneq \dots \subsetneq Z_n$ of irreducible closed subsets of $X$. For an irreducible closed subset $Z \subseteq X$, the *codimension* $\operatorname{codim}(Z, X)$ is the supremum of the lengths of such chains with $Z_0 = Z$. The dimension of a scheme is the dimension of its space. A scheme has *pure dimension* $d$ if all its irreducible components have dimension $d$. A *curve* over a field is a variety of dimension $1$, and a *surface* is a variety of dimension $2$.

Lean: Mathlib `topologicalKrullDim` for spaces, `ringKrullDim` for rings, and `Order.coheight` for the codimension of a point (definitions).

**Proposition P3.7.2 (first properties).** Let $X$ be a scheme.

1. If $X = \operatorname{Spec} A$, then $\dim X = \dim A$, and for a prime $\mathfrak{p}$, $\operatorname{codim}(V(\mathfrak{p}), X) = \operatorname{ht} \mathfrak{p}$.
2. If $X = \bigcup_i U_i$ is an open cover, then $\dim X = \sup_i \dim U_i$. For an open $U$ and an irreducible closed $Z$ with $Z \cap U \neq \emptyset$, $\operatorname{codim}(Z \cap U, U) = \operatorname{codim}(Z, X)$.
3. $\dim X$ is the supremum of the dimensions of the irreducible components of $X$, and $\dim Z \leq \dim X$ for every closed $Z \subseteq X$.
4. For $x \in X$, $\dim \mathcal{O}_{X, x} = \operatorname{codim}(\overline{\{x\}}, X)$.

Lean: Mathlib `AlgebraicGeometry.ringKrullDim_stalk_eq_coheight` is part 4 (proved in Mathlib). The other parts are not in Lean as stated.

**Proposition P3.7.3 (closed points over a field).** Let $X$ be a scheme locally of finite type over a field $k$.

1. A point $x \in X$ is closed if and only if $\kappa(x)$ is a finite extension of $k$.
2. A point that is closed in some nonempty open subset of $X$ is closed in $X$.
3. Every nonempty locally closed subset of $X$ contains a closed point of $X$. In particular the closed points are dense in every closed subset.

Lean: Mathlib `AlgebraicGeometry.isClosed_singleton_iff_locallyOfFiniteType` and `AlgebraicGeometry.Scheme.Hom.closedPoints_subset_preimage_closedPoints`, stated for `JacobsonSpace` (proved in Mathlib). The statement in this form is not in Lean as stated.

**Theorem P3.7.4 (dimension of varieties).** Let $X$ be an integral scheme of finite type over a field $k$, with function field $K(X)$.

1. $\dim X = \operatorname{trdeg}_k K(X)$. In particular $\dim X$ is finite.
2. $\dim U = \dim X$ for every nonempty open $U \subseteq X$.
3. $\dim \mathcal{O}_{X, x} = \dim X$ for every closed point $x$.
4. For every irreducible closed $Z \subseteq X$, $\dim Z + \operatorname{codim}(Z, X) = \dim X$.
5. Every chain of irreducible closed subsets of $X$ that cannot be refined has length $\dim X$.

Lean: not in Lean as stated.

**Proposition P3.7.5 (hypersurfaces and intersections).** Let $k$ be a field.

1. Let $X = \operatorname{Spec} A$ be an affine integral scheme of finite type over $k$ and $f \in A$ neither $0$ nor a unit. Then every irreducible component of $V(f)$ has dimension $\dim X - 1$.
2. In the same situation, for $f_1, \dots, f_r \in A$, every irreducible component of $V(f_1, \dots, f_r)$ has dimension at least $\dim X - r$.
3. $\dim \mathbb{P}^n_k = n$, and for a homogeneous polynomial $F$ of positive degree that is not zero, every irreducible component of $V_+(F)$ has dimension $n - 1$.
4. If $F_1, \dots, F_r$ are homogeneous of positive degree and $r \leq n$, then $V_+(F_1, \dots, F_r) \subseteq \mathbb{P}^n_k$ is nonempty, and each of its irreducible components has dimension at least $n - r$.

Lean: not in Lean as stated.

**Theorem P3.7.6 (dimension of fibres).** Let $f \colon X \to Y$ be a dominant morphism of integral schemes of finite type over a field $k$, and let $\eta$ be the generic point of $Y$.

1. The generic fibre $X_\eta$ is a nonempty integral scheme of finite type over $K(Y)$, with function field $K(X)$, and $\dim X_\eta = \dim X - \dim Y$.
2. For every closed point $y \in Y$, every irreducible component of the fibre $X_y$ has dimension at least $\dim X - \dim Y$.

Lean: not in Lean as stated. Mathlib `Ideal.height_le_height_add_of_liesOver` is the algebraic inequality behind part 2 (proved in Mathlib).

### Proof in words

The irreducible closed subsets of $\operatorname{Spec} A$ are the sets $V(\mathfrak{p})$, so the dimension of an affine scheme is the Krull dimension of its ring. A chain of irreducible closed subsets is seen in every open set that meets its smallest member, which reduces all statements to affine schemes. For an integral scheme of finite type over a field, the algebra of P1 Ch. 4 and Ch. 5 does the rest: the dimension of an affine domain is a transcendence degree, every maximal chain of primes has the same length, and Krull's principal ideal theorem cuts the dimension by one. The theorem on fibres is the inequality $\dim B \leq \dim A + \dim B/\mathfrak{m}B$ for local rings, read at a closed point of the fibre.

### Examples

**Example P3.7.7 (first dimensions).** $\dim \mathbb{A}^n_k = n$ by Theorem P3.7.4, since $\operatorname{trdeg}_k k(x_1, \dots, x_n) = n$, and $\dim \mathbb{P}^n_k = n$, as $\mathbb{P}^n_k$ contains $\mathbb{A}^n_k$ as a dense open set. $\dim \operatorname{Spec} \mathbb{Z} = 1$, with the chains $(0) \subsetneq (p)$. A field has dimension $0$. For a discrete valuation ring $R$, $\operatorname{Spec} R$ has two points, the closed point $\mathfrak{m}$ and the generic point $(0)$, and dimension $1$. The open set $\{(0)\}$ has dimension $0$. So part 2 of Theorem P3.7.4 fails for schemes that are not of finite type over a field.

**Example P3.7.8 (a plane and a line).** Let $X = V(xz, yz) \subseteq \mathbb{A}^3_k$. Since $(xz, yz) = (x, y) \cap (z)$, $X$ is the union of the plane $z = 0$ and the line $x = y = 0$, which meet at the origin. Then $\dim X = 2$, but $X$ does not have pure dimension. At the closed point $p = (0, 0, 1)$ on the line, $\mathcal{O}_{X, p}$ is the local ring of the line, of dimension $1$, and the line has codimension $0$ in $X$. So parts 3 and 4 of Theorem P3.7.4 fail for schemes that are not irreducible.

**Example P3.7.9 (a fibre that jumps).** Let $f \colon \mathbb{A}^2_k \to \mathbb{A}^2_k$ be $(x, y) \mapsto (x, xy)$, given by $k[u, v] \to k[x, y]$, $u \mapsto x$, $v \mapsto xy$. It is dominant, and $\dim X - \dim Y = 0$. Over a point $(a, b)$ with $a \neq 0$ the fibre is the one point $(a, b/a)$. Over $(0, 0)$ the fibre is $\operatorname{Spec} k[x, y]/(x, xy) = \operatorname{Spec} k[y]$, the line $x = 0$, of dimension $1$. Over $(0, b)$ with $b \neq 0$ the fibre is $\operatorname{Spec} k[x, y]/(x, xy - b) = \emptyset$. So the inequality in part 2 of Theorem P3.7.6 can be strict, and the image of $f$ is not closed. This map is a chart of the blow-up of the plane at the origin, the subject of Chapter 11.

**Example P3.7.10 (two lines in space).** In $\mathbb{P}^3_k$ the lines $L_1 = V_+(x_0, x_1)$ and $L_2 = V_+(x_2, x_3)$ are disjoint, since $(x_0, x_1, x_2, x_3)$ contains $S_+$. Here $L_1 \cap L_2$ is cut out by $4 > 3$ equations, so part 4 of Proposition P3.7.5 does not apply. In $\mathbb{P}^2_k$, on the other hand, two curves $V_+(F)$ and $V_+(G)$ always meet, as $2 \leq 2$. The count of the points of intersection with multiplicities is Bézout's theorem, which this volume does not prove.

**Example P3.7.11 (the quadric cone and its lines).** Let $X = V(xy - z^2) \subseteq \mathbb{A}^3_k$. Part 1 of Proposition P3.7.5 gives $\dim X = 2$. The line $L = V(x, z)$ lies on $X$, and it is not cut out by one equation in $X$: the ideal $(x, z)$ of $A = k[x, y, z]/(xy - z^2)$ is not principal, since its image in $\mathfrak{m}/\mathfrak{m}^2$ for $\mathfrak{m} = (x, y, z)$ has dimension $2$. But $V(x) = L$ as a set, as $x = 0$ forces $z^2 = 0$. So $L$ has codimension $1$ and is cut out set-theoretically by one equation. Chapter 8 measures this with the class group: $[L]$ has order $2$ in $\operatorname{Cl}(X)$.

### Proof

*Proof of Proposition P3.7.2.* (1) The irreducible closed subsets of $\operatorname{Spec} A$ are the sets $V(\mathfrak{p})$ for primes $\mathfrak{p}$, and $V(\mathfrak{p}) \subseteq V(\mathfrak{q})$ if and only if $\mathfrak{q} \subseteq \mathfrak{p}$ (Theorem P3.2.20 and its proof). So chains of irreducible closed subsets are chains of primes in reverse order, and chains that start at $V(\mathfrak{p})$ are chains of primes that end at $\mathfrak{p}$.

(2) Let $U \subseteq X$ be open. For an irreducible closed $Z \subseteq X$ with $Z \cap U \neq \emptyset$, the set $Z \cap U$ is irreducible, closed in $U$ and dense in $Z$. Conversely, for an irreducible closed $W \subseteq U$, the closure $\overline{W}$ in $X$ is irreducible and $\overline{W} \cap U = W$. These two maps are inverse bijections between the irreducible closed subsets of $X$ that meet $U$ and the irreducible closed subsets of $U$, and they preserve strict inclusion. If $Z_0 \subsetneq \dots \subsetneq Z_n$ is a chain in $X$ and $U$ meets $Z_0$, then $U$ meets every $Z_i$, and the chain gives a chain of the same length in $U$. If $U_i$ is a cover, some $U_i$ meets $Z_0$, so $\dim X \leq \sup \dim U_i$; the other inequality is the converse map. The same bijection gives the statement on codimension.

(3) Every irreducible closed subset lies in an irreducible component (Zorn's lemma, as the closure of a union of a chain of irreducible sets is irreducible), so every chain lies in a component. A chain in a closed $Z$ is a chain in $X$.

(4) Let $U = \operatorname{Spec} A$ be an affine open containing $x = \mathfrak{p}$. Then $\mathcal{O}_{X, x} = A_\mathfrak{p}$ (Theorem P3.1.11), and $\dim A_\mathfrak{p} = \operatorname{ht} \mathfrak{p}$ (Proposition P1.5.7). By part 1 this is $\operatorname{codim}(V(\mathfrak{p}), U)$, and by part 2 it is $\operatorname{codim}(\overline{\{x\}}, X)$. $\square$

*Proof of Proposition P3.7.3.* (1) Let $x$ be closed, and $U = \operatorname{Spec} A \ni x$ an affine open with $A$ a finitely generated $k$-algebra. Then $x$ is closed in $U$, so it is a maximal ideal $\mathfrak{m}$, and $\kappa(x) = A/\mathfrak{m}$ is a finitely generated $k$-algebra that is a field. It is finite over $k$ by Zariski's lemma (Corollary P1.4.28). Conversely, let $\kappa(x)$ be finite over $k$, and let $V = \operatorname{Spec} B$ be any affine open with $B$ finitely generated and $x = \mathfrak{q} \in V$. The domain $B/\mathfrak{q}$ embeds in $\kappa(x)$, so it is a $k$-vector space of finite dimension. A domain of finite dimension over a field is a field, since multiplication by a nonzero element is injective, hence surjective. So $\mathfrak{q}$ is maximal and $\{x\}$ is closed in $V$. As this holds for all affine opens of such a cover, and $\{x\} \cap V = \emptyset$ is closed in the affine opens that do not contain $x$, the set $\{x\}$ is closed in $X$.

(2) If $x$ is closed in an open $U$, then $\kappa(x)$ is finite over $k$ by part 1 applied to $U$, which is locally of finite type over $k$. By part 1 applied to $X$, $x$ is closed in $X$.

(3) Let $W = U \cap F$ be nonempty with $U$ open and $F$ closed. Choose an affine open $V = \operatorname{Spec} A$ with $A$ finitely generated and $V \cap W \neq \emptyset$. Then $F \cap V = V(I)$ for an ideal $I$, and $V \cap W$ is a nonempty open subset of $\operatorname{Spec} A/I$. It contains a nonempty basic open set $D(\bar g) = \operatorname{Spec} (A/I)_{\bar g}$. The ring $(A/I)_{\bar g}$ is a nonzero finitely generated $k$-algebra, so it has a maximal ideal. This is a closed point of $D(\bar g)$, and it is closed in $X$ by part 2. $\square$

*Proof of Theorem P3.7.4.* (1) Let $U = \operatorname{Spec} A$ be a nonempty affine open. Then $A$ is a finitely generated $k$-algebra and a domain with $\operatorname{Frac}(A) = K(X)$ (Proposition P3.2.24), so $\dim U = \dim A = \operatorname{trdeg}_k K(X)$ by Theorem P1.4.31. By part 2 of Proposition P3.7.2, applied to a cover by such $U$, $\dim X = \operatorname{trdeg}_k K(X)$.

(2) A nonempty open $U$ is again integral of finite type over $k$ with the same function field, so part 1 gives $\dim U = \dim X$.

(3) Let $x$ be closed, and $U = \operatorname{Spec} A \ni x$ affine. Then $x$ is a maximal ideal $\mathfrak{m}$ of $A$, and $\dim \mathcal{O}_{X, x} = \dim A_\mathfrak{m} = \dim A = \dim X$ by part 2 of Corollary P1.5.42 and part 2.

(4) Let $U = \operatorname{Spec} A$ be an affine open that meets $Z$, and $Z \cap U = V(\mathfrak{p})$. By Proposition P3.7.2, $\operatorname{codim}(Z, X) = \operatorname{ht} \mathfrak{p}$. The closed subscheme $Z$ with its reduced structure (Proposition P3.3.12) is integral of finite type over $k$, so $\dim Z = \dim (Z \cap U) = \dim A/\mathfrak{p}$ by part 2. Part 1 of Corollary P1.5.42 gives $\operatorname{ht} \mathfrak{p} + \dim A/\mathfrak{p} = \dim A = \dim X$.

(5) Let $Z_0 \subsetneq \dots \subsetneq Z_n$ be a chain that cannot be refined. Then $Z_n = X$, and $Z_0$ contains no smaller irreducible closed set. By part 3 of Proposition P3.7.3 it contains a closed point $x$, so $Z_0 = \{x\}$. Let $U = \operatorname{Spec} A$ be an affine open containing $x$. By the bijection in the proof of part 2 of Proposition P3.7.2, the sets $Z_i \cap U$ form a chain of primes $\mathfrak{m} = \mathfrak{p}_0 \supsetneq \dots \supsetneq \mathfrak{p}_n = 0$ that cannot be refined. By Theorem P1.5.41, $n = \dim A = \dim X$. $\square$

*Proof of Proposition P3.7.5.* (1) Let $\mathfrak{p}$ be a minimal prime over $(f)$; the irreducible components of $V(f)$ are the sets $V(\mathfrak{p})$. Then $\operatorname{ht} \mathfrak{p} \leq 1$ by Krull's principal ideal theorem (Theorem P1.5.17), and $\operatorname{ht} \mathfrak{p} \geq 1$, as $\mathfrak{p} \neq 0$ in the domain $A$. So $\dim V(\mathfrak{p}) = \dim A/\mathfrak{p} = \dim A - 1$ by part 1 of Corollary P1.5.42.

(2) The same argument with Krull's height theorem (Theorem P1.5.18): a minimal prime $\mathfrak{p}$ over $(f_1, \dots, f_r)$ has $\operatorname{ht} \mathfrak{p} \leq r$, so $\dim A/\mathfrak{p} \geq \dim A - r$.

(3) The first statement is Example P3.7.7. Let $Z$ be an irreducible component of $V_+(F)$, and choose $i$ with $Z \cap D_+(x_i) \neq \emptyset$. On $D_+(x_i) = \operatorname{Spec} k[x_0/x_i, \dots, x_n/x_i] \cong \mathbb{A}^n_k$, the set $V_+(F)$ is $V(f)$ with $f = F/x_i^{\deg F}$, and $f$ is not zero. It is not a unit, since $Z \cap D_+(x_i) \subseteq V(f)$ is nonempty. So $Z \cap D_+(x_i)$, a component of $V(f)$, has dimension $n - 1$ by part 1, and $\dim Z = n - 1$ by part 2 of Theorem P3.7.4.

(4) Let $S = k[x_0, \dots, x_n]$ and $I = (F_1, \dots, F_r) \subseteq S_+$. Let $\mathfrak{p}$ be a prime minimal over $I$ and contained in $S_+$; it exists, since $S_+$ is a prime containing $I$. By Krull's height theorem $\operatorname{ht} \mathfrak{p} \leq r$, so $\dim S/\mathfrak{p} = n + 1 - \operatorname{ht} \mathfrak{p} \geq n + 1 - r \geq 1$ by Corollary P1.5.42. In particular $\mathfrak{p} \neq S_+$, as $S/S_+ = k$ has dimension $0$. The prime $\mathfrak{p}$ is homogeneous, as a minimal prime over a homogeneous ideal (Proposition P1.13.3). So $\mathfrak{p}$ is a homogeneous prime that contains $I$ and does not contain $S_+$, that is, a point of $V_+(F_1, \dots, F_r)$. For the dimension of a component $Z$, choose $i$ with $Z \cap D_+(x_i) \neq \emptyset$, and apply part 2 on $D_+(x_i) \cong \mathbb{A}^n_k$ with the $r$ functions $F_j/x_i^{\deg F_j}$, and then part 2 of Theorem P3.7.4. $\square$

*Proof of Theorem P3.7.6.* (1) Let $V = \operatorname{Spec} B \subseteq Y$ and $U = \operatorname{Spec} A \subseteq f^{-1}(V)$ be nonempty affine opens. The map $\varphi \colon B \to A$ is injective. Indeed, $f$ maps the generic point of $X$ to a point whose closure is $\overline{f(X)} = Y$, so to $\eta$. As the generic point of $U$ is $(0)$, $\varphi^{-1}(0) = (0)$. So $B \setminus \{0\}$ maps to nonzero elements of $A$, and $U \times_Y \operatorname{Spec} K(Y) = \operatorname{Spec} A \otimes_B K(Y) = \operatorname{Spec} A_{B \setminus 0}$. This is a localization of the domain $A$, so it is a nonempty integral scheme with fraction field $\operatorname{Frac}(A) = K(X)$, of finite type over $K(Y) = \operatorname{Frac}(B)$. These affine schemes cover $X_\eta$ (Proposition P3.3.20) and are open in it with a common generic point, so $X_\eta$ is integral of finite type over $K(Y)$ with function field $K(X)$. By part 1 of Theorem P3.7.4,
$$\dim X_\eta = \operatorname{trdeg}_{K(Y)} K(X) = \operatorname{trdeg}_k K(X) - \operatorname{trdeg}_k K(Y) = \dim X - \dim Y.$$

(2) The fibre $X_y$ is of finite type over $\kappa(y)$, so it is Noetherian and has finitely many irreducible components. Let $Z$ be one of them. The set of points of $Z$ that lie on no other component is a nonempty open subset of $Z$, so it contains a point $x$ that is closed in $X_y$ (Proposition P3.7.3). As $y$ is closed, $X_y$ is closed in $X$, and $x$ is closed in $X$. Choose affine opens $\operatorname{Spec} B \ni y$ and $\operatorname{Spec} A \ni x$ over it, with $y = \mathfrak{n}$ and $x = \mathfrak{m}$. Then $X_y \cap \operatorname{Spec} A = \operatorname{Spec} A/\mathfrak{n}A$, so $\mathcal{O}_{X_y, x} = \mathcal{O}_{X, x}/\mathfrak{n} \mathcal{O}_{X, x}$, and $\mathcal{O}_{Y, y} \to \mathcal{O}_{X, x}$ is a local homomorphism of Noetherian local rings. Theorem P1.5.45 gives
$$\dim \mathcal{O}_{X, x} \leq \dim \mathcal{O}_{Y, y} + \dim \mathcal{O}_{X_y, x}.$$
By part 3 of Theorem P3.7.4, $\dim \mathcal{O}_{X, x} = \dim X$ and $\dim \mathcal{O}_{Y, y} = \dim Y$. The primes of $\mathcal{O}_{X_y, x}$ are the irreducible closed subsets of $X_y$ through $x$, up to the bijection of Proposition P3.7.2, and they all lie in $Z$. So $\dim \mathcal{O}_{X_y, x} = \dim \mathcal{O}_{Z, x}$, where $Z$ carries its reduced structure, and this is $\dim Z$ by part 3 of Theorem P3.7.4 over $\kappa(y)$. So $\dim Z \geq \dim X - \dim Y$. $\square$

### Exercises

1. (A) Compute the dimension of $\operatorname{Spec} \mathbb{Z}[x]$ and list one chain of irreducible closed subsets of length $2$. Let $R = \mathbb{Z}_{(2)}$, a discrete valuation ring. Show that $(2x - 1)$ is a maximal ideal of $R[x]$ of height $1$, while $\dim R[x] = 2$. So part 3 of Theorem P3.7.4 fails for integral schemes of finite type over a discrete valuation ring.
2. (A) Let $X = V(x^2 + y^2 + z^2 - 1) \subseteq \mathbb{A}^3_{\mathbb{R}}$. Show that $X$ is integral of dimension $2$, and that the point $V(x - 2, y^2 + 3, z)$ lies on $X$, has residue field $\mathbb{C}$ and is closed.
3. (A) Show that the twisted cubic, the image of $\mathbb{P}^1_k \to \mathbb{P}^3_k$, $[s : t] \mapsto [s^3 : s^2 t : s t^2 : t^3]$, has dimension $1$. Show that $V_+(x_0 x_2 - x_1^2, x_1 x_3 - x_2^2)$ is the union of the twisted cubic and the line $V_+(x_1, x_2)$, in accordance with part 4 of Proposition P3.7.5.
4. (B) Let $X$ be a Noetherian topological space. Show that $X$ has finitely many irreducible components and that $\dim X$ can be infinite: use Nagata's ring of Example P1.5.10.
5. (B) Let $X$ be an integral scheme of finite type over $k$, and $Z_1 \subseteq Z_2$ irreducible closed subsets. Show that $\operatorname{codim}(Z_1, X) = \operatorname{codim}(Z_1, Z_2) + \operatorname{codim}(Z_2, X)$.
6. (B) Let $f \colon X \to Y$ be a dominant morphism of integral schemes of finite type over $k$ with $\dim X = \dim Y$. Show that $K(X)$ is a finite extension of $K(Y)$, and that the generic fibre is $\operatorname{Spec} K(X)$. Deduce that there is a nonempty open $V \subseteq Y$ over which the fibres of $f$ are finite.
7. (C) Show that every irreducible component of $V_+(F_1, \dots, F_r) \subseteq \mathbb{P}^n_k$ has dimension $n - r$ when the components of the affine cone $V(F_1, \dots, F_r) \subseteq \mathbb{A}^{n+1}_k$ all have dimension $n + 1 - r$. For this, show that an irreducible closed $Z \subseteq \mathbb{P}^n_k$ has a cone of dimension $\dim Z + 1$, by comparing $Z \cap D_+(x_i)$ with the cone over it in $D(x_i) \subseteq \mathbb{A}^{n+1}_k$.

### Lean

Mathlib defines the Krull dimension of a space as `topologicalKrullDim` and of a ring as `ringKrullDim`, both with values in `WithBot ℕ∞`, and proves in `AlgebraicGeometry.ringKrullDim_stalk_eq_coheight` that the dimension of a stalk is the coheight of the point in the specialization order. Closed points of schemes locally of finite type over a Jacobson base are treated in `Mathlib/AlgebraicGeometry/Morphisms/Finite.lean`. The equality of the dimension with the transcendence degree for a variety, the theorem on chains, and the dimension of fibres for schemes are not in Lean as stated. The handbook adds no `MinimalModel` node here.

### Notes and history

The definition of dimension by chains of irreducible closed sets is the topological form of Krull's definition for rings. Hartshorne, Section I.1, proves the affine case for varieties over an algebraically closed field, and Exercise II.3.20 asks for the scheme version of Theorem P3.7.4. The theorem on the dimension of fibres is usually stated with a second part, Chevalley's upper semicontinuity: the function $x \mapsto \dim_x X_{f(x)}$ is upper semicontinuous, and there is a nonempty open $V \subseteq Y$ over which every component of every fibre has dimension exactly $\dim X - \dim Y$. That part needs more tools, and Hartshorne, Exercise II.3.22, outlines a proof. The literature state is theorem. In the minimal model program the dimension of fibres enters through the definition of a contraction: a birational contraction is divisorial if its exceptional locus has codimension one and small if it has codimension at least two, and a Mori fibre space is a contraction with $\dim Z < \dim X$.
