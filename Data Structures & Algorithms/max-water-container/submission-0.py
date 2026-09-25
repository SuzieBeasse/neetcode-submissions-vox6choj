class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        ans = 0
        l = 0
        r = n-1

        while l < r:
            curr = min(heights[l], heights[r])
            ans = max(ans, curr * (r - l))
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        return ans
        