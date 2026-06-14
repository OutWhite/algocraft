class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        set1: dict[str, int] = {}
        set2: dict[str, int] = {}
        for ch in s1:
            set1[ch] = set1.get(ch, 0) + 1
        left: int = 0
        for right, ch in enumerate(s2):
            set2[ch] = set2.get(ch, 0) + 1
            if right - left + 1 > len(s1):
                set2[s2[left]] -= 1
                if set2[s2[left]] == 0:
                    del set2[s2[left]]
                left += 1
            if right - left + 1 == len(s1) and set2 == set1:
                return True
        return False

