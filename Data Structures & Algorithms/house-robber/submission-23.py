class Solution:
    def rob(self, nums: List[int]) -> int:
        """

        rob
        ~rob

            i
    $   2 9 8  3 6
    dp  2 9 10  

        max(curr + dp[0], dp[1])

        """
        if len(nums) == 1:
            return nums[0]

        dp = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)):
            tmp = dp[1]
            dp[1] = max(nums[i] + dp[0], dp[1])
            dp[0] = tmp 
        
        return dp[-1]
            

        
