class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
          L              R
        [-1, 0, 2, 4, 6, 8]

        """
       
        L = 0
        R = len(nums)-1

        while L <= R:
            mid  = (L + R) // 2

            if target > nums[mid]:
                L = mid+1
            elif target < nums[mid]:
                R = mid-1
            else: # target == nums[mid]
                return mid

        return -1

