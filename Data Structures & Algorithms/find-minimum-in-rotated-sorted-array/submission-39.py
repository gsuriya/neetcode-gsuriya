class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        goal: find min

                L
                R
               
        3 4 5 6 1 2

        upper half
        - go right

        lower half
        - go left
    

        """

        L, R = 0, len(nums)-1

        while L < R: # no = cus infinite loop with R keep going to mid
            mid = (L+R) // 2

            # upper half
            if nums[mid] > nums[R]:
                L = mid+1
            # lower half
            else:
                R = mid # you don't know that mid is excluded here, it could be the mid

        return nums[L]




        


