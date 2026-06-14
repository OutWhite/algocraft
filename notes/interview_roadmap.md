# Interview Roadmap

Goal: reach high-confidence hand-written coding interview readiness for Hot 100 style rounds.

Progress labels:

- `[x]` practiced and currently usable
- `[~]` partly practiced, needs more medium coverage
- `[ ]` not yet systematically covered

## Core Lines

- `[~]` Array / Hash
  - Focus: lookup history, frequency maps, grouping, prefix-related hash state.
  - Practiced: `0001`, `0217`, `0242`, `0049`, `0560`.
  - Next: revisit mixed problems under time pressure.

- `[~]` Two Pointers
  - Focus: opposite pointers, fast/slow pointers, write pointers, invariant-based movement.
  - Practiced: `0011`, `0026`, `0027`, `0283`, `0125`.
  - Next: `0167`, `0015`.

- `[x]` Sliding Window
  - Focus: right-open window semantics, shrink conditions, count maps.
  - Practiced: `0003`, `0209`, `0424`, `0567`, `0076`, `0438`, `1004`.
  - Next: periodic review under speed pressure; optional follow-ups `0239` Sliding Window Maximum, `0992` Subarrays with K Different Integers.

- `[~]` Prefix Sum
  - Focus: prefix difference, hash count, modulo prefix.
  - Practiced: `0560`.
  - Next: `0523`, `0974`.

- `[~]` Binary Search
  - Focus: closed interval target search, boundary search, rotated arrays, answer location after loop.
  - Practiced: `0033`, `0035`, `0069`, `0153`, `0704`.
  - Next: `0034`, `0162`, `0278`, `0875`.

- `[x]` Monotonic Stack
  - Focus: maintain monotonicity, pop to settle waiting elements, next greater/smaller, circular arrays, contribution intervals, histogram, trapping rain water.
  - Practiced: `0496`, `0739`, `0503`, `1475`, `0907`, `0084`, `0042`.
  - Next: periodic review and explain-from-invariant drills.

- `[~]` Linked List
  - Focus: dummy nodes, reversal, fast/slow pointers, cycle entry, deletion by offset.
  - Practiced: `0002`, `0021`, `0141`, `0206`.
  - Next: `0019`, `0142`, `0234`, `0023`.

- `[ ]` Binary Tree
  - Focus: DFS recursion shape, BFS level order, return-value semantics, BST invariants, LCA.
  - Next: max depth, level order, validate BST, path sum, LCA.

- `[ ]` Graph / BFS / Topological Sort
  - Focus: visited state, queue layers, grid traversal, course dependency ordering.
  - Next: `0200`, `0994`, `0207`, `0133`.

- `[ ]` Backtracking
  - Focus: choose/explore/unchoose, duplicate handling, pruning, path state.
  - Next: `0078`, `0046`, `0039`, `0022`, `0079`.

- `[ ]` Heap / Priority Queue
  - Focus: top-k, k-way merge, streaming median.
  - Next: `0215`, `0347`, `0295`, `0023`.

- `[ ]` Dynamic Programming
  - Focus: state definition, transition, initialization, iteration order.
  - Next: `0070`, `0198`, `0322`, `0300`, `1143`, `0072`.

- `[ ]` Greedy / Intervals
  - Focus: sort-based decisions, local choice proof, interval merging/removal.
  - Next: `0056`, `0055`, `0045`, `0122`, `0435`.

## Readiness Criteria

For a module to count as interview-usable:

- State the invariant before coding.
- Write a passing solution from a blank template.
- Explain why each branch is safe.
- Explain where the answer lives after the loop.
- Pass local cases plus at least one adversarial/manual edge case.

## Next Training Order

1. Finish and periodically review monotonic stack explanations.
2. Cover linked list medium: `0019`, `0142`, `0234`.
3. Start binary tree DFS/BFS as a full module.
4. Add backtracking and graph BFS/topological sort.
5. Add heap and DP after traversal/backtracking patterns are active.
