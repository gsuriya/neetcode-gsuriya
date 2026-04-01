import heapq

class KthLargest:
    """

    stream values into a minheap of size k


    """
    def __init__(self, k: int, nums: List[int]):
        self.h = nums
        heapq.heapify(self.h)
        self.k = k

        # maintain k elements in the heap
        while len(self.h) > k:
            heapq.heappop(self.h)

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)

        while len(self.h) > self.k:
            heapq.heappop(self.h)

        return self.h[0]
        
