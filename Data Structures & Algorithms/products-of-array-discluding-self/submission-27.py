class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
                     i
                 0   1   2   3   4    5

        nums =   1   2   4   6 
        
                                 
        pre  =   1   1   2   8   48   0
        suf  =   0   48  48  24  6    1
        
        res  =       48  24  12  8


        for i in res:
            res[i] = pre[i-1] * suf[i+1]


        """

        # create prefix and suffix product arrays
        pre = [0] * (len(nums)+2)
        suf = [0] * (len(nums)+2)
        pre[0], suf[-1] = 1, 1
        pre[-1], suf[0] = 0, 0

        product = 1
        for i in range(1, len(pre)-1):
            product *= nums[i-1]
            pre[i] = product
        
        product = 1
        for i in range(len(suf)-2, 0, -1):
            product *= nums[i-1]
            suf[i] = product
        

        # construct res arr
        res = []
        for i in range(1, len(pre)-1):
            res.append(pre[i-1] * suf[i+1])
        return res






            

        

        
    

