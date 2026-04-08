import heapq

class KthLargest:
    """
    alw keep heap as small as possible
    - so make blank heap and THEN insert nums O(nlogk)
    - do NOT heapify O(n + (n-k)logn)) --> O(nlogn)

    k-size heap

    """

    def __init__(self, k: int, nums: List[int]):
        # insert every num into k-sized heap
        # O(nlogk)
        self.k = k
        self.h = []
        heapq.heapify(self.h)
        
        for n in nums:
            heapq.heappush(self.h, n)

            while len(self.h) > self.k:
                heapq.heappop(self.h)
        
    def add(self, val: int) -> int:
        # insert into heap, peek heap
        heapq.heappush(self.h, val)
        while len(self.h) > self.k:
            heapq.heappop(self.h)
        
        return self.h[0]







        
