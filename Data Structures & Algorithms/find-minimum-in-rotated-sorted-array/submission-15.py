class Solution:
    def findMin(self, nums: List[int]) -> int:
        # kokos bananas: min bin search algo

        # min of rotated array: ?

        l, r = 0, len(nums)-1

        """
                    r
                    m  
                    l    
        3  4  5  6  1  2  3

        """

        while l < r:

            m = (l + r) // 2

            # if m > r --> go right
            if nums[m] > nums[r]:
                l = m+1
            # if m <= r --> go left
            else:
                r = m
        return nums[l]





