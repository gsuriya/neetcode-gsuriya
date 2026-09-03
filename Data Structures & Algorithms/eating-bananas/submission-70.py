class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        min binary search - test k's from range [1, max(piles)]
        if hours_needed <= h
          work --> go left to find smaller k
        else hours_needed > h:
          ~work --> go right to find larger k

        return L

        """

        L, R = 1, max(piles)

        while L <= R:
            mid = (L+R) // 2

            if self.k_works(mid, piles, h):
                R = mid-1
            else:
                L = mid+1
        
        return L
    
    def k_works(self, k, piles, h):
        hours_needed = 0
        for p in piles:
            hours_needed += math.ceil(p/k)

        if hours_needed <= h:
            return True
        return False



