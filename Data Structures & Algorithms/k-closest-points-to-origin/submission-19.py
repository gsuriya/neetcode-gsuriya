import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """

        k-sized max heap
        - keep popping the larger distances until closest points r there

        calc distance for every point

        1. add points to k-sized maxheap (dist, x, y)
        2. return points left in k-sized maxheap

        """

        # push into k-size heap
        h = []
        heapq.heapify(h)

        for x, y in points:
            # push (dist, x, y)
            dist = math.sqrt((x**2) + (y**2))
            heapq.heappush(h, (-dist, x, y))

            while len(h) > k:
                heapq.heappop(h)
        
        # return points left in heap
        res = []
        for dist, x, y in h:
            res.append([x, y])
        return res
            







