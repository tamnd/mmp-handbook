---
title: Reading a Lean statement
nodes: [MMRP5RX4JJ]
sources: [Har77]
reads_with: [Har77:V.5]
requires: []
level: guide
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Reading a Lean statement

The statements of tamnd/mmp-lean are definitions of type `Prop` in the namespace `MinimalModel`. A definition of type `Prop` is a proposition: it states a theorem and does not prove it. A proof is a term of that type, with its own name. Here is Castelnuovo's contraction theorem, which P5 proves and Volume 2 uses, as the Lean code states it, in the file `MinimalModel/Statements/LowDim.lean`:

```lean
def Castelnuovo : Prop :=
  ∀ A : PairModel k, A.IsSmoothSurface →
    ∀ (E : PrimeDivisor A.X) (hE : height E.1 = 1),
      A.I.dot (Divisor.toReal (Finsupp.single E 1)) ⟨E.1, hE⟩ = -1 →
      A.I.dot A.P.KΔ ⟨E.1, hE⟩ = -1 →
      ∃ (Y : NormalVariety k) (f : A.X.toScheme ⟶ Y.toScheme), Y.IsSmooth ∧ Y.dim = 2 ∧
        IsProjective Y ∧ f ≫ Y.str = A.X.str ∧ IsProper f ∧
        ∃ (p : Y.toScheme) (hp : IsClosed ({p} : Set Y.toScheme)), f.base E.1 = p ∧
          IsIso (f ∣_ ⟨{p}ᶜ, hp.isOpen_compl⟩)
```

Node: MMRP5RX4JJ · Lean: `MinimalModel.Castelnuovo`

Read it line by line.

- `PairModel k` is a structure with four fields: the variety `X` over the field `k`, a pair `P` on it, an intersection theory `I`, and a proof that `X` is projective. A structure is a record of data and proofs. `A.IsSmoothSurface` says that $X$ is smooth, of dimension 2, and that the boundary $\Delta$ of the pair is 0.
- `E` is a prime divisor of $X$, that is an irreducible curve. The hypothesis `hE` says that the generic point of $E$ has height 1, so $E$ has codimension 1.
- The next two lines are the hypotheses $E^2 = -1$ and $K_X \cdot E = -1$. `A.I.dot D C` is the intersection number of a divisor $D$ with a curve $C$. With $\Delta = 0$, `A.P.KΔ` is $K_X$.
- The conclusion asks for a smooth projective surface $Y$ and a proper morphism $f \colon X \to Y$ over $k$ (the equation `f ≫ Y.str = A.X.str`). The morphism maps $E$ to a closed point $p$ and is an isomorphism over $Y \setminus \{p\}$.

Hartshorne states the theorem for an algebraically closed field (Har77, V.5.7). The Lean statement asks only for a field. The section "Lean" of each theorem section reports such a difference. The hypotheses of a Lean statement have names, and a black box of the text is a named hypothesis of the Lean code. So the reader sees the same list in both places.

**The axioms.** The Lean command `#print axioms MinimalModel.Castelnuovo` lists the axioms that a declaration uses. For the statements of mmp-lean the list is `propext`, `Classical.choice` and `Quot.sound`, the standard axioms of Lean and Mathlib. A proof that adds an axiom, or that uses `sorry`, does not count as `proved`.

### Exercises

1. (A) In the Lean statement above, find the line that says that $f$ is a morphism over $k$, and the line that says that $f$ is an isomorphism over $Y \setminus \{p\}$.
2. (A) The statement does not say that $E$ is a smooth rational curve. Use the adjunction formula $2p_a(E) - 2 = E^2 + K_X \cdot E$ to show that the two hypotheses imply $p_a(E) = 0$.
