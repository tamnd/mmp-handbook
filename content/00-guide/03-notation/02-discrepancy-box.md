---
title: The discrepancy box
nodes: []
sources: [KM98]
reads_with: [KM98:2.3]
requires: []
level: guide
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The discrepancy box

Two conventions are in use for discrepancies: the discrepancy $a$ and the log discrepancy $a + 1$. Students mix them. The handbook prints this box on the first page of Volumes 4 to 17.

> For a projective birational $f \colon Y \to X$ and a pair $(X, \Delta)$, write $K_Y + \Delta_Y = f^*(K_X + \Delta)$ with $f_*\Delta_Y = \Delta$. For a prime divisor $E$ on $Y$, the *discrepancy* is $a(E, X, \Delta) = -\operatorname{mult}_E \Delta_Y$, and the *log discrepancy* is $a(E, X, \Delta) + 1$. The pair is terminal or canonical if $a > 0$ or $a \ge 0$ for every exceptional $E$ over $X$. It is klt or lc if $a > -1$ or $a \ge -1$ for every prime divisor $E$ over $X$, exceptional or not. For a divisor $E$ on $X$ itself, $a(E, X, \Delta)$ is minus the coefficient of $E$ in $\Delta$, so klt asks for coefficients less than 1 and lc for coefficients at most 1. The Lean code states the same conditions with the log discrepancy, over all divisorial valuations.

Two examples fix the signs.

- Let $X$ be a smooth surface, $\Delta = 0$, and $f \colon Y \to X$ the blow-up of a point with exceptional curve $E$. Then $K_Y = f^*K_X + E$, so $a(E, X, 0) = 1$ and the log discrepancy is 2. In dimension $n$ the same blow-up gives $a = n - 1$.
- Let $X = \mathbb{A}^2$ and $\Delta = L$ a line through the origin. Blow up the origin. Then $f^*L = L' + E$, with $L'$ the strict transform, so $K_Y + L' = f^*(K_X + L)$ and $a(E, X, L) = 0$. The divisor $L$ itself has $a(L, X, L) = -1$. So $(\mathbb{A}^2, L)$ is lc and not klt.

In Lean, `MinimalModel.IsKlt` asks that every coefficient of $\Delta$ is less than 1 and that every log discrepancy over a divisorial valuation is positive. `MinimalModel.IsLc` asks for coefficients at most 1 and log discrepancies at least 0. Testing all divisorial valuations, and not only the exceptional ones, is the reason for the condition on the coefficients.
