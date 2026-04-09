class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 1
        curr = 0
        n = len(nums)
        if n==1:
            return 0
        while curr + nums[curr] < n-1:
            max_jump = float('-inf')
            ans += 1
            for i in range(curr+1, min(curr+nums[curr]+1, n)):
                if i+nums[i] >= max_jump:
                    max_jump = i+nums[i]
                    curr = i

        return ans
        