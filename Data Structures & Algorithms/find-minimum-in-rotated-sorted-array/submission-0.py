class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        l = 0
        r = n-1

        if nums[l] < nums[r]:
            return nums[l]
        
        # Binary search
        while l < r:
            mid = (l + r)//2
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        
        return nums[l]
        