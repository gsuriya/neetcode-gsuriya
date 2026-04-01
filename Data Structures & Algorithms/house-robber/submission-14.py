class Solution:
    def rob(self, nums: List[int]) -> int:

        # recurring subproblems cus at each node
        # --> max_loot at node i

        cache = {} # node --> max_loot
        def dfs(i):
            if i in cache:
                return cache[i]
            if i >= len(nums):
                return 0
            
            yes_rob = nums[i] + dfs(i+2) # skip next adjacent house
            no_rob = dfs(i+1) # dont rob this house, just go to next adjacent one

            curr_node_max_loot = max(yes_rob, no_rob)
            cache[i] = curr_node_max_loot
            return curr_node_max_loot
        
        # return max of robbing or not robbing at 0
        return dfs(0)
