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

- Python hand-writing fluency is mostly restored for easy and medium-prep problems.
- Array scanning, slow/write pointers, hash maps/sets, stack, linked list basics, two pointers, sliding window, prefix sum, Kadane DP, and binary-search variants have been reactivated.
- The user now starts from blank templates quickly and usually writes runnable first versions without syntax blockers.
- Easy problems are largely in a stable passing zone; current training has moved into "technique zone" medium-prep patterns.
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

## Completed / Practiced Problems

- `0001` Two Sum: dict lookup and `enumerate`.
- `0002` Add Two Numbers: linked list addition, carry, dummy node.
- `0020` Valid Parentheses: stack and mapping.
- `0021` Merge Two Sorted Lists: dummy node and linked-list merge.
- `0026` Remove Duplicates from Sorted Array: in-place slow pointer.
- `0027` Remove Element: in-place slow pointer, passed quickly.
- `0033` Search in Rotated Sorted Array: rotated-array target search with closed interval binary search; passed, then discussed scientific loop-boundary methodology.
- `0035` Search Insert Position: binary search, passed quickly.
- `0049` Group Anagrams: hash signature grouping using `tuple(sorted(word))`; passed.
- `0053` Maximum Subarray: Kadane state transition; passed and brute-force checked.
- `0058` Length of Last Word: reverse string scan and trailing-space boundaries, passed on first attempt.
- `0066` Plus One: reverse digit scan and carry; first version passed but was state-heavy, then was rewritten into a clean standard state machine.
- `0069` Sqrt(x): floor binary search; learned to distinguish "first invalid" vs "last valid" return boundary.
- `0088` Merge Sorted Array: reverse-write three-pointer merge, passed; key lesson was that loop conditions should protect read pointers, not just the result write pointer.
- `0121` Best Time to Buy and Sell Stock: one-pass min-cost / max-profit state maintenance, passed cleanly.
- `0125` Valid Palindrome: two-pointer scan with alnum filtering and case normalization; passed.
- `0153` Find Minimum in Rotated Sorted Array: binary-search variant that shrinks candidate interval to one point; passed and rotation-checked.
- `0141` Linked List Cycle: fast/slow pointer.
- `0209` Minimum Size Subarray Sum: positive-array sliding window; passed and brute-force checked.
- `0206` Reverse Linked List: iterative and recursive reversal concepts.
- `0217` Contains Duplicate: hash seen pattern; passed with dict-as-unordered-map style, with note that `set` is more idiomatic when no value is needed.
- `0242` Valid Anagram: dict counting; passed, with Python note that single characters are `str`, not `char`.
- `0283` Move Zeroes: in-place slow/write pointer with full mutation check, passed cleanly.
- `0560` Subarray Sum Equals K: prefix sum plus hash count; passed.
- `0704` Binary Search: closed-interval binary search, passed cleanly.

## Latest Session Notes

Most recent sessions moved from easy recovery into technique-zone medium-prep:

- Sliding window: `0209`.
- Prefix sum + hash count: `0560`.
- Rotated-array binary search: `0153`, `0033`.
- Supporting recent easy/medium-prep work: `0011`, `0049`, `0053`, `0125`, `0242`, `0069`.

Observed progress:

- `0209` confirmed the user can maintain a right-open sliding window (`nums[left:right]`) and use `right - left` consistently.
- `0560` confirmed prefix-sum hash counting is available and distinguishes itself from positive-array sliding window.
- `0153` confirmed the user can use `while left < right` when shrinking a candidate interval to one answer point, preserving `mid` when it may be the answer.
- `0033` confirmed the user can use closed-interval binary search with rotated-array ordered-half checks.
- The user asked specifically for a methodology to choose `while` conditions. Future coaching should ask them to state: interval definition, termination condition, whether `mid` is excluded or preserved, and where the answer lives after the loop.

Phase assessment:

- Python hand-writing recovery is largely complete for common interview primitives.
- Easy array/string/hash/binary-search problems are stable enough to stop over-indexing on them.
- The current phase is technique-zone reinforcement: medium-prep classics with strong invariant and boundary review.
- Next step is to broaden into monotonic stack, more sliding window, linked-list pointer tricks, and entry-level DP/greedy while keeping local case feedback and occasional brute-force checks.

Current coaching emphasis:

- Continue giving problem statement + empty framework + JSON cases, unless the user asks for implementation.
- After each pass, review correctness through invariants, boundary conditions, and final variable meaning.
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
- mutation checks for in-place array problems via `mutations`

## Recommended Next Problems

Move into medium-prep classics while keeping each problem short enough for hand-written feedback loops:

- Sliding window: `0003` review, `0424` Longest Repeating Character Replacement, `0567` Permutation in String.
- Prefix sum / hash: `0523` Continuous Subarray Sum, `0974` Subarray Sums Divisible by K.
- Binary-search variants: `0278` First Bad Version, `0034` Find First and Last Position, `0162` Find Peak Element, `0154` only after duplicate-handling is desired.
- Two pointers: `0167` Two Sum II, `0015` 3Sum, then later `0042` Trapping Rain Water.
- Monotonic stack: `0496` Next Greater Element I, `0739` Daily Temperatures.
- Linked list: `0234` Palindrome Linked List, `0142` Linked List Cycle II, `0019` Remove Nth Node From End.
- DP/greedy basics: `0070` Climbing Stairs, `0198` House Robber, `0122` Best Time to Buy and Sell Stock II.

Avoid jumping directly into hard problems or long implementation-heavy problems. The current goal is interview-usable pattern fluency: state the invariant, write the code, test locally, then explain why the loop terminates with the answer in the claimed place.
