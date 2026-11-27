---
title: Flat morphisms
nodes: []
sources: [Vak25, Har77, Stacks]
reads_with: [Vak25:ch24, Har77:III.9]
requires: [P1.1, P1.2, P1.5, P1.7, P3.3, P3.5, P3.7]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Flat morphisms

### Statement

Flatness of modules is Definition P1.1.43. This section moves it to schemes. For a morphism $f \colon X \to Y$ and $x \in X$ with $y = f(x)$, the map on stalks $f^\#_x \colon \mathcal{O}_{Y, y} \to \mathcal{O}_{X, x}$ is a local homomorphism, so every $\mathcal{O}_{X, x}$-module is an $\mathcal{O}_{Y, y}$-module.

**Definition P3.13.1 (flat sheaf, flat morphism).** Let $f \colon X \to Y$ be a morphism and $\mathcal{F}$ an $\mathcal{O}_X$-module. Then $\mathcal{F}$ is *flat over $Y$ at $x$* if the stalk $\mathcal{F}_x$ is a flat $\mathcal{O}_{Y, f(x)}$-module, and *flat over $Y$* if it is flat over $Y$ at every point. The morphism $f$ is *flat* if $\mathcal{O}_X$ is flat over $Y$, and *faithfully flat* if it is flat and surjective.

Lean: Mathlib `AlgebraicGeometry.Flat` (definition), for morphisms of schemes; `AlgebraicGeometry.Flat.iff_flat_stalkMap` says that it is the definition through stalks given here (proved in Mathlib). Flatness of a sheaf over the base is not in Lean as stated.

**Proposition P3.13.2 (flatness is local).** Let $\varphi \colon A \to B$ be a ring homomorphism and $M$ a $B$-module. For a prime $\mathfrak{Q}$ of $B$ write $\mathfrak{p} = \varphi^{-1}(\mathfrak{Q})$.

1. The following are equivalent: (a) $M$ is flat over $A$; (b) $M_\mathfrak{Q}$ is flat over $A_\mathfrak{p}$ for every prime $\mathfrak{Q}$ of $B$; (c) $M_\mathfrak{Q}$ is flat over $A$ for every maximal ideal $\mathfrak{Q}$ of $B$.
2. Let $f \colon X \to Y$ be a morphism and $\mathcal{F}$ a quasi-coherent sheaf on $X$. The following are equivalent: (a) $\mathcal{F}$ is flat over $Y$; (b) for every affine open $U = \operatorname{Spec} A$ of $Y$ and every affine open $V = \operatorname{Spec} B$ of $f^{-1}(U)$, the $B$-module $\mathcal{F}(V)$ is flat over $A$; (c) there are such pairs $(U_i, V_i)$ with $\bigcup_i V_i = X$ and every $\mathcal{F}(V_i)$ flat over $A_i$.

Lean: Mathlib `AlgebraicGeometry.Flat` is a `HasRingHomProperty` for `RingHom.Flat`, which contains part 2 for $\mathcal{F} = \mathcal{O}_X$ (proved in Mathlib). Part 1 and the version for sheaves are not in Lean as stated.

**Proposition P3.13.3 (first properties).** Let $f \colon X \to Y$ be a morphism and $\mathcal{F}$ a quasi-coherent sheaf on $X$.

1. Open immersions are flat. If $X = \operatorname{Spec} B$ and $Y = \operatorname{Spec} A$, then $f$ is flat if and only if $B$ is a flat $A$-algebra.
2. If $\mathcal{F}$ is flat over $Y$ and $g \colon Y \to Z$ is flat, then $\mathcal{F}$ is flat over $Z$. In particular a composite of flat morphisms is flat.
3. If $\mathcal{F}$ is flat over $Y$ and $g \colon Y' \to Y$ is a morphism, then the pullback $\mathcal{F}'$ of $\mathcal{F}$ to $X' = X \times_Y Y'$ is flat over $Y'$. In particular flatness is stable under base change.
4. The projections $\mathbb{A}^n_Y \to Y$ and $\mathbb{P}^n_Y \to Y$ are flat.
5. A flat morphism $\operatorname{Spec} B \to \operatorname{Spec} A$ is faithfully flat if and only if $B$ is a faithfully flat $A$-algebra. A flat local homomorphism of local rings is faithfully flat.

Lean: Mathlib `AlgebraicGeometry.Flat` has instances for open immersions, `AlgebraicGeometry.Flat.comp` and `AlgebraicGeometry.Flat.isStableUnderBaseChange`, and `AlgebraicGeometry.Flat.SpecMap_iff` and `AlgebraicGeometry.flat_and_surjective_SpecMap_iff` are the affine statements of parts 1 and 5 (proved in Mathlib). The versions for sheaves are not in Lean as stated.

A *Dedekind scheme* is an integral Noetherian normal scheme of dimension $1$. On an affine open $\operatorname{Spec} A$ the ring $A$ is a normal Noetherian domain (part 1 of Proposition P3.7.32) of dimension at most $1$, so each local ring $A_\mathfrak{p}$ at a nonzero prime is a discrete valuation ring by Corollary P1.7.13, and $A_{(0)}$ is a field. The spectrum of a discrete valuation ring, $\mathbb{A}^1_k$ and a smooth curve over $k$ are Dedekind schemes. For a quasi-coherent sheaf $\mathcal{F}$ on a locally Noetherian scheme $X$ and an affine open $V = \operatorname{Spec} B$, the *associated points* of $\mathcal{F}$ in $V$ are the primes of $\operatorname{Ass}_B(\mathcal{F}(V))$ (Definition P1.2.41).

**Theorem P3.13.4 (flatness over a Dedekind scheme).** Let $Y$ be a Dedekind scheme with generic point $\eta$, $f \colon X \to Y$ a morphism with $X$ locally Noetherian, and $\mathcal{F}$ a quasi-coherent sheaf on $X$. The following are equivalent.

1. $\mathcal{F}$ is flat over $Y$.
2. $\mathcal{F}$ is torsion free over $Y$: for every open $W \subseteq Y$ and every nonzero $a \in \mathcal{O}_Y(W)$, multiplication by $f^\# a$ is injective on $\mathcal{F}|_{f^{-1}(W)}$.
3. For every affine open $V$ of $X$ that maps into an affine open of $Y$, every associated point of $\mathcal{F}$ in $V$ maps to $\eta$.

In particular, if $X$ is integral and $f$ is dominant, then $f$ is flat.

Lean: not in Lean as stated.

**Proposition P3.13.5 (the flat closure over a discrete valuation ring).** Let $R$ be a discrete valuation ring with uniformizer $t$, fraction field $K = R_t$ and residue field $\kappa$. Let $B$ be a Noetherian $R$-algebra, $X = \operatorname{Spec} B$, and $X_K = \operatorname{Spec} B_t$ the generic fibre. Let $Z_K = V(J)$ be a closed subscheme of $X_K$, and let $I \subseteq B$ be the inverse image of $J$ under $B \to B_t$.

1. The closed subscheme $Z = V(I)$ of $X$ is flat over $R$, and $Z \times_R K = Z_K$.
2. $Z$ is the only closed subscheme of $X$ with the two properties of part 1.
3. The underlying set of $Z$ is the closure of $Z_K$ in $X$.

Lean: not in Lean as stated.

The scheme $Z$ is the *flat closure* of $Z_K$, and its special fibre $Z_\kappa = Z \times_R \kappa$ is the *flat limit* of $Z_K$.

**Theorem P3.13.6 (dimension of the fibres of a flat morphism).**

1. Let $f \colon X \to Y$ be a flat morphism of locally Noetherian schemes, $x \in X$ and $y = f(x)$. Then $\dim \mathcal{O}_{X, x} = \dim \mathcal{O}_{Y, y} + \dim \mathcal{O}_{X_y, x}$.
2. Let $f \colon X \to Y$ be a flat morphism of integral schemes of finite type over a field $k$, and let $y \in Y$ be a closed point. Then every irreducible component of the fibre $X_y$ has dimension $\dim X - \dim Y$.

Lean: not in Lean as stated. Mathlib `Ideal.height_eq_height_add_of_liesOver_of_hasGoingDown` is the algebraic equality behind part 1 (proved in Mathlib).

### Proof in words

A module is flat when tensoring with it keeps injections injective. The kernel of a tensored map is a module over the bigger ring, and a module is zero when all its localizations are zero, so flatness can be checked one prime at a time. This makes flatness a property of stalks, and it moves through composition and base change because tensor products are associative.

Over a Dedekind scheme the local rings of the base are discrete valuation rings, and over a principal ideal domain flat means torsion free. A section of the base kills a section of $\mathcal{F}$ exactly when it lies in an associated prime, so torsion freeness says that no associated point of $\mathcal{F}$ lies over a closed point. Over a discrete valuation ring this gives the flat closure: take the functions on $X$ whose restriction to the generic fibre lies in $J$. The quotient embeds in a module over $K$, so it has no $t$-torsion, and every other flat extension has the same ideal.

The dimension formula is the equality of P1 Ch. 5 for a flat local homomorphism. For varieties it gives the dimension of every component of a fibre over a closed point, once a closed point is chosen on that component and on no other.

### Examples

**Example P3.13.7 (a conic degenerating to a node).** Let $X = \operatorname{Spec} k[x, y, t]/(xy - t) \to \mathbb{A}^1_k = \operatorname{Spec} k[t]$, the family of Example P3.3.34. The ring $k[x, y, t]/(xy - t) \cong k[x, y]$ is a domain and $t \mapsto xy$ is injective, so $f$ is dominant, and $f$ is flat by Theorem P3.13.4. This is Example P1.1.54 in geometric form. The fibre over $t = a \neq 0$ is the smooth conic $xy = a$, and the fibre over $0$ is the node $xy = 0$. Both have pure dimension $1 = 2 - 1$, as part 2 of Theorem P3.13.6 says. A flat family of smooth curves may acquire singularities in a special fibre; what flatness keeps is the dimension and, in the projective case, the Hilbert polynomial of Section 13.2.

**Example P3.13.8 (the blow-up is not flat).** Let $\pi \colon \tilde X = \operatorname{Bl}_0 \mathbb{A}^2_k \to \mathbb{A}^2_k$ be the blow-up of the origin (Chapter 11). Both schemes are integral of dimension $2$. The fibre over a point $p \neq 0$ is a single point, of dimension $0 = 2 - 2$. The fibre over the origin is the exceptional curve $E \cong \mathbb{P}^1_k$, of dimension $1$. By part 2 of Theorem P3.13.6, $\pi$ is not flat. Example P1.1.56 shows the same thing in a chart by algebra: the ideals $(x)$ and $(y)$ have intersection $(xy)$, while their extensions to $k[x, u]$ meet in a larger ideal, against Proposition P1.1.51. The base $\mathbb{A}^2_k$ has dimension $2$, so Theorem P3.13.4 does not apply.

**Example P3.13.9 (an embedded point breaks flatness).** Let $B = k[t, x]/(tx, x^2)$ over $R = k[t]$, as in Example P1.2.51. The decomposition $(tx, x^2) = (x) \cap (t, x^2)$ gives $\operatorname{Ass}(B) = \{(x), (t, x)\}$. The prime $(x)$ is the generic point of the $t$-line and lies over $(0)$. The prime $(t, x)$ is an embedded point and lies over $(t)$, a closed point. By Theorem P3.13.4, $B$ is not flat over $k[t]$: the class of $x$ is a nonzero element killed by $t$. The underlying space of $\operatorname{Spec} B$ is the $t$-line, every fibre is one point, and still the family is not flat, because the fibre over $0$ is $\operatorname{Spec} k[x]/(x^2)$, of length $2$, and the others have length $1$.

**Example P3.13.10 (two points that collide).** Let $a \in k$ and let $Z \subseteq \mathbb{A}^2_{k[t]} = \operatorname{Spec} k[t][x, y]$ be $V(I)$ with $I = (y - ax, x(x - t))$. Then $k[t][x, y]/I \cong k[t][x]/(x^2 - tx)$, a free $k[t]$-module with basis $1, x$, so $Z$ is flat over $\mathbb{A}^1_k$. For $t = c \neq 0$ the fibre is the two reduced points $(0, 0)$ and $(c, ac)$ on the line $y = ax$. The fibre over $0$ is $V(y - ax, x^2)$, a point with multiplicity $2$ that remembers the line $y = ax$ along which the points came together. As $a$ varies, the limits are different subschemes with the same support. By Proposition P3.13.5 each is the unique flat limit of its family over $k[t]_{(t)}$. The set of all such double points at the origin, together with $V(x, y^2)$, is a projective line of directions: Exercise 6 of Section 13.4.

**Example P3.13.11 (two skew lines that come together).** Over $R = k[t]$ let $L_1 = V_+(x, z)$ and $L_2 = V_+(y, z - tw)$ in $\mathbb{P}^3_R$ with coordinates $x, y, z, w$. For $t = c \neq 0$ the two lines are disjoint, since $x = y = z = 0$ and $z = cw$ force $w = 0$. At $t = 0$ they meet in the point $p = [0 : 0 : 0 : 1]$. The union $L_1 \cup L_2$ has the ideal
$$
I = (x, z) \cap (y, z - tw) = (xy, \; x(z - tw), \; yz, \; z(z - tw)).
$$
To see the equality, note that the right side is contained in both primes. Conversely let $g = ax + bz$ lie in $(y, z - tw)$. Modulo the right side, every monomial multiple of $x$ or of $z$ can be reduced: $xy, yz \equiv 0$, $xz \equiv txw$ and $z^2 \equiv tzw$. So $g \equiv a'x + b'z$ with $a' \in k[t][x, w]$ and $b' \in k[t][w]$. Setting $y = 0$ and $z = tw$ gives $a'x + b'tw = 0$ in $k[t][x, w]$, so $x$ divides $b' t w$ and so $b'$, which has no $x$: $b' = 0$, then $a' = 0$, and $g$ lies in the right side. Both primes $(x, z)$ and $(y, z - tw)$ do not contain $t$, so $t$ is a nonzerodivisor on $S/I$ and the family is flat over $k[t]$, by the same argument as Theorem P3.13.4 on the charts $D_+(x_i)$ (Theorem P3.13.14 below states it for projective families). The flat limit is $I_0 = (xy, xz, yz, z^2)$. It is not the ideal $(xy, z)$ of the union of the two limit lines $V_+(x, z) \cup V_+(y, z)$: it is strictly smaller, and
$$
(xy, xz, yz, z^2) = (xy, z) \cap (x, y, z^2).
$$
For the equality, the monomials $w^a x^b$ with $b \geq 0$, $w^a y^b$ with $b \geq 1$ and $w^a z$ form a basis of $S/I_0$ over $k$. The images of $(xy, z)$ and $(x, y, z^2)$ in $S/I_0$ are spanned by the monomials $w^a z$, and by the monomials $w^a x^b, w^a y^b$ with $b \geq 1$. These sets are disjoint, so the images meet in $0$. The flat limit is the two crossing lines with an embedded point at $p$ that sticks out of their plane $z = 0$ in the direction of $z$. Section 13.2 shows why the embedded point must be there: two skew lines have Hilbert polynomial $2m + 2$, and two crossing lines have $2m + 1$.

### Proof

*Proof of Proposition P3.13.2.* Part 1. Assume (a). The module $M_\mathfrak{Q} = M \otimes_B B_\mathfrak{Q}$ is flat over $A$: for an $A$-module $N$, $N \otimes_A M_\mathfrak{Q} = (N \otimes_A M) \otimes_B B_\mathfrak{Q}$, a composite of the exact functors $- \otimes_A M$ and localization. An $A_\mathfrak{p}$-module $N$ has $N \otimes_A A_\mathfrak{p} = N$, so $N \otimes_{A_\mathfrak{p}} M_\mathfrak{Q} = N \otimes_A M_\mathfrak{Q}$. An injective map of $A_\mathfrak{p}$-modules is an injective map of $A$-modules, so it stays injective after $- \otimes_{A_\mathfrak{p}} M_\mathfrak{Q}$. This is (b). Assume (b). For an $A$-module $N$, $N \otimes_A M_\mathfrak{Q} = (N \otimes_A A_\mathfrak{p}) \otimes_{A_\mathfrak{p}} M_\mathfrak{Q}$, a composite of exact functors (Example P1.1.57), so $M_\mathfrak{Q}$ is flat over $A$, and (c) holds. Assume (c), and let $u \colon N' \to N$ be an injective map of $A$-modules. The kernel $C$ of $u \otimes 1 \colon N' \otimes_A M \to N \otimes_A M$ is a $B$-module, and localization at $\mathfrak{Q}$ is exact, so $C_\mathfrak{Q}$ is the kernel of $N' \otimes_A M_\mathfrak{Q} \to N \otimes_A M_\mathfrak{Q}$, which is $0$ by (c). By Theorem P1.2.8, $C = 0$.

Part 2. For an affine open $V = \operatorname{Spec} B$ inside $f^{-1}(U)$ with $U = \operatorname{Spec} A$, a point $x \in V$ is a prime $\mathfrak{Q}$ of $B$, $f(x)$ is $\mathfrak{p} = \varphi^{-1}(\mathfrak{Q})$, $\mathcal{F}_x = M_\mathfrak{Q}$ for $M = \mathcal{F}(V)$ (Theorem P3.5.12), and $\mathcal{O}_{Y, f(x)} = A_\mathfrak{p}$. So $\mathcal{F}$ is flat over $Y$ at every point of $V$ if and only if (b) of part 1 holds for $M$, that is, if and only if $M$ is flat over $A$. This gives (a) $\Rightarrow$ (b), and (b) $\Rightarrow$ (c) since such pairs cover $X$. If (c) holds, every $x$ lies in some $V_i$, and $\mathcal{F}$ is flat at $x$. $\square$

*Proof of Proposition P3.13.3.* Part 1. For an open immersion the stalk maps are isomorphisms. The affine statement is part 2 of Proposition P3.13.2 with $V = X$, $U = Y$, in the direction (a) $\Rightarrow$ (b), and (c) $\Rightarrow$ (a) with the single pair $(Y, X)$.

Part 2. Let $x \in X$, $y = f(x)$, $z = g(y)$. The $\mathcal{O}_{Z, z}$-module $\mathcal{F}_x$ has $N \otimes_{\mathcal{O}_{Z, z}} \mathcal{F}_x = (N \otimes_{\mathcal{O}_{Z, z}} \mathcal{O}_{Y, y}) \otimes_{\mathcal{O}_{Y, y}} \mathcal{F}_x$ by Proposition P1.1.34, a composite of exact functors.

Part 3. By part 2 of Proposition P3.13.2 it suffices to treat an affine cover of $X'$. Take affine opens $U = \operatorname{Spec} A$ of $Y$, $V = \operatorname{Spec} B$ of $f^{-1}(U)$ and $U' = \operatorname{Spec} A'$ of $g^{-1}(U)$. By the construction of the fibre product (Theorem P3.3.19), the opens $V \times_U U' = \operatorname{Spec}(B \otimes_A A')$ cover $X'$, and $\mathcal{F}'$ is the sheaf of $M \otimes_B (B \otimes_A A') = M \otimes_A A'$ for $M = \mathcal{F}(V)$ (Proposition P3.5.32). For an $A'$-module $N$, $N \otimes_{A'} (A' \otimes_A M) = N \otimes_A M$, which is exact in $N$ because $M$ is flat over $A$. So $M \otimes_A A'$ is flat over $A'$.

Part 4. $A[x_1, \dots, x_n]$ is a free $A$-module, hence flat (Proposition P1.1.45). So $\mathbb{A}^n_U \to U$ is flat for affine $U$, and $\mathbb{A}^n_Y \to Y$ is flat by part 2 of Proposition P3.13.2. The scheme $\mathbb{P}^n_Y$ is covered by the opens $D_+(x_i) \cong \mathbb{A}^n_Y$, so it is flat as well.

Part 5. Let $A \to B$ be flat. If $\operatorname{Spec} B \to \operatorname{Spec} A$ is surjective, every maximal ideal $\mathfrak{m}$ of $A$ is the inverse image of a prime $\mathfrak{Q}$ of $B$, and $\mathfrak{m} B \subseteq \mathfrak{Q} \neq B$, so $A \to B$ is faithfully flat by Proposition P1.1.53. Conversely, if $A \to B$ is faithfully flat and $\mathfrak{p}$ is a prime of $A$, then $\kappa(\mathfrak{p}) \neq 0$, so $B \otimes_A \kappa(\mathfrak{p}) \neq 0$ by Definition P1.1.52. A nonzero ring has a prime ideal, and by Proposition P3.3.28 the primes of $B \otimes_A \kappa(\mathfrak{p})$ are the points of the fibre over $\mathfrak{p}$, so the fibre is nonempty. For a flat local homomorphism $(A, \mathfrak{m}) \to (B, \mathfrak{n})$, $\mathfrak{m} B \subseteq \mathfrak{n} \neq B$, and $\mathfrak{m}$ is the only maximal ideal of $A$. $\square$

*Proof of Theorem P3.13.4.* All three conditions are local on $X$ and $Y$, by part 2 of Proposition P3.13.2 for condition 1. So let $U = \operatorname{Spec} A \subseteq Y$ and $V = \operatorname{Spec} B \subseteq f^{-1}(U)$ be affine, with $M = \mathcal{F}(V)$. The ring $B$ is Noetherian (Proposition P3.2.23), and $A$ is a normal Noetherian domain of dimension at most $1$. For $U$ affine, condition 2 on $V$ says that every $a \in A \setminus \{0\}$ acts injectively on $M$, so it is enough to prove that the following are equivalent: (1) $M$ is flat over $A$; (2) $M$ is torsion free over $A$; (3) $\mathfrak{P} \cap A = 0$ for every $\mathfrak{P} \in \operatorname{Ass}_B(M)$, where $\mathfrak{P} \cap A$ is the inverse image in $A$.

(1) $\Rightarrow$ (2). For $a \neq 0$ the map $a \colon A \to A$ is injective, as $A$ is a domain. Tensoring with the flat module $M$ keeps it injective, and the result is $a \colon M \to M$.

(2) $\Rightarrow$ (1). Let $\mathfrak{Q}$ be a prime of $B$ over $\mathfrak{p} \subseteq A$. The module $M_\mathfrak{Q}$ is torsion free over $A_\mathfrak{p}$: if $(a/s) \cdot (m/u) = 0$ with $a \in A \setminus \{0\}$, $s \in A \setminus \mathfrak{p}$ and $m \in M$, $u \in B \setminus \mathfrak{Q}$, then $v a m = 0$ for some $v \in B \setminus \mathfrak{Q}$, so $a (vm) = 0$, $vm = 0$ by (2), and $m/u = 0$. The ring $A_\mathfrak{p}$ is a field or a discrete valuation ring, a principal ideal domain in both cases, so $M_\mathfrak{Q}$ is flat over $A_\mathfrak{p}$ by Proposition P1.1.47. Part 1 of Proposition P3.13.2 gives (1).

(2) $\Leftrightarrow$ (3). By Proposition P1.2.44 the elements of $B$ that kill a nonzero element of $M$ form the union of the associated primes of $M$. So $a \in A$ kills a nonzero element of $M$ if and only if its image lies in some $\mathfrak{P} \in \operatorname{Ass}_B(M)$, that is, $a \in \mathfrak{P} \cap A$. Hence $M$ is torsion free over $A$ if and only if every $\mathfrak{P} \cap A$ is $0$. The point $\mathfrak{P}$ maps to the prime $\mathfrak{P} \cap A$ of $A$, and $(0)$ is the generic point $\eta$.

For the last statement let $X$ be integral and $f$ dominant. On $V = \operatorname{Spec} B$, $B$ is a domain, so $\operatorname{Ass}_B(B) = \{(0)\}$. The generic point of $X$ maps to the generic point of $Y$, because its image is dense, so $(0) \cap A = 0$, and (3) holds for $\mathcal{F} = \mathcal{O}_X$. $\square$

*Proof of Proposition P3.13.5.* Write $\iota \colon B \to B_t$. Part 1. The map $B/I \to B_t/J$ is injective by the definition of $I$, and $B_t/J$ is a module over $K$, on which $t$ is injective. So $t$ is injective on $B/I$, and $B/I$ is torsion free over $R$: every nonzero element of $R$ is a unit times a power of $t$. By Theorem P3.13.4 for $\operatorname{Spec} R$, $Z = \operatorname{Spec} B/I$ is flat over $R$. The generic fibre of $Z$ is $\operatorname{Spec} (B/I)_t = \operatorname{Spec} B_t / I B_t$. Here $I B_t \subseteq J$, as $\iota(I) \subseteq J$. Conversely, an element of $J$ is $\iota(b)/t^n$ for some $b \in B$, and $\iota(b) = t^n \cdot \iota(b)/t^n \in J$, so $b \in I$ and $\iota(b)/t^n \in I B_t$. So $I B_t = J$ and $Z \times_R K = Z_K$.

Part 2. Let $Z' = V(I')$ be a closed subscheme with $B/I'$ flat over $R$ and $I' B_t = J$. Then $\iota(I') \subseteq J$, so $I' \subseteq I$. Let $b \in I$. Then $\iota(b) \in J = I' B_t$, so $\iota(b) = \iota(c)/t^n$ with $c \in I'$, and $t^{n + l} b - t^l c = 0$ in $B$ for some $l$. So $t^{n + l} b \in I'$. By Theorem P3.13.4, $t$ is injective on $B/I'$, so $b \in I'$. Hence $I' = I$.

Part 3. A prime $\mathfrak{P}$ of $B$ with $t \notin \mathfrak{P}$ is a point of $X_K$, and it lies in $Z_K$ if and only if $\mathfrak{P} B_t \supseteq J$, that is, $\mathfrak{P} \supseteq I$. So $Z_K$ is the set of primes of $V(I)$ that do not contain $t$. The minimal primes over $I$ are associated primes of $B/I$ (Theorem P1.2.48), and $t$ lies in none of them, because $t$ is a nonzerodivisor on $B/I$ (Proposition P1.2.44). So all minimal primes over $I$ lie in $Z_K$. The closure of $Z_K$ is $V$ of the intersection of the primes in $Z_K$ (Proposition P1.2.18). That intersection contains $\sqrt{I}$, and is contained in the intersection of the minimal primes over $I$, which is $\sqrt{I}$. So the closure is $V(\sqrt I) = V(I)$. $\square$

*Proof of Theorem P3.13.6.* Part 1. The homomorphism $\mathcal{O}_{Y, y} \to \mathcal{O}_{X, x}$ is a flat local homomorphism of Noetherian local rings. Its fibre ring is $\mathcal{O}_{X, x}/\mathfrak{m}_y \mathcal{O}_{X, x}$, which is the local ring $\mathcal{O}_{X_y, x}$: on affine opens with $y = \mathfrak{p}$ and $x = \mathfrak{Q}$, the fibre is $\operatorname{Spec}(B_\mathfrak{p}/\mathfrak{p} B_\mathfrak{p})$ by Proposition P3.3.28, and its local ring at $\mathfrak{Q}$ is $B_\mathfrak{Q}/\mathfrak{p} B_\mathfrak{Q}$. Theorem P1.5.45 gives the equality.

Part 2. The fibre $X_y$ is of finite type over the field $\kappa(y)$, so it is Noetherian with finitely many irreducible components. Let $W$ be one of them, and let $W^\circ$ be the complement in $W$ of the other components, a nonempty open subset of $W$, locally closed in $X_y$. By part 3 of Proposition P3.7.3, $W^\circ$ contains a closed point $x$ of $X_y$. Every irreducible closed subset of $X_y$ through $x$ lies in an irreducible component, which contains $x$ and so is $W$. By part 4 of Proposition P3.7.2, $\dim \mathcal{O}_{X_y, x}$ is the codimension of $\{x\}$ in $X_y$, which is then its codimension in $W$, and this is $\dim W$ by part 4 of Theorem P3.7.4 applied to $W$ with its reduced structure. The point $y$ is closed, so $f^{-1}(y)$ is closed in $X$, and by Proposition P3.3.28 the point $x$ is closed in $X$. By part 3 of Theorem P3.7.4, $\dim \mathcal{O}_{X, x} = \dim X$ and $\dim \mathcal{O}_{Y, y} = \dim Y$. Part 1 gives $\dim W = \dim X - \dim Y$. $\square$

### Exercises

1. (A) Let $B = k[t, x]/(tx)$ over $R = k[t]$. Find $\operatorname{Ass}(B)$, show that $B$ is not flat over $R$ by Theorem P3.13.4, and describe the fibres. Compare with Example P1.1.55.
2. (A) Let $A$ be a ring and $f \in A[x]$ monic of degree $d$. Show that $A[x]/(f)$ is a free $A$-module with basis $1, x, \dots, x^{d - 1}$, so that $\operatorname{Spec} A[x]/(f) \to \operatorname{Spec} A$ is finite and flat.
3. (B) Let $f \colon X \to Y$ be a finite morphism with $Y$ locally Noetherian. Show that $f$ is flat if and only if $f_* \mathcal{O}_X$ is locally free. (Use Theorem P1.1.50 and part 5 of Proposition P3.5.25.) Deduce that the degree of the fibres $\dim_{\kappa(y)} \Gamma(X_y, \mathcal{O}_{X_y})$ is locally constant on $Y$.
4. (B) In $\mathbb{A}^2_{k[t]}$ let $Z_K$ be the three points $(0, 0)$, $(t, 0)$ and $(0, t)$ over $K = k(t)$. Show that $(xy, x^2 - tx, y^2 - ty)$ is the ideal of the flat closure, by showing that $k[t][x, y]$ modulo it is free over $k[t]$ with basis $1, x, y$. Deduce that the flat limit is $V((x, y)^2)$, the first order neighbourhood of the origin.
5. (B) Let $f \colon X \to Y$ be a flat morphism of locally Noetherian schemes. Show that $f$ maps the generic point of every irreducible component of $X$ to the generic point of an irreducible component of $Y$. (Use Lemma P1.5.44.) Deduce that if $f$ is flat and $Y$ is irreducible, every irreducible component of $X$ dominates $Y$.
6. (C) Over $R = k[a]$ consider the curves $C_a \subseteq \mathbb{A}^3$ parametrized by $x = s^2 - 1$, $y = s^3 - s$, $z = as$. Let $I = (xz - ay, \; z^2 - a^2(x + 1), \; yz - ax(x + 1), \; y^2 - x^2(x + 1)) \subseteq R[x, y, z]$. Show that the elements $x^i$, $x^i y$ for $i \geq 0$, and $z$ span $R[x, y, z]/I$ over $R$, and that their images in $K[s]$, $K = k(a)$, are linearly independent, by looking at degrees in $s$. Deduce that $R[x, y, z]/I$ is free over $R$, that $I$ is the ideal of the flat closure of the curve over $K$, and that the flat limit at $a = 0$ is the nodal cubic $y^2 = x^2(x + 1)$ in the plane $z = 0$ with an embedded point at the origin pointing out of the plane. This is Hartshorne's Example III.9.8.4.

### Lean

Mathlib defines a flat morphism of schemes as `AlgebraicGeometry.Flat`, through the flatness of the ring maps on affine opens. `AlgebraicGeometry.Flat.iff_flat_stalkMap` compares it with the stalk definition of Definition P3.13.1, and the instances for open immersions, composites and base change are parts 1 to 3 of Proposition P3.13.3 for $\mathcal{F} = \mathcal{O}_X$. Flatness of a quasi-coherent sheaf over the base, the flat closure and the dimension of fibres are not in Lean as stated. mmp-lean does not use flat morphisms yet, and the handbook adds no `MinimalModel` node here.

### Notes and history

Flatness was introduced by Serre in *Géométrie algébrique et géométrie analytique* (1956), where the analytic local rings are flat over the algebraic ones, and was made central by Grothendieck in EGA IV. The geometric meaning, that the fibres of a flat family vary continuously, is in Hartshorne, Section III.9, where Proposition III.9.7 is the criterion of Theorem P3.13.4 and Proposition III.9.8 is the flat closure. Exercise 6 is his Example III.9.8.4. Vakil, Chapter 24, treats flatness with the same examples. The literature state is theorem.

In the minimal model program flat families are the families of the moduli problems. The flat limit over a discrete valuation ring is the algebraic form of a degeneration, and its uniqueness is the separatedness of Hilbert schemes and of the moduli spaces of stable pairs (Volume 13). The embedded point of Example P3.13.11 is typical: flat limits of reduced schemes need not be reduced, which is why the Hilbert scheme parametrizes all closed subschemes and not only the varieties.
