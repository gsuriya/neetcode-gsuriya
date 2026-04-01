import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """

        sort intervals and queries

        1. add all possible intervals (start <= q)
        2. remove invalid intervals from top of heap (right < q)
        - (size, right)
        3. peek and add to res

          ---
        0 1 2 3 4 5 6 7 8 
queries       .

        """

        intervals.sort()

        res = {} # query --> res
        h = []
        heapq.heapify(h)

        i = 0
        for q in sorted(queries):
            # add possible intervals - start <= q
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(h, (intervals[i][1]-intervals[i][0]+1, intervals[i][1]))
                i += 1
            
            # heappop invalid intervals from top of heap (right < q)
            while h and h[0][1] < q:
                heapq.heappop(h)

            # peek and add to res
            res[q] = h[0][0] if h else -1

        return [res[q] for q in queries]






