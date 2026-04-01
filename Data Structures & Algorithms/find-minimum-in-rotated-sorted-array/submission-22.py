class Solution:
    def findMin(self, nums: List[int]) -> int:
        """

        if its sorted, then logically j keep going right

        so comparing mid to R tells u what half ur in

              R
              L m
        3 4 5 6 1 2

        """

        L, R = 0, len(nums)-1

        while L < R:
            mid = (L+R) // 2

            # in upper half, so go right into lower half
            if nums[mid] > nums[R]:
                L = mid+1
            # in lower half, so keep going left
            else:
                R = mid
        
        return nums[L]





