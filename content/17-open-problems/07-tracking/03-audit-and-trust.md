---
title: The audit of AxiomMath/MMP and the trust questions
nodes: [MMBTDMD2XP, MMTJ3YNHTG]
sources: [AxiomMMP, OAI26, KM98, BCHM10]
reads_with: []
requires: ["0", "10"]
level: research
kind: survey
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The audit of AxiomMath/MMP and the trust questions

### Statement

**Remark 17.7.5 (What the audit decides).** AxiomMath/MMP is a Lean proof that every program for a projective lc 4-fold with rational boundary terminates (claim C1, statement S22). The Lean kernel checked its inferences. Nobody has checked that its statements mean what the textbooks mean. The audit of route R2 checks this. If the audit passes and the bridge is proved, S22 moves from claimed to proved-ext, with the credit line "proof by OpenAI (paper) and Axiom (Lean); audit by the project" (spec 06.6). Until then S22 is claimed, whatever the bridge build says.

Node: MMBTDMD2XP · Lean: `MinimalModel.TerminationLc4Rational`

**Remark 17.7.6 (The state of the audit on 2026-11-26).** The record `records/audit.json` gives the source AxiomMath/MMP at commit 1f9ade367087ec711a2ce1382bad279a5a0284c3, with the date 2026-11-26.

| Step | Work | State |
|---|---|---|
| A1 | a clean build at the commit; the time, the memory, the manifest and the hash of each `.olean` | in progress |
| A2 | `#print axioms` on the four main theorems and the three other results | not started |
| A3 | a replay in lean4checker, then lean4lean and nanoda as a second and third kernel | not started |
| A4 | the definition index: each definition, structure, class and instance in the closure of the statements; 300 to 600 items [U] | not started |
| A5 | the reading of each item of A4 against KM98, BCHM and the Stacks Project, by two people | not started |
| A6 | the meaning of the main statements, the triviality attack and a positive instance | not started |
| A7 | the Stacks layer: the results of AxiomMath/Stacks whose statements differ from the Stacks Project | not started |
| A8 | the bridge from the theorems of AxiomMath/MMP to S20 to S24; a letter to Axiom, 30 days, then a public report | not started |

The findings of severity 1, 2, 3 and 4 are 0 each. The field `passed` is false.

### Proof in words

**What is known about the source** (spec 04.3). The commit is of 2026-11-16, under the Apache-2.0 licence, with Lean v4.35.0, Mathlib `56a005855e` and AxiomMath/Stacks at `c496df0d9b`. It has 2,269 files and about 2.05 million lines, in the universe `Scheme.{0}`. Its hypotheses are: $k$ algebraically closed of characteristic 0, $X$ projective, integral and normal, and a rational boundary. It needs no $\mathbb{Q}$-factoriality and no pseudo-effectivity. Its README says that no person has reviewed the code, and that abundance is out of scope. These facts are tagged [P][R]: a part is the word of the repository about itself.

**What the audit reads.** The audit reads statements, not proofs. The question is the meaning of a few hundred definitions. Spec 04.3 names the risk: a definition can be "almost" right, for example a cone of curves built from integral curves over the wrong field, or a program that allows steps that are not $\mathbb{Q}$-factorial where KM98 excludes them. An almost right definition needs an expert, not a Lean check.

**What A6 must show.** Step A6 checks that the main theorem `n_ne_top` says that every program terminates, not that one does. This is the first risk of spec 06.5. It also checks that `IsMaximal` cannot hold for a program that stops early, and that no hypothesis is vacuous.

**The targets of the route.** Route R2 (weight 0.15) has five targets.

- O-R2-1: T(4) for projective lc 4-folds with rational boundary, through A1 to A8.
- O-R2-2: the surface and 3-fold programs of AxiomMath/MMP bridged to S10 to S19.
- O-R2-3: the port of the vanishing theorem of Kawamata-Viehweg of AxiomMath to the vocabulary of the project.
- O-R2-4: does the proof extend from $\mathbb{Q}$ to $\mathbb{R}$ coefficients?
- O-R2-5: T(4) for klt Kähler 4-folds, the Kähler part of OpenAI 056.

Spec 04.3 rates O-R2-1 as the route with the best chance of a G4 result in the first year.

**The trust questions.** The record `records/trust.json` (updated 2026-11-26) answers eleven questions. Its answers are these.

| Id | Question | State | Note of the record |
|---|---|---|---|
| Q0 | Is the source the one that the site describes? | not run | "There is no records/lean.json." |
| Q1 | Does it build? | not run | no record of a build in the Lean record |
| Q2 | Which axioms do the top theorems use? | not run | "There is no records/lean.json." |
| Q3 | Do two more kernels accept it? | not run | no replay record `records/replay.json` |
| Q4 | Do the proved theorems have the pinned statements? | not run | `lake comparator` was not run |
| Q5 | Do the statements mean what the docstrings say? | open | 0 of the 60 statements pass the fidelity checks; 0 have an entry in `records/fidelity.json` |
| Q6 | Which published theorems are still hypotheses? | yes | no node is proved-mod |
| Q7 | Has a person read the proof? | not run | a person answers it from the reviews of the handbook |
| Q8 | Has someone outside the project reproduced Q1 to Q4? | not run | a person answers it with a link |
| Q9 | For a proved-ext theorem: has the external library passed the audit at the pinned commit? | open | "The audit of AxiomMath/MMP at commit 1f9ade3670 has no step done." |
| Q10 | For a check of a fresh claim: have the authors seen the result, and what did they answer? | not run | a person answers it from the letters |

The notes of Q0 and Q2 are out of date. The record `records/lean.json` exists on 2026-11-26, with the library mmp-lean at commit 6e779d01. A reviewer must check if the command `mmp trust` must run again.

**When the project says "proved".** Spec 06.6 gives the rule. The project never says that it has proved an open case unless all of these hold:

- the proof builds;
- the axioms are the three standard ones, `propext`, `Classical.choice` and `Quot.sound`;
- two kernels accept it, the Lean kernel and nanoda or lean4lean;
- the statement passed the fidelity checks F1 to F7;
- at least two experts who are not paid by the project have read the written proof in the handbook.

Before that, the status is "a Lean proof that has passed checks F1 to Fn", and the site says which checks. On 2026-11-26 no statement has passed F1 to F7, so the project can say "proved" of no open case.

### Examples

The first test of the audit is A1, the clean build. It is the one step in progress. Spec 15 puts A3 and A4 at milestone S1 (2027-02-28), and the close of the audit and the decision on S22 at milestone S3 (2027-06-30).

The first items that A5 reads are: variety, normal, prime divisor, $\mathbb{Q}$-divisor, $K_X$, discrepancy, lc, nef on curves, the cone of curves, extremal ray, contraction, flip, divisorial contraction, Mori fibre space, `Program` and `IsMaximal`.

A positive instance for A6 is a program for $\mathrm{Bl}_p \mathbb{P}^2 \times \mathbb{P}^2$ or for a toric 4-fold, if the interface of AxiomMath/MMP allows it.

### Lean

The bridge `MinimalModelBridge` of spec 09.4 is the place where S20 to S24 are to be proved from the theorems of AxiomMath/MMP. On 2026-11-26 it does not exist. The first nodes of route R2 are `axiom-t4-statement` (the statement of AxiomMath, copied as text with its source), `t4-lc-rational` (S22) and `bridge-t4` (the bridge theorem).

The universe is a known issue. AxiomMath/MMP works in `Scheme.{0}`, and the statements of the project are universe polymorphic. Spec 16, Q-07, gives the choices: a bridge for `Scheme.{0}` only, or a request to Axiom for statements in all universes. Risk 8 of spec 06.5 says that the bridge is the only place with universe 0.

Node: MMTJ3YNHTG · Lean: `MinimalModel.Termination`

S20 is open. A bridge that proves S22 from AxiomMath/MMP does not prove S20, because S20 is for all dimensions.

### Notes and history

**The work with Axiom.** Spec 16, Q-03, chooses a letter to Axiom with the audit plan at milestone S0, and the offer to send each finding to Axiom 30 days before it is public. Spec 16, Q-02, chooses to audit commit 1f9ade3670 in full, then each later commit as a delta: A1 to A3 again, and A5 and A6 only on the changed definitions. The record of the letter is not in `claims/AxiomMath-MMP.yaml`: its list `letters` is empty.

**Routes.** Route R2 (weight 0.15). If the audit finds a central definition wrong, spec 16, Q-06, moves weight from R2 to R3 and R4 at once.

**References.** AxiomMMP for the repository; OAI26 for the paper of OpenAI 056; KM98 and BCHM10 for the definitions that A5 reads against. Volume 16 reports the state of dimension 4.

**Questions for a reader.**

- Does `n_ne_top_of_isAlgClosed` say that every program terminates, or that one does?
- Which definition of AxiomMath/MMP is the first one where "almost right" is a risk?
- Must the notes of Q0 and Q2 change now that `records/lean.json` exists?
