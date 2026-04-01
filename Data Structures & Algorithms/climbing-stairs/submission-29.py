class Solution:
    def climbStairs(self, n: int) -> int:
        """

        n = 2

          i
        0 1 2 end
dp      2 1 1  0

        dp = [1, 0]

        dp[i] = dp[i+1] + dp[i+2]

        """

        dp = [1, 0]

        for i in range(n-1, -1, -1):
            tmp = dp[0]
            dp[0] = dp[0] + dp[1]
            dp[1] = tmp
        
        return dp[0]


        