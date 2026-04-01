class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        h = hrs to eat all bananas

        k = bananas per hour

        1. search for min k that works (1 - max(piles))
        2. check if k works (return if k is too little or too small)

        piles = 1 4 3 2 

        k = 2
        h = 

        therefore, doesn't matter which side of list I start at
        each value in list holds number of hours needed
        --> calculate the total hours needed for this specific k
        if hours_needed > hours_given:
            res = -1
        elif hours needed <= hours_given:
            res = 0

        """

        # search for min k in sorted list, binary search min val

        l = 1
        r = max(piles)

        while l <= r:
            mid = (l+r) // 2

            hours_needed, res = 0, 0
            for p in piles:
                hours_needed += math.ceil(p/mid)
            res = -1 if hours_needed > h else 0

            if res == -1:
            # if k too small --> need to find a bigger eating rate
                l = mid+1
            elif res == 0:
            # if k works --> try to find a smaller k that works
                r = mid-1
        return l # return the min k that works
        