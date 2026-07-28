class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """

        1-D DP solution 

        dp[i] is LIS starting from index i
        dp[i] = 1 + max(dp[j's where the nums[j] is increasing])

                  i j
        9 1 4 2 3 3 7
    dp          3 2 1


        """

        dp = [0] * len(nums)
        dp[-1] = 1

        for i in range(len(nums)-2, -1, -1):
            max_length = 0

            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    max_length = max(max_length, dp[j])
            
            dp[i] = 1 + max_length
        
        return max(dp)


        