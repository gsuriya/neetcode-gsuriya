class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """

        kadane's algo --> extend or collapse window

        2 4 -3 5

        curr_min = 2
        curr_max = 2

        """

        res = nums[0]
        curr_min, curr_max = nums[0], nums[0]

        for i in range(1, len(nums)):
            # extend or collapse?
            tmp = curr_min # need ts b/c for second line where curr_max is updated curr_min was alr changed
            # negatives can swap curr max and min so hv to have that in consideration
            curr_min = min(curr_min * nums[i], curr_max * nums[i], nums[i])
            curr_max = max(curr_max * nums[i], tmp * nums[i], nums[i])
            res = max(res, curr_max)
            
        return res

