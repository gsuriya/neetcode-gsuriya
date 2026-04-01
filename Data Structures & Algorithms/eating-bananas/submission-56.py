class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """

        min binary search --> L will be at min

        k range: [1, len(piles)]

        hours_needed += math.ceil(piles[i]/k)
        if hours_needed < hours we have:
            k is invalid --> higher k needed

        m
        R 
          L     
        1 2 3 4

        """

        L, R = 1, max(piles)

        while L <= R:
            k = (L+R) // 2

            # test k
            hours_needed = 0
            for p in piles:
                hours_needed += math.ceil(p/k)
            works = hours_needed <= h

            # if it works, move left in hopes of finding smaller
            if works:
                R = k-1
            # if it doesn't, move right to find k that works
            else:
                L = k+1
        
        return L

        
        


    
    