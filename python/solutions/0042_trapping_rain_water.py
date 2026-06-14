class Solution:
    def trap(self, height: list[int]) -> int:
        stack: list[int] = []
        res: int = 0
        for i ,h in enumerate(height):
            while stack and height[stack[-1]] <= h:
                bottom = stack.pop()
                if stack:
                    width = i - stack[-1] - 1
                    water_height = min(height[stack[-1]], height[i]) - height[bottom]
                    res += width * water_height
            stack.append(i)
        return res
            

