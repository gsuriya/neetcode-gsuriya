class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create prefix array (shifted left)
        total = 1
        prefix = [1 for i in range(len(nums))]
        for i in range(1, len(prefix)):
            total *= nums[i-1]
            prefix[i] = total

        # create suffix array (shifted right)
        total = 1
        suffix = [1 for i in range(len(nums))]
        for i in range(len(suffix)-2, -1, -1):
            total *= nums[i+1]
            suffix[i] = total

        # iterate through pre and suf to populate res array
        res = [1 for i in range(len(nums))]
        for i in range(len(res)):
            res[i] = prefix[i] * suffix[i]
        return res