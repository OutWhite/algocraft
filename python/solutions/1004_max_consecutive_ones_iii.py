class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left: int = 0
        res: int = 0
        ones: int = 0
        for right, num in enumerate(nums):
            if num == 1:
                ones += 1
            while right - left + 1 > ones + k:
                left_num = nums[left]
                if left_num == 1:
                    ones -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
