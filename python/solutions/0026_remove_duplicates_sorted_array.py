class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        diff: int = 0
        local : int = 1
        if len(nums) == 1 or len(nums)==0:
            return len(nums)
        for i,num in enumerate(nums):
            if i == 0 :
                continue
            if i > 0 and num == nums[i-1]:
                diff = diff + 1
            else:
                nums[local]=num
                local =local + 1

        return len(nums) - diff

