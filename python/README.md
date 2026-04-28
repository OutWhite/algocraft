# Python

Python solutions should follow the LeetCode submission shape unless a problem needs local helpers.

Example:

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen: dict[int, int] = {}
        for i, x in enumerate(nums):
            if target - x in seen:
                return [seen[target - x], i]
            seen[x] = i
        return []
```

## Local runner

Each solution can stay in LeetCode's normal format:

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ...
```

Run saved cases:

```bash
python3 scripts/run_python.py 0003
```

Run one ad-hoc call:

```bash
python3 scripts/run_python.py 0003 --method lengthOfLongestSubstring --args '["abcabcbb"]'
```

Case files live in `python/cases/<problem_id>.json`:

```json
{
  "method": "lengthOfLongestSubstring",
  "cases": [
    {
      "args": ["abcabcbb"],
      "expected": 3
    }
  ]
}
```
