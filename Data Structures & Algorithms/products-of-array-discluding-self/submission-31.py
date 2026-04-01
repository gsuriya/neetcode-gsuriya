class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """

        1. populate res w/ prefix shifted to the right
        2. multiply by suffix shifted to the left

        """
        res = [1] * len(nums)

        # res w/ shifted prefix
        product = 1
        for i in range(1, len(res)):
            product *= nums[i-1]
            res[i] = product
        
        # multiply res by shifted suffix
        product = 1
        for i in range(len(res)-1, -1, -1):
            res[i] = product * res[i]
            product *= nums[i]
        
        return res
        


