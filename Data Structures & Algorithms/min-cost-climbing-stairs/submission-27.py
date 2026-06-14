class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """

          i
cost    1 2 3 top
  dp    3 2 3  0  

        curr + min(j1, j2)

        """

        dp = [cost[-1], 0]

        for i in range(len(cost)-2, -1, -1):
            tmp = dp[0]
            dp[0] = cost[i] + min(dp[0], dp[1])
            dp[1] = tmp
        
        return min(dp[0], dp[1])

