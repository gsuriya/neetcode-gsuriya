class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        circular DP --> convert to 2 linear DP problems
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_dp(nums[1:]), self.rob_dp(nums[:len(nums)-1]))
    
    """
   
           
    2 9 8 3 6 end

dp          6  0
    """

    def rob_dp(self, nums):
        dp = [nums[-1], 0]

        for i in range(len(nums)-2, -1, -1):
            tmp = dp[0]
            dp[0] = max(nums[i]+dp[1], dp[0])
            dp[1] = tmp
        
        return dp[0]
