class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """

        y is the 1st one popped cus thats the only way x would be less than y

        y = pop
        x = pop

        if x == y --> don't add back
        if x < y --> add (y-x) back

        maxh
        """

        maxh = [-s for s in stones]
        heapq.heapify(maxh)

        while len(maxh) > 1:
            y = -heapq.heappop(maxh)
            x = -heapq.heappop(maxh)

            if x < y:
                heapq.heappush(maxh, -(y-x))
        
        return -maxh[0] if maxh else 0


