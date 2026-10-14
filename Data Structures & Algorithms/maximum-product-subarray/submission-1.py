class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        ans = float('-inf')
        curr_p = 1
        curr_n = 1

        for num in nums:
            if num == 0:
                ans = max(ans, 0)
                curr_p = 1
                curr_n = 1
            else:
                temp = curr_p * num
                curr_p = max(curr_p * num, num, curr_n*num)
                curr_n = min(temp, num, num*curr_n)
                ans = max(ans, curr_p)
        
        return ans




