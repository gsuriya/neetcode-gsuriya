class Solution:
    def findMin(self, nums: List[int]) -> int:
        """

        find minimum

                R
                m
                L 
        3 4 5 6 1 2 

        m > r --> upper half
        - go right
        m <= r --> lower half
        - go left

        """

        L, R = 0, len(nums)-1

        while L < R:
            mid = (L+R) // 2

            # upper half
            if nums[mid] > nums[R]:
                L = mid+1
            # lower half
            else:
                R = mid
        
        return nums[L]
            






