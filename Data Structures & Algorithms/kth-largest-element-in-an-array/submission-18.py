class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """

        find sorted index target=len(nums)-k

        1. get sorted pivot
        - recurse left or right depending on where target is

        """
        target = len(nums)-k

        def quick_select(L, R):
            # partition
            pivot = nums[R]
            p = L
            for i in range(L, R):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[R] = nums[R], nums[p]

            # recurse left or right
            if p < target:
                return quick_select(p+1, R)
            elif p > target:
                return quick_select(L, p-1)
            else:
                return nums[p]
        
        return quick_select(0, len(nums)-1)


        