class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """

        amount --> min # of coins to get there

          i           
    dp  0               
amount  0 1 2 3 4 5 6 7
        
        dp[i] = 1 + min(dp[all amounts u can possibly get to from here])
        
        """

        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for a in range(1, len(dp)):
            min_coins = float('inf')
            
            # all valid amounts u can get to from here
            for c in coins:
                if a-c >= 0: # amount - coin
                    min_coins = min(min_coins, 1 + dp[a-c]) 
            
            dp[a] = min_coins # map amount --> min number of coins needed

        return dp[-1] if dp[-1] != float('inf') else -1



