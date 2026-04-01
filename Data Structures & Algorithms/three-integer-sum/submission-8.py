class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """


        -1  0  1  2  -1  -4

         i  L            R
        -4 -2  -2  0  1  6

        """
        nums.sort()
        res = []

        for i in range(len(nums)):
            # duplicate triplet
            if i >= 1 and nums[i] == nums[i-1]:
                continue

            L, R = i+1, len(nums)-1
            while L < R:
                sum_ = nums[i] + nums[L] + nums[R]
                if sum_ < 0:
                    L += 1
                elif sum_ > 0:
                    R -= 1
                else:
                    # found triplet
                    res.append([nums[i], nums[L], nums[R]])

                    # move L pointer, R pointer will update by itself
                    L += 1
                    while L < R and nums[L] == nums[L-1]:
                        L += 1
        
        return res




