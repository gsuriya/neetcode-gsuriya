import heapq

class KthLargest:
    """

    k-sized heap insert all elements

    """

    def __init__(self, k: int, nums: List[int]):
        self.h = []
        heapq.heapify(self.h)
        for n in nums:
            heapq.heappush(self.h, n)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)

        while len(self.h) > self.k:
            heapq.heappop(self.h)

        return self.h[0]
        
