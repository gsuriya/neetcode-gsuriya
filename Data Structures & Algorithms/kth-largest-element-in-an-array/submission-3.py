class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """

        quick sort: allows us to sort for a sorted index

        the TARGET INDEX is alr sorted

        so once i find SORTED PIVOT, can compare

        if p < T --> search right of sorted
        elif p < T --> serach left of sorted
        else: sorted p is at sorted target


        """
        target = len(nums)-k

        def quick_select(L, R):
            # partition
            pivot = nums[R]
            p = L
            for i in range(L, R):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[R] = nums[R], nums[p]

            # recurse left OR recurse right
            if p < target:
                return quick_select(p+1, R)
            elif p > target:
                return quick_select(L, p-1)
            else:
                return nums[p]
        
        return quick_select(0, len(nums)-1)





