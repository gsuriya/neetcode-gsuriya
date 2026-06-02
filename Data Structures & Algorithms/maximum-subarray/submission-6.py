class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """

        if cumulative_sum is negative, js discard the entire windoow ts is useless, better to have 0

        """

        L = 0
        curr_sum = 0
        max_sum = float('-inf')

        for R in range(len(nums)):
            # shrink - throw away entire window
            if curr_sum < 0:
                curr_sum = 0
                L = R

            # expand
            curr_sum += nums[R]

            # update
            max_sum = max(max_sum, curr_sum)
        
        return max_sum