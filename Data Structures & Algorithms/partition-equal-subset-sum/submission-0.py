class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        
        t = sum(nums) // 2 #target
        n = len(nums)

        def dp(curr, i):
            if curr == t:
                return True
            if curr > t or i >= n:
                return False
        
            return dp(curr + nums[i], i+ 1) or dp(curr, i + 1)

        return dp(0, 0)