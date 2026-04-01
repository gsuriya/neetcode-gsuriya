class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        T = 4

               m
               R
               L  
        -1 0 2 4 6 8

        """
        L, R = 0, len(nums)-1

        while L <= R: # if L and R on target then want mid to execute and find target
            mid = (L+R) // 2

            if target > nums[mid]:
                L = mid+1
            elif target < nums[mid]:
                R = mid-1
            else:
                return mid
        
        return -1
