---
title: Dimension
nodes: []
sources: [Har77, Rei88, Sha13, Har92]
reads_with: [Har77:I.1, Rei88:ch6, Sha13:ch1, Har92:lecture11]
requires: [P0.3, P0.4, P0.5, P1.4, P1.5]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Dimension

### Statement

**Definition P0.6.1.** The *dimension* of a variety $X$ is the transcendence degree of its function field over $k$:

$$ \dim X = \operatorname{trdeg}_k k(X). $$

The dimension of an algebraic set is the largest dimension of its irreducible components. A variety of dimension $1$ is a *curve*, and a variety of dimension $2$ is a *surface*.

Lean: Mathlib `Algebra.trdeg` (the transcendence degree of an algebra, a cardinal).

**Example P0.6.2.** The function field of $\mathbb{A}^n$ is $k(x_1, \dots, x_n)$, and the variables are a transcendence basis, so $\dim \mathbb{A}^n = n$. The function field of $\mathbb{P}^n$ is $k(x_1/x_0, \dots, x_n/x_0)$, so $\dim \mathbb{P}^n = n$ as well. A point has function field $k$ and dimension $0$.

**Example P0.6.3.** Two birational varieties have the same dimension, because they have isomorphic function fields (Section 5.2). A nonempty open subset $U$ of a variety $X$ has $k(U) = k(X)$, so $\dim U = \dim X$. The cuspidal cubic $V(y^2 - x^3)$ has $k(C) = k(t)$ with $t = y/x$, so it is a curve.

**Definition P0.6.4.** The *topological dimension* of a topological space $Z$ is the supremum of the lengths $r$ of chains $Z_0 \subsetneq Z_1 \subsetneq \dots \subsetneq Z_r$ of irreducible closed subsets of $Z$. The *Krull dimension* of a ring $A$ is the supremum of the lengths $r$ of chains $\mathfrak{p}_0 \subsetneq \dots \subsetneq \mathfrak{p}_r$ of prime ideals of $A$.

Lean: Mathlib `ringKrullDim` (with values in `WithBot ℕ∞`).

**Example P0.6.5.** The Krull dimension of a field is $0$, and the Krull dimension of $k[x]$ is $1$: the chains of primes are $0 \subsetneq (x - a)$. The topological dimension of $\mathbb{A}^1$ is $1$, because its proper irreducible closed subsets are points.

**Example P0.6.6.** The Krull dimension of $k[x_1, \dots, x_n]$ is $n$ (P1 Ch. 5). The chain $0 \subsetneq (x_1) \subsetneq (x_1, x_2) \subsetneq \dots \subsetneq (x_1, \dots, x_n)$ shows that it is at least $n$.

**Theorem P0.6.7 (the three dimensions agree).** Let $X$ be an affine variety. Then the topological dimension of $X$, the Krull dimension of $k[X]$, and $\operatorname{trdeg}_k k(X)$ are equal. If $Y \subsetneq X$ is a proper closed subset, then $\dim Y < \dim X$.

Lean: Mathlib `MvPolynomial.ringKrullDim_of_isNoetherianRing_of_finite` gives the Krull dimension of a polynomial ring over a Noetherian ring; the equality with the transcendence degree for a general domain of finite type is not stated in this form.

*Proof.* The Nullstellensatz gives an inclusion reversing bijection between the irreducible closed subsets of $X$ and the prime ideals of $k[X]$ (Chapter 3). A chain of irreducible closed subsets of length $r$ corresponds to a chain of prime ideals of length $r$. So the topological dimension of $X$ is the Krull dimension of $k[X]$. The equality of the Krull dimension of a domain $B$ of finite type over $k$ with $\operatorname{trdeg}_k \operatorname{Frac}(B)$ is the main theorem of dimension theory in P1 Ch. 5, which uses Noether normalization (P1 Ch. 4). It is Hartshorne Theorem I.1.8A, and this proof cites it.

For the second claim, let $Y_0$ be an irreducible component of $Y$ with $\dim Y_0 = \dim Y = r$, and let $Z_0 \subsetneq \dots \subsetneq Z_r = Y_0$ be a chain of irreducible closed subsets of length $r$. Then $Z_0 \subsetneq \dots \subsetneq Z_r \subsetneq X$ is a chain of length $r + 1$ in $X$, so $\dim X \geq r + 1$. $\square$

For a projective variety $X$, each nonempty affine open subset has the same function field, so it has dimension $\dim X$.

**Theorem P0.6.8 (hypersurfaces).** A variety $Y \subset \mathbb{A}^n$ has dimension $n - 1$ if and only if $Y = V(f)$ for a nonconstant irreducible polynomial $f \in k[x_1, \dots, x_n]$. The same holds for a projective variety $Y \subset \mathbb{P}^n$ and a homogeneous irreducible $f$.

Lean: not in Lean; Mathlib has Krull's height theorem `Ideal.height_le_spanRank_toENat`, which gives the converse direction in the form "a minimal prime over a principal ideal has height at most $1$".

*Proof.* Let $f$ be nonconstant and irreducible. Then $(f)$ is a prime ideal, because $k[x_1, \dots, x_n]$ is a unique factorization domain, and $I(V(f)) = (f)$ by the Nullstellensatz. So $Y = V(f)$ is a variety with $k[Y] = k[x_1, \dots, x_n]/(f)$. Suppose that $x_n$ occurs in $f$, and let $\bar{x}_i$ be the image of $x_i$ in $k[Y]$. The elements $\bar{x}_1, \dots, \bar{x}_{n-1}$ are algebraically independent: if $g(\bar{x}_1, \dots, \bar{x}_{n-1}) = 0$, then $f$ divides $g(x_1, \dots, x_{n-1})$ in $k[x_1, \dots, x_n]$. A nonzero multiple $fh$ has positive degree in $x_n$, and $g$ has degree $0$ in $x_n$, so $g = 0$. The element $\bar{x}_n$ is algebraic over $k(\bar{x}_1, \dots, \bar{x}_{n-1})$, because $f(\bar{x}_1, \dots, \bar{x}_n) = 0$ and $f$ has positive degree in $x_n$. So $\bar{x}_1, \dots, \bar{x}_{n-1}$ is a transcendence basis of $k(Y)$, and $\dim Y = n - 1$.

Conversely, let $Y$ be a variety of dimension $n - 1$. Then $Y \neq \mathbb{A}^n$, so $I(Y)$ contains a nonzero polynomial $g$. The ideal $I(Y)$ is prime, so it contains an irreducible factor $f$ of $g$, and $f$ is not constant. So $Y \subset V(f)$. Both are varieties of dimension $n - 1$, so $Y = V(f)$ by the theorem above.

For $Y \subset \mathbb{P}^n$, choose $i$ with $Y \not\subset V(x_i)$. The affine piece $Y_i = Y \cap \{x_i \neq 0\}$ is a dense open subset of $Y$, so $\dim Y_i = \dim Y$. If $Y = V(f)$ with $f$ homogeneous and irreducible, then $f \neq c x_i$, the dehomogenization $g$ of $f$ with respect to $x_i$ is irreducible, and $Y_i = V(g)$, so $\dim Y = n - 1$. If $\dim Y = n - 1$, then $Y_i = V(g)$ with $g$ irreducible by the affine case, and $Y$ is the closure of $Y_i$, which is $V(f)$ for the homogenization $f$ of $g$ (Chapter 4). $\square$

### Proof in words

Dimension has three faces: the number of independent rational functions, the length of chains of subvarieties, and the length of chains of primes. The Nullstellensatz identifies the last two at once. The identification with the transcendence degree is the real theorem, and it needs Noether normalization, so this section cites it from P1. For a hypersurface the transcendence degree is visible: $n - 1$ of the coordinates are free, and the last one satisfies the equation $f = 0$.

### Examples

**Example P0.6.9.** The affine twisted cubic $C = \{(t, t^2, t^3)\} \subset \mathbb{A}^3$ is the image of the morphism $\mathbb{A}^1 \to \mathbb{A}^3$, $t \mapsto (t, t^2, t^3)$. Its ideal is $I(C) = (y - x^2, z - x^3)$: modulo this ideal every polynomial $g(x, y, z)$ is congruent to $g(x, x^2, x^3)$, and this vanishes on $C$ only if it is zero. So $k[C] \cong k[x]$, $k(C) = k(x)$ and $\dim C = 1$. By the hypersurface theorem, $C$ is not $V(f)$ for any single polynomial $f$, because $V(f)$ has dimension $2$ or is empty or $\mathbb{A}^3$.

**Example P0.6.10.** The hypothesis "irreducible" cannot be dropped. Let $f = xy \in k[x, y]$. Then $V(f)$ is the union of the two axes. It is not a variety, $k[x, y]/(xy)$ is not a domain, and there is no function field. Each component has dimension $1$, so the dimension of the algebraic set is $1$, but the conclusion "$V(f)$ is a variety" fails. For $f = x^2$, which is not irreducible, $V(f) = V(x)$ is a variety, but $I(V(f)) = (x) \neq (f)$.

### Exercises

1. (A) Show that $\dim \mathbb{P}^n = n$ by computing the transcendence degree of $k(x_1/x_0, \dots, x_n/x_0)$.
2. (A) Let $\operatorname{char} k \neq 2$. Show that $x^2 + y^2 + z^2 - 1$ is irreducible, and that the sphere $V(x^2 + y^2 + z^2 - 1) \subset \mathbb{A}^3$ is a surface.
3. (A) Show that the twisted cubic $\{(s^3 : s^2 t : s t^2 : t^3)\} \subset \mathbb{P}^3$ is a curve, and that it is not the zero set of one homogeneous polynomial.
4. (B) Let $X$ and $Y$ be affine varieties. Show that $X \times Y$ is a variety with $\dim (X \times Y) = \dim X + \dim Y$. Use $k[X \times Y] = k[X] \otimes_k k[Y]$ and transcendence bases.
5. (B) Let $Y \subset \mathbb{A}^3$ be the image of $t \mapsto (t^3, t^4, t^5)$. Show that $y^2 - xz$, $x^3 - yz$ and $z^2 - x^2 y$ lie in $I(Y)$, that $\dim Y = 1$, and that $I(Y)$ is a prime ideal of height $2$. Show that $I(Y)$ cannot be generated by two elements (Hartshorne, Ex. I.1.11).

### Lean

Mathlib has `Algebra.trdeg`, `ringKrullDim`, and the Krull dimension of polynomial rings over Noetherian rings, `MvPolynomial.ringKrullDim_of_isNoetherianRing_of_finite`. It has Krull's height theorem, `Ideal.height_le_spanRank_toENat`. The equality of the Krull dimension and the transcendence degree for domains of finite type over a field is not stated in Mathlib in this form.

### Notes and history

Krull defined the dimension of a ring by chains of prime ideals in the 1930s. The definition by transcendence degree is older and goes back to the algebraic geometry of the nineteenth century. Hartshorne gives the three definitions in Section I.1 and proves the hypersurface theorem as Proposition I.1.13, with a different proof of the converse that uses Krull's principal ideal theorem. The literature state is theorem. P3 Ch. 7 extends dimension to schemes. Every later volume uses dimension. For example, a divisorial contraction in Volume 1 contracts a prime divisor, a subvariety of dimension $\dim X - 1$.
