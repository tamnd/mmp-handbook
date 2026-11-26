---
title: The program in one paragraph
nodes: [MMDZBZY2BV, MMP51FQ005, MMTJ3YNHTG, MMY4HT1Q8M, MMPTP8SV13]
sources: [KM98, BCHM10, Bir12]
reads_with: [KM98:ch3, Bir12:ch1]
requires: []
level: guide
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The program in one paragraph

Let $X$ be a normal projective variety over a field of characteristic 0, and let $(X, \Delta)$ be a klt pair (Chapter 3 of this volume defines the words). The *MMP conjecture* says this. There is a finite sequence of birational maps $X = X_0 \dashrightarrow X_1 \dashrightarrow \cdots \dashrightarrow X_m$, each a divisorial contraction or a flip of a $(K + \Delta)$-negative extremal ray, such that one of two things holds at the end. Either $K_{X_m} + \Delta_m$ is nef, and $(X_m, \Delta_m)$ is a *minimal model*, or there is a contraction $X_m \to Y$ with $\dim Y < \dim X_m$ and $-(K_{X_m} + \Delta_m)$ ample over $Y$, a *Mori fibre space*. The *abundance conjecture* adds that on a minimal model $K + \Delta$ is semiample, so that a multiple of it defines a morphism.

Each step of the program exists. The cone and contraction theorems give the extremal rays and their contractions:

Node: MMDZBZY2BV · Lean: `MinimalModel.ConeTheoremKlt`

The flips of klt pairs exist in all dimensions (Birkar, Cascini, Hacon and McKernan, BCHM10):

Node: MMP51FQ005 · Lean: `MinimalModel.KltFlips`

What is not known is that the program stops. Termination of flips is a theorem in dimension at most 3. In dimension 4 and higher it is an open conjecture in general, with special cases known (Section 2.4):

Node: MMTJ3YNHTG · Lean: `MinimalModel.Termination`

The existence of minimal models for lc pairs with $K + \Delta$ pseudo-effective, and abundance, are open in general in dimension 4 and higher:

Node: MMY4HT1Q8M · Lean: `MinimalModel.MinimalModelConj`

Node: MMPTP8SV13 · Lean: `MinimalModel.Abundance`

### The blow-up of a point of the plane

Let $X = \mathrm{Bl}_p \mathbb{P}^2$, with exceptional curve $E$. Then $E \cong \mathbb{P}^1$, $E^2 = -1$ and $K_X \cdot E = -1$, so $E$ spans a $K_X$-negative extremal ray, and its contraction is the blow-down $X \to \mathbb{P}^2$; on $\mathbb{P}^2$ the divisor $-K$ is ample, so the program ends at the Mori fibre space $\mathbb{P}^2 \to \mathrm{pt}$.

The other extremal ray of $X$ is spanned by the strict transform $\ell$ of a line through $p$. Here $\ell^2 = 0$ and $K_X \cdot \ell = -2$. Its contraction is the ruling $X \to \mathbb{P}^1$, which is a Mori fibre space at once. So the end of the program depends on the choice of the ray, and $X$ has no minimal model, because $K_X$ is not pseudo-effective.

### Exercises

1. (A) Check $K_X \cdot E = -1$ and $K_X \cdot \ell = -2$ on $X = \mathrm{Bl}_p \mathbb{P}^2$ from $K_X = \pi^* K_{\mathbb{P}^2} + E$, $\pi^* H = \ell + E$ and $E^2 = -1$.
