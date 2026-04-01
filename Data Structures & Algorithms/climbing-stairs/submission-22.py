class Solution:
    def climbStairs(self, n: int) -> int:
        """

        start at n
        1. dfs(n-1)
        2. dfs(n-2)

        if any of those gets to be 0, then return 1

        return the count

        """
        
        # 3
        def dfs(n):
            if n == 0: # possible path found
                return 1
            if n < 0: # backtrack
                return 0

            count = dfs(n-1) + dfs(n-2)

            return count
        
        return dfs(n)

