class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """

        combination sum w/ caching

        use (i)
        ~use (i+1)

        bubble up min number of coins used

        """
        cache = {} # i --> min coins used
        def dfs(i, path_sum, coins_used):
            if (i, path_sum, coins_used) in cache:
                return cache[(i, path_sum, coins_used)]

            if path_sum == amount:
                return coins_used
            if i == len(coins) or path_sum > amount:
                return float('inf')
        
            cache[(i, path_sum, coins_used)] = min(
                dfs(i, path_sum + coins[i], coins_used + 1), # use (i)
                dfs(i+1, path_sum, coins_used)               # ~use (i+1)
            ) 

            return cache[(i, path_sum, coins_used)]
        
        res = dfs(0, 0, 0)
        return res if res != float('inf') else -1



