---
title: Readers and parts
nodes: []
sources: [KM98, Kol87]
reads_with: []
requires: []
level: guide
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Readers and parts

The handbook is the minimal model program (MMP) written as a set of textbooks. The MMP is the part of birational geometry that tries to find, in each birational class of projective varieties, a model that is as simple as possible. The model is either a *minimal model*, where the canonical divisor is nef, or a *Mori fibre space*, a fibration whose general fibre has ample anticanonical divisor.

The handbook has two parts.

- **The prerequisites, Volumes P0 to P8.** They teach the algebraic geometry that the MMP uses. P0 starts at classical varieties over an algebraically closed field. P8 ends at bend-and-break, resolution of singularities, toric varieties and the first discrepancies.
- **The program, Volumes 0 to 17.** Volume 0 is this guide. Volumes 1 to 8 are the classical theory, from divisors and cones to flips and the 3-fold MMP. Volumes 9 to 12 are the theory after 2006: the existence of minimal models for varieties of log general type, abundance and termination, characteristic $p$, and boundedness. Volumes 13 to 17 are research surveys and the open problems.

There are three kinds of reader.

- A student with a first course in algebra and topology starts at P0 and reads the P volumes in order.
- A student who knows Chapters II, III and V of Hartshorne, or the matching parts of Vakil, takes the fast path of Section 1.2 and starts at this volume.
- A working mathematician who does not read Lean uses the handbook for the status of a statement and for a proof in standard notation. Chapter 4 of this volume explains the status lines.

The handbook comes as PDF and EPUB volumes. The site <https://mmp.tamnd.com> has the same text in HTML at `/learn/`.

The handbook never proves a theorem twice. A program volume cites a prerequisite volume by number, for example "by Theorem P7.8.4". A result that a P volume uses without proof is a *black box*. Each black box has one row in the table of P0 Chapter 1, and the label "black box" at each use.

### Exercises

1. (A) Use Chapter 2 of this volume to find the volume that proves the existence of klt flips, and the volume that treats the MMP in characteristic $p$.
2. (A) A reader knows the Nullstellensatz and the Jacobian criterion but not sheaf cohomology. Find the first P volume and chapter that this reader must read.
