class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        maxP = 0 # data structure for window, dynamically updating
        # window has to be INCREASING

        """
                  R        
            L
        [10,1,5,6,7,1]

        """

        for R in range(len(prices)):
            # condition to move L
            if prices[R] < prices[L]:
                L = R

            maxP = max(maxP, prices[R]-prices[L])
        
        return maxP