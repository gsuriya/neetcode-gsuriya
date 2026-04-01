class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """

        find k=2 closest integers to x=6 in the arr

        min_total_difference = 3
        - even if the next window has the same min_total_diff, DO NOT UPDATE
          L and R pointers cus its just the next window now not the same thing

k=3
x = 1


arr     2 3 4

diff    1 2 3


        sorted --> closest ints to x are NEXT TO EACH OTHER

        k size sliding window, keep track of final window L and R pointers

        1. calculate curr_total_diff for each window
        - if curr_total_diff < min_total_diff --> dynamically update min and f L&R
        - NOT <= b/c ur updating L&R to later window w/ same total diff

        """

        min_total_diff = float('inf')
        Lf, Rf = 0, 0

        window_total_diff = 0
        L = 0

        for R in range(len(arr)):
            # expand window
            window_total_diff += abs(arr[R] - x)

            # shrink window if window size > k
            while R-L+1 > k:
                window_total_diff -= abs(arr[L] - x)
                L += 1

            # calculate total diff
            if R-L+1 == k:
                if window_total_diff < min_total_diff:
                    min_total_diff = window_total_diff
                    Lf, Rf = L, R
        
        return arr[Lf : Rf+1]
                
            





