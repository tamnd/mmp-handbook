---
title: Positive characteristic, and log resolutions in the program
nodes: []
sources: [Abh56, Abh66, Lip78, CP08, CP09, dJ96, KM98, Kol07]
reads_with: [Kol07:3, CP08:0, dJ96:4, KM98:2.3]
requires: [P5.6, P5.8, P8.4, P8.5, P8.9, P8.13, 2.3, 4.1, 4.2, 4.6]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Positive characteristic, and log resolutions in the program

### Statement

Hironaka's method uses characteristic $0$ at its core, through hypersurfaces of maximal contact, which need not exist in positive characteristic. What is known in characteristic $p > 0$ is the following, and every part is cited.

**Theorem P8.5.16 (resolution in positive characteristic).** Let $k$ be a field of characteristic $p > 0$.

1. (*Curves.*) If $k$ is perfect, every integral curve over $k$ has a resolution, its normalization, by Theorem P8.4.2.
2. (*Surfaces; Abhyankar 1956, Lipman 1978.*) Every reduced surface over $k$ has a resolution by a regular scheme that is an isomorphism over the regular locus, by parts 2 and 3 of Theorem P8.4.15.
3. (*Abhyankar 1966.*) If $k$ is algebraically closed and $p > 5$, every threefold over $k$ has a resolution.
4. (*Cossart and Piltant, 2008 and 2009.*) If $[k : k^p]$ is finite, in particular if $k$ is perfect, every reduced quasi-projective scheme of dimension $3$ over $k$ has a projective birational morphism from a regular scheme that is an isomorphism over its regular locus.

In dimension at least $4$, resolution in positive characteristic is open.

Lean: not in Lean as stated.

An *alteration* of a variety $X$ is a proper surjective morphism $X' \to X$ from a variety of the same dimension, so it is generically finite. A resolution is a birational alteration.

**Theorem P8.5.17 (de Jong's alterations).** Let $X$ be a variety over an algebraically closed field of any characteristic and $Z \subsetneq X$ a closed subset. Then there are an alteration $\varphi \colon X' \to X$ and an open immersion $X' \subseteq \bar X'$ into a smooth projective variety such that $\varphi^{-1}(Z) \cup (\bar X' \setminus X')$ is an snc divisor of $\bar X'$.

Lean: not in Lean as stated.

For surfaces, Chapter 4 gives log resolutions of pairs in every characteristic, with the definitions of Volume 4.

**Proposition P8.5.18 (log resolutions of pairs on surfaces).** Let $X$ be a normal projective surface over an algebraically closed field of any characteristic and $\Delta$ an $\mathbb{R}$-divisor on $X$. Then $(X, \Delta)$ has a log resolution in the sense of Definition 4.2.9 of Volume 4, which is projective and is an isomorphism over the smooth points of $X$ at which $\operatorname{Supp} \Delta$ has simple normal crossings.

Lean: not in Lean as stated.

**Proposition P8.5.19 (log discrepancies of point blow-ups).** Let $S$ be a smooth projective surface over an algebraically closed field, $C = \sum_j c_j C^{(j)}$ a curve with prime components $C^{(j)}$, $t \geq 0$, and $\pi \colon S_n \to S$ a sequence of point blow-ups with the data $N_i$, $k_i$ of Proposition P8.4.9. Then
$$K_{S_n} + t C_n + \sum_{i=1}^n (t N_i - k_i) F_i = \pi^* (K_S + tC),$$
so in the notation of Definition 4.1.4 of Volume 4 the crepant pullback of $(S, tC)$ to $S_n$ is $t C_n + \sum_i (t N_i - k_i) F_i$, and the log discrepancy of $F_i$ is $1 + k_i - t N_i$. If $\pi$ is a log resolution of $(S, C)$ and $\operatorname{char} k = 0$, then $(S, tC)$ is log canonical if and only if $t c_j \leq 1$ for all $j$ and $t N_i \leq 1 + k_i$ for all $i$, so
$$\operatorname{lct}(S; C) = \min \Bigl\{ \min_j \frac{1}{c_j}, \ \min_i \frac{1 + k_i}{N_i} \Bigr\}.$$

Lean: not in Lean as stated.

The minimal model program uses log resolutions in four places in this handbook. First, the classes of singularities are tested on one log resolution, by Theorem 4.2.14 of Volume 4 and Proposition P8.13.6. Second, the existence of a log resolution, Theorem 4.2.10 of Volume 4, is the form in which Hironaka's theorem enters, through Proposition P8.5.10. Third, the vanishing theorems of Kawamata and Viehweg are proved on a log resolution, where the boundary has simple normal crossings and covering tricks apply. Fourth, multiplier ideals are defined as $f_* \mathcal{O}_Y(K_{Y/X} - \lfloor f^* D \rfloor)$ on a log resolution $f$, and Proposition P8.5.11 is used to make the relevant divisors relatively ample. In characteristic $p > 0$, Proposition P8.5.18 and Theorem P8.5.16 are why the program for surfaces and for threefolds with $p > 5$ can follow the same lines, while vanishing theorems fail and are replaced by other arguments.

### Proof in words

The two propositions are consequences of Chapter 4. For surfaces in any characteristic a resolution exists, so the minimal resolution exists, it is an isomorphism over the smooth locus, and the minimal log resolution of the preimage of the boundary together with the exceptional curves finishes the job. The log discrepancies on a sequence of point blow-ups follow from the two recursions of Section 4.2, and the log canonical threshold is then read off from one log resolution.

### Examples

**Example P8.5.20 (an inseparable projection).** Let $\operatorname{char} k = 2$ and $X = V(z^2 - xy) \subseteq \mathbb{A}^3$, singular only at the origin. The projection $(x, y, z) \mapsto (x, y)$ is finite of degree $2$, but $K(X) = k(x, y)(\sqrt{xy})$ is purely inseparable over $k(x, y)$, so the projection is not étale at any point, and step 2 of the proof of Theorem P8.4.17 fails. The blow-up of the origin is still a resolution with one $(-2)$-curve, since the computation of Example P3.11.15 does not use the characteristic. The projection $(x, y, z) \mapsto (x + y, z)$ is finite and separable: $x$ is a root of $T^2 + (x + y) T + z^2$, whose derivative $x + y$ is not zero.

**Example P8.5.21 (two log canonical thresholds).** Let $\operatorname{char} k = 0$. For the cusp, Example P8.4.11 gives $N = (2, 3, 6)$, $k = (1, 2, 4)$ on a log resolution, so by Proposition P8.5.19, $\operatorname{lct}(\mathbb{A}^2; V(y^2 - x^3)) = \min \{ 1, 2/2, 3/3, 5/6 \} = 5/6$, as in Example 4.6.7 of Volume 4. For the tacnode, Example P8.4.13 gives $N = (2, 4)$ and $k = (1, 2)$, so $\operatorname{lct}(\mathbb{A}^2; V(y^2 - x^4)) = \min \{ 1, 2/2, 3/4 \} = 3/4$. The numbers $N_i$ and $k_i$ in both examples are the same in every characteristic, for the tacnode outside characteristic $2$.

**Example P8.5.22 (a quotient map as an alteration).** Let $d \geq 2$ be prime to $\operatorname{char} k$ and $\mu_d$ act on $\mathbb{A}^2$ with type $\frac{1}{d}(1, q)$. The quotient map $\mathbb{A}^2 \to \mathbb{A}^2 / \mu_d$ is finite and surjective of degree $d$ from a smooth variety, so it is an alteration that is not a resolution. It is étale over the complement of the image of the origin, by Proposition P8.9.5, since the action is free away from the origin. The toric resolution of Theorem P8.8.3 is a resolution of the same singularity, so in this case the alteration is not needed; de Jong's theorem matters where no resolution is known.

### Proof

*Proposition P8.5.18.* By part 2 of Theorem P8.4.15, and by Theorem P8.4.17 in characteristic $0$, $X$ has a resolution, so by Theorem 2.3.8 of Volume 2 it has a minimal resolution $f_0 \colon Y_0 \to X$, which is an isomorphism over $X_{\mathrm{sm}}$ by Corollary P8.4.18. If $\Delta \neq 0$, Corollary P8.4.19 with $C = \operatorname{Supp} \Delta$ gives a projective resolution $f$ with $f^{-1}(C) \cup \operatorname{Exc}(f)$ snc, an isomorphism over the smooth points of $X$ where $C$ is snc. Its exceptional set is a union of curves by part 2 of Theorem P5.8.3, so a divisor, and $\operatorname{Supp} f^{-1}_* \Delta \subseteq f^{-1}(C)$, so $\operatorname{Exc}(f) \cup \operatorname{Supp} f^{-1}_* \Delta$ is a union of components of an snc curve and is snc. If $\Delta = 0$ and $X$ is smooth, the identity is a log resolution. If $\Delta = 0$ and $X$ is singular, let $\pi$ be the minimal log resolution of $(Y_0, \operatorname{Exc}(f_0))$ from Theorem P8.4.10; then $\operatorname{Exc}(f_0 \circ \pi) \subseteq \pi^{-1}(\operatorname{Exc}(f_0)) \cup \operatorname{Exc}(\pi)$ by Lemma P8.5.9, which is snc.

*Proposition P8.5.19.* By parts 1 and 2 of Proposition P8.4.9, $\pi^* C = C_n + \sum_i N_i F_i$ and $\pi^* K_S = K_{S_n} - \sum_i k_i F_i$, where $C_n$ is the strict transform of $C$ with its coefficients. Adding $t$ times the first to the second gives the displayed equality, and Definition 4.1.4 of Volume 4 gives the crepant pullback. Its coefficients are $t c_j$ on the strict transform of $C^{(j)}$ and $t N_i - k_i$ on $F_i$. If $\pi$ is a log resolution, part 1 of Theorem 4.2.14 of Volume 4 says that $(S, tC)$ is log canonical if and only if all these coefficients are at most $1$, which is the stated condition; the threshold is the largest such $t$.

### Exercises

1. (A) Use Proposition P8.5.19 and Example P8.4.14 to show that the log canonical threshold of $m \geq 2$ lines through a point of $\mathbb{A}^2$ with distinct directions is $2/m$.
2. (A) Use Exercise 3 of Section 4.2 to compute the log canonical threshold of $y^a = x^b$, for $a, b \geq 2$ coprime, as $\min \{ 1, 1/a + 1/b \}$.
3. (B) In Example P8.5.20, show that the projection $(x, y, z) \mapsto (x + y, z)$ is finite, and find its branch curve.
4. (B) Show that the quotient map of Example P8.5.22 is an alteration of degree $d$, and describe its fibres over the image of the origin and over the images of the coordinate axes.
5. (B) For a reduced curve $C$ on a smooth surface in characteristic $0$, show that $(S, tC)$ is klt for $0 \leq t < \operatorname{lct}(S; C)$ and not log canonical for $t > \operatorname{lct}(S; C)$.
6. (C) Let $C$ be a reduced curve with a point of multiplicity $m \geq 2$. Using only the first blow-up, with $N_1 = m$ and $k_1 = 1$, show that the log canonical threshold of $C$ at that point is at most $2/m$, even when one blow-up is not a log resolution.

### Lean

The repository defines the singularities of the program without resolutions. In `MinimalModel/Statements/Basic.lean`, `MinimalModel.IsDivisorial` says that a valuation of the function field is a normalized divisorial valuation, `MinimalModel.IsCentre` says that a point is its centre, and `MinimalModel.IsExceptional` says that the centre is not a prime divisor. The predicate `MinimalModel.LogDiscrepancyIs` computes the log discrepancy $A = 1 + \operatorname{ord}_v(\omega) - \sum r_i \operatorname{ord}_v(h_i)$ from local equations $h_i$ of $K + \Delta$ near the centre, with `MinimalModel.FormOrd` for the order of the canonical form, so no model on which $v$ is a divisor is chosen. Then `MinimalModel.IsKlt`, `MinimalModel.IsLc`, `MinimalModel.IsTerminal` and `MinimalModel.IsCanonical` quantify over all divisorial valuations, or all exceptional ones, as in Definition 4.2.1 of Volume 4. These definitions need no resolution: the statement that one log resolution decides, Theorem 4.2.14 of Volume 4, would be a theorem relating them to `MinimalModel.HasLogResolution` of Section 5.1, and it is not formalized. On `origin/main`, `MinimalModel.HasLogResolution` is defined and no other declaration uses it; its docstring records it as a shared hypothesis. For generalized pairs, `MinimalModel.logDiscrepancyOfIs_iff` in `MinimalModel/Fidelity/GeneralizedPairs.lean` states that the log discrepancy of a generalized pair with no moduli part is `MinimalModel.LogDiscrepancyIs`, and it holds by definition. The theorems of this section are not in Lean.

### Notes and history

Abhyankar proved resolution of surfaces in positive characteristic in 1956, and of threefolds in characteristic greater than $5$ in his book of 1966. Lipman's theorem of 1978 removed the field, covering excellent two-dimensional schemes. Cossart and Piltant proved resolution of threefolds in every positive characteristic in two papers of 2008 and 2009, and extended it to arithmetic threefolds in 2019. De Jong's alterations of 1996 replace resolution by a generically finite map; Gabber and Temkin later refined them to alterations of degree prime to a given prime. The minimal model program for threefolds in characteristic $p > 5$, due to Hacon and Xu, Birkar, and others, uses the threefold resolution of Cossart and Piltant at the same places where the characteristic $0$ program uses Hironaka.
