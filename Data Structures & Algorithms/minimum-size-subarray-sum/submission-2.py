class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """

        return min_length else 0 if no valid

        goal:
        - find smallest subarray where sum >= target

        sliding window
        - expand --> expand until curr_sum >= T
        - shrink --> shrink until curr_sum < T
            - update (3)

        T = 5
        min_length = inf
        curr_sum = 4

        L     R
        1 2 1
        """

        min_length = float('inf')
        L = 0
        curr_sum = 0 # window

        for R in range(len(nums)):
            # expand
            curr_sum += nums[R]

            # shrink
            while curr_sum >= target:
                # - update
                min_length = min(min_length, R-L+1)

                curr_sum -= nums[L]
                L += 1

        return min_length if min_length != float('inf') else 0



