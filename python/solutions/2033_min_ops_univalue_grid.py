from typing import List


class Solution:
      def minOperations(self, grid:List[List[int]], x: int) -> int:
          nums = []

          for row in grid:
              for num in row:
                  nums.append(num)

          base = nums[0] % x
          for num in nums:
              if num % x != base:
                  return -1

          nums.sort()
          target = nums[len(nums) // 2]

          ops = 0
          for num in nums:
              ops += abs(num - target) // x

          return ops