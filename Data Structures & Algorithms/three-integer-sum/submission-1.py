class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []

        for i in range(0, n-2):
            l = i+1
            r=n-1
            num = nums[i]
            if i > 0 and num == nums[i-1]:
                continue

            while l < r:
                if nums[l] + nums[r] + num == 0:
                    print(l,r)
                    ans.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
 
                elif nums[l] + nums[r] + num < 0:
                    l +=1
                else:
                    r -= 1
            
        return ans



# Design
# Sort array nums
# Choose first element. i
# define left and right pointer l = i+1, r = n-1
# adjust left and right so their sum is == - nums[i], if not possible choose next first element