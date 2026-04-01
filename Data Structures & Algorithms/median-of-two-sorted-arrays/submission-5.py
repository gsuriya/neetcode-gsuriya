class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """

        binary search the cut position on the smaller array

        1. find i --> find j
        2. have variables for endpoints
        3. compare endpoints
        - if valid partition --> return median
        - if not --> move L and R pointers
            
               i
        A: [1, 3, 8]
        B: [7, 9, 10, 11]
            j

        1 3 7 8 9 10
        """
        total = len(nums1) + len(nums2)
        half = total // 2

        A, B = nums1, nums2 # A should be the smaller array
        if len(nums1) > len(nums2):
            A, B = B, A # swap so A is smaller

        # start binary search on smaller array
        L, R = 0, len(A)-1
        while True:
            i = (L+R) // 2
            j = half - (i+1) - 1

            # set endpoints
            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i+1] if i < len(A)-1 else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j+1] if j < len(B)-1 else float('inf')

            # compare endpoints
            if Aleft <= Bright and Bleft <= Aright:
                # return median
                if total % 2 == 0: # even
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else: # odd
                    return min(Aright, Bright)
            
            elif not Aleft <= Bright and Bleft <= Aright: # too many from A
                R = i-1
            elif Aleft <= Bright and not Bleft <= Aright: # too few from A
                L = i+1

    