class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """

        buy low sell high


        move L to R if R is lower
        """

        max_profit = 0
        L = 0

        for R in range(len(prices)):
            if prices[R] < prices[L]:
                L = R
            
            max_profit = max(prices[R]-prices[L], max_profit)
        
        return max_profit