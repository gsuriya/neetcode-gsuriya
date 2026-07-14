class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """

        at each n
        - extend
        - start fresh

        """

        curr_min, curr_max, res = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            tmp = curr_min
            curr_min = min(curr_min*nums[i], curr_max*nums[i], nums[i])
            curr_max = max(tmp*nums[i], curr_max*nums[i], nums[i])
            res = max(res, curr_max)
        
        return res