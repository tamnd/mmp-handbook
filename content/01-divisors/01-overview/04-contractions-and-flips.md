---
title: Contractions, flips and the program
nodes: [MMQ2K4RSHT, MMP51FQ005, MM3A98X8YR]
sources: [KM98, Mor88, Kol92, BCHM10, Bir12]
reads_with: [KM98:ch3, Bir12:ch1]
requires: [P7, P8]
level: background
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Contractions, flips and the program

### Statement

**Definition 1.1.11.** A *contraction* is a projective morphism $\varphi \colon X \to Z$ of normal varieties with $\varphi_* \mathcal{O}_X = \mathcal{O}_Z$. Then $\varphi$ is surjective with connected fibres. A contraction is *extremal* if the classes of the curves that it contracts span one ray of $\overline{NE}(X)$.

Lean: `MinimalModel.IsContraction` and `MinimalModel.IsExtremalContraction`, in the project library.

**Theorem 1.1.12 (Contraction theorem).** Let $(X, \Delta)$ be a projective klt pair and $R$ a $(K_X + \Delta)$-negative extremal ray of $\overline{NE}(X)$. Then there is a unique contraction $\varphi_R \colon X \to Z$ such that a curve $C \subset X$ maps to a point if and only if $[C] \in R$. A line bundle $L$ on $X$ with $L \cdot R = 0$ is the pullback of a line bundle on $Z$.

Node: MMQ2K4RSHT

**Definition 1.1.13.** Let $X$ be $\mathbb{Q}$-factorial and $\varphi_R \colon X \to Z$ as above. Then $\rho(Z) = \rho(X) - 1$, and $\varphi_R$ has one of three types.

1. *Fibre type*: $\dim Z < \dim X$. Then $-(K_X + \Delta)$ is ample over $Z$, and $\varphi_R$ is a *Mori fibre space*.
2. *Divisorial*: $\varphi_R$ is birational and its exceptional set is a prime divisor. Then $Z$ is $\mathbb{Q}$-factorial, $(Z, \varphi_* \Delta)$ is klt, and the program goes on with $Z$.
3. *Small*: $\varphi_R$ is birational and its exceptional set has codimension at least 2.

Lean: `MinimalModel.IsMoriFibreSpace` and `MinimalModel.MMPStepData` (a step is a divisorial contraction or a flip), in the project library.

In the small case $K_Z + \varphi_* \Delta$ is not $\mathbb{R}$-Cartier. Suppose it is. Then $\varphi^*(K_Z + \varphi_*\Delta)$ and $K_X + \Delta$ agree outside the exceptional set, which has codimension at least 2, so they are equal. For a curve $C$ with $[C] \in R$ this gives $(K_X + \Delta) \cdot C = \varphi^*(K_Z + \varphi_* \Delta) \cdot C = 0$, because $\varphi$ maps $C$ to a point. This is a contradiction. So the program cannot go on with $Z$, and it needs a new model.

**Definition 1.1.14.** Let $\varphi \colon X \to Z$ be a small $(K_X + \Delta)$-negative extremal contraction, a *flipping contraction*. A *flip* of $\varphi$ is a small contraction $\varphi^+ \colon X^+ \to Z$ such that $K_{X^+} + \Delta^+$ is $\mathbb{R}$-Cartier and ample over $Z$, where $\Delta^+$ is the strict transform of $\Delta$. The birational map $X \dashrightarrow X^+$ is also called the flip.

Lean: `MinimalModel.IsFlip`, in the project library.

The flip is unique when it exists. For a $\mathbb{Q}$-divisor $\Delta$, $X^+ = \operatorname{Proj}_Z \bigoplus_{m \ge 0} \varphi_* \mathcal{O}_X(\lfloor m(K_X + \Delta) \rfloor)$, so it exists if and only if this sheaf of algebras is finitely generated.

**Theorem 1.1.15 (Existence of klt flips).** Let $(X, \Delta)$ be a projective klt pair and $\varphi \colon X \to Z$ a flipping contraction. Then the flip of $\varphi$ exists.

Node: MMP51FQ005 · Lean: `MinimalModel.KltFlips`

**Theorem 1.1.16 (Flips of 3-folds).** The flips of 3-fold klt pairs exist.

Node: MM3A98X8YR

The program for a $\mathbb{Q}$-factorial klt pair $(X, \Delta)$ is the loop below.

1. If $K_X + \Delta$ is nef, stop: $(X, \Delta)$ is a minimal model.
2. If not, the cone theorem gives a $(K_X + \Delta)$-negative extremal ray $R$, and the contraction theorem gives $\varphi_R$.
3. If $\varphi_R$ is of fibre type, stop: it is a Mori fibre space.
4. If $\varphi_R$ is divisorial, replace $(X, \Delta)$ by $(Z, \varphi_* \Delta)$ and go to 1.
5. If $\varphi_R$ is small, replace $(X, \Delta)$ by its flip $(X^+, \Delta^+)$ and go to 1.

Each step keeps the pair $\mathbb{Q}$-factorial and klt. The open question is whether the loop stops (Section 1.5).

### Proof in words

The contraction theorem is a consequence of the base point free theorem. The cone theorem and the rationality theorem give a nef Cartier divisor $L$ with $L^\perp \cap \overline{NE}(X) = R$. Then $mL - (K_X + \Delta)$ is ample, and the base point free theorem says that $|mL|$ is free for large $m$. The Stein factorization of the morphism of $|mL|$ is $\varphi_R$. The base point free theorem in turn comes from the Kawamata-Viehweg vanishing theorem (KM98, Chapter 3).

The existence of flips is much harder, and it was the main open problem of the program for a long time. Mori proved it for terminal 3-folds in 1988 by a classification of the extremal neighbourhoods (Mor88). Shokurov proved it for klt 3-folds by a reduction to pl flips (Kol92). Birkar, Cascini, Hacon and McKernan proved it in all dimensions (BCHM10), by an induction on dimension that proves the existence of flips together with the existence of minimal models for pairs with a big boundary. Hacon and McKernan gave the key step, the existence of pl flips in dimension $n$ from the program in dimension $n - 1$.

### Examples

A divisorial contraction, computed in full. Let $X = \mathrm{Bl}_p \mathbb{P}^3$ with exceptional divisor $E \cong \mathbb{P}^2$, and let $\ell \subset E$ be a line. Then $\mathcal{O}_E(E) = \mathcal{O}_{\mathbb{P}^2}(-1)$, so $E \cdot \ell = -1$. The formula $K_X = \pi^* K_{\mathbb{P}^3} + 2E$ gives $K_X \cdot \ell = 0 + 2(-1) = -2$. The class of $\ell$ spans a $K_X$-negative extremal ray, and its contraction is the blow-down $\pi \colon X \to \mathbb{P}^3$, which is divisorial. The other ray is spanned by the strict transform $f$ of a line through $p$; here $E \cdot f = 1$ and $K_X \cdot f = -4 + 2 = -2$, and its contraction is the projection $X \to \mathbb{P}^2$ from $p$, a $\mathbb{P}^1$-bundle and so a Mori fibre space.

A small contraction with $K$ trivial on the ray. Let $X$ be the total space of $\mathcal{O}_{\mathbb{P}^1}(-1) \oplus \mathcal{O}_{\mathbb{P}^1}(-1)$ and $C$ its zero section. The normal bundle of $C$ has degree $-2$, so adjunction gives $K_X \cdot C = -2 - (-2) = 0$. The contraction of $C$ is the cone $Z = \{xy = zw\} \subset \mathbb{A}^4$, and $K_Z$ is Cartier. The plane $\{x = z = 0\}$ is a Weil divisor on $Z$ that is not $\mathbb{Q}$-Cartier, so $Z$ is not $\mathbb{Q}$-factorial. The other small resolution $X^+$ of $Z$ replaces $C$ by another $\mathbb{P}^1$. This is the Atiyah flop. It is not a flip, because $K_X \cdot C = 0$: the hypothesis of $(K_X + \Delta)$-negativity fails, and $K_{X^+}$ is not ample over $Z$ but trivial over $Z$. The conclusion of the argument above also fails: $K_Z$ is Cartier here, because the ray is not $K_X$-negative.

A flip in the true sense needs dimension 3 and singularities, or dimension 4. Let $X$ be the total space of $\mathcal{O}_{\mathbb{P}^2}(-1)^{\oplus 2}$ and $P$ its zero section. Then $K_X \cdot \ell = -3 + 2 = -1$ for a line $\ell \subset P$. The contraction of $P$ is small, and its flip replaces $P \cong \mathbb{P}^2$ by $\mathbb{P}^1$, with $K_{X^+}$ positive on the new curve (Volume 3 computes it as a toric flip).

### Exercises

1. (A) In the example of $\mathrm{Bl}_p \mathbb{P}^3$, check that $\overline{NE}(X)$ is spanned by $\ell$ and $f$, and that $\rho$ drops by one under each of the two contractions.
2. (A) Show that a contraction $\varphi$ with $\varphi_* \mathcal{O}_X = \mathcal{O}_Z$ has connected fibres, and that $Z$ is normal if $X$ is.
3. (A) Show that the plane $\{x = z = 0\}$ in $\{xy = zw\}$ is not $\mathbb{Q}$-Cartier: show that its pullback to $X$ meets $C$ with a degree that is not zero, while a pulled back $\mathbb{Q}$-Cartier divisor meets $C$ in degree 0.
4. (B) Let $X$ be the total space of $\mathcal{O}_{\mathbb{P}^{a}}(-1)^{\oplus (b+1)}$, with zero section $P \cong \mathbb{P}^a$. Show that $K_X \cdot \ell = b - a$ for a line $\ell \subset P$. For which $a, b$ is the contraction of $P$ a flipping contraction, a flop, or the inverse of a flip?
5. (B) Show that the flip of a flipping contraction is unique, using the description of $X^+$ as a relative Proj.

### Lean

`MinimalModel.MMPStepData` holds one step of the program over a base $Z$: a $(K + \Delta)$-negative birational extremal contraction $f$, a small contraction $g$ from the next model with $K + \Delta$ ample over $Z$, and the strict transform of the boundary. For a divisorial contraction $g$ is the identity. `MinimalModel.KltFlips` asks for the existence of $g$ for a small $f$. The contraction theorem and the 3-fold flips are nodes of the map with no Lean statement yet. Mathlib has `AlgebraicGeometry.Proj` but no relative Proj of a sheaf of algebras.

### Notes and history

The contraction theorem is due to Kawamata and Shokurov (base point free theorem) in the 1980s. Reid named flips and saw that the program needs them. All three theorems of this section are theorems in the literature: Mori proved terminal 3-fold flips in 1988, Shokurov klt 3-fold flips in 1992, and BCHM10 klt flips in all dimensions. Birkar, and Hacon and Xu, extended the existence to lc flips (2012 to 2013). Volume 3 gives toric flips, where everything is explicit. Volume 8 gives the 3-fold flips and flops, with the Francia flip as the first example. Volume 9 gives BCHM.
