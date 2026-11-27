---
title: The cohomology of O(n) on projective space
nodes: []
sources: [Har77, Vak25, Ser55, Stacks]
reads_with: [Har77:III.5, Vak25:ch18]
requires: [P2.7, P3.4, P3.6, P3.12, P4.1]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The cohomology of O(n) on projective space

### Statement

Let $A$ be a ring, $r \geq 1$, $S = A[x_0, \dots, x_r]$ with the standard grading and $X = \mathbb{P}^r_A = \operatorname{Proj} S$. For $a = (a_0, \dots, a_r) \in \mathbb{Z}^{r+1}$ write $x^a = x_0^{a_0} \cdots x_r^{a_r}$ and $|a| = a_0 + \dots + a_r$. For a subset $I \subseteq \{0, \dots, r\}$ write $x_I = \prod_{i \in I} x_i$. The localization $S_{x_I}$ is a free $A$-module with basis the monomials $x^a$ with $a_i \geq 0$ for $i \notin I$, graded by $|a|$.

**Theorem P4.2.1 (Serre).** In this situation:

1. The map $S_n \to H^0(X, \mathcal{O}(n))$ is an isomorphism for every $n \in \mathbb{Z}$.
2. $H^r(X, \mathcal{O}(n))$ is a free $A$-module with basis the classes of the monomials $x^a$ with $a_i \leq -1$ for all $i$ and $|a| = n$. In particular $H^r(X, \mathcal{O}(n)) = 0$ for $n > -r-1$, and $H^r(X, \mathcal{O}(-r-1))$ is free of rank one with basis the class of $(x_0 \cdots x_r)^{-1}$.
3. $H^p(X, \mathcal{O}(n)) = 0$ for $p \neq 0, r$ and every $n$.
4. For $n \geq 0$ the multiplication pairing
$$H^0(X, \mathcal{O}(n)) \times H^r(X, \mathcal{O}(-n-r-1)) \to H^r(X, \mathcal{O}(-r-1)) \cong A$$
is a perfect pairing of free $A$-modules of finite rank: the basis $x^b$, $b_i \geq 0$, $|b| = n$, of the first is dual to the basis $x^{-b - (1, \dots, 1)}$ of the second.

All these isomorphisms are compatible with base change along any ring map $A \to B$.

Lean: not in Lean as stated.

The pairing in part 4 is defined on the Čech complex in the proof. It is the cup product with a global section, and Chapter 7 makes it the first case of Serre duality, with $\mathcal{O}(-r-1) \cong \omega_X$ by Corollary P3.12.22.

**Corollary P4.2.2 (dimensions).** Let $k$ be a field and $X = \mathbb{P}^r_k$. Then
$$h^0(X, \mathcal{O}(n)) = \binom{n + r}{r} \text{ for } n \geq 0, \qquad h^r(X, \mathcal{O}(n)) = \binom{-n-1}{r} \text{ for } n \leq -r-1,$$
and all other $h^p(X, \mathcal{O}(n))$ vanish. For every $n \in \mathbb{Z}$,
$$\sum_p (-1)^p h^p(X, \mathcal{O}(n)) = \frac{(n+r)(n+r-1) \cdots (n+1)}{r!}.$$

Lean: not in Lean as stated.

The right side of the last formula is a polynomial in $n$ of degree $r$ that agrees with the dimension of $S_n$ for $n \geq 0$. Chapter 3 shows that this is the general pattern: the alternating sum of the dimensions of the cohomology of the twists of a coherent sheaf is always a polynomial, the Hilbert polynomial.

### Proof in words

The standard open sets $D_+(x_i)$ form an affine cover of $X$ with affine intersections, so the Čech complex of this cover computes cohomology. Taking all twists at once, the Čech complex of $\bigoplus_n \mathcal{O}(n)$ is built from the localizations $S_{x_I}$, which are free on monomials, and its differential sends a monomial to signed copies of the same monomial. So the complex splits into one small complex for each exponent vector $a \in \mathbb{Z}^{r+1}$. The monomial $x^a$ lives in $S_{x_I}$ exactly when $I$ contains the set $N(a)$ of indices with $a_i < 0$, so the small complex is the cochain complex of the faces of a simplex that contain $N(a)$. If some index $j$ is not in $N(a)$, adding $j$ to a face is a contracting homotopy, as in Theorem P4.1.2, and the only cohomology occurs for $N(a) = \emptyset$, in degree $0$, where it is the polynomial ring. If $N(a)$ is everything, the complex is the single face $\{0, \dots, r\}$ in degree $r$. So the cohomology lives in degrees $0$ and $r$, and the pairing matches $x^b$ with the unique inverse monomial that brings it to $(x_0 \cdots x_r)^{-1}$.

### Examples

**Example P4.2.3 (the projective plane).** Let $X = \mathbb{P}^2_k$ with coordinates $x, y, z$. The space $H^2(X, \mathcal{O}(-4))$ has dimension $\binom{3}{2} = 3$, with basis the classes of
$$x^{-2} y^{-1} z^{-1}, \qquad x^{-1} y^{-2} z^{-1}, \qquad x^{-1} y^{-1} z^{-2},$$
and the pairing with $H^0(X, \mathcal{O}(1)) = k x \oplus k y \oplus k z$ sends $(x, x^{-2} y^{-1} z^{-1})$ to the generator $(xyz)^{-1}$ and $(y, x^{-2} y^{-1} z^{-1})$ to the class of $x^{-2} z^{-1}$, which is $0$ because this monomial lies in $S_{xz}$. The groups $H^1(X, \mathcal{O}(n))$ vanish for all $n$, and $H^2(X, \mathcal{O}(n)) = 0$ for $n \geq -2$.

**Example P4.2.4 (the canonical sheaf).** By Corollary P3.12.22 the canonical sheaf of $\mathbb{P}^r_k$ is $\omega = \bigwedge^r \Omega \cong \mathcal{O}(-r-1)$. So $H^0(\mathbb{P}^r_k, \omega) = 0$, $H^r(\mathbb{P}^r_k, \omega) \cong k$, and $H^p(\mathbb{P}^r_k, \mathcal{O}) = 0$ for $p > 0$. For $r = 1$ this is the residue computation of Example P4.1.25, where $\omega = \Omega$ and the generator of $H^1$ is the class of $dt/t$, which corresponds to $(x_0 x_1)^{-1}$ up to sign under $\Omega \cong \mathcal{O}(-2)$.

**Example P4.2.5 (hypersurfaces and the genus of a plane curve).** Let $k$ be a field, $r \geq 2$, $f \in S_d$ a nonzero form of degree $d \geq 1$ and $Y = V_+(f) \subseteq \mathbb{P}^r_k$, with ideal sheaf $\mathcal{O}(-d)$. The sequence of graded modules $0 \to S(-d) \xrightarrow{f} S \to S/(f) \to 0$ is exact, since $S$ is a domain, and by part 3 of Proposition P3.6.11 it gives the exact sequence
$$0 \to \mathcal{O}_X(-d) \xrightarrow{\ f\ } \mathcal{O}_X \to i_* \mathcal{O}_Y \to 0.$$
By Proposition P4.1.19, $H^p(Y, \mathcal{O}_Y) = H^p(X, i_* \mathcal{O}_Y)$. The long exact sequence and Theorem P4.2.1 give:

- $H^0(Y, \mathcal{O}_Y) = k$, since $H^0(\mathcal{O}(-d)) = 0$ and $H^1(\mathcal{O}(-d)) = 0$ for $r \geq 2$. In particular $Y$ is connected, since a disconnection would give a nontrivial idempotent in $H^0(Y, \mathcal{O}_Y)$.
- $H^p(Y, \mathcal{O}_Y) = 0$ for $0 < p < r - 1$.
- $H^{r-1}(Y, \mathcal{O}_Y) \cong H^r(X, \mathcal{O}(-d))$, of dimension $\binom{d-1}{r}$.

For a plane curve, $r = 2$, this gives $h^1(Y, \mathcal{O}_Y) = \binom{d-1}{2} = (d-1)(d-2)/2$: a line or a conic has $h^1 = 0$, a plane cubic has $h^1 = 1$, and a plane quartic has $h^1 = 3$. This number is the arithmetic genus of $Y$, defined in Chapter 3. For a surface $Y \subseteq \mathbb{P}^3_k$ of degree $d$ it gives $h^1(\mathcal{O}_Y) = 0$ and $h^2(\mathcal{O}_Y) = \binom{d-1}{3}$, which is $0$ for $d \leq 3$ and $1$ for a quartic surface.

**Example P4.2.6 (base change and torsion).** Take $A = \mathbb{Z}$. By Theorem P4.2.1 every $H^p(\mathbb{P}^r_{\mathbb{Z}}, \mathcal{O}(n))$ is a free abelian group, and its rank does not depend on the fibre: $h^p(\mathbb{P}^r_{\mathbb{F}_\ell}, \mathcal{O}(n)) = h^p(\mathbb{P}^r_{\mathbb{Q}}, \mathcal{O}(n))$ for every prime $\ell$. Chapter 5 explains that the cohomology of a flat family can jump on special fibres in general. For the line bundles $\mathcal{O}(n)$ on projective space it does not, because the cohomology over $\mathbb{Z}$ is torsion free.

### Proof

*Theorem P4.2.1.* The open sets $U_i = D_+(x_i)$, $0 \leq i \leq r$, cover $X$, and $U_I = \bigcap_{i \in I} U_i = D_+(x_I)$ is affine with ring $(S_{x_I})_0$ by Theorem P3.6.3. By part 1 of Proposition P3.6.11, $\Gamma(U_I, \mathcal{O}(n)) = (S(n)_{x_I})_0 = (S_{x_I})_n$. Let $\mathcal{F} = \bigoplus_{n \in \mathbb{Z}} \mathcal{O}(n)$. Since $X$ is separated (Example P3.4.6), Corollary P4.1.9 shows that the Čech complex $C^\bullet$ of $\mathcal{F}$ for this cover computes $H^\bullet(X, \mathcal{F})$, and by Proposition P4.1.18 this is $\bigoplus_n H^\bullet(X, \mathcal{O}(n))$. With the ordered Čech complex,
$$C^p = \prod_{|I| = p+1} \Gamma(U_I, \mathcal{F}) = \bigoplus_{|I| = p+1} S_{x_I},$$
the product being finite, and the differential is $(dc)_{i_0 \cdots i_{p+1}} = \sum_{k} (-1)^k c_{i_0 \cdots \widehat{i_k} \cdots i_{p+1}}$, each term mapped into $S_{x_{i_0} \cdots x_{i_{p+1}}}$ by the localization map. The localization maps are inclusions of free $A$-modules that send each monomial to itself.

*The grading.* For $a \in \mathbb{Z}^{r+1}$ let $N(a) = \{i : a_i < 0\}$. The monomial $x^a$ lies in $S_{x_I}$ if and only if $N(a) \subseteq I$. Let $C^p_a \subseteq C^p$ be the free $A$-module with basis the elements $x^a e_I$, for $|I| = p + 1$ and $I \supseteq N(a)$, where $e_I$ marks the component of $I$. The differential maps $C^p_a$ into $C^{p+1}_a$, and $C^\bullet = \bigoplus_a C^\bullet_a$ as complexes of $A$-modules. The summand for $a$ lies in the part of $C^\bullet$ that computes $H^\bullet(X, \mathcal{O}(|a|))$. So $H^p(X, \mathcal{O}(n)) = \bigoplus_{|a| = n} H^p(C^\bullet_a)$.

*The case $\emptyset \neq N(a)$, $N(a) \neq \{0, \dots, r\}$.* Choose $j \notin N(a)$. The faces $I \supseteq N(a)$ are closed under adding and removing $j$, because $j \notin N(a)$. Extend the cochains of $C^\bullet_a$ to all ordered tuples by the alternating rule, and put $(hc)_{i_0 \cdots i_{p-1}} = c_{j i_0 \cdots i_{p-1}}$ for $p \geq 1$. This is a well defined map $C^p_a \to C^{p-1}_a$: if $\{i_0, \dots, i_{p-1}\} \supseteq N(a)$ then so is $\{j, i_0, \dots, i_{p-1}\}$, and the component is $0$ when $j$ is one of the $i_k$. For $p \geq 1$ the computation in the proof of Theorem P4.1.2 gives $(dh + hd)c = c$, and it is a formal identity on alternating cochains, valid on any family of faces closed under adding $j$. In degree $0$, $C^0_a$ is spanned by the $x^a e_{\{i\}}$ with $\{i\} \supseteq N(a)$. Since $N(a) \neq \emptyset$ this forces $N(a) = \{i\}$, and $(hd c)_{i} = (dc)_{ji} = c_i - c_j = c_i$ because $\{j\} \not\supseteq N(a)$ gives $c_j = 0$. So $hd = \mathrm{id}$ on $C^0_a$, and $C^\bullet_a$ is contractible. Its cohomology is $0$.

*The case $N(a) = \emptyset$.* All faces occur, and $C^\bullet_a$ is the Čech complex of the free module $A \cdot x^a$ for the cover of a one-point space by $r + 1$ copies of itself. Adding the augmentation $A \to C^0_a$, $1 \mapsto (x^a, \dots, x^a)$, the face $\emptyset$, the same homotopy with any $j$ shows that the augmented complex is exact. So $H^0(C^\bullet_a) = A \cdot x^a$ and $H^p(C^\bullet_a) = 0$ for $p > 0$. The element of $H^0$ is the global section $x^a \in S_{|a|}$.

*The case $N(a) = \{0, \dots, r\}$.* Only the face $\{0, \dots, r\}$ occurs, so $C^\bullet_a = A \cdot x^a$ in degree $r$, and $H^r(C^\bullet_a) = A \cdot x^a$.

Collecting the cases, $H^0(X, \mathcal{O}(n))$ is free on the $x^a$ with $a_i \geq 0$ and $|a| = n$, which is part 1, compatible with the map $S_n \to H^0$ of Theorem P3.6.12. The module $H^r(X, \mathcal{O}(n))$ is free on the $x^a$ with all $a_i \leq -1$ and $|a| = n$, which is part 2: if $n > -r-1$ there are none, and if $n = -r-1$ there is exactly one, $a = (-1, \dots, -1)$. All other cohomology vanishes, which is part 3. For $p > r$ this is also Corollary P4.1.10.

*Part 4.* In degree $r$, $H^r(X, \mathcal{O}(m))$ is the cokernel of $d \colon \bigoplus_i (S_{x_0 \cdots \widehat{x_i} \cdots x_r})_m \to (S_{x_0 \cdots x_r})_m$, and the image of $d$ is spanned by the monomials with some exponent $\geq 0$. Multiplication by $s \in S_n$ maps $(S_{x_0 \cdots x_r})_m$ to $(S_{x_0 \cdots x_r})_{m+n}$ and the image of $d$ into the image of $d$, since it preserves each $S_{x_I}$. This defines the pairing $S_n \times H^r(\mathcal{O}(m)) \to H^r(\mathcal{O}(m+n))$, and by part 1 a pairing with $H^0(X, \mathcal{O}(n))$. Take $m = -n-r-1$, $b \geq 0$ with $|b| = n$, and $a \leq -1$ with $|a| = m$. The product $x^b x^a = x^{a+b}$ has degree $-r-1$. Its class is nonzero exactly when $a + b \leq -1$ in every coordinate, and since the coordinates of $a + b$ sum to $-r-1$ this happens exactly when $a + b = (-1, \dots, -1)$, that is, $a = -b - (1, \dots, 1)$. The bases are therefore dual, and the pairing is perfect. Both modules are free of rank equal to the number of $b \geq 0$ with $|b| = n$.

*Base change.* For a ring map $A \to B$, $\mathbb{P}^r_A \times_A \operatorname{Spec} B = \mathbb{P}^r_B$, the pullback of $\mathcal{O}(n)$ is $\mathcal{O}(n)$, and the Čech complex for $B$ is $C^\bullet \otimes_A B$, with the same splitting by monomials. Since each $C^\bullet_a$ is a complex of free modules that is either contractible or a single free module in one degree, its cohomology commutes with $- \otimes_A B$. $\square$

*Corollary P4.2.2.* The monomials $x^b$ with $b \geq 0$ and $|b| = n$ correspond to choices of $n$ objects from $r + 1$ types with repetition, and there are $\binom{n+r}{r}$ of them. The substitution $b_i = -a_i - 1$ identifies the $a$ with $a_i \leq -1$ and $|a| = n$ with the $b \geq 0$ with $|b| = -n - r - 1$, so there are $\binom{-n-1}{r}$ of them for $n \leq -r-1$. Let $P(n) = (n+r) \cdots (n+1)/r!$. For $n \geq 0$, $P(n) = \binom{n+r}{r} = h^0$. For $-r \leq n \leq -1$ one factor $n + j$, $j = -n$, is $0$, so $P(n) = 0$, and all cohomology vanishes. For $n \leq -r-1$ all $r$ factors are negative, and
$$P(n) = (-1)^r \frac{(-n-1)(-n-2) \cdots (-n-r)}{r!} = (-1)^r \binom{-n-1}{r} = (-1)^r h^r. \qquad \square$$

### Exercises

1. (A) List the basis of $H^2(\mathbb{P}^2_k, \mathcal{O}(-5))$ given by Theorem P4.2.1, and write down the dual basis of $H^0(\mathbb{P}^2_k, \mathcal{O}(2))$ under the pairing of part 4.
2. (A) Check that for $r = 1$ Theorem P4.2.1 agrees with Proposition P4.1.24, and match the bases: the class of $t^m$ in $H^1(\mathbb{P}^1_A, \mathcal{O}(n))$, $n < m < 0$, with a monomial $x_0^{a_0} x_1^{a_1}$, using $t = x_1/x_0$ and the trivialization of $\mathcal{O}(n)$ on $U_0$ by $x_0^n$.
3. (A) Let $M = \bigoplus_n H^r(\mathbb{P}^r_A, \mathcal{O}(n))$ with the $S$-module structure of part 4. Show that multiplication by each $x_i$ is surjective on $M$, that every element of $M$ is annihilated by a power of the ideal $(x_0, \dots, x_r)$, and that $M$ is not finitely generated over $S$.
4. (B) Let $f, g \in k[x_0, \dots, x_3]$ be forms of degrees $d, e \geq 1$ that form a regular sequence, and let $C = V_+(f, g) \subseteq \mathbb{P}^3_k$. Use the exactness of the Koszul complex $0 \to S(-d-e) \to S(-d) \oplus S(-e) \to S \to S/(f, g) \to 0$ to show that $h^0(C, \mathcal{O}_C) = 1$ and
$$h^1(C, \mathcal{O}_C) = 1 + \frac{de(d + e - 4)}{2}.$$
Check the cases of a plane cubic, $d = 1$, $e = 3$, and of the intersection of two quadrics, $d = e = 2$.
5. (B) Let $k$ be a field and $f$ a form of degree $d$ in $k[x_0, \dots, x_r]$, $r \geq 1$, with $Y = V_+(f)$. Compute $h^p(Y, \mathcal{O}_Y(n))$ for all $p$ and $n$ from the twisted sequence $0 \to \mathcal{O}(n-d) \to \mathcal{O}(n) \to \mathcal{O}_Y(n) \to 0$, including the case $r = 1$, where $Y$ is a finite scheme of length $d$.
6. (C) Let $X = \mathbb{P}^r_A \times_A \mathbb{P}^s_A$ with $\mathcal{O}(a, b) = \operatorname{pr}_1^* \mathcal{O}(a) \otimes \operatorname{pr}_2^* \mathcal{O}(b)$. Use the cover by the products $D_+(x_i) \times D_+(y_j)$ and a grading by $\mathbb{Z}^{r+1} \times \mathbb{Z}^{s+1}$ to show that $H^p(X, \mathcal{O}(a, b)) \cong \bigoplus_{p_1 + p_2 = p} H^{p_1}(\mathbb{P}^r_A, \mathcal{O}(a)) \otimes_A H^{p_2}(\mathbb{P}^s_A, \mathcal{O}(b))$, and deduce that $H^1(\mathbb{P}^1 \times \mathbb{P}^1, \mathcal{O}(a, b)) \neq 0$ for $a = -2$ and $b \geq 0$.

### Lean

Mathlib has the $\operatorname{Proj}$ construction, `AlgebraicGeometry.Proj`, and the Čech complex over all tuples, `CategoryTheory.cechComplexFunctor`. The cohomology of $\mathcal{O}(n)$ on $\mathbb{P}^r_A$, its perfect pairing and the dimension formulas are not in Lean as stated. The handbook adds no `MinimalModel` node here.

### Notes and history

Theorem P4.2.1 is the computation of Serre's *Faisceaux algébriques cohérents* (Ser55), where Čech cohomology of coherent sheaves was introduced for this purpose, and Hartshorne's Theorem III.5.1 is the form given here, with the proof by the grading by monomials. The duality of part 4 was the model for Serre duality, and the formula for the genus of a plane curve in Example P4.2.5 goes back to the nineteenth century, where it was proved by counting the conditions that adjoint curves impose. The literature state is theorem. In the minimal model program the computation is the base case of every cohomological argument on a projective variety: a projective variety embeds in some $\mathbb{P}^r$, its coherent sheaves are resolved by sums of the $\mathcal{O}(n)$, and the vanishing of Section 2.2 is deduced from the vanishing proved here.
