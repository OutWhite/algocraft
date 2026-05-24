class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen : dict[int, int] = {}
        for i , num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i

        return []
