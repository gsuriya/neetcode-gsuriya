class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """

        collapse window when profit is negative
        
        dynamically update max_profit

        """

        max_profit = 0
        L = 0

        for R in range(len(prices)):
            if prices[R] < prices[L]: # collapse window cus negative profit
                L = R
            
            max_profit = max(max_profit, prices[R] - prices[L])

        return max_profit