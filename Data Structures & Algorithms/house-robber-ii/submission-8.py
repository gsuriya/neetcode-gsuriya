class Solution:
    def rob(self, nums: List[int]) -> int:
        """

        2 3 2 --> 4
                

        2 3 2 --> 3
                
        can't rob BOTH endpoints
        - SOLUTION: run on separate subarrays excluding endpoints
        - ensures don't rob both endpoints

        """
        if len(nums) == 1: return nums[0]

        return max(self.house_robber(nums[1:]), self.house_robber(nums[:len(nums)-1]))

    def house_robber(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)):
            tmp = dp[1]
            dp[1] = max(nums[i] + dp[0], dp[1])
            dp[0] = tmp
        
        return dp[-1]


