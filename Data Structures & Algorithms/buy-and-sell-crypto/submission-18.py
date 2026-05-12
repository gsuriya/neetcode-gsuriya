class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """

        ok so on this day you HAVE to wait until you get to the biggest one
        or actually you can js calculate every time and dynamically update the max

        L       R
        10 1 5 6 7 1


        slding window
        - if R < L

        """

        L = 0
        max_profit = 0 # window

        for R in range(len(prices)):
            if prices[R] < prices[L]:
                L = R
            
            max_profit = max(max_profit, prices[R]-prices[L])

        return max_profit
