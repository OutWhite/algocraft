class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count: dict[int, int] = {0: 1}
        prefix: int = 0
        res: int = 0
        for num in nums:
            prefix += num
            if prefix - k in count:
                res += count[prefix - k]
            count[prefix] = count.get(prefix, 0) + 1
        return res