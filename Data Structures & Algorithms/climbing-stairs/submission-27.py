class Solution:
    def climbStairs(self, n: int) -> int:
        """

          i
        0 1 2 3
dp      3 2 1 1

        """

        dp = [1, 1]

        for i in range(n-2, -1, -1):
            tmp = dp[0]
            dp[0] = dp[0] + dp[1]
            dp[1] = tmp
        
        return dp[0]
