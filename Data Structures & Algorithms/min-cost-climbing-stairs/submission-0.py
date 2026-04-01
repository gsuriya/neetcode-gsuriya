class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """

        start at either floor 0 or floor 1
        dfs(0)
        dfs(1)
        return min_cost

        choice each floor, you pay a cost 
        --> move 1 floor up OR move 2 floors up

        base case: on top floor i = len(cost), dynamically update min_cost with cost atp

        """
        min_cost = float('inf')

        def dfs(floor_i, path_cost):
            nonlocal min_cost

            # base case - hit top floor, or overshoot top floor
            if floor_i == len(cost):
                min_cost = min(path_cost, min_cost)
                return

            if floor_i > len(cost): # overshot
                return

            path_cost += cost[floor_i]

            dfs(floor_i+1, path_cost) # move up one floor
            dfs(floor_i+2, path_cost) # move up two floors
        
        dfs(0, 0)
        dfs(1, 0)

        return min_cost