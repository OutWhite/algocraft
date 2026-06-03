class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cur = nums[0]
        res = nums[0]
        for num in nums[1:]:
            cur = max(num, cur + num)
            res = max(res, cur)
        return res