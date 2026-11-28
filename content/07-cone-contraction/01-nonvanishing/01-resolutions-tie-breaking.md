---
title: Resolutions and tie-breaking
nodes: []
sources: [KM98, Kaw85, KMM87, Laz04]
reads_with: [KM98:3.3, KMM87:ch2, Laz04:ch9]
requires: [4.1, 4.2, P4.2, P7.1, P7.3, P7.5, P7.8, P7.9, P7.10]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Resolutions and tie-breaking

### Statement

The ground field $k$ is algebraically closed of characteristic $0$. A curve on a projective variety $V$ is an integral closed subscheme of dimension $1$, and a $\mathbb{Q}$-Cartier divisor $D$ on $V$ is *numerically trivial*, written $D \equiv 0$, if $D \cdot C = 0$ for every curve $C \subseteq V$. For a $\mathbb{Q}$-divisor $B = \sum_j b_j F_j$ with distinct prime divisors $F_j$, the round-up is $\lceil B \rceil = \sum_j \lceil b_j \rceil F_j$.

**Lemma 7.1.1 (nef against ample).** Let $V$ be a projective variety of dimension $d \ge 1$, $D$ a nef $\mathbb{Q}$-Cartier divisor and $A$ an ample $\mathbb{Q}$-Cartier divisor on $V$.

1. $(D^k \cdot A^{d-k} \cdot V) \ge 0$ for $0 \le k \le d$.
2. If $(D \cdot A^{d-1} \cdot V) = 0$, then $D \equiv 0$ on $V$.

Lean: not yet in Lean.

**Lemma 7.1.2 (a log resolution with an ample perturbation).** Let $X$ be a normal projective variety, $\Delta$ a $\mathbb{Q}$-divisor, $\Gamma$ a reduced divisor, $\mathfrak{b} \subseteq \mathcal{O}_X$ a nonzero ideal sheaf and $H$ an ample $\mathbb{Q}$-Cartier divisor on $X$. There are a projective birational morphism $f \colon Y \to X$ from a smooth projective variety and an effective $\mathbb{Q}$-divisor $P_H$ on $Y$ with the following properties.

1. $\operatorname{Exc}(f)$ is a divisor, and $\mathfrak{b} \cdot \mathcal{O}_Y = \mathcal{O}_Y(-F_{\mathfrak{b}})$ for an effective divisor $F_{\mathfrak{b}}$.
2. $f^* H - P_H$ is ample.
3. The union of $\operatorname{Exc}(f)$, $\operatorname{Supp} F_{\mathfrak{b}}$, $\operatorname{Supp} P_H$ and $f^{-1}_*(\operatorname{Supp} \Delta \cup \Gamma)$ is the support of a reduced snc divisor $\sum_{j=1}^s F_j$.

In particular, if $K_X + \Delta$ is $\mathbb{Q}$-Cartier, then $f$ is a log resolution of $(X, \Delta)$ in the sense of Definition 4.2.9, and every divisor of the form $K_Y - f^*(K_X + \Delta)$, $F_{\mathfrak{b}}$, $P_H$ or $f^* N$ with $\operatorname{Supp} N \subseteq \Gamma$ is a combination of the $F_j$.

Lean: not yet in Lean.

**Lemma 7.1.3 (tie-breaking).** Let $Y$ be a smooth projective variety and $\sum_{j=1}^s F_j$ a reduced snc divisor on $Y$. Let $a_j > -1$, $r_j \ge 0$ and $p_j \ge 0$ be rational numbers, with some $r_j > 0$, put $P_0 = \sum_j p_j F_j$, and let $U$ be a nef $\mathbb{Q}$-divisor with $U - P_0$ ample. Put
$$c_0 = \min \Bigl\{ \frac{1 + a_j}{r_j} : r_j > 0 \Bigr\} > 0.$$
For every $\eta > 0$ there are a rational number $c$ with $\max(0, c_0 - \eta) < c \le c_0$, an effective $\mathbb{Q}$-divisor $P = \sum_j p'_j F_j$ with $U - P$ ample, and an index $j_0$ with $r_{j_0} > 0$, such that the numbers
$$b_j = a_j - c r_j - p'_j$$
satisfy $b_{j_0} = -1$ and $b_j > -1$ for $j \neq j_0$. For $B = \sum_j b_j F_j$ and $F_0 = F_{j_0}$:

1. $\lceil B \rceil = A_Y - F_0$, where $A_Y = \sum_{j \neq j_0} \lceil b_j \rceil F_j$ is effective, has no component $F_0$, and has coefficient $\lceil b_j \rceil \le \lceil a_j \rceil$ along $F_j$.
2. $\Theta = \lceil B \rceil - B$ has snc support, coefficients in $[0, 1)$ and no component $F_0$, so $(Y, \Theta)$ is klt.
3. $F_0$ is a smooth projective variety, $G_0 = (B + F_0)|_{F_0}$ is a $\mathbb{Q}$-divisor with snc support on $F_0$, $\lceil G_0 \rceil = A_Y|_{F_0}$, and $\Theta|_{F_0}$ has snc support and coefficients in $[0, 1)$.

Lean: not yet in Lean.

The number $c_0$ is the log canonical threshold of Definition 4.6.1 in the cases of Section 2 and Chapters 2 and 3, computed on the resolution, but the lemma uses only the numbers $a_j$ and $r_j$.

### Proof in words

For Lemma 7.1.1, cut $V$ by general members of a very ample multiple of $A$: the intersection numbers become intersection numbers of $D$ on subvarieties, which are nonnegative because $D$ is nef. For the second part, a curve $C \subseteq V$ lies in a member of $|mA|$ that contains $C$, and the vanishing of $D \cdot A^{d-1}$ passes to the component through $C$, so induction on $d$ reaches $D \cdot C = 0$.

For Lemma 7.1.2, resolve first so that $\mathfrak{b}$ becomes invertible. The pullback of $H$ is nef and big, so by Kodaira's lemma it is an ample divisor plus an effective one. A second resolution, given by Theorem P7.8.15, makes all the divisors in sight snc and provides an exceptional divisor whose negative is relatively ample.

For Lemma 7.1.3, the threshold $c$ at which the first coefficient reaches $-1$ may be reached by several $F_j$ at once. Subtracting a small multiple $s P_0$ moves the threshold only a little, and then lowering $c$ slightly and subtracting a small multiple of the chosen $F_{j_0}$ keeps $F_{j_0}$ at $-1$ and lifts every other tied coefficient above $-1$. Ampleness of $U - P$ survives because the ample cone is open.

### Examples

**Example 7.1.4 (the cusp).** Let $X = \mathbb{P}^2$, $\Delta = 0$, and $M$ a cuspidal cubic with cusp $x$, locally $y^2 = x^3$. Three blow-ups give a log resolution over $x$: the first blows up the cusp, with exceptional $E_1$; the second blows up the point where the strict transform is tangent to $E_1$, with exceptional $E_2$; the third blows up the point where the strict transform, $E_1$ and $E_2$ meet, with exceptional $E_3$. The discrepancies are $a(E_1) = 1$, $a(E_2) = 2$, $a(E_3) = 4$, and the multiplicities of $f^* M$ are $2$, $3$, $6$, by Lemma 4.1.20 applied three times. With the strict transform $M'$, where $a = 0$ and $r = 1$, the ratios $(1 + a_j)/r_j$ are $1$, $1$, $5/6$ and $1$. So $c_0 = 5/6$ is attained only along $E_3$, no perturbation is needed, and $F_0 = E_3$. The pair $(X, cM)$ is klt near $x$ exactly for $c < 5/6$ by Theorem 4.2.14.

**Example 7.1.5 (a three-way tie).** Let $X = \mathbb{P}^2$, $M = L_1 + L_2$ two lines meeting at $x$, and $f \colon Y \to X$ the blow-up of $x$ with exceptional $E$. Then $a(E) = 1$ and $\operatorname{mult}_E f^* M = 2$, while the strict transforms $L'_1, L'_2$ have $a = 0$ and $r = 1$. All three ratios equal $1$, so $c_0 = 1$ is attained along $L'_1$, $L'_2$ and $E$. Take $U = f^* H$ for a line $H$ and $P_0 = \tfrac{1}{2} E$, so $U - P_0 = f^* H - \tfrac{1}{2} E$ is ample. For $P = s P_0$ with $s$ small, the threshold becomes $c(s) = \min\{1, 1, (2 - s/2)/2\} = 1 - s/4$, attained only along $E$. So here the term $s P_0$ already breaks the tie in favour of $E$, with $b_E = -1$ and $b_{L'_i} = -1 + s/4$. If instead $P_0 = 0$ and $U = f^* H$, the proof of the lemma chooses $j_0$ among the three, say $L'_1$, and replaces $c = 1$ by $c' = 1 - \varepsilon$ and $P = \varepsilon L'_1$; then $b_{L'_1} = -1$, $b_{L'_2} = -1 + \varepsilon$ and $b_E = 1 - 2(1 - \varepsilon) = -1 + 2\varepsilon$.

### Proof

*Lemma 7.1.1.* Both statements are unchanged when $D$ and $A$ are replaced by positive multiples, so assume that $D$ and $A$ are Cartier and $A$ very ample. Part 1 is proved by induction on $d - k$. If $k = d$, then $(D^d \cdot V) \ge 0$ by part 5 of Theorem P7.3.12. If $k < d$, choose a section $\sigma \in H^0(V, \mathcal{O}_V(A))$ that does not vanish at the generic point of $V$. Its divisor $H_\sigma$ is an effective Cartier divisor on $V$ with cycle $[H_\sigma] = \sum_i m_i W_i$, where the $W_i$ are subvarieties of dimension $d - 1$ and $m_i > 0$. By parts 1 and 6 of Theorem P7.1.6 and Theorem P7.1.13,
$$(D^k \cdot A^{d-k} \cdot V) = (D^k \cdot A^{d-1-k} \cdot H_\sigma) = \sum_i m_i \, (D^k \cdot A^{d-1-k} \cdot W_i),$$
and every term is nonnegative by induction.

For part 2 the proof is by induction on $d$. If $d = 1$, then $V$ is the only curve on $V$ and $D \cdot V = 0$ is the hypothesis. Let $d \ge 2$ and let $C \subseteq V$ be a curve with ideal sheaf $\mathcal{I}_C \subseteq \mathcal{O}_V$. By Theorem P4.2.1 there is $m \ge 1$ such that $\mathcal{I}_C \otimes \mathcal{O}_V(mA)$ is generated by global sections. Since $\mathcal{I}_C$ is nonzero at the generic point of $V$, some global section $\sigma$ of $\mathcal{I}_C(mA) \subseteq \mathcal{O}_V(mA)$ does not vanish there. Its divisor $H_\sigma \in |mA|$ contains $C$, and $[H_\sigma] = \sum_i m_i W_i$ as before. Then
$$0 = m \, (D \cdot A^{d-1} \cdot V) = (D \cdot A^{d-2} \cdot H_\sigma) = \sum_i m_i \, (D \cdot A^{d-2} \cdot W_i),$$
and every term is nonnegative by part 1, so every term is $0$. Since $C$ is irreducible and lies in $\bigcup_i W_i$, it lies in some $W_i$, and $D \equiv 0$ on $W_i$ by induction. So $D \cdot C = 0$.

*Lemma 7.1.2.* By Theorem 4.2.10, with a resolution that is a composite of blow-ups, and its form for ideals that underlies Definition P7.10.1, there is a projective birational morphism $f_1 \colon Y_1 \to X$ from a smooth projective variety with $\mathfrak{b} \cdot \mathcal{O}_{Y_1} = \mathcal{O}_{Y_1}(-F_1)$ for an effective divisor $F_1$ and with $\operatorname{Exc}(f_1)$ a divisor. Let $m_0 \ge 1$ with $m_0 H$ Cartier. The divisor $f_1^*(m_0 H)$ is nef and big by Lemma P7.9.2, so by part 1 of Corollary P7.5.4 there is $m \ge 1$ with $m f_1^*(m_0 H) \sim A_1 + E_1$, where $A_1$ is an ample Cartier divisor and $E_1$ is effective. Put $E'_1 = E_1 / (m m_0)$, so $f_1^* H - E'_1$ is $\mathbb{Q}$-linearly equivalent to the ample $\mathbb{Q}$-divisor $A_1 / (m m_0)$.

Apply Theorem P7.8.15 on $Y_1$ to the reduced divisor $D_1$ with support $\operatorname{Supp} F_1 \cup \operatorname{Supp} E_1 \cup \operatorname{Exc}(f_1) \cup (f_1)^{-1}_*(\operatorname{Supp} \Delta \cup \Gamma)$. It gives $\mu \colon Y \to Y_1$, a composite of blow-ups with $Y$ smooth projective, such that $\mu^{-1}_* D_1 + \operatorname{Exc}(\mu)$ is a reduced snc divisor, and an effective $\mu$-exceptional $F'$ with $\mu^*(f_1^* H - E'_1) - \delta F'$ ample for a small rational $\delta > 0$. Put $f = f_1 \circ \mu$ and $P_H = \mu^* E'_1 + \delta F'$. Then $f$ is projective and birational, $f^* H - P_H$ is ample, and $\mathfrak{b} \cdot \mathcal{O}_Y = \mathcal{O}_Y(-\mu^* F_1)$, so $F_{\mathfrak{b}} = \mu^* F_1$. The support of $\mu^*$ of any divisor supported on $D_1$ lies in $\mu^{-1}_* D_1 \cup \operatorname{Exc}(\mu)$, and so do $\operatorname{Supp} F'$, $\operatorname{Exc}(f) = \mu^{-1}(\operatorname{Exc}(f_1)) \cup \operatorname{Exc}(\mu)$ and $f^{-1}_*(\operatorname{Supp} \Delta \cup \Gamma)$. So $\operatorname{Exc}(f)$ is a divisor and part 3 holds with $\sum_j F_j = \mu^{-1}_* D_1 + \operatorname{Exc}(\mu)$. The last assertion follows: $K_Y - f^*(K_X + \Delta)$ is supported on $\operatorname{Exc}(f) \cup f^{-1}_* \operatorname{Supp} \Delta$, and $f^* N$ on $\operatorname{Exc}(f) \cup f^{-1}_* \operatorname{Supp} N$.

*Lemma 7.1.3.* For a rational $0 < s \le 1$, the divisor $U - s P_0 = (1 - s) U + s (U - P_0)$ is ample by part 3 of Theorem P7.3.12. Put
$$c(s) = \min \Bigl\{ \frac{1 + a_j - s p_j}{r_j} : r_j > 0 \Bigr\}.$$
Then $c(s) \le c_0$, and $c(s) \to c_0$ as $s \to 0$. Choose $s$ so small that $c(s) > \max(0, c_0 - \eta)$ and $a_j - s p_j > -1$ for every $j$ with $r_j = 0$. Let $J$ be the set of indices with $r_j > 0$ at which the minimum $c(s)$ is attained, and choose $j_0 \in J$. With $c = c(s)$ and $P = s P_0$, the numbers $a_j - c r_j - s p_j$ are $\ge -1$, with equality exactly for $j \in J$.

For a rational $\varepsilon > 0$ put $c' = c - \varepsilon / r_{j_0}$ and $P' = s P_0 + \varepsilon F_{j_0}$, and $b_j = a_j - c' r_j - p'_j$ with $P' = \sum_j p'_j F_j$. Then
$$b_{j_0} = a_{j_0} - c r_{j_0} - s p_{j_0} + \varepsilon - \varepsilon = -1,$$
for $j \in J \setminus \{j_0\}$, $b_j = -1 + \varepsilon r_j / r_{j_0} > -1$, and for $j \notin J$ the number $b_j$ differs from $a_j - c r_j - s p_j > -1$ by at most $\varepsilon r_j / r_{j_0}$. Since the ample cone is open (part 1 of Theorem P7.3.12) and $U - s P_0$ is ample, $U - P' = (U - s P_0) - \varepsilon F_{j_0}$ is ample for small $\varepsilon$. For $\varepsilon$ small enough all these conditions hold together with $c' > \max(0, c_0 - \eta)$, and $c'$ and $P'$ are the required $c$ and $P$.

For part 1, $b_j > -1$ gives $\lceil b_j \rceil \ge 0$ for $j \neq j_0$, and $\lceil b_{j_0} \rceil = -1$, so $\lceil B \rceil = A_Y - F_0$ with $A_Y$ as stated. Since $c > 0$, $r_j \ge 0$ and $p'_j \ge 0$, $b_j \le a_j$ and $\lceil b_j \rceil \le \lceil a_j \rceil$. For part 2, $\Theta = \sum_{j \neq j_0} (\lceil b_j \rceil - b_j) F_j$, since $b_{j_0}$ is an integer, and its coefficients lie in $[0, 1)$; so $(Y, \Theta)$ is klt by Corollary 4.2.13, applied with the identity as log resolution. For part 3, $F_0$ is smooth since $\sum_j F_j$ is snc. For $j \neq j_0$ the restriction $F_j|_{F_0}$ is a reduced divisor on $F_0$, possibly zero, the divisor $\sum_{j \neq j_0} F_j|_{F_0}$ is snc on $F_0$, and for $j \neq j'$ the restrictions $F_j|_{F_0}$ and $F_{j'}|_{F_0}$ have no common component, since $F_j \cap F_{j'} \cap F_0$ has codimension $3$ in $Y$. So restriction to $F_0$ commutes with round-up for divisors supported on $\bigcup_{j \neq j_0} F_j$, and
$$\lceil G_0 \rceil = \Bigl\lceil \sum_{j \neq j_0} b_j F_j|_{F_0} \Bigr\rceil = \sum_{j \neq j_0} \lceil b_j \rceil F_j|_{F_0} = A_Y|_{F_0},$$
because $B + F_0 = \sum_{j \neq j_0} b_j F_j$. The same reasoning gives the claim on $\Theta|_{F_0}$.

### Exercises

1. (A) In Example 7.1.4, verify the discrepancies $1, 2, 4$ and the multiplicities $2, 3, 6$ by applying Lemma 4.1.20 at each blow-up.
2. (A) Let $M = \{x^a = y^b\}$ near the origin of $\mathbb{A}^2$ with $a, b \ge 2$ coprime. Using the toric resolution, show that $c_0 = 1/a + 1/b$ when $1/a + 1/b \le 1$, and that it is attained along a single exceptional divisor.
3. (A) Show that part 2 of Lemma 7.1.1 fails when $D$ is not nef, using $D = h - 2e$ and $A = 2h - e$ on the blow-up of $\mathbb{P}^2$ at a point, with $h$ the pullback of a line and $e$ the exceptional curve.
4. (B) Show that in Lemma 7.1.3 the threshold $c_0$ cannot be replaced by a number larger than $c_0$: for $c > c_0$ and any $P \ge 0$, some coefficient of $\sum_j (a_j - c r_j - p'_j) F_j$ is less than $-1$.
5. (B) Let $D$ be a nef $\mathbb{Q}$-Cartier divisor on a projective variety $V$ of dimension $d$ and $A$ ample. Show that $D \equiv 0$ if and only if $(D \cdot A^{d-1}) = 0$, and that $(D^d) > 0$ implies $(D \cdot A^{d-1}) > 0$.
6. (C) Let $X$ be a normal projective surface with a cyclic quotient singularity of type $\frac{1}{3}(1, 1)$, with minimal resolution exceptional curve $E$, $E^2 = -3$. Compute the discrepancy $a(E, X, 0) = -1/3$, and for a curve $M$ through the singular point whose strict transform meets $E$ transversally once, compute $c_0$ for $(X, M)$ on the minimal resolution.

### Lean

The library has `MinimalModel.IsNef`, `MinimalModel.IsBig` and `MinimalModel.IsKlt`, but no log resolutions in the sense of Lemma 7.1.2 and no statement of Lemma 7.1.1 or Lemma 7.1.3.

### Notes and history

The tie-breaking device goes back to Kawamata's proof of the base point free theorem (Kaw85) and to Shokurov's nonvanishing paper (Sho85). The form of Lemma 7.1.3, with the auxiliary $P$ that keeps an ample class ample, follows the proofs of KM98, Theorems 3.3 and 3.4; KMM87, Chapter 2, has the same argument in the language of minimal models, and Lazarsfeld's account of multiplier ideals (Laz04, Chapter 9) explains the threshold $c_0$ as a jumping number. Lemma 7.1.2 combines the two forms of resolution in P7.8 and P7.10 so that the three chapters can use one resolution throughout.
