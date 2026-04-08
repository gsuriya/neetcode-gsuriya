class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """

        make stones a max heap
        - pick 2
        - x == y --> destroy
        - x < y --> heappush(y-x) back


        u hv to logically figure out that x is the second pop
        b/c the 1st pop never < 2nd pop
        """

        h = [-s for s in stones]
        heapq.heapify(h)
        
        while len(h) > 1:
            # pick 2, simulate
            y = -heapq.heappop(h)
            x = -heapq.heappop(h)

            if x < y:
                heapq.heappush(h, -(y-x))
        
        return -h[0] if h else 0




