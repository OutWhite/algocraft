class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        last = {}
        res = float("inf")
        for i, card in enumerate(cards):
            if card in last:
                res = min(res, i - last[card] + 1)
            last[card]=i
        return -1 if res == float("inf") else res