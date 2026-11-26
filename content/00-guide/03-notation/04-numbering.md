---
title: Numbering and cross references
nodes: []
sources: []
reads_with: []
requires: []
level: guide
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Numbering and cross references

- **Items.** Definitions, theorems, examples and the other numbered items have the number of their volume, their chapter and their place in the chapter. In the P volumes the number has the prefix of the volume: Theorem P5.7.2 is item 2 of chapter 7 of P5. In the program volumes it has no prefix: Theorem 8.3.4 is item 4 of chapter 3 of Volume 8.
- **Sections.** A section has the number of its chapter and its place: Section 3.2 is the second section of chapter 3 of the same volume. A reference to another volume names it: "P0 Section 6.4", "Volume 4 Chapter 2".
- **Requires.** The source file of each section lists the chapters it uses, in the form `P5.6` (P5 Chapter 6) or `3.4` (Volume 3 Chapter 4). The builder checks that each key names a chapter of the plan.
- **Reads with.** The source file also lists the places in standard books that read in parallel, in the form `KM98:2.7` (KM98, item or section 2.7) or `Mat02:ch14` (Matsuki, Chapter 14).
- **Numbers in other books.** A theorem number of another book is given only when it is checked. Otherwise the handbook gives the chapter only.
