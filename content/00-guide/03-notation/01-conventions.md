---
title: Varieties and the base
nodes: []
sources: [KM98, Har77]
reads_with: [KM98:ch0]
requires: []
level: guide
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Varieties and the base

- **The field.** P0 works over an algebraically closed field $k$, and says so at the start of each chapter. From P3 on, $k$ is a field, and the text says when it must be algebraically closed or of characteristic 0. The program volumes 1 to 10 and 12 to 14 work in characteristic 0. Volume 11 treats characteristic $p$.
- **Varieties.** In P0 a variety is a classical object: an irreducible closed subset of $\mathbb{A}^n$ or $\mathbb{P}^n$, or an open subset of one, with its regular functions. From P3 on, a *variety* over $k$ is an integral separated scheme of finite type over $k$. A *curve* is a variety of dimension 1 and a *surface* a variety of dimension 2.
- **The base.** Every statement of the program is relative. A projective morphism $f \colon X \to Z$ is fixed, and positivity is measured on the curves that $f$ contracts. The absolute case is $Z = \operatorname{Spec} k$. From P3 on, a statement is written over a base $Z$ when the program needs the relative version.
- **Divisors.** A divisor is a Weil divisor, a finite formal sum of prime divisors. A $\mathbb{Q}$-divisor or $\mathbb{R}$-divisor has rational or real coefficients. $K_X$ is a canonical divisor of a normal variety $X$, defined up to linear equivalence.
- **Pairs.** A *pair* $(X, \Delta)$ is a normal variety $X$ and an effective $\mathbb{R}$-divisor $\Delta$ such that $K_X + \Delta$ is $\mathbb{R}$-Cartier. This is the convention of KM98 for log pairs, and the Lean structure `MinimalModel.Pair` has the same four parts: $K$, $\Delta$, $\Delta \ge 0$, and $K + \Delta$ $\mathbb{R}$-Cartier.
