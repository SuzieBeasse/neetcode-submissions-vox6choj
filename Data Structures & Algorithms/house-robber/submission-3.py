
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_prev = 0
        prev = 0 

        for num in nums:
            curr = max(num + prev_prev, prev)
            prev_prev = prev
            prev = curr
        
        return prev
        