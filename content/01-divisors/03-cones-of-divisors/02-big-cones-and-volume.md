---
title: The big and pseudoeffective cones and the volume
nodes: []
sources: [Laz04, KM98, KMM87, Har77, BDPP13]
reads_with: [Laz04:2.2, KM98:ch1]
requires: [P5.5, P5.6, P5.8, P5.12, 1.1, 1.2]
level: background
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The big and pseudoeffective cones and the volume

### Statement

The setting is that of Section 1: $\pi \colon X \to Z$ is a projective morphism from a normal quasi-projective variety to a quasi-projective variety over $k$. When the volume is involved, $Z = \operatorname{Spec} k$, so $X$ is a normal projective variety, and $n = \dim X \ge 1$. For a Cartier divisor $D$ write $h^0(D) = \dim_k H^0(X, \mathcal{O}_X(D))$.

**Definition 1.3.10 (volume).** Let $X$ be a normal projective variety of dimension $n$ and $D$ a Cartier divisor on $X$. The *volume* of $D$ is
$$\operatorname{vol}(D) = \limsup_{m \to \infty} \frac{h^0(mD)}{m^n / n!}.$$
The divisor $D$ is *big* if $\operatorname{vol}(D) > 0$.

**Lemma 1.3.11 (growth of sections).** Let $Y$ be a projective scheme over $k$ of dimension $d$ and $L$ a line bundle on $Y$. There is a constant $C$ with $h^0(Y, L^{\otimes m}) \le C (m + 1)^d$ for all $m \ge 0$. In particular $\operatorname{vol}(D) < \infty$ for every Cartier divisor $D$ on a normal projective variety.

Lean: not yet in Lean.

**Lemma 1.3.12 (Kodaira's lemma).** Let $X$ be a normal projective variety of dimension $n$, $D$ a Cartier divisor with $\operatorname{vol}(D) > 0$, and $F$ any Cartier divisor. Then $mD - F$ is linearly equivalent to an effective divisor for infinitely many $m \ge 1$.

Lean: not yet in Lean.

**Proposition 1.3.13 (first properties of the volume).** Let $X$ be a normal projective variety of dimension $n$ and $D$ a Cartier divisor.

1. If $N$ is an effective Cartier divisor, then $\operatorname{vol}(D + N) \ge \operatorname{vol}(D)$.
2. If $\operatorname{vol}(D) > 0$, then $h^0(mD) \ne 0$ for all sufficiently large $m$.
3. $\operatorname{vol}(aD) = a^n \operatorname{vol}(D)$ for every integer $a \ge 1$.
4. If $A$ is ample, then $\operatorname{vol}(A) = A^n > 0$, and the $\limsup$ in Definition 1.3.10 is a limit.

So for a $\mathbb{Q}$-Cartier divisor $D$ the number $\operatorname{vol}(D) = \operatorname{vol}(qD)/q^n$, for any $q \ge 1$ with $qD$ Cartier, does not depend on $q$.

Lean: not yet in Lean.

**Definition 1.3.14 (effective, big and pseudoeffective cones).** In the setting of Section 1:

1. The *effective cone* $\operatorname{Eff}(X/Z) \subseteq N^1(X/Z)$ is the set of classes of effective $\mathbb{R}$-Cartier divisors. It is a convex cone, since a positive combination of effective $\mathbb{R}$-Cartier divisors is again one.
2. The *big cone* is $\operatorname{Big}(X/Z) = \operatorname{Amp}(X/Z) + \operatorname{Eff}(X/Z)$. An $\mathbb{R}$-Cartier divisor is *big over $Z$* if its class is in $\operatorname{Big}(X/Z)$.
3. The *pseudoeffective cone* is the closure $\operatorname{Psef}(X/Z) = \overline{\operatorname{Eff}(X/Z)}$. An $\mathbb{R}$-Cartier divisor is *pseudoeffective over $Z$* if its class is in $\operatorname{Psef}(X/Z)$.

**Proposition 1.3.15 (big Cartier divisors).** Let $X$ be a normal projective variety and $D$ a Cartier divisor. The following are equivalent.

1. $\operatorname{vol}(D) > 0$.
2. There are $m \ge 1$, an ample Cartier divisor $A$ and an effective Cartier divisor $N$ with $mD = A + N$.
3. $[D] \in \operatorname{Big}(X)$.

In particular bigness of a Cartier divisor depends only on its numerical class.

Lean: not yet in Lean.

**Theorem 1.3.16 (the big cone is the interior of the pseudoeffective cone).** In the setting of Section 1:

1. $\operatorname{Amp}(X/Z) \subseteq \operatorname{Eff}(X/Z)$, so $\operatorname{Big}(X/Z) \subseteq \operatorname{Eff}(X/Z)$.
2. $\operatorname{Big}(X/Z)$ is an open convex cone. It is the interior of $\operatorname{Psef}(X/Z)$, and $\operatorname{Psef}(X/Z)$ is its closure.
3. $\operatorname{Nef}(X/Z) \subseteq \operatorname{Psef}(X/Z)$, and $\operatorname{Psef}(X/Z) + \operatorname{Amp}(X/Z) \subseteq \operatorname{Big}(X/Z)$.

Lean: not yet in Lean.

**Theorem 1.3.17 (the volume on $N^1(X)$).** Let $X$ be a normal projective variety of dimension $n$.

1. The volume of a $\mathbb{Q}$-Cartier divisor depends only on its numerical class, and it extends uniquely to a continuous function $\operatorname{vol} \colon N^1(X) \to \mathbb{R}_{\ge 0}$ with $\operatorname{vol}(\lambda x) = \lambda^n \operatorname{vol}(x)$ for $\lambda \ge 0$.
2. $\operatorname{vol}(x) > 0$ if and only if $x \in \operatorname{Big}(X)$. So $\operatorname{vol}$ vanishes on the boundary of $\operatorname{Psef}(X)$ and outside it.
3. $\operatorname{vol}(x) = x^n$ for every $x \in \operatorname{Nef}(X)$.

Part 1 is Laz04, Proposition 2.2.41 and Theorem 2.2.44, and part 3 for rational classes is Laz04, Corollary 1.4.41. Parts 2 and 3 are proved below from these.

Lean: not yet in Lean.

**Proposition 1.3.18 (volume on a surface).** Let $S$ be a smooth projective surface and $D$ a $\mathbb{Q}$-divisor. If $D$ is pseudoeffective with Zariski decomposition $D = P + N$ (Theorem P5.8.24), then $\operatorname{vol}(D) = P^2$. If $D$ is not pseudoeffective, then $\operatorname{vol}(D) = 0$.

Lean: not yet in Lean.

### Proof in words

The volume measures how fast the sections of multiples of $D$ grow. They grow at most like $m^n$, because sections restrict to a hyperplane section with a kernel that is one twist smaller, and induction on the dimension bounds the restricted spaces by $m^{n-1}$. If they grow exactly like $m^n$, they outgrow the sections on any fixed hyperplane section $H$, so some section of $mD$ vanishes on $H$; this is Kodaira's lemma, and it writes a multiple of $D$ as ample plus effective. Conversely an ample divisor has volume $A^n$ by Riemann-Roch and Serre vanishing, and adding an effective divisor only adds sections.

The cone statements are then convex geometry, in the same way as in Section 1. The effective cone contains the ample cone, so the big cone $\operatorname{Amp} + \operatorname{Eff}$ is an open set inside $\operatorname{Eff}$, and a point of the interior of $\overline{\operatorname{Eff}}$ can be written as a small ample class plus a class that is still interior, hence effective. The hard analytic fact is the continuity of the volume, quoted from Lazarsfeld; given it, the volume is positive exactly on the big cone, because a class outside the big cone is a limit of rational classes that are not big.

On a surface the Zariski decomposition computes everything. The negative part is in the base locus of every multiple, so $h^0(mD) = h^0(mP)$, and $P$ is nef, so its volume is $P^2$. The volume is then a piecewise quadratic function, and it differs from $D^2$ exactly where $D$ is not nef.

### Examples

**Example 1.3.19 (the plane blown up at a point).** On $X = \operatorname{Bl}_p \mathbb{P}^2$ let $x = a\ell - bE$. The curves on $X$ are $E$ and the classes $a\ell - bE$ with $a \ge 1$ and $0 \le b \le a$ (Example P5.6.7), so $\operatorname{Eff}(X) = NE(X)$ is the closed cone spanned by $E$ and $\ell - E$, and $x = a(\ell - E) + (a - b)E$ gives
$$\operatorname{Psef}(X) = \{ a \ge 0, \ a \ge b \}, \qquad \operatorname{Big}(X) = \{ a > 0, \ a > b \}.$$
The Zariski decomposition of a pseudoeffective $x$ is $P = x$ if $0 \le b \le a$, since $x$ is nef (Example 1.3.6), and $P = a\ell$, $N = -bE$ if $b < 0$, since $x \cdot E = b < 0$ and $a\ell \cdot E = 0$. Proposition 1.3.18 and continuity give
$$\operatorname{vol}(a\ell - bE) = \begin{cases} a^2 - b^2 & 0 \le b \le a, \\ a^2 & b < 0 \le a, \\ 0 & a < 0 \text{ or } a < b. \end{cases}$$
The two formulas agree on the ray $b = 0$, and the function is continuous, as Theorem 1.3.17 says.

**Example 1.3.20 (a big divisor that is not nef).** On $\operatorname{Bl}_p \mathbb{P}^2$ let $D = \ell + 2E$. Then $D \cdot E = -2$, so $D$ is not nef, and $D^2 = 1 - 4 = -3 < 0$. Its class lies in $\operatorname{Big}(X)$, since $D = \ell + 2E$ with $a = 1 > 0 > -2 = b$. By Example P5.8.27 its Zariski decomposition is $P = \ell$, $N = 2E$, and $h^0(nD) = h^0(n\ell) = (n + 1)(n + 2)/2$. So $\operatorname{vol}(D) = \lim (n+1)(n+2)/n^2 = 1 = P^2$, while $D^2 = -3$. Kodaira's lemma is visible here: with the ample class $A = 2\ell - E$, the divisor $2D - A = 5E$ is effective.

**Example 1.3.21 (the quadric surface).** On $\mathbb{P}^1 \times \mathbb{P}^1$ every effective divisor has class $aF_1 + bF_2$ with $a, b \ge 0$, so $\operatorname{Psef} = \operatorname{Nef}$ is the positive quadrant and $\operatorname{Big} = \operatorname{Amp}$ is its interior. For integers $a, b \ge 0$, $h^0(m(aF_1 + bF_2)) = (ma + 1)(mb + 1)$, the number of monomials of bidegree $(mb, ma)$, and
$$\operatorname{vol}(aF_1 + bF_2) = \lim_{m \to \infty} \frac{(ma + 1)(mb + 1)}{m^2/2} = 2ab = (aF_1 + bF_2)^2.$$

**Example 1.3.22 (the Hirzebruch surfaces).** On $\mathbb{F}_n$ with $n \ge 1$, $\operatorname{Psef}(\mathbb{F}_n) = \overline{NE}(\mathbb{F}_n)$ is spanned by $C_-$ and $F$ (Example P5.12.8), so $x = aC_- + bF$ is pseudoeffective if and only if $a, b \ge 0$, and big if and only if $a, b > 0$. If $b \ge na$, then $x$ is nef and $\operatorname{vol}(x) = x^2 = -na^2 + 2ab = a(2b - na)$. If $0 \le b < na$, then $x \cdot C_- = b - na < 0$, and $N = \gamma C_-$ with $(x - \gamma C_-) \cdot C_- = 0$ gives $\gamma = a - b/n$, so
$$P = \frac{b}{n} C_- + bF = \frac{b}{n}(C_- + nF), \qquad \operatorname{vol}(x) = P^2 = \frac{b^2}{n^2} \cdot n = \frac{b^2}{n}.$$
The two formulas agree at $b = na$, where both give $na^2$. For the anticanonical class $-K = 2C_- + (n + 2)F$ this gives $\operatorname{vol}(-K) = 8$ for $n \le 2$ and $\operatorname{vol}(-K) = (n + 2)^2/n$ for $n \ge 3$, while $K^2 = 8$ for every $n$. So for $n \ge 3$ the volume of $-K$ is strictly larger than $(-K)^2$; for $n = 3$ it is $25/3$.

**Example 1.3.23 (failures).** On $\operatorname{Bl}_p \mathbb{P}^2$:

1. $D = 2\ell + E$ has $D^2 = 4 - 1 = 3$, but $\operatorname{vol}(D) = 4$, since $P = 2\ell$. So $\operatorname{vol}(D) = D^2$ fails off the nef cone, even for big $D$ with $D^2 > 0$.
2. $D = -\ell$ has $D^2 = 1 > 0$ and $\operatorname{vol}(D) = 0$, since $a = -1 < 0$ puts $-\ell$ outside $\operatorname{Psef}(X)$ of Example 1.3.19. A positive square does not imply bigness without the condition $D \cdot H > 0$ of Lemma P5.5.21.
3. $E$ is effective, so pseudoeffective, and $\operatorname{vol}(E) = 0$ because $h^0(mE) = 1$ for all $m$. So $\operatorname{Eff}(X)$ is not contained in $\operatorname{Big}(X)$, and $\operatorname{Psef}(X) \ne \operatorname{Big}(X)$.
4. Over $Z = \mathbb{P}^2$ every class is big. In $N^1(X/Z) \cong \mathbb{R}$ of Example 1.3.6 the effective classes $E$ and $\ell - E$ map to $-1$ and $1$, so $\operatorname{Eff}(X/Z) = \mathbb{R}$ and $\operatorname{Big}(X/Z) = \operatorname{Psef}(X/Z) = \mathbb{R}$. The divisor $E$ is big over $\mathbb{P}^2$ but not big on $X$.

### Proof

*Lemma 1.3.11.* Fix a very ample line bundle $\mathcal{O}_Y(1)$. First the case $L = \mathcal{O}_Y(1)$, by induction on $d$. If $d = 0$, $Y$ is finite and $h^0(\mathcal{O}_Y(m)) = h^0(\mathcal{O}_Y)$. If $d \ge 1$, $Y$ has finitely many associated points, and the sections of $\mathcal{O}_Y(1)$ that vanish at a given point form a proper subspace of $H^0(\mathcal{O}_Y(1))$, since $\mathcal{O}_Y(1)$ is globally generated. As $k$ is infinite, a vector space is not a finite union of proper subspaces, so there is a section $s$ that vanishes at no associated point. Multiplication by $s$ is then injective on $\mathcal{O}_Y$, and with $H = \{ s = 0 \}$, of dimension $d - 1$, there are exact sequences $0 \to \mathcal{O}_Y(j - 1) \to \mathcal{O}_Y(j) \to \mathcal{O}_H(j) \to 0$. By induction $h^0(\mathcal{O}_H(j)) \le C'(j + 1)^{d-1}$, so
$$h^0(\mathcal{O}_Y(m)) \le h^0(\mathcal{O}_Y) + \sum_{j=1}^m C'(j + 1)^{d - 1} \le h^0(\mathcal{O}_Y) + C' m (m + 1)^{d - 1} \le C(m + 1)^d.$$
For general $L$, choose $r$ with $L^{-1}(r)$ globally generated (Har77, Theorem II.5.17). As before there is a section $t$ of $L^{-1}(r)$ that vanishes at no associated point of $Y$, and multiplication by $t^m$ embeds $L^{\otimes m}$ into $\mathcal{O}_Y(mr)$. So $h^0(L^{\otimes m}) \le h^0(\mathcal{O}_Y(mr)) \le C(mr + 1)^d \le C r^d (m + 1)^d$. For the last statement, apply this to $Y = X$, $d = n$ and $L = \mathcal{O}_X(D)$. $\square$

*Lemma 1.3.12.* Choose a very ample divisor $A$ and $j \ge 1$ such that $jA - F$ is globally generated (Har77, Theorem II.5.17), and so linearly equivalent to an effective divisor. Since $jA$ is very ample and $n \ge 1$, $|jA|$ contains an effective divisor $H$, a closed subscheme of dimension $n - 1$. The exact sequence $0 \to \mathcal{O}_X(mD - H) \to \mathcal{O}_X(mD) \to \mathcal{O}_H(mD) \to 0$ gives
$$h^0(mD - H) \ge h^0(mD) - h^0(H, \mathcal{O}_H(mD)).$$
By Lemma 1.3.11 on $H$, the last term is at most $C(m + 1)^{n-1}$. Since $\operatorname{vol}(D) > 0$, there are infinitely many $m$ with $h^0(mD) \ge \frac12 \operatorname{vol}(D) \, m^n/n!$, and for all large such $m$ this exceeds $C(m + 1)^{n-1}$. For these $m$, $mD - H \sim G$ with $G \ge 0$, and $mD - F \sim G + (H - F)$, where $H - F \sim jA - F$ is linearly equivalent to an effective divisor. $\square$

*Proposition 1.3.13.* (1) Let $s$ be the section of $\mathcal{O}_X(N)$ that defines $N$. Since $X$ is integral, multiplication by $s^m$ is an injection $H^0(mD) \to H^0(m(D + N))$, so $h^0(m(D + N)) \ge h^0(mD)$ for every $m$.

(2) By Lemma 1.3.12 with $F$ an ample divisor $A$ there are $m_1 \ge 1$ and $N \ge 0$ with $m_1 D \sim A + N$. By Serre's theorem there is $b \ge 1$ such that $bA + rD$ is globally generated, so linearly equivalent to an effective divisor, for each $r = 0, 1, \dots, m_1 - 1$. Then $(bm_1 + r)D \sim (bA + rD) + bN$ is linearly equivalent to an effective divisor for these $r$, and so is $m_1 D$. The set $\{ m : h^0(mD) \ne 0 \}$ is closed under addition, as a product of nonzero sections is nonzero on the integral scheme $X$. It contains $m_1$ and the $m_1$ consecutive integers $bm_1, \dots, bm_1 + m_1 - 1$, so it contains every $m \ge bm_1$.

(3) Restricting the $\limsup$ to multiples of $a$ gives
$$\operatorname{vol}(aD) = \limsup_{m} \frac{h^0(maD)}{m^n / n!} = a^n \limsup_m \frac{h^0(maD)}{(ma)^n / n!} \le a^n \operatorname{vol}(D).$$
For the reverse inequality assume $\operatorname{vol}(D) > 0$, the case $\operatorname{vol}(D) = 0$ being clear. By (2) there is $e_0$ with $h^0(eD) \ne 0$ for all $e \ge e_0$. Choose $m_j \to \infty$ with $h^0(m_j D)/(m_j^n/n!) \to \operatorname{vol}(D)$, and $e_j \in [e_0, e_0 + a)$ with $m_j + e_j = a q_j$ divisible by $a$. A nonzero section of $e_j D$ gives, as in (1), $h^0(q_j \cdot aD) \ge h^0(m_j D)$. So
$$\operatorname{vol}(aD) \ge \limsup_j \frac{h^0(q_j \cdot aD)}{q_j^n/n!} \ge \lim_j a^n \Bigl( \frac{m_j}{m_j + e_j} \Bigr)^n \frac{h^0(m_j D)}{m_j^n/n!} = a^n \operatorname{vol}(D).$$

(4) By asymptotic Riemann-Roch (Laz04, Theorem 1.1.24) $\chi(mA) = A^n m^n/n! + O(m^{n-1})$, and by Serre vanishing (Har77, Theorem III.5.2) $h^i(mA) = 0$ for $i > 0$ and $m$ large. So $h^0(mA) = A^n m^n/n! + O(m^{n-1})$ and $h^0(mA)/(m^n/n!) \to A^n$. Finally $A^n > 0$ for ample $A$, since $A^n = \deg_{\mathcal{O}(qA)}(X)/q^n$ for very ample $qA$.

The statement on $\mathbb{Q}$-Cartier divisors follows from (3): if $qD$ and $q'D$ are Cartier, then $\operatorname{vol}(q'qD) = q'^n \operatorname{vol}(qD) = q^n \operatorname{vol}(q'D)$. $\square$

*Proposition 1.3.15.* (1) implies (2): by Lemma 1.3.12 with $F = A$ ample, $mD - A \sim N$ with $N \ge 0$. Then $A' = mD - N$ is linearly equivalent to $A$, so it is ample, and $mD = A' + N$.

(2) implies (1): by Proposition 1.3.13, $m^n \operatorname{vol}(D) = \operatorname{vol}(A + N) \ge \operatorname{vol}(A) = A^n > 0$.

(2) implies (3): $[D] = \frac1m [A] + \frac1m [N]$ with $\frac1m [A] \in \operatorname{Amp}(X)$ and $\frac1m [N] \in \operatorname{Eff}(X)$.

(3) implies (2): write $[D] = h + [\Delta]$ with $h \in \operatorname{Amp}(X)$ and $\Delta = \sum_{i=1}^r a_i \Gamma_i$ an effective $\mathbb{R}$-Cartier divisor, $a_i > 0$ and $\Gamma_i$ prime. The $\mathbb{R}$-Cartier divisors are the $\mathbb{R}$-linear combinations of Cartier divisors (Definition 1.1.6), so those supported on $\Gamma_1 \cup \dots \cup \Gamma_r$ form the subspace $V = (\operatorname{CDiv}(X) \otimes \mathbb{R}) \cap \bigoplus_i \mathbb{R}\Gamma_i$ of the real Weil divisors. Both subspaces are spanned by rational vectors, so $V$ is too, and the rational points of $V$, which are the $\mathbb{Q}$-Cartier divisors supported on the $\Gamma_i$, are dense in $V$. The vector $(a_i)$ lies in the open subset of $V$ where all coordinates are positive, so there are effective $\mathbb{Q}$-Cartier divisors $\Delta_j \to \Delta$ in $V$. Then $[D] - [\Delta_j] \to h$, and since $\operatorname{Amp}(X)$ is open, $[D] - [\Delta_j]$ is a rational point of $\operatorname{Amp}(X)$ for some $j$. By Theorem 1.3.4(4) there is $m \ge 1$ such that $N = m\Delta_j$ is Cartier and $m[D] - [N]$ is the class of an ample Cartier divisor. The Cartier divisor $A = mD - N$ is numerically equivalent to an ample divisor, so it is ample by Theorem 1.1.9, and $mD = A + N$.

Condition (3) depends only on the class of $D$. $\square$

*Theorem 1.3.16.* (1) Let $A$ be a Cartier divisor ample over $Z$ and $H$ an ample divisor on the quasi-projective variety $Z$. For $j$ large, $A + \pi^* (jH)$ is ample on $X$ (Laz04, Proposition 1.7.10), so some multiple $q(A + \pi^* (jH))$ is very ample, and a hyperplane section of $X$ in the corresponding immersion gives an effective Cartier divisor $G \sim q(A + \pi^*(jH))$. For a curve $C$ over $Z$, $\pi|_C$ is constant, so $\mathcal{O}_X(\pi^* H)|_C$ is trivial and $\pi^* H \cdot C = 0$. Hence $[A] = \frac1q [G]$ in $N^1(X/Z)$, and $[A] \in \operatorname{Eff}(X/Z)$. A positive combination of such classes is again in the convex cone $\operatorname{Eff}(X/Z)$. Then $\operatorname{Big}(X/Z) = \operatorname{Amp}(X/Z) + \operatorname{Eff}(X/Z) \subseteq \operatorname{Eff}(X/Z)$.

(2) Both summands are convex cones, so $\operatorname{Big}(X/Z)$ is one. It is the union of the translates $\operatorname{Amp}(X/Z) + e$, $e \in \operatorname{Eff}(X/Z)$, of an open set, so it is open, and it is nonempty by Theorem 1.3.4. By (1), $\operatorname{Big}(X/Z)$ is an open subset of $\operatorname{Psef}(X/Z)$, so it lies in the interior. Conversely, the convex set $\operatorname{Eff}(X/Z)$ has nonempty interior, as it contains $\operatorname{Big}(X/Z)$. By Lemma 1.3.3 the interior of $\operatorname{Psef}(X/Z) = \overline{\operatorname{Eff}(X/Z)}$ is the interior of $\operatorname{Eff}(X/Z)$. Let $x$ be in it and $h \in \operatorname{Amp}(X/Z)$. For small $\varepsilon > 0$ the point $x - \varepsilon h$ is still in the interior of $\operatorname{Eff}(X/Z)$, so $x = \varepsilon h + (x - \varepsilon h) \in \operatorname{Amp}(X/Z) + \operatorname{Eff}(X/Z) = \operatorname{Big}(X/Z)$. So $\operatorname{Big}(X/Z)$ is the interior of $\operatorname{Psef}(X/Z)$, and Lemma 1.3.3 applied to the convex set $\operatorname{Psef}(X/Z)$ shows that it is the closure of its interior.

(3) $\operatorname{Nef}(X/Z) = \overline{\operatorname{Amp}(X/Z)} \subseteq \overline{\operatorname{Eff}(X/Z)}$ by Theorem 1.3.4 and (1). Let $x \in \operatorname{Psef}(X/Z)$ and $h \in \operatorname{Amp}(X/Z)$. Then $h$ is in the interior $\operatorname{Big}(X/Z)$ of $\operatorname{Psef}(X/Z)$, and by Lemma 1.3.3(1) the point $\frac12 x + \frac12 h$ is in the interior too. So $x + h = 2 (\frac12 x + \frac12 h) \in \operatorname{Big}(X/Z)$. $\square$

*Theorem 1.3.17.* Part 1 is quoted. For part 2 first take a rational class $x = \frac1q [D]$ with $D$ Cartier: by Proposition 1.3.15, $\operatorname{vol}(D) > 0$ if and only if $[D] \in \operatorname{Big}(X)$, and both conditions are invariant under positive scaling.

Let $x \in \operatorname{Big}(X)$ be arbitrary, $x = h + e$ with $h$ ample and $e$ effective. Choose a rational ample class $h'$ with $h - h'$ ample, for instance a rational point near $\frac12 h$. By Theorem 1.3.16(1), $e' = (h - h') + e \in \operatorname{Eff}(X)$, and $x = h' + e'$. As in the proof of Proposition 1.3.15, $e'$ is a limit of classes $e'_j$ of effective $\mathbb{Q}$-Cartier divisors. Clearing denominators in Proposition 1.3.13(1) and (4) gives $\operatorname{vol}(h' + e'_j) \ge \operatorname{vol}(h') = h'^n > 0$. By continuity $\operatorname{vol}(x) \ge h'^n > 0$.

Let $x \notin \operatorname{Big}(X)$. If $a \in \operatorname{Amp}(X)$ and $x - a \in \operatorname{Big}(X)$, then $x \in \operatorname{Big}(X) + \operatorname{Amp}(X) \subseteq \operatorname{Big}(X)$, which is false. So the open set $x - \operatorname{Amp}(X)$ contains no big class, and in particular its rational points have volume $0$. The point $x$ is a limit of points of $x - \operatorname{Amp}(X)$, such as $x - \varepsilon h$, and each of them is a limit of rational points of the open set $x - \operatorname{Amp}(X)$. By continuity $\operatorname{vol}(x) = 0$. Since $\operatorname{Big}(X)$ is the interior of $\operatorname{Psef}(X)$ by Theorem 1.3.16, this is the second sentence of part 2.

For part 3, both sides are continuous on $N^1(X)$, and they agree on rational points of $\operatorname{Amp}(X)$ by Proposition 1.3.13(4) and homogeneity. These points are dense in $\operatorname{Amp}(X)$, which is dense in $\operatorname{Nef}(X)$ by Theorem 1.3.4. $\square$

*Proposition 1.3.18.* If $D$ is not pseudoeffective, then no multiple $mD$ is linearly equivalent to an effective divisor, since the classes of effective divisors lie in $\overline{NE}(S)$ (Definition P5.8.22). So $h^0(mD) = 0$ for all $m \ge 1$ with $mD$ integral, and $\operatorname{vol}(D) = 0$.

Let $D$ be pseudoeffective. By Theorem P5.8.24, $N$ and $P$ have rational coefficients, so there is $q \ge 1$ with $qD$, $qN$ and $qP$ integral. For every $m \ge 1$, $\lceil mqN \rceil = mqN$, and Corollary P5.8.26 applied to the divisor $qD$, whose Zariski decomposition is $qP + qN$, gives $h^0(mqD) = h^0(mqD - mqN) = h^0(mqP)$. So $\operatorname{vol}(qD) = \operatorname{vol}(qP)$. The divisor $qP$ is nef, so $\operatorname{vol}(qP) = (qP)^2$ by Theorem 1.3.17(3). Dividing by $q^2$ gives $\operatorname{vol}(D) = P^2$. $\square$

### Exercises

1. (A) On $\operatorname{Bl}_p \mathbb{P}^2$, check that $-K = 3\ell - E$ is nef and compute $\operatorname{vol}(-K)$. Check the answer against the dimension of the space of plane curves of degree $3m$ with multiplicity at least $m$ at $p$.
2. (A) On $\mathbb{F}_n$, compute $\operatorname{vol}(-K)$ for $n = 0, 1, \dots, 5$, with $\mathbb{F}_0 = \mathbb{P}^1 \times \mathbb{P}^1$, and check that $\operatorname{vol}(-K) \ge K^2$, with equality exactly for $n \le 2$.
3. (B) Show that the volume function of Example 1.3.19 is continuously differentiable on the interior of $\operatorname{Big}(X)$, but that its second derivative in the direction of $E$ jumps across the ray $b = 0$.
4. (B) Let $X$ be a normal projective variety of dimension $n$ and $H$ an ample divisor. Show that $x \cdot H^{n-1} \ge 0$ for every $x \in \operatorname{Psef}(X)$, and deduce that $\operatorname{vol}(x) = 0$ whenever $x \cdot H^{n-1} < 0$.
5. (B) Let $S$ be a smooth projective surface. Use Corollary P5.5.23 to show that $\operatorname{vol}^{1/2}$ is concave on $\operatorname{Nef}(S)$, that is, $\operatorname{vol}(x + y)^{1/2} \ge \operatorname{vol}(x)^{1/2} + \operatorname{vol}(y)^{1/2}$ for nef $x$ and $y$.
6. (C) Let $X = \mathbb{F}_n \to Z = \mathbb{P}^1$ be the ruling. Compute $\operatorname{Eff}(X/Z)$, $\operatorname{Big}(X/Z)$ and $\operatorname{Psef}(X/Z)$ in the identification $N^1(X/Z) \cong \mathbb{R}$ of Example 1.3.8. Show that a class is big over $Z$ if and only if its restriction to a general fibre has positive degree.

### Lean

The project library defines `MinimalModel.IsBig` as $\mathbb{R}$-linear equivalence to an ample divisor plus an effective one, `MinimalModel.IsBigRel` as the same with an ample divisor over $Z$, and `MinimalModel.IsPseudoEffective` and `MinimalModel.IsPseudoEffectiveOver` by the condition that $D + \varepsilon A$ is big for every $\varepsilon > 0$. These match Definition 1.3.14 up to the passage from linear to numerical equivalence, which is Proposition 1.3.15 for Cartier divisors; the characterization by $D + \varepsilon A$ is Theorem 1.3.16(2) and (3). The library has `MinimalModel.h0` and `MinimalModel.iitakaDim`, but no volume function, so Definition 1.3.10, Kodaira's lemma and the continuity of the volume are not formalized.

### Notes and history

The volume first appears on surfaces in Zariski's 1962 paper on the Riemann-Roch theorem for high multiples of a divisor, which introduced the decomposition of Theorem P5.8.24 in order to compute it, and Proposition 1.3.18 is its main consequence. Kodaira's lemma, in the form of Proposition 1.3.15, is in KMM87, Lemma 0-3-3, and is the basic tool for perturbing big divisors in the minimal model program. The continuity of the volume and its numerical invariance are in Laz04, Section 2.2.C, and the volume is in fact continuously differentiable on the big cone, by work of Boucksom, Favre and Jonsson and of Lazarsfeld and Mustață, although Example 1.3.19 shows that it is not twice differentiable. The dual of the pseudoeffective cone is the closure of the cone of movable curves, by BDPP13; this is the analogue for $\operatorname{Psef}$ of the duality of Theorem 1.3.4, and it is the starting point of the theory of movable cones.
