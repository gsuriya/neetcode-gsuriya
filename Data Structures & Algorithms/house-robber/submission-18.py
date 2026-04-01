class Solution:
    def rob(self, nums: List[int]) -> int:
        """

                    i
nums    2  9  8  3  6
dp      2  9  10 12 16

        dp = [nums[0], max(nums[0], nums[1])]

        dp[i] = either rob curr house + 2 to the left OR 
        dp[i] = max(nums[i] + dp[0], dp[1])

    
        """ 
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)):
            tmp = dp[1]
            dp[1] = max(nums[i]+dp[0], dp[1])
            dp[0] = tmp
        
        return dp[-1]