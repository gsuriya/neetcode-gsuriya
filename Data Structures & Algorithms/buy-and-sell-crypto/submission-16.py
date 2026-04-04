class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """

        R should alw > L

        want L to be on the smallest thing

           L
                   R
        10 1 5 6 7 1

        """
        
        max_profit = 0
        L = 0

        for R in range(len(prices)):
            if prices[R] < prices[L]:
                L = R
            
            max_profit = max(max_profit, prices[R]-prices[L])

        return max_profit



