class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """

        L
        2 -3 4 -2 2 1 -1 4

        sliding window
        throw away prev result if negative (collapse window)
        """

        max_sum = float('-inf')
        cumulative_sum = 0

        for n in nums:
            # shrink
            if cumulative_sum < 0:
                cumulative_sum = 0

            # expand
            cumulative_sum += n

            # update
            max_sum = max(max_sum, cumulative_sum)
        
        return max_sum

