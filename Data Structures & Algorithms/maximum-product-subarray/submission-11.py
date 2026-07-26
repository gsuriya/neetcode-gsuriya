class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """

        at each n:
        - extend
        - start fresh from here

        """

        curr_min = curr_max = res = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]
            tmp = curr_min

            curr_min = min(curr_min * n, n, curr_max * n)
            curr_max = max(tmp * n, n, curr_max * n)
            res = max(res, curr_max)

        return res