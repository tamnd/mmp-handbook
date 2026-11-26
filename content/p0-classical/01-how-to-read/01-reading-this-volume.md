---
title: Reading this volume
nodes: []
sources: [Rei88, Sha13, Har92]
reads_with: [Rei88:ch0, Sha13:ch1]
requires: []
level: guide
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Reading this volume

P0 assumes undergraduate algebra and topology: groups, rings and fields, polynomial rings, the quotient of a ring by an ideal, a first idea of a field extension, and the definition of a topological space. It does not assume commutative algebra beyond that. When a proof needs a result of commutative algebra, the text states it, proves it when the proof is short, and else points to P1.

P0 works over an algebraically closed field $k$. Each chapter says so at its start. The field $\mathbb{C}$ is the main example, and a picture over $\mathbb{R}$ is often a good guide. Characteristic 0 is needed only in a few places, and the text says where.

The volume follows three texts: Reid's *Undergraduate algebraic geometry* (Rei88), the first volume of Shafarevich's *Basic algebraic geometry* (Sha13), and Harris's *Algebraic geometry: a first course* (Har92). The front matter of each section names the chapters of these books that read in parallel. A student who reads Reid alongside P0 has the best match.

Chapters 3 to 8 are a textbook course. Each section has six parts: the statement with full proofs, the proof in words, examples, exercises, the Lean part and notes. Each definition has two examples. The exercises have grades: (A) is routine, and (B) needs an idea. A chapter has 15 to 30 exercises. Chapters 1 and 2 are a guide and have no proofs.

Three examples of P0 return in the program volumes, so the reader should know them well:

- the quadric cone $xy = z^2$ of Chapter 6, the singularity $A_1$ and the quotient $\frac12(1,1)$;
- the cuspidal cubic $y^2 = x^3$ of Chapter 7, which P8 resolves and whose log canonical threshold Volume 4 computes;
- the cubic surfaces and their 27 lines of Chapter 8, which are the del Pezzo surfaces of degree 3 in Volumes 2, 6, 7, 12 and 14.

After P0, a reader goes on to P1 (commutative algebra). A reader who knows Hartshorne Chapters II, III and V reads only Chapters 1 and 2 of P0 and takes the fast path. Volume 0 Chapter 1 gives all the paths.

| Path | Chapters of P0 |
|---|---|
| Full | all |
| Fast | Ch. 1 and 2 |
| Surfaces first | all |
| Toric first | Ch. 1 to 4 |

### Exercises

1. (A) Find the chapter of Reid's book that reads with P0 Chapter 6, and the chapter that reads with P0 Chapter 8.
