class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        local:int = 0
        diff:int = 0
        for i ,num in enumerate(nums):
            if num != val:
                nums[local] = num
                local += 1
            else:
                diff += 1
        return len(nums) - diff
