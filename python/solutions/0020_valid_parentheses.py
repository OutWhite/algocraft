class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        pairs: dict = {"{":"}","(":")","[":"]"}
        for i,ch in enumerate(s):
            if ch in pairs:
                stack.append(ch)
            else:
                if stack and ch == pairs[stack[-1]]:
                    stack.pop()
                else:
                    return False

        return not stack
