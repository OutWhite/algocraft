class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        res: list[int] = []
        target_len: int = len(p)
        window: dict[str, int] = {}
        need: dict[str, int] = {}
        for ch in p:
            need[ch] = need.get(ch, 0) + 1
        left: int = 0
        for right, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1
            if ch not in need:
                left = right + 1
                window.clear()
                continue
            while right - left + 1 > target_len:
                window[s[left]] -= 1
                if window[s[left]] <= 0:
                    del window[s[left]]
                left += 1
            if window == need:
                res.append(left)
        return res
                

