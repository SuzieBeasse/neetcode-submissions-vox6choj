class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        if len(s) == 0:
            return ans
        n = len(s)
        #Palindrom with odd length
        for i in range(n):
            j = 0
            ans += 1
            while i - j -1 >= 0 and i + j + 1 < n and s[i-j-1] == s[i+j+1]:
                ans += 1
                j+=1
        
        #Palindrom with even length
        for i in range(n-1):
            if s[i] == s[i+1]:
                j = 0
                ans += 1
                while i - j -1 >= 0 and i + 1 + j + 1 < n and s[i-j-1] == s[i+j+2]:
                    ans += 1
                    j+=1
        
        return ans
        