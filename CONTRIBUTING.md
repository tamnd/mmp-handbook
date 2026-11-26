# Contributing

Thank you for your help. This file tells how to send a change.

## Before you start

1. Read `README.md`. It gives the volumes, the content format and the build.
2. Read Volume 0 of the handbook. Chapter 4 tells how a section links to Lean and to the map.
3. Read the plan of the handbook, spec 11 of [tamnd/mmp](https://github.com/tamnd/mmp).
4. For a large change, open an issue first.

## A pull request

1. Make a branch from `main`.
2. Keep one subject in one pull request. A new chapter or a group of chapters is one subject.
3. Run `python scripts/style.py`. It must print nothing.
4. Run `python -m mhb check` with a checkout of tamnd/mmp at `../mmp`. It must report 0 faults.
5. Run `python -m mhb number --write` when you add or move a statement.
6. When you change the builder, run `python -m unittest discover -s tests`.

## A section

1. Give the section the front matter of the README. Set `status: drafted` and your name in `drafted_by`.
2. Follow the published proof. Give the paper keys in `sources` and the places in `reads_with`. A book that is not a paper of the map gets a record in `books/`.
3. Put a `Node:` line under each statement that has a node in the map. Do not write a status in that line. The build writes it.
4. Do not claim more than the state of the node. An open case is not proved, and the text must not say or suggest that it is. A claimed result is called claimed.
5. Give each exercise a grade: (A) routine, (B) needs an idea, (C) hard. Add (M) when the exercise asks for a machine check.
6. Only a person who has read the section can add a name to `reviewed_by` and set `status: reviewed`.

## The writing rules

The text follows ASD-STE100 technical English.

1. Write short sentences. Use one idea in one sentence.
2. Use the active voice.
3. Do not use an em dash or an en dash. Use a comma, a colon or a new sentence.
4. Do not break a line in the middle of a sentence. Write each paragraph on one line.
5. Do not add a page break.
6. Write math in `$...$` and `$$...$$`.
7. Write the names of theorems with more than one author with a hyphen: Kawamata-Viehweg.
