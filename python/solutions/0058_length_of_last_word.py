class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res: int = 0
        idx: int = len(s) - 1
        if idx < 0:
            return res
        while not(res>0 and (s[idx] == ' ' or idx < 0 )):
            if s[idx] !=' ':
                res+=1
            idx -=1
        return res
        