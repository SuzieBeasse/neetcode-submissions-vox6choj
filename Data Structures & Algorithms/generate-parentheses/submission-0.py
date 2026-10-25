class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        
        self.n = n
        self.ans = []
        self.backTrack(1, 0, ["("])
        return self.ans
    
    def backTrack(self, o: int, c: int, curr: list):
        if o + c == 2*self.n:
            self.ans.append("".join(curr))
            return
        if o > c:
            curr.append(")")
            self.backTrack(o, c+1, curr)
            curr.pop()
        if o < self.n:
            curr.append("(")
            self.backTrack(o+1, c, curr)
            curr.pop()
        
        
        

        

        


# Design
# Backtracking problem
# Startwith a list with just an opening parenthesis
# if o == c => open
# if o > c => open, backtrack, close
