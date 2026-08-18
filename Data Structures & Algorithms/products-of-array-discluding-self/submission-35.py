class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """

        
        nums      1  2  4  6

        prefix  1 1, 2, 8, 48 --> 
<--     postfix   48 48 24 6  1

SHIFTED
           prefix  1  1, 2, 8, 48 --> 
<--   postfix   48 48 24 6  1


        res       48 24 12 8

        1. put first 4 for shifted prefix
        2. multiply by shifted postfix

        count = 48

                i
        nums = [1, 2, 4, 6]
        res =  [48, 24, 12, 8]
      
        """

        # put first 4 in res for shifted prefix
        res = [1] * len(nums)
        count = 1
        for i, n in enumerate(nums):
            res[i] *= count
            count *= n

        # multiply by shifted postfix
        count = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= count
            count *= nums[i]
        
        return res


