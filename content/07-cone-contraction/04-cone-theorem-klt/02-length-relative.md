---
title: Kawamata's length bound and the relative cone theorem
nodes: [MMHTX4Z2B7]
sources: [Kaw91, KM98, Mat02]
reads_with: [KM98:3.7, KM98:3.25, Mat02:ch8]
requires: [P7.3, P7.4, 5.1, 6.1, 6.2]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Kawamata's length bound and the relative cone theorem

### Statement

Keep the notation of Section 1: $(X, \Delta)$ is a projective klt pair of dimension $d$ over $k$ of characteristic $0$, $\Delta$ is a $\mathbb{Q}$-divisor, $a (K_X + \Delta)$ is Cartier, and $K_\Delta$ is the class of $K_X + \Delta$. Section 1 found the $K_\Delta$-negative extremal rays as exposed faces, with no curves in sight. This section puts curves in them, first any curve, by the base point free theorem of Chapter 2, then rational curves of bounded degree, by Kawamata's theorem. The contraction of a ray, used in the statement of Theorem 7.4.13, is constructed in Theorem 7.5.2 of the next chapter from Section 1 and the base point free theorem alone, so there is no circularity.

**Corollary 7.4.12 (extremal faces contain curves).** Let $F$ be a $K_\Delta$-negative extremal face. There is an integral curve $C \subseteq X$ with $[C] \in F \setminus \{0\}$. In particular every $K_\Delta$-negative extremal ray is spanned by the class of an integral curve.

Lean: not yet in Lean.

**Theorem 7.4.13 (Kawamata's length bound, cited).** Let $R$ be a $K_\Delta$-negative extremal ray and $\varphi \colon X \to Y$ its contraction (Theorem 7.5.2). Let $E$ be an irreducible component of the exceptional locus of $\varphi$, with $E = X$ if $\varphi$ is not birational, and $e = \dim E - \dim \varphi(E)$. Then $E$ is covered by rational curves $\Gamma$ contracted by $\varphi$ with
$$0 < -K_\Delta \cdot \Gamma \le 2 e.$$
In particular $R$ is spanned by the class of a rational curve $\Gamma$ with $0 < -K_\Delta \cdot \Gamma \le 2d$.

Lean: `MinimalModel.LengthOfExtremalRays`, in the project library, is the last sentence, as a statement without proof.

**Corollary 7.4.14 (the cone theorem with rational curves).** There are countably many rational curves $\Gamma_j \subseteq X$ with $0 < -K_\Delta \cdot \Gamma_j \le 2d$ such that
$$\overline{NE}(X) = \overline{NE}(X)_{K_\Delta \ge 0} + \sum_j \mathbb{R}_{\ge 0} [\Gamma_j],$$
each $\mathbb{R}_{\ge 0} [\Gamma_j]$ is a $K_\Delta$-negative extremal ray, and for every ample $H$ and $\varepsilon > 0$ only finitely many $\Gamma_j$ are $(K_\Delta + \varepsilon H)$-negative.

Lean: `MinimalModel.ConeTheoremKlt` and `MinimalModel.LengthOfExtremalRays` together state this corollary without proof.

For a morphism $f \colon X \to S$ of projective varieties the *relative cone* is the face of $f$,
$$\overline{NE}(X/S) = F_f = \{ z \in \overline{NE}(X) : f_* z = 0 \} = \overline{NE}(X) \cap (f^* A)^\perp$$
for any ample $A$ on $S$ (Definition P7.4.10 and Proposition P7.4.11). A curve $C$ is contracted by $f$ if and only if $[C] \in \overline{NE}(X/S)$.

**Proposition 7.4.15 (the relative cone theorem).** Let $f \colon X \to S$ be a morphism to a projective variety and $H$ an ample class on $X$.

1. $\overline{NE}(X/S) = \overline{NE}(X/S)_{K_\Delta \ge 0} + \sum_j R_j$, where the $R_j$ are the $K_\Delta$-negative extremal rays of $\overline{NE}(X)$ contained in $\overline{NE}(X/S)$; they are exactly the $K_\Delta$-negative extremal rays of $\overline{NE}(X/S)$.
2. For every $\varepsilon > 0$ only finitely many $R_j$ are $(K_\Delta + \varepsilon H)$-negative, and $\overline{NE}(X/S) = \overline{NE}(X/S)_{K_\Delta + \varepsilon H \ge 0} + \sum_{(K_\Delta + \varepsilon H) \cdot R_j < 0} R_j$.
3. Each $R_j$ is spanned by a rational curve $\Gamma_j$ contracted by $f$, with $0 < -K_\Delta \cdot \Gamma_j \le 2d$.
4. Every $K_\Delta$-negative extremal face of $\overline{NE}(X/S)$ is a $K_\Delta$-negative extremal face of $\overline{NE}(X)$.

Lean: not yet in Lean.

When $S$ is only quasi-projective and $f$ is projective, the same statements hold for the cone spanned by the curves contracted by $f$, by the relative forms of the rationality and base point free theorems (KM98, Theorem 3.25); they are not needed in this volume.

### Proof in words

Corollary 7.4.12 is the base point free theorem applied to a supporting divisor $L$ of the face: a multiple of $L$ defines a morphism, which cannot be finite since $L$ is not ample, so it contracts a curve, and the class of that curve lies in the face cut out by $L$. Kawamata's theorem is harder, and it is cited. Its proof takes a general fibre $G$ of $E \to \varphi(E)$, of dimension $e$, and a resolution $G' \to G$. The relative Kawamata-Viehweg vanishing of Theorem 5.1.13, applied to multiples of a $\varphi$-ample divisor, controls the sections of the restrictions of these multiples to $G$, and Riemann-Roch on $G'$ turns this control into the inequality that the canonical divisor of $G'$ is at least as negative as the pullback of $K_X + \Delta$ on suitable curves of $G'$. The bend-and-break degree bound of Theorem 6.1.2, part 4, applied on the smooth variety $G'$ with the pullback of $-(K_X + \Delta)$ as the polarization, then produces rational curves of degree at most $2e$. The relative cone theorem is a formal consequence of the absolute one, since the relative cone is a face.

### Examples

**Example 7.4.16 (projective space).** For $X = \mathbb{P}^d$ and $\Delta = 0$ the cone is the ray of a line $\ell$ with $-K_X \cdot \ell = d + 1$. Kawamata's bound $2d$ is attained only for $d = 1$; for $d \ge 2$ it is weaker than Mori's bound $d + 1$ of Corollary 6.2.10, which is attained. For $\Delta = c H_0$ with $H_0$ a hyperplane and $0 \le c < 1$ rational, $(X, \Delta)$ is klt by Corollary 4.2.13, and $-K_\Delta \cdot \ell = d + 1 - c$. The length of a ray of a pair need not be an integer.

**Example 7.4.17 (a curve in the ray, by the base point free theorem).** Let $X = \mathbb{P}^1 \times \mathbb{P}^2$ as in Example 7.4.10, with the ray $R = \mathbb{R}_{\ge 0} [f]$ cut out by $L = h_1$. Here $L - K_X = 3 h_1 + 3 h_2$ is ample, $|L|$ is already free, and the morphism it defines is $p_1 \colon X \to \mathbb{P}^1$, which contracts exactly the curves in the fibres $\{ t \} \times \mathbb{P}^2$, the curves with class in $R$. A line $f$ in a fibre is a rational curve with $-K_X \cdot f = 3 \le 2e = 4$, where $E = X$ and $e = 3 - 1 = 2$, as in Theorem 7.4.13. A conic in a fibre has degree $6$, more than $2e$: the theorem asserts that some curves of bounded degree cover $E$, not that all do.

**Example 7.4.18 (the relative cone of a projection).** Let $X = \mathbb{P}^1 \times \mathbb{P}^2$ and $f = p_2 \colon X \to S = \mathbb{P}^2$. Then $\overline{NE}(X/S) = \overline{NE}(X) \cap h_2^\perp = \mathbb{R}_{\ge 0} [g]$, the ray of a fibre $g = \mathbb{P}^1 \times \{ s \}$, with $-K_X \cdot g = 2$. Proposition 7.4.15 gives the single relative ray $R_1 = \mathbb{R}_{\ge 0} [g]$, and the ray of $f$, though $K_X$-negative, is not relative. Over $S = \mathbb{P}^1$ with $f = p_1$ the roles are exchanged, and over $S = \operatorname{Spec} k$ the relative cone is the whole cone.

### Proof

*Corollary 7.4.12.* By Corollary 7.4.7 there is $L \in \mathcal{L}$ with $F_L = F$ and $L - K_\Delta$ ample. The base point free theorem of Chapter 2, with $b = 1$, makes $|m L|$ free for some $m \ge 1$; let $\psi \colon X \to \mathbb{P}^N$ be the morphism it defines, so $\psi^* \mathcal{O}(1) \cong \mathcal{O}_X(m L)$. If $\psi$ contracted no curve, it would be finite by part 4 of Proposition P7.4.11, and $m L$ would be ample by Corollary P7.3.3, against $F_L \ne \{0\}$. So $\psi$ contracts an integral curve $C$, and by part 6 of Proposition P7.4.11, $L \cdot C = 0$, that is $[C] \in F_L = F$. If $F$ is a ray, $[C] \ne 0$ spans it, since $H \cdot C > 0$ for an ample $H$.

*Theorem 7.4.13.* This is Kawamata's theorem (Kaw91, Theorem 1), proved there for weakly log terminal pairs, a class containing the klt pairs; the outline is in the proof in words. The last sentence follows because $e \le d$ and, by Theorem 7.5.2, a curve contracted by $\varphi$ has its class in $R$, nonzero since it has positive degree against an ample class.

*Corollary 7.4.14.* By part 2 of Theorem 7.4.6 the $K_\Delta$-negative extremal rays $R_i$, $i \in I$, are countable, finitely many are $(K_\Delta + \varepsilon H)$-negative for each $\varepsilon$, and with $\overline{NE}(X)_{K_\Delta \ge 0}$ they span $\overline{NE}(X)$. By Theorem 7.4.13 each $R_i$ is $\mathbb{R}_{\ge 0} [\Gamma_i]$ for a rational curve $\Gamma_i$ with $0 < -K_\Delta \cdot \Gamma_i \le 2d$.

*Proposition 7.4.15.* Let $G = \overline{NE}(X/S)$, a face of $\overline{NE}(X)$ by part 2 of Proposition P7.4.11. An extremal ray of $G$ is an extremal ray of $\overline{NE}(X)$: if $u + v \in R \subseteq G$ with $u, v \in \overline{NE}(X)$, then $u, v \in G$ because $G$ is a face, and then $u, v \in R$ because $R$ is extremal in $G$. Conversely an extremal ray of $\overline{NE}(X)$ contained in $G$ is extremal in $G$. The same argument proves part 4.

For part 1, let $z \in G$ and write $z = w + \sum_i r_i$ by part 2 of Theorem 7.4.6, with $w \in \overline{NE}(X)_{K_\Delta \ge 0}$ and $r_i \in R_i$, a finite sum. Since $G$ is a face, every summand lies in $G$: so $w \in G_{K_\Delta \ge 0}$, and every $R_i$ with $r_i \ne 0$ is contained in $G$. Part 2 follows in the same way from part 1 of Theorem 7.4.6, keeping only the rays $R_i$ on which $K_\Delta + \varepsilon H$ is negative and absorbing the others into the first summand, which is legitimate because $G_{K_\Delta + \varepsilon H \ge 0}$ is a convex cone containing them. For part 3, Theorem 7.4.13 gives a rational curve $\Gamma_j$ with $[\Gamma_j] \in R_j \subseteq G$ and the bound, and $f$ contracts $\Gamma_j$ by part 3 of Proposition P7.4.11.

### Exercises

1. (A) For $X = \mathbb{P}^1 \times \mathbb{P}^1$ and $\Delta = \frac12 D$ as in Example 7.4.9, find rational curves spanning the two rays and their lengths, and compare them with the bounds $2d = 4$ and $d + 1 = 3$.
2. (A) Let $X = \mathbb{P}^2$ and $\Delta = \frac12 (\ell_1 + \ell_2 + \ell_3)$ for three lines in general position. Show that $(X, \Delta)$ is klt and compute the length of the unique ray.
3. (B) In Example 7.4.17, describe all rational curves $\Gamma \subseteq X$ contracted by $p_1$ with $-K_X \cdot \Gamma \le 4$, and show that they cover $X$.
4. (B) Let $f \colon X \to S$ be a morphism of projective varieties and $g \colon S \to T$ another. Show that $\overline{NE}(X/S) \subseteq \overline{NE}(X/T)$ and that every $K_\Delta$-negative extremal ray of $\overline{NE}(X/S)$ is one of $\overline{NE}(X/T)$.
5. (B) Show that $\overline{NE}(X/S) = \{0\}$ if and only if $f$ is finite, and deduce that the relative cone theorem is empty for finite morphisms.
6. (C) Let $(X, \Delta)$ be klt with $d = 2$ and $\Delta = 0$, and suppose $X$ smooth. Show that Mori's bound $3$ of Corollary 6.2.10 and Kawamata's bound $4$ of Theorem 7.4.13 give the same set of rays, and that the minimal length of every ray is $1$, $2$ or $3$, using Proposition P7.4.21 and Theorem 6.3.9 only as a guide.

### Lean

The library has `MinimalModel.LengthOfExtremalRays`, the last sentence of Theorem 7.4.13, and `MinimalModel.ConeTheoremKlt`, both for projective klt pairs in characteristic $0$ and both as statements without proof. The relative cone theorem and Corollary 7.4.12 are not yet in Lean.

### Notes and history

The bound $2d$ is Kawamata's (Kaw91), who used the Miyaoka-Mori bend-and-break on a resolution of the fibres of the contraction; KM98 states it as Theorem 3.7, part 1, and refers to Kawamata for the proof. For smooth $X$ and $\Delta = 0$ Mori's bound $d + 1$ of Volume 6 is better, and it is expected that $d + 1$ holds for all klt pairs. The relative cone theorem over a quasi-projective base is KM98, Theorem 3.25; over a projective base it follows from the absolute theorem as above.
