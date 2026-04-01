class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """

        T = 3

        M
        L R
        1 3


        T = 3

                M     
        4 5 6 7 1 2 3 


        upper half
        - T is larger --> go right
        - T smaller and > nums[0] --> go left
        - T smaller and < nums[0] --> go right

        lower half
        - T is larger and > nums[-1] --> go left
        - T is larger and < nums[-1] --> go right
        - T is smaller --> go left
 
        """

        L, R = 0, len(nums)-1
        
        while L <= R:
            mid = (L+R) // 2

            if nums[mid] == target:
                return mid

            # mid is not a valid candidate anymore:
            # upper half
            elif nums[mid] > nums[R]:
                # find larger value
                if target > nums[mid]:
                    L = mid+1
                # find smaller value
                else:
                    if target >= nums[L]: R = mid-1
                    elif target < nums[L]: L = mid+1

            # lower half
            else:
                # find smaller value
                if target < nums[mid]:
                    R = mid-1
                # find larger value
                else:
                    if target > nums[R]: R = mid-1
                    elif target <= nums[R]: L = mid+1
        
        return -1















                 
