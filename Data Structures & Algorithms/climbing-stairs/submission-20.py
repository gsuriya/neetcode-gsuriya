class Solution:
    def climbStairs(self, n: int) -> int:
        """
        how many ways to get from floor node to the END node?
        - sum(# of ways of nodes AROUND them)

        floor 1  2  3  4  5

        2 directions of movement:
        - 1 node ahead
        - 2 nodes ahead

        cache ways to get to end node from N node

        """

        cache = {} # node n --> # of ways from node n to end
        # returns number of ways from n node to end node
        def dfs(i):
            if i in cache:
                return cache[i]
            if i == n: # hit target
                return 1
            if i > n: # overshot
                return 0

            ways_from_curr_node = dfs(i+1) + dfs(i+2)
            cache[i] = ways_from_curr_node
            return ways_from_curr_node
        
        return dfs(0)

