---
title: K-stability, moduli and Cremona groups
nodes: []
sources: []
reads_with: []
requires: ["12", "13", "14"]
level: research
kind: survey
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## K-stability, moduli and Cremona groups

Spec 11 lists "K-stability problems (Xu-Zhuang 2026)" and "Cremona groups" among the subjects of this volume. On 2026-11-26 the map has no node for either subject, and the records give little. This section reports what the records give and marks the rest.

### Statement

**Remark 17.4.7 (Claim C15: a K-polystable 5-fold with no cscK metric).** There is a smooth polarized 5-fold that is K-polystable and has no constant scalar curvature Kähler metric.

This is claimed by J. Liu (arXiv:2608.19301). The paper says that the example "was obtained using generative AI". The map has no node for it.

**Remark 17.4.8 (The open problems of the records).** The records name these problems of K-stability and moduli as open, or as not checked:

- the cscK form of the Yau-Tian-Donaldson conjecture (spec 01.8, with C15 and Trusiani);
- the KSBA moduli of stable pairs in characteristic $p$, which spec 01.8 marks "not checked in this session" [U].

### Proof in words

**What is known.** Spec 01.8 gives the state of moduli on 2026-11-26.

- K-moduli of Fano varieties are proper and projective (Liu, Xu and Zhuang, arXiv:2102.09405, Ann. of Math.) [P]. Blum, Liu, Xu and Zhuang (arXiv:2510.06197) give a second proof of properness that is purely birational [P].
- The Yau-Tian-Donaldson conjecture for log Fano pairs is a theorem [P]. For the cscK case, spec 01.8 points to C15 and to Trusiani (arXiv:2605.30063) [P]. The records do not say what Trusiani proves.
- The moduli of stable pairs (KSBA) is projective in characteristic 0 [S]. The reference is Kollár, "Families of Varieties of General Type" (CUP 2023). Spec 07 adds Birkar, "Moduli of algebraic varieties" (arXiv:2211.11237), for stable minimal models (row T10-14).
- The reference for K-stability is the book of Xu, "K-stability of Fano Varieties" (CUP, New Mathematical Monographs 50, April 2025) [S].

At ICM 2026, Z. Zhuang spoke on local volumes of klt singularities and K-stability, and K. Fujita on criteria for K-stability of Fano manifolds (spec 01.10, [S]).

**Xu-Zhuang 2026.** Spec 11 names "Xu-Zhuang 2026" as a spine of this volume and as the source of its K-stability problems. The records of the project do not say which paper this is: they give no title, no arXiv number and no paper record. Row T4-12 of spec 07 names Xu-Zhuang only for normalized volumes. So this report does not list the problems of that source.

**Cremona groups.** The records of the project do not say which problems on Cremona groups are open. Spec 11 lists the Jordan property of Cremona groups among the main theorems of Volume 12. Spec 01.10 lists the ICM 2026 talk of S. Zimmermann on algebraic groups of birational maps, for Volume 10 [S]. The records give nothing more.

### Examples

The first test case of C15 is the example itself. The records name no target for it: route R1 has no O-R1 target for C15, and the lab has no experiment for it. The records name no first test case for K-stability or for Cremona groups.

For moduli in characteristic $p$, target O-R7-7 of route R7 is KSBA in characteristic $p$. Chapter 5 treats route R7.

A known case that the handbook treats is the K-moduli of cubic surfaces, a required example of Volume 14 (spec 11).

### Lean

The library has no statement on K-stability, on KSBA moduli or on Cremona groups on 2026-11-26. Spec 06.2.2 lists no row for these subjects. The vocabulary that they need (test configurations, the $\delta$-invariant, moduli functors, groups of birational maps) is not in the list of spec 06.1.

### Notes and history

**Claims of 2025 and 2026.**

| Claim | What it claims | Record | Status |
|---|---|---|---|
| C15, J. Liu | a K-polystable smooth polarized 5-fold with no cscK metric | `claims/arXiv-2608-19301.yaml` | fresh; unrefereed; "obtained using generative AI" |

The record says: "Nobody has read the claim for the project yet."

**Routes.** No route of spec 04 has K-stability or Cremona groups as its subject. Route R7 has O-R7-7 for KSBA in characteristic $p$. Route R9 (Chapter 6) treats the analytic side of the program, but its targets are Kähler programs, not cscK metrics.

**References.** arXiv:2608.19301 (J. Liu); arXiv:2102.09405 (Liu, Xu and Zhuang); arXiv:2510.06197 (Blum, Liu, Xu and Zhuang); arXiv:2605.30063 (Trusiani); arXiv:2211.11237 (Birkar); Kollár, "Families of Varieties of General Type" (CUP 2023); Xu, "K-stability of Fano Varieties" (CUP 2025). Volume 13 treats KSBA moduli and Volume 14 treats K-stability.

**Questions for a reader.**

- Which paper is "Xu-Zhuang 2026" in spec 11, and which open problems does it list?
- Which open problems on Cremona groups should the next report list, and does any of them need the minimal model program?
- Does C15 need a node in the map, with the kind claim?
