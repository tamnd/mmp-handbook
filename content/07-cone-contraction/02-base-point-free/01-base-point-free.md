---
title: The base point free theorem
nodes: []
sources: [Kaw85, Sho85, KM98, KMM87, Mat02]
reads_with: [KM98:3.3, KMM87:ch3, Mat02:ch6]
requires: [4.2, 5.1, 7.1, P4.2, P7.3, P7.6, P7.9]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The base point free theorem

### Statement

The ground field $k$ is algebraically closed of characteristic $0$. For a Cartier divisor $N$ on a projective variety $X$, the base locus $\operatorname{Bs} |N|$ is the intersection of the supports of the divisors in $|N|$, with $\operatorname{Bs} |N| = X$ if $|N| = \emptyset$, and the *base ideal* $\mathfrak{b}_N$ is the image of $H^0(X, N) \otimes \mathcal{O}_X(-N) \to \mathcal{O}_X$, so that $\operatorname{Bs} |N|$ is the zero set of $\mathfrak{b}_N$. The system $|N|$ is *free* if $\operatorname{Bs} |N| = \emptyset$.

**Theorem 7.2.1 (base point free theorem, Kawamata and Shokurov).** Let $(X, \Delta)$ be a projective klt pair, $D$ a nef Cartier divisor on $X$, and $a > 0$ a rational number such that $aD - (K_X + \Delta)$ is nef and big. Then $|bD|$ is free for every integer $b \gg 0$.

Lean: not yet in Lean. The case $D = r(K_X + \Delta)$ with $K_X + \Delta$ nef and big is part of `MinimalModel.AbundanceBig`; see Corollary 7.2.5.

Two remarks on the statement. Freeness of $|bD|$ forces $D$ to be nef, so the nef hypothesis cannot be dropped. Freeness for one $b$ does not give freeness for $b + 1$, and "for every $b \gg 0$" is what makes $D$ itself, and not only a multiple, the pullback of an ample divisor in Corollary 7.2.4.

### Proof in words

Make $A = aD - (K_X + \Delta)$ ample by adding a small multiple of an effective divisor to $\Delta$. Nonvanishing gives $|mD| \neq \emptyset$ for $m \gg 0$.

The heart of the proof is a claim. If $|mD|$ is nonempty with base points, resolve its base ideal, so that $f^* |mD| = |M| + F_{\mathfrak{b}}$ with $M$ free and $F_{\mathfrak{b}} \neq 0$ over the base locus. Tie-breaking with the discrepancies $a_j$ of $(X, \Delta)$ and the multiplicities $r_j$ of $F_{\mathfrak{b}}$ picks a divisor $F_0$ over the base locus, and
$$f^*(b'D) + B - K_Y = f^*\bigl( (b' - cm - a) D \bigr) + c M + (f^* A - P)$$
is ample for $b' \ge cm + a$. Vanishing lifts sections from $F_0$, nonvanishing on $F_0$ provides them, and the round-up $A_Y$ is exceptional, so sections of $b'D$ on $X$ do not vanish on $f(F_0)$, for every $b' \gg 0$.

For a prime $p$, the base loci of $|p^u D|$ form a decreasing chain of closed sets, which stabilizes. If the stable set were nonempty, the claim with $m = p^u$ and $b' = p^{u'}$ would give a smaller one. So $|p^u D|$ is free for $u \gg 0$, and with a second prime every large $b$ is a combination $\alpha p^u + \beta p'^{u'}$ with $\alpha, \beta \ge 0$.

### Examples

**Example 7.2.2 (the plane blown up at a point).** Let $X = \operatorname{Bl}_x \mathbb{P}^2$, with $h$ the pullback of a line and $e$ the exceptional curve, so $K_X = -3h + e$ and $xh - ye$ is ample exactly when $x > y > 0$. For $D = h$ and every $a \ge 0$, $aD - K_X = (a + 3) h - e$ is ample, and $|bh|$ is free, defining the blow-up $\pi \colon X \to \mathbb{P}^2$ that contracts $e$. For $D = h - e$, the class of a fibre of the ruling, $aD - K_X = (a + 3) h - (a + 1) e$ is ample, and $|b(h - e)|$ is free, defining the ruling $X \to \mathbb{P}^1$. These are the two contractions of the two extremal rays of $\overline{NE}(X)$, and $D \cdot C = 0$ picks out $e$ and the fibres respectively.

**Example 7.2.3 (Zariski's example).** On the blow-up $X$ of $\mathbb{P}^2$ at twelve points of a smooth cubic in Theorem P7.6.22, the divisor $L = 4H - \sum_i E_i$ is nef and big, but $C'$ lies in the base locus of every $|mL|$, so no multiple of $L$ is free. Theorem 7.2.1 does not apply: $K_X = -3H + \sum_i E_i$ gives $K_X \cdot C' = -9 + 12 = 3$, while $L \cdot C' = 0$, so $(aL - K_X) \cdot C' = -3 < 0$ for every $a$, and $aL - K_X$ is never nef. The hypothesis of the theorem controls exactly the curves on which $D$ has degree $0$: they must be $K_X$-negative, up to the boundary.

### Proof

*Step 0: reductions.* Replacing $a$ by $\lceil a \rceil$ keeps the hypothesis by Lemma P7.9.2, so $a$ is a positive integer. By Lemma 5.1.9, over a point, there is an effective $\mathbb{Q}$-Cartier divisor $E$ with $aD - (K_X + \Delta) - \varepsilon E$ ample for $0 < \varepsilon \le 1$, and by Lemma 5.1.10, $(X, \Delta + \varepsilon E)$ is klt for $\varepsilon$ small. Replacing $\Delta$ by $\Delta + \varepsilon E$, assume that $A = aD - (K_X + \Delta)$ is ample. By Corollary 7.1.8 there is $m_1$ with $H^0(X, mD) \neq 0$ for every $m \ge m_1$.

*Step 1: the claim.* Let $m \ge 1$ with $|mD| \neq \emptyset$ and $\operatorname{Bs} |mD| \neq \emptyset$. Then there is a closed irreducible subset $W \subseteq \operatorname{Bs} |mD|$ such that $W \not\subseteq \operatorname{Bs} |b'D|$ for every $b' \gg 0$.

Let $f \colon Y \to X$ and $P_A$ be given by Lemma 7.1.2 for $\Delta$, $\Gamma = 0$, $\mathfrak{b} = \mathfrak{b}_{mD}$ and $H = A$, with prime divisors $F_1, \dots, F_s$. Then $\mathfrak{b} \cdot \mathcal{O}_Y = \mathcal{O}_Y(-F_{\mathfrak{b}})$, and the pullbacks of the sections of $mD$ generate $\mathcal{O}_Y(f^*(mD) - F_{\mathfrak{b}})$, so $M = f^*(mD) - F_{\mathfrak{b}}$ is free, hence nef by part 1 of Proposition P7.3.9. Since $f$ is surjective, the zero set of $\mathfrak{b} \cdot \mathcal{O}_Y$ is $f^{-1}(\operatorname{Bs} |mD|) \neq \emptyset$, so $F_{\mathfrak{b}} \neq 0$ and $\operatorname{Supp} F_{\mathfrak{b}} = f^{-1}(\operatorname{Bs} |mD|)$. Write
$$K_Y = f^*(K_X + \Delta) + \sum_j a_j F_j, \qquad F_{\mathfrak{b}} = \sum_j r_j F_j.$$
Since $(X, \Delta)$ is klt, every $a_j > -1$; along a non-exceptional $F_j$, $a_j$ is minus the coefficient of $\Delta$, so $a_j \le 0$. Some $r_j > 0$. Apply Lemma 7.1.3 with $U = f^* A$, $P_0 = P_A$ and $\eta = c_0/2$. It gives $c \in (c_0/2, c_0]$, $P$ with $f^* A - P$ ample, and $F_0 = F_{j_0}$ with $r_{j_0} > 0$, and
$$B = \sum_j (a_j - c r_j - p'_j) F_j = K_Y - f^*(K_X + \Delta) - c F_{\mathfrak{b}} - P,$$
with $\lceil B \rceil = A_Y - F_0$ and $\Theta = \lceil B \rceil - B$ as in that lemma. For every integer $b'$,
$$f^*(b'D) + B - K_Y = f^*\bigl( b'D - (K_X + \Delta) \bigr) - c\bigl( f^*(mD) - M \bigr) - P = f^*\bigl( (b' - a - cm) D \bigr) + cM + (f^* A - P).$$
For $b' \ge b_1 = \lceil a + cm \rceil$ this is a sum of two nef divisors and an ample one, hence ample by part 3 of Theorem P7.3.12.

The divisor $A_Y$ is $f$-exceptional: along a non-exceptional $F_j$ with $j \neq j_0$ its coefficient is $\lceil b_j \rceil \le \lceil a_j \rceil \le 0$ by part 1 of Lemma 7.1.3, hence $0$, and it has no component $F_0$. Let $b' \ge b_1$. As in Step 5 of the proof of Theorem 7.1.7, part 1 of Corollary 5.1.14 for the klt pair $(Y, \Theta)$ and $N = f^*(b'D) + A_Y - F_0$ gives $H^1(Y, N) = 0$, so
$$H^0(Y, f^*(b'D) + A_Y) \to H^0(F_0, (f^*(b'D) + A_Y)|_{F_0})$$
is surjective. If $\dim X = 1$, then $F_0$ is a point and the right side is $k$. Otherwise $F_0$ is smooth projective of dimension $\dim X - 1$, $D_0 = (f^* D)|_{F_0}$ is nef, $G_0 = (B + F_0)|_{F_0}$ has snc support with $\lceil G_0 \rceil = A_Y|_{F_0} \ge 0$, and $b_1 D_0 + G_0 - K_{F_0} = (f^*(b_1 D) + B - K_Y)|_{F_0}$ is ample, by Lemma 7.1.3 and adjunction. By Theorem 7.1.7 the right side is nonzero for $b' \gg 0$. So for $b' \gg 0$ some section of $f^*(b'D) + A_Y$ does not vanish along $F_0$, and by part 2 of Lemma 7.1.6, $f(F_0) \not\subseteq \operatorname{Bs} |b'D|$. Since $r_{j_0} > 0$, $F_0 \subseteq \operatorname{Supp} F_{\mathfrak{b}} = f^{-1}(\operatorname{Bs} |mD|)$, so $W = f(F_0)$ proves the claim.

*Step 2: powers of a prime.* Let $p$ be a prime. If $s \in H^0(X, p^u D)$, then $s^{p^{u'-u}} \in H^0(X, p^{u'} D)$ for $u' \ge u$ has the same support, so $\operatorname{Bs} |p^{u'} D| \subseteq \operatorname{Bs} |p^u D|$. The sequence of closed sets $\operatorname{Bs} |p^u D|$, $u \ge 0$, is decreasing, so it is constant for $u \ge u_0$, with value $Z_p$. Choose $u \ge u_0$ with $p^u \ge m_1$, so $|p^u D| \neq \emptyset$. If $Z_p \neq \emptyset$, Step 1 with $m = p^u$ gives $W \subseteq Z_p$ with $W \not\subseteq \operatorname{Bs} |p^{u'} D| = Z_p$ for $u'$ large, which is absurd. So $|p^u D|$ is free for every $u \ge u_0$.

*Step 3: two primes.* Let $p \neq p'$ be primes and choose $u, u'$ with $|p^u D|$ and $|p'^{u'} D|$ free. Since $p^u$ and $p'^{u'}$ are coprime, every integer $b \ge p^u p'^{u'}$ is $\alpha p^u + \beta p'^{u'}$ with integers $\alpha, \beta \ge 0$. Products of sections of free systems give $\operatorname{Bs} |bD| \subseteq \operatorname{Bs} |p^u D| \cup \operatorname{Bs} |p'^{u'} D| = \emptyset$, so $|bD|$ is free for every $b \ge p^u p'^{u'}$.

### Exercises

1. (A) Show that if $|bD|$ is free for some $b \ge 1$, then $D$ is nef, and that freeness of $|2D|$ and $|3D|$ implies freeness of $|bD|$ for every $b \ge 2$.
2. (A) In Example 7.2.2, compute $\operatorname{Bs} |m(h - e)|$ and $\operatorname{Bs} |mh|$ for every $m \ge 1$ directly.
3. (A) Show that every integer $b \ge (\alpha_0 - 1)(\beta_0 - 1)$ is a nonnegative combination of coprime positive integers $\alpha_0$ and $\beta_0$, and give the bound on $b$ that results in Step 3.
4. (B) Let $E$ be an elliptic curve, $X = E \times \mathbb{P}^1$ and $D = \operatorname{pr}_1^* D_E$ for a divisor $D_E$ of degree $0$ on $E$ that is not torsion. Show that $D$ is nef, that $aD - K_X$ is nef but not big for every $a$, and that $|bD| = \emptyset$ for every $b \ge 1$.
5. (B) Show that in Step 1 the divisor $W = f(F_0)$ can be taken to be an irreducible component of $\operatorname{Bs} |mD|$ when $\operatorname{Bs} |mD|$ is a finite set of points, and give an example on a surface where $W$ is a point of a curve in the base locus.
6. (C) Prove the relative version of Theorem 7.2.1 for a projective morphism $\pi \colon X \to S$ to a quasi-projective variety, with $D$ $\pi$-nef and $aD - (K_X + \Delta)$ $\pi$-nef and $\pi$-big, by running Steps 0 to 3 with relative base loci and Theorem 5.1.13 in place of Corollary 5.1.14. Which step needs nonvanishing over $S$, and how does it follow from Theorem 7.1.7 on the generic fibre?

### Lean

The library has `MinimalModel.IsSemiample` and `MinimalModel.IsFree` and the statement `MinimalModel.AbundanceBig`, the case of Corollary 7.2.5 with real coefficients, without proof. Theorem 7.2.1 itself is not yet in Lean.

### Notes and history

The theorem is due to Kawamata (Kaw85), who proved it under an additional nonvanishing hypothesis, and Shokurov (Sho85), whose nonvanishing theorem removed it. Reid's account, with the Noetherian induction on base loci, made the argument standard. The proof here is KM98, Theorem 3.3, with the descent through Lemma 7.1.6 written out. The relative version, KM98, Theorem 3.24, is the form used for contractions over a base; this volume proves only the absolute version, and Exercise 6 outlines the changes. Fujino (Fuj17d) proves the version for lc pairs and quasi-log schemes, which Chapter 6 sketches.
