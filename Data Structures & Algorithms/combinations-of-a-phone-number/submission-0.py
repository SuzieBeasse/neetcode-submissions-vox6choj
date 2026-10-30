from collections import defaultdict
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        hm = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        ans = []

        def backtrack(curr):
            if len(curr) == len(digits):
                ans.append(''.join(curr[:]))
                return
            i = len(curr) 
            d = digits[i]
            for c in hm[d]:
                curr.append(c)
                backtrack(curr)
                curr.pop()
        
        backtrack([])
        return ans