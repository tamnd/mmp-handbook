---
title: The big cone and the pseudo-effective cone
nodes: []
sources: [Laz04, Deb01, Nak04, Har77]
reads_with: [Laz04:2.2.B, Deb01:ch1, Nak04:II.5]
requires: [P4.7, P5.5, P5.9, P7.1, P7.2, P7.3, P7.4]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The big cone and the pseudo-effective cone

### Statement

Throughout, $X$ is a projective variety over $k$ of dimension $n \geq 1$, and $\operatorname{Big}(X) = \operatorname{Amp}(X) + \operatorname{Eff}(X)$ is the big cone of Definition P7.5.5. For classes $\xi_1, \dots, \xi_n \in N^1(X)$ the number $(\xi_1 \cdots \xi_n)$ is the real intersection number of part 1 of Definition P7.3.8.

**Definition P7.5.11 (pseudo-effective classes).** A class $\xi \in N^1(X)$ is *pseudo-effective* if $\xi \in \overline{\operatorname{Eff}}(X)$, the closure of the effective cone (Definition P7.4.13). The closed cone $\overline{\operatorname{Eff}}(X)$ is the *pseudo-effective cone*. An $\mathbb{R}$-Cartier divisor, or a line bundle, is pseudo-effective if its class is.

**Theorem P7.5.12 (big and pseudo-effective cones).**

1. $\operatorname{Big}(X) = \operatorname{int} \operatorname{Eff}(X) = \operatorname{int} \overline{\operatorname{Eff}}(X)$.
2. $\overline{\operatorname{Big}(X)} = \overline{\operatorname{Eff}}(X)$.
3. For $\xi \in N^1(X)$ the following are equivalent: (a) $\xi$ is pseudo-effective; (b) $\xi + \alpha \in \operatorname{Big}(X)$ for every $\alpha \in \operatorname{Amp}(X)$; (c) for one $\alpha \in \operatorname{Amp}(X)$, $\xi + \varepsilon \alpha \in \operatorname{Big}(X)$ for every real $\varepsilon > 0$.
4. $\operatorname{Big}(X) + \overline{\operatorname{Eff}}(X) \subseteq \operatorname{Big}(X)$.
5. $\overline{\operatorname{Eff}}(X)$ is a closed convex cone with nonempty interior, and it contains $\operatorname{Nef}(X)$ and $\operatorname{Big}(X)$.

Lean: `MinimalModel.IsPseudoEffective`, in the project library, is the condition that for some ample $A$, $D + \varepsilon A$ satisfies `MinimalModel.IsBig` for every $\varepsilon > 0$, which is condition (c) of part 3; the equivalence with the closure of the effective cone is not stated there.

**Proposition P7.5.13 (degrees of pseudo-effective classes).** Let $h_1, \dots, h_{n-1} \in N^1(X)$.

1. If the $h_i$ are nef and $\xi$ is pseudo-effective, then $(\xi \cdot h_1 \cdots h_{n-1}) \geq 0$.
2. If the $h_i$ are ample and $\xi$ is big, then $(\xi \cdot h_1 \cdots h_{n-1}) > 0$.

Lean: not in Lean as stated.

**Proposition P7.5.14 (pullback).** Let $f \colon Y \to X$ be a surjective morphism of projective varieties with $\dim Y = \dim X$. Then $f^* \operatorname{Big}(X) \subseteq \operatorname{Big}(Y)$ and $f^* \overline{\operatorname{Eff}}(X) \subseteq \overline{\operatorname{Eff}}(Y)$.

Lean: not in Lean as stated.

### Proof in words

The two cones are related by a single inclusion: a pseudo-effective class plus an ample class is big. Indeed, a pseudo-effective class is a limit of effective classes, and the difference between the class and a nearby effective class is small enough to be absorbed by the open ample cone. Everything in Theorem P7.5.12 follows from this inclusion and the openness of the big cone: the big cone is open and contained in the effective cone, so it lies in the interior; a class in the interior of the pseudo-effective cone stays pseudo-effective after subtracting a small ample class, and adding it back makes it big.

The degree with respect to an ample class is positive on effective divisors, by cutting with the canonical section. It is therefore nonnegative on the pseudo-effective cone and positive on the big cone. On a surface, a class with positive square and positive degree is big by Riemann-Roch, which is the source of most of the examples.

### Examples

**Example P7.5.15 (the blow-up of a point).** Let $X = \operatorname{Bl}_p \mathbb{P}^n$, $n \geq 2$, and write classes as $x H - y E$. By Proposition P7.4.18, $\overline{\operatorname{Eff}}(X) = \operatorname{Eff}(X) = \langle E, H - E \rangle = \{ x \geq 0, \ y \leq x \}$. By part 1 of Theorem P7.5.12,
$$\operatorname{Big}(X) = \{ x H - y E : x > 0, \ y < x \}.$$
The boundary rays are spanned by $E$, which has $h^0(mE) = 1$ (Example P7.5.9), and by $H - E$, whose sections are the forms of degree $m$ vanishing to order $m$ at $p$, that is, the cones with vertex $p$ over hypersurfaces of degree $m$ in $\mathbb{P}^{n-1}$; there are $\binom{m + n - 1}{n - 1}$ of them, which grows like $m^{n-1}$. The class $H$ is big and lies on the boundary of $\operatorname{Nef}(X)$, and $H + E$ is big and not nef.

**Example P7.5.16 (Hirzebruch surfaces).** Let $X = \mathbb{F}_n$, $n \geq 1$. By Proposition P7.4.19, $\overline{\operatorname{Eff}}(X) = \langle C_-, F \rangle$, so $a C_- + b F$ is big if and only if $a > 0$ and $b > 0$. By part 2 of Proposition P5.9.9, $-K_X \sim 2 C_- + (n + 2) F$, which is big for every $n$. Since $C_+ \equiv C_- + n F$, $-K_X \equiv 2 C_+ + (2 - n) F$, and since $\operatorname{Nef}(X) = \langle F, C_+ \rangle$, the class $-K_X$ is nef if and only if $n \leq 2$. For $n \geq 3$, $-K_X$ is big and not nef, with $-K_X \cdot C_- = 2 - n < 0$ by part 4 of Proposition P5.9.9.

**Example P7.5.17 (two points).** Let $X$ be the blow-up of $\mathbb{P}^2$ at two points, with $L_{12} = H - E_1 - E_2$. By Proposition P7.4.20, $\overline{\operatorname{Eff}}(X) = \langle E_1, E_2, L_{12} \rangle$, a simplicial cone, so $\operatorname{Big}(X)$ is the set of combinations $a_1 E_1 + a_2 E_2 + c L_{12}$ with all three coefficients positive. The class $H = L_{12} + E_1 + E_2$ is big. The class $H - E_1 = L_{12} + E_2$ lies on a face and is not big; it is the class of the pencil of lines through the first point, and it is nef by Proposition P7.4.20.

**Example P7.5.18 (positive square on a surface).** Let $X$ be a smooth projective surface, $H$ ample and $D$ a divisor with $D^2 > 0$ and $D \cdot H > 0$. Then $D$ is big. By Theorem P5.5.13,
$$h^0(mD) - h^1(mD) + h^2(mD) = \chi(\mathcal{O}_X) + \tfrac12 (m^2 D^2 - m D \cdot K_X).$$
By Corollary P4.7.21, $h^2(mD) = h^0(K_X - mD)$. For large $m$, $(K_X - mD) \cdot H < 0$, so $K_X - mD$ is not effective by part 1 of Proposition P7.5.13, and $h^2(mD) = 0$. Hence $h^0(mD) \geq \tfrac12 D^2 m^2 + O(m)$, and $D$ is big. If $D^2 > 0$ and $D \cdot H < 0$, the same argument shows that $-D$ is big. So the classes of positive square form two open cones, one of which lies in $\operatorname{Big}(X)$.

### Proof

*Theorem P7.5.12.* The key step is the inclusion
$$\overline{\operatorname{Eff}}(X) + \operatorname{Amp}(X) \subseteq \operatorname{Big}(X). \qquad (*)$$
Let $\xi \in \overline{\operatorname{Eff}}(X)$ and $\alpha \in \operatorname{Amp}(X)$. Since $\operatorname{Amp}(X)$ is open (part 1 of Theorem P7.3.12), there is a neighbourhood $U$ of $0$ with $\alpha + U \subseteq \operatorname{Amp}(X)$. Choose $\varepsilon \in \operatorname{Eff}(X)$ with $\xi - \varepsilon \in U$. Then $\xi + \alpha = (\alpha + (\xi - \varepsilon)) + \varepsilon \in \operatorname{Amp}(X) + \operatorname{Eff}(X) = \operatorname{Big}(X)$.

Part 1. By parts 1 and 3 of Proposition P7.5.6, $\operatorname{Big}(X)$ is open and contained in $\operatorname{Eff}(X)$, so $\operatorname{Big}(X) \subseteq \operatorname{int} \operatorname{Eff}(X) \subseteq \operatorname{int} \overline{\operatorname{Eff}}(X)$. Let $\xi \in \operatorname{int} \overline{\operatorname{Eff}}(X)$ and fix $\alpha \in \operatorname{Amp}(X)$, which is nonempty since $X$ is projective. For small $\delta > 0$, $\xi - \delta \alpha \in \overline{\operatorname{Eff}}(X)$, and $\xi = (\xi - \delta \alpha) + \delta \alpha \in \operatorname{Big}(X)$ by $(*)$.

Part 2. Since $\operatorname{Big}(X) \subseteq \operatorname{Eff}(X)$, $\overline{\operatorname{Big}(X)} \subseteq \overline{\operatorname{Eff}}(X)$. Conversely, for $\xi \in \overline{\operatorname{Eff}}(X)$ and $\alpha$ ample, $\xi + \alpha / j \in \operatorname{Big}(X)$ for all $j \geq 1$ by $(*)$, and these classes converge to $\xi$.

Part 3. (a) implies (b) by $(*)$. (b) implies (c) because $\varepsilon \alpha$ is ample for $\varepsilon > 0$. Assume (c). Then $\xi = \lim_{\varepsilon \to 0} (\xi + \varepsilon \alpha)$ lies in $\overline{\operatorname{Big}(X)} = \overline{\operatorname{Eff}}(X)$ by part 2.

Part 4. Let $\beta \in \operatorname{Big}(X)$ and $\xi \in \overline{\operatorname{Eff}}(X)$, and fix $\alpha$ ample. Since $\operatorname{Big}(X)$ is open, $\beta - \delta \alpha \in \operatorname{Big}(X)$ for small $\delta > 0$. By $(*)$, $\xi + \delta \alpha \in \operatorname{Big}(X) \subseteq \operatorname{Eff}(X)$. So $\beta + \xi = (\beta - \delta \alpha) + (\xi + \delta \alpha) \in \operatorname{Big}(X) + \operatorname{Eff}(X) \subseteq \operatorname{Big}(X)$, by part 1 of Proposition P7.5.6.

Part 5. The closure of a convex cone is a closed convex cone. It contains the nonempty open set $\operatorname{Amp}(X)$, so it has nonempty interior. It contains $\operatorname{Nef}(X)$ by part 1 of Proposition P7.4.15 and $\operatorname{Big}(X)$ by part 3 of Proposition P7.5.6.

*Proposition P7.5.13.* Part 1. First let $E$ be an effective Cartier divisor, $E \neq 0$, and $A_1, \dots, A_{n-1}$ ample line bundles. The canonical section $s_E$ of $\mathcal{O}_X(E)$ does not vanish at the generic point, the only associated point of $\mathcal{O}_X$, and its cokernel is $\mathcal{O}_E$, so by part 6 of Theorem P7.1.6,
$$(A_1 \cdots A_{n-1} \cdot \mathcal{O}_X(E)) = (A_1 \cdots A_{n-1} \cdot \mathcal{O}_E).$$
Since $E \neq 0$, Krull's principal ideal theorem gives $\dim \operatorname{Supp} \mathcal{O}_E = n - 1$. By part 2 of Proposition P7.1.14, applied to the sheaf $\mathcal{O}_E$, the right side is positive. If $h_1, \dots, h_{n-1}$ are in $\operatorname{Amp}(X)$, each is a positive combination of classes of ample line bundles (part 3 of Definition P7.3.8), and expanding by multilinearity gives $(\varepsilon \cdot h_1 \cdots h_{n-1}) \geq 0$ for $\varepsilon \in \operatorname{Eff}(X)$. The intersection number is a continuous function of its arguments, being multilinear on a finite-dimensional space. Since $\overline{\operatorname{Eff}}(X)$ is the closure of $\operatorname{Eff}(X)$ and $\operatorname{Nef}(X)$ is the closure of $\operatorname{Amp}(X)$ (part 4 of Theorem P7.3.12), the inequality extends to $\xi$ pseudo-effective and $h_i$ nef.

Part 2. Write $\xi = \alpha + \varepsilon$ with $\alpha$ ample and $\varepsilon \in \operatorname{Eff}(X)$. Then $(\varepsilon \cdot h_1 \cdots h_{n-1}) \geq 0$ by part 1. Expanding $\alpha$ and the $h_i$ as positive combinations of classes of ample line bundles, $(\alpha \cdot h_1 \cdots h_{n-1})$ is a positive combination of numbers $(A_0 \cdot A_1 \cdots A_{n-1})$ with all $A_i$ ample, each positive by part 2 of Proposition P7.1.14 with $V = X$. So the sum is positive.

*Proposition P7.5.14.* The map $f^* \colon N^1(X) \to N^1(Y)$ is linear (part 1 of Proposition P7.2.7), hence continuous. Let $E$ be an effective Cartier divisor on $X$ with local equations $g_i$. Since $f$ is surjective and $Y$ is integral, the generic point of $Y$ maps to the generic point of $X$, so $f^* g_i$ is a nonzero function and $f^* E$ is an effective Cartier divisor with $[f^* E] = f^* [E]$. So $f^* \operatorname{Eff}(X) \subseteq \operatorname{Eff}(Y)$. If $A$ is an ample line bundle on $X$, $f^* A$ is big by part 6 of Corollary P7.5.4, so $f^* [A] \in \operatorname{Big}(Y)$ by part 2 of Proposition P7.5.6. A class of $\operatorname{Amp}(X)$ is a positive combination of such classes, so $f^* \operatorname{Amp}(X) \subseteq \operatorname{Big}(Y)$, since $\operatorname{Big}(Y)$ is a convex cone. Hence $f^* \operatorname{Big}(X) \subseteq \operatorname{Big}(Y) + \operatorname{Eff}(Y) \subseteq \operatorname{Big}(Y)$. By continuity, $f^* \overline{\operatorname{Eff}}(X) \subseteq \overline{\operatorname{Eff}}(Y)$.

### Exercises

1. (A) On $\mathbb{P}^1 \times \mathbb{P}^1$, show that $\overline{\operatorname{Eff}} = \operatorname{Nef} = \langle (1, 0), (0, 1) \rangle$ and $\operatorname{Big} = \operatorname{Amp}$.
2. (A) On $\mathbb{F}_n$, decide for which $(a, b)$ the class $a C_- + b F$ is big and nef, and check that these classes are the classes of $\operatorname{Big} \cap \operatorname{Nef}$ described by Proposition P7.4.19.
3. (B) On $\operatorname{Bl}_p \mathbb{P}^2$, find a nonzero pseudo-effective class $\xi'$ with $(\xi' \cdot H) = 0$ for the nef class $H$, so that part 2 of Proposition P7.5.13 fails for nef classes. On a smooth projective surface, show that a pseudo-effective class $\xi$ with $(\xi \cdot h) = 0$ for an ample $h$ is zero, by writing $\xi$ as a limit of effective classes and using the Hodge index theorem; deduce that $\overline{\operatorname{Eff}}$ of a surface contains no line.
4. (B) Let $X$ be a smooth projective surface. Using Example P7.5.18, show that a nef class $\xi$ with $\xi^2 > 0$ is big, and that a nef class with $\xi^2 = 0$ is on the boundary of $\overline{\operatorname{Eff}}(X)$.
5. (B) Let $f \colon Y = \operatorname{Bl}_p \mathbb{P}^2 \to X = \mathbb{P}^2$. Show that $f^* \overline{\operatorname{Eff}}(X) = \overline{\operatorname{Eff}}(Y) \cap f^* N^1(X)$ and that $f_*$, defined on divisor classes by pushing forward cycles, maps $\overline{\operatorname{Eff}}(Y)$ onto $\overline{\operatorname{Eff}}(X)$.
6. (C) Let $X$ be a smooth projective surface and $\xi \in N^1(X)$ with $\xi^2 > 0$. Show that $\xi$ or $-\xi$ is big, and deduce from the Hodge index theorem that the positive cone $\{ \xi^2 > 0, \ \xi \cdot h > 0 \}$, for $h$ ample, is contained in $\operatorname{Big}(X)$ and has closure contained in $\overline{\operatorname{Eff}}(X)$.

### Lean

The project library defines `MinimalModel.IsPseudoEffective` for an $\mathbb{R}$-divisor as the existence of an ample $A$ with $D + \varepsilon A$ big, in the sense of `MinimalModel.IsBig`, for all $\varepsilon > 0$, and it defines the effective cone `MinimalModel.effCone` and the nef cone `MinimalModel.nefCone`. Theorem P7.5.12, which identifies this condition with membership in the closure of the effective cone, is not stated in the library. Mathlib has no pseudo-effective cones. The handbook adds no `MinimalModel` node here.

### Notes and history

The big cone and the pseudo-effective cone are treated in Lazarsfeld, Section 2.2.B (Laz04), where Theorem 2.2.26 identifies the big cone with the interior of the pseudo-effective cone, and in Debarre, Section 1.5 (Deb01). Nakayama, Chapter II (Nak04), works with the pseudo-effective cone throughout and constructs on it the $\sigma$-decomposition that generalizes the Zariski decomposition of Section 7.3 to higher dimension. The literature state is theorem. The pseudo-effective cone need not be generated by the classes of effective divisors: on a general blow-up of $\mathbb{P}^2$ at nine or more points it has infinitely many extremal rays, and on some threefolds it is round. The definition of pseudo-effectivity by the condition $D + \varepsilon A$ big, used in the project library, is the one that generalizes to the relative setting of the minimal model program.
