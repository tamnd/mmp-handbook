---
title: The black boxes
nodes: []
sources: [Hir64, Kol07, Har66, Gro61, Ser56, SGA6, BDPP13, Kle66]
reads_with: [Kol07:ch3]
requires: []
level: guide
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The black boxes

A result that a P volume states without proof is a *black box*. The proof is long and does not teach a method that the program uses. The handbook states each black box with care, gives its reference, and writes "black box" at each use. In the Lean code a black box is a named hypothesis, a definition of type `Prop` that the theorems which use it take as an argument. It is never an axiom. So the list in the book and the list in the Lean code are the same.

| Black box | Statement in short | Reference | Stated in | Used in | Lean hypothesis |
|---|---|---|---|---|---|
| Hironaka's theorem | in characteristic 0, every variety has a resolution, and every pair a log resolution | Hir64; Kol07 | P8 Ch. 5 | Volumes 4, 5, 7, 9 and later | `MinimalModel.HasLogResolution` |
| Grothendieck duality | for a proper morphism $f$, the derived functor $Rf_*$ has a right adjoint $f^!$; for a projective variety over $k$, $f^!k$ is a dualizing complex | Har66 | P4 Ch. 9 | Volumes 4 and 5 | not yet named |
| Hilbert schemes | the Hilbert functor of a projective scheme is represented by a scheme, which is projective for each fixed Hilbert polynomial; the Hom functor is represented by an open subscheme of the Hilbert scheme of $X \times Y$ | Gro61 | P8 Ch. 1 | Volume 6, Volume 13 | not yet named |
| The Hodge theorem | on a compact Hermitian manifold, every Dolbeault class, and on a compact Riemannian manifold every de Rham class, has a unique harmonic representative, and the cohomology is finite dimensional | Huy05; Wel80 | P6 Ch. 4 | P6 Ch. 4 to 8, P7 | not yet named |
| GAGA | on a complex projective variety, analytic coherent sheaves are algebraic, with the same cohomology | Ser56 | P6 Ch. 7 | P7 Ch. 8, Volume 5 | not yet named |
| The theorem of the base | $N^1(X)$ is a finite dimensional real vector space for a projective variety $X$ | SGA6; Kle66 | P7 Ch. 2 | Volume 1, Volume 7 | `TheoremOfTheBase` (planned) |
| BDPP | a divisor is pseudo-effective if and only if it is nonnegative on every movable curve | BDPP13 | P7 Ch. 5 | Volume 1, Volume 10 | not yet named |

The theorem of the base has an elementary proof over $\mathbb{C}$ from the Lefschetz theorem on $(1,1)$ classes. The black box is the statement over any algebraically closed field. BDPP is stated in BDPP13 for complex projective manifolds. The handbook uses it in that form.

A row in the column "Lean hypothesis" with "not yet named" means that the Lean code does not use the result yet. The Lean name comes when a statement of the map needs it. `TheoremOfTheBase` is in the plan of the Lean code and not yet in tamnd/mmp-lean.
