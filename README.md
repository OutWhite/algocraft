# algocraft

`algocraft` is a personal algorithm practice repository for LeetCode-style problems.

The repository is organized by implementation language so the same problem can be solved and compared in Python and C++.

## Layout

- `python/solutions/`: Python accepted solutions
- `python/templates/`: Python starter templates and snippets
- `cpp/solutions/`: C++ accepted solutions
- `cpp/templates/`: C++ starter templates and snippets
- `notes/`: problem notes, patterns, and review logs
- `scripts/`: small local helpers

## Naming

Use the problem id and slug:

```text
python/solutions/0001_two_sum.py
cpp/solutions/0001_two_sum.cpp
notes/0001_two_sum.md
```

Prefer keeping each solution file close to the online judge format. If a platform expects only a `Solution` class, the file should be easy to copy directly.

## Practice Notes

For each non-trivial problem, record:

```text
problem:
tags:
approach:
complexity:
pitfalls:
follow-ups:
```
