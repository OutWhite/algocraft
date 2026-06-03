class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        res = float("inf")
        left = 0
        right = 0
        cur_sum = 0

        while right < len(nums):
            cur_sum += nums[right]
            right += 1

            while cur_sum >= target:
                res = min(res, right - left)
                cur_sum -= nums[left]
                left += 1

        return 0 if res == float("inf") else res