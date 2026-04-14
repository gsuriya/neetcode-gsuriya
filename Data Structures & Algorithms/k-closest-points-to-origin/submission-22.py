class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """

        k-sized maxheap

        1. add (-dist, x, y) to heap
        2. take k left in heap, return as res arr

        """
        
        # push points into k-sized maxheap
        h = []
        heapq.heapify(h)
        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(h, (-dist, x, y))
            
            while len(h) > k:
                heapq.heappop(h)
        
        res = []
        for dist, x, y in h:
            res.append([x, y])
        return res

        
