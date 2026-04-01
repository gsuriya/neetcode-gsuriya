class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """

        T = 4

        L     m     R
        4 5 6 7 1 2 3

        upper half (m > R)
        - T > m --> move right
        - T < m
            - T < L --> move right
            - T >= R --> move left

        lower half (m < R)
        - T < m --> move left
        - T > m
            - T > R --> move left
            - T <= R --> move right

        """

        L, R = 0, len(nums)-1

        while L <= R: # do we skip mid all the time?
            mid = (L+R) // 2

            if nums[mid] == target:
                return mid

            # upper half
            elif nums[mid] >= nums[R]:
                if target > nums[mid]:
                    L = mid+1
                else:
                    if target < nums[L]:
                        L = mid+1
                    else:
                        R = mid-1

            # lower half
            elif nums[mid] < nums[R]:
                if target < nums[mid]:
                    R = mid-1
                else:
                    if target > nums[R]:
                        R = mid-1
                    else:
                        L = mid+1

        
        return -1











