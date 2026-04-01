class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        start at node 0 or node 1
        --> return min(dfs(0), dfs(1))
        - dfs returs min_cost from starting location

cost = [1 2 3]
        
        0 1 2 end

        directional movement
        - 1 node ahead (i+1)
        - 2 nodes ahead (i+2)

        curr_node_min_cost = min (dfs(i+1), dfs(i+2))
        return curr_node_min_cost

        base case: 
        1. add the end
         - return cumulative cost at that point
        2. overshot
         - return float('inf') so cost not considered in min()
        """

        # returns min_cost to go from this node i to the end
        def dfs(i, cumulative_cost):
            # if at end
            if i == len(cost):
                # return curr cumulative cost
                return cumulative_cost
            # if overshot
            if i > len(cost):
                return float('inf') # this cost cancels out in min()

            # return curr node min_cost
            curr_node_min_cost = min(dfs(i+1, cumulative_cost + cost[i]), dfs(i+2, cumulative_cost + cost[i]))

            return curr_node_min_cost
        
        return min(dfs(0,0), dfs(1,0))



