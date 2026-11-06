class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n =len(prices)

        curr_min = prices[0]
        profit = 0

        for price in prices:
            if price - curr_min > profit:
                profit = price - curr_min
            curr_min = min(curr_min, price)
        
        return profit
            