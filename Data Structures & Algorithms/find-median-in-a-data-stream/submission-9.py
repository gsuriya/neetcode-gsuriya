import heapq

class MedianFinder:
    """

    maintain two boundary values w/ max & min heap
    - maxheap (lower vals)
    - minheap (higher vals)

    invariants: 
    - len(maxheap) == len(minheap) + 1 (balancing)
    - add to maxheap if empty, always compare added num to MAXHEAP

    getMedian:
    - even # elems: equal length heaps --> return avg(min[0], max[0])
    - odd # elems: maxheap > minheap --> return max[0]

    """
    def __init__(self):
        self.maxh = [] # lower vals
        self.minh = [] # higher vals
        
        heapq.heapify(self.maxh)
        heapq.heapify(self.minh)

    # O(logN) compared to O(N) if you kept a sorted arr w/ insertion sort
    def addNum(self, num: int) -> None:
        if not self.maxh:
            heapq.heappush(self.maxh, -num)
        else:
            # compare num to boundaries
            if num <= -self.maxh[0]:
                heapq.heappush(self.maxh, -num)
            else:
                heapq.heappush(self.minh, num)
        
        # balancing 
        # maxheap too big
        if len(self.maxh) > len(self.minh) + 1:
            heapq.heappush(self.minh, -heapq.heappop(self.maxh))
        # maxheap too small
        if len(self.maxh) < len(self.minh):
            heapq.heappush(self.maxh, -heapq.heappop(self.minh))

    # O(1) - see if even or odd and return
    def findMedian(self) -> float:
        # odd
        if len(self.maxh) > len(self.minh):
            return -self.maxh[0]
        # even
        return (self.minh[0] + -self.maxh[0]) / 2





        