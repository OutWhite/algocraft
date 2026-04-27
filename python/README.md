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
