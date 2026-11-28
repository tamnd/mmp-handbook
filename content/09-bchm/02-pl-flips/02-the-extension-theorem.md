---
title: The extension theorem
nodes: []
sources: [HM07, HM06, Cor07, Siu98, Kaw07, Tak06, Laz04]
reads_with: [HM07:5, Cor07:4]
requires: [1.3, 4.5, 5.1, 5.3, 5.5, 7.2, P7.7]
level: advanced
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The extension theorem

### Statement

The extension theorem compares the sections of $m(K_X + \Delta)$ restricted to a component $S$ of $\Delta$ with the sections of an adjoint divisor $m(K_S + \Theta)$ on $S$. Volume 5 states it as Theorem 5.5.16 and proves the vanishing theorems behind it. This section sets up the fixed divisors that define $\Theta$, restates the theorem in the form used for pl flips and draws its consequence for restricted algebras.

**Definition 9.2.6 (restricted linear systems and asymptotic fixed divisors).** Let $X$ be a normal projective variety, $S$ a normal prime divisor and $D$ a Cartier divisor on $X$. The *restricted linear system* $|D|_S$ is the set of divisors $G|_S$ with $G \in |D|$ and $S \not\subseteq \operatorname{Supp} G$, a linear system on $S$, possibly incomplete or empty. If it is not empty, $\operatorname{Fix}(|D|_S)$ is its fixed divisor, the largest divisor $F$ on $S$ with $G' \ge F$ for every $G' \in |D|_S$. Let $D$ be a $\mathbb{Q}$-divisor and $k \ge 1$ an integer with $kD$ Cartier and $S \not\subseteq \mathbf{B}(D)$, the stable base locus of Definition P7.7.12. For $m$ divisible by $k$ put $F_m = \operatorname{Fix}(|mD|_S)$ when $|mD|_S$ is not empty, and
$$F = F(D, S) = \lim_{m} \frac{1}{m} F_m,$$
the limit over the integers $m$ divisible by $k$ with $|mD|_S$ not empty, taken coefficient by coefficient.

**Lemma 9.2.7 (the asymptotic fixed divisor exists).** In Definition 9.2.6 the set $\Lambda$ of integers $m$ divisible by $k$ with $|mD|_S$ not empty contains all large multiples of some $m_0$, it is closed under addition, and $F_{m_1 + m_2} \le F_{m_1} + F_{m_2}$ for $m_1, m_2 \in \Lambda$. The limit $F$ exists, it does not depend on $k$, and it equals the coefficientwise infimum of $\frac1m F_m$ over $m \in \Lambda$. In particular $F_m \ge mF$ for every $m \in \Lambda$.

Lean: not yet in Lean.

**Theorem 9.2.8 (Hacon and McKernan, the extension theorem).** Let $X$ be smooth and projective and $\Delta = S + A + B$ a $\mathbb{Q}$-divisor with simple normal crossing support, where $S$ is a smooth prime divisor, $A$ is a general ample $\mathbb{Q}$-divisor and $B \ge 0$ with $\lfloor B \rfloor = 0$ and $S \not\subseteq \operatorname{Supp} B$. Let $k \ge 1$ with $k(K_X + \Delta)$ Cartier and suppose $S \not\subseteq \mathbf{B}(K_X + \Delta)$. Put $\Omega = (\Delta - S)|_S$, let $F = F(K_X + \Delta, S)$ be as in Definition 9.2.6 and $\Theta = \Omega - \Omega \wedge F$. Then for every $m$ divisible by $k$ with $m\Theta$ integral,
$$|m(K_S + \Theta)| + m(\Omega - \Theta) \subseteq |m(K_X + \Delta)|_S.$$

Lean: not yet in Lean.

This is Theorem 5.5.16, with the limit written as in Definition 9.2.6; the hypotheses are those of the source HM07, and Cor07 gives a version for $X$ projective over an affine variety, which is the case needed for pl flips.

**Corollary 9.2.9 (the restricted algebra is an adjoint algebra).** In Theorem 9.2.8, for every $m$ divisible by $k$ with $m\Theta$ integral,
$$|m(K_X + \Delta)|_S = |m(K_S + \Theta)| + m(\Omega - \Theta).$$
If $\Theta$ is a $\mathbb{Q}$-divisor and $r$ is a multiple of $k$ with $r\Theta$ integral, multiplication by a section of $\mathcal{O}_S(r(\Omega - \Theta))$ in each degree identifies $R(S, r(K_S + \Theta))$ with the Veronese subalgebra in degrees divisible by $r$ of $\operatorname{res}_S R(X, k(K_X + \Delta))$, read in degrees $m/k$. In particular the restricted algebra is finitely generated if and only if the adjoint algebra $R(S, r(K_S + \Theta))$ is.

Lean: not yet in Lean.

**Lemma 9.2.10 (the nef and big case).** In Theorem 9.2.8, suppose $K_X + \Delta$ is nef and big. Then for every $m \ge 2$ with $m(K_X + \Delta)$ Cartier the restriction map
$$H^0(X, \mathcal{O}_X(m(K_X + \Delta))) \to H^0(S, \mathcal{O}_S(m(K_S + \Omega)))$$
is surjective, so $|m(K_X + \Delta)|_S = |m(K_S + \Omega)|$. If in addition $K_S + \Omega$ is big, then $F = 0$ and $\Theta = \Omega$.

Lean: not yet in Lean.

### Proof in words

The fixed divisors are subadditive because the product of two sections is a section, so their averages converge to an infimum, as for any subadditive sequence. The extension theorem says that every section of $m(K_S + \Theta)$, shifted by the part $m(\Omega - \Theta)$ that every restricted section must contain, extends to $X$. The opposite inclusion is free: every restricted divisor contains the fixed divisor, which is at least $m(\Omega \wedge F) = m(\Omega - \Theta)$. So the restricted linear systems are adjoint linear systems on $S$, and the restricted algebra is an adjoint ring in dimension $n - 1$.

When $K_X + \Delta$ is nef and big no asymptotic analysis is needed: $m(K_X + \Delta) - (K_X + S)$ differs from the nef and big divisor $(m - 1)(K_X + \Delta)$ by the klt part $A + B$ of the boundary, and the klt extension theorem of Volume 5 applies. The general proof runs the same vanishing argument with an asymptotic multiplier ideal in place of $A + B$, and its difficulty is to control that ideal on $S$.

### Examples

**Example 9.2.11 (a nonzero asymptotic fixed divisor).** Let $X = \operatorname{Bl}_p \mathbb{P}^2$ with line class $L$ and exceptional curve $E$, and let $S \sim L - E$ be the strict transform of a line through $p$, so $S \cong \mathbb{P}^1$, $S^2 = 0$ and $S \cdot E = 1$; put $q = S \cap E$. Let $G \in |6L - E|$ be general, $A = \frac12 G$, $B = \frac34 E$ and $\Delta = S + A + B$. The support $S + G + E$ has simple normal crossings, $A$ is a general ample $\mathbb{Q}$-divisor and $\lfloor B \rfloor = 0$. Since $K_X = -3L + E$,
$$K_X + \Delta \sim_{\mathbb{Q}} -3L + E + (L - E) + (3L - \tfrac12 E) + \tfrac34 E = L + \tfrac14 E.$$
Take $k = 4$. For $m$ divisible by $4$, every divisor in $|mL + \frac m4 E|$ contains $\frac m4 E$, since $H^0(X, \mathcal{O}(mL + jE)) = H^0(\mathbb{P}^2, \mathcal{O}(m))$ for $j \ge 0$, and the moving part $|mL|$ is base point free, so $S \not\subseteq \mathbf{B}(K_X + \Delta)$. Restricting to $S$, where $L|_S$ has degree $1$ and the restriction $H^0(\mathbb{P}^2, \mathcal{O}(m)) \to H^0(\mathbb{P}^1, \mathcal{O}(m))$ to a line is surjective,
$$|m(K_X + \Delta)|_S = |\mathcal{O}_S(m)| + \tfrac m4 q, \qquad F_m = \tfrac m4 q, \qquad F = \tfrac14 q.$$
Here $\Omega = A|_S + \frac34 q$, where $A|_S$ is $\frac12$ times five general points of $S$, as $G \cdot S = 5$. So $\Omega \wedge F = \frac14 q$, $\Theta = A|_S + \frac12 q$ and $\Omega - \Theta = \frac14 q$. The degree of $K_S + \Theta$ is $-2 + \frac52 + \frac12 = 1$, so for $m$ divisible by $4$, $|m(K_S + \Theta)| = |\mathcal{O}_S(m)|$, and Corollary 9.2.9 reads $|m(K_X + \Delta)|_S = |\mathcal{O}_S(m)| + \frac m4 q$, in agreement with the direct computation. The naive guess $\Theta = \Omega$ fails: $K_S + \Omega$ has degree $\frac54$, and $|m(K_S + \Omega)|$ is larger than the restricted system.

**Example 9.2.12 (the nef and big case on the same surface).** In Example 9.2.11 replace $B$ by $B' = \frac34 G'$ for a second general $G' \in |L|$, so that $\Delta' = S + \frac12 G + \frac34 G'$ and $K_X + \Delta' \sim_{\mathbb{Q}} \frac74 L - \frac12 E$, which is ample since $(\frac74 L - \frac12 E) \cdot E = \frac12$ and $(\frac74 L - \frac12 E) \cdot (L - E) = \frac54$. Lemma 9.2.10 applies: the restriction to $S$ is surjective in every degree $m \ge 2$ divisible by $4$, $F = 0$ and $\Theta = \Omega = \frac12 G|_S + \frac34 G'|_S$, of degree $\frac52 + \frac34$, and $K_S + \Theta$ has degree $\frac54 = (K_X + \Delta') \cdot S$.

### Proof

*Lemma 9.2.7.* The set $\Lambda$ is not empty, since $S \not\subseteq \mathbf{B}(D)$ gives $m_0$ divisible by $k$ and $G \in |m_0 D|$ with $S \not\subseteq \operatorname{Supp} G$. If $G_i \in |m_i D|$ with $S \not\subseteq \operatorname{Supp} G_i$ for $i = 1, 2$, then $G_1 + G_2 \in |(m_1 + m_2) D|$, it does not contain $S$, and $(G_1 + G_2)|_S = G_1|_S + G_2|_S$. So $\Lambda$ is closed under addition and contains all multiples of $m_0$, and since $G_i|_S$ runs through $|m_i D|_S$, every member of $|m_1 D|_S + |m_2 D|_S$ lies in $|(m_1 + m_2) D|_S$, whose fixed divisor is therefore at most $F_{m_1} + F_{m_2}$.

Fix a prime divisor $P$ of $S$ and let $a_m$ be the coefficient of $P$ in $F_m$ for $m \in \Lambda$, so $a_m \ge 0$ and $a_{m_1 + m_2} \le a_{m_1} + a_{m_2}$. Let $g$ be the greatest common divisor of $\Lambda$. A subsemigroup of $g\mathbb{Z}_{> 0}$ with greatest common divisor $g$ contains every multiple of $g$ beyond some bound $N$. Let $c = \inf_{m \in \Lambda} a_m / m$, let $\varepsilon > 0$, and choose $m_1 \in \Lambda$ with $a_{m_1} / m_1 < c + \varepsilon$. Every $m \in \Lambda$ with $m \ge N + m_1$ can be written $m = q m_1 + r$ with $q \ge 0$ and $r$ a multiple of $g$ in $[N, N + m_1)$, so $r \in \Lambda$ and $r$ ranges over a finite set. Then $a_m \le q a_{m_1} + a_r \le (m / m_1) a_{m_1} + \max_r a_r$, and so $\limsup_m a_m / m \le a_{m_1} / m_1 < c + \varepsilon$. As $a_m / m \ge c$ for all $m$, $a_m / m \to c$. Only the finitely many $P$ in $F_{m_0}$ can have $c > 0$, since $F_{l m_0} \le l F_{m_0}$, so the limit holds for the divisor. Replacing $k$ by a multiple $k'$ replaces $\Lambda$ by $\Lambda \cap k'\mathbb{Z}$, which contains all large multiples of $\operatorname{lcm}(g, k')$, and the infimum argument above, run inside it, gives the same limit because a limit along a sequence agrees with the limit along a subsequence. The last statement is $c \le a_m / m$.

*Theorem 9.2.8.* This is Theorem 5.5.16, cited from HM07. An outline of its proof, following HM07 and Cor07, is given here; it is an outline and not a proof.

1. *Reduction.* One may replace $X$ by a log resolution and perturb $\Delta$ so that the components of $\Omega$ do not meet one another in a way that obstructs the next steps. The general ample divisor $A$ absorbs the perturbation.
2. *Asymptotic multiplier ideals.* For $m$ divisible by $k$ the sections of $|m(K_X + \Delta)|$ define an asymptotic multiplier ideal $\mathcal{J}(\lVert m(K_X + \Delta) \rVert)$ in the sense of Definition 5.5.3, and on $S$ its restriction is controlled by $F$: the ideal of $S$ contains $\mathcal{O}_S(-\lfloor m F \rfloor - \text{a bounded error})$.
3. *Extension by vanishing.* Write $m(K_X + \Delta) = K_X + S + L$ with $L = (m - 1)(K_X + \Delta) + A + B$. Theorem 5.5.11, with the asymptotic multiplier ideal playing the part of $\mathcal{J}(S, D|_S)$, extends every section of $m(K_S + \Omega)$ that vanishes along a divisor of size about $m(\Omega \wedge F)$ plus the error. The argument extends sections of the form $\sigma \cdot \tau^{l}$ inductively in $l$, in the manner of Siu98 and Kaw07, with a section $\tau$ of a multiple of $A$ absorbing the error.
4. *Removing the error.* The error terms are of size bounded independently of $m$, and a Diophantine approximation, using that $\Theta$ has coefficients in $[0, 1)$, removes them for $m$ divisible enough with $m\Theta$ integral.

*Corollary 9.2.9.* The inclusion of the right side in the left is Theorem 9.2.8. Conversely let $G' \in |m(K_X + \Delta)|_S$, so $G' = G|_S$ with $G \in |m(K_X + \Delta)|$ and $S \not\subseteq \operatorname{Supp} G$. By adjunction for the snc pair $(X, \Delta)$, Theorem 4.5.17 with zero different, $(K_X + \Delta)|_S = K_S + \Omega$, so $G' \sim m(K_S + \Omega)$. By Lemma 9.2.7, $G' \ge F_m \ge mF \ge m(\Omega \wedge F) = m(\Omega - \Theta)$. So $G' - m(\Omega - \Theta)$ is effective and linearly equivalent to $m(K_S + \Omega) - m(\Omega - \Theta) = m(K_S + \Theta)$, which proves equality.

For the algebras, let $\sigma_j \in H^0(S, \mathcal{O}_S(jr(\Omega - \Theta)))$ be the section with divisor $jr(\Omega - \Theta)$, so $\sigma_j \sigma_{j'} = \sigma_{j + j'}$. By the equality just proved, applied with $m = jr$, multiplication by $\sigma_j$ maps $H^0(S, \mathcal{O}_S(jr(K_S + \Theta)))$ onto the degree $jr/k$ part of $\operatorname{res}_S R(X, k(K_X + \Delta))$, injectively, and these maps are compatible with products. So the two graded algebras are isomorphic, and the restricted algebra is finitely generated if and only if this Veronese subalgebra is, since for a graded integral domain $R$ with $R_0$ noetherian, $R$ is finitely generated if and only if $R^{(r)}$ is. The restricted algebra is such a domain, as a graded subring of $\bigoplus_m H^0(S, \mathcal{O}_S(mk(K_S + \Omega)))$ on the integral variety $S$. One direction is that $R^{(r)}$ is the ring of invariants of the action of the $r$-th roots of unity that multiplies $R_m$ by $\zeta^m$, and invariants of a finite group acting on a finitely generated algebra are finitely generated. For the other, if $R^{(r)}$ is finitely generated, $R$ is integral over it, since $x^r \in R^{(r)}$ for homogeneous $x$; and for each residue $i$ modulo $r$ with $M_i = \bigoplus_j R_{jr + i}$ not zero, multiplication by $t^{r - 1}$ for a fixed nonzero homogeneous $t \in M_i$ embeds $M_i$ in $R^{(r)}$ as an $R^{(r)}$-module, so $M_i$ is a finitely generated module over the noetherian ring $R^{(r)}$, and $R = \bigoplus_i M_i$ is finitely generated.

*Lemma 9.2.10.* Write $m(K_X + \Delta) = K_X + S + L$ with $L = m(K_X + \Delta) - K_X - S$, a Cartier divisor because $X$ is smooth and $m(K_X + \Delta)$ is Cartier. Let $D = A + B$, an effective $\mathbb{Q}$-divisor with $S \not\subseteq \operatorname{Supp} D$. Then $L - D = (m - 1)(K_X + \Delta)$ is nef and big, and $(S, D|_S) = (S, \Omega)$ is klt, because $\Omega$ has simple normal crossing support and coefficients in $[0, 1)$. By Corollary 5.5.12 the restriction $H^0(X, \mathcal{O}_X(K_X + S + L)) \to H^0(S, \mathcal{O}_S(K_S + L|_S))$ is surjective, and $K_S + L|_S = (K_X + S + L)|_S = m(K_S + \Omega)$. Every divisor of $|m(K_S + \Omega)|$ is therefore the restriction of a divisor of $|m(K_X + \Delta)|$ not containing $S$, which is the equality of linear systems. If $K_S + \Omega = (K_X + \Delta)|_S$ is also big, it is a nef and big log canonical divisor of the klt pair $(S, \Omega)$, so it is semiample by Corollary 7.2.5, and $|m(K_S + \Omega)|$ is base point free for all large $m$ divisible by some $m_1$. For those $m$, $F_m = 0$, and Lemma 9.2.7 gives $F = 0$, so $\Theta = \Omega$.

### Exercises

1. (A) In Example 9.2.11, compute $F_m$ for every $m$ divisible by $4$ directly, and check that $\frac1m F_m$ is constant.
2. (A) Give an example of a divisor $D$ on a surface $X$ and a curve $S$ for which $|mD|_S$ is not the complete linear system $|mD|_S|$ on $S$ for any $m \ge 1$.
3. (B) Show that the limit $F$ of Lemma 9.2.7 can have irrational coefficients when $D$ is an $\mathbb{R}$-divisor, and that it is rational on a toric variety with a torus-invariant $\mathbb{Q}$-divisor $D$.
4. (B) In Example 9.2.11 replace $B = \frac34 E$ by $B = bE$ with $0 \le b < 1$. Compute $F$, $\Theta$ and $|m(K_S + \Theta)|$ as functions of $b$, and find the values of $b$ for which $S \not\subseteq \mathbf{B}(K_X + \Delta)$.
5. (B) Prove that $\Theta$ in Theorem 9.2.8 satisfies $0 \le \Theta \le \Omega$, so that $(S, \Theta)$ is klt, and that $K_S + \Theta$ is pseudo-effective whenever $|m(K_X + \Delta)|_S$ is not empty for some $m$.
6. (C) Let $X = \mathbb{P}^1 \times \mathbb{P}^1$, $S$ a fibre of the first projection and $\Delta = S + A + B$ with $B$ supported on fibres of both projections. Show that $F = 0$ for every admissible $\Delta$, and determine when $|m(K_X + \Delta)|_S$ is the complete linear system $|m(K_S + \Omega)|$.

### Lean

Nothing in this section is in Lean. The library has no restricted linear system, no fixed divisor and no multiplier ideal.

### Notes and history

The extension theorem grew out of Siu's proof of the deformation invariance of plurigenera, Siu98, and its algebraic treatment by Kawamata, Kaw07, and Takayama, Tak06, which are Theorems 5.5.13 to 5.5.15. Hacon and McKernan proved the version with a boundary and the correction $\Theta$ in HM06 and HM07, and used it to prove the existence of pl flips from finite generation in lower dimension. The exposition of Cor07, Chapter 4, written with Hacon and McKernan's input, is the standard reference for the relative form over an affine base. Example 9.2.11 is constructed to show the correction: the boundary has a component $E$ that is in the stable base locus of $K_X + \Delta$ and meets $S$, and the asymptotic fixed divisor removes part of its trace.
