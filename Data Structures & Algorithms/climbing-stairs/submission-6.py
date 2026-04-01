class Solution:
    def climbStairs(self, n: int) -> int:
        """

        n = 5

        0 1 2 3 4

        """

        cache = {}
        # given an n steps, tells you how many ways to walk down it
        def dfs(n):
            # base case - overshoot, on target
            if n in cache: # alr calc how many was to walk down w/ n steps
                return cache[n]
            if n < 0: # overshoot
                return 0
            if n == 0: # on target
                return 1
            
            count = 0
            count = dfs(n-1) + dfs(n-2)
            cache[n] = count
            return count
        return dfs(n)


