class Solution:
    def findMin(self, nums: List[int]) -> int:
        """

        if its sorted, then logically j keep going right

        so comparing mid to R tells u what half ur in

                R
                M
                L 
        3 4 5 6 1 2 3

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
        
        return nums[R]


