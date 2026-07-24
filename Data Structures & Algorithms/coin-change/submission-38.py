class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """

        amount --> min # of coins to reach 0

        [3, 5, 6]

          i    
min c   0 f f 1 f 1                
    a   0 1 2 3 4 5 6 7 8 9 10 11 12

        min c (dp[i]) = 1 + min(dp[every amount u can get to])

        """

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for a in range(1, len(dp)):
            # calculate min number of other coins needed
            min_count = float('inf')
            for c in coins:
                if a - c >= 0:
                    min_count = min(min_count, dp[a - c])
            
            # min coins needed for this amount
            dp[a] = 1 + min_count

        return dp[-1] if dp[-1] != float('inf') else -1

