class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        right : int = len(nums)-1
        left : int = 0
        if nums[right] < target:
            return right + 1
        if nums[left] > target:
            return left
        while right > left and right-left !=1:
            if nums[(right + left)//2] > target:
                right = (right + left)//2
            else :
                if nums[(right + left)//2] == target:
                    return (right + left)//2
                else:
                    left =(right + left)//2
        return right

