class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """

        combination sum w/ caching
        - return MIN coins used to make the combination
        - for valid combinations, bubble up coins used

        use (i)
        ~use (i+1)         
        
                0
              1
            2
          12 2

        """

        cache = {} # path_sum --> min # of coins needed
        def dfs(i, path_sum):
            if (i, path_sum) in cache:
                return cache[(i, path_sum)]

            if path_sum == amount: 
                return 0 # min # of coins needed to reach target from here
            if i == len(coins) or path_sum > amount:
                return float('inf')
            
            use = 1 + dfs(i, path_sum + coins[i])
            skip = dfs(i+1, path_sum)

            cache[(i, path_sum)] = min(use, skip)
            return cache[(i, path_sum)]
        
        res = dfs(0, 0)
        return res if res != float('inf') else -1


