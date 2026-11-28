# The 2026 frontier: generalized pairs, Kähler spaces, 4-folds

This volume is a dated report. Its date is 2026-11-28. It is the first release of Volume 16, the report that spec 11.10 of the project ties to milestone S3. Each later milestone gives a new dated report, and each report replaces the one before it. The report reads the records of the project tamnd/mmp as they stand on 2026-11-27 (commit `b1f85dd`) and the library mmp-lean at commit `8028303`. A reader who finds this text after 2026-11-28 must check the records for changes. A claim of this report can be withdrawn, refereed or refuted after the date.

The volume treats the parts of the minimal model program where the work of 2025 and 2026 is concentrated: generalized pairs, compact Kähler spaces, and termination in dimension 4. It also reports what the project itself does with the new claims: the audit of the Lean formalization AxiomMath/MMP (route R2) and the formal checks of fresh claims (route R1). Volume 17 lists the open problems of the whole program; this volume gives the mathematics behind the part of that list that moved in 2026, with worked examples.

The words of the volume have exact meanings, the same as in Volume 17.

- *Theorem* means a proof that referees accepted, as the records give it.
- *Open* and *conjecture* mean that no proof is known or claimed in a form that the records accept.
- *Claimed* means that a preprint, an AI manuscript or a Lean repository gives a proof, and that no referee and no reader of the project has checked it yet. A claimed result is never called proved in this volume, and no argument in the handbook uses one as a hypothesis.
- *Withdrawn* means that the authors took the claim back.

A claimed result appears as a Remark, never as a Theorem. A Theorem of this volume is a refereed result, and a Lemma is a short argument that the section proves in full. After each Theorem and Lemma a Lean line says what the library mmp-lean has. The library states many results as a `def` of type `Prop` with no proof. Such a statement is named on its Node line; it is not a proof, and the Lean part of the section says so. Where the library has no declaration, the line says "Lean: not yet in Lean."

The chapters are these.

1. Generalized pairs: the definitions of Birkar and Zhang, the canonical bundle formula of an elliptic fibration as the first example, and the generalized program with its claims of 2026.
2. Kähler 3-folds: the program for compact Kähler 3-folds, which is a theorem, and the claims of 2026 in higher dimension.
3. Termination in dimension 4: what is proved, what is claimed, and one sequence of 4-fold flips whose termination is checked by hand.
4. Claims and checks: the preprints of 2026 with their records, the audit of AxiomMath/MMP, and the claim checks of route R1.

The spine of the volume is Birkar-Zhang (BZ16) for generalized pairs, Moraga (Mor25) for pseudo-effective 4-fold flips, and the claim records of the project on 2026-11-28 for the rest. The volume needs Volumes 9, 10 and 12 for the program with scaling, flips and termination, and the toric material of the handbook for Chapter 3. Each chapter ends with problems of grade C: research-level questions, most of them with no known answer, or exercises that need a source paper in hand.
