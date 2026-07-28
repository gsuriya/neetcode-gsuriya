class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """

        k closest points to origin

        find dist btwn all points to origin
        - put (dist, x, y) into k-sized maxheap

        """

        maxh = []
        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            maxh.append((-dist, x, y))
        heapq.heapify(maxh)

        # keep it k-sized
        while len(maxh) > k:
            heapq.heappop(maxh)

        # extract remaining points and put in res
        res = []
        for dist, x, y in maxh:
            res.append([x, y])
        return res

