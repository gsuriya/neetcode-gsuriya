import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """

        1 4 3 2
        
        L     R
        1 2 3 4

        search for min k in range: [1, max(piles)]

        """

        # min binary search
        L, R = 1, max(piles)

        while L <= R:
            k = (L+R) // 2

            # if it works, go left to find smaller
            if self.test_k(k, piles, h):
                R = k-1
            # if it doesn't, then go right to find larger that works
            else:
                L = k+1
        
        return L


    def test_k(self, k, piles, h):
        # test how many hours it takes to eat piles w/ given k
        hours_needed = 0
        for p in piles:
            hours_needed += math.ceil(p/k)
        # if more hours needed than allotted --> return False else True
        return hours_needed <= h 

      


