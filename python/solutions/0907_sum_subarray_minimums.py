class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10 ** 9 + 7
        res: int = 0
        left: list[int] = [0] * len(arr)
        right: list[int] = [0] * len(arr)
        stack: list[int] = []
        n: int = len(arr)
        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] >= num:
                stack.pop()
            if stack:
                left[i] = i - stack[-1]
            else:
                left[i] = i + 1
            stack.append(i)
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1] - i
            else:
                right[i] = n - i
            stack.append(i)
        for i in range(0, len(arr)):
            res += left[i] * right[i] * arr[i]
        return res % MOD