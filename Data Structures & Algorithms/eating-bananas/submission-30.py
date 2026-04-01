class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # trying log(m) k's
        # for each k we test out, O(n) time to check
        # thererfore, O(nlog(m))

        # range of possible k's
        l, r = 1, max(piles)

        # min binary search
        while l <= r:
            mid = (l+r) // 2
            res = self.test_k(piles, mid, h)

            # for k's that work, keep going left to find smaller k
            if res == 1:
                r = mid-1
            # for k's that don't work, go right to find bigger k that works
            elif res == -1:
                l = mid+1

        return l
    
    def test_k(self, piles, k, h):
        hours_needed = 0
        for p in piles:
            hours_needed += math.ceil(p/k)
        
        # k is too small
        if hours_needed > h:
            return -1
        # k works
        else:
            return 1
        

