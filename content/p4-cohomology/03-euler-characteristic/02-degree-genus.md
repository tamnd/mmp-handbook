---
title: Degree, arithmetic genus and Bezout's theorem
nodes: []
sources: [Har77, Vak25, Stacks]
reads_with: [Har77:III.5, Vak25:ch18]
requires: [P1.2, P3.6, P3.13, P4.2, P4.3]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Degree, arithmetic genus and Bezout's theorem

### Statement

Let $k$ be a field, $X \subseteq \mathbb{P}^r_k$ a closed subscheme and $\mathcal{F} \neq 0$ a coherent sheaf on $\mathbb{P}^r_k$ with $d = \dim \operatorname{Supp} \mathcal{F}$. By Lemma P4.3.3 and part 3 of Theorem P4.3.4 the Hilbert polynomial has the form
$$P_\mathcal{F}(n) = \frac{e}{d!} n^d + (\text{terms of lower degree}), \qquad e \in \mathbb{Z}_{> 0}.$$

**Definition P4.3.9 (degree and arithmetic genus).** The integer $e = \deg \mathcal{F}$ above is the *degree* of $\mathcal{F}$, and $\deg X = \deg \mathcal{O}_X$ for $X \neq \emptyset$. If $X$ has dimension $d$, its *arithmetic genus* is
$$p_a(X) = (-1)^d \bigl(\chi(X, \mathcal{O}_X) - 1\bigr) = (-1)^d \bigl(P_X(0) - 1\bigr).$$

For a curve, $p_a(X) = 1 - P_X(0)$, the arithmetic genus of Definition P3.13.12. Since $\chi(X, \mathcal{O}_X)$ does not involve the embedding, $p_a(X)$ depends only on $X$ and $k$, while the degree depends on the embedding: a line and a conic are both isomorphic to $\mathbb{P}^1_k$, with degrees $1$ and $2$ and the same arithmetic genus $0$. Both are unchanged by extension of the base field, by part 3 of Proposition P4.3.2.

**Proposition P4.3.10 (cutting by a hypersurface).** Let $f \in S_e$, $e \geq 1$, be a form such that multiplication by $f$ is injective on $\mathcal{F}(-e) \to \mathcal{F}$, for instance a form that vanishes at no associated point of $\mathcal{F}$. Let $\mathcal{F}_Y = \mathcal{F}/f \mathcal{F}(-e)$. If $d \geq 1$, then $\dim \operatorname{Supp} \mathcal{F}_Y = d - 1$ and $\deg \mathcal{F}_Y = e \deg \mathcal{F}$.

Lean: not in Lean as stated.

**Corollary P4.3.11 (Bezout's theorem for plane curves).** Let $f, g \in k[x, y, z]$ be forms of degrees $c, e \geq 1$ without a common factor, and $Z = V_+(f, g) \subseteq \mathbb{P}^2_k$, the closed subscheme defined by the ideal $(f, g)$. Then $Z$ is finite and
$$\sum_{P \in Z} \dim_k \mathcal{O}_{Z, P} = c e.$$

Lean: not in Lean as stated.

The number $\dim_k \mathcal{O}_{Z, P}$ is the *intersection multiplicity* of the two curves at $P$. Over an algebraically closed field the corollary says that two plane curves without a common component meet in $ce$ points counted with multiplicity.

### Proof in words

Multiplication by $f$ gives a sequence $0 \to \mathcal{F}(n - e) \to \mathcal{F}(n) \to \mathcal{F}_Y(n) \to 0$, so the Hilbert polynomial of $\mathcal{F}_Y$ is the difference $P_\mathcal{F}(n) - P_\mathcal{F}(n - e)$. Taking a difference with step $e$ lowers the degree of a polynomial by one and multiplies its leading coefficient by $e$ times the old degree. The new degree is the dimension of the support, by Theorem P4.3.4, so the support drops in dimension by one and the degree is multiplied by $e$. For two plane curves the result has finite support, and the constant Hilbert polynomial of a finite scheme is its length.

### Examples

**Example P4.3.12 (hypersurfaces and complete intersections).** A hypersurface $Y \subseteq \mathbb{P}^r_k$ of degree $d$ has $P_Y(n) = \binom{n + r}{r} - \binom{n + r - d}{r}$, with leading term $d n^{r-1}/(r-1)!$, so $\deg Y = d$. For a surface in $\mathbb{P}^3_k$,
$$p_a(Y) = P_Y(0) - 1 = -\binom{3 - d}{3} = \binom{d - 1}{3},$$
which is $0$ for $d \leq 3$ and $1$ for a quartic surface, in agreement with Example P4.2.5. For a complete intersection curve $C = V_+(f, g) \subseteq \mathbb{P}^3_k$ of degrees $d, e$, Proposition P4.3.10 applied to $\mathcal{F} = \mathcal{O}_{V_+(f)}$ and $g$ gives $\deg C = de$, and the Koszul resolution of Exercise 4 of Section 2.1 gives
$$P_C(n) = \binom{n+3}{3} - \binom{n+3-d}{3} - \binom{n+3-e}{3} + \binom{n+3-d-e}{3}, \qquad p_a(C) = 1 + \frac{de(d + e - 4)}{2}.$$

**Example P4.3.13 (rational normal curves).** The image $C_r$ of $\mathbb{P}^1_k \to \mathbb{P}^r_k$, $[s : t] \mapsto [s^r : s^{r-1} t : \dots : t^r]$, is a closed subscheme isomorphic to $\mathbb{P}^1_k$ with $\mathcal{O}_{C_r}(1) \cong \mathcal{O}_{\mathbb{P}^1}(r)$, as in Example P3.10.13. So $P_{C_r}(n) = rn + 1$, $\deg C_r = r$ and $p_a(C_r) = 0$. The twisted cubic is $C_3$.

**Example P4.3.14 (negative arithmetic genus).** Two skew lines in $\mathbb{P}^3_k$ have $P(n) = 2n + 2$ (Example P4.3.7), so they form a curve of degree $2$ with $p_a = -1$. More generally a disjoint union of $s$ lines has $p_a = 1 - s$. The arithmetic genus of a curve that is not connected, or not reduced, can be negative, and it is the geometric genus only for smooth connected curves over an algebraically closed field, as Section 3.3 explains.

**Example P4.3.15 (a conic and its tangent).** Let $f = xz - y^2$ and $g = z$. On $V_+(z)$ the equation $f$ becomes $y^2$, so $Z = V_+(z, y^2)$ is the double point at $[1 : 0 : 0]$ with $\mathcal{O}_{Z, P} = k[y]/(y^2)$ in the chart $x = 1$, of length $2 = 2 \cdot 1$. The line $g' = x$ meets the same conic in $V_+(x, y^2)$, the double point at $[0 : 0 : 1]$, and the line $y - z$ meets it in $V_+(y - z, xz - z^2)$, the two points $[1 : 0 : 0]$ and $[1 : 1 : 1]$, each of multiplicity one.

### Proof

*Proposition P4.3.10.* If $f$ vanishes at no associated point of $\mathcal{F}$, injectivity is the argument of the proof of Lemma P4.2.18, with $f/x_i^e$ in place of $h/x_i$: on $D_+(x_i)$ it is not in any associated prime of the module of $\mathcal{F}$, so it is a nonzerodivisor by Proposition P1.2.44. Twisting the exact sequence $0 \to \mathcal{F}(-e) \xrightarrow{f} \mathcal{F} \to \mathcal{F}_Y \to 0$ by $\mathcal{O}(n)$ and using part 1 of Proposition P4.3.2 gives
$$P_{\mathcal{F}_Y}(n) = P_\mathcal{F}(n) - P_\mathcal{F}(n - e).$$
For every $j \geq 1$, $n^j - (n - e)^j = j e n^{j-1} + (\text{terms of lower degree})$, and $n^0 - (n - e)^0 = 0$. With $P_\mathcal{F}(n) = \sum_{j \leq d} a_j n^j$ and $a_d = \deg \mathcal{F}/d!$, the difference is
$$d e a_d \, n^{d-1} + (\text{terms of lower degree}) = \frac{e \deg \mathcal{F}}{(d-1)!} n^{d-1} + \dots,$$
nonzero of degree $d - 1 \geq 0$. So $\mathcal{F}_Y \neq 0$, by part 3 of Theorem P4.3.4 its support has dimension $d - 1$, and $\deg \mathcal{F}_Y = e \deg \mathcal{F}$. $\square$

*Corollary P4.3.11.* Let $C = V_+(f)$ and $\mathcal{F} = \mathcal{O}_C$, with $\dim \operatorname{Supp} \mathcal{F} = 1$ and $\deg \mathcal{F} = c$ by Example P4.3.12. Multiplication by $g$ is injective on $\mathcal{O}_C(-e) \to \mathcal{O}_C$. On $D_+(x)$, say, this is multiplication by $g/x^e$ on $(S/(f))_{(x)}$, and it suffices that $g$ is a nonzerodivisor on $S_x/f S_x$. The ring $S_x$ is factorial, and $f$ and $g$ have no common prime factor in $S_x$, since a common prime factor of $f$ and $g$ in $S_x$ would come from one in $S$. So $g a \in f S_x$ implies $a \in f S_x$. The quotient $\mathcal{F}_Y = \mathcal{O}_C/g \mathcal{O}_C(-e)$ is $\mathcal{O}_Z$, the structure sheaf of the subscheme defined by $(f, g)$. By Proposition P4.3.10, $\dim Z = 0$, so $Z$ is finite, and $P_{\mathcal{O}_Z}$ is the constant $c e$. By Example P4.3.6 this constant is $h^0(\mathcal{O}_Z)$, and since $Z$ is a finite, hence affine, scheme, $\Gamma(Z, \mathcal{O}_Z) = \prod_{P \in Z} \mathcal{O}_{Z, P}$. $\square$

### Exercises

1. (A) Compute the degree and the arithmetic genus of the quadric surface $V_+(x_0 x_3 - x_1 x_2) \subseteq \mathbb{P}^3_k$ and of the Veronese surface, the image of $\mathbb{P}^2_k$ in $\mathbb{P}^5_k$ by the forms of degree $2$, with $\mathcal{O}(1)$ pulling back to $\mathcal{O}_{\mathbb{P}^2}(2)$.
2. (A) Use the arithmetic genus to show that a plane curve of degree $d \geq 3$ is not isomorphic to $\mathbb{P}^1_k$.
3. (A) Compute the intersection multiplicities of the two conics $xz - y^2$ and $xz - y^2 + y z$, and check that they add up to $4$. Do the same for the cubic $y^2 z - x^3$ and the line $y = 0$.
4. (B) Let $X \subseteq \mathbb{P}^r_k$ be a closed subscheme of dimension $d$ and $L \subseteq \mathbb{P}^r_k$ a linear subspace of codimension $d$ cut out by linear forms $h_1, \dots, h_d$ such that each $h_j$ is a nonzerodivisor in the sense of Proposition P4.3.10 on $\mathcal{O}_{X \cap V_+(h_1, \dots, h_{j-1})}$. Show that $X \cap L$ is finite of length $\deg X$. Use Lemma P4.2.18 to show that such forms exist when $k$ is infinite.
5. (B) Let $X = X_1 \cup X_2$ be the union of two closed subschemes of $\mathbb{P}^r_k$ of the same dimension $d$, with ideal sheaf $\mathcal{I}_1 \cap \mathcal{I}_2$, such that $\dim(X_1 \cap X_2) < d$. Show that $\deg X = \deg X_1 + \deg X_2$. Compute $p_a$ of two lines in $\mathbb{P}^3_k$ that meet in a point, and compare with Example P4.3.14.
6. (C) Let $C \subseteq \mathbb{P}^3_k$ be a curve of degree $d$ that lies on no plane, with $k$ algebraically closed, $C$ integral. Using a general plane section and Exercise 4, show that $d \geq 3$, and that equality holds for the twisted cubic.

### Lean

Mathlib has the polynomial attached to a rational power series, `Polynomial.hilbertPoly`. The degree and the arithmetic genus of a projective scheme and Bezout's theorem for plane curves are not in Lean as stated. The handbook adds no `MinimalModel` node here.

### Notes and history

Bezout stated in 1779 that two plane curves of degrees $c$ and $e$ meet in $ce$ points, and the correct count with multiplicities took another century. The definition of the multiplicity as the length of the local ring of the intersection scheme is the one that makes the statement true without exceptions, and Serre's Tor formula extends it to intersections that are not complete intersections. The arithmetic genus was defined by Cayley and Noether through the constant term of the Hilbert polynomial before cohomology existed. Hartshorne's Exercises I.7.2 and III.5.3 cover this section. The literature state is theorem. In the minimal model program the degree is the first intersection number, the degree of a curve $C$ with respect to an ample divisor $H$, and the bound of Exercise 6 is the simplest case of the bounds on the degrees of rational curves that drive the cone theorem.
