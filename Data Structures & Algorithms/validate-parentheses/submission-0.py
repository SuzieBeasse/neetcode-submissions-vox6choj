class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 1:
            return False
        hm = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []

        for c in s:
            if c not in hm.keys():
                stack.append(c)
            else:
                if not stack or stack[-1] != hm[c]:
                    return False
                stack.pop()
        return len(stack) == 0
