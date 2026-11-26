---
title: Pairs and their singularities
nodes: []
sources: [KM98, Rei88, Kol87]
reads_with: [KM98:ch2]
requires: [P3, P8]
level: background
kind: background
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Pairs and their singularities

### Statement

In dimension 3 and higher the program cannot stay inside smooth varieties: a contraction of an extremal ray can make a singular variety (Section 1.4). So the program runs on a class of singular varieties, and it carries a boundary divisor along. This section gives the words. Let $X$ be a normal variety over $k$ of characteristic 0.

**Definition 1.1.6.** An *$\mathbb{R}$-divisor* on $X$ is a finite sum $\Delta = \sum d_i D_i$ of prime divisors with real coefficients. It is *$\mathbb{R}$-Cartier* if it is a sum $\sum r_j H_j$ of Cartier divisors with real coefficients, and $\mathbb{Q}$-Cartier if a multiple $m\Delta$ with $m \ge 1$ is Cartier. The variety $X$ is *$\mathbb{Q}$-factorial* if every Weil divisor is $\mathbb{Q}$-Cartier. A *pair* $(X, \Delta)$ is a normal variety $X$ and an effective $\mathbb{R}$-divisor $\Delta$ such that $K_X + \Delta$ is $\mathbb{R}$-Cartier.

Lean: `MinimalModel.Pair` (a canonical divisor $K$, an effective $\Delta$, and $K + \Delta$ $\mathbb{R}$-Cartier) and `MinimalModel.IsQFactorial`, in the project library.

A smooth variety is $\mathbb{Q}$-factorial, because every Weil divisor on it is Cartier. The quadric cone $xy = z^2$ is $\mathbb{Q}$-factorial and not factorial: a line $L$ through the vertex is not Cartier, but $2L$ is the Cartier divisor $\{x = 0\}$.

**Definition 1.1.7.** Let $(X, \Delta)$ be a pair and $f \colon Y \to X$ a proper birational morphism from a normal variety. Write

$$
K_Y + \Delta_Y = f^*(K_X + \Delta), \qquad f_* \Delta_Y = \Delta,
$$

with the same choice of canonical divisor on both sides. For a prime divisor $E$ on $Y$, the *discrepancy* is $a(E, X, \Delta) = -\operatorname{mult}_E \Delta_Y$, and the *log discrepancy* is $a(E, X, \Delta) + 1$. The pair is

1. *terminal* if $a(E, X, \Delta) > 0$ for every exceptional $E$ over $X$;
2. *canonical* if $a(E, X, \Delta) \ge 0$ for every exceptional $E$ over $X$;
3. *klt* (Kawamata log terminal) if $a(E, X, \Delta) > -1$ for every prime divisor $E$ over $X$;
4. *lc* (log canonical) if $a(E, X, \Delta) \ge -1$ for every prime divisor $E$ over $X$.

Here "every $E$ over $X$" means every prime divisor on every such $Y$. For a prime divisor $D$ of $X$ itself, $a(D, X, \Delta)$ is minus the coefficient of $D$ in $\Delta$, so klt needs the coefficients of $\Delta$ to be less than 1, and lc needs them at most 1. The terminal and canonical conditions are usually stated with $\Delta = 0$ or with coefficients less than 1.

Lean: `MinimalModel.IsTerminal`, `MinimalModel.IsCanonical`, `MinimalModel.IsKlt` and `MinimalModel.IsLc` in the project library, stated with the log discrepancy over all divisorial valuations.

The definitions are those of KM98, Definition 2.34, which also defines the plt and dlt pairs. The conditions are local on $X$. Each condition reduces to a finite check: it is enough to test the divisors of one log resolution (KM98, Chapter 2).

### Examples

The blow-up of a smooth point. Let $X$ be smooth of dimension $n$, $\Delta = 0$, and $f \colon Y \to X$ the blow-up of a point with exceptional divisor $E \cong \mathbb{P}^{n-1}$. Then $K_Y = f^* K_X + (n - 1) E$, so $a(E, X, 0) = n - 1$. Every smooth variety is terminal.

Cones over plane curves, computed in full. Let $C \subset \mathbb{P}^2$ be a smooth curve of degree $d$, and let $X$ be the affine cone over $C$. The blow-up of the vertex is a resolution $f \colon Y \to X$, where $Y$ is the total space of the line bundle $\mathcal{O}_C(-1)$ and the exceptional curve $E$ is the zero section, $E \cong C$. So $E^2 = \deg \mathcal{O}_C(-1) = -d$. The genus formula gives $2g(C) - 2 = d(d - 3)$, and adjunction on $Y$ gives

$$
K_Y \cdot E = 2g(C) - 2 - E^2 = d(d - 3) + d = d(d - 2).
$$

Write $K_Y = f^* K_X + aE$. The left side has degree $d(d - 2)$ on $E$, and $f^* K_X \cdot E = 0$. So $a \cdot (-d) = d(d - 2)$, and

$$
a(E, X, 0) = 2 - d.
$$

For $d = 1$ the cone is a plane, and $a = 1$. For $d = 2$ the cone is the quadric cone $xy = z^2$, the $A_1$ singularity, and $a = 0$: canonical and not terminal. For $d = 3$ the cone over a smooth plane cubic has $a = -1$: lc and not klt. For $d \ge 4$, $a < -1$ and the cone is not lc. The resolution $Y$ is a log resolution with one exceptional divisor, so these numbers decide the class.

A quotient singularity. The cyclic quotient $\frac{1}{3}(1, 1)$ is the cone over the twisted cubic. Its minimal resolution has one exceptional curve $E \cong \mathbb{P}^1$ with $E^2 = -3$. Adjunction gives $K_Y \cdot E = -2 + 3 = 1$, so $-3a = 1$ and $a = -\frac{1}{3}$. The singularity is klt and not canonical. In general $\frac{1}{n}(1, 1)$ has $E^2 = -n$ and $a = -\frac{n-2}{n}$, so it is klt for every $n$.

A boundary. Let $X = \mathbb{A}^2$ and $\Delta = L$ a line through the origin. Blow up the origin: $f^* L = L' + E$, so $K_Y + L' = f^*(K_X + L)$ and $a(E, X, L) = 0$. The divisor $L$ has $a(L, X, L) = -1$. So $(\mathbb{A}^2, L)$ is lc and not klt. With $\Delta = cL$ for $0 \le c < 1$ the pair is klt.

A hypothesis that fails. The discrepancy needs $K_X + \Delta$ to be $\mathbb{R}$-Cartier, or $f^*(K_X + \Delta)$ has no meaning. Let $X$ be the affine cone over $\mathbb{P}^1 \times \mathbb{P}^1$ embedded by $\mathcal{O}(1, 2)$. The canonical class of a cone over $(S, L)$ is $\mathbb{Q}$-Cartier only when $K_S$ is numerically a rational multiple of $L$. Here $K_S = \mathcal{O}(-2, -2)$ is not a multiple of $\mathcal{O}(1, 2)$. So $K_X$ is not $\mathbb{Q}$-Cartier, $(X, 0)$ is not a pair, and none of the four classes applies to it.

### Exercises

1. (A) Let $X$ be a smooth surface and $f \colon Y \to X$ the blow-up of a point $p$. For a smooth curve $D$ through $p$ and $0 \le c \le 1$, compute $a(E, X, cD)$. For which $c$ is $(X, cD)$ terminal near $p$?
2. (A) Show that the classes form a chain: terminal implies canonical, canonical with coefficients less than 1 implies klt, and klt implies lc.
3. (A) Let $D_1, D_2$ be two lines through the origin in $\mathbb{A}^2$. Compute the discrepancy of the exceptional curve of the blow-up of the origin for $(\mathbb{A}^2, c(D_1 + D_2))$. Find the largest $c$ for which this discrepancy is at least $-1$.
4. (B) Let $X = \frac{1}{n}(1, 1)$. Use the minimal resolution and adjunction to show that $a = -\frac{n-2}{n}$.
5. (B) Let $C = \{y^2 = x^3\} \subset \mathbb{A}^2$. Resolve $C$ by three blow-ups and show that $(\mathbb{A}^2, cC)$ is lc if and only if $c \le \frac{5}{6}$.

### Lean

The project library states all four classes with the log discrepancy $A_{X, \Delta}(v) = a + 1$ of a divisorial valuation $v$ of $k(X)$. The prime divisors of $X$ are among these valuations, and this gives the conditions on the coefficients of $\Delta$. Mathlib has the valuations (`Valuation`) but no discrepancies and no resolutions.

### Notes and history

Reid introduced canonical singularities in 1980 and terminal singularities in 1983, and found that the 3-fold program needs them. Kawamata and Shokurov brought in the boundary divisor and the klt and lc classes in the 1980s, and Kollár's survey (Kol87) fixed the words. The sign conventions differ in the literature: the discrepancy box of Volume 0 fixes the convention of the handbook. The quadric cone and the cusp are running examples: P0 Chapter 6 introduces the quadric cone, P8 Chapter 4 resolves the cusp, and Volume 4 computes the log canonical threshold $\frac{5}{6}$ of the cusp and gives the full theory of the singularities of pairs.
