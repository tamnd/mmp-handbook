---
title: Stable, augmented and restricted base loci
nodes: []
sources: [Laz04, ELMNP06, Nkm00]
reads_with: [Laz04:2.1.A, Laz04:10.3, ELMNP06:1]
requires: [P3.6, P3.10, P5.10, P7.1, P7.2, P7.3, P7.4, P7.5, P7.6]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Stable, augmented and restricted base loci

### Statement

Throughout, $X$ is a projective variety over $k$ of dimension $n \geq 1$, $\mathbb{Q}$-divisors are as in Section 7.1, and base loci are closed subsets of $X$ with the reduced structure. For a Cartier divisor $D$, $\operatorname{Bs}|D|$ is the base locus of $\Gamma(X, \mathcal{O}_X(D))$ (part 2 of Definition P3.10.1); it is $X$ when $\Gamma(X, \mathcal{O}_X(D)) = 0$. An ample $\mathbb{Q}$-divisor is a $\mathbb{Q}$-divisor with ample class; by part 2 of Theorem P7.3.12 some multiple is then an ample Cartier divisor.

**Definition P7.7.12 (stable base locus).** The *stable base locus* of a $\mathbb{Q}$-divisor $D$ is
$$\mathbf{B}(D) = \bigcap_{m} \operatorname{Bs}|mD|,$$
the intersection over the integers $m \geq 1$ such that $mD$ is a Cartier divisor. For a Cartier divisor it is the stable base locus of part 4 of Definition P3.10.1.

The integers $m \geq 1$ with $mD$ Cartier are the positive multiples of one $m_0$, so $\mathbf{B}(D) = \mathbf{B}(m_0 D)$, and by part 4 of Proposition P3.10.2, $\mathbf{B}(D) = \operatorname{Bs}|mD|$ for every sufficiently divisible $m$. Hence $\mathbf{B}(cD) = \mathbf{B}(D)$ for rational $c > 0$, and $\mathbf{B}(D)$ depends only on the $\mathbb{Q}$-linear equivalence class of $D$.

**Lemma P7.7.13 (sums).** Let $D$, $D'$ be $\mathbb{Q}$-divisors.

1. $\mathbf{B}(D + D') \subseteq \mathbf{B}(D) \cup \mathbf{B}(D')$.
2. If $A$ is an ample $\mathbb{Q}$-divisor, $\mathbf{B}(D + A) \subseteq \mathbf{B}(D)$.
3. If $G$ is an effective $\mathbb{Q}$-divisor, $\mathbf{B}(D + G) \subseteq \mathbf{B}(D) \cup \operatorname{Supp} G$.

Lean: not in Lean as stated.

**Definition P7.7.14 (augmented and restricted base loci).** Let $D$ be a $\mathbb{Q}$-divisor. The *augmented base locus* and the *restricted base locus* of $D$ are
$$\mathbf{B}_+(D) = \bigcap_A \mathbf{B}(D - A), \qquad \mathbf{B}_-(D) = \bigcup_A \mathbf{B}(D + A),$$
over all ample $\mathbb{Q}$-divisors $A$.

**Proposition P7.7.15 (properties).** Let $D$ be a $\mathbb{Q}$-divisor and $A_0$ an ample $\mathbb{Q}$-divisor.

1. $\mathbf{B}_-(D) \subseteq \mathbf{B}(D) \subseteq \mathbf{B}_+(D)$.
2. There is $\varepsilon_0 > 0$ with $\mathbf{B}_+(D) = \mathbf{B}(D - \varepsilon A_0)$ for every rational $0 < \varepsilon < \varepsilon_0$. In particular $\mathbf{B}_+(D)$ is closed.
3. $\mathbf{B}_-(D) = \bigcup_{\varepsilon} \mathbf{B}(D + \varepsilon A_0)$, over rational $\varepsilon > 0$, an increasing union as $\varepsilon$ decreases.
4. If $D' \equiv D$, then $\mathbf{B}_+(D') = \mathbf{B}_+(D)$ and $\mathbf{B}_-(D') = \mathbf{B}_-(D)$. So $\mathbf{B}_+$ and $\mathbf{B}_-$ are defined on $N^1(X)_\mathbb{Q}$.
5. $\mathbf{B}_+(D) = \emptyset$ if and only if $D$ is ample.
6. $\mathbf{B}_+(D) \neq X$ if and only if $D$ is big.
7. $\mathbf{B}_-(D) = \emptyset$ if and only if $D$ is nef.
8. $D$ is pseudo-effective if and only if $\mathbf{B}(D + A) \neq X$ for every ample $\mathbb{Q}$-divisor $A$. If $D$ is not pseudo-effective, $\mathbf{B}_-(D) = X$.

Lean: not in Lean as stated.

**Definition P7.7.16 (null locus).** Let $\xi \in N^1(X)$ be nef. The *null locus* $\operatorname{Null}(\xi)$ is the union of the subvarieties $V \subseteq X$ of positive dimension with $(\xi^{\dim V} \cdot V) = 0$. For a nef $\mathbb{Q}$-divisor $D$, $\operatorname{Null}(D) = \operatorname{Null}([D])$.

By part 5 of Theorem P7.3.12, $(\xi^{\dim V} \cdot V) \geq 0$ for every subvariety, so the null locus collects the subvarieties on which $\xi$ is as small as a nef class can be. By Theorem P7.7.7, $\operatorname{Null}(\xi) = X$ if and only if $\xi$ is not big.

**Proposition P7.7.17 (the null locus is augmented).** Let $D$ be a nef $\mathbb{Q}$-divisor. Then $\operatorname{Null}(D) \subseteq \mathbf{B}_+(D)$. More precisely, if $V \subseteq X$ is a subvariety of positive dimension not contained in $\mathbf{B}_+(D)$, then $D|_V$ is big on $V$ and $(D^{\dim V} \cdot V) > 0$.

Lean: not in Lean as stated.

**Theorem P7.7.18 (Nakamaye's theorem).** Let $k$ have characteristic $0$, let $X$ be a smooth projective variety, and let $D$ be a nef and big $\mathbb{Q}$-divisor on $X$. Then
$$\mathbf{B}_+(D) = \operatorname{Null}(D).$$

Lean: not in Lean as stated.

### Proof in words

The stable base locus is the part of $X$ that every member of every multiple of $|D|$ passes through. It is not a numerical invariant, because a numerically trivial twist can destroy all sections. Perturbing by a small ample class removes this defect: subtracting an ample class can only enlarge the base locus, and by Noetherian induction the intersection over all ample perturbations is reached by one small multiple of a fixed ample divisor. Since a numerically trivial divisor plus a small ample divisor is ample, the perturbed loci only see numerical classes. The augmented base locus is empty exactly for ample classes, and it is the whole space exactly for classes that are not big; the restricted base locus is empty exactly for nef classes.

For a nef divisor, a subvariety not contained in the augmented base locus carries a member of a multiple of $D - \varepsilon A$ that does not contain it, so $D$ restricted to the subvariety is ample plus effective, hence big, and its top self-intersection there is positive. Nakamaye's theorem, which is stated, gives the converse in characteristic $0$.

### Examples

**Example P7.7.19 (the stable base locus is not numerical).** Let $C$ be a smooth projective curve of genus $g \geq 1$ and $\eta$ a line bundle of degree $0$ and infinite order, which exists when $k$ is not the algebraic closure of a finite field. Then $\eta \equiv \mathcal{O}_C$, while $H^0(C, \eta^m) = 0$ for all $m \geq 1$ gives $\mathbf{B}(\eta) = C$ and $\mathbf{B}(\mathcal{O}_C) = \emptyset$. The two classes are equal in $N^1(C)$, and $\mathbf{B}_-(\eta) = \mathbf{B}_-(\mathcal{O}_C) = \emptyset$ since both are nef, while $\mathbf{B}_+(\eta) = \mathbf{B}_+(\mathcal{O}_C) = C$ since neither is big. On $X = \mathbb{P}^1 \times C$ the divisors $p_1^* \mathcal{O}(1)$ and $p_1^* \mathcal{O}(1) \otimes p_2^* \eta$ have the same class, base loci $\emptyset$ and $X$, and $\mathbf{B}_- = \emptyset$, $\mathbf{B}_+ = X$.

**Example P7.7.20 (three different loci).** Let $X = X_9$ be the blow-up of $\mathbb{P}^2$ at nine points on a smooth cubic $C$ with $\sum P_i = R$ of infinite order, as in Example P5.10.26 and Example P7.6.9, and $\tilde C$ the strict transform of $C$. There $-K_X$ is nef with $(-K_X)^2 = 0$ and $|-mK_X| = \{ m \tilde C \}$ for all $m \geq 1$. So
$$\mathbf{B}_-(-K_X) = \emptyset \subsetneq \mathbf{B}(-K_X) = \tilde C \subsetneq \mathbf{B}_+(-K_X) = X,$$
the first by part 7 of Proposition P7.7.15, the last by part 6 and Theorem P7.7.7, since $-K_X$ is nef with $(-K_X)^2 = 0$. Here $\operatorname{Null}(-K_X) = X$, as the subvariety $V = X$ already has $((-K_X)^2 \cdot X) = 0$.

**Example P7.7.21 (a big and nef divisor on a blow-up).** Let $X = \operatorname{Bl}_p \mathbb{P}^n$, $n \geq 2$, with $H$ and $E$ as in Example P7.7.11, and $A_0 = 2H - E$, which is ample by Proposition P7.4.18. Then $\mathbf{B}(H) = \emptyset$, since $|H|$ is the pullback of the base point free system of hyperplanes. For rational $0 < \varepsilon < \frac12$,
$$H - \varepsilon A_0 = (1 - 2\varepsilon) H + \varepsilon E,$$
and for integers $x \geq 1$, $c \geq 1$, Example P7.7.11 shows that every section of $\mathcal{O}_X(xH + cE)$ is $s_E^c \, \pi^* t$ with $t \in H^0(\mathbb{P}^n, \mathcal{O}(x))$. These sections all vanish on $E$ and have no common zero off $E$, so $\operatorname{Bs}|xH + cE| = E$, and by part 2 of Proposition P7.7.15, $\mathbf{B}_+(H) = E$. On the other side, $E$ has dimension $n - 1 \geq 1$ and $(H^{n-1} \cdot E) = 0$ by part 3 of Proposition P7.1.23, so $E \subseteq \operatorname{Null}(H)$, and Proposition P7.7.17 gives $\operatorname{Null}(H) = \mathbf{B}_+(H) = E$, as Nakamaye's theorem predicts. For the nef class $H - E$, which is not big, $\mathbf{B}(H - E) = \emptyset$ because $H - E$ is the pullback of $\mathcal{O}(1)$ by the projection from $p$, and $\mathbf{B}_+(H - E) = \operatorname{Null}(H - E) = X$.

### Proof

*Lemma P7.7.13.* Part 1. Choose $m$ so divisible that $mD$ and $mD'$ are Cartier, $\mathbf{B}(D) = \operatorname{Bs}|mD|$ and $\mathbf{B}(D') = \operatorname{Bs}|mD'|$. The products of sections of $\mathcal{O}_X(mD)$ and $\mathcal{O}_X(mD')$ span a subspace of $\Gamma(X, \mathcal{O}_X(m(D + D')))$, so by parts 2 and 3 of Proposition P3.10.2,
$$\mathbf{B}(D + D') \subseteq \operatorname{Bs}|m(D + D')| \subseteq \operatorname{Bs}|mD| \cup \operatorname{Bs}|mD'| = \mathbf{B}(D) \cup \mathbf{B}(D').$$
Part 2. Some multiple $aA$ is an ample Cartier divisor, and by part 2 of Definition P3.6.22 some further multiple is generated by global sections, so $\mathbf{B}(A) = \emptyset$; apply part 1. Part 3. If $aG$ is an effective Cartier divisor, its canonical section does not vanish off $\operatorname{Supp} G$, so $\mathbf{B}(G) \subseteq \operatorname{Supp} G$; apply part 1.

*Proposition P7.7.15.* First, monotonicity in $A$: if $A$ and $A'$ are ample $\mathbb{Q}$-divisors with $A' - A$ ample, then by part 2 of Lemma P7.7.13
$$\mathbf{B}(D - A) \subseteq \mathbf{B}(D - A'), \qquad \mathbf{B}(D + A') \subseteq \mathbf{B}(D + A). \tag{*}$$
For an ample $\mathbb{Q}$-divisor $A$, the class of $A - \varepsilon A_0$ is ample for small rational $\varepsilon > 0$ because $\operatorname{Amp}(X)$ is open (part 1 of Theorem P7.3.12), so $A - \varepsilon A_0$ is an ample $\mathbb{Q}$-divisor.

Part 1. By part 2 of Lemma P7.7.13, $\mathbf{B}(D + A) \subseteq \mathbf{B}(D)$ and $\mathbf{B}(D) = \mathbf{B}((D - A) + A) \subseteq \mathbf{B}(D - A)$ for every ample $A$.

Part 2. The space $X$ is Noetherian, so the intersection of the closed sets $\mathbf{B}(D - A)$ equals a finite intersection $\mathbf{B}(D - A_1) \cap \dots \cap \mathbf{B}(D - A_r)$. Choose $\varepsilon_0 > 0$ with $A_i - \varepsilon A_0$ ample for all $i$ and all rational $0 < \varepsilon < \varepsilon_0$. By (*), $\mathbf{B}(D - \varepsilon A_0) \subseteq \mathbf{B}(D - A_i)$ for each $i$, so $\mathbf{B}(D - \varepsilon A_0) \subseteq \mathbf{B}_+(D) \subseteq \mathbf{B}(D - \varepsilon A_0)$.

Part 3. Every $\mathbf{B}(D + \varepsilon A_0)$ is a term of the union defining $\mathbf{B}_-(D)$. Conversely, for an ample $A$ choose $\varepsilon$ with $A - \varepsilon A_0$ ample; by (*), $\mathbf{B}(D + A) \subseteq \mathbf{B}(D + \varepsilon A_0)$. The union increases as $\varepsilon$ decreases by (*).

Part 4. Let $N = D' - D$, a numerically trivial $\mathbb{Q}$-divisor, and $A$ ample. Then $\frac12 A + N$ and $\frac12 A - N$ have the class of $\frac12 A$, so they are ample. Since $D - \frac12 A = (D' - A) + (\frac12 A - N)$, part 2 of Lemma P7.7.13 gives $\mathbf{B}_+(D) \subseteq \mathbf{B}(D - \frac12 A) \subseteq \mathbf{B}(D' - A)$; intersecting over $A$ gives $\mathbf{B}_+(D) \subseteq \mathbf{B}_+(D')$, and the reverse inclusion holds by symmetry. Similarly $D' + A = (D + \frac12 A) + (\frac12 A + N)$ gives $\mathbf{B}(D' + A) \subseteq \mathbf{B}(D + \frac12 A) \subseteq \mathbf{B}_-(D)$, so $\mathbf{B}_-(D') \subseteq \mathbf{B}_-(D)$, and symmetry gives equality.

Part 5. If $D$ is ample, so is $D - \varepsilon A_0$ for small $\varepsilon$, and $\mathbf{B}(D - \varepsilon A_0) = \emptyset$ by part 2 of Lemma P7.7.13 applied with $D = 0$. Conversely, if $\mathbf{B}_+(D) = \emptyset$, part 2 gives $\varepsilon$ and $m$ with $\operatorname{Bs}|m(D - \varepsilon A_0)| = \emptyset$, so $\mathcal{O}_X(m(D - \varepsilon A_0))$ is generated by global sections and nef by part 1 of Proposition P7.3.9. Then the class of $D = (D - \varepsilon A_0) + \varepsilon A_0$ is ample by part 3 of Theorem P7.3.12.

Part 6. If $D$ is big, $D - \varepsilon A_0$ is big for small $\varepsilon$, since $\operatorname{Big}(X)$ is open, so by part 2 of Proposition P7.5.6 some multiple is a big Cartier divisor with a nonzero section, and $\mathbf{B}(D - \varepsilon A_0) \neq X$. Conversely, if $\mathbf{B}(D - \varepsilon A_0) \neq X$, some $m(D - \varepsilon A_0)$ is linearly equivalent to an effective Cartier divisor $G$, so $[D] = \varepsilon [A_0] + \frac1m [G]$ is an ample class plus an effective class, which lies in $\operatorname{Big}(X)$ by part 1 of Proposition P7.5.6, since ample classes are big, and $D$ is big by part 2 of Proposition P7.5.6.

Part 7. If $D$ is nef, $D + A$ is ample for every ample $A$ by part 3 of Theorem P7.3.12, so $\mathbf{B}(D + A) = \emptyset$ and $\mathbf{B}_-(D) = \emptyset$. If $D$ is not nef, there is a curve $C$ with $D \cdot C < 0$, and $(D + \varepsilon A_0) \cdot C < 0$ for small $\varepsilon$. For $m$ with $m(D + \varepsilon A_0)$ Cartier, every member of $|m(D + \varepsilon A_0)|$ contains $C$ by Lemma P7.4.14, so $C \subseteq \mathbf{B}(D + \varepsilon A_0) \subseteq \mathbf{B}_-(D)$.

Part 8. If $D$ is pseudo-effective and $A$ is ample, $D + A$ is big by part 3 of Theorem P7.5.12, so $\mathbf{B}(D + A) \subseteq \mathbf{B}_+(D + A) \neq X$ by parts 1 and 6. Conversely, if $\mathbf{B}(D + \varepsilon A_0) \neq X$ for all $\varepsilon$, some multiple of $D + \varepsilon A_0$ has a nonzero section, so $[D] + \varepsilon [A_0] \in \operatorname{Eff}(X)$, and letting $\varepsilon \to 0$ gives $[D] \in \overline{\operatorname{Eff}}(X)$. If $D$ is not pseudo-effective, neither is $D + \varepsilon A_0$ for small $\varepsilon$, since the complement of $\overline{\operatorname{Eff}}(X)$ is open, so no multiple of $D + \varepsilon A_0$ has a section and $\mathbf{B}(D + \varepsilon A_0) = X$.

*Proposition P7.7.17.* Let $V$ be a subvariety of dimension $d \geq 1$ with $V \not\subseteq \mathbf{B}_+(D)$. By part 2 of Proposition P7.7.15 there are an ample $\mathbb{Q}$-divisor $A$ and $m \geq 1$ with $mA$ and $m(D - A)$ Cartier and $V \not\subseteq \operatorname{Bs}|m(D - A)|$, so some $G \in |m(D - A)|$ does not contain $V$. Since $V$ is integral, the local equations of $G$ are nonzerodivisors on $\mathcal{O}_V$, and $G|_V$ is an effective Cartier divisor on $V$. So $m D|_V$ is linearly equivalent to $mA|_V + G|_V$, where $A|_V$ is ample on $V$ by Corollary P7.3.3. Ample classes are big, so $[D|_V] \in \operatorname{Big}(V) + \operatorname{Eff}(V) \subseteq \operatorname{Big}(V)$ by part 1 of Proposition P7.5.6. The class $D|_V$ is nef by part 3 of Proposition P7.3.9, so Theorem P7.7.7 and part 4 of Theorem P7.7.6 on $V$ give $((D|_V)^d) > 0$, and $((D|_V)^d) = (D^d \cdot V)$ by part 7 of Theorem P7.1.6. Hence every subvariety $V$ of positive dimension with $(D^{\dim V} \cdot V) = 0$ lies in $\mathbf{B}_+(D)$, and $\operatorname{Null}(D) \subseteq \mathbf{B}_+(D)$.

*Theorem P7.7.18.* This is Nakamaye's theorem (Nkm00), not proved here; Lazarsfeld, Theorem 10.3.5 (Laz04), gives the proof, and Ein, Lazarsfeld, Mustaţă, Nakamaye and Popa (ELMNP06) extend it to $\mathbb{R}$-divisors. The inclusion $\operatorname{Null}(D) \subseteq \mathbf{B}_+(D)$ is Proposition P7.7.17. The converse is the substance of the theorem: for a point outside the null locus one produces, by vanishing theorems and a multiplicity estimate, sections of $m(D - \varepsilon A)$ that do not vanish there.

### Exercises

1. (A) Compute $\mathbf{B}$, $\mathbf{B}_-$ and $\mathbf{B}_+$ for every $\mathbb{Q}$-divisor on $\mathbb{P}^n$, and for every $\mathbb{Q}$-divisor of nonzero degree on a smooth projective curve.
2. (A) On $\operatorname{Bl}_p \mathbb{P}^n$, $n \geq 3$, compute $\mathbf{B}$, $\mathbf{B}_-$ and $\mathbf{B}_+$ for every class $xH - yE$ with $x, y$ rational. Show in particular that $\mathbf{B}_-(bE) = \mathbf{B}(bE) = E$ and $\mathbf{B}_+(bE) = X$ for $b > 0$. The case $n = 2$ is Example P7.7.26.
3. (B) Show that $\mathbf{B}_+(D_1 + D_2) \subseteq \mathbf{B}_+(D_1) \cup \mathbf{B}_+(D_2)$ and $\mathbf{B}_-(D_1 + D_2) \subseteq \mathbf{B}_-(D_1) \cup \mathbf{B}_-(D_2)$.
4. (B) Show that $\mathbf{B}_+(D)$ is the intersection of the supports $\operatorname{Supp} E$ over all $\mathbb{Q}$-linear equivalences $D \sim_\mathbb{Q} A + E$ with $A$ an ample and $E$ an effective $\mathbb{Q}$-divisor.
5. (B) In the situation of Proposition P7.7.17, write $mD = G + mA$ and show by cutting with $G$ and expanding that $(D^j \cdot A^{d - j} \cdot V) \geq (D^{j-1} \cdot A^{d - j + 1} \cdot V)$ for $1 \leq j \leq d$, using that mixed intersection numbers of nef classes on subvarieties are nonnegative. Deduce $(D^d \cdot V) \geq (A^d \cdot V) > 0$, a second proof of the proposition.
6. (C) Let $D$ be a nef and big $\mathbb{Q}$-divisor on a smooth projective surface $S$. Show without Theorem P7.7.18 that $\mathbf{B}_+(D)$ is the union of the curves $C$ with $D \cdot C = 0$. (These curves form a negative definite configuration by the Hodge index theorem; perturb $D$ by $\varepsilon A - \delta \sum_i C_i$ for suitable small $\delta$ and use Lemma P5.8.23.)

### Lean

The project library defines `MinimalModel.IsNef`, `MinimalModel.IsBig`, `MinimalModel.IsSemiample` and `MinimalModel.IsPseudoEffective` for $\mathbb{R}$-divisors. It has no base loci of linear systems, no stable, augmented or restricted base locus and no null locus, so the results of this section are not stated there, and Nakamaye's theorem is not recorded as a hypothesis. Mathlib has no base loci of line bundles on schemes. The handbook adds no `MinimalModel` node here.

### Notes and history

The augmented base locus was introduced by Nakamaye (Nkm00), who proved Theorem P7.7.18 for nef and big $\mathbb{Q}$-divisors on smooth complex projective varieties. The restricted base locus and the systematic comparison of the three loci are due to Ein, Lazarsfeld, Mustaţă, Nakamaye and Popa (ELMNP06), who also show that $\mathbf{B}_-(D)$ is the set of points where some asymptotic order of vanishing of $D$ is positive, and that it can fail to be closed. Lazarsfeld, Section 10.3 (Laz04), presents Nakamaye's theorem as here. The literature state is theorem. Propositions P7.7.15 and P7.7.17 hold over any algebraically closed field; Nakamaye's theorem in positive characteristic was proved for semiample divisors by Cascini, McKernan and Mustaţă, and in general, for nef $\mathbb{R}$-divisors on projective schemes over any field, by Birkar. In the minimal model program the augmented base locus of a big divisor bounds the locus where a run of the program with scaling can modify the variety.
