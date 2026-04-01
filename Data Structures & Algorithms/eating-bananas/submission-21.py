class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # The possible k range: [1, max(piles)]
        l, r = 1, max(piles)
        
        while l <= r:
            mid = (l + r) // 2
            # If we can finish in h hours or less with speed mid
            if self.canFinish(piles, h, mid):
                # mid is a valid or possibly too high speed; try lower
                r = mid - 1
            else:
                # mid is too slow, we can't finish in h hours
                l = mid + 1
        
        return l

    def canFinish(self, piles: List[int], h: int, k: int) -> bool:
        # Calculate total hours needed with eating speed k
        hours_needed = 0
        for p in piles:
            hours_needed += (p + k - 1) // k  # or math.ceil(p / k)
        
        # True if total hours needed is <= h
        return hours_needed <= h