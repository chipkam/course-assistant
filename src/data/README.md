# Data

`kb/` and `scaffolding/` are the complete dataset copied from the reference
project on branch `sample` (`docs/sample-src/data/`). `grammar.cfg` is the
phase 1 grammar: the frozen reference grammar plus the alternatives accepted from
the team's PRs (see `docs/progress/done/T03-grammar-phase1.md`).

- `grammar.cfg`: one syntactic source of truth for parser and generator, with
  the 26 semantic `Q_*` branches. Add new phrasings as alternatives of an
  existing branch, never as a new `Q_*` branch.
- `kb/`: course facts queried at runtime, copied from the sample data supplied
  with the CO3085 assignment.
- `scaffolding/entities.txt`: lexicon for grammar design and entity
  canonicalization, mapping aliases to stable canonical IDs.
- `scaffolding/sample_queries.txt`: official/regression evaluation cases from the
  assignment, extended with verbatim PDF questions, expected query status, and
  required answer facts for end-to-end evaluation.
- `scaffolding/dialogues.txt`: ordered multi-turn context cases.
- `scaffolding/challenge_queries.txt`: author-created edge cases for paraphrases
  outside the grammar, not-found status, and error analysis; sources are noted in
  the file.
- `scaffolding/faq.txt`: kept to preserve the original dataset; never used as the
  primary query engine or a shortcut answer table.

Keep grammar, semantics, canonical IDs, and KB indexes synchronized. Do not put
course facts into the grammar and do not parse raw user text inside the KB.
