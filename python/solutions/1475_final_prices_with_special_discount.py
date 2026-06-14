class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        res: list[int] = prices[:]
        stack: list[int] = []
        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                tmp: int = stack.pop()
                res[tmp] = prices[tmp] - price
            stack.append(i)
        return res

