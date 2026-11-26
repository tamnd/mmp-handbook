---
title: Curves and surfaces
nodes: [MMRP5RX4JJ, MM861R2D6G]
sources: [Rei97, Bea96, Har77]
reads_with: [Rei97:ch1, Bea96:ch2, Har77:V.5]
requires: []
level: guide
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Curves and surfaces

Birational geometry asks when two varieties have the same field of rational functions. Such varieties are *birational*. Chapter 5 defines the words. For example, $\mathbb{P}^2$ and the quadric surface $\mathbb{P}^1 \times \mathbb{P}^1$ are birational: the projection of the quadric from one of its points is a birational map to $\mathbb{P}^2$. They are not isomorphic, because two curves on $\mathbb{P}^2$ always meet, and the two rulings of the quadric do not.

**Curves.** For curves the question has a simple answer. Each birational class of curves contains exactly one smooth projective curve, up to isomorphism. The genus $g$ of this curve is the main invariant, and the degree of the canonical divisor $K$ is $2g - 2$. So there are three cases: $\mathbb{P}^1$, with $\deg K < 0$; the elliptic curves of Chapter 7, with $K = 0$; and the curves of genus at least 2, with $\deg K > 0$.

**Surfaces.** For surfaces one birational class contains many smooth projective surfaces. If $X$ is one and $p$ is a point of $X$, the blow-up $\mathrm{Bl}_p X$ of Chapter 5 is another. It replaces $p$ by a curve $E \cong \mathbb{P}^1$ with self-intersection $E^2 = -1$, a *$(-1)$-curve*. Castelnuovo's theorem says that this is the only way a $(-1)$-curve appears:

Node: MMRP5RX4JJ · Lean: `MinimalModel.Castelnuovo`

So a smooth projective surface can be made smaller by the contraction of its $(-1)$-curves. Each contraction lowers the rank of the Néron-Severi group by 1, so the process stops. The result is a *minimal surface*: a surface with no $(-1)$-curve. The canonical divisor tells where the process ends. The program for surfaces, in the form of Mori, says that each smooth projective surface $X$ has a birational morphism to a surface $Y$ such that one of two things holds:

- $K_Y$ is nef, that is $K_Y \cdot C \ge 0$ for every curve $C$ on $Y$; then $Y$ is the unique minimal model of $X$;
- $Y$ is $\mathbb{P}^2$, or $Y$ maps to a curve and each fibre is $\mathbb{P}^1$; then $-K_Y$ is positive on the fibres, and $Y$ is a *Mori fibre space*.

Node: MM861R2D6G · Lean: `MinimalModel.SurfaceMMP`

In the second case $X$ is covered by rational curves, and the surface $Y$ is not unique: both $\mathbb{P}^2$ and $\mathbb{P}^1 \times \mathbb{P}^1$ are ends of the program for the blow-up of $\mathbb{P}^2$ at two points.

### Exercises

1. (A) The blow-up $\pi \colon X \to \mathbb{P}^2$ at a point $p$ has $K_X = \pi^* K_{\mathbb{P}^2} + E$ and $K_{\mathbb{P}^2} = -3H$, with $H$ a line. Use $E^2 = -1$ and $\pi^*H \cdot E = 0$ to show that $K_X \cdot E = -1$.
2. (A) Let $\ell$ be the strict transform on $X$ of a line through $p$. Use $\pi^*H = \ell + E$ to show that $\ell^2 = 0$ and $K_X \cdot \ell = -2$.
3. (A) Show that $K$ of a smooth plane curve of degree $d$ has degree $d(d - 3)$, given the adjunction formula $K_C = (K_{\mathbb{P}^2} + C)|_C$. Which degrees give the three cases of the curves?
