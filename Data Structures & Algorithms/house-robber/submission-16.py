class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        recurring subproblems cus at each node
         --> max_loot at node i and onwards

        0 1 2 3  4         
 nums   1 2 3 1 end

 dp     4 3 3 1  0  

    curr_node_value = max(curr_node.val + dp[1], dp[0])

        """

        dp = [nums[-1], 0]

        for i in range(len(nums)-2, -1, -1):
            tmp = dp[0]
            dp[0] = max(nums[i] + dp[1], dp[0])
            dp[1] = tmp
        
        return dp[0]
        

