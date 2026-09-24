class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        prev = 1
        prev_prev = 1
        
        for i in range(n-1):
            curr = prev
            prev = prev + prev_prev
            prev_prev = curr
        
        return prev
        
        