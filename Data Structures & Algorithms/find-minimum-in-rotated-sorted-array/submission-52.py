class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        goal: go smaller

        upper
        - go right

        lower
        - go left


        """
        L, R = 0, len(nums)-1

        while L < R:
            mid = (L+R) // 2

            # upper
            if nums[mid] > nums[R]: # mid ruled out as not min
                L = mid+1
            # lower
            else:
                R = mid
        
        return nums[R]

        