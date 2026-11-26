---
title: The start
nodes: [MM0000000A]
sources: [Har77]
reads_with: [Har77:V.5]
requires: [P0.5, 2]
level: core
kind: theorem
status: reviewed
drafted_by: writer
reviewed_by: [reviewer]
---
## The start

### Statement

A $(-1)$-curve on a smooth projective surface is a curve $E \cong \mathbb{P}^1$ with $E^2 = -1$.

**Theorem (Castelnuovo).** A $(-1)$-curve on a smooth projective surface is the exceptional curve of the blow-up of a point of a smooth projective surface.

Node: MM0000000A · Lean: `MinimalModel.Castelnuovo`

### Proof in words

The linear system of a suitable divisor maps $E$ to a point.

### Examples

The blow-up of $\mathbb{P}^2$ at a point has one $(-1)$-curve.

*Proof.* See the source. $\square$

**Definition.** A surface is *minimal* when it has no $(-1)$-curve.

Lean: not in Lean.

### Exercises

1. (A) Compute $E^2$ for the blow-up of a point of $\mathbb{P}^2$.
2. (B) Show that $\mathbb{P}^2$ has no $(-1)$-curve.
3. (B) (M) Count the $(-1)$-curves on a cubic surface by computer.

### Lean

The statement is `MinimalModel.Castelnuovo`.

### Notes and history

Castelnuovo proved it.
