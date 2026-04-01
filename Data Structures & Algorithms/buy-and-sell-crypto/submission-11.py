class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0

        max_profit = 0

        for R in range(len(prices)):
            if prices[R] < prices[L]:
                L = R
            
            max_profit = max(max_profit, prices[R]-prices[L])
        
        return max_profit