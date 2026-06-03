# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         count = [0] * 52

#         for i in range(len(s)):
#             count[ord(s[i]) - ord('a')] += 1
#             count[ord(t[i]) - ord('a')] -= 1

#         return all(c == 0 for c in count)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count:dict[str, int] = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1

            if count[ch] < 0:
                return False
        return True
