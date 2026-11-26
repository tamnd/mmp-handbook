---
title: The notation table
nodes: []
sources: [KM98, Laz04]
reads_with: [KM98:ch1, Laz04:ch1]
requires: []
level: guide
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The notation table

| Notation | Meaning |
|---|---|
| $D \equiv D'$ | numerical equivalence: $D \cdot C = D' \cdot C$ for every curve $C$ (over $Z$, for every curve that $f$ contracts) |
| $D \sim D'$, $D \sim_{\mathbb{Q}} D'$ | linear equivalence; $\mathbb{Q}$-linear equivalence, that is $mD \sim mD'$ for some integer $m > 0$ |
| $N^1(X/Z)$, $N_1(X/Z)$ | the real vector spaces of $\mathbb{R}$-Cartier divisors and of 1-cycles over $Z$, modulo numerical equivalence; they are dual by the intersection pairing |
| $\rho(X/Z)$ | the relative Picard number, $\dim N^1(X/Z)$ |
| $\overline{NE}(X/Z)$ | the closed cone in $N_1(X/Z)$ spanned by the classes of the curves that $f$ contracts |
| $\kappa(D)$ | the Iitaka dimension of $D$; $\kappa(X) = \kappa(K_X)$ is the Kodaira dimension |
| $\kappa_\sigma(D)$, also $\nu(D)$ | the numerical dimension of $D$ (Nakayama) |
| $X^- \dashrightarrow X^+$ | a flip: $K_{X^-}$ (or $K + \Delta$) is negative on the flipping curves and $K_{X^+}$ is positive on the flipped curves |
| $\frac1r(a_1, \dots, a_n)$ | the quotient of $\mathbb{A}^n$ by $\zeta \cdot (x_1, \dots, x_n) = (\zeta^{a_1} x_1, \dots, \zeta^{a_n} x_n)$, with $\zeta$ a primitive $r$-th root of unity |
| $\mathbb{F}_n$ | the Hirzebruch surface $\mathbb{P}(\mathcal{O}_{\mathbb{P}^1} \oplus \mathcal{O}_{\mathbb{P}^1}(-n))$, with a section of self-intersection $-n$ |
| $\mathrm{Bl}_p X$ | the blow-up of $X$ at the point $p$ |
| $\operatorname{mld}(x, X, \Delta)$ | the minimal log discrepancy at $x$: the infimum of the log discrepancies of the prime divisors over $X$ with centre $x$ |
| $\operatorname{lct}(X, \Delta; D)$ | the log canonical threshold: the largest $t$ such that $(X, \Delta + tD)$ is lc |

Example: $\frac12(1,1)$ is the quotient of $\mathbb{A}^2$ by $(x, y) \mapsto (-x, -y)$. Its invariant ring is $k[x^2, xy, y^2] \cong k[u, v, w]/(uw - v^2)$ when the characteristic of $k$ is not 2. It is the quadric cone of P0 Chapter 6, the $A_1$ singularity.

### Exercises

1. (A) Show that the quotient $\frac13(1,1)$ has invariant ring $k[x^3, x^2y, xy^2, y^3]$ when the characteristic of $k$ is not 3, and that it is the cone over the twisted cubic curve.
