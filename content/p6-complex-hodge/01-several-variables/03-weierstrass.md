---
title: Weierstrass preparation and the local ring O_n
nodes: []
sources: [Huy05, Hor90, GR65, GH78]
reads_with: [Huy05:1.1, Hor90:VI.1, GR65:II.B, GH78:0.1]
requires: [P1.3, P1.4, P1.5, P1.6, P1.9]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Weierstrass preparation and the local ring O_n

### Statement

For $n \geq 1$ write $z = (z', z_n)$ with $z' = (z_1, \dots, z_{n-1})$, and $\mathbb{C}\{z\} \subseteq \mathbb{C}[[z_1, \dots, z_n]]$ for the subring of power series that converge on some polydisc about $0$.

**Definition P6.1.20 (germs and the ring O_n).** Let $X \subseteq \mathbb{C}^n$ be open and $a \in X$. Two holomorphic functions on open neighbourhoods of $a$ have the same *germ* at $a$ if they agree on some neighbourhood of $a$. The germs form the stalk $\mathcal{O}_{X, a} = \varinjlim_{U \ni a} \mathcal{O}(U)$ of the sheaf $\mathcal{O}_X$, a $\mathbb{C}$-algebra. Translation identifies all stalks with $\mathcal{O}_n = \mathcal{O}_{\mathbb{C}^n, 0}$, the *ring of convergent power series*; $\mathcal{O}_0 = \mathbb{C}$. A germ $f$ has a well defined value $f(0)$ and Taylor series $\sum_\alpha c_\alpha z^\alpha$. The *order* $\operatorname{ord} f$ of $f \neq 0$ is the least $|\alpha|$ with $c_\alpha \neq 0$.

**Proposition P6.1.21 (first properties of O_n).**

1. The Taylor map $\mathcal{O}_n \to \mathbb{C}[[z_1, \dots, z_n]]$ is an injective ring homomorphism with image $\mathbb{C}\{z\}$.
2. $\mathcal{O}_n$ is a domain, and $\operatorname{ord}(fg) = \operatorname{ord} f + \operatorname{ord} g$.
3. A germ $f$ is a unit if and only if $f(0) \neq 0$. So $\mathcal{O}_n$ is a local ring with maximal ideal $\mathfrak{m} = \{ f : f(0) = 0 \}$, and $\mathfrak{m} = (z_1, \dots, z_n)$.
4. For $k \geq 0$, $\mathfrak{m}^k$ is the ideal of germs of order at least $k$ (with $0$), and $\bigcap_k \mathfrak{m}^k = 0$.
5. Restriction to $\{ z_n = 0 \}$ induces an isomorphism $\mathcal{O}_n / (z_n) \cong \mathcal{O}_{n-1}$. More generally $\mathcal{O}_n / (z_{k+1}, \dots, z_n) \cong \mathcal{O}_k$.

Lean: not yet in Lean.

**Definition P6.1.22 (regular germs and Weierstrass polynomials).** A germ $f \in \mathcal{O}_n$ is *regular of order $d$ in $z_n$* if the germ $f(0', z_n) \in \mathcal{O}_1$ has order exactly $d$, that is, $f(0', z_n) = z_n^d u(z_n)$ with $u(0) \neq 0$. A *Weierstrass polynomial of degree $d$* is an element
$$P = z_n^d + a_1(z') z_n^{d-1} + \dots + a_d(z') \in \mathcal{O}_{n-1}[z_n] \quad \text{with } a_1(0) = \dots = a_d(0) = 0.$$
A Weierstrass polynomial of degree $d$ is regular of order $d$ in $z_n$, since $P(0', z_n) = z_n^d$. Here and below $\mathcal{O}_{n-1}$ is viewed as the subring of $\mathcal{O}_n$ of germs independent of $z_n$.

**Lemma P6.1.23 (regularity after a linear change of coordinates).** Let $0 \neq f \in \mathcal{O}_n$ have order $d$, and let $f_d$ be the homogeneous part of degree $d$ of its Taylor series. For every $v \in \mathbb{C}^n$ with $f_d(v) \neq 0$, which is a nonempty Zariski open set of $v$, and every $A \in GL_n(\mathbb{C})$ with $A e_n = v$, the germ $f \circ A$ is regular of order $d$ in $z_n$. The map $g \mapsto g \circ A$ is an automorphism of the ring $\mathcal{O}_n$ that preserves orders.

Lean: not yet in Lean.

**Theorem P6.1.24 (Weierstrass division theorem).** Let $g \in \mathcal{O}_n$ be regular of order $d$ in $z_n$. For every $f \in \mathcal{O}_n$ there are unique $q \in \mathcal{O}_n$ and $r \in \mathcal{O}_{n-1}[z_n]$ of degree less than $d$ in $z_n$ with
$$f = q g + r.$$
Equivalently, $\mathcal{O}_n / (g)$ is a free $\mathcal{O}_{n-1}$-module with basis the classes of $1, z_n, \dots, z_n^{d-1}$.

Lean: not yet in Lean.

**Theorem P6.1.25 (Weierstrass preparation theorem).** Let $g \in \mathcal{O}_n$ be regular of order $d$ in $z_n$. There are a unique unit $u \in \mathcal{O}_n$ and a unique Weierstrass polynomial $P$ of degree $d$ with $g = u P$. If $g$ is holomorphic on a neighbourhood of a closed polydisc $\bar\Delta' \times \{ |z_n| \leq \rho \}$, with $g(0', t) \neq 0$ for $0 < |t| \leq \rho$ and $g(z', t) \neq 0$ for $z' \in \bar\Delta'$, $|t| = \rho$, then $P(z', \cdot)$ is the monic polynomial whose roots are the zeros of $g(z', \cdot)$ in $\{|t| < \rho\}$, counted with multiplicity.

Lean: not yet in Lean.

**Theorem P6.1.26 (O_n is Noetherian).** The ring $\mathcal{O}_n$ is Noetherian.

Lean: not yet in Lean.

**Lemma P6.1.27 (Weierstrass polynomials and divisibility).** Let $P \in \mathcal{O}_{n-1}[z_n]$ be a Weierstrass polynomial of degree $d$.

1. If $f \in \mathcal{O}_{n-1}[z_n]$ and $f = h P$ with $h \in \mathcal{O}_n$, then $h \in \mathcal{O}_{n-1}[z_n]$.
2. If $P = Q_1 Q_2$ with $Q_1, Q_2 \in \mathcal{O}_{n-1}[z_n]$ monic, then $Q_1$ and $Q_2$ are Weierstrass polynomials.
3. $P$ is irreducible in $\mathcal{O}_n$ if and only if it is irreducible in $\mathcal{O}_{n-1}[z_n]$.

Lean: not yet in Lean.

**Theorem P6.1.28 (O_n is factorial).** The ring $\mathcal{O}_n$ is a unique factorization domain.

Lean: not yet in Lean.

**Corollary P6.1.29 (O_n is a regular local ring).** The ring $\mathcal{O}_n$ is a Noetherian local ring of dimension $n$ whose maximal ideal is generated by $z_1, \dots, z_n$, so it is a regular local ring (Definition P1.9.1), and it is normal. Its $\mathfrak{m}$-adic completion is $\mathbb{C}[[z_1, \dots, z_n]]$.

Lean: not yet in Lean.

### Proof in words

The Weierstrass theorems reduce germs in $n$ variables to polynomials in one variable over germs in $n - 1$ variables. For $g$ regular of order $d$ in $z_n$, the slice $g(z', \cdot)$ has exactly $d$ zeros near $0$ for each small $z'$ by the argument principle. Their power sums are residue integrals, hence holomorphic in $z'$, so the monic polynomial $P$ with these roots has holomorphic coefficients, and $g/P$ is a nonvanishing holomorphic function by a Cauchy integral. Division by the monic $P$ is a Cauchy integral whose remainder is visibly a polynomial of degree less than $d$, and uniqueness is root counting. Preparation then follows from dividing $z_n^d$ by $g$. Once $\mathcal{O}_n / (g)$ is a finite $\mathcal{O}_{n-1}$-module, induction on $n$ gives Noetherianity. For factoriality, a Weierstrass polynomial that is irreducible in $\mathcal{O}_n$ is irreducible in the polynomial ring over the factorial ring $\mathcal{O}_{n-1}$, hence prime there by Gauss's lemma, and divisibility in $\mathcal{O}_n$ and in the polynomial ring agree. The dimension is $n$ by the chain of coordinate primes and Krull's height theorem.

### Examples

**Example P6.1.30 (preparation in examples).** (a) Let $g = \sin z_2 - z_1 \in \mathcal{O}_2$. Then $g(0, z_2) = \sin z_2$ has order $1$, so $g$ is regular of order $1$ in $z_2$. For small $z_1$ the unique zero of $\sin(\cdot) - z_1$ near $0$ is $\arcsin z_1 = z_1 + z_1^3/6 + \dots$ in the sense of its convergent Taylor series, so $P = z_2 - \arcsin z_1$ and $u = (\sin z_2 - z_1)/(z_2 - \arcsin z_1)$, a germ with $u(0) = \lim_{t \to 0} \sin t / t = 1$. Division of $f = z_2^2$ by $g$ has remainder $r = (\arcsin z_1)^2$, the value of $f$ at the root.

(b) Let $g = z_1 z_2$. It is not regular in $z_2$, since $g(0, z_2) = 0$, nor in $z_1$. Its homogeneous part of degree $2$ is $f_2 = z_1 z_2$, and $v = (1, 1)$ has $f_2(v) = 1$. With $A(w_1, w_2) = (w_1 + w_2, w_2)$, so that $A e_2 = v$, the germ $g \circ A = w_2^2 + w_1 w_2$ is a Weierstrass polynomial of degree $2$ in $w_2$, and it factors as $w_2 (w_2 + w_1)$ into Weierstrass polynomials of degree $1$, as Lemma P6.1.27 predicts.

(c) Let $g = z_2^2 - z_1^3$, a Weierstrass polynomial of degree $2$ in $z_2$. It is irreducible in $\mathcal{O}_1[z_2]$: a factorization into monic factors of degree $1$ would give a root $c(z_1) \in \mathcal{O}_1$ with $c^2 = z_1^3$, impossible since $\operatorname{ord} c^2$ is even. By Lemma P6.1.27, $g$ is irreducible in $\mathcal{O}_2$, so by Theorem P6.1.28 the cusp $\{z_2^2 = z_1^3\}$ is defined by a prime element.

**Example P6.1.31 (smooth germs do not form a Noetherian ring).** Let $\mathcal{E}_1$ be the ring of germs at $0$ of $C^\infty$ real functions on $\mathbb{R}$. It is local with maximal ideal $\mathfrak{m} = \{ f : f(0) = 0 \}$, since a germ with $f(0) \neq 0$ has the inverse $1/f$. By Taylor's formula with integral remainder, $f = \sum_{j < k} f^{(j)}(0) x^j / j! + x^k \int_0^1 \frac{(1-t)^{k-1}}{(k-1)!} f^{(k)}(tx) \, dt$, so $\mathfrak{m} = (x)$ and $\mathfrak{m}^k = (x^k)$ is the ideal of germs with $f^{(j)}(0) = 0$ for $j < k$. The germ $\varphi(x) = e^{-1/x^2}$ ($\varphi(0) = 0$) has all derivatives $0$ at $0$, so $\varphi \in \bigcap_k \mathfrak{m}^k$, and $\varphi \neq 0$. If $\mathcal{E}_1$ were Noetherian, Krull's intersection theorem (Theorem P1.6.6) for the local ring $\mathcal{E}_1$ would give $\bigcap_k \mathfrak{m}^k = 0$. So $\mathcal{E}_1$ is not Noetherian, and the Weierstrass theorems fail for smooth germs in the form above. For $\mathcal{O}_n$ the hypothesis of the identity theorem is exactly what makes $\bigcap_k \mathfrak{m}^k = 0$ (part 4 of Proposition P6.1.21).

### Proof

*Proof of Proposition P6.1.21.* Part 1: the Taylor map is a ring homomorphism because products and sums of absolutely convergent series are computed termwise; it is injective by Theorem P6.1.4, since a function on a polydisc is the sum of its Taylor series, and its image is $\mathbb{C}\{z\}$ by part 3 of the same theorem. Part 2: if $f, g \neq 0$ with lowest homogeneous parts $f_d$ and $g_e$, then the part of degree $d + e$ of $fg$ is $f_d g_e \neq 0$, as $\mathbb{C}[z]$ is a domain. Part 3: if $f(0) \neq 0$, then $1/f$ is holomorphic near $0$; conversely $fg = 1$ forces $f(0) \neq 0$. So the non-units form the ideal $\mathfrak{m}$, which is then the unique maximal ideal. For $f \in \mathfrak{m}$ holomorphic on a polydisc about $0$,
$$f(z) = \int_0^1 \frac{d}{dt} f(tz) \, dt = \sum_{j=1}^n z_j h_j(z), \qquad h_j(z) = \int_0^1 \frac{\partial f}{\partial z_j}(tz) \, dt,$$
and the $h_j$ are holomorphic by differentiation under the integral sign, so $\mathfrak{m} = (z_1, \dots, z_n)$. Part 4: by part 3, $\mathfrak{m}^k$ is generated by the monomials of degree $k$, so its elements have order at least $k$. Conversely, if $\operatorname{ord} f \geq k$, apply the formula for $\mathfrak{m}$ repeatedly: the $h_j$ have order at least $\operatorname{ord} f - 1$, because their Taylor series are obtained from that of $\partial f / \partial z_j$ by multiplying the coefficient of $z^\alpha$ by $1/(|\alpha| + 1)$. Induction on $k$ gives $f \in \mathfrak{m}^k$. A germ of infinite order has zero Taylor series, so it is $0$ by part 1. Part 5: the map $f \mapsto f(z', 0)$ is a surjective homomorphism $\mathcal{O}_n \to \mathcal{O}_{n-1}$, split by the inclusion. If $f(z', 0) = 0$, then $f = z_n h$ with $h(z) = \int_0^1 \frac{\partial f}{\partial z_n}(z', t z_n) \, dt$, holomorphic, so the kernel is $(z_n)$. The general statement follows by iterating.

*Proof of Lemma P6.1.23.* The Taylor series of $f \circ A$ is obtained from that of $f$ by the linear substitution, which maps homogeneous parts of degree $k$ to homogeneous parts of degree $k$, so $f \circ A$ has order $d$ with lowest part $f_d \circ A$. Then $(f \circ A)(0', t) = f(t v) = t^d f_d(v) + \sum_{k > d} t^k f_k(v)$, a convergent series in $t$ of order exactly $d$. The polynomial $f_d$ is nonzero, so $\{ f_d \neq 0 \}$ is a nonempty Zariski open subset of $\mathbb{C}^n$. Composition with $A$ is a ring automorphism with inverse composition with $A^{-1}$.

*Proof of Theorem P6.1.24 and existence in Theorem P6.1.25.* Step 1: choice of a polydisc. Represent $g$ and $f$ by holomorphic functions on a neighbourhood of $0$. Since $g(0', \cdot)$ has a zero of order exactly $d$ at $0$, there is $\rho > 0$ such that $f$ and $g$ are holomorphic near $\{0'\} \times \{ |t| \leq \rho \}$ and $g(0', t) \neq 0$ for $0 < |t| \leq \rho$. By compactness of the circle and continuity there is $\delta > 0$ such that, with $\Delta'$ the open polydisc of radius $\delta$ in $\mathbb{C}^{n-1}$, both functions are holomorphic near $\bar\Delta' \times \{|t| \leq \rho\}$ and $g(z', t) \neq 0$ for $z' \in \bar\Delta'$ and $|t| = \rho$. Every integral below is over the circle $|\zeta| = \rho$, and all integrands are continuous on $\Delta' \times \{|w| < \rho\} \times \{|\zeta| = \rho\}$ and holomorphic in $(z', w)$, so the integrals are holomorphic functions of $(z', w)$ by differentiation under the integral sign and Corollary P6.1.5.

Step 2: the roots. For $z' \in \Delta'$ the number of zeros of $g(z', \cdot)$ in $\{|t| < \rho\}$, counted with multiplicity, is $N(z') = \frac{1}{2\pi i} \int \frac{\partial g / \partial \zeta (z', \zeta)}{g(z', \zeta)} d\zeta$ by the argument principle. It is a continuous integer-valued function on the connected set $\Delta'$ with $N(0') = d$, so $N = d$. Write $b_1(z'), \dots, b_d(z')$ for the zeros, listed with multiplicity in some order. By the residue theorem the power sums
$$s_k(z') = \sum_{j=1}^d b_j(z')^k = \frac{1}{2\pi i} \int \zeta^k \, \frac{\partial g / \partial \zeta (z', \zeta)}{g(z', \zeta)} \, d\zeta$$
are holomorphic on $\Delta'$. Newton's identities $k \sigma_k = \sum_{i=1}^k (-1)^{i-1} \sigma_{k-i} s_i$, $\sigma_0 = 1$, express the elementary symmetric functions $\sigma_k$ of the $b_j$ as polynomials with rational coefficients in $s_1, \dots, s_k$, so the $\sigma_k$ are holomorphic on $\Delta'$. Put
$$P(z', w) = \prod_{j=1}^d (w - b_j(z')) = w^d + \sum_{k=1}^d (-1)^k \sigma_k(z') w^{d-k}.$$
At $z' = 0'$ all roots are $0$, so $\sigma_k(0') = 0$, and $P$ is a Weierstrass polynomial of degree $d$. For each $z'$ the polynomial $P(z', \cdot)$ has the same zeros with the same multiplicities as $g(z', \cdot)$ in $\{|t| < \rho\}$, and no zeros on $|t| = \rho$.

Step 3: the unit. Define $u(z', w) = \frac{1}{2\pi i} \int \frac{g(z', \zeta)}{P(z', \zeta)(\zeta - w)} d\zeta$, holomorphic on $\Delta' \times \{|w| < \rho\}$. For fixed $z'$ the quotient $g(z', \cdot)/P(z', \cdot)$ has removable singularities at the common zeros and extends to a holomorphic function near $\{|t| \leq \rho\}$ without zeros. By Cauchy's formula it equals $u(z', \cdot)$ on $\{|w| < \rho\}$. So $g = u P$ on $\Delta' \times \{|w| < \rho\}$ and $u$ has no zeros there; in particular $u(0) \neq 0$ and the germ of $u$ is a unit. This proves existence in Theorem P6.1.25, together with the description of $P$ by roots.

Step 4: division by $P$. Define $q_0(z', w) = \frac{1}{2\pi i} \int \frac{f(z', \zeta)}{P(z', \zeta)(\zeta - w)} d\zeta$. By Cauchy's formula $f(z', w) = \frac{1}{2\pi i} \int f(z', \zeta) (\zeta - w)^{-1} d\zeta$, so
$$r(z', w) := f(z', w) - q_0(z', w) P(z', w) = \frac{1}{2\pi i} \int \frac{f(z', \zeta)}{P(z', \zeta)} \cdot \frac{P(z', \zeta) - P(z', w)}{\zeta - w} \, d\zeta.$$
Since $(\zeta^m - w^m)/(\zeta - w) = \sum_{i=0}^{m-1} \zeta^{m-1-i} w^i$, the fraction $(P(z', \zeta) - P(z', w))/(\zeta - w)$ is a polynomial in $w$ of degree at most $d - 1$ whose coefficients are polynomials in $\zeta$ and the $\sigma_k(z')$. Integrating coefficient by coefficient shows $r = \sum_{i < d} r_i(z') w^i$ with $r_i$ holomorphic on $\Delta'$. With $q = q_0 / u$ this gives $f = q g + r$, which proves existence in Theorem P6.1.24.

Step 5: uniqueness of division. Suppose $q g + r = 0$ with $q \in \mathcal{O}_n$ and $r \in \mathcal{O}_{n-1}[z_n]$ of degree less than $d$. Shrinking $\Delta'$ and $\rho$ (Step 1 holds for all smaller $\rho$ after shrinking $\delta$), the functions $q$, $r$ are defined on $\Delta' \times \{ |w| < \rho \}$. For fixed $z'$, $r(z', \cdot) = -q(z', \cdot) g(z', \cdot)$ vanishes at the $d$ zeros of $g(z', \cdot)$ to at least their multiplicities, so the polynomial $r(z', \cdot)$ of degree less than $d$ has at least $d$ zeros with multiplicity and is $0$. So $r = 0$, then $q g = 0$ and $q = 0$ since $\mathcal{O}_n$ is a domain and $g \neq 0$. The reformulation: by existence the classes of $1, \dots, z_n^{d-1}$ generate $\mathcal{O}_n / (g)$ over $\mathcal{O}_{n-1}$, and by uniqueness a relation $\sum_i r_i z_n^i \in (g)$ with $r_i \in \mathcal{O}_{n-1}$ forces all $r_i = 0$.

*Proof of uniqueness in Theorem P6.1.25.* Here is the argument from division, which also reproves existence. Divide $z_n^d$ by $g$: $z_n^d = q g + r$ with $\deg_{z_n} r < d$. Setting $z' = 0'$ gives $t^d = q(0', t) g(0', t) + r(0', t)$, and $g(0', t)$ is divisible by $t^d$ in $\mathcal{O}_1$, so $t^d$ divides the polynomial $r(0', t)$ of degree less than $d$, which is therefore $0$. So $P := z_n^d - r$ is a Weierstrass polynomial of degree $d$, and $t^d = q(0', t) g(0', t) = q(0', t) t^d v(t)$ with $v(0) \neq 0$ shows $q(0) \neq 0$; hence $g = q^{-1} P$. If $g = u P = u_1 P_1$ with units $u, u_1$ and Weierstrass polynomials $P, P_1$ of degree $d$, then $z_n^d = u^{-1} g + (z_n^d - P) = u_1^{-1} g + (z_n^d - P_1)$ are two divisions of $z_n^d$ by $g$, so $u = u_1$ and $P = P_1$ by Theorem P6.1.24.

*Proof of Theorem P6.1.26.* Induction on $n$; $\mathcal{O}_0 = \mathbb{C}$ is a field. Let $n \geq 1$ and $0 \neq I \subseteq \mathcal{O}_n$ an ideal, and choose $0 \neq g \in I$. By Lemma P6.1.23 there is an automorphism of $\mathcal{O}_n$ after which $g$ is regular in $z_n$, of order $d$ say, and it suffices to show that the image of $I$ is finitely generated. By Theorem P6.1.24, $\mathcal{O}_n / (g)$ is generated as an $\mathcal{O}_{n-1}$-module by the classes of $1, z_n, \dots, z_n^{d-1}$, so it is a quotient of $\mathcal{O}_{n-1}^d$. The ring $\mathcal{O}_{n-1}$ is Noetherian by induction, so the module $\mathcal{O}_{n-1}^d$ is Noetherian by Proposition P1.3.5 and induction on $d$, and so is its quotient $\mathcal{O}_n / (g)$, again by Proposition P1.3.5. The image $I / (g)$ is an $\mathcal{O}_{n-1}$-submodule, hence generated by the classes of finitely many $f_1, \dots, f_m \in I$. Then $I = (g, f_1, \dots, f_m)$.

*Proof of Lemma P6.1.27.* Part 1: since $P$ is monic, Euclidean division in $\mathcal{O}_{n-1}[z_n]$ gives $f = q P + r$ with $q, r \in \mathcal{O}_{n-1}[z_n]$ and $\deg r < d$. Also $f = h P + 0$. These are two divisions of $f$ by the regular germ $P$ in $\mathcal{O}_n$, so $h = q$ and $r = 0$ by Theorem P6.1.24. Part 2: setting $z' = 0'$ gives $z_n^d = Q_1(0', z_n) Q_2(0', z_n)$ in $\mathbb{C}[z_n]$, with monic factors, so by unique factorization in $\mathbb{C}[z_n]$ the factors are $z_n^{d_1}$ and $z_n^{d_2}$. So all non-leading coefficients of $Q_i$ vanish at $0$. Part 3: suppose $P = f_1 f_2$ with non-units $f_1, f_2 \in \mathcal{O}_n$. Then $z_n^d = f_1(0', z_n) f_2(0', z_n)$, so each $f_i$ is regular in $z_n$ of some order $d_i$, with $d_1 + d_2 = d$ and $d_i \geq 1$ because $f_i(0) = 0$. By Theorem P6.1.25, $f_i = u_i P_i$ with Weierstrass polynomials $P_i$ of degree $d_i$. Then $P = (u_1 u_2) (P_1 P_2)$, and $P_1 P_2$ is a Weierstrass polynomial of degree $d$, so $P = P_1 P_2$ by uniqueness in Theorem P6.1.25, a factorization in $\mathcal{O}_{n-1}[z_n]$ into factors of positive degree, which are non-units there. Conversely, suppose $P = Q_1 Q_2$ with non-units $Q_1, Q_2$ of $\mathcal{O}_{n-1}[z_n]$. The product of their leading coefficients is $1$, so after multiplying by units of $\mathcal{O}_{n-1}$ both are monic. A monic factor of degree $0$ is $1$, a unit, so both have positive degree. By part 2 they are Weierstrass polynomials of positive degree, which vanish at $0$ and are non-units of $\mathcal{O}_n$. So $P$ is reducible in $\mathcal{O}_n$.

*Proof of Theorem P6.1.28.* In a Noetherian domain every nonzero non-unit is a product of irreducible elements: otherwise the set of principal ideals $(f)$ with $f$ a nonzero non-unit that is not such a product has a maximal element $(f)$ by Proposition P1.3.4, $f$ is not irreducible, $f = f_1 f_2$ with $(f) \subsetneq (f_i)$, and the $f_i$ are products, a contradiction. So by Theorem P6.1.26 it suffices to show that every irreducible $f \in \mathcal{O}_n$ is prime. Induction on $n$, the case $n = 0$ being trivial; let $A = \mathcal{O}_{n-1}$, factorial by induction, with fraction field $K$.

First, Gauss's lemma in the form needed. (i) A polynomial in $A[t]$ is *primitive* if no prime element of $A$ divides all its coefficients. A product of primitive polynomials is primitive: if a prime $\pi$ divided all coefficients of $F G$, then $\bar F \bar G = 0$ in $(A/\pi)[t]$, a polynomial ring over a domain, so $\bar F = 0$ or $\bar G = 0$. (ii) Every nonzero $F \in K[t]$ is $c F_0$ with $c \in K^*$ and $F_0 \in A[t]$ primitive, obtained by clearing denominators and dividing by the gcd of the coefficients. (iii) Let $P \in A[t]$ be monic and irreducible in $A[t]$. Then $P$ is irreducible in $K[t]$: if $P = F G$ in $K[t]$ with positive degrees, write $F = c F_0$, $G = c' G_0$ as in (ii) and $cc' = a/b$ with coprime $a, b \in A$; then $b P = a F_0 G_0$, a prime factor of $b$ would divide all coefficients of the primitive $F_0 G_0$ by (i), so $b$ is a unit, and $a$ divides the leading coefficient $1$ of $P$, so $a$ is a unit; thus $P = (a/b) F_0 G_0$ is a factorization in $A[t]$ into polynomials of positive degree. (iv) If such a $P$ divides $QR$ in $A[t]$, then it divides $Q$ or $R$ in $K[t]$, a principal ideal domain in which $P$ is irreducible, hence prime. If $Q = P H$ with $H \in K[t]$, Euclidean division by the monic $P$ in $A[t]$ gives $Q = P H_1 + R_1$ with $H_1, R_1 \in A[t]$ and $\deg R_1 < \deg P$, and uniqueness of division in $K[t]$ gives $H = H_1 \in A[t]$. So $P$ is prime in $A[t]$.

Now let $f \in \mathcal{O}_n$ be irreducible and suppose $f \mid g h$ with $g, h \in \mathcal{O}_n$, both nonzero (otherwise there is nothing to prove). By Lemma P6.1.23 applied to $f g h \neq 0$, after an automorphism of $\mathcal{O}_n$, which preserves irreducibility and divisibility, $fgh$ is regular in $z_n$. Since $(fgh)(0', t) = f(0', t) g(0', t) h(0', t)$ is not identically zero, each factor is regular in $z_n$. By Theorem P6.1.25, $f = u P$, $g = v Q$ and $h = w R$ with units $u, v, w$ and Weierstrass polynomials $P, Q, R$ ($Q = 1$ if $g$ is a unit). Then $P$ is irreducible in $\mathcal{O}_n$, so irreducible in $A[z_n]$ by Lemma P6.1.27, so prime in $A[z_n]$ by (iv). Since $P$ divides $QR$ in $\mathcal{O}_n$ and $QR \in A[z_n]$, it divides $QR$ in $A[z_n]$ by Lemma P6.1.27, hence divides $Q$ or $R$ in $A[z_n]$, and so $f$ divides $g$ or $h$ in $\mathcal{O}_n$.

*Proof of Corollary P6.1.29.* By part 5 of Proposition P6.1.21, $\mathcal{O}_n / (z_1, \dots, z_k) \cong \mathcal{O}_{n-k}$ after renumbering, a domain, so $0 \subsetneq (z_1) \subsetneq (z_1, z_2) \subsetneq \dots \subsetneq (z_1, \dots, z_n) = \mathfrak{m}$ is a chain of primes, strict because $z_{k+1} \notin (z_1, \dots, z_k)$ (its image in $\mathcal{O}_{n-k}$ is a coordinate, which is nonzero). So $\dim \mathcal{O}_n \geq n$. The ring is Noetherian by Theorem P6.1.26 and $\mathfrak{m}$ is minimal over $(z_1, \dots, z_n)$, so Krull's height theorem (Theorem P1.5.18) gives $\dim \mathcal{O}_n = \operatorname{ht} \mathfrak{m} \leq n$. Hence $\dim \mathcal{O}_n = n$ and $\mathfrak{m}$ is generated by $n$ elements, which is Definition P1.9.1. It is normal by Theorem P6.1.28 and Proposition P1.4.19. For the completion, $\mathcal{O}_n / \mathfrak{m}^k$ is, by part 4 of Proposition P6.1.21, the space of polynomials of degree less than $k$, compatibly with $\mathbb{C}[[z]] / (z)^k$, so $\varprojlim_k \mathcal{O}_n / \mathfrak{m}^k = \mathbb{C}[[z_1, \dots, z_n]]$.

*Verification of Example P6.1.30(a).* With $c = \arcsin z_1$, the remainder of $z_2^2$ on division by $z_2 - c$ is the constant $c^2$, since $z_2^2 = (z_2 + c)(z_2 - c) + c^2$, and $q = (z_2 + c) u^{-1}$.

### Exercises

1. (A) Find the Weierstrass polynomial and the unit of $g = e^{z_2} - 1 - z_1$ and of $g = z_2^2 - z_1 - z_1 z_2$ with respect to $z_2$.
2. (A) Let $g = z_1^2 + z_2^2 + z_3^2 \in \mathcal{O}_3$ and $A \in GL_3(\mathbb{C})$ with $A e_3 = v$. Show that $g \circ A$ is regular of order $2$ in $z_3$ if $v_1^2 + v_2^2 + v_3^2 \neq 0$ and is not regular in $z_3$ otherwise. Is $g$ itself regular in $z_3$?
3. (B) Prove that $\mathcal{O}_n / (g)$ for $g$ regular of order $d$ in $z_n$ is isomorphic, as an $\mathcal{O}_{n-1}$-algebra, to $\mathcal{O}_{n-1}[z_n]/(P)$, where $P$ is the Weierstrass polynomial of $g$. Compute it for $g = z_2^2 - z_1^3$.
4. (B) Show that $f \in \mathcal{O}_2$ is irreducible if $f$ is regular of order $1$ in some coordinate, and that $z_1^2 - z_2^2$ is reducible. Show that $z_1^p - z_2^q$ with $p, q$ coprime is irreducible in $\mathcal{O}_2$.
5. (B) Let $f, g \in \mathcal{O}_n$ be coprime. Show that their germs remain coprime at all points near $0$: there is a neighbourhood $V$ of $0$ on which $f$ and $g$ are holomorphic and coprime in $\mathcal{O}_{\mathbb{C}^n, a}$ for every $a \in V$. (Reduce to Weierstrass polynomials and use a Bézout relation $a P + b Q = D(z')$ in $\mathcal{O}_{n-1}[z_n]$ with $D \neq 0$.)
6. (C) Prove that $\mathcal{O}_n$ is Henselian: if $F \in \mathcal{O}_n[t]$ is monic and $\bar F \in \mathbb{C}[t]$ factors as $\bar G \bar H$ with coprime monic factors, then $F = G H$ with monic $G, H$ lifting $\bar G, \bar H$. (Apply Theorem P6.1.25 in $\mathcal{O}_{n+1}$ to $F(z, t + c)$ for each root $c$ of $\bar F$.)

### Lean

Mathlib has Noetherian rings, unique factorization domains, regular local rings in the form of their definitions, Krull's height theorem and formal power series rings, and it has the Weierstrass preparation theorem for power series over complete local rings; it does not have the ring of convergent power series or the analytic Weierstrass theorems. The handbook adds no `MinimalModel` node here.

### Notes and history

Weierstrass proved the preparation theorem in lectures from 1860 and published it in 1886; Stickelberger gave the division theorem in 1887. The proof by power sums of roots and Cauchy integrals is the one of Griffiths and Harris, Section 0.1 (GH78), and Huybrechts, Section 1.1 (Huy05), and the derivation of preparation from division is the order of Grauert and Remmert and of Gunning and Rossi, Chapter II (GR65). That $\mathcal{O}_n$ is Noetherian is due to Rückert (1933), and factoriality goes back to the same circle of ideas. Example P6.1.31 is the reason that the local algebra of smooth functions needs the Malgrange preparation theorem, whose statement is weaker than Weierstrass'. Exercise 5 is the starting point of the coherence theorems of Oka, which Chapter 7 uses through the analytic side of GAGA.
