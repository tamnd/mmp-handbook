---
title: Intersection multiplicity and Bézout's theorem
nodes: []
sources: [Ful69, Har77, Rei88]
reads_with: [Ful69:ch3, Ful69:ch5, Har77:I.7, Rei88:ch1]
requires: [P0.3, P0.4]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Intersection multiplicity and Bézout's theorem

### Statement

Let $\mathcal{O}_P$ be the local ring of $\mathbb{A}^2$ at a point $P$: the rational functions $a/b$ with $a, b \in k[x, y]$ and $b(P) \neq 0$.

**Definition P0.7.9.** Let $f, g \in k[x, y]$ and $P \in \mathbb{A}^2$. The *intersection multiplicity* of $f$ and $g$ at $P$ is
$$
I(P, f \cap g) = \dim_k \mathcal{O}_P / (f, g),
$$
an integer or $\infty$. For projective curves $F$ and $G$ and a point $P \in \mathbb{P}^2$, choose a standard affine chart that contains $P$, dehomogenize $F$ and $G$ in that chart, and take the intersection multiplicity of the two affine polynomials.

Lean: not in Lean.

**Example P0.7.10.** Let $f = y - x^2$ and $g = y$ at $P = (0, 0)$. Then $(f, g) = (x^2, y)$ and $\mathcal{O}_P / (x^2, y) \cong k[x]_{(x)} / (x^2)$ has the basis $1, x$. So $I(P, f \cap g) = 2$: the tangent line meets the parabola twice at $P$.

**Example P0.7.11.** Let $f = y^2 - x^3$ and $g = y$. Then $(f, g) = (x^3, y)$ and $I(P, f \cap g) = 3$ at the origin.

**Theorem P0.7.12 (properties of intersection multiplicity).** Let $f, g, h \in k[x, y]$ and $P \in \mathbb{A}^2$.

1. $I(P, f \cap g) = I(P, g \cap f)$, and $I(P, f \cap g) = I(P, f \cap (g + af))$ for every $a \in k[x, y]$.
2. $I(P, f \cap g) = 0$ if and only if $P \notin V(f) \cap V(g)$.
3. $I(P, f \cap g) < \infty$ if $f$ and $g$ have no common component through $P$.
4. If $f$ and $g$ have no common component, then $I(P, f \cap gh) = I(P, f \cap g) + I(P, f \cap h)$.
5. $I(P, f \cap g)$ does not change under an affine change of coordinates that moves $P$ with the curves.

Lean: not in Lean.

*Proof.* (1) The ideals $(f, g)$, $(g, f)$ and $(f, g + af)$ are equal. (2) If $f(P) \neq 0$, then $f$ is a unit in $\mathcal{O}_P$, so the quotient is 0; the same holds for $g$. If $f(P) = g(P) = 0$, then $(f, g)$ is in the maximal ideal of $\mathcal{O}_P$, so the quotient is not 0. (3) Translate $P$ to the origin. Remove from $f$ and $g$ the components that do not pass through $P$: they are units in $\mathcal{O}_P$. Then $f$ and $g$ have no common factor, and by the Lemma in Section 7.1, $V(f, g) = \{P, P_2, \dots, P_r\}$ is finite. Choose a polynomial $h$ with $h(P) \neq 0$ and $h(P_i) = 0$ for $i \ge 2$, for example a product of lines. Then $hx$ and $hy$ vanish on $V(f, g)$, so by the Nullstellensatz $(hx)^N$ and $(hy)^N$ are in $(f, g)$ for some $N$. As $h$ is a unit in $\mathcal{O}_P$, the elements $x^N$ and $y^N$ are in $(f, g)\mathcal{O}_P$. So $\mathcal{O}_P / (f, g)$ is a quotient of $\mathcal{O}_P / (x^N, y^N) \cong k[x, y]/(x^N, y^N)$, which has finite dimension. (4) Consider the sequence of $\mathcal{O}_P$-modules
$$
0 \to \mathcal{O}_P / (f, h) \xrightarrow{\ \cdot g\ } \mathcal{O}_P / (f, gh) \to \mathcal{O}_P / (f, g) \to 0 .
$$
The second map is the quotient map, and it is surjective with kernel $(f, g)/(f, gh)$, which is the image of the first map. The first map is injective: if $gz = uf + vgh$ in $\mathcal{O}_P$, then $g(z - vh) = uf$. As $f$ and $g$ have no common factor, $f$ divides $z - vh$ in $\mathcal{O}_P$ (clear denominators and use unique factorization in $k[x, y]$), so $z \in (f, h)$. The dimensions add. (5) An affine change of coordinates is a $k$-algebra automorphism of $k[x, y]$, and it gives an isomorphism of the local rings and of the quotients. $\square$

Property (5) and a short computation show that the projective definition does not depend on the chart (Fulton, Ch. 5).

**Proposition P0.7.13 (multiplicity bound).** Let $P$ be a common point of $f$ and $g$ with no common component through $P$. Then $I(P, f \cap g) \ge m_P(f)\, m_P(g)$. Equality holds if and only if $f$ and $g$ have no common tangent line at $P$.

Lean: not in Lean.

*Proof.* Fulton proves this in Ch. 3. The proof compares $\dim_k k[x, y]/(f, g, \mathfrak{m}^n)$ with $\dim_k k[x, y]/\mathfrak{m}^n$ for large $n$, where $\mathfrak{m} = (x, y)$. The handbook uses only the case where $g$ is a line, and the next proposition proves that case. $\square$

**Proposition P0.7.14 (a curve and a line).** Let $F$ be a projective curve of degree $d$ and let $L$ be a line that is not a component of $F$. Choose a parametrization $[s : t] \mapsto sA + tB$ of $L$, with $A, B \in k^3$ independent. Then $F(sA + tB)$ is a nonzero binary form of degree $d$, and for $P = s_0 A + t_0 B$ on $L$, $I(P, F \cap L)$ is the multiplicity of $[s_0 : t_0]$ as a root of this form. In particular $\sum_{P \in L} I(P, F \cap L) = d$, and $I(P, F \cap L) \ge m_P(F)$, with equality if and only if $L$ is not a tangent line of $F$ at $P$.

Lean: not in Lean.

*Proof.* By Property (5), choose coordinates with $P = (0, 0)$ in the chart $Z \neq 0$ and $L = \{y = 0\}$. Then the parametrization $x \mapsto (x, 0)$ of $L$ is an affine chart of the parametrization in the statement, and the order of the root does not depend on the choice of $A$ and $B$. Let $f(x, y) = F(x, y, 1)$. Since $\mathcal{O}_P / (y) \cong k[x]_{(x)}$, there is an isomorphism
$$
\mathcal{O}_P / (f, y) \cong k[x]_{(x)} / (f(x, 0)).
$$
As $L$ is not a component of $F$, $f(x, 0) \neq 0$. Write $f(x, 0) = x^r u(x)$ with $u(0) \neq 0$. Then $u$ is a unit in $k[x]_{(x)}$, the quotient has the basis $1, x, \dots, x^{r - 1}$, and $I(P, F \cap L) = r$, the order of the root $x = 0$ of $f(x, 0)$. A binary form of degree $d$ over an algebraically closed field is a product of $d$ linear forms, so the orders of its roots add up to $d$. For the last claim, write $f = f_m + f_{m+1} + \dots$ with $m = m_P(f)$. Then $f(x, 0) = f_m(x, 0) + f_{m+1}(x, 0) + \dots$, so $r \ge m$. Equality holds if and only if $f_m(1, 0) \neq 0$, that is, if and only if $y$ does not divide $f_m$, that is, if and only if $L$ is not a tangent line at $P$. $\square$

**Theorem P0.7.15 (Bézout).** Let $F$ and $G$ be projective plane curves of degrees $d$ and $e$ with no common component. Then
$$
\sum_{P \in V(F) \cap V(G)} I(P, F \cap G) = de .
$$

Lean: not in Lean; Mathlib has `Polynomial.resultant`, the usual tool of an elimination proof.

*Proof.* The proof follows Fulton, Ch. 5. The set $V(F) \cap V(G)$ is finite by the Lemma in Section 7.1, applied in each chart. As $k$ is infinite, there is a line that misses this finite set; choose coordinates so that this line is $Z = 0$. Then every intersection point lies in the chart $Z \neq 0$, with affine polynomials $f = F(x, y, 1)$ and $g = G(x, y, 1)$.

Let $R = k[X, Y, Z]$, let $R_n$ be its forms of degree $n$, and let $\Gamma = R/(F, G)$ with graded parts $\Gamma_n$. For $n \ge d + e$, the sequence
$$
0 \to R_{n - d - e} \to R_{n - d} \oplus R_{n - e} \to R_n \to \Gamma_n \to 0,
$$
with maps $C \mapsto (CG, -CF)$ and $(A, B) \mapsto AF + BG$, is exact. The only point to check is the middle: if $AF + BG = 0$, then $F$ divides $BG$, so $F$ divides $B$, since $F$ and $G$ have no common factor. Then $B = -CF$ and $A = CG$. As $\dim R_m = \frac{(m + 1)(m + 2)}{2}$, the alternating sum of dimensions gives $\dim \Gamma_n = de$ for $n \ge d + e$.

Next, multiplication by $Z$ is injective on $\Gamma$. Suppose $ZH = AF + BG$. Put $Z = 0$: $A_0 F_0 + B_0 G_0 = 0$, where $A_0 = A(X, Y, 0)$ and so on. The forms $F_0$ and $G_0$ have no common zero on the line $Z = 0$, so they have no common factor, and $A_0 = C G_0$, $B_0 = -C F_0$ for a form $C$. Then $A - CG$ and $B + CF$ vanish on $Z = 0$, so $A - CG = Z A'$ and $B + CF = Z B'$. This gives $ZH = Z(A'F + B'G)$, so $H \in (F, G)$. Hence $\cdot Z : \Gamma_n \to \Gamma_{n + 1}$ is injective, and it is an isomorphism for $n \ge d + e$, since both sides have dimension $de$.

Dehomogenization $H \mapsto H(x, y, 1)$ identifies $k[x, y]/(f, g)$ with the union of the spaces $\Gamma_n$ along the maps $\cdot Z$. These maps are isomorphisms from $n = d + e$ on, so $\dim_k k[x, y]/(f, g) = de$. Finally, $k[x, y]/(f, g)$ has finite support $V(f, g)$, so it is the product of its localizations $\mathcal{O}_P / (f, g)$ over $P \in V(f, g)$ (Fulton, Ch. 2). The dimensions of the factors are the intersection multiplicities, and they add up to $de$. $\square$

**Corollary P0.7.16 (curves meet).** Any two projective plane curves meet in at least one point.

Lean: not in Lean.

*Proof.* If the curves have a common component, they share its points. If not, the sum in Bézout's theorem is $de \ge 1$, so some term is not 0. $\square$

**Corollary P0.7.17 (smooth curves are irreducible).** A smooth projective plane curve is irreducible. An irreducible plane cubic has at most one singular point.

Lean: not in Lean.

*Proof.* Suppose $F = GH$ with $G$ and $H$ of positive degree. By the Corollary above, $G$ and $H$ meet at a point $P$. Then $m_P(F) = m_P(G) + m_P(H) \ge 2$, since the lowest form of a product is the product of the lowest forms. So $P$ is a singular point of $F$. For the second claim, let $P \neq Q$ be singular points of an irreducible cubic $F$, and let $L$ be the line through them. $L$ is not a component of $F$. By the Proposition on a curve and a line, $I(P, F \cap L) + I(Q, F \cap L) \ge 2 + 2 = 4 > 3$, a contradiction. $\square$

### Proof in words

The intersection multiplicity is the length of a local ring, so it adds up over the points of a finite set. Bézout's theorem counts the total length of $k[x, y]/(f, g)$ in two ways. In the projective ring $R/(F, G)$, the graded parts of high degree have dimension $de$, by an exact sequence of forms and a count of monomials. The line at infinity carries no intersection points, so multiplication by $Z$ is injective, and the affine ring is a graded part in disguise.

The difficulty is the choice of the line at infinity. If an intersection point lies on $Z = 0$, the affine ring misses it, and multiplication by $Z$ is not injective. The case of a line is direct: restrict $F$ to the line and count the roots of a binary form.

### Examples

A cusp and a node. Let $f = y^2 - x^3$ and $g = y^2 - x^2 - x^3$, with $\operatorname{char} k \neq 2$. At the origin, $g - f = -x^2$, so by Properties (1) and (4),
$$
I(0, f \cap g) = I(0, f \cap x^2) = 2\, I(0, f \cap x) = 2\, I(0, y^2 \cap x) = 4 .
$$
This is equal to $m_0(f)\, m_0(g) = 2 \cdot 2$: the tangent cones $y^2$ and $(y - x)(y + x)$ have no common line. In $\mathbb{A}^2$, the equations $f = g = 0$ give $x^2 = 0$, so the origin is the only affine common point. On $Z = 0$, the forms $Y^2 Z - X^3$ and $Y^2 Z - X^2 Z - X^3$ give $X = 0$, so the only other common point is $[0 : 1 : 0]$. Bézout's theorem gives $I([0 : 1 : 0], F \cap G) = 9 - 4 = 5$.

Two conics with one common point. Let $f = y - x^2$ and $g = y - x^2 - y^2$. Then $g - f = -y^2$, and at the origin $I = I(f \cap y^2) = 2\, I(f \cap y) = 2 \cdot 2 = 4$, by the first Example in the Statement. On $Z = 0$, $YZ - X^2$ and $YZ - X^2 - Y^2$ give $X = Y = 0$, which is not a point. So the two conics meet only at the origin, with multiplicity $4 = 2 \cdot 2$.

A hypothesis that fails: affine space. The lines $y = 0$ and $y = 1$ do not meet in $\mathbb{A}^2$, and the sum in Bézout's theorem is 0, not 1. In $\mathbb{P}^2$ the lines $Y = 0$ and $Y = Z$ meet at $[1 : 0 : 0]$, with multiplicity 1. A second hypothesis that fails: the curves $y(x - 1)$ and $y(x + 1)$ share the component $y = 0$, and they meet in infinitely many points.

### Exercises

1. (A) Let $g = y - h(x)$ with $h \in k[x]$, and let $P = (a, h(a))$. Show that $I(P, f \cap g)$ is the order of vanishing of $f(x, h(x))$ at $x = a$. Use this to compute $I(0, (y^2 - x^3) \cap (y - x^2))$.
2. (A) Show that the line $y = 0$ meets $y = x^3$ only at the origin in $\mathbb{A}^2$, with multiplicity 3, and find the other intersection points in $\mathbb{P}^2$.
3. (A) Find all intersection points and their multiplicities of the conics $x^2 + y^2 = 1$ and $(x - 1)^2 + y^2 = 1$ in $\mathbb{P}^2$, with $\operatorname{char} k \neq 2$. Check that they add up to 4.
4. (B) Show that an irreducible plane curve of degree $d$ has at most $\frac{(d - 1)(d - 2)}{2}$ singular points for $d = 3$ and $d = 4$. For $d = 4$, use a conic through four singular points and one more point of the curve.
5. (B) Let $F$ be a smooth curve of degree $d \ge 2$ and $P \in V(F)$. Show that the tangent line $T_P$ satisfies $I(P, F \cap T_P) \ge 2$. A point with $I(P, F \cap T_P) \ge 3$ is a *flex*. Show that $[X : Y : Z]$ is a flex of $F$ if and only if $F$ and the Hessian $\det(\partial^2 F / \partial X_i \partial X_j)$ both vanish there, for $\operatorname{char} k = 0$.
6. (B) Use Bézout's theorem to show that five points of $\mathbb{P}^2$, no three on a line, lie on exactly one conic, and that this conic is irreducible.

### Lean

Not in Lean. Mathlib has `Polynomial.resultant`, which gives an elimination proof of Bézout's theorem, but it has no intersection multiplicity of plane curves. A formal version would define the multiplicity as the `Module.length` of a quotient of a local ring.

### Notes and history

Bézout stated the theorem in 1779; a complete proof with multiplicities came much later, with the work of the nineteenth century and the definition by length in the twentieth. The axioms in the Theorem above, with the multiplicity bound, determine $I(P, f \cap g)$ uniquely (Fulton, Ch. 3). Hartshorne proves Bézout's theorem in all dimensions as Corollary I.7.8 with Hilbert polynomials. The literature state is "theorem". Volume 1 uses the intersection number of a curve and a divisor, and the multiplicity of this section is its local term on a surface.
