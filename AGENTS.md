# AlgoCraft Practice Notes

This repository is being used for Python coding fluency recovery and LeetCode-style practice.

## Coaching Mode

- Do not write full solutions unless explicitly asked.
- Prefer opening solution templates and case files for new problems.
- Give small hints, debug feedback, and edge-case explanations.
- Let the user hand-write the algorithm.
- When reviewing code, focus on concrete bugs, boundary cases, Python semantics, and state changes.
- Keep explanations concise and training-oriented.

## Current Recovery State

The user is an experienced systems/CUTLASS/inference-engine engineer rebuilding manual coding fluency after heavy AI-assisted coding.

Current state:

- Python hand-writing fluency is restored for easy and medium-prep problems.
- Array scanning, slow/write pointers, hash maps/sets, stack, linked list pointer manipulation, two pointers, sliding window, prefix sum, Kadane DP, monotonic stack, and binary-search variants have been reactivated.
- The user now starts from blank templates quickly and usually writes runnable first versions without syntax blockers.
- Easy problems are largely in a stable passing zone; current training is focused on medium-prep modules and Hot 100 coverage.
- The main remaining risk is no longer basic syntax, but proof discipline: loop boundaries, candidate interval meaning, branch exclusion reasoning, pointer movement invariants, and final answer location.
- The user benefits from concise pre-problem framing: state the problem, method target, and key invariant, then leave implementation to the user.

Known error patterns from recent sessions:

- Treating `stack[-1]` as if it safely represents stack existence; must check `if stack` before indexing.
- Assigning `stack = stack.pop()` instead of calling `stack.pop()` for mutation.
- Checking `node.next` instead of `node`, which can skip the final linked-list node.
- Starting slow/write pointers one slot off in in-place array problems.
- Mixing node objects and node values in linked-list construction.
- Passing sample cases with a plausible pointer rule that is not tied to the real invariant, e.g. early `0011` moved based on `height[left + 1]` instead of the shorter wall.
- Returning the wrong binary-search boundary after moving `left` past the last valid candidate, e.g. early `0069` returned `left` for floor sqrt instead of the last valid value.
- For binary search, the user now explicitly wants methodology for choosing `while` conditions and update rules; explain through interval semantics, not templates alone.
- For linked lists, the key breakthrough was treating lists as local graph rewrites: first snapshot nodes (`prev/a/b/rest`, `group_prev/group_start/kth/group_next`), then reconnect `next` edges. Prefer this framing over "follow next pointers while mutating".
- Under speed pressure, the user may narrow a condition accidentally, e.g. using `==` where the invariant is `<=`; ask for the exact validity condition before reviewing code.

## Completed / Practiced Problems

- `0001` Two Sum: dict lookup and `enumerate`.
- `0002` Add Two Numbers: linked list addition, carry, dummy node.
- `0020` Valid Parentheses: stack and mapping.
- `0021` Merge Two Sorted Lists: dummy node and linked-list merge.
- `0024` Swap Nodes in Pairs: local graph rewrite with `prev -> a -> b -> rest`; passed.
- `0025` Reverse Nodes in k-Group: k-group boundary snapshot and local segment reversal; passed after adopting `group_prev/group_start/kth/group_next` framing.
- `0026` Remove Duplicates from Sorted Array: in-place slow pointer.
- `0027` Remove Element: in-place slow pointer, passed quickly.
- `0033` Search in Rotated Sorted Array: rotated-array target search with closed interval binary search; passed, then discussed scientific loop-boundary methodology.
- `0035` Search Insert Position: binary search, passed quickly.
- `0042` Trapping Rain Water: monotonic stack version; passed and brute-force checked.
- `0045` Jump Game II: greedy BFS-layer boundary (`cur_end/farthest/jumps`); passed.
- `0049` Group Anagrams: hash signature grouping using `tuple(sorted(word))`; passed.
- `0053` Maximum Subarray: Kadane state transition; passed and brute-force checked.
- `0055` Jump Game: greedy farthest-reach invariant; passed.
- `0056` Merge Intervals: sort by start and merge against last output interval; passed.
- `0058` Length of Last Word: reverse string scan and trailing-space boundaries, passed on first attempt.
- `0066` Plus One: reverse digit scan and carry; first version passed but was state-heavy, then was rewritten into a clean standard state machine.
- `0069` Sqrt(x): floor binary search; learned to distinguish "first invalid" vs "last valid" return boundary.
- `0076` Minimum Window Substring: variable sliding window with `need/window` and satisfied character count; passed.
- `0084` Largest Rectangle in Histogram: monotonic stack with sentinel; passed.
- `0088` Merge Sorted Array: reverse-write three-pointer merge, passed; key lesson was that loop conditions should protect read pointers, not just the result write pointer.
- `0092` Reverse Linked List II: local head-insertion reversal inside `[left, right]`; passed.
- `0121` Best Time to Buy and Sell Stock: one-pass min-cost / max-profit state maintenance, passed cleanly.
- `0125` Valid Palindrome: two-pointer scan with alnum filtering and case normalization; passed.
- `0153` Find Minimum in Rotated Sorted Array: binary-search variant that shrinks candidate interval to one point; passed and rotation-checked.
- `0141` Linked List Cycle: fast/slow pointer.
- `0142` Linked List Cycle II: fast/slow cycle entrance; runner now supports comparing returned linked-list node values.
- `0209` Minimum Size Subarray Sum: positive-array sliding window; passed and brute-force checked.
- `0206` Reverse Linked List: iterative and recursive reversal concepts.
- `0217` Contains Duplicate: hash seen pattern; passed with dict-as-unordered-map style, with note that `set` is more idiomatic when no value is needed.
- `0242` Valid Anagram: dict counting; passed, with Python note that single characters are `str`, not `char`.
- `0283` Move Zeroes: in-place slow/write pointer with full mutation check, passed cleanly.
- `0234` Palindrome Linked List: fast/slow midpoint, reverse second half, compare; passed.
- `0424` Longest Repeating Character Replacement: sliding window with max-frequency validity; passed.
- `0438` Find All Anagrams in a String: fixed-length frequency window; passed.
- `0496` Next Greater Element I: monotonic stack next-greater map; passed.
- `0503` Next Greater Element II: circular next-greater stack; passed and brute-force checked.
- `0560` Subarray Sum Equals K: prefix sum plus hash count; passed.
- `0567` Permutation in String: fixed-length frequency window; passed.
- `0704` Binary Search: closed-interval binary search, passed cleanly.
- `0739` Daily Temperatures: monotonic stack over indices; passed.
- `0907` Sum of Subarray Minimums: contribution intervals with asymmetric strictness for duplicates; passed and brute-force checked.
- `1004` Max Consecutive Ones III: sliding window with at most `k` zeroes; passed after fixing update condition.
- `1475` Final Prices With a Special Discount: next smaller-or-equal stack; passed.

## Latest Session Notes

Most recent sessions completed three major technique modules and started greedy/intervals:

- Monotonic stack completed as a coherent module: `0496`, `0739`, `0503`, `1475`, `0907`, `0084`, `0042`.
- Sliding window completed as a coherent module: `0003`, `0209`, `0424`, `0567`, `0076`, `0438`, `1004`.
- Linked list pointer-manipulation module completed: `0019`, `0142`, `0234`, `0024`, `0092`, `0025`, plus earlier `0002`, `0021`, `0206`, `0141`.
- Greedy/intervals started: `0055`, `0045`, `0056`.

Observed progress:

- The user now writes many medium-prep solutions quickly from blank templates, then uses runner feedback to tighten edge conditions.
- The most useful coaching pattern is still invariant-first: ask what state means, when a window/interval/group is valid, and what is safe to discard or reconnect.
- For linked lists, the "snapshot local nodes, then reconnect edges" model was a major unlock and should be reused for any future pointer-heavy problem.
- For greedy, the current framing is range/coverage based: `0055` uses farthest reachable; `0045` uses BFS-like layer boundaries.

Phase assessment:

- Python hand-writing recovery is largely complete for common interview primitives.
- Monotonic stack, sliding window, and linked list are interview-usable with periodic review.
- Greedy/intervals is in progress.
- The largest remaining Hot 100 coverage gaps are binary tree, graph/BFS/topological sort, backtracking, heap, and DP.
- Next step is to finish a short greedy/interval set, then start binary tree DFS/BFS as a full module.

Current coaching emphasis:

- Continue giving problem statement + empty framework + JSON cases, unless the user asks for implementation.
- After each pass, review correctness through invariants, boundary conditions, and final variable meaning.
- For linked-list work, coach via local topology diagrams and named node snapshots before code.
- For greedy work, require a one-sentence proof of why the local state is sufficient (`farthest`, current layer end, sorted interval end, etc.).
- For binary search, always identify one of two modes:
  - find a concrete target and empty the interval: `while left <= right`, update with `mid +/- 1`, return not-found after loop.
  - shrink to an answer point/boundary: `while left < right`, preserve possible answer with `left = mid` or `right = mid`, return `left/right`.
- Use brute-force cross-checks for technique-zone problems when feasible.
- Keep explanations concise; the user is technically strong and mainly needs disciplined pattern recall and edge-case review.

## Runner Capabilities

Use:

```bash
python3 scripts/run_python.py <problem_id>
```

The runner supports:

- plain JSON arguments and expected values
- `linked_list` arguments and linked-list expected outputs
- `linked_list_cycle` arguments encoded as `[values, pos]`
- `linked_list_node_value` expected outputs for functions that return a node, such as cycle entrance detection
- mutation checks for in-place array problems via `mutations`

## Recommended Next Problems

Continue medium-prep classics while keeping each problem short enough for hand-written feedback loops:

- Greedy / intervals: `0435` Non-overlapping Intervals, `0122` Best Time to Buy and Sell Stock II, `0134` Gas Station.
- Binary tree DFS/BFS: max depth, level order, validate BST, path sum, LCA.
- Backtracking: `0078` Subsets, `0046` Permutations, `0039` Combination Sum, `0022` Generate Parentheses, `0079` Word Search.
- Graph / BFS / topological sort: `0200`, `0994`, `0207`, `0133`.
- Heap / priority queue: `0215`, `0347`, `0023`, `0295`.
- DP: `0070`, `0198`, `0322`, `0300`, `1143`, `0072`.

Completed modules should be periodically reviewed under speed pressure: monotonic stack, sliding window, and linked list.
