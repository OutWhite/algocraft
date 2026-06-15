class Solution:
    def canJump(self, nums: list[int]) -> bool:
        farest: int = 0
        for i, num in enumerate(nums):
            if i > farest:
                return False
            else:
                farest = max(num + i, farest)
        return True