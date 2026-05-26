class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen: dict[int, int] = {}
        for i, num in enumerate(nums):
            if num in seen:
                return True
            seen[num] = 1
        return False
