class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        subarray with monotonocity so sliding window works

        length of smallest subarray w/ sum >= target

        """

        min_length = float('inf')
        L = 0
        window_sum = 0 # current sum

        for R in range(len(nums)):
            # expand
            window_sum += nums[R]

            # if sum >= target --> shrink
            while window_sum >= target:
                # update length
                min_length = min(min_length, R-L+1)
                window_sum -= nums[L]
                L += 1
        
        return min_length if min_length != float('inf') else 0
            
            