import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """

        distances = []
        - populate w/ distf from (0,0) for each point

        for dist in distances:
            - add to heap of size k, pop if len(heap) > k
            - max_heap of k smallest values

        return k smallest values left in max_heap

        """
        dist_and_point = [(-math.sqrt(x**2 + y**2), (x, y)) for x, y in points]

        # max_heap with k smallest distances
        max_heap = []
        heapq.heapify(max_heap)

        for d, p in dist_and_point:
            heapq.heappush(max_heap, (d, p))

            while len(max_heap) > k:
                heapq.heappop(max_heap)
        
        # now max_heap has k smallest distances
        res = []
        for d, p in max_heap:
            res.append(p)
        return res


