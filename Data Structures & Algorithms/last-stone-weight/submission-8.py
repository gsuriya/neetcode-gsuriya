class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-s for s in stones]
        heapq.heapify(h)

        while len(h) > 1:
            y = -heapq.heappop(h)
            x = -heapq.heappop(h) # x is second popped cus now x can be lighter than y

            if x == y:
                pass
            elif x < y:
                heapq.heappush(h, -(y-x))

        if not h:
            return 0
        return -h[0]