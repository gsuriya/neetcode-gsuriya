import heapq

class KthLargest:
    """

    size k min heap
    1. add all elems to min heap
    2. return h[0]

    """

    def __init__(self, k: int, nums: List[int]):
        # initialize k size min heap, add all of nums to it
        self.h = []
        self.k = k
        heapq.heapify(self.h)

        for n in nums:
            heapq.heappush(self.h, n)
            
            while len(self.h) > k:
                heapq.heappop(self.h)


    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        while len(self.h) > self.k:
            heapq.heappop(self.h)
        
        return self.h[0]

        
