---
title: The audit of route R2
nodes: [MMBTDMD2XP]
sources: [AxiomMMP, OAI26, KM98, BCHM10]
reads_with: []
requires: ["16.1", "16.3"]
level: research
kind: survey
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The audit of route R2

### Statement

AxiomMath/MMP is a Lean proof, written by Axiom, of the program for lc pairs in dimension at most 4. It formalizes the paper of the OpenAI family 056 (OAI26), and together they are claim C1. The Lean kernel has checked its inferences. What nobody has checked is whether its statements mean what the textbooks mean. Route R2 of tamnd/mmp is the audit that checks this, in eight steps A1 to A8 (spec 04.3), followed by a bridge to the project's own statements. Its weight in the plan of the project is 0.15.

**Remark 16.4.6 (what the audit would decide).** Let $(X, \Delta)$ be a projective lc pair of dimension 4 over an algebraically closed field of characteristic 0, with $\Delta$ a $\mathbb{Q}$-divisor. Then each $(K_X + \Delta)$-program terminates.

Node: MMBTDMD2XP · Lean: `MinimalModel.TerminationLc4Rational`

This is statement S22, and it is claimed. The Lean name is the statement of the project, a `def` of type `Prop` with no proof in mmp-lean at commit 8028303. AxiomMath/MMP proves its own statement of the result, in its own definitions, and those are what the audit reads. If the audit passes, the bridge of step A8 would prove it from the AxiomMath/MMP theorems, the node would change to the Lean state `proved-ext`, and its literature state would stay claimed until peer review (spec 14.7). The credit line of spec 14.2 for S22 is: "proof by OpenAI (paper) and Axiom (Lean); audit by the project".

**The source.** By spec 04.3: commit `1f9ade3670` of 2026-11-16, licence Apache-2.0, Lean v4.35.0, Mathlib at `56a005855e`, and AxiomMath/Stacks at `c496df0d9b`. The main theorems are

- `MMP.Fourfold.Program.IsMaximal.isNefOnCurves_or_isMoriFibreSpace`,
- `MMP.Fourfold.Program.isContinuableRay`,
- `MMP.Fourfold.Program.n_ne_top_of_isAlgClosed`,
- `MMP.Fourfold.projectiveLowerLogMMP_three`.

The hypotheses are: $k$ algebraically closed of characteristic 0, $X$ projective, integral and normal, and a rational boundary. There is no $\mathbb{Q}$-factorial hypothesis and no pseudo-effective hypothesis. The README says that no human has reviewed the code and that abundance is out of scope.

**The steps.** The table gives the steps of spec 04.3 and their states in `records/audit.json`, dated 2026-11-26.

| Step | Work | State |
|---|---|---|
| A1 | a clean build at the pinned commit, with time, memory, `lake-manifest.json` and the hash of each `.olean` | in progress |
| A2 | `#print axioms` on the four main theorems and three other results; the expected set is `propext`, `Classical.choice`, `Quot.sound` | not started |
| A3 | replay with `lean4checker`, then with the kernels lean4lean and nanoda | not started |
| A4 | the index of the definitions in the closure of the statements of the main theorems | not started |
| A5 | the reading of each definition of A4 against KM98, BCHM10 and the Stacks Project, by two people | not started |
| A6 | the meaning of the main statements; the triviality attack; a positive instance | not started |
| A7 | the AxiomMath/Stacks results used whose statements differ from the Stacks Project | not started |
| A8 | the bridge to S20 to S24, a letter to Axiom, 30 days, then a public report | not started |

The same record has 0 findings of each severity 1 to 4 and `passed: false`. No finding is not a pass: the reading steps that would find one have not started.

### Proof in words

There is no proof in this section. What follows is what step A1 has done, from `audit/axiom-mmp/A1-inventory.md` of tamnd/mmp.

**The inventory.** On 2026-11-26 a shallow fetch of the pinned commit was counted and scanned as text. It has 2,269 `.lean` files with 2,054,277 lines, and 3,723 uses of the blueprint attribute `@[mmp "label"]`. A text scan of all `.lean` files for the words that can hide an unchecked proof found no `sorry` and no `axiom`; the word `admit` appears 22 times, all in comments. No step ran Lean, so these numbers come from the source text only.

**The build.** The clean build is not done. The workflow `audit-build` of tamnd/mmp builds on standard runners, with 4 cores and 16 GB of memory, in segments of at most 120 minutes whose partial builds are cached, because one job stops after 6 hours and two long runs lost the runner, most likely for memory. The build now runs in a systemd scope with a memory limit and `OOMPolicy=continue`, so that the kernel kills a lean process rather than the runner, and a segment with a killed process counts as unfinished, not as an error. The runs add up to one clean build, since Lake does not rebuild a module whose trace is unchanged.

**The next two steps.** The files `A2.lean` and `A4.lean` are written and wait for the build. `A2.lean` has one `#print axioms` line for each of the seven declarations. `A4.lean` computes the closure of their statements: it follows types and values of definitions, not theorems, and stops at Mathlib, which the audit takes as given. Spec 04.3 estimates 300 to 600 items for the closure, and marks the estimate as unsure.

**Severities and disclosure.** A finding is a file `audit/axiom-mmp/findings/<n>.yaml`, with one of four severities (spec 14.5):

| Severity | Meaning | Effect |
|---|---|---|
| 1 | a main theorem does not mean what it is said to mean | S22 stays claimed; Q9 is no |
| 2 | a main theorem is right in content but weaker or different in scope than said | S22 can change only to a weaker statement that the bridge proves |
| 3 | a definition differs from the textbook, and the main theorems do not depend on the difference | a note; Q9 can be yes |
| 4 | a style or documentation issue | a note |

Before a page about a finding goes public, the project writes to the authors, and the page waits 30 days or until they answer (spec 14.4). For a finding of severity 1 or 2 no public statement about the affected theorem is made in those 30 days, in either direction. A finding is reported, not fixed.

**The trust row.** Row Q9 of `records/trust.json`, updated 2026-11-26, asks whether the external library has passed the audit at the pinned commit. Its state is open, with the note that the audit has no step done.

### Examples

**Example 16.4.7 (an almost right definition).** Spec 04.3 gives the kind of defect that the reading of A5 looks for: a cone of curves built from integral curves over the wrong field, or a program that allows steps that are not $\mathbb{Q}$-factorial where KM98 excludes them. A Lean check does not see such a defect, because the code is consistent; only a comparison with the textbook does. For a program, the question of step A6 is whether `n_ne_top` says that every program terminates, as S22 says, and not that one program does. The difference is that between Conjecture T(n) and the statement S23 of termination with scaling in Section 16.3.1.

**Example 16.4.8 (the positive instance).** Step A6 asks for a program built in the API of AxiomMath/MMP for a known 4-fold, such as $\mathrm{Bl}_p \mathbb{P}^2 \times \mathbb{P}^2$ or a toric 4-fold, if the API allows. The toric 4-fold $X_0$ of Section 16.3.2 is a candidate: its two programs are known by hand, so a Lean program for it that satisfies `IsMaximal` and ends in the wrong place would show a defect.

### Lean

The project's statement S22 is `MinimalModel.TerminationLc4Rational`, a `def` with no proof. The fidelity record `records/fidelity.json` gives it the class claimed and the checks F1 and F3, and it does not pass the battery of its class. The bridge library `MinimalModelBridge` of step A8 does not exist yet.

### Notes and history

The route is spec 04.3; the trust rows are spec 14.1, the credit lines 14.2, disclosure 14.4 and severities 14.5. Its open targets are:

| Id | Target |
|---|---|
| O-R2-1 | T(4) for projective lc 4-folds with rational boundary, through A1 to A8 |
| O-R2-2 | the surface and 3-fold programs of AxiomMath/MMP, bridged to S10 to S19 |
| O-R2-3 | the Kawamata-Viehweg vanishing statement of AxiomMath/MMP, ported to the project's vocabulary |
| O-R2-4 | whether the proof extends from $\mathbb{Q}$ to $\mathbb{R}$ coefficients |
| O-R2-5 | T(4) for klt Kähler 4-folds, the Kähler part of OpenAI 056 |

The record `records/trust.json` has one more point that a reader should know. Its row Q5 says that 4 statements have an entry in `records/fidelity.json`. The file itself, at the same commit, has 13 entries, and none passes. The row is out of date; its conclusion, that no statement passes, is not.

**Questions for a reader.**

- Which of the sixteen definitions that spec 04.3 names first for A5 would be hardest to compare with KM98? A program, `Program`, and its maximality, `IsMaximal`, have no textbook definition in Lean form.
- Can the build of A1 be split so that A2 runs on the modules of the seven theorems alone?
