class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        cost :int = 2**31 - 1
        res :int = 0
        for day, price in enumerate(prices):
            if cost > price:
                cost = price
            else:
                if res < price - cost:
                    res = price - cost
        return res



