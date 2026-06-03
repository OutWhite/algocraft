class Solution:
    def findMin(self, nums: list[int]) -> int:
        left: int = 0
        right: int = len(nums) - 1
        while left < right:
            mid: int = (left + right) // 2
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[left]
