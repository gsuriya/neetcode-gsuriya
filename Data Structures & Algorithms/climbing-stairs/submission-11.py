class Solution:
    def climbStairs(self, n: int) -> int:
        """
        only need visited set if the dfs traversal
        collapses in on itself and makes a loop

        n = 5

        curr_step = 0

        1 2 3 4 5

        """


        def dfs(curr_step):
            if curr_step == n:
                return 1
            if curr_step > n:
                return 0


            count_ways = dfs(curr_step+1) + dfs(curr_step+2)

            return count_ways
        
        return dfs(0)



