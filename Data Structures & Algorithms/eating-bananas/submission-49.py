import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """

        hours = 9

        1 4 3 2

        k = 2

        k range: [1, max(piles)]
        - binary search this range and check that k works

        time: O(nlogn)

        """

        L, R = 1, max(piles)

        while L <= R:
            mid = (L+R) // 2

            # if this k is good, move left to find smaller k that work
            if self.check_k(mid, piles, h):
                R = mid-1
            # if not good, then move right go find larger k that work
            else:
                L = mid+1
        
        return L

    
    def check_k(self, k, piles, h):
        hours_needed = 0
        for n in piles:
            hours_needed += math.ceil(n/k)
        if hours_needed <= h:
            return True
        else:
            return False



