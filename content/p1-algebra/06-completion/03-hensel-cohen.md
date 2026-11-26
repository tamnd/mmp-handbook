---
title: Hensel's lemma and the Cohen structure theorem
nodes: []
sources: [AM69, Mat86, Eis95]
reads_with: [AM69:ch10, Mat86:ch3, Eis95:ch7]
requires: [P1.1, P1.5]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Hensel's lemma and the Cohen structure theorem

### Statement

Throughout, $(A, \mathfrak{m}, k)$ is a *complete local ring*: a Noetherian local ring with $A = \hat{A}$ for the $\mathfrak{m}$-adic completion. Then $\mathfrak{m}^n$ is the kernel of $A \to A/\mathfrak{m}^n$, every compatible sequence of classes modulo the $\mathfrak{m}^n$ comes from a unique element of $A$, and $\bigcap_n \mathfrak{m}^n = 0$ (Sections 6.1 and 6.2). For $a \in A$ write $\bar{a}$ for its class in $k$, and for $f \in A[x]$ write $\bar{f} \in k[x]$.

**Theorem P1.6.23 (Hensel's lemma).** Let $f \in A[x]$ and $a_0 \in A$ with $f(a_0) \in \mathfrak{m}$ and $f'(a_0) \notin \mathfrak{m}$. Then there is a unique $a \in A$ with $f(a) = 0$ and $a \equiv a_0 \pmod{\mathfrak{m}}$.

Lean: Mathlib `HenselianLocalRing` and `HenselianRing` (definitions), with the instance `IsAdicComplete.henselianRing` for monic polynomials over any adically complete ring, and `hensels_lemma` for $\mathbb{Z}_p$ (proved in Mathlib).

*Proof.* By the Taylor formula there is $G \in A[x, h]$ with $f(x + h) = f(x) + f'(x) h + h^2 G(x, h)$. Define $a_{n+1} = a_n - f(a_n)/f'(a_n)$. By induction on $n$: $a_n \equiv a_0 \pmod{\mathfrak{m}}$, so $f'(a_n) \equiv f'(a_0) \pmod{\mathfrak{m}}$ is a unit and $a_{n+1}$ is defined; and $f(a_n) \in \mathfrak{m}^{2^n}$. Both hold for $n = 0$. If they hold for $n$, then $h = -f(a_n)/f'(a_n) \in \mathfrak{m}^{2^n}$, so $a_{n+1} \equiv a_n \pmod{\mathfrak{m}^{2^n}}$, and
$$
f(a_{n+1}) = f(a_n) + f'(a_n) h + h^2 G(a_n, h) = h^2 G(a_n, h) \in \mathfrak{m}^{2^{n+1}} .
$$
The classes of the $a_n$ modulo $\mathfrak{m}^{2^n}$ are compatible, so there is $a \in A$ with $a \equiv a_n \pmod{\mathfrak{m}^{2^n}}$ for all $n$. Then $f(a) \equiv f(a_n) \equiv 0 \pmod{\mathfrak{m}^{2^n}}$ for all $n$, so $f(a) = 0$, and $a \equiv a_0 \pmod{\mathfrak{m}}$.

If $b$ is another root with $b \equiv a_0$, then $0 = f(b) - f(a) = (b - a)\big(f'(a) + (b - a) G(a, b - a)\big)$. The second factor is congruent to $f'(a)$ modulo $\mathfrak{m}$, so it is a unit, and $b = a$. $\square$

**Theorem P1.6.24 (Hensel's lemma, factorization form).** Let $f \in A[x]$ be monic, and suppose $\bar{f} = g_0 h_0$ with $g_0, h_0 \in k[x]$ monic and coprime. Then there are monic $g, h \in A[x]$ with $f = gh$, $\bar{g} = g_0$ and $\bar{h} = h_0$.

Lean: not in Lean in this form.

*Proof sketch.* Construct monic $g_n, h_n$ that lift $g_0, h_0$, with $\deg g_n = \deg g_0$, $\deg h_n = \deg h_0$ and $f \equiv g_n h_n$ modulo $\mathfrak{m}^n A[x]$. Given them, $e = f - g_n h_n$ has coefficients in $\mathfrak{m}^n$ and degree less than $\deg f$. Since $g_0$ and $h_0$ are coprime, every polynomial over $k$ of degree less than $\deg f$ is $u_0 g_0 + v_0 h_0$ with $\deg u_0 < \deg h_0$ and $\deg v_0 < \deg g_0$. Applying this to the coefficients of $e$ in a basis of the $k$-vector space $\mathfrak{m}^n/\mathfrak{m}^{n+1}$ gives $u, v$ with coefficients in $\mathfrak{m}^n$ and $e \equiv u g_n + v h_n$ modulo $\mathfrak{m}^{n+1}A[x]$. Then $g_{n+1} = g_n + v$ and $h_{n+1} = h_n + u$ work, since $uv$ has coefficients in $\mathfrak{m}^{2n}$. The coefficients of $g_n$ and $h_n$ converge, and the limits $g$ and $h$ satisfy $f = gh$. Eisenbud, Chapter 7, gives the details. $\square$

A local ring that satisfies the conclusion of the first theorem, for monic $f$, is called *Henselian*. So every complete local ring is Henselian. The local ring of a variety at a point is not Henselian in general (Exercise 7).

**Lemma P1.6.25 (formal inverse function theorem).** Let $K$ be a field, $B = K[[x_1, \dots, x_n]]$ with maximal ideal $\mathfrak{n}$, and let $f_1, \dots, f_n \in \mathfrak{n}$ have linearly independent linear parts. Then the substitution $\varphi: B \to B$, $\varphi(F) = F(f_1, \dots, f_n)$, is an automorphism.

Lean: not in Lean.

*Proof.* The substitution is defined, since $f_i \in \mathfrak{n}$ makes each coefficient of $F(f_1, \dots, f_n)$ a finite sum, and it is a ring homomorphism with $\varphi(\mathfrak{n}^j) \subseteq \mathfrak{n}^j$. On $\mathfrak{n}^j/\mathfrak{n}^{j+1}$, the forms of degree $j$, it induces the linear change of variables given by the linear parts of the $f_i$, which is bijective. If $\varphi(F) = 0$ with $F \neq 0$, let $F_j$ be the lowest form of $F$. Then the form of degree $j$ of $\varphi(F)$ is the image of $F_j$, which is not $0$; a contradiction. For the surjectivity, let $G \in B$. Choose forms $F_0, F_1, \dots$ one degree at a time, so that $G - \varphi(F_0 + \dots + F_j) \in \mathfrak{n}^{j+1}$: this is possible since $\varphi$ is bijective on each $\mathfrak{n}^j/\mathfrak{n}^{j+1}$. Then $F = \sum_j F_j$ satisfies $G - \varphi(F) \in \mathfrak{n}^{j+1}$ for all $j$, so $\varphi(F) = G$. $\square$

**Definition P1.6.26 (coefficient field).** A *coefficient field* of $A$ is a subfield $K \subseteq A$ that maps isomorphically onto $k$ under $A \to k$.

Lean: not in Lean.

**Theorem P1.6.27 (Cohen structure theorem).** Let $(A, \mathfrak{m}, k)$ be a complete local ring.

1. If $A$ contains a field, then $A$ has a coefficient field $K$. For every set of generators $y_1, \dots, y_n$ of $\mathfrak{m}$ there is a surjective homomorphism $K[[x_1, \dots, x_n]] \to A$ with $x_i \mapsto y_i$. So $A \cong K[[x_1, \dots, x_n]]/J$.
2. In general, $A$ is a quotient of a power series ring $R[[x_1, \dots, x_n]]$, where $R$ is a field or a complete discrete valuation ring with maximal ideal $pR$, $p = \operatorname{char} k$.

Lean: not in Lean.

*Proof of (1) when $k$ has characteristic $0$.* A field contained in $A$ meets $\mathfrak{m}$ only in $0$, so it maps injectively to $k$, and $\operatorname{char} k = 0$ means that $A$ contains $\mathbb{Q}$. By Zorn's lemma, there is a maximal subfield $K \subseteq A$: the union of a chain of subfields is a subfield. Let $\bar{K} \subseteq k$ be its image.

First, $k$ is algebraic over $\bar{K}$. Otherwise let $\bar{t} \in k$ be transcendental over $\bar{K}$ and $t \in A$ a lift. For $0 \neq g \in K[x]$, the image $\bar{g}(\bar{t}) \neq 0$, so $g(t) \notin \mathfrak{m}$ is a unit. So $K(t) \subseteq A$, which contradicts the maximality of $K$.

Next, $\bar{K} = k$. Otherwise let $\bar{\alpha} \in k \setminus \bar{K}$, with minimal polynomial $p_0$ over $\bar{K}$, and let $p \in K[x]$ be the monic polynomial with $\bar{p} = p_0$. It is irreducible over $K$, since $K \cong \bar{K}$. In characteristic $0$ the root $\bar{\alpha}$ of $p_0$ is simple, so Hensel's lemma gives $\alpha \in A$ with $p(\alpha) = 0$ and $\bar{\alpha}$ as its class. Then $K[\alpha] \cong K[x]/(p)$ is a field in $A$ that is larger than $K$, a contradiction. So $K$ is a coefficient field.

Now let $y_1, \dots, y_n$ generate $\mathfrak{m}$. The substitution $\Phi(F) = F(y_1, \dots, y_n)$ is defined on $K[[x_1, \dots, x_n]]$ as in the theorem on the Noetherian property in Section 6.2, since $A$ is complete. Since $A = K + \mathfrak{m}$, the $k$-vector space $\mathfrak{m}^j/\mathfrak{m}^{j+1}$ is spanned by the classes of the monomials of degree $j$ in the $y_i$, with coefficients that can be taken in $K$. So for $a \in A$ there are forms $F_j \in K[x_1, \dots, x_n]$ of degree $j$, chosen one degree at a time, with $a - \sum_{j < m} F_j(y) \in \mathfrak{m}^m$ for all $m$. Then $\Phi(\sum_j F_j) = a$. $\square$

*Sketch for the remaining cases.* In characteristic $p$ a maximal subfield need not be a coefficient field when $k$ is not perfect, since Hensel's lemma does not apply to inseparable polynomials, and the proof chooses a $p$-basis of $k$ and lifts it. When $A$ contains no field, the ring $R$ of (2) is a Cohen ring, a complete discrete valuation ring with maximal ideal $pR$ and residue field $k$, such as $\mathbb{Z}_p$ for $k = \mathbb{F}_p$. Cohen proved both parts in 1946. Eisenbud, Chapter 7, gives the proofs.

**Corollary P1.6.28 (complete local rings of the expected size).** Let $(A, \mathfrak{m}, k)$ be a complete local ring that contains a field, with $\dim A = \dim_k \mathfrak{m}/\mathfrak{m}^2 = n$. Then $A \cong k[[x_1, \dots, x_n]]$.

Lean: not in Lean.

*Proof.* By Corollary P1.1.26, $\mathfrak{m}$ has $n$ generators, so the Cohen structure theorem gives $A \cong K[[x_1, \dots, x_n]]/J$ with $K \cong k$. The ring $B = K[[x_1, \dots, x_n]]$ is a domain (Exercise 1) of dimension $n$ (Corollary P1.5.36). If $J \neq 0$, take $0 \neq f \in J$. It is a nonzerodivisor in $B$, so $\dim B/(f) = n - 1$ by the corollary on systems of parameters in Section 5.2, and $\dim A \leq \dim B/(f) = n - 1$, a contradiction. So $J = 0$. $\square$

The local rings with $\dim A = \dim_k \mathfrak{m}/\mathfrak{m}^2$ are the regular local rings of Chapter 9. By the theorem on completions of local rings in Section 6.2, $A$ is regular if and only if $\hat{A}$ is, so the completion of a regular local ring that contains a field is a power series ring.

### Proof in words

Hensel's lemma is Newton's method. A simple root modulo $\mathfrak{m}$ is an approximate root, and the Newton step $a \mapsto a - f(a)/f'(a)$ doubles the order of approximation, because the error after the step is the square of the error before it. In a complete ring the approximations converge to a root. The factorization form is the same idea for factors of a polynomial, with the coprimality of the factors in the role of the unit $f'(a_0)$.

The Cohen structure theorem says that every complete local ring that contains a field is a power series ring modulo an ideal. The coefficient field is the hard part. In characteristic zero a maximal subfield is a coefficient field: a transcendental element of the residue field lifts freely, and an algebraic one lifts by Hensel's lemma, since its minimal polynomial is separable. Once the coefficient field is there, every element is a power series in the generators of $\mathfrak{m}$, by approximation degree by degree.

For the geometry, the completion of the local ring at a point $p$ of a variety $X$ is the ring of formal functions near $p$, and $\hat{\mathcal{O}}_{X, p} \cong k[[x_1, \dots, x_n]]/J$ is a formal embedding of $X$ near $p$ in affine $n$-space. Over the complex numbers, the completion of the analytic local ring is the same ring. Two points with isomorphic completions have the same singularity in the analytic sense. Artin's approximation theorem of 1969 says that for varieties over a field, an isomorphism of completions comes from a common étale neighbourhood. This is why the minimal model program can classify singularities by normal forms in power series: the $A_n$ singularity is any surface point whose completion is $k[[x, y, z]]/(xy - z^{n+1})$, and the terminal threefold singularities of Volume 4 are classified up to analytic isomorphism.

### Examples

**Example P1.6.29 (square roots).** Let $p$ be an odd prime and $u \in \mathbb{Z}_p$ a unit. If $\bar{u}$ is a square in $\mathbb{F}_p$, say $\bar{u} = \bar{b}^2$, then Hensel's lemma for $f = x^2 - u$ and $a_0 = b$ applies, since $f'(b) = 2b$ is a unit. So $u$ is a square in $\mathbb{Z}_p$ if and only if $\bar{u}$ is a square in $\mathbb{F}_p$. For example $2 \equiv 3^2 \pmod 7$, so $\sqrt{2} \in \mathbb{Z}_7$, and $-1 \equiv 2^2 \pmod 5$, so $\sqrt{-1} \in \mathbb{Z}_5$. In the same way, if $\operatorname{char} k \neq 2$, then $1 + x$ has a square root in $k[[x]]$, the binomial series $\sqrt{1 + x} = 1 + x/2 - x^2/8 + \dots$.

**Example P1.6.30 (the node is analytically two lines).** Let $\operatorname{char} k \neq 2$ and $A = k[x, y]_{(x, y)}/(y^2 - x^2 - x^3)$, the local ring of the nodal cubic at the node. It is a domain, since $y^2 - x^2 - x^3$ is irreducible in $k[x, y]$. Its completion is $\hat{A} = k[[x, y]]/(y^2 - x^2(1 + x))$ (Section 6.2). Let $u = \sqrt{1 + x} \in k[[x]]$. Then
$$
y^2 - x^2(1 + x) = (y - xu)(y + xu) .
$$
The series $s = y - xu$ and $t = y + xu$ have linear parts $y - x$ and $y + x$, which are linearly independent since $\operatorname{char} k \neq 2$. By the formal inverse function theorem, $s$ and $t$ are formal coordinates: $k[[x, y]] = k[[s, t]]$. So $\hat{A} \cong k[[s, t]]/(st)$, the completed local ring of the pair of axes. It has two minimal primes, $(s)$ and $(t)$, the two branches of the node. The node is *analytically reducible*: irreducible in the Zariski topology, but with two branches in the formal neighbourhood. The two branches are the two points of the normalization over the node in Example P1.4.23.

**Example P1.6.31 (the cusp is analytically irreducible).** For the cusp $y^2 = x^3$, the completion is $k[[x, y]]/(y^2 - x^3) \cong k[[t^2, t^3]] \subseteq k[[t]]$ (Exercise 4 of Section 6.2), which is a domain. The cusp has one branch. The normalization is a bijection over the cusp, as in Example P1.4.24.

**Example P1.6.32 (the completion forgets global data).** Let $k$ be algebraically closed, let $p$ be a point of $\mathbb{P}^1$ and $q$ a point of a smooth plane cubic $E$. Both local rings are discrete valuation rings with residue field $k$, of dimension $1$ and embedding dimension $1$, and they contain $k$. By the corollary, both completions are isomorphic to $k[[t]]$. But the local rings are not isomorphic: their fraction fields are $k(\mathbb{P}^1) = k(t)$ and $k(E)$, and $E$ is not rational, since it has genus $1$. So a smooth point of a curve has no analytic invariants, while the Zariski local ring still remembers the function field.

### Exercises

1. (A) Show that $K[[x_1, \dots, x_n]]$ is a domain: the lowest form of a product is the product of the lowest forms. Show that $x_1$ is a prime element.
2. (A) Decide which of $2$, $3$, $5$ and $6$ are squares in $\mathbb{Z}_7$.
3. (A) Show that $x^3 - 2$ has exactly one root in $\mathbb{Z}_5$.
4. (A) Let $\operatorname{char} k \nmid n$. Show that a unit $u \in k[[x_1, \dots, x_m]]$ is an $n$-th power if and only if $u(0)$ is an $n$-th power in $k$.
5. (B) Let $\operatorname{char} k \neq 2$. Show that $k[[x, y, z]]/(x^2 + y^2 + z^2 + z^3)$ is isomorphic to $k[[x, y, w]]/(x^2 + y^2 + w^2)$. If $k$ contains $\sqrt{-1}$, show that it is also isomorphic to $k[[u, v, w]]/(uv - w^2)$, the completed local ring of the quadric cone.
6. (B) Let $\operatorname{char} k \neq 2$, and let $\hat{A} = k[[x, y]]/(y^2 - x^2 - x^3)$. Show that the normalization of $\hat{A}$, the integral closure in its total ring of fractions, is $k[[s]] \times k[[t]]$.
7. (B) Let $\operatorname{char} k \neq 2$ and $A = k[x]_{(x)}$. Show that $y^2 - (1 + x)$ has a simple root modulo $\mathfrak{m}$ but no root in $A$, so $A$ is not Henselian.
8. (C) Prove the factorization form of Hensel's lemma in full, and deduce it from the first form when $g_0$ has degree $1$.

### Lean

Mathlib defines Henselian rings by the root lifting property, `HenselianRing` and `HenselianLocalRing`, and proves that a ring that is adically complete along an ideal is Henselian at it, `IsAdicComplete.henselianRing`, by the Newton iteration used here. For the $p$-adic integers it has the sharper `hensels_lemma`, with norms in place of the maximal ideal. Coefficient fields, Cohen rings and the Cohen structure theorem are not in Mathlib. The handbook adds no `MinimalModel` node here.

### Notes and history

Hensel's lemma is named after Hensel, who used it in his theory of $p$-adic numbers, and Newton's method is much older. Cohen, a student of Zariski, proved the structure theorem for complete local rings in 1946. Artin proved his approximation theorem in 1969, and it is the reason that étale local and formal local properties of varieties agree. The literature state of every result here is theorem. The section follows Atiyah-Macdonald, Chapter 10, Matsumura, Chapter 3, and Eisenbud, Chapter 7.
