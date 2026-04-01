import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """

        min_heap (k size), get k largest elems inside, peek

        """

        h = []
        heapq.heapify(h)
        for n in nums:
            heapq.heappush(h, n)

            while len(h) > k:
                heapq.heappop(h)

        return h[0]
        