import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """

        max heap of size k
        
        1. funnel (distance, point) into the heap of size k
        2. extract final points from heap and put into res array

        """

        # step 1
        h = []
        heapq.heapify(h)
        for x, y in points:
            heapq.heappush(h, (-math.sqrt(x**2 + y**2), (x, y)))

            while len(h) > k:
                heapq.heappop(h)
        
        # step 2
        res = []
        for distance, (x, y) in h:
            res.append([x, y])
        return res
            




            