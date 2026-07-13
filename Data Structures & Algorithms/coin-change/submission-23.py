class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """

        dfs(amount) --> min coins u need to reach 0 from this amount
        
        """

        cache = {} # amount --> min coins needed to reach 0
        def dfs(amount):
            if amount in cache:
                return cache[amount]

            if amount == 0:
                return 0 # 0 coins needed to reach 0
            if amount < 0:
                return float('inf') # this combo didn't work
            
            # test out every coin
            count = float('inf')
            for c in coins:
                count = min(count, 1 + dfs(amount - c))

            cache[amount] = count
            return count
        
        res =  dfs(amount)
        return res if res != float('inf') else -1
