class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)

        # MIN binary search algorithm
        # keep moving k, if found possible value, save it
        min_k = 1
        while l <= r:
            mid = (l+r)//2

            if self.test_k(mid, piles, h):
                min_k = mid
                r = mid-1
            else:
                l = mid+1
               

        return min_k

    def test_k(self, k, piles, h):
        # if k too big (it works) return True
        # if k too small (bigger k needed) return False

        # calculate the number of hours
        hours = 0
        for n in piles:
            hours += math.ceil(n/k)
        
        if hours <= h:
            return True
        else:
            return False
        




