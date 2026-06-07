class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """

        2 -3 4 -2 2 1 -1 4

        if curr_sum negative --> throw away cus it doesn't help at all

        """
        
        max_sum = float("-inf") # ALW do float('-inf') at first to be safe
        curr_sum = 0
        L = 0

        for R in range(len(nums)):
            # shrink - collapse window
            if curr_sum < 0:
                curr_sum = 0
                L = R
            
            # expand
            curr_sum += nums[R]

            # update
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
            

