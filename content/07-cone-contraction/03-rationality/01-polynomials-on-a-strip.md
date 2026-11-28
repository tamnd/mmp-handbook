---
title: Polynomials vanishing on a strip
nodes: []
sources: [KM98, Kaw84, KMM87]
reads_with: [KM98:3.5, KMM87:ch4]
requires: []
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Polynomials vanishing on a strip

### Statement

For a real number $r > 0$ and an integer $a \ge 1$, the *strip* is the set of $(x, y) \in \mathbb{Z}^2$ with $0 < ay - rx < 1$. A rational number $r > 0$ is written $r = u/v$ with $u, v$ coprime positive integers, and $v$ is its denominator.

**Lemma 7.3.1 (polynomials vanishing on a strip).** Let $n \ge 0$ and $a \ge 1$ be integers, $r > 0$ and $x_0$ real numbers, and $P \in \mathbb{R}[x, y]$ a polynomial of degree at most $n$. Suppose that $P(x, y) = 0$ for every $(x, y) \in \mathbb{Z}^2$ with $x \ge x_0$ and $0 < ay - rx < 1$. If $r$ is irrational, or if $r = u/v$ with $v > a(n + 1)$, then $P = 0$.

Lean: not yet in Lean.

Equivalently, a nonzero polynomial of degree at most $n$ that vanishes on the strip far out forces $r = u/v$ with $v \le a(n + 1)$. Section 2 uses the lemma in this form, with the lattice points of the strip parametrizing divisors $pH + qa(K_X + \Delta)$ that are not nef.

### Proof in words

A polynomial of degree at most $n$ that vanishes at $n + 1$ points of a line vanishes on the line, and then the linear equation of the line divides it. So it suffices to find $n + 1$ distinct parallel lines, each containing $n + 1$ lattice points of the strip with $x \ge x_0$. If $r = u/v$, the values of $avy - ux$ on $\mathbb{Z}^2$ are the multiples of $g = \gcd(a, u) \le a$, and the strip is $0 < avy - ux < v$; when $v > a(n + 1)$ the $n + 1$ lines $avy - ux = kg$, $1 \le k \le n + 1$, lie in it, and each has infinitely many lattice points. If $r$ is irrational, Dirichlet's theorem gives a lattice vector $w$ along which $ay - rx$ changes by a tiny $\delta \neq 0$, so the strip contains $n + 1$ consecutive points of many lines in direction $w$, and the density of $rx$ modulo $a$ gives infinitely many such lines.

### Examples

**Example 7.3.2 (the bound is sharp).** Let $a = 1$ and $r = 1/(n + 1)$. The strip is $0 < (n + 1) y - x < n + 1$, and its lattice points lie on the $n$ lines $(n + 1) y - x = k$, $1 \le k \le n$. The nonzero polynomial
$$P(x, y) = \prod_{k=1}^{n} \bigl( (n + 1) y - x - k \bigr)$$
of degree $n$ vanishes on the strip, and $v = n + 1 = a(n + 1)$. So the bound of Lemma 7.3.1 cannot be improved for $a = 1$. Example 7.3.6 realizes it geometrically on $\mathbb{P}^n$.

**Example 7.3.3 (an irrational slope).** Let $a = 1$, $r = \sqrt{2}$ and $n = 1$. The vector $w = (5, 7)$ has $7 - 5\sqrt{2} \approx -0.071$, so $y - \sqrt{2} x$ decreases by about $0.071$ along $w$. A lattice point $z$ of the strip with $y - \sqrt{2} x \in (0.1, 1)$ and its translate $z + w$ both lie in the strip, so a linear polynomial vanishing on the strip vanishes on the line through $z$ in direction $w$. The points $(1, 2)$ and $(2, 3)$ have values $0.586$ and $0.172$ and lie on different lines in direction $w$, so the polynomial has two non-proportional linear factors and is $0$.

### Proof

Every nonzero real polynomial of degree at most $n$ in one variable has at most $n$ roots. If $\ell$ is a line in $\mathbb{R}^2$ through a point $z$ with direction $w$, and $P$ vanishes at $n + 1$ distinct points of $\ell$, then $t \mapsto P(z + t w)$ has $n + 1$ roots, so $P$ vanishes on $\ell$. A polynomial vanishing on the zero set of a linear polynomial $\lambda$ is divisible by $\lambda$, by division with remainder in the variable along which $\lambda$ is monic. Distinct parallel lines have non-proportional equations, so if $P$ vanishes on $n + 1$ distinct parallel lines, the product of their equations, of degree $n + 1$, divides $P$, and $P = 0$.

*The rational case.* Let $r = u/v$ with $v > a(n + 1)$. Then $ay - rx = (avy - ux)/v$, and the strip is $0 < avy - ux < v$. Put $g = \gcd(av, u)$; since $\gcd(u, v) = 1$, $g = \gcd(a, u) \le a$. For $1 \le k \le n + 1$ we have $0 < kg \le (n + 1) a < v$, so the line $\ell_k \colon avy - ux = kg$ lies in the strip. It contains a lattice point $(x_k, y_k)$, since $kg$ is a multiple of $\gcd(av, u)$, and with it all the points $(x_k + t\, av/g, \; y_k + t\, u/g)$, $t \in \mathbb{Z}$, whose first coordinates tend to $+\infty$ as $t \to \infty$. So $P$ vanishes at infinitely many points of each $\ell_k$, hence on the $n + 1$ parallel lines $\ell_1, \dots, \ell_{n+1}$, and $P = 0$.

*The irrational case.* Let $r$ be irrational. By Dirichlet's approximation theorem, for $N > 2a(n + 1)$ there are integers $1 \le v_1 \le N$ and $v_2$ with $|v_1 (r/a) - v_2| < 1/N$. Dividing $(v_1, v_2)$ by its greatest common divisor, assume it is primitive, which only decreases both sides. Put $w = (v_1, v_2)$ and $\delta = a v_2 - r v_1$. Then $\delta \neq 0$ since $r$ is irrational, and $|\delta| < a/N < 1/(2(n + 1))$. Let $I = (n|\delta|, 1 - n|\delta|)$, an open interval of positive length. If $z = (x, y) \in \mathbb{Z}^2$ has $x \ge x_0$ and $ay - rx \in I$, then for $0 \le t \le n$ the point $z + t w$ has value $ay - rx + t\delta \in (0, 1)$ and first coordinate $x + t v_1 \ge x_0$. So $n + 1$ points of the line $z + \mathbb{R} w$ lie in the strip with first coordinate at least $x_0$, and $P$ vanishes on this line.

It remains to find infinitely many such lines. Since $r/a$ is irrational, the numbers $-rx$ modulo $a\mathbb{Z}$, for integers $x \ge x_0$, are dense in $\mathbb{R}/a\mathbb{Z}$ (Kronecker). So for infinitely many integers $x \ge x_0$ there is $y$ with $ay - rx \in I$, which gives infinitely many points $z$. Two of them lie on the same line in direction $w$ only if they differ by $t w$ with $t \in \mathbb{Z}$, since $w$ is primitive, and then their values differ by $t \delta$, so $|t| < 1/|\delta|$. So each line contains finitely many of the points $z$, there are infinitely many distinct parallel lines on which $P$ vanishes, and $P = 0$.

### Exercises

1. (A) For $a = 2$, $n = 1$ and $r = 1/2$, show that the strip lies on the single line $4y - x = 1$, so the nonzero linear polynomial $4y - x - 1$ vanishes on it, and check that $v = 2 \le a(n + 1)$. Do the same for $r = 1/4$ and show that no nonzero linear polynomial vanishes on the strip.
2. (A) For $a = 1$, $n = 2$ and $r = 2/5$, show that every polynomial of degree at most $2$ vanishing on the strip is $0$.
3. (A) Show that for $a = 1$ and $r = 1$ the strip contains no lattice points, so every polynomial vanishes on it. Explain why this is consistent with Lemma 7.3.1.
4. (B) Show that for rational $r = u/v$ the strip lies on exactly $\lceil v/g \rceil - 1$ lines in direction $(av, u)$, with $g = \gcd(a, u)$, and find the least degree of a nonzero polynomial vanishing on it.
5. (B) Replace the strip by $0 < ay - rx < \varepsilon$ for some $0 < \varepsilon \le 1$, and find the resulting bound on $v$.
6. (C) Prove the analogue of Lemma 7.3.1 in three variables: a polynomial of degree at most $n$ vanishing on the lattice points of $\{ x \ge x_0, \; 0 < a z - r_1 x - r_2 y < 1 \}$ with $r_1/a$ irrational is $0$.

### Lean

The lemma is elementary, but it is not yet in Lean, and the library has no statement of the rationality theorem it serves.

### Notes and history

The lemma is the arithmetic step in the proof of KM98, Theorem 3.5, and it goes back to Kawamata's proof of the rationality theorem (Kaw84) and its account in KMM87. The irrational case uses only that the strip contains $n + 1$ consecutive points of infinitely many parallel lines, and the rational case is where the bound $a(n + 1)$ comes from.
