---
title: Grauert's and Artin's contraction criteria
nodes: []
sources: [Art66, Mum61, DuV34, KM98, Bea96, Har77]
reads_with: [Art66:all, KM98:ch4]
requires: [P2.7, P3.11, P4.6, P5.5, P5.6, P5.7]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Grauert's and Artin's contraction criteria

### Statement

Theorem P5.8.3 says that the curves contracted by a birational morphism of surfaces form a negative definite configuration. This section asks for the converse, and the answer depends on the category. Grauert's theorem gives the converse for analytic contractions. Artin's theorem gives an algebraic contraction onto a projective surface when the configuration satisfies a numerical condition on its arithmetic genera, and the singularities that arise are the rational ones. The analytic theorem and the existence half of Artin's theorem are cited; the necessity of the numerical conditions, the theory of the fundamental cycle and the analysis of configurations of $(-2)$-curves are proved.

**Definition P5.8.10 (contractible configuration).** A configuration $C_1, \dots, C_r$ of integral curves on $S$ is *contractible* if there is a birational morphism $f \colon S \to T$ onto a normal projective surface whose exceptional curves are exactly $C_1, \dots, C_r$. If $C_1 \cup \dots \cup C_r$ is connected, then $f$ maps it to a single point $t$ by part 2 of Theorem P5.8.3, and $f$ *contracts* the configuration to $t$.

**Theorem P5.8.11 (Grauert's criterion).** Let $X$ be a smooth complex analytic surface and $C = C_1 \cup \dots \cup C_r$ a connected compact curve in $X$, with $C_i$ its irreducible components. There is a proper holomorphic map $f \colon X \to Y$ onto a normal complex analytic surface, with $f(C)$ a point $y$ and $f \colon X \setminus C \to Y \setminus \{y\}$ biholomorphic, if and only if the intersection matrix $(C_i \cdot C_j)$ is negative definite.

Lean: not in Lean as stated.

The theorem is cited, from Grauert's paper of 1962 in the form of Barth, Hulek, Peters and Van de Ven, *Compact complex surfaces*, Theorem III.2.1. The necessity of negative definiteness is the analytic form of Theorem P5.8.3. For a configuration on a smooth projective complex surface the space $Y$ obtained from Grauert's theorem need not be a projective variety, so a further condition is needed for an algebraic contraction.

From now on let $C_1, \dots, C_r$ be a connected negative definite configuration on $S$, with intersection matrix $M$.

**Definition P5.8.12 (cycles and the fundamental cycle).** A *cycle* is a divisor $Z = \sum_i a_i C_i$ with integer coefficients, and it is *positive*, written $Z > 0$, if $Z \geq 0$ and $Z \neq 0$. A positive cycle is an effective divisor on $S$, so a closed subscheme of $S$ of dimension $1$, and its *arithmetic genus* is $p_a(Z) = 1 - \chi(\mathcal{O}_Z)$. By the genus formula of Theorem P5.5.14,
$$2 p_a(Z) - 2 = Z \cdot (Z + K_S).$$
The *fundamental cycle* $Z_f$ of the configuration is the smallest positive cycle $Z$ with $Z \cdot C_j \leq 0$ for every $j$.

**Proposition P5.8.13 (the fundamental cycle).**

1. The set $\mathcal{Z}$ of positive cycles $Z$ with $Z \cdot C_j \leq 0$ for every $j$ is nonempty and closed under taking coefficientwise minima. Every $Z \in \mathcal{Z}$ has all coefficients $\geq 1$, and $\mathcal{Z}$ has a smallest element, so $Z_f$ exists.
2. (*Laufer's algorithm.*) Put $Z_0 = C_1 + \dots + C_r$. As long as there is $j$ with $Z_k \cdot C_j > 0$, choose such a $j$ and put $Z_{k+1} = Z_k + C_j$. This process stops after finitely many steps, at $Z_f$, and every $Z_k$ satisfies $Z_k \leq Z_f$.
3. For positive cycles $A, B$, $p_a(A + B) = p_a(A) + p_a(B) + A \cdot B - 1$.
4. $p_a(Z_f) \geq 0$.

Lean: not in Lean as stated.

**Definition P5.8.14 (rational singularity).** Let $f \colon S \to T$ be a birational morphism onto a normal projective surface. A point $t \in T$ is a *rational singularity* (of $f$) if $(R^1 f_* \mathcal{O}_S)_t = 0$. The sheaf $R^1 f_* \mathcal{O}_S$ is coherent, because $f$ is projective, and it vanishes on the open set $T \setminus T_0$ over which $f$ is an isomorphism, so it is supported on the finite set $T_0$ of Theorem P5.8.3. Every point of $T \setminus T_0$ is a smooth point of $T$ and a rational singularity in this sense. Exercise 5 shows that the condition does not depend on $f$.

**Proposition P5.8.15 (necessity of Artin's condition).** Let $f \colon S \to T$ be a birational morphism onto a normal projective surface, $t \in T_0$ a rational singularity, and $C_1, \dots, C_r$ the curves in $f^{-1}(t)$. Then $H^1(Z, \mathcal{O}_Z) = 0$ and $p_a(Z) \leq 0$ for every positive cycle $Z$ supported on $f^{-1}(t)$. In particular $p_a(Z_f) = 0$.

Lean: not in Lean as stated.

**Theorem P5.8.16 (Artin's contractibility and rationality criteria).** Let $C_1, \dots, C_r$ be a connected negative definite configuration on $S$.

1. The following are equivalent: $p_a(Z) \leq 0$ for every positive cycle $Z$, and $p_a(Z_f) = 0$.
2. If these hold, the configuration is contractible, and the point $t$ to which it is contracted is a rational singularity.
3. Conversely, if the configuration is contracted to a rational singularity $t$ by some $f$, then the conditions of part 1 hold.
4. If $t$ is a rational singularity obtained in this way, then $\mathfrak{m}_t \mathcal{O}_S = \mathcal{O}_S(-Z_f)$ on a neighbourhood of $f^{-1}(t)$, the local ring $\mathcal{O}_{T,t}$ has multiplicity $-Z_f^2$, and if $-Z_f^2 \geq 2$ its embedding dimension $\dim_k \mathfrak{m}_t / \mathfrak{m}_t^2$ is $-Z_f^2 + 1$.

Lean: not in Lean as stated.

Part 3 is Proposition P5.8.15, and the implication from the first condition of part 1 to the second follows from it and part 4 of Proposition P5.8.13. The remaining statements are cited: the equivalence in part 1 and part 4 from Artin (Art66, Theorems 3 and 4 and Corollary 6), and part 2 from Artin, *Some numerical criteria for contractability of curves on algebraic surfaces*, Amer. J. Math. 84 (1962), Theorem 2.3.

**Proposition P5.8.17 (configurations of $(-2)$-curves).** Let $C_1, \dots, C_r$ be a connected negative definite configuration with $C_i^2 = -2$ and $K_S \cdot C_i = 0$ for every $i$.

1. Every $C_i$ is isomorphic to $\mathbb{P}^1$, $C_i \cdot C_j \in \{0, 1\}$ for $i \neq j$, and the dual graph is a tree.
2. For every positive cycle $Z$, $Z^2$ is even and negative, and $p_a(Z) = 1 + \frac{1}{2} Z^2 \leq 0$.
3. $Z_f^2 = -2$. Consequently the configuration is contractible to a rational singularity of multiplicity $2$ and embedding dimension $3$, a rational double point.

Lean: not in Lean as stated.

The negative $-M$ of the intersection matrix in Proposition P5.8.17 is a positive definite symmetric matrix with $2$ on the diagonal, entries $0$ and $-1$ off the diagonal, and a tree as its graph. By the classification of such matrices, which is the classification of simply laced Dynkin diagrams (Bourbaki, *Groupes et algèbres de Lie*, Chapter VI, Section 4), the dual graph is one of $A_n$ ($n \geq 1$), $D_n$ ($n \geq 4$), $E_6$, $E_7$, $E_8$. This is cited. Du Val found these configurations as the resolutions of the surface singularities now named after him (DuV34), and Artin identified them with the rational double points (Art66).

### Proof in words

The fundamental cycle exists because the inverse of a negative definite matrix with nonnegative entries off the diagonal has negative entries, by Lemma P5.8.1, and it is the smallest element of a set closed under minima. Laufer's algorithm climbs to it from below: adding a curve $C_j$ with $Z \cdot C_j > 0$ never overshoots, because such a $C_j$ must occur in $Z_f$ with larger coefficient. Each step changes the arithmetic genus by $Z \cdot C_j - 1 + p_a(C_j) \geq 0$, so the genus of the fundamental cycle is at least that of the reduced curve, which is nonnegative.

For the necessity of Artin's condition, the theorem on formal functions writes the completed stalk of $R^1 f_* \mathcal{O}_S$ at $t$ as an inverse limit of the groups $H^1$ of the infinitesimal neighbourhoods of the fibre. Every positive cycle is a closed subscheme of a large enough neighbourhood, and on a scheme of dimension $1$ the restriction maps on $H^1$ are surjective. So all these groups vanish when the limit does.

For a configuration of $(-2)$-curves the canonical class is invisible: $K_S \cdot Z = 0$, and the genus formula gives $p_a(Z) = 1 + \frac12 Z^2$. The lattice is even and negative definite, so every positive cycle has $Z^2 \leq -2$, and Artin's criterion applies with $Z_f^2 = -2$.

### Examples

**Example P5.8.18 (fundamental cycles of $A_n$ and $D_4$).** For the chain $A_n$ of Example P5.8.6, $Z_0 = C_1 + \dots + C_n$ already satisfies $Z_0 \cdot C_j \leq 0$ for all $j$, so $Z_f = C_1 + \dots + C_n$ and $Z_f^2 = -2$, both for $n = 1$ and, by the computation of $M_{A_n} z$ there, for $n \geq 2$. For a configuration of type $D_4$, with a central $(-2)$-curve $C_0$ meeting three disjoint $(-2)$-curves $C_1, C_2, C_3$ transversally in one point each, Laufer's algorithm starts with $Z_0 = C_0 + C_1 + C_2 + C_3$. Then $Z_0 \cdot C_0 = -2 + 3 = 1 > 0$, so $Z_1 = 2C_0 + C_1 + C_2 + C_3$, with $Z_1 \cdot C_0 = -4 + 3 = -1$ and $Z_1 \cdot C_i = 2 - 2 = 0$ for $i = 1, 2, 3$. So
$$Z_f = 2C_0 + C_1 + C_2 + C_3, \qquad Z_f^2 = 2 Z_f \cdot C_0 = -2,$$
as part 3 of Proposition P5.8.17 predicts. The fundamental cycle is not reduced here.

**Example P5.8.19 (a single rational curve).** Let $C \cong \mathbb{P}^1$ be a smooth rational curve on $S$ with $C^2 = -n$, $n \geq 1$. By Theorem P5.5.14, $K_S \cdot C = -2 - C^2 = n - 2$. The positive cycles are $mC$, $m \geq 1$, and
$$p_a(mC) = 1 + \tfrac{1}{2}\left(-n m^2 + (n - 2) m\right) = 1 - m - \tfrac{n m (m - 1)}{2} \leq 0,$$
with equality only for $m = 1$. So $Z_f = C$, $p_a(Z_f) = 0$, and by Theorem P5.8.16, $C$ is contracted to a rational singularity of multiplicity $n$, with embedding dimension $n + 1$ if $n \geq 2$. For $n = 1$ the multiplicity is $1$ and the point is smooth, which is Castelnuovo's criterion, Theorem P5.7.4. For $n = 2$ this is the vertex of the quadric cone of Example P5.8.9. For general $n$ it is the vertex of the cone over the rational normal curve of degree $n$, whose embedding dimension $n + 1$ is visible from its equations.

**Example P5.8.20 (the vertex of the quadric cone is rational).** In Example P5.8.9, $U = f^{-1}(\operatorname{Spec} A)$ is covered by the two affine planes $U_1 = \operatorname{Spec} k[x, z']$ and $U_2 = \operatorname{Spec} k[y, z'']$, with $U_1 \cap U_2 = \operatorname{Spec} k[x, z', z'^{-1}]$, $z'' = z'^{-1}$ and $y = x z'^2$. Since $\operatorname{Spec} A$ is affine, the restriction of $R^1 f_* \mathcal{O}_S$ to it is the sheaf associated to $H^1(U, \mathcal{O}_U)$ (Hartshorne, Proposition III.8.5), and $H^1(U, \mathcal{O}_U)$ is the cokernel of the Čech map
$$k[x, z'] \oplus k[y, z''] \to k[x, z', z'^{-1}].$$
A monomial $x^a z'^b$ with $a \geq 0$ lies in the first summand if $b \geq 0$. If $b < 0$, then $x^a z'^b = y^a z''^{2a - b}$ with $2a - b > 0$, so it lies in the image of the second summand. Hence the map is onto, $H^1(U, \mathcal{O}_U) = 0$, and $v$ is a rational singularity. Consistently with Theorem P5.8.16, $E$ is a single $(-2)$-curve with $Z_f = E$, $-Z_f^2 = 2$ is the multiplicity of the quadric $xy = z^2$ at the origin, and $-Z_f^2 + 1 = 3$ is its embedding dimension. In the classification after Proposition P5.8.17 it is the rational double point $A_1$.

**Example P5.8.21 (the cone over a plane cubic is not rational).** Let $T$ be the projective cone over a smooth plane cubic $E_0$ and $f \colon S \to T$ the blow-up of the vertex, as in Example P4.6.5, where $S$ contains the total space of $\mathcal{O}_{E_0}(-1)$ and $R^1 f_* \mathcal{O}_S$ is the skyscraper $k$ at the vertex. The exceptional curve $E \cong E_0$ is the zero section, with normal bundle $\mathcal{O}_{E_0}(-1)$ of degree $-3$, so $E^2 = -3$. It is a smooth curve of genus $1$, so $p_a(E) = 1 > 0$, and Proposition P5.8.15 shows again that the vertex is not rational. Here $Z_f = E$ and $-Z_f^2 = 3$ is the multiplicity of the cone, but its embedding dimension is $3$, not $-Z_f^2 + 1 = 4$, so part 4 of Theorem P5.8.16 fails outside rational singularities.

### Proof

*Proposition P5.8.13.* (1) By Theorem P5.8.2, applied to $Z$ with $Z \cdot C_j \leq 0$, every $Z \in \mathcal{Z}$ has all coefficients positive, hence $\geq 1$, since the configuration is connected. Let $x = -M^{-1}(1, \dots, 1)^T$. Then $M x \leq 0$ and $M x \neq 0$, so all $x_i > 0$ by part 1 of Lemma P5.8.1, and $x$ has rational coordinates because $M$ has integer entries. For a positive integer $N$ with $N x$ integral, $Z = \sum_i N x_i C_i$ satisfies $Z \cdot C_j = -N < 0$, so $Z \in \mathcal{Z}$. Let $Z, Z' \in \mathcal{Z}$ and $W$ their coefficientwise minimum. Then $W \geq C_1 + \dots + C_r$ is positive. Fix $j$ and suppose, by symmetry, that $W$ and $Z$ have the same coefficient at $C_j$. Then $Z - W \geq 0$ does not contain $C_j$, so $(Z - W) \cdot C_j \geq 0$ and $W \cdot C_j \leq Z \cdot C_j \leq 0$. So $W \in \mathcal{Z}$. An element $Z_f \in \mathcal{Z}$ with the smallest sum of coefficients satisfies $\min(Z_f, Z) = Z_f$ for every $Z \in \mathcal{Z}$, that is, $Z_f \leq Z$.

(2) By part 1, $Z_0 \leq Z_f$. Suppose $Z_k \leq Z_f$ and $Z_k \cdot C_j > 0$. If $Z_k$ and $Z_f$ had the same coefficient at $C_j$, then $Z_f - Z_k \geq 0$ would not contain $C_j$ and $Z_f \cdot C_j = Z_k \cdot C_j + (Z_f - Z_k) \cdot C_j > 0$, a contradiction. So the coefficient of $C_j$ in $Z_k$ is smaller than in $Z_f$, and $Z_{k+1} \leq Z_f$. The sum of the coefficients increases at each step and is bounded by that of $Z_f$, so the process stops, at some $Z_k$ with $Z_k \cdot C_j \leq 0$ for all $j$. Then $Z_k \in \mathcal{Z}$, so $Z_f \leq Z_k \leq Z_f$.

(3) By the genus formula,
$$2 p_a(A + B) - 2 = (A + B) \cdot (A + B + K_S) = \big(2 p_a(A) - 2\big) + \big(2 p_a(B) - 2\big) + 2 A \cdot B.$$

(4) A connected reduced projective scheme over the algebraically closed field $k$ has $H^0(\mathcal{O}) = k$, so $p_a(Z_0) = h^1(\mathcal{O}_{Z_0}) \geq 0$, and in the same way $p_a(C_j) \geq 0$ for each integral $C_j$. In the step $Z_{k+1} = Z_k + C_j$ of part 2, part 3 gives $p_a(Z_{k+1}) = p_a(Z_k) + p_a(C_j) + Z_k \cdot C_j - 1 \geq p_a(Z_k)$, since $Z_k \cdot C_j \geq 1$. So $p_a(Z_f) \geq p_a(Z_0) \geq 0$. $\square$

*Proposition P5.8.15.* Let $\mathfrak{m} \subseteq \mathcal{O}_{T, t}$ be the maximal ideal and $V \ni t$ an affine open neighbourhood with $V \cap T_0 = \{t\}$, and work over $V$. Let $X_n \subseteq f^{-1}(V)$ be the closed subscheme defined by $\mathfrak{m}^n \mathcal{O}_S$, where $\mathfrak{m}$ also denotes the ideal of $t$ in $\mathcal{O}(V)$. By the theorem on formal functions (Theorem P4.6.1),
$$\left(R^1 f_* \mathcal{O}_S\right)_t^{\wedge} \cong \varprojlim_n H^1(X_n, \mathcal{O}_{X_n}),$$
and the completion of the finitely generated $\mathcal{O}_{T,t}$-module on the left vanishes, because the module does. Each $X_n$ has underlying space $f^{-1}(t)$, of dimension $1$. For $n \leq n'$ the surjection $\mathcal{O}_{X_{n'}} \to \mathcal{O}_{X_n}$ has a kernel supported on a space of dimension $1$, whose $H^2$ vanishes by Grothendieck's vanishing theorem (Theorem P2.7.13), so $H^1(\mathcal{O}_{X_{n'}}) \to H^1(\mathcal{O}_{X_n})$ is surjective. An inverse system of surjections indexed by $\mathbb{N}$ maps its limit onto every term, so $H^1(X_n, \mathcal{O}_{X_n}) = 0$ for every $n$.

Let $E_{\mathrm{red}} = C_1 + \dots + C_r$. A function in $\mathfrak{m}$ pulls back to a regular function on $f^{-1}(V)$ vanishing on every $C_i$, so it lies in the ideal $\mathcal{O}_S(-E_{\mathrm{red}})$ of the reduced curve $E_{\mathrm{red}}$, and $\mathfrak{m}^n \mathcal{O}_S \subseteq \mathcal{O}_S(-n E_{\mathrm{red}})$. Let $Z > 0$ be a cycle supported on $f^{-1}(t)$ and $n$ larger than all its coefficients. Then $\mathfrak{m}^n \mathcal{O}_S \subseteq \mathcal{O}_S(-Z)$, so $Z$ is a closed subscheme of $X_n$, and the same vanishing argument shows that $0 = H^1(\mathcal{O}_{X_n}) \to H^1(\mathcal{O}_Z)$ is surjective. Hence $H^1(Z, \mathcal{O}_Z) = 0$ and $p_a(Z) = 1 - h^0(\mathcal{O}_Z) \leq 0$, because $H^0(\mathcal{O}_Z)$ contains the constants. With part 4 of Proposition P5.8.13, $p_a(Z_f) = 0$. $\square$

*Proposition P5.8.17.* (1) By Theorem P5.5.14, $2 p_a(C_i) - 2 = C_i^2 + K_S \cdot C_i = -2$, so $p_a(C_i) = 0$ and $C_i \cong \mathbb{P}^1$ by Corollary P5.5.15. For $i \neq j$, $(C_i + C_j)^2 = -4 + 2 C_i \cdot C_j < 0$, so $C_i \cdot C_j \leq 1$. If the dual graph contained a cycle, say $C_1, \dots, C_m$ with $m \geq 3$ and $C_i$ meeting $C_{i+1}$ for all $i$, indices modulo $m$, then $Z = C_1 + \dots + C_m$ would have $Z^2 \geq -2m + 2m = 0$, contradicting negative definiteness. The dual graph is connected, so it is a tree.

(2) For $Z = \sum_i a_i C_i$, $Z^2 = -2 \sum_i a_i^2 + 2 \sum_{i < j} a_i a_j \, C_i \cdot C_j$ is even, and it is negative for $Z \neq 0$. So $Z^2 \leq -2$. Since $K_S \cdot Z = 0$, the genus formula gives $p_a(Z) = 1 + \frac12 Z^2 \leq 0$.

(3) By Proposition P5.8.13 and part 2, $0 \leq p_a(Z_f) = 1 + \frac12 Z_f^2 \leq 0$, so $Z_f^2 = -2$. The rest is Theorem P5.8.16: by part 2 the configuration is contractible to a rational singularity, and by part 4 its multiplicity is $2$ and its embedding dimension $3$. $\square$

### Exercises

1. (A) Compute the fundamental cycle of the configurations $D_n$ ($n \geq 4$) and $E_6$ by Laufer's algorithm, and check that $Z_f^2 = -2$ in each case.
2. (A) Let $C_1, C_2$ be smooth rational curves with $C_1^2 = -2$ and $C_2^2 = -3$ meeting transversally in one point. Show that the configuration is negative definite, that $Z_f = C_1 + C_2$ and $p_a(Z_f) = 0$, and find the multiplicity and the embedding dimension of the singularity obtained by contracting it.
3. (A) Show that two $(-2)$-curves with $C_1 \cdot C_2 = 2$ do not form a negative definite configuration, and find the nef divisor that part 2 of Lemma P5.8.1 produces.
4. (B) Let $t$ be a rational singularity of $f$. Using Proposition P5.8.15 and part 3 of Proposition P5.8.13, show that every curve $C_i$ over $t$ is isomorphic to $\mathbb{P}^1$, that $C_i \cdot C_j \leq 1$ for $i \neq j$, and that the dual graph of $f^{-1}(t)$ is a tree.
5. (B) Let $f \colon S \to T$ be as in Definition P5.8.14 and $g \colon S' \to S$ the blow-up of a point. Show that $R^1 g_* \mathcal{O}_{S'} = 0$ and $g_* \mathcal{O}_{S'} = \mathcal{O}_S$, deduce from the Leray spectral sequence, or from the five term exact sequence, that $R^1 (f \circ g)_* \mathcal{O}_{S'} \cong R^1 f_* \mathcal{O}_S$, and conclude with Theorem P5.7.12 that the notion of rational singularity does not depend on $f$.
6. (C) Let $C$ be a smooth curve of genus $g \geq 1$ on $S$ with $C^2 < 0$. Show that the fundamental cycle of $\{C\}$ is $C$, with $p_a(Z_f) = g$, and that $C$ is never contracted to a rational singularity. For a smooth projective curve $B$ of genus $g$, blow up a point of the section $B \times \{0\}$ of $B \times \mathbb{P}^1$ and show that the strict transform of the section is such a curve with $C^2 = -1$, so that every value $p_a(Z_f) \geq 0$ occurs.

### Lean

Mathlib has the theory of root systems and Cartan matrices (`RootPairing`, `CartanMatrix.E₈`), which covers the linear algebra behind the classification of $(-2)$-configurations. It has no intersection theory on surfaces, no fundamental cycle and no rational singularities. The handbook adds no `MinimalModel` node here.

### Notes and history

Du Val studied in 1934 the isolated singularities of surfaces that do not affect the conditions of adjunction and found the configurations $A_n$, $D_n$, $E_6$, $E_7$, $E_8$ of $(-2)$-curves on their resolutions (DuV34). Mumford proved negative definiteness in general (Mum61), and Grauert proved in 1962 that negative definiteness characterizes the analytically contractible configurations (H. Grauert, *Über Modifikationen und exzeptionelle analytische Mengen*, Math. Ann. 146 (1962)). Artin gave in 1962 the numerical criterion for an algebraic contraction onto a projective surface, and in 1966 introduced the fundamental cycle and the theory of rational singularities (Art66). Laufer's algorithm and the classification of minimally elliptic singularities followed in the 1970s, and Lipman developed rational singularities of two-dimensional schemes in general in 1969. The literature state is theorem. In the minimal model program, the Du Val singularities are exactly the canonical surface singularities, and in characteristic $0$ the log terminal surface singularities are rational, being quotient singularities (KM98, Section 4.1). Artin's criterion is the surface ancestor of the contraction theorem of Volume 2, where the existence of a contraction is proved by the base point free theorem rather than by a numerical criterion on the exceptional curves.
