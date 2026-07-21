class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
      nums  1  2  4  6
            
            1  1  2  8  24 ->
    <-  48 48 24 6  1
        
        res 48 24 12 8


        1. get shifted prefix
        2. multiply by shifted suffix

        """

        res = [1] * len(nums)

        # shifted prefix
        product = 1
        for i in range(len(nums)):
            res[i] = product
            product *= nums[i]
        
        # shifted suffix
        product = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= product
            product *= nums[i]
        
        return res
        









