class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """

        do tasks w/ highest freq first

        1. create freq map, put freqs into maxheap
        2. while maxheap or q
        - pull from q (if u can)
        - pop from maxheap, increment time
        - q the val-1 into the heap w/ expiration time

        3. return time at the end

        """

        # create freq_map, put freqs into maxheap
        freq_map = defaultdict(int)
        for c in tasks:
            freq_map[c] += 1
        
        maxh = [-f for f in freq_map.values()]
        heapq.heapify(maxh)
        q = deque() # time-based queue

        # simulate w/ time
        """

        maxh = []
        q = [(-2, 4)]
        time = 4

        """
        time = 0
        while maxh or q:
            # pull from q into maxheap
            if q and q[0][1] == time:
                heapq.heappush(maxh, q.popleft()[0])

            # pop from maxheap, if can't idle time
            if not maxh:
                time += 1
            
            else:
                val = heapq.heappop(maxh) 
                val += 1 
                time += 1 # increment time when popping

                if abs(val) > 0:
                    q.append((val, time + n)) # (val-1, expiration time)
        
        return time


