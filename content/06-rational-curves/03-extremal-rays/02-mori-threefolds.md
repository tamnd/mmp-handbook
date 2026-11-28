---
title: Extremal contractions of smooth threefolds
nodes: []
sources: [Mor82, KM98, Deb01, MM81]
reads_with: [Mor82:all, KM98:1.32, Deb01:ch7]
requires: [P5.10, P8.12, 1.5, 6.2]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Extremal contractions of smooth threefolds

### Statement

Let $X$ be a smooth projective threefold over $\mathbb{C}$, $R$ a $K_X$-negative extremal ray and $\varphi \colon X \to Y$ its contraction, which exists by the contraction theorem (Volume 7). By Corollary 6.3.4, $\varphi$ is either divisorial or of fibre type.

**Theorem 6.3.9 (Mori's classification, cited).** Exactly one of the following holds.

1. ($E$, divisorial.) $\varphi$ is birational, and $\operatorname{Exc}(\varphi)$ is an irreducible divisor $E$. Then one of:
   - (E1) $Y$ is smooth and $\varphi$ is the blow-up of a smooth curve $C \subseteq Y$;
   - (E2) $Y$ is smooth and $\varphi$ is the blow-up of a point, with $E \cong \mathbb{P}^2$ and $\mathcal{O}_E(E) \cong \mathcal{O}(-1)$;
   - (E3) $E \cong \mathbb{P}^1 \times \mathbb{P}^1$ with $\mathcal{O}_E(E) \cong \mathcal{O}(-1, -1)$, contracted to an ordinary double point $x y - z w = 0$;
   - (E4) $E$ is a quadric cone in $\mathbb{P}^3$ with $\mathcal{O}_E(E) \cong \mathcal{O}_E(-1)$, contracted to a double point $x y - z^2 - w^3 = 0$;
   - (E5) $E \cong \mathbb{P}^2$ with $\mathcal{O}_E(E) \cong \mathcal{O}(-2)$, contracted to the point $\frac12(1, 1, 1)$.
2. ($C$, conic bundles.) $\dim Y = 2$, $Y$ is smooth and every fibre is a conic in $\mathbb{P}^2$: (C1) some fibre is singular, or (C2) $\varphi$ is a $\mathbb{P}^1$-bundle.
3. ($D$, del Pezzo fibrations.) $\dim Y = 1$, $Y$ is a smooth curve and the general fibre is a del Pezzo surface $F$ with $\rho(X/Y) = 1$: (D1) $K_F^2 \le 6$; (D2) $F$ is a quadric surface; (D3) $\varphi$ is a $\mathbb{P}^2$-bundle.
4. ($F$.) $Y$ is a point, $\rho(X) = 1$ and $X$ is a Fano threefold.

Lean: not yet in Lean.

**Proposition 6.3.10 (the lengths).** In the cases of Theorem 6.3.9 the length $\ell(R)$ is $1$ for E1, E3, E4, E5, C1 and D1; $2$ for E2, C2 and D2; $3$ for D3; and at most $4$ in case F, with $\ell(R) = 4$ for $X = \mathbb{P}^3$.

Lean: not yet in Lean.

**Proposition 6.3.11 (the inequality on threefolds).** In every case of Theorem 6.3.9, $\dim E + \dim F \ge 2 + \ell(R)$ for a fibre $F$ through a point of a minimal curve. It is an equality exactly in the cases E1, E2, C2, D3, and in case F for $\mathbb{P}^3$.

Lean: not yet in Lean.

### Proof in words

The classification is Mori's (Mor82), cited here. Its proof starts from Corollary 6.3.4, which rules out small contractions, and studies the exceptional divisor through its minimal curves: the restriction $-E|_E$ is ample, and adjunction relates $K_E$ to $K_X$ and $E$. The lengths then follow by adjunction: for a curve $\Gamma$ in $E$, $-K_X \cdot \Gamma = -K_E \cdot \Gamma + E \cdot \Gamma$, and for a curve in a fibre $F$ of a fibre type contraction, $-K_X \cdot \Gamma = -K_F \cdot \Gamma$, since the normal bundle of a general fibre is trivial. The inequality is then a table.

### Examples

**Example 6.3.12 (type E3: the cone over a quadric surface).** Let $Y_0 \subseteq \mathbb{A}^4$ be the cone $x y - z w = 0$ over a smooth quadric surface, and $Y$ a projective threefold with one such singular point. The blow-up of the vertex has exceptional divisor $E \cong \mathbb{P}^1 \times \mathbb{P}^1$ with normal bundle $\mathcal{O}(-1, -1)$. For a ruling $f$, $-K_E \cdot f = 2$ and $E \cdot f = -1$, so $-K_X \cdot f = 1$. The two rulings have the same class in $X$ when $\rho(X/Y) = 1$, and Proposition P8.12.3 gives $K_X = \varphi^* K_Y + E$, a discrepancy of $1$.

**Example 6.3.13 (type E5: the Veronese cone).** Let $X = \mathbb{P}(\mathcal{O} \oplus \mathcal{O}(2))$ over $\mathbb{P}^2$, with the negative section $E \cong \mathbb{P}^2$, $\mathcal{O}_E(E) \cong \mathcal{O}(-2)$. The morphism given by the tautological bundle contracts $E$ to the vertex of the cone over the Veronese surface, the singularity $\frac12(1, 1, 1)$. A line $e \subseteq E$ has $-K_X \cdot e = 3 - 2 = 1$, and $K_X = \varphi^* K_Y + \tfrac12 E$, the discrepancy $\frac12$ of Example P8.12.13. The other ray of $X$ is the $\mathbb{P}^1$-bundle over $\mathbb{P}^2$, of type C2 and length $2$.

**Example 6.3.14 (types C1, C2, D1 and E1).** Let $X \subseteq \mathbb{P}^2 \times \mathbb{P}^2$ be a general divisor of bidegree $(2, 1)$, with $\rho(X) = 2$ by the Lefschetz theorem. Its equation is quadratic in the first variables, so the projection to the second factor is a conic bundle whose discriminant, the determinant of a symmetric $3 \times 3$ matrix of linear forms, is a plane cubic: type C1. The equation is linear in the second variables, so the projection to the first factor has lines as fibres, and for a general divisor it is a $\mathbb{P}^1$-bundle: type C2. A general divisor of bidegree $(1, 3)$ in $\mathbb{P}^1 \times \mathbb{P}^3$ is a fibration in cubic surfaces over $\mathbb{P}^1$, of type D1, and its projection to $\mathbb{P}^3$ is the blow-up of the curve $\{ f = g = 0 \}$ cut out by the two cubics of the equation $s f + t g = 0$, of type E1.

### Proof

*Proposition 6.3.10.* In case E1, a fibre $f \cong \mathbb{P}^1$ of $E \to C$ has $\mathcal{O}_E(E) \cdot f = -1$ and $-K_E \cdot f = 2$, so $-K_X \cdot f = -K_E \cdot f + E \cdot f = 1$ by adjunction, $K_E = (K_X + E)|_E$. In case E2, a line $e$ has $-K_X \cdot e = 3 - 1 = 2$. In case E3, a ruling has $2 - 1 = 1$, as in Example 6.3.12. In case E4, $E$ is a normal Gorenstein surface with $K_E = \mathcal{O}_E(-2)$ by adjunction in $\mathbb{P}^3$, and a ruling $r$ through the vertex has $\mathcal{O}_E(1) \cdot r = 1$, so $-K_X \cdot r = 2 - 1 = 1$. In case E5, a line has $3 - 2 = 1$. In each case the curves contracted by $\varphi$ are the curves in the fibres of $E \to \varphi(E)$: the fibres $f$ in case E1 and the curves of $E$ in the other cases. In cases E2 to E5, $N_1(E)$ has rank $1$ after identifying the two rulings in case E3, and every curve of $E$ is numerically a positive integral multiple of the curve used, so these values are the lengths.

In the fibre type cases, a general fibre $F$ is smooth with trivial normal bundle, so $K_F = K_X|_F$ and $-K_X \cdot \Gamma = -K_F \cdot \Gamma$ for $\Gamma \subseteq F$. In case C2, a fibre is a smooth conic with $-K_F = 2$. In case C1, a singular fibre is $\ell_1 + \ell_2$, the class of a conic is $[\ell_1] + [\ell_2]$ with $-K_X \cdot (\ell_1 + \ell_2) = 2$, and both summands are positive integers, so $-K_X \cdot \ell_i = 1$. In case D3, a line in a fibre $\mathbb{P}^2$ has $-K_F \cdot L = 3$. In case D2, a line on a smooth quadric fibre has $-K_F \cdot L = 2$. In case D1, $F$ is a del Pezzo surface of degree at most $6$, and it contains a line, a $(-1)$-curve $L$ with $-K_F \cdot L = 1$, by Theorem P5.10.5 and its analogues in other degrees. In each case the minimum over all rational curves in $R$ is the value given, since $-K_X$ takes positive integer values on $R$ and the values found are $1$, or the classes of all curves in fibres are multiples of the class found. In case F, Corollary 6.2.10 gives $\ell(R) \le 4$, and a line in $\mathbb{P}^3$ has $-K \cdot L = 4$.

*Proposition 6.3.11.* In case E, $\dim E = 2$. In E1, $\dim F = 1$ and $\ell = 1$: $3 = 3$. In E2, $\dim F = 2$ and $\ell = 2$: $4 = 4$. In E3, E4 and E5, $\dim F = 2$ and $\ell = 1$: $4 > 3$. In case C, $\dim E = 3$ and $\dim F = 1$: $4 > 3$ for C1 and $4 = 4$ for C2. In case D, $\dim F = 2$: $5 > 3$, $5 > 4$ and $5 = 5$ for D1, D2 and D3. In case F, $\dim E = \dim F = 3$, so $6 \ge 2 + \ell(R)$, with equality if and only if $\ell(R) = 4$, which happens for $\mathbb{P}^3$ and, by the theorem of Cho, Miyaoka and Shepherd-Barron (CMSB02), only for $\mathbb{P}^3$.

### Exercises

1. (A) Let $X = \operatorname{Bl}_C \mathbb{P}^3$ for a line $C$. Show that the ray contracted by $X \to \mathbb{P}^3$ is of type E1, with length $1$.
2. (A) Show that $\operatorname{Bl}_p \mathbb{P}^3$ has a ray of type E2 and a ray of type C2, and compute both lengths.
3. (B) In case E2, show that the discrepancy of $E$ over $Y$ is $2$, and in case E1 that it is $1$. Compare with the lengths, and with Example 1.5.15.
4. (B) Let $X \subseteq \mathbb{P}^1 \times \mathbb{P}^3$ be a smooth divisor of bidegree $(1, 2)$. Show that the projection to $\mathbb{P}^1$ is a quadric fibration and that the projection to $\mathbb{P}^3$ is the blow-up of a smooth curve, the base locus of a pencil of quadrics, so $X$ has a ray of type D2 and a ray of type E1.
5. (B) Show that in case E4 the two rulings of a smooth quadric degenerate to a single ruling through the vertex, so that the class of a ruling is well defined, and that $r^2 = \frac12$ on the cone.
6. (C) Let $X$ be a smooth projective threefold with a contraction of type E5 or E3. Show that $Y$ is not smooth, using the discrepancy of $E$: every exceptional divisor over a smooth point of a threefold has discrepancy at least $2$ by Proposition P8.13.4, and E3, E5 give $1$ and $\frac12$.

### Lean

Nothing in this section is in Lean. The library has `MinimalModel.ContractionTheorem`, which gives the morphism $\varphi$ in characteristic $0$ as a statement, and `MinimalModel.IsMoriFibreSpace` for the fibre type cases with $\rho(X/Y) = 1$.

### Notes and history

The classification is Mori's (Mor82, Theorem 3.3), and it is the first case of the minimal model program beyond surfaces: on a smooth threefold every step that is not a Mori fibre space is a divisorial contraction, but types E3, E4 and E5 lead out of the smooth category, which is why the program must allow terminal singularities. Mori and Mukai used the classification to list the Fano threefolds with $\rho \ge 2$ (MM81), $36$ families with $\rho = 2$. The case of length $4$ in case F characterizes $\mathbb{P}^3$; for the treatment followed here, see KM98, Theorem 1.32, and Debarre's Chapter 7 (Deb01).
