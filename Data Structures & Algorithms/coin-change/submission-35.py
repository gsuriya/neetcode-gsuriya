class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """

        don't care ab duplicate combos --> use all coins at each dfs

        use: 10, 1, 1

                12
             2      7 
          1           2
        0

        """

        cache = {} # amount --> min # of coins to reach 0
        def dfs(amount):
            if amount == 0: 
                return 0

            if amount in cache:
                return cache[amount]
            
            if amount < 0:
                return float('inf')
                
            count = float('inf')
            for c in coins:
                count = min(count, 1 + dfs(amount - c))
            
            cache[amount] = count
            return count
        
        res = dfs(amount)
        return res if res != float('inf') else -1 

