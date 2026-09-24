from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(k):
            if k < 4:
                return k

            return  dp(k-1) + dp(k-2)
        
        return dp(n)
        