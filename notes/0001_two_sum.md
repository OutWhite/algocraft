# 0001 Two Sum

problem: Two Sum
tags: hash table, array

## Approach

Scan once from left to right. Keep a hash table from value to index for values already seen.

For each `x = nums[i]`, look for `target - x` in the table. If it exists, the pair is complete. Otherwise store `x -> i`.

This order prevents using the same element twice.

## Complexity

Time: `O(n)`

Space: `O(n)`

## Pitfalls

- Insert after lookup, not before lookup.
- Duplicates are valid. For example, `[3, 3]` with target `6`.
- LeetCode guarantees exactly one answer, but the code returns an empty result as a fallback.

## Follow-Ups

- If the array is sorted, use two pointers in `O(1)` extra space.
- If many queries share the same `nums`, build an index structure once.
