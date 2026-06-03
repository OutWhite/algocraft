class Solution:
    def maxArea(self, height: list[int]) -> int:
        left: int = 0
        right: int = len(height) - 1
        res: int = 0
        while left < right:
            area: int = min(height[left], height[right]) * (right - left)
            if area > res:
                res = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res