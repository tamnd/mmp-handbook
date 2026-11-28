---
title: Snapper's theorem and intersection numbers
nodes: []
sources: [Kle66, Laz04, Deb01, Har77]
reads_with: [Kle66:I.2, Laz04:1.1.C, Deb01:1.1]
requires: [P1.2, P3.6, P3.7, P3.10, P4.3, P5.3, P5.5]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Snapper's theorem and intersection numbers

### Statement

In this chapter $k$ is an algebraically closed field and $X$ is a projective scheme over $k$, that is, a scheme that admits a closed immersion into some $\mathbb{P}^N_k$. Line bundles are invertible sheaves. For a line bundle $L$ and $m \in \mathbb{Z}$, $L^m$ is the tensor power $L^{\otimes m}$, with $L^{-m} = (L^{-1})^{\otimes m}$ and $L^{-1}$ the dual. For line bundles $L_1, \dots, L_r$ and $\mathbf{m} = (m_1, \dots, m_r) \in \mathbb{Z}^r$, write $L^{\mathbf{m}} = L_1^{m_1} \otimes \cdots \otimes L_r^{m_r}$, and for a subset $I \subseteq \{1, \dots, r\}$ write $L_I = \bigotimes_{i \in I} L_i$, with $L_\emptyset = \mathcal{O}_X$. The dimension of the empty set is $-1$. For a coherent sheaf $\mathcal{F}$, $\chi(\mathcal{F}) = \sum_i (-1)^i h^i(X, \mathcal{F})$ is its Euler characteristic (Definition P4.3.1), a finite sum by Theorem P4.2.7.

A *numerical polynomial in $r$ variables* is a polynomial $P \in \mathbb{Q}[t_1, \dots, t_r]$ with $P(\mathbb{Z}^r) \subseteq \mathbb{Z}$. The zero polynomial has total degree $-1$. For a function $f \colon \mathbb{Z}^r \to \mathbb{Z}$ and $1 \leq i \leq r$, the *difference* in the $i$-th variable is $\Delta_i f(\mathbf{m}) = f(\mathbf{m}) - f(\mathbf{m} - \mathbf{e}_i)$, where $\mathbf{e}_i$ is the $i$-th unit vector. For $r = 1$ this is the operator $\Delta$ of Lemma P4.3.3.

**Lemma P7.1.1 (very ample line bundles).** Let $X$ be projective over $k$.

1. Let $A$ be a very ample line bundle and $x_1, \dots, x_s$ finitely many points of $X$, not necessarily closed. There is a section $\sigma \in H^0(X, A)$ that does not vanish at any $x_j$, that is, whose image in the fibre $A(x_j) = A_{x_j} \otimes \kappa(x_j)$ is nonzero for every $j$.
2. Every line bundle $L$ on $X$ is isomorphic to $A \otimes B^{-1}$ with $A$ and $B$ very ample.

Lean: not in Lean as stated.

**Lemma P7.1.2 (cutting by a section).** Let $X$ be a Noetherian scheme, $\mathcal{F}$ a coherent sheaf, $M$ a line bundle and $\sigma \in H^0(X, M)$ a section that does not vanish at any associated point of $\mathcal{F}$. Let $Z(\sigma) = \{ x : \sigma(x) = 0 \}$ be its zero set.

1. Multiplication by $\sigma$ is an injective map $\mathcal{F} \otimes M^{-1} \to \mathcal{F}$. Write $\mathcal{F}_\sigma$ for its cokernel, so that $0 \to \mathcal{F} \otimes M^{-1} \to \mathcal{F} \to \mathcal{F}_\sigma \to 0$ is exact.
2. $\operatorname{Supp} \mathcal{F}_\sigma = \operatorname{Supp} \mathcal{F} \cap Z(\sigma)$.
3. If $X$ is of finite type over $k$ and $\mathcal{F} \neq 0$, then $\dim \operatorname{Supp} \mathcal{F}_\sigma \leq \dim \operatorname{Supp} \mathcal{F} - 1$.

Lean: not in Lean as stated.

**Lemma P7.1.3 (functions with polynomial differences).** Let $d \geq 0$ and let $f \colon \mathbb{Z}^r \to \mathbb{Z}$ be a function such that each difference $\Delta_i f$, $1 \leq i \leq r$, is a numerical polynomial of total degree at most $d - 1$. Then $f$ is a numerical polynomial of total degree at most $d$.

Lean: not in Lean as stated.

**Theorem P7.1.4 (Snapper).** Let $\mathcal{F}$ be a coherent sheaf on $X$ with $\dim \operatorname{Supp} \mathcal{F} \leq d$, where $d \geq 0$, and let $L_1, \dots, L_r$ be line bundles on $X$. There is a numerical polynomial $P_{\mathcal{F}} \in \mathbb{Q}[t_1, \dots, t_r]$ of total degree at most $d$ such that
$$\chi(\mathcal{F} \otimes L^{\mathbf{m}}) = P_{\mathcal{F}}(\mathbf{m}) \quad \text{for all } \mathbf{m} \in \mathbb{Z}^r.$$

Lean: not in Lean as stated.

**Definition P7.1.5 (intersection numbers).** Let $L_1, \dots, L_r$ be line bundles on $X$ and $\mathcal{F}$ a coherent sheaf with $\dim \operatorname{Supp} \mathcal{F} \leq r$. The *intersection number* of $L_1, \dots, L_r$ with $\mathcal{F}$ is
$$(L_1 \cdots L_r \cdot \mathcal{F}) = \sum_{I \subseteq \{1, \dots, r\}} (-1)^{|I|} \, \chi(\mathcal{F} \otimes L_I^{-1}).$$
For a closed subscheme $V \subseteq X$ of dimension at most $r$, write $(L_1 \cdots L_r \cdot V) = (L_1 \cdots L_r \cdot \mathcal{O}_V)$, and if $\dim X = n$, write $(L_1 \cdots L_n) = (L_1 \cdots L_n \cdot X)$. If $L_1 = \dots = L_r = L$, write $(L^r \cdot \mathcal{F})$. For Cartier divisors $D_i$, $(D_1 \cdots D_r \cdot \mathcal{F}) = (\mathcal{O}_X(D_1) \cdots \mathcal{O}_X(D_r) \cdot \mathcal{F})$, and the parentheses are dropped when no confusion is possible: $D^n$, $D \cdot C$, $D_1 \cdots D_r \cdot V$.

**Theorem P7.1.6 (properties of intersection numbers).** Let $L_1, \dots, L_r$ be line bundles on $X$ and $\mathcal{F}$ coherent with $\dim \operatorname{Supp} \mathcal{F} \leq r$.

1. $(L_1 \cdots L_r \cdot \mathcal{F})$ is an integer, and it is the coefficient of $t_1 t_2 \cdots t_r$ in the polynomial $P_{\mathcal{F}}$ of Theorem P7.1.4. It is symmetric in $L_1, \dots, L_r$ and depends only on their isomorphism classes.
2. If $\dim \operatorname{Supp} \mathcal{F} < r$, then $(L_1 \cdots L_r \cdot \mathcal{F}) = 0$.
3. (Additivity.) For an exact sequence $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$ of coherent sheaves with supports of dimension at most $r$, $(L_1 \cdots L_r \cdot \mathcal{F}) = (L_1 \cdots L_r \cdot \mathcal{F}') + (L_1 \cdots L_r \cdot \mathcal{F}'')$.
4. (Multilinearity.) For a line bundle $L_1'$, $((L_1 \otimes L_1') \cdot L_2 \cdots L_r \cdot \mathcal{F}) = (L_1 \cdot L_2 \cdots L_r \cdot \mathcal{F}) + (L_1' \cdot L_2 \cdots L_r \cdot \mathcal{F})$. In particular $(L_1^{-1} \cdot L_2 \cdots L_r \cdot \mathcal{F}) = -(L_1 \cdots L_r \cdot \mathcal{F})$ and $(\mathcal{O}_X \cdot L_2 \cdots L_r \cdot \mathcal{F}) = 0$.
5. (Twisting.) For every line bundle $M$, $(L_1 \cdots L_r \cdot \mathcal{F} \otimes M) = (L_1 \cdots L_r \cdot \mathcal{F})$.
6. (Cutting.) Let $r \geq 1$ and let $\sigma \in H^0(X, L_r)$ be a section that does not vanish at any associated point of $\mathcal{F}$. Then $(L_1 \cdots L_r \cdot \mathcal{F}) = (L_1 \cdots L_{r-1} \cdot \mathcal{F}_\sigma)$, with $\mathcal{F}_\sigma$ as in Lemma P7.1.2. In particular, if $V$ is a closed subscheme of dimension at most $r$ and $D$ is an effective Cartier divisor whose local equations are nonzerodivisors on $\mathcal{O}_V$, then $(L_1 \cdots L_{r-1} \cdot D \cdot V) = (L_1 \cdots L_{r-1} \cdot V \cap D)$, where $V \cap D$ is the scheme-theoretic intersection.
7. (Restriction.) Let $i \colon Y \to X$ be a closed immersion and $\mathcal{G}$ a coherent sheaf on $Y$ with $\dim \operatorname{Supp} \mathcal{G} \leq r$. Then $(L_1 \cdots L_r \cdot i_* \mathcal{G}) = (i^* L_1 \cdots i^* L_r \cdot \mathcal{G})$, the second number computed on $Y$.

Lean: not in Lean as stated.

**Proposition P7.1.7 (small dimension).**

1. If $\dim \operatorname{Supp} \mathcal{F} \leq 0$, the intersection number with no line bundles is $(\cdot \mathcal{F}) = \chi(\mathcal{F}) = h^0(\mathcal{F}) = \sum_{x} \operatorname{length}_{\mathcal{O}_{X,x}} \mathcal{F}_x$.
2. If $C \subseteq X$ is an integral curve, then $(L \cdot C) = \deg(L|_C)$, the degree of Theorem P5.3.10, which is the degree of the pullback of $L$ to the normalization of $C$.
3. If $X = S$ is a smooth projective surface, then $(L \cdot M)$ is the intersection pairing of Definition P5.5.4.

Lean: not in Lean as stated.

### Proof in words

The Euler characteristic $\chi(\mathcal{F} \otimes L^m)$ of a single ample $L$ is a polynomial in $m$ of degree $\dim \operatorname{Supp} \mathcal{F}$, by Theorem P4.3.4. Snapper's theorem is the same statement for several line bundles, none of them ample, and the proof is the proof of Theorem P4.3.4 run on differences. Each line bundle is a difference of two very ample ones. For a very ample $A$, a general section $\sigma$ of $A$ does not vanish at the finitely many associated points of $\mathcal{F}$, so it cuts $\mathcal{F}$ to a sheaf $\mathcal{F}_\sigma$ with smaller support, and the exact sequence $0 \to \mathcal{F} \otimes A^{-1} \to \mathcal{F} \to \mathcal{F}_\sigma \to 0$ says that the difference of the function $\chi(\mathcal{F} \otimes L^{\mathbf{m}})$ in the variable of $A$ is the Euler characteristic of $\mathcal{F}_\sigma$. By induction on the dimension of the support, every difference is a polynomial of smaller degree, and a function whose differences are polynomials is a polynomial.

Once $\chi(\mathcal{F} \otimes L^{\mathbf{m}})$ is a polynomial of total degree at most $r$ in $r$ variables, its coefficient of $t_1 \cdots t_r$ is the iterated difference $\Delta_1 \cdots \Delta_r$ evaluated at $0$, which is the alternating sum of Definition P7.1.5. All properties follow from that identity. Additivity in $\mathcal{F}$ is additivity of $\chi$. Multilinearity follows from Snapper's theorem with one more variable: the coefficient of $t_1 t_2 \cdots t_r$ after the substitution $t_1 = t_1' = t$ is the sum of two coefficients. Cutting by a section is the alternating sum taken in two steps.

### Examples

**Example P7.1.8 (projective space).** Let $X = \mathbb{P}^n_k$ and $H = \mathcal{O}(1)$. By Theorem P4.2.1, $\chi(\mathcal{O}(m)) = \binom{m + n}{n}$ for every $m \in \mathbb{Z}$. With $L_1 = \dots = L_n = H$, the polynomial of Theorem P7.1.4 is $P(\mathbf{t}) = \binom{t_1 + \dots + t_n + n}{n}$, whose part of total degree $n$ is $(t_1 + \dots + t_n)^n / n!$. The coefficient of $t_1 \cdots t_n$ in $(t_1 + \dots + t_n)^n$ is $n!$, so $(H^n) = 1$. By multilinearity, $(\mathcal{O}(d_1) \cdots \mathcal{O}(d_n)) = d_1 \cdots d_n$. For $n = 2$ the alternating sum can be checked by hand: $\chi(\mathcal{O}) - 2\chi(\mathcal{O}(-1)) + \chi(\mathcal{O}(-2)) = 1 - 0 + 0 = 1$.

**Example P7.1.9 (the quadric surface).** Let $X = \mathbb{P}^1 \times \mathbb{P}^1$ and $\mathcal{O}(a, b) = p_1^* \mathcal{O}(a) \otimes p_2^* \mathcal{O}(b)$. By the Künneth formula, as in Example P5.5.9, $\chi(\mathcal{O}(a, b)) = (a + 1)(b + 1)$ for all $a, b$. Definition P7.1.5 gives
$$(\mathcal{O}(a, b) \cdot \mathcal{O}(c, d)) = 1 - (1 - a)(1 - b) - (1 - c)(1 - d) + (1 - a - c)(1 - b - d) = ad + bc.$$
So $\mathcal{O}(1, 0)^2 = 0$, $\mathcal{O}(1, 0) \cdot \mathcal{O}(0, 1) = 1$ and $\mathcal{O}(1, 1)^2 = 2$, the degree of the quadric in $\mathbb{P}^3$.

**Example P7.1.10 (a double line).** Let $X = \mathbb{P}^2$ with coordinates $x, y, z$, let $\ell = V_+(x)$ and $V = V_+(x^2)$, the double line. Multiplication by $x$ gives an exact sequence $0 \to \mathcal{O}_\ell(-1) \to \mathcal{O}_V \to \mathcal{O}_\ell \to 0$. By additivity and twisting, $(H \cdot V) = (H \cdot \mathcal{O}_\ell(-1)) + (H \cdot \mathcal{O}_\ell) = 2 (H \cdot \ell) = 2$. The intersection number sees the nonreduced structure, as it must for $V$ to be a conic in the family $V_+(x^2 - t yz)$. A direct computation agrees: $\chi(\mathcal{O}_V(m)) = \chi(\mathcal{O}(m)) - \chi(\mathcal{O}(m - 2)) = 2m + 1$, and $(H \cdot V) = \chi(\mathcal{O}_V) - \chi(\mathcal{O}_V(-1)) = 1 - (-1) = 2$.

**Example P7.1.11 (a curve of degree $d$).** Let $C \subseteq \mathbb{P}^2$ be a plane curve of degree $d$, possibly reducible or nonreduced, and $L = \mathcal{O}(e)|_C$. From $0 \to \mathcal{O}(m - d) \to \mathcal{O}(m) \to \mathcal{O}_C(m) \to 0$, $\chi(\mathcal{O}_C(m)) = dm + 1 - \frac{(d-1)(d-2)}{2}$, so $(\mathcal{O}(1) \cdot C) = d$ and $(\mathcal{O}(e) \cdot C) = de$. By part 6 of Theorem P7.1.6 this is $(\mathcal{O}(1) \cdot \mathcal{O}(d))$ on $\mathbb{P}^2$, which is $d$ by Example P7.1.8. It is the first case of Bézout's theorem, Example P7.1.21 below.

### Proof

*Lemma P7.1.1.* For part 1, let $A \cong i^* \mathcal{O}(1)$ for an immersion $i \colon X \to \mathbb{P}^N_k$, which is a closed immersion by part 3 of Proposition P3.6.24 because $X$ is proper. For each $j$, the point $i(x_j)$ lies in some open set $D_+(x_l)$, so the linear forms $\lambda \in H^0(\mathbb{P}^N, \mathcal{O}(1))$ that vanish at $i(x_j)$ form a proper linear subspace $W_j$ of $H^0(\mathbb{P}^N, \mathcal{O}(1)) = k^{N+1}$. A vector space over an infinite field is not a finite union of proper subspaces: if $W_1 \cup \dots \cup W_s = k^{N+1}$ with $s$ minimal, pick $u \in W_1$ outside $W_2 \cup \dots \cup W_s$ and $v \notin W_1$. The line $\{ v + c u : c \in k \}$ meets $W_1$ in no point and meets each other $W_j$ in at most one point, so it is covered by $s - 1$ points, which is absurd because $k$ is infinite. A linear form $\lambda$ outside all $W_j$ gives $\sigma = i^* \lambda$.

For part 2, fix a very ample $H$. It is ample by Proposition P3.6.24, so by part 2 of Proposition P3.10.27 the bundles $L \otimes H^m$ and $H^m = \mathcal{O}_X \otimes H^m$ are very ample for $m$ large. Then $L \cong (L \otimes H^m) \otimes (H^m)^{-1}$. $\square$

*Lemma P7.1.2.* The statements are local. Let $x \in X$, trivialize $M$ near $x$, and let $f \in \mathcal{O}_{X,x}$ be the image of $\sigma$. The associated primes of the $\mathcal{O}_{X,x}$-module $\mathcal{F}_x$ are the associated points $y$ of $\mathcal{F}$ with $x \in \overline{\{y\}}$, and $\sigma(y) \neq 0$ means $f \notin \mathfrak{p}_y$. Let $K \subseteq \mathcal{F}_x$ be the kernel of multiplication by $f$. If $K \neq 0$, it has an associated prime $\mathfrak{p}$ by Proposition P1.2.44, and $\mathfrak{p} \in \operatorname{Ass}(\mathcal{F}_x)$ by Lemma P1.2.45. Since $f$ kills $K$, $f$ lies in the annihilator of an element of $K$, which is $\mathfrak{p}$. This contradicts the hypothesis, so $K = 0$ and part 1 holds. For part 2, $(\mathcal{F}_\sigma)_x = \mathcal{F}_x / f \mathcal{F}_x$, which is zero if $f$ is a unit, and nonzero by Nakayama's lemma if $f \in \mathfrak{m}_x$ and $\mathcal{F}_x \neq 0$. For part 3, let $Z$ be an irreducible component of $\operatorname{Supp} \mathcal{F}$, with generic point $\eta$. By Theorem P1.2.48, $\eta$ is an associated point of $\mathcal{F}$, so $\sigma(\eta) \neq 0$ and $Z \cap Z(\sigma)$ is a proper closed subset of $Z$. Each irreducible component $W$ of $Z \cap Z(\sigma)$ has $\operatorname{codim}(W, Z) \geq 1$, so $\dim W \leq \dim Z - 1$ by part 4 of Theorem P3.7.4, applied to $Z$ with its reduced structure. Taking all components $Z$ gives part 3. $\square$

*Lemma P7.1.3.* Induction on $r$. If $r = 0$, $f$ is a constant, a numerical polynomial of degree at most $0 \leq d$. Let $r \geq 1$ and write $\mathbf{m} = (\mathbf{m}', t)$ with $\mathbf{m}' \in \mathbb{Z}^{r-1}$. The difference $P = \Delta_r f$ is a numerical polynomial of total degree at most $d - 1$; write $P(\mathbf{m}', t) = \sum_{j = 0}^{d-1} p_j(\mathbf{m}') t^j$ with $p_j \in \mathbb{Q}[t_1, \dots, t_{r-1}]$ of total degree at most $d - 1 - j$. For each $j \geq 0$ there is $S_j \in \mathbb{Q}[t]$ of degree $j + 1$ with $S_j(t) - S_j(t - 1) = t^j$ and $S_j(0) = 0$. Indeed, the linear map $S \mapsto S(t) - S(t - 1)$ from the polynomials of degree at most $j + 1$ to those of degree at most $j$ has as kernel the constants, because a polynomial with $S(t) = S(t - 1)$ takes the value $S(0)$ at every integer. By dimension count it is surjective, and the constant can be adjusted so that $S_j(0) = 0$. Put
$$Q(\mathbf{m}', t) = \sum_{j=0}^{d-1} p_j(\mathbf{m}') \, S_j(t).$$
It is a polynomial of total degree at most $d$, $Q(\mathbf{m}', t) - Q(\mathbf{m}', t - 1) = P(\mathbf{m}', t)$ and $Q(\mathbf{m}', 0) = 0$. Telescoping gives $Q(\mathbf{m}', t) = \sum_{u = 1}^{t} P(\mathbf{m}', u)$ for $t \geq 0$ and $Q(\mathbf{m}', t) = - \sum_{u = t + 1}^{0} P(\mathbf{m}', u)$ for $t < 0$, so $Q$ takes integer values on $\mathbb{Z}^r$. The function $h = f - Q$ has $\Delta_r h = 0$, so $h(\mathbf{m}', t) = h(\mathbf{m}', 0) = f(\mathbf{m}', 0)$ for every $t$. The function $g(\mathbf{m}') = f(\mathbf{m}', 0)$ on $\mathbb{Z}^{r-1}$ has differences $\Delta_i g(\mathbf{m}') = (\Delta_i f)(\mathbf{m}', 0)$ for $i < r$, which are numerical polynomials of total degree at most $d - 1$. By induction $g$ is a numerical polynomial of total degree at most $d$, and so is $f = Q + g$. $\square$

*Theorem P7.1.4.* By part 2 of Lemma P7.1.1 write $L_i \cong A_i \otimes B_i^{-1}$ with $A_i$, $B_i$ very ample. Consider the function of $2r$ variables
$$f(\mathbf{a}, \mathbf{b}) = \chi(\mathcal{F} \otimes A^{\mathbf{a}} \otimes B^{\mathbf{b}}), \qquad \mathbf{a}, \mathbf{b} \in \mathbb{Z}^r.$$
It suffices to prove that $f$ is a numerical polynomial of total degree at most $\dim \operatorname{Supp} \mathcal{F}$: then $\chi(\mathcal{F} \otimes L^{\mathbf{m}}) = f(\mathbf{m}, -\mathbf{m})$ is a polynomial in $\mathbf{m}$ of no larger total degree with integer values. The proof is by induction on $e = \dim \operatorname{Supp} \mathcal{F} \geq -1$, for the statement that $f$ is a numerical polynomial of total degree at most $e$, with the convention that degree at most $-1$ means $f = 0$. If $e = -1$, then $\mathcal{F} = 0$ and $f = 0$.

Let $e \geq 0$. The associated points of $\mathcal{F}$ are finite in number, by Theorem P1.2.46 on a finite affine cover of $X$. By part 1 of Lemma P7.1.1 there is a section $\sigma_i$ of $A_i$ that does not vanish at any of them, and similarly a section $\tau_i$ of $B_i$. Tensoring the sequence of Lemma P7.1.2 for $\sigma_i$ with the line bundle $A^{\mathbf{a}} \otimes B^{\mathbf{b}}$, which preserves exactness, gives
$$0 \to \mathcal{F} \otimes A^{\mathbf{a} - \mathbf{e}_i} \otimes B^{\mathbf{b}} \to \mathcal{F} \otimes A^{\mathbf{a}} \otimes B^{\mathbf{b}} \to \mathcal{F}_{\sigma_i} \otimes A^{\mathbf{a}} \otimes B^{\mathbf{b}} \to 0.$$
By additivity of $\chi$ (Proposition P4.3.2), the difference of $f$ in the variable $a_i$ is $\chi(\mathcal{F}_{\sigma_i} \otimes A^{\mathbf{a}} \otimes B^{\mathbf{b}})$. By part 3 of Lemma P7.1.2, $\dim \operatorname{Supp} \mathcal{F}_{\sigma_i} \leq e - 1$, so by induction this difference is a numerical polynomial of total degree at most $e - 1$. The same holds for the difference in $b_i$, with $\tau_i$. By Lemma P7.1.3, applied with $d = e$, $f$ is a numerical polynomial of total degree at most $e$. $\square$

*Theorem P7.1.6.* Let $P = P_{\mathcal{F}}$ be the polynomial of Theorem P7.1.4, of total degree at most $r$. For a monomial $\mathbf{t}^{\mathbf{a}} = t_1^{a_1} \cdots t_r^{a_r}$, the difference $\Delta_i \mathbf{t}^{\mathbf{a}}$ has degree $a_i - 1$ in $t_i$, it does not involve higher powers of the other variables, and it is zero if $a_i = 0$. So $\Delta_1 \cdots \Delta_r \mathbf{t}^{\mathbf{a}}$ is zero unless every $a_i \geq 1$, and if also $|\mathbf{a}| \leq r$, then $\mathbf{a} = (1, \dots, 1)$, with $\Delta_1 \cdots \Delta_r (t_1 \cdots t_r) = 1$. So $\Delta_1 \cdots \Delta_r P$ is the constant $c$, the coefficient of $t_1 \cdots t_r$ in $P$. Expanding the iterated difference at $\mathbf{m} = 0$,
$$c = (\Delta_1 \cdots \Delta_r P)(0) = \sum_{I \subseteq \{1, \dots, r\}} (-1)^{|I|} P(- \mathbf{e}_I) = \sum_I (-1)^{|I|} \chi(\mathcal{F} \otimes L_I^{-1}),$$
with $\mathbf{e}_I = \sum_{i \in I} \mathbf{e}_i$. This proves the identity of part 1. The alternating sum is an integer, symmetric in the $L_i$, and it depends only on isomorphism classes. Part 2 follows, because then $P$ has total degree at most $r - 1$ and no monomial $t_1 \cdots t_r$. Part 3 follows from the additivity of $\chi$ in the alternating sum, because tensoring with $L_I^{-1}$ is exact.

For part 4, apply Theorem P7.1.4 to the $r + 1$ line bundles $L_1, L_1', L_2, \dots, L_r$: $\chi(\mathcal{F} \otimes L_1^{u} \otimes L_1'^{u'} \otimes L_2^{m_2} \otimes \cdots) = R(u, u', m_2, \dots, m_r)$ with $R$ of total degree at most $r$. Setting $u' = 0$ deletes the monomials that involve $u'$ and does not change the coefficient of $u m_2 \cdots m_r$, so this coefficient is $(L_1 \cdots L_r \cdot \mathcal{F})$ by part 1. In the same way the coefficient of $u' m_2 \cdots m_r$ is $(L_1' L_2 \cdots L_r \cdot \mathcal{F})$. Setting $u = u' = t$ gives the polynomial of $L_1 \otimes L_1', L_2, \dots, L_r$. A monomial $u^\alpha u'^\beta m_2^{c_2} \cdots m_r^{c_r}$ of $R$ becomes $t^{\alpha + \beta} m_2^{c_2} \cdots$, and it contributes to $t m_2 \cdots m_r$ only if $\alpha + \beta = 1$ and all $c_j = 1$. So the coefficient of $t m_2 \cdots m_r$ is the sum of the two coefficients above. The two special cases follow from $L_1 \otimes L_1^{-1} \cong \mathcal{O}_X$ and from $\mathcal{O}_X \otimes \mathcal{O}_X \cong \mathcal{O}_X$.

For part 5, apply Theorem P7.1.4 to $L_1, \dots, L_r, M$: $\chi(\mathcal{F} \otimes L^{\mathbf{m}} \otimes M^{u}) = R(\mathbf{m}, u)$ of total degree at most $r$. The coefficient of $t_1 \cdots t_r$ in $R(\mathbf{t}, u)$, viewed as a polynomial in $\mathbf{t}$ for fixed $u$, comes from the monomials $t_1 \cdots t_r u^\beta$, and these have $\beta = 0$ by the degree bound. So it does not depend on $u$. The values $u = 0$ and $u = 1$ give part 5, by part 1.

For part 6, by Lemma P7.1.2 the sequence $0 \to \mathcal{F} \otimes L_r^{-1} \to \mathcal{F} \to \mathcal{F}_\sigma \to 0$ is exact, and $\dim \operatorname{Supp} \mathcal{F}_\sigma \leq r - 1$. Split the sum of Definition P7.1.5 according to whether $r \in I$:
$$(L_1 \cdots L_r \cdot \mathcal{F}) = \sum_{J \subseteq \{1, \dots, r-1\}} (-1)^{|J|} \bigl( \chi(\mathcal{F} \otimes L_J^{-1}) - \chi(\mathcal{F} \otimes L_r^{-1} \otimes L_J^{-1}) \bigr) = \sum_J (-1)^{|J|} \chi(\mathcal{F}_\sigma \otimes L_J^{-1}),$$
which is $(L_1 \cdots L_{r-1} \cdot \mathcal{F}_\sigma)$. For the special case take $\mathcal{F} = \mathcal{O}_V$ and $\sigma$ the canonical section of $\mathcal{O}_X(D)$. Its local equation is a nonzerodivisor on $\mathcal{O}_V$, which means that $\sigma$ does not vanish at an associated point of $\mathcal{O}_V$, and the cokernel of $\sigma$ is $\mathcal{O}_V / \mathcal{O}_V(-D) = \mathcal{O}_{V \cap D}$. Part 7 follows from $\chi(X, i_* \mathcal{G}') = \chi(Y, \mathcal{G}')$ (part 2 of Proposition P4.3.2) and the projection formula $i_* \mathcal{G} \otimes L_I^{-1} \cong i_* (\mathcal{G} \otimes i^* L_I^{-1})$. $\square$

*Proposition P7.1.7.* Part 1: with $r = 0$ the sum has the single term $I = \emptyset$. A coherent sheaf with finite support is a finite direct sum of skyscraper sheaves, so it has no higher cohomology and $h^0$ is the sum of the lengths, by Corollary P1.3.29. Part 2: by part 7 of Theorem P7.1.6, $(L \cdot C) = \chi(\mathcal{O}_C) - \chi(L^{-1}|_C)$ on $C$, and by Theorem P5.3.10 this is $(1 - p_a) - (-\deg L|_C + 1 - p_a) = \deg L|_C$. Part 3: for $r = 2$, Definition P7.1.5 is the formula of Definition P5.5.4. $\square$

### Exercises

1. (A) Compute $(\mathcal{O}(1)^2 \cdot \mathcal{O}(2))$ on $\mathbb{P}^3$ in two ways: from the alternating sum of Definition P7.1.5, and from part 6 of Theorem P7.1.6 and the quadric of Example P7.1.9.
2. (A) Let $\mathcal{F}$ be coherent with $\dim \operatorname{Supp} \mathcal{F} \leq r$ and $L_1 = \mathcal{O}_X$. Check directly from Definition P7.1.5 that $(L_1 \cdots L_r \cdot \mathcal{F}) = 0$.
3. (B) Let $V = V_+(x^2, xy) \subseteq \mathbb{P}^2$, the line $x = 0$ with an embedded point. Show that $(H \cdot V) = 1$, and that $\chi(\mathcal{O}_V)$ differs from $\chi(\mathcal{O}_\ell)$. So the intersection number of a line bundle with a one-dimensional scheme ignores embedded points, while the Euler characteristic does not.
4. (B) Let $\mathcal{F}$ be coherent with $\dim \operatorname{Supp} \mathcal{F} = r$ and $L$ ample. Show that $(L^r \cdot \mathcal{F})$ is $r!$ times the leading coefficient of the Hilbert polynomial of $\mathcal{F}$ with respect to $L$, and is positive. Use Theorem P4.3.4 for a very ample power of $L$.
5. (B) Show that the function $f(m_1, m_2) = \binom{m_1 + m_2}{2}$ satisfies the hypothesis of Lemma P7.1.3 with $d = 2$, and write it in the form $Q + g$ of the proof.
6. (C) Let $X$ be projective of dimension $n$ and $L_1, \dots, L_n$ line bundles. Prove that $(L_1 \cdots L_n)$ is determined by the values $(M^n)$ for $M$ in the subgroup of $\operatorname{Pic}(X)$ generated by the $L_i$, through the polarization identity $n! \, (L_1 \cdots L_n) = \sum_{I} (-1)^{n - |I|} (L_I^n)$, the sum over nonempty $I \subseteq \{1, \dots, n\}$.

### Lean

Mathlib has no Euler characteristic of a coherent sheaf on a projective scheme, so neither Snapper's theorem nor Definition P7.1.5 is in Mathlib. It has `Polynomial` and multivariate `MvPolynomial`, and Lemma P7.1.3 is a statement about them that could be formalized directly. The project library takes the intersection numbers of $\mathbb{R}$-divisors with curves as the data of a structure `MinimalModel.IntersectionData`, whose field `dot` gives $D \cdot C$; on a Cartier divisor its value is fixed by `MinimalModel.IsIntersectionNumber`, the degree of $\mathcal{O}(D)$ on the normalization of $C$, which is part 2 of Proposition P7.1.7. The handbook adds no `MinimalModel` node here.

### Notes and history

The Euler characteristic definition of intersection numbers is due to Snapper, who proved in 1959 that $\chi(\mathcal{F} \otimes L_1^{m_1} \otimes \cdots \otimes L_r^{m_r})$ is a polynomial, and to Kleiman, who took the coefficient of $m_1 \cdots m_r$ as the definition and derived its properties in Chapter I of *Toward a numerical theory of ampleness* (1966). The literature state is theorem. Its advantage over Weil's and Fulton's definitions through intersection multiplicities is that it needs no moving lemma and works for arbitrary coherent sheaves on arbitrary projective schemes; its disadvantage is that it gives a number, not a cycle, so it cannot compute intersections of subvarieties of dimension larger than the expected one. Fulton's *Intersection theory* gives the refined theory. In the minimal model program the numbers $(L_1 \cdots L_r \cdot V)$ are used for singular and reducible $X$, for instance on the exceptional locus of a contraction or on a nonnormal fibre, and the definition through $\chi$ is the one that applies there without change.
