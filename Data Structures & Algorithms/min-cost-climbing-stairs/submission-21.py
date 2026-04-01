class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
            i
cost    1 2 3 top 0 
dp      3 2 3  0  0

        formula: cost[i] + min(cost[i+1], cost[i+2])

        """

        dp = [0, 0]

        for i in range(len(cost)-1, -1, -1):
            tmp = dp[0]
            dp[0] = cost[i] + min(dp[0], dp[1])
            dp[1] = tmp
        
        return min(dp[0], dp[1])