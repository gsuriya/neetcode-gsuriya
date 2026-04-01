class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        i represents floor #

        cost = [1,2,3]
                i

        0  1  2

        directional movement for each node:
        - move 1 node ahead (i+1)
        - move 2 nodes ahead (i+2)

        curr_node_cost = min(dfs(i+1), dfs(i+2))
        - dfs(i) returns the min cost to reach end from that node

        base cases: 
        1. i == len(cost) which is top floor --> return 0 cost
        2. i > len(cost) which is overshot --> return float('inf') so min() b/c this is an invalid way to get to top floor
        """

        cache = {} # floor --> min_cost to get to end floor from this floor
        # returns min cost from floor i to top floor
        def dfs(i, cst):
            # if i in cache:
            #     return cache[i]
            if i == len(cost): # top floor reached
                return cst
            if i > len(cost):
                return float('inf')

            min_curr_floor_cost = min(dfs(i+1, cst+cost[i]), dfs(i+2, cst+cost[i]))
            # cache[i] = min_curr_floor_cost
            return min_curr_floor_cost
        
        return min(dfs(0, 0), dfs(1, 0))

