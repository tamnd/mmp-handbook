---
title: Noether normalization and its consequences
nodes: []
sources: [AM69, Mat86, Eis95]
reads_with: [AM69:ch5, Mat86:ch2, Eis95:ch13]
requires: [P1.1, P1.2, P1.3]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Noether normalization and its consequences

### Statement

**Theorem P1.4.27 (Noether normalization).** Let $k$ be a field and $A$ a finitely generated $k$-algebra. Then there are elements $y_1, \dots, y_d \in A$, algebraically independent over $k$, such that $A$ is finite over $k[y_1, \dots, y_d]$.

Lean: Mathlib `exists_integral_inj_algHom_of_fg` and `exists_finite_inj_algHom_of_fg` (proved in Mathlib).

*Proof.* Let $A = k[x_1, \dots, x_n]$. Induction on $n$. If $x_1, \dots, x_n$ are algebraically independent, take $y_i = x_i$. Otherwise there is a nonzero polynomial $f$ with $f(x_1, \dots, x_n) = 0$. Choose an integer $r$ larger than every exponent that occurs in $f$, and put
$$
z_i = x_i - x_n^{r^i} \qquad (1 \leq i \leq n - 1).
$$
Then $f(z_1 + x_n^{r}, z_2 + x_n^{r^2}, \dots, z_{n-1} + x_n^{r^{n-1}}, x_n) = 0$. A monomial $c\, x_1^{a_1} \cdots x_n^{a_n}$ of $f$ becomes $c\, x_n^{e(a)}$ plus terms of lower degree in $x_n$, with coefficients in $k[z_1, \dots, z_{n-1}]$, where
$$
e(a) = a_n + a_1 r + a_2 r^2 + \dots + a_{n-1} r^{n-1} .
$$
Since all $a_i < r$, the numbers $e(a)$ are distinct for distinct exponent vectors $a$, by uniqueness of base $r$ expansion. So exactly one monomial of $f$ gives the largest $e(a)$, and after division by its coefficient $c \in k^\times$ the relation is a monic equation for $x_n$ over $k[z_1, \dots, z_{n-1}]$. Hence $A = k[z_1, \dots, z_{n-1}][x_n]$ is finite over $A' = k[z_1, \dots, z_{n-1}]$. By induction, $A'$ is finite over $k[y_1, \dots, y_d]$ with the $y_i$ algebraically independent, and finite over finite is finite (Section 4.1). $\square$

**Corollary P1.4.28 (Zariski's lemma).** Let $K$ be a field that is a finitely generated $k$-algebra. Then $K$ is a finite extension of $k$.

Lean: Mathlib `finite_of_finite_type_of_isJacobsonRing` (proved in Mathlib), with $k$ a field, hence a Jacobson ring.

*Proof.* Choose $y_1, \dots, y_d$ by the theorem. Then $K$ is integral over $R = k[y_1, \dots, y_d]$, so $R$ is a field by Section 4.2. A polynomial ring in $d \geq 1$ variables is not a field, since $y_1$ has no inverse. So $d = 0$, and $K$ is finite over $k$. $\square$

P0 Ch. 3 deduces the Nullstellensatz from this corollary.

**Definition P1.4.29 (Jacobson ring).** A ring $A$ is a *Jacobson ring* if every prime ideal is an intersection of maximal ideals. Equivalently, the nilradical of every quotient $A/I$ equals its Jacobson radical.

Lean: Mathlib `IsJacobsonRing` (definition), stated with radical ideals.

**Theorem P1.4.30 (finitely generated algebras are Jacobson).** Let $A$ be a finitely generated $k$-algebra. Then $A$ is a Jacobson ring, and for every maximal ideal $\mathfrak{m}$ the field $A/\mathfrak{m}$ is finite over $k$. In $\operatorname{Spec} A$, the closed points are dense in every closed subset.

Lean: Mathlib `isJacobsonRing_of_finiteType` (proved in Mathlib).

*Proof.* The second claim is Zariski's lemma applied to $A/\mathfrak{m}$. For the first, let $\mathfrak{p}$ be a prime and $f \notin \mathfrak{p}$. It suffices to find a maximal ideal $\mathfrak{m} \supseteq \mathfrak{p}$ with $f \notin \mathfrak{m}$. The ring $C = (A/\mathfrak{p})[1/f]$ is a nonzero finitely generated $k$-algebra. Let $\mathfrak{n}$ be a maximal ideal of $C$ and $\mathfrak{m}$ its contraction to $A$. Then $\mathfrak{m} \supseteq \mathfrak{p}$ and $f \notin \mathfrak{m}$, since $f$ is a unit in $C$. By Zariski's lemma $C/\mathfrak{n}$ is finite over $k$. The domain $A/\mathfrak{m}$ is a $k$-subalgebra of $C/\mathfrak{n}$, so it is a domain of finite dimension over $k$, hence a field (multiplication by a nonzero element is an injective linear map, so it is surjective). So $\mathfrak{m}$ is maximal. For the last claim: a closed set is $V(\mathfrak{p}_1) \cup \dots \cup V(\mathfrak{p}_r)$ (Section 3.3), and $V(\mathfrak{p})$ is the closure of its closed points because $\mathfrak{p}$ is the intersection of the maximal ideals containing it. $\square$

**Theorem P1.4.31 (dimension of an affine domain).** Let $A$ be a finitely generated $k$-algebra that is a domain, with fraction field $K$. Then $\dim A = \operatorname{trdeg}_k K$, and this is the number $d$ of the normalization theorem. In particular $\dim k[x_1, \dots, x_n] = n$.

Lean: not in Lean in this form; Mathlib has `ringKrullDim` and the lower bound `ringKrullDim_add_natCard_le_ringKrullDim_mvPolynomial`.

*Proof.* Choose $R = k[y_1, \dots, y_d] \subseteq A$ by the theorem. Then $K$ is algebraic over $k(y_1, \dots, y_d)$, so $\operatorname{trdeg}_k K = d$, and $\dim A = \dim R$ by Section 4.2. The chain $0 \subsetneq (y_1) \subsetneq (y_1, y_2) \subsetneq \dots \subsetneq (y_1, \dots, y_d)$ of primes gives $\dim R \geq d$. For the upper bound, it suffices to show: if $\mathfrak{p} \neq 0$ is a prime of a finitely generated domain $A$, then $\operatorname{trdeg} \operatorname{Frac}(A/\mathfrak{p}) < \operatorname{trdeg} \operatorname{Frac}(A)$. Then along a chain of primes of length $m$ the transcendence degree drops $m$ times, so $m \leq d$. To prove it, let $\mathfrak{p}_0 = \mathfrak{p} \cap R$. By incomparability with the zero ideal, $\mathfrak{p}_0 \neq 0$. The ring $A/\mathfrak{p}$ is integral over $R/\mathfrak{p}_0$, so they have the same transcendence degree. The ring $R/\mathfrak{p}_0$ is generated by the images of $y_1, \dots, y_d$, and a nonzero $g \in \mathfrak{p}_0$ is an algebraic relation among them. So its transcendence degree is at most $d - 1$. $\square$

**Theorem P1.4.32 (finiteness of the integral closure).** Let $A$ be a finitely generated $k$-algebra that is a domain, with fraction field $K$, and let $L$ be a finite extension of $K$. Then the integral closure of $A$ in $L$ is a finite $A$-module, and it is a finitely generated $k$-algebra. In particular the normalization of an affine variety is a finite morphism.

Lean: Mathlib `IsIntegralClosure.finite` and `IsIntegralClosure.isNoetherianRing`, in the case where $A$ is integrally closed and $L/K$ is separable (proved in Mathlib).

*Proof sketch.* By Noether normalization $A$ is finite over $R = k[y_1, \dots, y_d]$, and the integral closure of $A$ in $L$ equals the integral closure of $R$ in $L$. So one may assume $A = R$, which is normal since it is factorial. If $L/K$ is separable, the trace form $(x, y) \mapsto \operatorname{Tr}_{L/K}(xy)$ is nondegenerate. Choose a basis $v_1, \dots, v_n$ of $L/K$ in the integral closure $B$, and let $w_1, \dots, w_n$ be the dual basis. For $b \in B$, the coefficients of $b$ in the basis $w_j$ are $\operatorname{Tr}(b v_j)$, which lie in $R$ by Exercise 5 of Section 4.3. So $B \subseteq \sum R w_j$, a finitely generated $R$-module, and $B$ is finite since $R$ is Noetherian. For inseparable $L/K$ one passes to a purely inseparable extension of $k(y_1, \dots, y_d)$ by adjoining $p$-th roots of the $y_i$; see Eisenbud, Chapter 13, and Atiyah-Macdonald, Chapter 5, for the separable step. $\square$

### Proof in words

Noether normalization finds, inside any finitely generated algebra, a polynomial ring over which the algebra is finite. A relation among the generators becomes a monic equation for the last generator after a change of variables, and induction does the rest. Over an infinite field a general linear change of variables works too.

Geometrically, every affine variety $X$ of dimension $d$ admits a finite surjective morphism $X \to \mathbb{A}^d$. This gives the dimension of $X$ as the transcendence degree of its function field, the number of independent rational functions. It gives the Nullstellensatz through Zariski's lemma: a point of $X$ in the scheme theoretic sense that is closed has a residue field finite over $k$. The Jacobson property says that the closed points of $\operatorname{Spec} A$ determine everything: two closed subsets with the same closed points are equal. This is why the MMP can work with varieties as sets of closed points and still use scheme theory. The finiteness of the normalization is used each time a construction starts by normalizing: the normalization of a variety, of a pair in Volume 13, or of the image of a morphism.

### Examples

**Example P1.4.33 (a hyperbola over a line).** Let $A = k[x, y]/(xy - 1)$. It is not finite over $k[x]$ (Section 4.1). Put $z = x + y$. Then $x^2 - zx + 1 = x^2 - x^2 - xy + 1 = 0$, so $x$ is integral over $k[z]$, and so is $y = z - x$. So $A$ is finite over $k[z]$: the map $(x, y) \mapsto x + y$ from the hyperbola to the line is a finite double cover.

**Example P1.4.34 (the substitution in practice).** For $A = k[x, y]/(xy)$, the pair of axes, $x$ and $y$ are not integral over each other's polynomial ring. The substitution of the proof with $r = 2$ is $z = x - y^2$. Then $0 = xy = (z + y^2)y = y^3 + zy$, a monic equation for $y$ over $k[z]$. So $A$ is finite over $k[z]$, and both axes map finitely onto the $z$-line. The simpler choice $z = x - y$ works too, since $y^2 + zy = 0$.

**Example P1.4.35 (failure over the integers).** The ring $\mathbb{Z}[1/2]$ is a finitely generated $\mathbb{Z}$-algebra and a domain of dimension $1$, but it is not finite over any polynomial ring $\mathbb{Z}[y_1, \dots, y_d]$. Its fraction field is $\mathbb{Q}$, so $d = 0$, and $1/2$ is not integral over $\mathbb{Z}$. Over $\mathbb{Z}$ the right form of Zariski's lemma is that a field which is a finitely generated $\mathbb{Z}$-algebra is a finite field (Exercise 4). The local ring $\mathbb{Z}_{(p)}$ is not a Jacobson ring: its zero ideal is prime, and the only maximal ideal is $(p)$.

### Exercises

1. (A) Find a Noether normalization of $k[x, y, z]/(xy - z^2)$ and of $k[x, y]/(x^2 y - 1)$.
2. (A) Use the dimension theorem to compute the dimension of $k[x, y, z, w]/(xw - yz)$, and, through its minimal primes, of $k[x, y, z]/(xy, xz)$.
3. (B) Deduce the strong Nullstellensatz from the Jacobson property: if $k$ is algebraically closed and $J \subseteq k[x_1, \dots, x_n]$, then the polynomials vanishing on $V(J) \subseteq k^n$ form $\sqrt{J}$.
4. (B) Show that $\mathbb{Z}$ is a Jacobson ring and that $k[[t]]$ is not. Show that a field $K$ that is a finitely generated $\mathbb{Z}$-algebra is finite. (Hint: if $\mathbb{Q} \subseteq K$, Zariski's lemma makes $K$ finite over $\mathbb{Q}$, and the Artin-Tate lemma of Section 3.2 makes $\mathbb{Q}$ a finitely generated $\mathbb{Z}$-algebra, which it is not.)
5. (B) Show that $\dim A/\mathfrak{p} + \operatorname{ht} \mathfrak{p} \leq \dim A$ for every ring $A$ and prime $\mathfrak{p}$. Show that $\dim A[x] = \dim A + 1$ when $A$ is a finitely generated $k$-domain. Chapter 5 proves equality in the first statement for finitely generated $k$-domains.
6. (C) Let $k$ be infinite and $A = k[x_1, \dots, x_n]/I$. Show that for a general linear change of coordinates, the images of the first $d$ coordinates give a Noether normalization. (Hint: replace $f$ by its top degree part and choose the coordinates so that it does not vanish at the point $(0, \dots, 0, 1)$.)

### Lean

Mathlib proves Noether normalization as `exists_integral_inj_algHom_of_fg` and `exists_finite_inj_algHom_of_fg`, with an injective algebra map from `MvPolynomial (Fin s) k`. Jacobson rings are `IsJacobsonRing`, and finitely generated algebras over a Jacobson ring are Jacobson by `isJacobsonRing_of_finiteType`. Zariski's lemma is `finite_of_finite_type_of_isJacobsonRing`. The finiteness of the integral closure appears as `IsIntegralClosure.finite` in the separable case. The handbook adds no `MinimalModel` node here.

### Notes and history

Emmy Noether proved the normalization lemma in 1926 and used it to prove that the integral closure of a finitely generated domain over a field is finite. The substitution $x_i - x_n^{r^i}$, which works over every field, is due to Nagata. Zariski proved his lemma in 1947 for a proof of the Nullstellensatz. Jacobson rings were introduced by Krull and by Goldman in 1951, under the name Hilbert rings. The literature state of every result here is theorem. The section follows Atiyah-Macdonald, Chapter 5, Matsumura, Chapter 2, and Eisenbud, Chapter 13.
