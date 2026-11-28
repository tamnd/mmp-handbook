---
title: Fano varieties and the theorem of Graber, Harris and Starr
nodes: []
sources: [KMM92b, Cam92, Kol96, KM98, GHS03, Deb01, KMM92a]
reads_with: [Kol96:V.2, Deb01:4.3]
requires: [P3.7, P3.10, P5.2, P5.9, P5.10, P7.2, P8.1, P8.2]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Fano varieties and the theorem of Graber, Harris and Starr

### Statement

In this section $k$ is algebraically closed, and from Theorem P8.3.21 on $k = \mathbb{C}$. Rationally connected varieties are as in Definition P8.3.11.

**Definition P8.3.18 (Fano variety).** A *Fano variety* is a smooth projective variety $X$ over $k$ with $-K_X$ ample.

**Theorem P8.3.19 (Kollár, Miyaoka and Mori; Campana, cited).** Let $X$ be a Fano variety. Then $X$ is rationally chain connected. If $k$ has characteristic $0$, then $X$ is rationally connected.

Lean: not in Lean as stated.

**Corollary P8.3.20 (consequences for Fano varieties).** Let $X$ be a Fano variety of dimension $n$ and let $k$ have characteristic $0$.

1. $X$ is uniruled, and contains a very free rational curve through every finite set of closed points.
2. $H^0(X, (\Omega^1_X)^{\otimes m}) = 0$ and $H^0(X, \Omega^p_X) = 0$ for all $m \geq 1$ and $1 \leq p \leq n$.
3. Through a general point $x \in X$ there is a rational curve $\Gamma$ with $-K_X \cdot \Gamma \leq 2n$.

Lean: not in Lean as stated.

**Theorem P8.3.21 (Graber, Harris and Starr, cited).** Let $f \colon X \to B$ be a proper morphism of complex varieties, with $B$ a smooth curve, whose general fibre is rationally connected. Then $f$ has a section.

Lean: not in Lean as stated.

**Corollary P8.3.22 (fibrations, cited).** Let $f \colon X \to Y$ be a dominant morphism of complex varieties. If $Y$ and the general fibre of $f$ are rationally connected, then $X$ is rationally connected.

Lean: not in Lean as stated.

**Example P8.3.23 (conic bundles over the line).** Let $S$ be a smooth projective surface and $\varphi \colon S \to \mathbb{P}^1$ a surjective morphism whose general fibre is a smooth conic. Then $S$ is rational, hence rationally connected. On the smooth cubic surface $X$ of Example P8.3.16, the pencil $|\ell - E_6|$ of Example P5.10.8 is such a conic bundle, with five singular fibres, each a pair of lines, and with the line $E_6$ as a section.

**Example P8.3.24 (conic bundles over a curve of positive genus).** Let $C$ be a smooth projective curve of genus $g \geq 1$ and $\varphi \colon S \to C$ a surjective morphism from a smooth projective surface whose general fibre is a smooth conic, for example a geometrically ruled surface $\mathbb{P}(\mathcal{E})$ of Definition P5.9.1. Then $S$ is uniruled but not rationally connected, and $H^0(S, \Omega^1_S) \neq 0$.

**Example P8.3.25 (Fano hypersurfaces).** Let $X \subseteq \mathbb{P}^N$ be a smooth hypersurface of degree $d$, with $N \geq 3$. Then $-K_X = (N + 1 - d) H|_X$, so $X$ is a Fano variety exactly when $d \leq N$, and then $X$ is rationally connected in characteristic $0$. For $d \leq N - 1$ there is a line through every point. Examples are quadrics, cubic surfaces, cubic threefolds and quartic threefolds.

### Proof in words

Mori's bend-and-break, run in characteristic $p$ with the ample class $-K_X$, produces rational curves of bounded anticanonical degree through every point, and in a Fano variety these curves can be chained: the variety is covered by rational curves of bounded degree, and the equivalence relation of being joined by a chain of them has a single class, because the quotient by it would be a variety of smaller dimension on which the ampleness of $-K_X$ produces further rational curves that are not contracted. In characteristic $0$, chain connectedness becomes rational connectedness by part 2 of Theorem P8.3.13. The consequences in Corollary P8.3.20 are then the results of Section 3.2 applied to Fano varieties.

The theorem of Graber, Harris and Starr is a statement about sections of a family over a curve. It is proved by a deformation argument on the space of sections of auxiliary families of curves, and is not reproduced here. Its corollary follows: given a general point of $X$ and a second general point, join their images in $Y$ by a rational curve, and apply Theorem P8.3.21 to the restriction of $f$ over that curve.

### Examples

*Example P8.3.23.* The general fibre of $\varphi$ is a smooth conic over the algebraically closed field $k$, hence isomorphic to $\mathbb{P}^1_k$. By Theorem P5.9.18, there is a nonempty open $U \subseteq \mathbb{P}^1$ with $\varphi^{-1}(U) \cong U \times \mathbb{P}^1$, so $S$ is birational to $\mathbb{P}^1 \times \mathbb{P}^1$ and to $\mathbb{P}^2$. A rational variety is rationally connected: a birational map $\mathbb{P}^2 \dashrightarrow S$ is defined outside finitely many points by part 2 of Proposition P3.10.29, two general points of $S$ are images of two points of $\mathbb{P}^2$ lying on a line missing the indeterminacy points, and the lines with this property form a dense open subset of the dual plane. For the cubic surface, Example P5.10.8 identifies the members of $|\ell - E_6|$ as the strict transforms of lines through $P_6$, the conics residual to the line $G_6$ in the planes through $G_6$; its five singular fibres are the pairs $F_{j6} + E_j$ for $j \neq 6$, with $F_{j6}$ the strict transform of the line $L_{j6}$ through $P_j$ and $P_6$, and $E_6 \cdot (\ell - E_6) = 1$ shows that $E_6$ meets each fibre once, so it is a section. Here the rationality of $S$ is visible from the start, since $S$ is the blown-up plane.

*Example P8.3.24.* The surface $S$ is uniruled: the fibres over the dense open set where they are smooth conics are rational curves covering a dense subset of $S$, and over a dense open $U \subseteq C$ Theorem P5.9.18 gives $\varphi^{-1}(U) \cong U \times \mathbb{P}^1$, whose second projection is a family as in Definition P8.3.1. A rational curve $\mathbb{P}^1 \to S$ composed with $\varphi$ is a morphism $\mathbb{P}^1 \to C$, which is constant by Theorem P5.2.12, since $C \not\cong \mathbb{P}^1$. So every connected curve with rational components lies in a fibre of $\varphi$, and as in Example P8.3.17 the pairs of points of $S$ joined by such curves lie in $S \times_C S$, a proper closed subset of $S \times S$. Finally, $\varphi$ is flat, being a surjective morphism from an integral surface to a smooth curve, and its fibres over a dense open $V \subseteq C$ are smooth conics, so $\varphi$ is smooth over $V$ and $\varphi^* \Omega^1_C \to \Omega^1_S$ is injective there. So the pullback of a nonzero section of $\omega_C$, which exists since $h^0(\omega_C) = g \geq 1$, is a nonzero global $1$-form on $S$. This shows that the hypothesis that the base is rationally connected cannot be dropped in Corollary P8.3.22.

*Example P8.3.25.* By the adjunction formula and $K_{\mathbb{P}^N} = -(N + 1) H$, as in Example P8.3.8, $K_X = (d - N - 1) H|_X$, and $(N + 1 - d) H|_X$ is ample exactly when $N + 1 - d > 0$. Theorem P8.3.19 gives rational connectedness, and Example P8.3.8 gives the lines. For $d = N$ the lines need not pass through every point; a smooth quartic threefold in $\mathbb{P}^4$ is still rationally connected, and has $-K_X = H$. The cubic surface was treated directly in Example P8.3.16.

### Proof

*Theorem P8.3.19.* This is Kollár, Miyaoka and Mori (KMM92b) and Campana (Cam92), and Kollár, Chapter V, Section 2 (Kol96); see also Kollár and Mori, Section 1.3 (KM98), and Debarre, Chapter 4 (Deb01). The proof is not given here. In characteristic $p$, the version of Theorem P8.2.10 that keeps a point fixed gives, through every point, rational curves of $-K_X$-degree at most $n + 1$. These curves define an equivalence relation, and its quotient, constructed by Kollár, Miyaoka and Mori and by Campana, is a rational map $X \dashrightarrow Z$. If $\dim Z > 0$, bend-and-break applied to curves in $X$ lying over curves in $Z$ produces rational curves through general points that are not contracted, a contradiction; so $Z$ is a point and $X$ is rationally chain connected. The characteristic $0$ case reduces to characteristic $p$ as in Theorem P8.2.12, and part 2 of Theorem P8.3.13 turns chains into single curves.

*Corollary P8.3.20.* By Theorem P8.3.19, $X$ is rationally connected, hence uniruled by the remark after Definition P8.3.11, and part 1 of Theorem P8.3.13 gives the very free curves of part 1. Part 2 is Proposition P8.3.14. For part 3, $-K_X$ is ample, so some multiple $-m K_X$ is very ample and embeds $X$ in a projective space. By part 2 of Proposition P3.7.5, applied in an affine neighbourhood of $x$, every irreducible component through $x$ of the intersection of $X$ with $n - 1$ hyperplanes through $x$ has dimension at least $1$; cutting with further hyperplanes through $x$ if needed gives a curve $C \subseteq X$ through $x$, and $X$ is smooth along $C$. With $H = -K_X$, Theorem P8.3.6 gives a rational curve $\Gamma$ through $x$ with
$$-K_X \cdot \Gamma \leq \frac{2 n \, (-K_X \cdot C)}{-K_X \cdot C} = 2 n.$$
Kollár and Mori, Theorem 1.10 (KM98), improves this to a rational curve through every point with $-K_X \cdot \Gamma \leq n + 1$, the bound of Theorem P8.2.13.

*Theorem P8.3.21.* This is Graber, Harris and Starr, Theorem 1.1 (GHS03). The proof is not given here. When the fibres are conics, it reduces to Tsen's theorem that the function field $\mathbb{C}(B)$ of a curve is $C_1$, so that a conic over it has a rational point; for $B = \mathbb{P}^1$ this is the situation of Example P8.3.23, where Theorem P5.9.18 gives the section directly.

*Corollary P8.3.22.* This is Graber, Harris and Starr, Corollary 1.3 (GHS03). Granting Theorem P8.3.21, the argument is as follows when $X$ and $Y$ are smooth and projective; Graber, Harris and Starr reduce the general case to this one by compactifying and resolving. Let $Y^0 \subseteq Y$ be a dense open set over which the fibres of $f$ are rationally connected. Two general points $x_1, x_2 \in X$ have images $y_1, y_2 \in Y^0$, joined by a rational curve $g \colon \mathbb{P}^1 \to Y$, since $Y$ is rationally connected, with $g(a_1) = y_1$ and $g(a_2) = y_2$. The base change $X \times_Y \mathbb{P}^1 \to \mathbb{P}^1$ has rationally connected general fibre, so by Theorem P8.3.21 it has a section, a rational curve $\sigma$ in $X$ over $g$. The points $x_1$ and $\sigma(a_1)$ lie in the rationally connected fibre $X_{y_1}$, and similarly for $x_2$, so a chain of three rational curves joins $x_1$ to $x_2$. Letting the points and curves vary in families shows that $X$ is rationally chain connected, and part 2 of Theorem P8.3.13 shows that it is rationally connected.

### Exercises

1. (A) Show that $\mathbb{P}^n$, smooth quadrics and products of Fano varieties are Fano varieties.
2. (A) Show that the blow-up of $\mathbb{P}^2$ at $r \leq 8$ points in general position is a Fano variety, and that the blow-up at $9$ general points is not, though it is rational.
3. (B) Let $X$ be a general smooth quartic threefold in $\mathbb{P}^4$ over $\mathbb{C}$. Granting that the lines on $X$ form a family of dimension $1$, show that they sweep out a surface, so a general point of $X$ lies on no line. Using Corollary P8.1.12, show that every component of $\operatorname{Hom}(\mathbb{P}^1, X)$ containing a conic has dimension at least $5$, and deduce that the conics on $X$ form a family of dimension at least $2$.
4. (B) Let $X$ be a smooth Fano variety over $\mathbb{C}$. Using Corollary P8.3.20 and Hodge theory, show that $H^i(X, \mathcal{O}_X) = 0$ for $i \geq 1$, and that $\operatorname{Pic}(X)$ is a finitely generated abelian group.
5. (B) Let $\varphi \colon S \to C$ be as in Example P8.3.24, with $C$ an elliptic curve. Show that $\varphi$ has a section, using Theorem P5.9.18, and compare with Theorem P8.3.21.
6. (C) Let $f \colon X \to Y$ be a Mori fibre space with $X$ smooth over $\mathbb{C}$. Show that the general fibre of $f$ is a Fano variety, and deduce from Corollary P8.3.22 that $X$ is rationally connected when $Y$ is.

### Lean

The repository does not define Fano varieties as such, but `MinimalModel.IsAmple` in `MinimalModel/Statements/Basic.lean` applied to `-A.P.KΔ` expresses ampleness of the anticanonical class, and the statement `MinimalModel.FanoTypeMDS` in `MinimalModel/Statements/Models.lean` uses it for pairs of Fano type. Mori fibre spaces, the output of the program that Example P8.3.24 and Exercise 6 concern, are `MinimalModel.IsMoriFibreSpace`. Rational connectedness, Theorem P8.3.19 and the theorem of Graber, Harris and Starr are not stated.

### Notes and history

Theorem P8.3.19 was proved in 1992 independently by Kollár, Miyaoka and Mori (KMM92b) and by Campana (Cam92); Kollár, Miyaoka and Mori also deduced that Fano varieties of a given dimension form a bounded family. The quotient construction in the proof gives, for every smooth projective $X$ in characteristic $0$, the maximal rationally connected fibration $X \dashrightarrow Z$, whose general fibres are rationally connected and which is universal with this property (KMM92a, Cam92; Kollár, Section IV.5 (Kol96)). The theorem of Graber, Harris and Starr (GHS03) shows that $Z$ is not uniruled. Theorem P8.3.21 generalizes Tsen's theorem, and over a base of dimension $1$ it is the geometric form of the statement that rationally connected varieties over the function field of a curve have rational points. In the minimal model program these results combine: a Mori fibre space $X \to Y$ has rationally connected general fibre, and $X$ is rationally connected when $Y$ is.
