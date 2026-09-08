import heapq
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if n == k or n == 0:
            return n
        
        l = 0
        freq = dict()

        ans = 0
        curr_max = 0
        for r in range(n):
            freq[s[r]] = freq.get(s[r], 0) + 1
            curr_max = max(curr_max, freq[s[r]])
            while r - l + 1 - curr_max > k:
                freq[s[l]] -= 1
                l += 1
            ans = max(ans, r - l+1)
            
        return ans

            

