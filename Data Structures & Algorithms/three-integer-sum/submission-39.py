class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """

        sort to
        1. skip duplicates (for i and L)
        2. two sum II algo

         i       L   R
        -4 -1 -1 0 1 2 

        res = [
        
        ]

        """
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            L, R = i+1, len(nums)-1

            while L < R:
                if nums[i] + nums[L] + nums[R] > 0:
                    R -= 1
                elif nums[i] + nums[L] + nums[R] < 0:
                    L += 1
                else:
                    res.append([nums[i], nums[L], nums[R]])
                    L += 1

                    # skip duplicates
                    while L < R and nums[L-1] == nums[L]:
                        L += 1
        
        return res


        

