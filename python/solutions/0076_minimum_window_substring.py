class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need: dict[str, int] = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1
        window: dict[str, int] = {}
        left: int = 0
        have: int = 0
        required: int = len(need)
        best_len = float("inf")
        best_start = 0
        for right, ch in enumerate(s):
            if ch in need:
                window[ch] = window.get(ch, 0) + 1
                if window[ch] == need[ch]:
                    have += 1
            while have == required:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start = left
                left_ch = s[left]
                if left_ch in need:
                    window[left_ch] -= 1
                    if window[left_ch] < need[left_ch]:
                        have -= 1
                left += 1
        if best_len == float("inf"):
            return ""
        return s[best_start: best_start + best_len]
