class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}
        for ch in strs:
            sig = tuple(sorted(ch))
            if sig not in groups:
                groups[sig] = []
            groups[sig].append(ch)
        return list(groups.values())
