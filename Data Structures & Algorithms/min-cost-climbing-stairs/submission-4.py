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

                0 1 2
        cost = [1,2,3]

        base case: floor 3 hit

                    0
                1       2
              2   3   3   4
            3  4 

        """

        # time: O(2^n)
        # space: O(n)

        cache = {} # floor_i --> min_cost to reach top
        # for any floor_i, return min path_cost
        def dfs(floor_i, path_cost, min_cost):
            # base case - hit top floor, or overshoot top floor
            if floor_i == len(cost):
                min_cost[0] = min(path_cost, min_cost[0])
                return

            if floor_i > len(cost): # overshot
                return

            path_cost += cost[floor_i]

            dfs(floor_i+1, path_cost, min_cost) # move up one floor
            dfs(floor_i+2, path_cost, min_cost) # move up two floors
            return min_cost[0]
        
        return min(dfs(0, 0, [float('inf')]), dfs(1, 0, [float('inf')]))
        
        
