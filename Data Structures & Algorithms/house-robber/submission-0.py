from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dp(i, curr):
            if i > n-1:
                return curr
            return max(dp(i+1, curr), dp(i+2, curr + nums[i]))
        
        return dp(0, 0)
        