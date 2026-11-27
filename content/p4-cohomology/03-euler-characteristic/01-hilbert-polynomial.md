---
title: The Euler characteristic and the Hilbert polynomial
nodes: []
sources: [Har77, Vak25, GW23, Stacks]
reads_with: [Har77:III.5, Vak25:ch18]
requires: [P1.2, P3.5, P3.7, P3.13, P4.1, P4.2]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The Euler characteristic and the Hilbert polynomial

### Statement

Let $k$ be a field and $X$ a projective scheme over $k$. By Corollary P4.2.8 the groups $H^p(X, \mathcal{F})$ of a coherent sheaf are finite-dimensional and vanish for $p$ large.

**Definition P4.3.1 (Euler characteristic).** The *Euler characteristic* of a coherent sheaf $\mathcal{F}$ on $X$ is
$$\chi(X, \mathcal{F}) = \sum_{p \geq 0} (-1)^p h^p(X, \mathcal{F}).$$
Write $\chi(\mathcal{F})$ when $X$ is clear.

**Proposition P4.3.2 (first properties).** Let $\mathcal{F}$ be coherent on $X$.

1. For an exact sequence $0 \to \mathcal{F}_1 \to \mathcal{F}_2 \to \dots \to \mathcal{F}_s \to 0$ of coherent sheaves, $\sum_i (-1)^i \chi(\mathcal{F}_i) = 0$. In particular $\chi$ is additive on short exact sequences.
2. For a closed immersion $i \colon Y \to X$ and $\mathcal{G}$ coherent on $Y$, $\chi(X, i_* \mathcal{G}) = \chi(Y, \mathcal{G})$.
3. For a field extension $K/k$, $\chi(X_K, \mathcal{F}_K) = \chi(X, \mathcal{F})$, where $\mathcal{F}_K$ is the pullback of $\mathcal{F}$ to $X_K = X \times_k \operatorname{Spec} K$.

Lean: not in Lean as stated.

A *numerical polynomial* is a polynomial $P \in \mathbb{Q}[n]$ with $P(n) \in \mathbb{Z}$ for all $n \in \mathbb{Z}$. Write $\binom{n}{i} = n(n-1) \cdots (n - i + 1)/i!$ for the binomial polynomial of degree $i$.

**Lemma P4.3.3 (numerical polynomials).**

1. Every numerical polynomial of degree $d \geq 0$ is $\sum_{i=0}^d c_i \binom{n}{i}$ with $c_i \in \mathbb{Z}$ and $c_d \neq 0$. Its leading coefficient is $c_d/d!$.
2. Let $\varphi \colon \mathbb{Z} \to \mathbb{Z}$ be a function such that $\Delta \varphi(n) = \varphi(n) - \varphi(n - 1)$ is a numerical polynomial of degree $e \geq -1$, where the zero polynomial has degree $-1$. Then $\varphi$ is a numerical polynomial of degree $e + 1$, or of degree $\leq 0$ if $e = -1$.

Lean: not in Lean as stated.

Now fix a closed immersion $X \to \mathbb{P}^r_k$, with $\mathcal{O}_X(1)$ the pullback of $\mathcal{O}(1)$, and write $\dim \emptyset = -1$.

**Theorem P4.3.4 (the Hilbert polynomial).** Let $\mathcal{F}$ be a coherent sheaf on $X$.

1. There is a unique polynomial $P_\mathcal{F} \in \mathbb{Q}[n]$ with $\chi(X, \mathcal{F}(n)) = P_\mathcal{F}(n)$ for every $n \in \mathbb{Z}$. It is a numerical polynomial.
2. $P_\mathcal{F}(n) = h^0(X, \mathcal{F}(n))$ for all large $n$.
3. $\deg P_\mathcal{F} = \dim \operatorname{Supp} \mathcal{F}$, and the leading coefficient of $P_\mathcal{F}$ is positive if $\mathcal{F} \neq 0$.
4. If $X \subseteq \mathbb{P}^r_k$ is a closed subscheme, then $P_{\mathcal{O}_X}$ is the Hilbert polynomial $P_X$ of Definition P3.13.12.

Lean: not in Lean as stated.

The polynomial $P_\mathcal{F}$ is the *Hilbert polynomial* of $\mathcal{F}$. It depends on $\mathcal{O}_X(1)$, but part 1 shows that it does not depend on any graded module that defines $\mathcal{F}$. In particular, the Hilbert polynomial of P3 Ch. 13, defined by the dimensions of the graded pieces of a homogeneous coordinate ring for large degrees, is an Euler characteristic in every degree, including the degrees where it differs from the Hilbert function.

### Proof in words

Euler characteristics are additive because a long exact sequence of finite-dimensional vector spaces has alternating sum of dimensions zero. Base change to an infinite field changes no dimension, so a hyperplane in general position exists, and multiplication by it gives the sequence $0 \to \mathcal{F}(n-1) \to \mathcal{F}(n) \to \mathcal{F}_H(n) \to 0$. The difference $\chi(\mathcal{F}(n)) - \chi(\mathcal{F}(n-1))$ is the Euler characteristic of a sheaf on a projective space of one dimension less, which is a polynomial by induction. Summing differences gives a polynomial. The hyperplane cuts the support in dimension one less, which raises the degree by one at each step. For large $n$ Serre's vanishing theorem kills all higher cohomology, so the polynomial counts global sections, and for the structure sheaf of a subscheme these are the graded pieces of its saturated homogeneous coordinate ring in large degrees.

### Examples

**Example P4.3.5 (projective space and hypersurfaces).** By Corollary P4.2.2, $P_{\mathcal{O}_{\mathbb{P}^r}}(n) = \binom{n + r}{r}$, for all $n$, including $-r \leq n \leq -1$, where both sides vanish, and $n \leq -r-1$, where the left side is $(-1)^r h^r$. For a hypersurface $Y = V_+(f)$ of degree $d$, the sequence $0 \to \mathcal{O}(n-d) \to \mathcal{O}(n) \to \mathcal{O}_Y(n) \to 0$ and part 1 of Proposition P4.3.2 give
$$P_{\mathcal{O}_Y}(n) = \binom{n + r}{r} - \binom{n + r - d}{r},$$
as polynomials, which is the formula of Example P3.13.17. For $r = 2$, $P_{\mathcal{O}_Y}(0) = 1 - \binom{2 - d}{2} = 1 - (d-1)(d-2)/2$, and Example P4.2.5 computes the two terms: $h^0(\mathcal{O}_Y) = 1$ and $h^1(\mathcal{O}_Y) = (d-1)(d-2)/2$.

**Example P4.3.6 (finite support).** If $\operatorname{Supp} \mathcal{F}$ is finite, every $\mathcal{F}(n)$ has no higher cohomology (Example P4.2.20), and $\mathcal{F}(n) \cong \mathcal{F}$ because $\mathcal{O}(n)$ is trivial on the semilocal affine scheme on which $\mathcal{F}$ lives. So $P_\mathcal{F}$ is the constant $h^0(\mathcal{F}) = \dim_k \Gamma(X, \mathcal{F})$. For $Z = V_+(x^2, y) \subseteq \mathbb{P}^2_k$, a double point, $P_{\mathcal{O}_Z} = 2$.

**Example P4.3.7 (two lines).** Let $X_1 = L_1 \sqcup L_2 \subseteq \mathbb{P}^3_k$ be two skew lines and $X_0 = L_1 \cup L_2'$ two lines that meet in a point, a conic in a plane. By Example P3.13.20, $P_{X_1}(n) = 2n + 2$ and $P_{X_0}(n) = 2n + 1$. The values at $n = 0$ are the Euler characteristics of the structure sheaves. For $X_1$, $h^0(\mathcal{O}_{X_1}) = 2$, one constant on each line, and $h^1 = 0$. For $X_0$, Example P4.2.5 in the plane gives $h^0 = 1$ and $h^1 = 0$. The flat limit of skew lines in Example P3.13.11 keeps $P(0) = 2$: it is $X_0$ with an embedded point, and its structure sheaf is an extension of $\mathcal{O}_{X_0}$ by a skyscraper sheaf of length one, with Euler characteristic $1 + 1$.

**Example P4.3.8 (a twisted cubic).** Let $C \subseteq \mathbb{P}^3_k$ be the image of $\nu \colon \mathbb{P}^1_k \to \mathbb{P}^3_k$, $[s : t] \mapsto [s^3 : s^2 t : s t^2 : t^3]$, a closed immersion with $\nu^* \mathcal{O}(1) = \mathcal{O}_{\mathbb{P}^1}(3)$. By part 2 of Proposition P4.3.2 and Corollary P4.2.2, $P_{\mathcal{O}_C}(n) = \chi(\mathbb{P}^1, \mathcal{O}(3n)) = 3n + 1$, which is the Hilbert polynomial of Example P3.13.43.

### Proof

*Proposition P4.3.2.* For part 1, split the sequence into short exact sequences $0 \to \mathcal{K}_i \to \mathcal{F}_i \to \mathcal{K}_{i+1} \to 0$ of coherent sheaves, by Proposition P3.5.22, and add with signs. So it suffices to treat $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$. Its long exact sequence of cohomology is a finite exact sequence of finite-dimensional vector spaces, and the alternating sum of the dimensions in such a sequence is $0$, by rank-nullity at each term. Part 2 is Proposition P4.1.19. For part 3, $X$ is quasi-compact and separated over $k$ and $K$ is flat over $k$, so $H^p(X_K, \mathcal{F}_K) = H^p(X, \mathcal{F}) \otimes_k K$ by Theorem P4.1.17, of the same dimension over $K$. $\square$

*Lemma P4.3.3.* The polynomials $\binom{n}{i}$ are numerical, since they count subsets for $n \geq 0$ and $\binom{-n}{i} = (-1)^i \binom{n + i - 1}{i}$ for $n > 0$. They form a $\mathbb{Q}$-basis of $\mathbb{Q}[n]$, so $P = \sum_i c_i \binom{n}{i}$ with $c_i \in \mathbb{Q}$. Pascal's rule $\binom{n}{i} - \binom{n-1}{i} = \binom{n-1}{i-1}$ gives $\Delta P(n) = \sum_{i \geq 1} c_i \binom{n-1}{i-1}$, again numerical. By induction on the degree the $c_i$ with $i \geq 1$ are integers, and $c_0 = P(0) \in \mathbb{Z}$. This is part 1. For part 2, write $\Delta \varphi(n) = \sum_{i=0}^{e} c_i \binom{n - 1}{i}$ with $c_i \in \mathbb{Z}$, an expansion of the same kind as in part 1 after the shift $n \mapsto n - 1$. Then $Q(n) = \sum_i c_i \binom{n}{i+1}$ has $\Delta Q = \Delta \varphi$ by Pascal's rule, so $\varphi - Q$ has $\Delta(\varphi - Q) = 0$ and is a constant $c \in \mathbb{Z}$. So $\varphi = Q + c$ is numerical of degree $e + 1$ if $e \geq 0$, since $c_e \neq 0$, and constant if $e = -1$. $\square$

*Theorem P4.3.4, part 4 assuming part 2.* Let $X \subseteq \mathbb{P}^r_k$ with ideal sheaf $\mathcal{I}_X$ and $I = \Gamma_*(\mathcal{I}_X) = \bigoplus_n \Gamma(\mathcal{I}_X(n))$, a homogeneous ideal of $S = k[x_0, \dots, x_r]$ by Theorem P3.6.12, with $\widetilde{I} = \mathcal{I}_X$ by Theorem P3.6.14, so that $\operatorname{Proj} S/I = X$. By Corollary P4.2.9 applied to $0 \to \mathcal{I}_X \to \mathcal{O} \to \mathcal{O}_X \to 0$, the sequence $0 \to I_n \to S_n \to \Gamma(X, \mathcal{O}_X(n)) \to 0$ is exact for large $n$. So $h^0(\mathcal{O}_X(n)) = \dim_k (S/I)_n$ for large $n$, and this is $P_X(n)$ for large $n$ by part 1 of Lemma P3.13.13. By part 2, $P_{\mathcal{O}_X}(n) = h^0(\mathcal{O}_X(n))$ for large $n$, and two polynomials that agree for large $n$ are equal.

*Part 2.* By Theorem P4.2.7, $h^p(\mathcal{F}(n)) = 0$ for $p > 0$ and $n$ large, so $\chi(\mathcal{F}(n)) = h^0(\mathcal{F}(n))$.

*Reduction to an infinite field.* Let $K = k(t)$. The scheme $X_K$ is a closed subscheme of $\mathbb{P}^r_K$, $(\mathcal{F}(n))_K = \mathcal{F}_K(n)$, and $\chi(\mathcal{F}_K(n)) = \chi(\mathcal{F}(n))$ by part 3 of Proposition P4.3.2. Over an affine open $\operatorname{Spec} B$ of $X$ with $\mathcal{F} = \widetilde{M}$, $\mathcal{F}_K$ corresponds to $M \otimes_k K$ over $B \otimes_k K$, and the support of $\mathcal{F}_K$ is the preimage of $\operatorname{Supp} \mathcal{F}$, which has the same dimension by Lemma P3.7.23 applied to its irreducible components with the reduced structure. So parts 1 and 3 for $\mathcal{F}_K$ give them for $\mathcal{F}$. Assume $k$ infinite. Replacing $\mathcal{F}$ by its pushforward to $\mathbb{P}^r_k$, which has the same twists, cohomology and support by part 2 of Proposition P4.3.2, assume $X = \mathbb{P}^r_k$.

*Parts 1 and 3, by induction on $r$.* Uniqueness in part 1 is clear, since a polynomial is determined by its values at infinitely many integers. If $\mathcal{F} = 0$ then $P_\mathcal{F} = 0$, of degree $-1 = \dim \emptyset$. For $r = 0$, $\mathcal{F}(n) = \mathcal{F}$ is a vector space of dimension $\chi(\mathcal{F})$, and if $\mathcal{F} \neq 0$ the constant is positive and $\operatorname{Supp} \mathcal{F}$ is a point. Let $r \geq 1$ and $\mathcal{F} \neq 0$ with $d = \dim \operatorname{Supp} \mathcal{F}$. By Lemma P4.2.18 there is a linear form $h$ that vanishes at no associated point of $\mathcal{F}$, with exact sequences $0 \to \mathcal{F}(n-1) \to \mathcal{F}(n) \to \mathcal{F}_H(n) \to 0$ and $\mathcal{F}_H$ coherent on $H \cong \mathbb{P}^{r-1}_k$. By part 1 of Proposition P4.3.2,
$$\chi(\mathcal{F}(n)) - \chi(\mathcal{F}(n-1)) = \chi(\mathcal{F}_H(n)) = P_{\mathcal{F}_H}(n),$$
a numerical polynomial of degree $\dim \operatorname{Supp} \mathcal{F}_H$ by induction. By part 2 of Lemma P4.3.3, $n \mapsto \chi(\mathcal{F}(n))$ is a numerical polynomial. This proves part 1.

For part 3, first $\operatorname{Supp} \mathcal{F}_H = \operatorname{Supp} \mathcal{F} \cap H$. At $x \notin H$ the stalk of $\mathcal{F}_H$ is $0$. At $x \in H$, the local equation of $h$ lies in $\mathfrak{m}_x$, and $(\mathcal{F}_H)_x = \mathcal{F}_x / h \mathcal{F}_x$ up to the twist, which is nonzero if $\mathcal{F}_x \neq 0$ by Nakayama's lemma. Next, let $Z$ be an irreducible component of $\operatorname{Supp} \mathcal{F}$, with the reduced structure, of dimension $d_Z$. Its generic point is an associated point of $\mathcal{F}$ by Theorem P1.2.48, so $h$ does not vanish on $Z$. On each chart $Z \cap D_+(x_i)$, an integral affine scheme of finite type over $k$, the function $h/x_i$ is not $0$, and if it is not a unit, every component of its zero set has dimension $d_Z - 1$ by part 1 of Proposition P3.7.5. So every component of $Z \cap H$ has dimension $d_Z - 1$, using part 2 of Proposition P3.7.2 and part 2 of Theorem P3.7.4 to pass between $Z$ and its charts.

If $d_Z \geq 1$, then $Z \cap H \neq \emptyset$. Otherwise $Z$ lies in $D_+(h) \cong \mathbb{A}^r_k$, closed there, so $Z$ is affine with a ring $B$ that is a finitely generated $k$-algebra and a domain, and $Z$ is proper over $k$, being closed in $\mathbb{P}^r_k$. For $b \in B$, the morphism $Z \to \mathbb{A}^1_k \subseteq \mathbb{P}^1_k$ given by $b$ has closed irreducible image in $\mathbb{P}^1_k$ that misses the point at infinity, so the image is a closed point $V(g)$ with $g \in k[t]$ irreducible. Then $g(b)$ vanishes at every point of $Z$, and $g(b) = 0$ since $B$ is reduced. So every element of $B$ is algebraic over $k$, $B$ is a finite-dimensional $k$-vector space, and $\dim Z = 0$, a contradiction.

So $\dim(\operatorname{Supp} \mathcal{F} \cap H) = d - 1$ if $d \geq 1$, and $\operatorname{Supp} \mathcal{F} \cap H = \emptyset$ if $d = 0$, because then every point of the finite set $\operatorname{Supp} \mathcal{F}$ is the generic point of a component and so not on $H$. By induction $\deg P_{\mathcal{F}_H} = d - 1$, and by part 2 of Lemma P4.3.3, $\deg P_\mathcal{F} = d$ if $d \geq 1$, while $P_\mathcal{F}$ is constant if $d = 0$. In the latter case $\mathcal{F}_H = 0$, $\chi(\mathcal{F}(n))$ is constant, and its value $h^0(\mathcal{F}(n))$ for large $n$ is positive, because a coherent sheaf $\mathcal{F} \neq 0$ has $\mathcal{F}(n)$ generated by global sections for large $n$ by Theorem P3.6.23. If $d \geq 1$ the leading coefficient of $P_\mathcal{F}$ is the leading coefficient of $P_{\mathcal{F}_H}$ divided by $d$, positive by induction. $\square$

### Exercises

1. (A) Compute $P_{\mathcal{O}(a)}$ on $\mathbb{P}^r_k$ and $P_{\mathcal{O}_X}$ for $X = \mathbb{P}^1_k \times \mathbb{P}^1_k$ embedded in $\mathbb{P}^3_k$ as the quadric $V_+(x_0 x_3 - x_1 x_2)$.
2. (A) Let $\mathcal{F}$ be coherent on $\mathbb{P}^r_k$ with a resolution $0 \to \mathcal{E}_s \to \dots \to \mathcal{E}_0 \to \mathcal{F} \to 0$ by finite sums $\mathcal{E}_j = \bigoplus_l \mathcal{O}(-a_{jl})$. Show that $P_\mathcal{F}(n) = \sum_{j, l} (-1)^j \binom{n - a_{jl} + r}{r}$.
3. (A) Show that $P_{\mathcal{F} \oplus \mathcal{G}} = P_\mathcal{F} + P_\mathcal{G}$ and $P_{\mathcal{F}(a)}(n) = P_\mathcal{F}(n + a)$.
4. (B) Let $Z \subseteq \mathbb{P}^2_k$ be the union of the three coordinate points with the reduced structure. Compute $h^0(\mathcal{O}_Z(n))$ and $\dim_k (S/I_Z)_n$ for all $n \geq 0$, where $I_Z$ is the ideal of $Z$, and find the first $n$ where they agree with $P_{\mathcal{O}_Z} = 3$.
5. (B) Show that the numerical polynomials of degree $d$ that occur as Hilbert polynomials of coherent sheaves on $\mathbb{P}^r_k$, $d \leq r$, all have leading coefficient in $\frac{1}{d!} \mathbb{Z}_{> 0}$, and give a sheaf with $P(n) = n + 5$.
6. (C) Let $\mathcal{F}$ be coherent on $\mathbb{P}^r_k$ and $\mathcal{G} = \mathcal{H}om(\mathcal{F}, \mathcal{O})$. Show by an example on $\mathbb{P}^1_k$ that $P_\mathcal{G}$ is not determined by $P_\mathcal{F}$, and check that $P_{\mathcal{F}^\vee}(n) = (-1)^r P_\mathcal{F}(-n - r - 1)$ when $\mathcal{F}$ is a finite sum of line bundles $\mathcal{O}(a)$. Chapter 7 proves this formula for every locally free $\mathcal{F}$ by Serre duality.

### Lean

Mathlib has the polynomial attached to a rational power series, `Polynomial.hilbertPoly`, which is the algebraic step from a Hilbert series to its polynomial. The Euler characteristic of a coherent sheaf and the Hilbert polynomial of a coherent sheaf on a projective scheme are not in Lean as stated. The handbook adds no `MinimalModel` node here.

### Notes and history

Hilbert introduced the Hilbert function of a graded module and proved that it is eventually a polynomial in 1890. Serre identified it with an Euler characteristic in *Faisceaux algébriques cohérents* (Ser55), which made it a sheaf invariant independent of the graded module. Hartshorne proves parts 1 and 4 of Theorem P4.3.4 in Exercise III.5.2. The literature state is theorem. The minimal model program uses Theorem P4.3.4 in its asymptotic form: for a line bundle $\mathcal{L}$ on a projective variety, $\chi(\mathcal{L}^m)$ is a polynomial in $m$, and when the higher cohomology of $\mathcal{L}^m$ vanishes or grows slowly its leading term computes $h^0(\mathcal{L}^m)$, the growth of the sections that defines bigness and the volume.
