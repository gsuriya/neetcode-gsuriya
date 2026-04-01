import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """

        k range: 1 - max(piles)

        if k works, go smaller

        if k doesn't, go bigger


        return L at the end

        """

        L, R = 1, max(piles)
        
        while L <= R:
            mid = (L+R) // 2

            # if mid works, go find smaller k
            if self.test_k(mid, piles, h):
                R = mid-1
            # if it doesn't, go bigger
            else:
                L = mid+1
        
        return L

    
    def test_k(self, k, piles, h):
        hours_needed = 0
        for n in piles:
            hours_needed += math.ceil(n/k)
        if hours_needed <= h:
            return True
        else:
            return False


        