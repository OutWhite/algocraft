class Solution:
    def mySqrt(self, x: int) -> int:
        left: int = 0
        right:int = x
        while (right >= left):
            mid: int = (left + right)//2
            if mid * mid > x:
                right = mid - 1
            else:
                if mid * mid == x:
                    return mid
                else:
                    left = mid + 1
        return right
