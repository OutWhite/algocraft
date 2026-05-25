class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        idx : int = len(digits) - 1
        while(idx >= 0):
            if digits[idx] != 9:
                digits[idx] +=1
                return digits
            else:
                digits[idx] = 0
                idx -= 1
        return [1] + digits
