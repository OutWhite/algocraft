class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        local: int = 0
        fast: int = 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[local] = nums[fast]
                local += 1
            fast += 1
        for idx in range(local, fast):
            nums[idx] = 0

