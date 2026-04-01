class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        # small number @ start --> big num @ end
        # sliding window --> when R lands on smaller num than L, move L to R

        L = 0
        
        for R in range(len(prices)):
            # move L to R if R is smaller
            if prices[R] < prices[L]: # check dup case later
                L = R
            profit = prices[R] - prices[L]
            max_profit = max(profit , max_profit)

        return max_profit