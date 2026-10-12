class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = dict()
        n = len(nums)
        for i in range(n):
            if target - nums[i] in hm:
                return [hm[target - nums[i]], i]
            hm[nums[i]] = i
        