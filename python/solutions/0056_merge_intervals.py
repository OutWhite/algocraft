class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        res: list[list[int]] = []
        for interval in intervals:
            if res and interval[0] <= res[-1][1]:
                res[-1][1] = max(interval[1], res[-1][1])
            else:
                res.append(interval)
        return res
