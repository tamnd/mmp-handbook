---
title: The numerical dimension of Nakayama
nodes: []
sources: [Laz04, Har77, BDPP13, KM98]
reads_with: [Laz04:ch2, BDPP13:ch3]
requires: [P3.6, P5.5, P5.6, P5.10, P5.11, P5.12]
level: background
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The numerical dimension of Nakayama

### Statement

The Iitaka dimension only sees divisors with sections. A divisor such as a nonzero class of degree 0 on an elliptic curve has none in any multiple, although it is numerically trivial, and Theorem 1.4.26 below gives a nef divisor whose multiples have a single section each, although the sections of $mC_0 + A$ grow linearly in $m$. Nakayama's numerical dimension counts the sections of $mD + A$ for a fixed ample $A$, which makes the count stable under small numerical changes. The reference is Nakayama, *Zariski-decomposition and abundance*, MSJ Memoirs 14, Mathematical Society of Japan, 2004, Chapter V, Section 2, where $\kappa_\sigma$ is Definition V.2.5. Keep the notation of Section 1, with $X$ a projective variety of dimension $n$.

**Definition 1.4.22 (the numerical dimension $\kappa_\sigma$).** Let $D$ and $A$ be Cartier divisors on $X$. Put $\sigma(D; A) = -\infty$ if $h^0(mD + A) \ne 0$ for only finitely many $m \ge 1$, and otherwise

$$\sigma(D; A) = \max \{ j \ge 0 : h^0(mD + A) \ge \varepsilon \, m^j \text{ for some } \varepsilon > 0 \text{ and infinitely many } m \}.$$

The *numerical dimension* of $D$ is $\kappa_\sigma(D) = \max \{ \sigma(D; A) : A \text{ ample} \}$. For a $\mathbb{Q}$-Cartier $D$ on a normal $X$, $\kappa_\sigma(D) = \kappa_\sigma(aD)$ for any $a \ge 1$ with $aD$ Cartier.

Lean: `MinimalModel.numericalDim`, in the project library.

**Proposition 1.4.23 (properties of $\kappa_\sigma$).** Let $D$ be a Cartier divisor on $X$ and $H$ a very ample divisor.

1. $\sigma(D; A) \in \{-\infty, 0, 1, \dots, n\}$ for every $A$, so $\kappa_\sigma(D)$ is defined and lies in the same set.
2. If $A' - A$ is linearly equivalent to an effective divisor, then $\sigma(D; A') \ge \sigma(D; A)$. There is $c_0$ with $\kappa_\sigma(D) = \sigma(D; cH)$ for every $c \ge c_0$.
3. $\kappa_\sigma(aD) = \kappa_\sigma(D)$ for every $a \ge 1$, and $\kappa_\sigma(D) = \kappa_\sigma(D')$ if $D \sim D'$. So the definition for $\mathbb{Q}$-Cartier divisors is consistent.
4. $\kappa(D) \le \kappa_\sigma(D)$.
5. $\kappa_\sigma(D + F) \ge \kappa_\sigma(D)$ for every effective Cartier divisor $F$.
6. Let $X$ be normal. If $\kappa_\sigma(D) \ge 0$, then $D + \varepsilon A'$ is big for every ample $A'$ and every rational $\varepsilon > 0$.

Lean: not yet in Lean.

In part 6, bigness for rational $\varepsilon$ gives it for real $\varepsilon$ by the openness of the big cone, proved in Chapter 3, so $D$ is pseudo-effective in the sense of Definition 1.1.26. The converse also holds: for a pseudo-effective $D$ on a smooth projective $X$ there is an ample $A$ with $h^0(mD + A) \ne 0$ for every $m \ge 1$, so $\kappa_\sigma(D) \ge 0$ (Nakayama, Chapter V, Section 1). So $\kappa_\sigma(D) = -\infty$ exactly when $D$ is not pseudo-effective, and $\kappa_\sigma$ depends only on the numerical class of $D$ (Nakayama, Chapter V, Section 2). These two facts are cited and are not used in the proofs below.

**Theorem 1.4.24 (bigness and $\kappa_\sigma$).** For a Cartier divisor $D$ on $X$ the following are equivalent:

1. $D$ is big, that is $\kappa(D) = n$;
2. $\kappa_\sigma(D) = n$;
3. $aD \sim A + F$ for some $a \ge 1$, an ample $A$ and an effective $F$.

Lean: not yet in Lean.

**Proposition 1.4.25 (nef divisors on surfaces).** Let $X$ be a smooth projective surface and $D$ a nef divisor. Then

$$\kappa_\sigma(D) = \begin{cases} 0 & \text{if } D \equiv 0, \\ 1 & \text{if } D^2 = 0 \text{ and } D \not\equiv 0, \\ 2 & \text{if } D^2 > 0. \end{cases}$$

Lean: not yet in Lean.

Since a nef divisor has $D^2 \ge 0$ (Lemma P5.12.4), the three cases cover all nef divisors. In every dimension, for a nef $D$, $\kappa_\sigma(D)$ is the numerical dimension $\nu(D) = \max\{ j : D^j \cdot H^{n - j} \ne 0 \}$ for an ample $H$ (Nakayama, Chapter V, Section 2); the proposition is the case $n = 2$, proved here directly.

**Theorem 1.4.26 (a divisor with $\kappa = 0$ and $\kappa_\sigma = 1$).** Let $E$ be an elliptic curve and $P$ an invertible sheaf of degree 0 on $E$ that has infinite order in $\operatorname{Pic}(E)$. Let $\mathcal{V} = \mathcal{O}_E \oplus P$, $\pi \colon X = \mathbb{P}(\mathcal{V}) \to E$ with the quotient convention of Definition P3.6.33, and $f$ the class of a fibre. Let $C_0 \subseteq X$ be the section of $\pi$ given by the quotient $\mathcal{V} \to P$. Then:

1. $\mathcal{O}_X(C_0) \cong \mathcal{O}_X(1)$, $C_0^2 = 0$, $C_0 \cdot f = 1$, and $C_0$ is nef;
2. $h^0(mC_0) = 1$ for every $m \ge 0$, so $\kappa(C_0) = 0$;
3. $A = C_0 + f$ is ample, and $h^0(mC_0 + cA) = c(m + c + 1)$ for all $m \ge 0$ and $c \ge 1$;
4. $\kappa_\sigma(C_0) = 1$.

Lean: not yet in Lean.

Fix a divisor $Q$ on $E$ with $\mathcal{O}_E(Q) \cong P$. Such a $P$ exists. By Proposition P5.1.13, part 2, the classes of degree 0 are the classes $\mathcal{O}_E(R - O)$ for points $R$, with the group law of $E$, so a point of infinite order gives one. Example P5.10.26 shows that $R = (-1, 4)$ on $y^2 = x^3 + 17$ has infinite order, over $\overline{\mathbb{Q}}$ and so over every algebraically closed field containing it. Over an uncountable field, all but countably many points have infinite order, since the points of order $r$ are finitely many for each $r$.

### Proof in words

Adding a fixed ample $A$ before counting sections fills in what the semigroup misses: the sections of $mD + A$ see the numerical class of $D$ through Riemann-Roch, while the sections of $mD$ see its linear class. So $\kappa_\sigma$ is at least $\kappa$, it does not exceed $n$, and it reaches $n$ only if $mD + A$ has so many sections that some of them vanish on a hyperplane section, which makes $mD$ ample plus effective. For a nef divisor on a surface, Riemann-Roch computes $\chi(mD + cH)$, the term $h^2$ vanishes, and the growth of $\chi$ is quadratic, linear or constant according to $D^2$ and $D \cdot H$. On the ruled surface of Theorem 1.4.26 everything is computed by pushing forward to $E$: the sections of $\mathcal{O}_X(m)$ are the sections of $\operatorname{Sym}^m \mathcal{V} = \bigoplus_{i=0}^m P^i$, and only the summand $P^0$ has a section, because $P$ has infinite order. After a twist by the ample $A$, every summand becomes a line bundle of positive degree $c$ on $E$, with $c$ sections, and the count grows linearly in $m$.

### Examples

**Example 1.4.27 (the exceptional curve).** On $X = \operatorname{Bl}_p \mathbb{P}^2$, Example 1.4.10 gives $\kappa(E) = 0$. Every ample divisor is $A = a\ell - bE$ with $a > b > 0$ (Example P5.12.7). For $m \ge b$, Corollary P5.6.5, part 3, gives $h^0(mE + A) = h^0(\pi^*(a\ell) + (m - b)E) = h^0(\mathbb{P}^2, \mathcal{O}(a)) = \binom{a + 2}{2}$, a constant. So $\sigma(E; A) = 0$ for every ample $A$, and $\kappa_\sigma(E) = 0 = \kappa(E)$. A curve of negative square adds nothing to the growth, unlike the nef curve $C_0$ of Theorem 1.4.26.

**Example 1.4.28 (the anticanonical divisor of the ruled surface).** Keep the notation of Theorem 1.4.26. By Har77, Exercise III.8.4, $\omega_X \cong \pi^*(\omega_E \otimes \det \mathcal{V}) \otimes \mathcal{O}_X(-2)$, and $\omega_E \cong \mathcal{O}_E$, $\det \mathcal{V} = P$. So $-K_X \sim 2C_0 - \pi^*Q$. By the projection formula and Proposition P3.6.35, part 3,

$$h^0(-mK_X) = \sum_{i=0}^{2m} h^0(E, P^{i - m}) = 1, \qquad h^0(-mK_X + cA) = \sum_{i=0}^{2m + c} h^0(E, P^{i - m}(cp)) = c(2m + c + 1),$$

with $f = \pi^*p$ for a point $p$, since only $i = m$ contributes to the first sum and every summand of the second has degree $c \ge 1$. So $\kappa(-K_X) = 0$ and $\kappa_\sigma(-K_X) = 1$. The surface is a ruled surface with $-K_X$ nef of square $0$ whose anticanonical ring is $k[t]$.

**Example 1.4.29 ($\kappa$ is not numerical).** In the same surface, $\pi^*Q$ is numerically trivial. Its multiples have $h^0(m\pi^*Q) = h^0(E, P^m) = 0$, so $\kappa(\pi^*Q) = -\infty$, while $\kappa(0) = 0$. On the other side, $h^0(m\pi^*Q + cA) = \sum_{i=0}^{c} h^0(P^{i + m}(cp)) = c(c + 1)$, so $\kappa_\sigma(\pi^*Q) = 0 = \kappa_\sigma(0)$, as Proposition 1.4.25 predicts. Likewise $C_0 + \pi^*Q$ is numerically equal to $C_0$, and $h^0(m(C_0 + \pi^*Q)) = \sum_{i=0}^m h^0(P^{i + m}) = 0$ for $m \ge 1$, so $\kappa(C_0 + \pi^*Q) = -\infty$ while $\kappa(C_0) = 0$.

**Example 1.4.30 (when $P$ is torsion).** If $P$ has finite order $r$, the same computation gives $h^0(mC_0) = \#\{0 \le i \le m : r \mid i\} = \lfloor m/r \rfloor + 1$, so $\kappa(C_0) = 1 = \kappa_\sigma(C_0)$, the upper bound coming from Theorem 1.4.24, since $C_0$ is not big. The section $C_1$ given by the quotient $\mathcal{V} \to \mathcal{O}_E$ is the divisor of the section $(0, 1)$ of $\mathcal{O}_X(1) \otimes \pi^*P^{-1}$, so $C_1 \sim C_0 - \pi^*Q$, and $C_0 \cap C_1 = \emptyset$, because the two quotients differ at every point. Then $rC_0 \sim rC_1$, and the pencil spanned by $rC_0$ and $rC_1$ has no base points; it is a morphism $X \to \mathbb{P}^1$ whose general fibre $\Gamma \equiv rC_0$ has $\Gamma^2 = K_X \cdot \Gamma = 0$, so has arithmetic genus 1, and its Stein factorization is the Iitaka fibration of $C_0$. The hypothesis of infinite order in Theorem 1.4.26 is exactly what destroys this fibration.

**Example 1.4.31 (nine points on a cubic).** Let $X_9$ be the blow-up of $\mathbb{P}^2$ in nine points of a smooth cubic whose sum has infinite order, as in Example P5.10.26. There $-K$ is nef with $h^0(-mK) = 1$, so $\kappa(-K) = 0$. Also $(-K)^2 = 9 - 9 = 0$, and $-K \not\equiv 0$, since $-K$ is the class of the strict transform of the cubic, an effective nonzero curve. By Proposition 1.4.25, $\kappa_\sigma(-K) = 1$. So $X_9$ is a rational example of the phenomenon of Theorem 1.4.26, and Example 1.4.18 is its counterpart with $\kappa = \kappa_\sigma = 1$.

### Proof

*Proof of Proposition 1.4.23.* (1) If $\sigma(D; A) \ne -\infty$, then $h^0(mD + A) \ge 1 = 1 \cdot m^0$ for infinitely many $m$, so $\sigma(D; A) \ge 0$. By Lemma 1.4.5 with $\mathcal{F} = \mathcal{O}_X$, $\mathcal{L} = \mathcal{O}_X(D)$ and $\mathcal{M} = \mathcal{O}_X(A)$, $h^0(mD + A) \le C m^n$, so no $j > n$ satisfies the condition. The set of values over all ample $A$ is a subset of the finite set $\{-\infty, 0, \dots, n\}$ and has a maximum.

(2) If $A' \sim A + G$ with $G$ effective, multiplication by the section $s_G$ embeds $H^0(mD + A)$ in $H^0(mD + A')$, which gives the first statement. Let $A$ be an ample divisor with $\sigma(D; A) = \kappa_\sigma(D)$. By Serre's theorem P3.6.23, applied to the sheaf $\mathcal{O}_X(-A)$ and the embedding by $H$, the sheaf $\mathcal{O}_X(c_0H - A)$ is globally generated for some $c_0$, so it has a nonzero section and $c_0H - A$ is linearly equivalent to an effective divisor. For $c \ge c_0$, $cH - A$ is equivalent to that divisor plus $(c - c_0)H$, again effective. So $\sigma(D; cH) \ge \sigma(D; A) = \kappa_\sigma(D)$, and the reverse inequality holds because $cH$ is ample.

(3) A linear equivalence does not change any $h^0(mD + A)$. Let $a \ge 1$. If $h^0(m \cdot aD + A) \ge \varepsilon m^j$ for infinitely many $m$, then $h^0(m' D + A) \ge \varepsilon a^{-j} m'^j$ for the infinitely many $m' = am$, so $\sigma(D; A) \ge \sigma(aD; A)$, and $\kappa_\sigma(D) \ge \kappa_\sigma(aD)$. Conversely, let $A$ be ample with $\sigma(D; A) = j = \kappa_\sigma(D) \ge 0$; if $\kappa_\sigma(D) = -\infty$, the first inequality already gives $\kappa_\sigma(aD) = -\infty$. By Serre's theorem as in part 2, applied to the sheaves $\mathcal{O}_X(\rho D - A)$, there is $c$ such that $cH - A + \rho D$ is linearly equivalent to an effective divisor $G_\rho$ for each $\rho = 0, 1, \dots, a - 1$. For each of the infinitely many $m$ with $h^0(mD + A) \ge \varepsilon m^j$, write $m = qa - \rho$ with $q \ge 1$ and $0 \le \rho < a$. Then $qaD + cH \sim (mD + A) + G_\rho$, so $h^0(q \cdot aD + cH) \ge h^0(mD + A) \ge \varepsilon m^j \ge \varepsilon q^j$, since $m \ge q$. Infinitely many $q$ occur, so $\sigma(aD; cH) \ge j$ and $\kappa_\sigma(aD) \ge \kappa_\sigma(D)$.

(4) If $\kappa(D) = -\infty$ there is nothing to prove. Otherwise, by part 2 take $c$ with $\kappa_\sigma(D) = \sigma(D; cH)$; multiplication by a nonzero section of $cH$ embeds $H^0(mD)$ in $H^0(mD + cH)$, so $h^0(mD + cH) \ge a \, m^{\kappa(D)}$ for all large $m \in N(D)$ by Theorem 1.4.6, and $\sigma(D; cH) \ge \kappa(D)$.

(5) Multiplication by $s_F^m$ embeds $H^0(mD + A)$ in $H^0(m(D + F) + A)$ for every $A$.

(6) Let $A$ be ample with $h^0(mD + A) \ne 0$ for infinitely many $m$, let $A'$ be ample and $\varepsilon = p/q$ with $p, q \ge 1$. By Har77, Exercise II.7.5, there is $c$ with $cA' - qA$ ample, and then $c'A' - qA = (c' - c)A' + (cA' - qA)$ is ample for every $c' \ge c$, as a sum of ample divisors. Choose $m$ with $h^0(mD + A) \ne 0$ and $mp \ge c$, and an effective $G \sim mD + A$. Then

$$qm(D + \varepsilon A') = q(mD + A) + (mpA' - qA) \sim qG + (mpA' - qA),$$

an effective divisor plus an ample one. By Corollary 1.4.7, part 4, applied to the Cartier divisor $qm(D + \varepsilon A')$, it is big, and so is the $\mathbb{Q}$-divisor $D + \varepsilon A'$. $\square$

*Proof of Theorem 1.4.24.* Corollary 1.4.7, part 4, gives (3) implies (1), and Proposition 1.4.23, part 4, gives (1) implies (2). Assume (2). Let $H$ be very ample and choose $c$, by Har77, Exercise II.7.5, such that $B = cH$ has $B - A$ ample, where $A$ is an ample divisor with $\sigma(D; A) = n$. Let $Y \in |B|$ be the divisor of a nonzero section of $\mathcal{O}_X(B)$. It is an effective Cartier divisor on the variety $X$, so a projective scheme of dimension $n - 1$. The exact sequence

$$0 \to \mathcal{O}_X(mD + A - B) \to \mathcal{O}_X(mD + A) \to \mathcal{O}_Y(mD + A) \to 0$$

and Lemma 1.4.5 on $Y$, with $\mathcal{F} = \mathcal{O}_Y$, give

$$h^0(mD + A - B) \ge h^0(mD + A) - h^0(Y, \mathcal{O}_Y(mD + A)) \ge \varepsilon m^n - C m^{n-1}$$

for infinitely many $m$. Take such an $m$ with $\varepsilon m > C$. Then $mD + A - B \sim F$ with $F$ effective, so $mD \sim (B - A) + F$ with $B - A$ ample. This is (3). $\square$

*Proof of Proposition 1.4.25.* Let $H$ be very ample. Since $D$ is nef, $D \cdot H \ge 0$. If $D \not\equiv 0$, then $D \cdot H > 0$: otherwise $D \cdot H = 0$, and the Hodge index theorem P5.5.22 gives $D^2 \le 0$, so $D^2 = 0$ and then $D \equiv 0$.

*The lower bounds.* For $c \ge 1$ and $m \ge 0$, Serre duality gives $h^2(mD + cH) = h^0(K - mD - cH)$, which is $0$ as soon as $(K - mD - cH) \cdot H < 0$, because an effective divisor has nonnegative degree on the ample $H$ (Proposition P5.5.5). Since $D \cdot H \ge 0$, this holds for all $m \ge 0$ once $c H^2 > K \cdot H$. Then Riemann-Roch, Theorem P5.5.13, gives

$$h^0(mD + cH) \ge \chi(\mathcal{O}_X) + \tfrac{1}{2}(mD + cH) \cdot (mD + cH - K) = \tfrac{1}{2} m^2 D^2 + \tfrac{1}{2} m (2c \, D \cdot H - D \cdot K) + \chi(cH),$$

with $\chi(cH) = \chi(\mathcal{O}_X) + \frac{1}{2} cH \cdot (cH - K)$, which is positive for large $c$. If $D \equiv 0$, the right side is the positive constant $\chi(cH)$, so $\sigma(D; cH) \ge 0$. If $D^2 = 0$ and $D \not\equiv 0$, the coefficient of $m$ is positive for large $c$, because $D \cdot H > 0$, so $\sigma(D; cH) \ge 1$. If $D^2 > 0$, then $D \cdot H > 0$ as above, $D$ is big by Proposition P5.11.3, part 4, and $\kappa_\sigma(D) = 2$ by Theorem 1.4.24.

*The upper bounds.* If $D \equiv 0$, let $H'$ be the very ample divisor fixed in Proposition P5.11.3. For every ample $A$ the divisor $mD + A$ has $(mD + A) \cdot H' = A \cdot H'$, and part 1 of that proposition gives $h^0(mD + A) \le (A \cdot H' + 1)^2$, a bound independent of $m$. So $\sigma(D; A) \le 0$ and $\kappa_\sigma(D) = 0$. If $D^2 = 0$ and $D \not\equiv 0$, suppose $\kappa_\sigma(D) = 2$. By Theorem 1.4.24, $aD \sim A' + F$ with $A'$ ample and $F$ effective, so $0 = a^2 D^2 = aD \cdot A' + aD \cdot F \ge a D \cdot A' > 0$, using that $D$ is nef and that $D \cdot A' > 0$ by the first paragraph with $A'$ in place of $H$. This is a contradiction, so $\kappa_\sigma(D) = 1$. $\square$

*Proof of Theorem 1.4.26.* (1) By Proposition P3.6.35, part 3, $H^0(X, \mathcal{O}_X(1)) = H^0(E, \mathcal{V}) = H^0(\mathcal{O}_E) \oplus H^0(P) = k \cdot (1, 0)$, since $P$ is a nontrivial line bundle of degree 0 and has no nonzero section. Let $s$ be the section $(1, 0)$. A point of $X$ over $y \in E$ is a one-dimensional quotient of the fibre $\mathcal{V}(y) = k \oplus P(y)$ (Theorem P3.6.34), and $s$ vanishes there exactly when the quotient kills the first summand, that is at the point of the section $C_0$ given by $\mathcal{V} \to P$ (Proposition P3.6.35, part 1). On each fibre $\pi^{-1}(y) \cong \mathbb{P}^1$, $s$ restricts to a nonzero linear form, so $\operatorname{div}(s)$ contains no fibre and meets each fibre in one point with multiplicity one. So $\operatorname{div}(s) = C_0$ and $\mathcal{O}_X(C_0) \cong \mathcal{O}_X(1)$. By Theorem P5.5.6, $C_0 \cdot f = \deg \mathcal{O}_X(1)|_f = 1$, and $C_0^2 = \deg \mathcal{O}_X(1)|_{C_0} = \deg P = 0$, since the restriction of $\mathcal{O}_X(1)$ to the section given by $\mathcal{V} \to P$ is $P$. For every integral curve $C \ne C_0$, $C_0 \cdot C \ge 0$ by Proposition P5.5.5, and $C_0^2 = 0$, so $C_0$ is nef.

(2) By Proposition P3.6.35, part 3, $\pi_* \mathcal{O}_X(m) = \operatorname{Sym}^m \mathcal{V} = \bigoplus_{i=0}^m P^i$. So $h^0(mC_0) = \sum_{i=0}^m h^0(E, P^i)$. For $i \ge 1$, $P^i$ has degree 0 and is not trivial, because $P$ has infinite order, so it has no section; $P^0 = \mathcal{O}_E$ has one. So $h^0(mC_0) = 1$ for all $m \ge 0$, and $\kappa(C_0) = 0$ by Corollary 1.4.7, part 3.

(3) The divisor $A = C_0 + f$ has $A^2 = C_0^2 + 2C_0 \cdot f + f^2 = 0 + 2 + 0 = 2 > 0$, with $f^2 = 0$ because two fibres are disjoint. For an integral curve $C$: if $C$ is a fibre, $A \cdot C = C_0 \cdot f = 1$; if $C = C_0$, $A \cdot C = 0 + 1 = 1$; otherwise $C \cdot C_0 \ge 0$, and $C \cdot f > 0$, because $C$ maps onto $E$ and meets every fibre in a nonempty finite set. So $A \cdot C > 0$ for every integral curve, and $A$ is ample by the Nakai-Moishezon criterion P5.12.5. Let $f = \pi^*p$ for a point $p \in E$. Then $\mathcal{O}_X(mC_0 + cA) = \mathcal{O}_X(m + c) \otimes \pi^* \mathcal{O}_E(cp)$, and by the projection formula P4.4.10 and Proposition P3.6.35, part 3,

$$\pi_* \mathcal{O}_X(mC_0 + cA) = \operatorname{Sym}^{m + c} \mathcal{V} \otimes \mathcal{O}_E(cp) = \bigoplus_{i=0}^{m + c} P^i(cp).$$

Each summand has degree $c \ge 1 > 2g(E) - 2 = 0$, so it has exactly $c$ sections by Corollary P5.1.11, part 2. Hence $h^0(mC_0 + cA) = c(m + c + 1)$.

(4) By part 3, $h^0(mC_0 + cA) \ge c \, m$ for all $m$, so $\sigma(C_0; cA) \ge 1$ and $\kappa_\sigma(C_0) \ge 1$. If $\kappa_\sigma(C_0) = 2$, then $C_0$ would be big by Theorem 1.4.24, while $\kappa(C_0) = 0$. So $\kappa_\sigma(C_0) = 1$. This also follows from Proposition 1.4.25, since $C_0$ is nef, $C_0^2 = 0$ and $C_0 \cdot f = 1$, so $C_0 \not\equiv 0$. $\square$

### Exercises

1. (A) On $\mathbb{P}^1 \times \mathbb{P}^1$, compute $\kappa_\sigma$ of the divisors of bidegree $(a, b)$ for all integers $a, b$, and compare with Example 1.4.9.
2. (A) Show that $\kappa_\sigma(D) = -\infty$ when $-D$ is ample, and that $\kappa_\sigma(D) = 0$ for a divisor of degree 0 on a smooth projective curve, whatever its order in the Picard group.
3. (B) In the surface of Theorem 1.4.26, compute $\kappa$ and $\kappa_\sigma$ of $aC_0 + bf$ for all integers $a, b$. For $b < 0$ or $a < 0$, use that $C_0$ and $f$ are nef to show that $aC_0 + bf$ is not pseudo-effective and that $\kappa_\sigma = -\infty$.
4. (B) Let $X$ be a smooth projective surface, $C$ an integral curve with $C^2 < 0$, and $A$ ample. Show that if $(mC + A) \cdot C < 0$, then $C$ is a fixed component of $|mC + A|$, and $h^0(mC + A) = h^0((m - 1)C + A)$. Deduce that $\kappa_\sigma(C) = 0$, and check this against Example 1.4.27.
5. (B) Let $X$ and $Y$ be smooth projective varieties and $D$ a divisor on $X$. Show that $\kappa_\sigma(p^*D) = \kappa_\sigma(D)$ on $X \times Y$, using Lemma P5.11.4 and ample divisors of the form $A \boxtimes A_Y$.
6. (C) In the surface of Theorem 1.4.26, use $\operatorname{Pic}(X) = \mathbb{Z} C_0 \oplus \pi^* \operatorname{Pic}(E)$ (Har77, Proposition V.2.3) to show that the integral curves $\Gamma$ with $\Gamma \equiv dC_0$, $d \ge 1$, are $C_0$ and the section $C_1$ of Example 1.4.30, so $d = 1$. Show also that $h^0(D) \le 1$ for every divisor $D \equiv mC_0$. Deduce that $\kappa(D) \le 0$ for every $D \equiv mC_0$ with $m \ge 1$, while $\kappa_\sigma(D) = 1$ by Proposition 1.4.25.

### Lean

`MinimalModel.numericalDim` is $\kappa_\sigma$ for an $\mathbb{R}$-divisor $D$: it is $\bot$ when $D$ is not pseudo-effective, and otherwise the largest $\kappa$ such that for some ample Cartier $A$ and some $c > 0$, $h^0(\lfloor mD \rfloor + A) \ge c \, m^\kappa$ for infinitely many $m$. For a Cartier divisor with $\kappa_\sigma(D) \ge 0$ this is Definition 1.4.22. The value $\bot$ is attached to the non pseudo-effective divisors, where Definition 1.4.22 attaches $-\infty$ to the divisors with $\sigma(D; A) = -\infty$ for every ample $A$; the two agree by part 6 of Proposition 1.4.23 and its cited converse. `MinimalModel.IsPseudoEffective` asks for one ample $A$ with $D + \varepsilon A$ big for all $\varepsilon > 0$, which is equivalent to Definition 1.1.26 because the big cone is open. None of the statements of this section is in Lean yet.

### Notes and history

Nakayama introduced $\kappa_\sigma$ and the numerical dimension $\kappa_\nu$ in his memoir of 2004, together with the $\sigma$-decomposition, a version in all dimensions of the Zariski decomposition of P5.8.24. The example of Theorem 1.4.26 is classical, and it is the basic example in the literature on abundance of a nef divisor whose Iitaka dimension is smaller than its numerical dimension. The generalized abundance conjecture asks for $\kappa(K_X + \Delta) = \kappa_\sigma(K_X + \Delta)$ for log canonical pairs; for $\Delta = 0$ and $K_X$ pseudo-effective it implies the non-vanishing conjecture of Chapter 1. Lehmann showed that several other definitions of the numerical dimension agree with $\kappa_\sigma$, and Lesieutre found an example in 2016 in which two of the proposed definitions differ, so the choice of $\kappa_\sigma$ matters. BDPP13 use the dual cone of movable curves to characterize pseudo-effectivity, which is where $\kappa_\sigma \ge 0$ meets the duality of Chapter 3.
