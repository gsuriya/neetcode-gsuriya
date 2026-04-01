class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """

        0. heapify

        while len(heap) > 1
            1. pop two largest stones
            - delete smaller, insert updated bigger

        return last stone

        """

        max_heap = [-1*s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            first = -1*heapq.heappop(max_heap) 
            second = -1*heapq.heappop(max_heap) # lighter than first cus popped after

            if second < first:
                heapq.heappush(max_heap, -1*(first-second))
        
        if max_heap:
            return -1*max_heap[0]
        return 0

