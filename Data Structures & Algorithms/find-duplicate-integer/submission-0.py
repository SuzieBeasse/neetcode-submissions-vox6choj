class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        num_set = set(nums)
        k = n - len(num_set)
        j = sum(nums)-sum(num_set)

        return j // k
        

# Design
# set of nums -> exactly x differents
# len(nums) - len(set(nums)) => how many different 
# sum(nums) - sum(set(nums)) => 