class Solution:
    def climbStairs(self, n: int) -> int:
        """
        bottom-up: base case to answer

        goal: how many ways from floor (node 0) to node 5?

        n = 5
        i    
        0 1 2 3 4 5

  dp =          2 1   

        draw dp array and fill it in
        iterate over rest

        """

        dp = [1, 1]

        for i in range(n-2, -1, -1):
            # curr node = sum of ways to get to node 5 of surrounding nodes
            tmp = dp[0]
            dp[0] = dp[0] + dp[1]
            dp[1] = tmp

        return dp[0]


