class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        res: list[int] = [-1] * len(nums)
        stack: list[int] = []
        n: int = len(nums)

        for i in range(n * 2):
            idx = i % n
            while stack and nums[stack[-1]] < nums[idx]:
                tmp = stack.pop()
                res[tmp] = nums[idx]
            if i < n:
                stack.append(idx)
        return res
