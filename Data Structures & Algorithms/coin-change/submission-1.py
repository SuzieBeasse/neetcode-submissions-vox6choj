class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        memo = [-1]*(amount+1)
        
        def dp(curr_amount):
            if curr_amount == 0:
                return 0
            if curr_amount < 0:
                return float('inf')
            if memo[curr_amount]!= -1:
                return memo[curr_amount]

            l = [1 + dp(curr_amount - coin) for coin in coins]
            memo[curr_amount] = min(l)
            return min(l)

        dp(amount)
        return -1 if memo[amount] == float('inf') else memo[amount]
        