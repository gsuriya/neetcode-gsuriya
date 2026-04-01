class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        target = 3

        m
        l  r
        1  3
          
        l     m     r
        4  5  1  2  3 

        l     m        r
        3  4  5  6  1  2

        """

        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r) // 2

            if target > nums[mid]:
                # move right
                if ((nums[mid] < nums[r] and target <= nums[r]) # both in lower half or both in upper half
                    or (nums[mid] > nums[r] and target > nums[r])):
                    l = mid+1 # move right
                else:
                    r = mid-1 # move left

               
            elif target < nums[mid]:
                # move left
                if ((nums[mid] < nums[r] and target < nums[r]) # both in lower half or both in upper half
                    or (nums[mid] > nums[r] and target > nums[r])):
                    r = mid-1 # move left
                else:
                    l = mid+1 # move right
            else:
                return mid

        return -1
