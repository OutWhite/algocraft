class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack: list[int] = []
        next_greater: dict[int, int] = {}
        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)
        return [next_greater.get(num, -1) for num in nums1]



