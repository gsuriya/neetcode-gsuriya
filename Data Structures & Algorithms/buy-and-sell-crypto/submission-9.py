class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """

        buy low sell high

        move R pointer across (dynamically update max)
        if R < L --> move L pointer to R


        """

        L = 0
        max_profit = 0


        for R in range(len(prices)):
            if prices[R] < prices[L]:
                L = R
            
            max_profit = max(max_profit, prices[R] - prices[L])
        
        return max_profit