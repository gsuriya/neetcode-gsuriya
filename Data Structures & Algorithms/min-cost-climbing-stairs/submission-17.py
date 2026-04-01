class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        goal: return min cost for curr_node

        formula: curr_node cost + min of surrounding node costs 
        curr_node_min_cost = cost[i] + min(dfs(i+1), dfs(i+2))

        0  1  2 end

        """
        cache = {} # node --> min_cost from this node to end
        def dfs(i):
            if i in cache:
                return cache[i]
            if i >= len (cost): # reached end
                return 0
            curr_node_min_cost = cost[i] + min(dfs(i+1), dfs(i+2))
            cache[i] = curr_node_min_cost
            return curr_node_min_cost

        
        return min(dfs(0), dfs(1))