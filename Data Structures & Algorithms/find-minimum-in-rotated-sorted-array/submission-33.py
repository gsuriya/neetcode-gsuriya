class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
                
                
              L m R
        3 4 5 6 1 2


        upper half
        - go right (exclude mid)

        lower half
        - go left (include mid)

        """
        L, R = 0, len(nums)-1

        while L < R:
            mid = (L+R) // 2

            # upper half
            if nums[mid] > nums[R]:
                L = mid+1

            # lower half
            elif nums[mid] < nums[R]:
                R = mid
        
        return nums[R]




