class Solution:
    def climbStairs(self, n: int) -> int:
        """

        n = 5

        0 1 2 3 4

        """

        def dfs(n):
            # base case - overshoot, on target
            if n < 0: # overshoot
                return 0
            if n == 0: # on target
                return 1
            
            count = 0
            count = dfs(n-1) + dfs(n-2)
            return count
        return dfs(n)


