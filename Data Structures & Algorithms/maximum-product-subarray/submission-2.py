class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """

        at each i
        - extend from prev index
        - start fresh and discard prev arr (starting fresh is better and using prev only hurts us)

             i
        2 4 -3 5

        curr_min = 4 --> -12
        curr_max = 8 --> 

        """

        res = nums[0]
        curr_min, curr_max = nums[0], nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                curr_min, curr_max = curr_max, curr_min

            # extend or start fresh
            curr_min = min(curr_min * nums[i], nums[i])
            curr_max = max(curr_max * nums[i], nums[i])
            
            res = max(res, curr_max)
        
        return res




