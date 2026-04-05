class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """

        min bin search to find smallest k that works
        
        k range: [1, max(piles)]
        - sorted so binary search it

        """

        L = 1
        R = max(piles)

        while L <= R:
            k = (L+R) // 2

            if self.k_works(k, h, piles):
                # go smaller
                R = k-1
            else:
                # go bigger
                L = k+1
        
        return L
        
    def k_works(self, k, h, piles):
        # find num of hrs to eat everything
        total = 0
        for p in piles:
            total += math.ceil(p/k)
        
        return total <= h




            