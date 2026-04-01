class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        T = 1


        L   m       R
        3 4 5 6 0 1 2

        upper half
            smaller
             T < nums[L]? --> go right
             T >= nums[L]? --> go left

            larger --> go right


        lower half
            smaller --> go left

            larger
             T > nums[R]? --> go left
             T <= nums[R]? --> go right

        """

        L, R = 0, len(nums)-1
        
        while L <= R:
            mid = (L+R) // 2

            if nums[mid] == target:
                return mid

            # upper half
            elif nums[mid] > nums[R]:
                # smaller
                if target < nums[mid]:
                    if target < nums[L]:
                        L = mid+1
                    else:
                        R = mid-1
                # larger
                else:
                    L = mid+1

            # lower half
            else:
                # smaller
                if target < nums[mid]:
                    R = mid-1
                # larger
                else:
                    if target > nums[R]:
                        R = mid-1
                    else:
                        L = mid+1
        
        return -1
                        

             
        

        