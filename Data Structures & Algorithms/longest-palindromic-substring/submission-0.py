class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ''
        ans = s[0]

        #Odd length palindromes
        for i in range(1, n-1):
            l = i
            r = i

            while l > 0 and r < n-1 and s[l-1] == s[r+1]:
                l-=1
                r+= 1
            if (r - l + 1) > len(ans):
                ans = s[l:r+1]
        
        # Even length palindromes
        for i in range(n-1):
            if s[i] == s[i+1]:
                # possible center of a palindrome
                l = i
                r = i+1
                while l > 0 and r < n-1 and s[l-1] == s[r+1]:
                    l-=1
                    r+=1
                if (r-l+1) > len(ans):
                    ans = s[l:r+1]
        
        return ans



        