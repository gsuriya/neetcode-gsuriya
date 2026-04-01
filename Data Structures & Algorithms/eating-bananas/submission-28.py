class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = float('inf')
        # the GPT solution is diff from the neetcode solution

        while l <= r:
            mid = (l+r) // 2

            if self.is_valid_k(mid, h, piles):
                r = mid-1
                # if val works, store it as a res
                res = min(res, mid)
            else:
                l = mid+1
        return res


    def is_valid_k(self, k, h, piles):
        hours_needed = 0
        for p in piles:
            hours_needed += math.ceil(p/k)
        
        if hours_needed <= h:
            return True # k is big enough, can go smaller
        else:
            return False # k is too small, go bigger
    
    