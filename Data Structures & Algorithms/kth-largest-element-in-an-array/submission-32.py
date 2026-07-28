class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """

        k-sized minheap approach

        """

        h = nums[:]
        heapq.heapify(h)

        while len(h) > k:
            heapq.heappop(h)
        return h[0]