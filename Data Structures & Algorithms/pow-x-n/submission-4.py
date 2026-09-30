class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if x == 0.0:
            return x

        ans = self.myPow(x, abs(n) // 2) 
        ans = ans * ans
        if n % 2 == 1:
            ans *= x
        
        return ans if n > 0 else 1/ans
            
       
            
        