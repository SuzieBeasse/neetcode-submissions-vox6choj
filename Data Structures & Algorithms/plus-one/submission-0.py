class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        r = 1
        i = n - 1

        while i >=0 and r > 0:
            d = digits[i]
            digits[i] = (d + r) % 10
            r = (d + r)//10
            i-=1

    
        if r == 0:
            return digits
        
        ans = []
        ans.append(r)
        for digit in digits:
            ans.append(digit)
        return ans
        




# Design
# Calculate the new value 

        
        