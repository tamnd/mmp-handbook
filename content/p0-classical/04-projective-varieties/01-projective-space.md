---
title: Projective space and homogeneous coordinates
nodes: []
sources: [Rei88, Har77, Har92, Sha13]
reads_with: [Rei88:ch5, Har77:I.2, Har92:lecture1, Sha13:ch1]
requires: [P0.3]
level: prereq
kind: background
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Projective space and homogeneous coordinates

### Statement

**Definition P0.4.1 (projective space).** The projective space of dimension $n$ over $k$ is the set $\mathbb{P}^n$ of lines through $0$ in $k^{n+1}$. Equivalently, $\mathbb{P}^n = (k^{n+1} \setminus \{0\}) / k^\times$, where $\lambda \in k^\times$ acts by scalar multiplication. The class of a vector $(a_0, \dots, a_n) \neq 0$ is written $[a_0 : \dots : a_n]$, and the $a_i$ are homogeneous coordinates of the point. So $[a_0 : \dots : a_n] = [\lambda a_0 : \dots : \lambda a_n]$ for every $\lambda \neq 0$.

Lean: Mathlib `Projectivization` (a definition, with notation `ℙ K V` and points `Projectivization.mk`).

**Example P0.4.2.** The projective line is $\mathbb{P}^1 = \{[1 : t] : t \in k\} \cup \{[0 : 1]\}$. The first part is a copy of $\mathbb{A}^1$, and $[0 : 1]$ is the point at infinity. The map $[a_0 : a_1] \mapsto a_1 / a_0$ identifies $\mathbb{P}^1$ with $k \cup \{\infty\}$.

**Example P0.4.3.** The projective plane is $\mathbb{P}^2 = \{[1 : x : y]\} \cup \{[0 : a : b]\}$. The first part is a copy of $\mathbb{A}^2$. The second part is the line at infinity, a copy of $\mathbb{P}^1$, and its points are the directions $[a : b]$ of lines in $\mathbb{A}^2$.

**Definition P0.4.4 (linear subspace).** A linear subspace of $\mathbb{P}^n$ of dimension $r$ is the set $\mathbb{P}(W)$ of lines in a linear subspace $W \subseteq k^{n+1}$ of dimension $r + 1$. A line is a linear subspace of dimension 1, and a hyperplane is one of dimension $n - 1$. A projective transformation is a map $\mathbb{P}^n \to \mathbb{P}^n$, $[v] \mapsto [Av]$, for an invertible matrix $A \in \mathrm{GL}_{n+1}(k)$.

Lean: not in Lean as stated; Mathlib has `Projectivization.map` for injective linear maps and the group `Matrix.GeneralLinearGroup`.

**Example P0.4.5.** The hyperplane $H_0 = \{x_0 = 0\}$ is $\mathbb{P}(W)$ for $W = \{v : v_0 = 0\}$. Its points are $[0 : a_1 : \dots : a_n]$, so $H_0$ is a copy of $\mathbb{P}^{n-1}$. In $\mathbb{P}^2$ the line through $[1 : 0 : 0]$ and $[0 : 1 : 0]$ is $\{x_2 = 0\}$.

**Example P0.4.6.** The matrix $\lambda I$ gives the identity of $\mathbb{P}^n$ for every $\lambda \neq 0$. So the group of projective transformations is $\mathrm{PGL}_{n+1}(k) = \mathrm{GL}_{n+1}(k)/k^\times$. On $\mathbb{P}^1$, in the coordinate $t = a_1/a_0$, these are the maps $t \mapsto (at + b)/(ct + d)$ with $ad - bc \neq 0$: the matrix with rows $(d, c)$ and $(b, a)$ sends $(1, t)$ to $(ct + d, at + b)$.

**Proposition P0.4.7 (standard charts).** For $i = 0, \dots, n$ let $U_i = \{[a] \in \mathbb{P}^n : a_i \neq 0\}$. Then $\mathbb{P}^n = U_0 \cup \dots \cup U_n$, and the map

$$\varphi_i \colon U_i \to \mathbb{A}^n, \qquad [a_0 : \dots : a_n] \mapsto \Big(\frac{a_0}{a_i}, \dots, \widehat{\frac{a_i}{a_i}}, \dots, \frac{a_n}{a_i}\Big)$$

is a bijection, where the hat means that the entry is left out. The complement $\mathbb{P}^n \setminus U_i$ is the hyperplane $\{x_i = 0\} \cong \mathbb{P}^{n-1}$.

Lean: not in Lean as stated; the scheme version is the cover of `AlgebraicGeometry.Proj` by basic open affines.

*Proof.* A vector $a \neq 0$ has some $a_i \neq 0$, so the $U_i$ cover $\mathbb{P}^n$. The ratios $a_j/a_i$ do not change when $a$ is multiplied by $\lambda \neq 0$, so $\varphi_i$ is well defined. The inverse sends $(b_1, \dots, b_n)$ to the point with $1$ in position $i$ and the $b_j$ in the other positions, in order. The last statement is the example of $H_0$ with the index $i$ in place of $0$. $\square$

**Proposition P0.4.8 (lines in the plane).** Two distinct lines in $\mathbb{P}^2$ meet in exactly one point. Through two distinct points of $\mathbb{P}^2$ there is exactly one line.

Lean: not in Lean as stated.

*Proof.* Lines in $\mathbb{P}^2$ are planes $W_1 \neq W_2$ in $k^3$. Then $W_1 + W_2 = k^3$, so $\dim (W_1 \cap W_2) = 2 + 2 - 3 = 1$, and $W_1 \cap W_2$ is one point of $\mathbb{P}^2$. Two distinct points are two lines $L_1 \neq L_2$ in $k^3$, and $L_1 + L_2$ is the only plane that contains both. $\square$

**Proposition P0.4.9 (frames).** Let $p_0, \dots, p_{n+1} \in \mathbb{P}^n$ be $n + 2$ points such that no $n + 1$ of them lie in a hyperplane. Then there is exactly one projective transformation that sends $p_i$ to $[e_i]$ for $i \leq n$ and $p_{n+1}$ to $[1 : 1 : \dots : 1]$.

Lean: not in Lean as stated.

*Proof.* Choose vectors $v_i$ with $p_i = [v_i]$. The vectors $v_0, \dots, v_n$ are a basis, so $v_{n+1} = \sum_{i \leq n} c_i v_i$. Each $c_i \neq 0$, because otherwise $v_{n+1}$ and the $v_j$ with $j \neq i$ lie in a hyperplane. The matrix $A$ with $A(c_i v_i) = e_i$ sends $p_i$ to $[e_i]$ and $v_{n+1}$ to $(1, \dots, 1)$. If $B$ is a second such matrix, then $C = BA^{-1}$ fixes each $[e_i]$, so $C$ is diagonal, and it fixes $[1 : \dots : 1]$, so $C$ is a scalar. So $B$ and $A$ give the same projective transformation. $\square$

### Examples

Two parallel lines in $\mathbb{A}^2$ meet at infinity in $\mathbb{P}^2$. The lines $y = 0$ and $y = 1$ in the chart $U_0$, with coordinates $x = x_1/x_0$ and $y = x_2/x_0$, are $\{x_2 = 0\}$ and $\{x_2 = x_0\}$ in $\mathbb{P}^2$. Their common point has $x_2 = x_0 = 0$, so it is $[0 : 1 : 0]$, the direction of the $x$-axis.

On $\mathbb{P}^1$ the frame proposition says that a projective transformation is fixed by the images of three distinct points. The cross ratio of four distinct points $p_1, p_2, p_3, p_4$ is the coordinate $t \in k \setminus \{0, 1\}$ of the image of $p_4$ under the transformation that sends $p_1, p_2, p_3$ to $\infty, 0, 1$. Two ordered sets of four points are related by a projective transformation if and only if they have the same cross ratio.

### Exercises

1. (A) Show that $[a_0 : a_1 : a_2] \mapsto [a_1 : a_0 : a_2]$ is a projective transformation of $\mathbb{P}^2$, and find its fixed points.
2. (A) Find the point of intersection of the lines $x_0 + x_1 + x_2 = 0$ and $x_0 - x_1 = 0$ in $\mathbb{P}^2$, and find the line through $[1 : 0 : 1]$ and $[0 : 1 : 1]$.
3. (A) Show that two distinct linear subspaces of dimension $r$ and $s$ in $\mathbb{P}^n$ meet when $r + s \geq n$. Show that two skew lines exist in $\mathbb{P}^3$.
4. (B) Let $k = \mathbb{F}_q$ be a finite field (here not algebraically closed). Count the points of $\mathbb{P}^n(\mathbb{F}_q)$, and check the answer against the decomposition $\mathbb{P}^n = \mathbb{A}^n \cup \mathbb{P}^{n-1}$.
5. (B) Let $p_i = [1 : t_i]$ for distinct $t_1, \dots, t_4 \in k$. Show that the cross ratio of $p_1, \dots, p_4$ is $(t_4 - t_2)(t_3 - t_1) / ((t_4 - t_1)(t_3 - t_2))$. If the cross ratio is $t$, find the six values that it takes when the four points are permuted.

### Lean

Mathlib has projective space as `Projectivization`, the type `ℙ K V` of lines in a vector space `V` over a division ring `K`, with points `Projectivization.mk`. It has no Zariski topology or variety structure on `ℙ K V`. The scheme version is `AlgebraicGeometry.Proj` of a graded ring, and $\mathbb{P}^n$ is the case of the polynomial ring with the grading by degree. The handbook uses these Mathlib names and adds no `MinimalModel` node here.

### Notes and history

Points at infinity entered geometry through perspective drawing. Desargues (1639) treated parallel lines as lines that meet at infinity, and Poncelet (1822) built projective geometry as a subject. Homogeneous coordinates are due to Möbius (1827) and Plücker (1830). The frame proposition is the fundamental theorem of projective geometry in its linear form. In this handbook $\mathbb{P}^n$ is the basic ambient space: every variety of the minimal model program is a closed subvariety of some $\mathbb{P}^n$, or a variety that is projective over a base.
