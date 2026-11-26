---
title: Hilbert's Nullstellensatz
nodes: []
sources: [Rei88, Har77, AM69]
reads_with: [Rei88:ch3, Har77:I.1, AM69:ch5, AM69:ch7]
requires: [P1.4, P0.3]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Hilbert's Nullstellensatz

### Statement

The proof uses two facts of commutative algebra from P1 Chapter 4. Both hold over any field $k$.

- **Noether normalization.** Let $A$ be a finitely generated $k$-algebra. Then there are elements $y_1, \dots, y_d \in A$, algebraically independent over $k$, such that $A$ is a finitely generated module over $k[y_1, \dots, y_d]$.
- **Fields in integral extensions.** Let $A \subseteq B$ be integral domains with $B$ integral over $A$. Then $B$ is a field if and only if $A$ is a field (Atiyah-Macdonald, Chapter 5).

**Lemma P0.3.11 (Zariski).** Let $k$ be any field, and let $K$ be a field that is a finitely generated $k$-algebra. Then $K$ is a finite extension of $k$. If $k$ is algebraically closed, then $k \to K$ is an isomorphism.

Lean: not in Lean as stated; Mathlib has Noether normalization as `exists_integral_inj_algHom_of_fg`.

*Proof.* By Noether normalization there are $y_1, \dots, y_d \in K$, algebraically independent, with $K$ finite over $R = k[y_1, \dots, y_d]$. A finite module is integral, so by the second fact $R$ is a field. If $d \geq 1$, then $y_1$ has no inverse in $R$, because $y_1 g = 1$ fails for degree reasons. So $d = 0$ and $K$ is a finite $k$-module. If $k$ is algebraically closed, each $\alpha \in K$ is algebraic over $k$, so its minimal polynomial is linear and $\alpha \in k$. $\square$

**Theorem P0.3.12 (weak Nullstellensatz).** Let $k$ be algebraically closed.

1. The maximal ideals of $k[x_1, \dots, x_n]$ are exactly the ideals $\mathfrak{m}_a = (x_1 - a_1, \dots, x_n - a_n)$ for $a \in \mathbb{A}^n$.
2. If $J \subseteq k[x_1, \dots, x_n]$ is an ideal and $J \neq (1)$, then $V(J) \neq \emptyset$.

Lean: Mathlib `MvPolynomial.isMaximal_iff_eq_vanishingIdeal_singleton` (proved in Mathlib, for `K` algebraically closed and `σ` finite).

*Proof.* The ideal $\mathfrak{m}_a$ is the kernel of the evaluation $f \mapsto f(a)$, which maps onto $k$. So $k[x_1, \dots, x_n] / \mathfrak{m}_a \cong k$ and $\mathfrak{m}_a$ is maximal. Let $\mathfrak{m}$ be any maximal ideal. The field $K = k[x_1, \dots, x_n]/\mathfrak{m}$ is a finitely generated $k$-algebra, so $k \to K$ is an isomorphism by Zariski's lemma. Let $a_i \in k$ be the element with the same image as $x_i$ in $K$. Then $x_i - a_i \in \mathfrak{m}$ for each $i$, so $\mathfrak{m}_a \subseteq \mathfrak{m}$. Since $\mathfrak{m}_a$ is maximal, $\mathfrak{m}_a = \mathfrak{m}$. This proves 1. For 2, a proper ideal $J$ lies in a maximal ideal, because the ring is Noetherian. By 1 this ideal is $\mathfrak{m}_a$ for some $a$. Each $f \in J$ is in $\mathfrak{m}_a$, so $f(a) = 0$, and $a \in V(J)$. $\square$

**Theorem P0.3.13 (Nullstellensatz).** Let $k$ be algebraically closed and let $J \subseteq k[x_1, \dots, x_n]$ be an ideal. Then $I(V(J)) = \sqrt{J}$.

Lean: Mathlib `MvPolynomial.vanishingIdeal_zeroLocus_eq_radical` (proved in Mathlib, for `K` algebraically closed and `σ` finite).

*Proof.* If $f^m \in J$ then $f^m$ vanishes on $V(J)$, so $f$ does. So $\sqrt{J} \subseteq I(V(J))$. Conversely let $f \in I(V(J))$. If $f = 0$ there is nothing to prove. By the Hilbert basis theorem $J = (f_1, \dots, f_r)$. In $k[x_1, \dots, x_n, t]$ consider the ideal $J' = (f_1, \dots, f_r, 1 - t f)$. Its zero set in $\mathbb{A}^{n+1}$ is empty: at a common zero $(a, b)$ of $f_1, \dots, f_r$ the point $a$ lies in $V(J)$, so $f(a) = 0$ and $1 - b f(a) = 1$. By the weak Nullstellensatz $J' = (1)$, so

$$1 = \sum_{i=1}^r g_i(x, t) f_i(x) + g_0(x, t)\,(1 - t f(x))$$

for some polynomials $g_0, \dots, g_r$. Substitute $t = 1/f$ in the field $k(x_1, \dots, x_n)$. The last term becomes $0$. Multiply by $f^N$, with $N$ the largest power of $t$ in the $g_i$. This gives $f^N = \sum_i h_i f_i$ with $h_i = f^N g_i(x, 1/f) \in k[x_1, \dots, x_n]$. So $f^N \in J$ and $f \in \sqrt{J}$. $\square$

**Corollary P0.3.14.** Over an algebraically closed field, $V(J) = \emptyset$ if and only if $J = (1)$. Polynomials $f_1, \dots, f_r$ have no common zero if and only if $\sum g_i f_i = 1$ for some polynomials $g_i$.

Lean: not in Lean as stated; it follows from `MvPolynomial.vanishingIdeal_zeroLocus_eq_radical` in one step.

### Proof in words

The weak form is the heart. A maximal ideal gives a field $K$ that is finitely generated as a $k$-algebra. Zariski's lemma says that such a field is algebraic over $k$, so it is $k$ itself, and the images of the coordinates give a point. The difficulty is in Zariski's lemma: a finitely generated algebra can be a field only when it has no transcendental elements. Noether normalization reduces this to a polynomial ring, which is not a field.

The strong form follows by the trick of Rabinowitsch. A polynomial $f$ that vanishes on $V(J)$ makes the system $f_1 = \dots = f_r = 0$, $tf = 1$ have no solution. The weak form then writes $1$ in terms of these equations, and clearing the denominators of $t = 1/f$ shows that a power of $f$ lies in $J$.

### Examples

Take $J = (y - x^2, y) \subset k[x, y]$. A common zero has $y = 0$ and then $x^2 = 0$, so $V(J) = \{(0, 0)\}$ and $I(V(J)) = (x, y)$. The ideal is $J = (y, x^2)$, and $\sqrt{J} = (x, y)$, because $x^2 \in J$ and $(x, y)$ is maximal. The two sides agree, as the theorem says. The ideal $J$ itself is not radical: $x \notin J$. Geometrically, the parabola $y = x^2$ meets the line $y = 0$ at one point with multiplicity 2, and $J$ remembers the multiplicity.

A failure when $k$ is not algebraically closed: in $\mathbb{R}[x]$ the ideal $(x^2 + 1)$ is maximal and $\mathbb{R}[x]/(x^2 + 1) \cong \mathbb{C}$. It is not of the form $(x - a)$, and $V(x^2 + 1) = \emptyset$ in $\mathbb{R}$ although $(x^2 + 1) \neq (1)$. Both parts of the weak Nullstellensatz fail. Zariski's lemma still holds: $\mathbb{C}$ is finite over $\mathbb{R}$, but it is not $\mathbb{R}$.

### Exercises

1. (A) Find $\sqrt{J}$ and $V(J)$ for $J = (x^2 y, x y^2) \subset k[x, y]$, and check that $I(V(J)) = \sqrt{J}$.
2. (A) Show that the polynomials $x^2 + y^2 - 1$ and $x - 2$ have common zeros over $\mathbb{C}$ but not over $\mathbb{R}$. Explain which step of the proof of the weak Nullstellensatz fails over $\mathbb{R}$.
3. (A) Show that the field $k(t)$ of rational functions is not a finitely generated $k$-algebra. (Hint: Zariski's lemma.)
4. (B) Let $k$ be algebraically closed and let $f, g \in k[x, y]$ have no common factor. Show that $V(f, g)$ is finite. (Hint: in $k(x)[y]$ write $1 = a f + b g$ and clear denominators to get a nonzero polynomial in $x$ alone in $(f, g)$.)
5. (B) Let $k$ be uncountable and algebraically closed. Prove the weak Nullstellensatz without Noether normalization: show that $K = k[x_1, \dots, x_n]/\mathfrak{m}$ has countable dimension over $k$, and that $\{1/(t - c) : c \in k\}$ is linearly independent in $k(t)$.
6. (B) Show that an ideal $J$ of $k[x_1, \dots, x_n]$ is the ideal $I(X)$ of some subset $X$ if and only if $J$ is radical.

### Lean

Mathlib proves both forms of the Nullstellensatz for polynomial rings in finitely many variables over a field $k$, with points in an algebraically closed extension $K$. The names are `MvPolynomial.isMaximal_iff_eq_vanishingIdeal_singleton` and `MvPolynomial.vanishingIdeal_zeroLocus_eq_radical`. Noether normalization is `exists_integral_inj_algHom_of_fg`. The handbook uses these Mathlib names and adds no `MinimalModel` node here.

### Notes and history

Hilbert proved the Nullstellensatz in 1893 in his paper on the invariants of forms. The literature state is theorem. The trick with the extra variable $t$ is due to Rabinowitsch (1929). Zariski proved his lemma in 1947, and the proof by Noether normalization is the one of Atiyah-Macdonald. Exercise 5 is the short proof for uncountable fields, for example $k = \mathbb{C}$. In the language of P1 Chapter 4, the Nullstellensatz says that $k[x_1, \dots, x_n]$ is a Jacobson ring. P3 uses this to show that the closed points of a scheme of finite type over $k$ are dense.
