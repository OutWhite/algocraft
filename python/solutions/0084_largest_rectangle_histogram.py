class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        res: int = 0
        stack = []

        heights.append(0)
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                h = heights[stack.pop()]
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                res = max(res, h * width)
            stack.append(i)
        heights.pop()
        return res
