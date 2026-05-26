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

- Python syntax and basic control flow are now usable for short hand-written solutions.
- Array scanning, slow/write pointers, simple state maintenance, and binary-search easy problems are passing reliably.
- Stack, dict/set, linked-list, in-place array, reverse-write merge, and simple carry patterns have been reactivated.
- The user is regaining subjective control and confidence: less hesitation when starting from a blank template, quicker self-review, and faster willingness to refactor.
- The user can still solve practice problems after a demanding systems-engineering workday, though Python API recall can be slower under fatigue.
- Main remaining risk is still low-level hand-written state control on harder problems: loop boundaries, `None` checks, mutation vs return values, read-pointer vs write-pointer conditions, and off-by-one pointer/index placement.

Known error patterns from recent sessions:

- Treating `stack[-1]` as if it safely represents stack existence; must check `if stack` before indexing.
- Assigning `stack = stack.pop()` instead of calling `stack.pop()` for mutation.
- Checking `node.next` instead of `node`, which can skip the final linked-list node.
- Starting slow/write pointers one slot off in in-place array problems.
- Mixing node objects and node values in linked-list construction.

## Completed / Practiced Problems

- `0001` Two Sum: dict lookup and `enumerate`.
- `0002` Add Two Numbers: linked list addition, carry, dummy node.
- `0020` Valid Parentheses: stack and mapping.
- `0021` Merge Two Sorted Lists: dummy node and linked-list merge.
- `0026` Remove Duplicates from Sorted Array: in-place slow pointer.
- `0027` Remove Element: in-place slow pointer, passed quickly.
- `0035` Search Insert Position: binary search, passed quickly.
- `0058` Length of Last Word: reverse string scan and trailing-space boundaries, passed on first attempt.
- `0066` Plus One: reverse digit scan and carry; first version passed but was state-heavy, then was rewritten into a clean standard state machine.
- `0088` Merge Sorted Array: reverse-write three-pointer merge, passed; key lesson was that loop conditions should protect read pointers, not just the result write pointer.
- `0121` Best Time to Buy and Sell Stock: one-pass min-cost / max-profit state maintenance, passed cleanly.
- `0141` Linked List Cycle: fast/slow pointer.
- `0206` Reverse Linked List: iterative and recursive reversal concepts.
- `0217` Contains Duplicate: hash seen pattern; passed with dict-as-unordered-map style, with note that `set` is more idiomatic when no value is needed.
- `0283` Move Zeroes: in-place slow/write pointer with full mutation check, passed cleanly.
- `0704` Binary Search: closed-interval binary search, passed cleanly.

## Latest Session Notes

Most recent session completed three problems after a demanding workday: `0088`, `0704`, and `0217`.

Observed progress:

- `0088` showed improved pointer reasoning: the user identified that `ptr_res >= 0` is the wrong primary loop condition because it does not protect reads from `nums1` / `nums2`.
- `0704` confirmed the closed-interval binary-search template is now stable.
- `0217` confirmed the hash seen pattern is active again; the user used a Python `dict` like C++ `unordered_map`, which is correct but less idiomatic than `set`.
- Fatigue mainly affected Python API recall, not problem solving or debugging quality.

Phase assessment:

- Clear improvement from early sessions: fewer language-semantics mistakes, faster implementation, better self-review, and stronger confidence.
- Easy array/string/hash/binary-search problems are now mostly in a stable passing zone.
- The training has moved from syntax recovery into boundary-control and classic-pattern reinforcement.
- Next step is to gradually introduce medium-prep classics while keeping local case feedback and code review discipline.

Current coaching emphasis:

- Continue confirming both correctness and code shape after each pass.
- Prefer concise state variables with clear semantics.
- Keep using local cases to reinforce short feedback loops.
- Begin introducing medium-prep classics gradually, especially array/two-pointer problems before `0042` Trapping Rain Water.

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

Keep the near-term sequence focused on short code with dense boundary practice:

- `0058` Length of Last Word
- `0066` Plus One
- `0069` Sqrt(x)
- `0088` Merge Sorted Array
- `0121` Best Time to Buy and Sell Stock
- `0011` Container With Most Water
- `0217` Contains Duplicate
- `0242` Valid Anagram
- `0283` Move Zeroes
- `0704` Binary Search
- `0049` Group Anagrams
- `0053` Maximum Subarray

Avoid jumping too quickly into hard problems. The current goal is reliable manual control, not contest speed.
