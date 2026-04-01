class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
           
           i
cost     1 2 3 end
dp       3 2 3  0


        dp = [cost[-1], 0]
        
        dp[i] = min cost to get to end
        dp[i] = cost[i] + min(cost[i+1], cost[i+2])

        return min(dp[0], dp[1])

        """

        dp = [cost[-1], 0]

        for i in range(len(cost)-2, -1, -1):
            tmp = dp[0]
            dp[0] = cost[i] + min(dp[0], dp[1])
            dp[1] = tmp
        
        return min(dp[0], dp[1])


