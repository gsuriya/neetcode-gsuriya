class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # window condition: increasing numbers

        # L: if R < L is less, move L to R
        # R:


        """
           L        
                   R
        10 4 6 5 1 3


        dynamic max profit as R moves

        """

        L = 0
        max_profit = 0
        for R in range(len(prices)):
            max_profit = max(prices[R]-prices[L], max_profit)
            if prices[R] <= prices[L]:
                L = R
        return max_profit