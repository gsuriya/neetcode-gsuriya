class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """

        maxheap
        x is 2nd pop b/c x < y


        """

        h = [-s for s in stones]
        heapq.heapify(h)

        while len(h) > 1:
            y = -heapq.heappop(h)
            x = -heapq.heappop(h)

            if x < y:
                heapq.heappush(h, -(y-x))

        if not h:
            return 0
        return -h[0]