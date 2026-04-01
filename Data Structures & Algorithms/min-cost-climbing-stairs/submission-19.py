class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        goal: return min cost for curr_node

        formula: curr_node cost + min of surrounding node costs 

        node 2: 20 + min(0, 0) --> 20

        node 1: 15 + min(20, 0) --> 35

        10 + min(35, 20) --> 30

        curr_node_min_cost = cost[i] + min(dfs(i+1), dfs(i+2))

graph   0    1    2   end
cost    10   15   20

             i          
dp =    30   35   20   0

        """
        # [20, 0]
        # tmp = 20 
        dp = [cost[-1], 0]

        for i in range(len(cost)-2, -1, -1):
            tmp = dp[0]
            dp[0] = cost[i] + min(dp[0], dp[1])
            dp[1] = tmp
        
        return min(dp[0], dp[1])


        