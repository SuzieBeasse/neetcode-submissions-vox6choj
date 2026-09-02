from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)
        prev_prev = 0
        prev = 0 

        for num in nums:
            curr = max(num + prev_prev, prev)
            prev_prev = prev
            prev = curr
        
        return prev
        