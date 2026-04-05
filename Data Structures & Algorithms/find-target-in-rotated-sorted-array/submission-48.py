class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """

        return index of T

        T = 1

                L m R
        3 4 5 6 1 2 3
        
        upper half
        - T < mid
            T >= nums[L] --> go left
            T < nums[L] --> go right
        - T > mid
            go right

        lower half
        - T < mid
            go left
        - T > mid
            T <= nums[R] --> go right
            T > nums[R] --> go left

        """

        L, R = 0, len(nums)-1

        while L <= R:
            mid = (L+R) // 2

            # index found
            if nums[mid] == target:
                return mid

            # upper half
            elif nums[mid] > nums[R]:
                if target > nums[mid]:
                    L = mid+1
                else:
                    if target >= nums[L]:
                        R = mid-1
                    else:
                        L = mid+1

            # lower half
            else:
                if target > nums[mid]:
                    if target <= nums[R]:
                        L = mid+1
                    else:
                        R = mid-1
                else:
                    R = mid-1

        return -1


