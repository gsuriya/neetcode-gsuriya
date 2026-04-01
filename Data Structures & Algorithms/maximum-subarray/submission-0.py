class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cumulative_sum = 0

        """

        -4, -1, -2, -3

        """

        for n in nums:
            # throw away prev if < 0
            if cumulative_sum < 0:
                cumulative_sum = 0
            
            cumulative_sum += n
            max_sum = max(max_sum, cumulative_sum)
        
        return max_sum