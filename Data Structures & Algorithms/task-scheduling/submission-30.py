import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """

        1. put freqs into maxheap
        2. maxheap time-based queue
        - pop highest freq, q it w/ expiration time
        - time += 1 when popping
        - if nothing in heap but in q, idle time
        
        n = 2

        maxheap = []
        time = 3
        q = [(-1, 4)]
        """

        # put freqs into maxheap
        freq_map = defaultdict(int)
        for t in tasks:
            freq_map[t] += 1
        h = [-f for f in freq_map.values()]
        heapq.heapify(h)

        # maxheap time-based queue
        q = deque()
        time = 0
        while h or q:
            if not h and q: # idle time
                time += 1
            
            # pop from maxheap
            if h:
                val = heapq.heappop(h)+1
                if abs(val) > 0:
                    q.append((val, time+n+1))
                time += 1 # popping increments time
            
            # pull from q
            if q and q[0][1] == time:
                heapq.heappush(h, q.popleft()[0])
        
        return time





        