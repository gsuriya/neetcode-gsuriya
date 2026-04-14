class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """

        insert freqs into maxheap
        
        while heap or q:
            pull from q

            if not heap:
                idle time so increment time
            else:
                pop max --> increment time

                add freq to time-based queue
                - (freq-1, expiration_time)

        n = 2
        time = 0
        maxh = [-2, -2]
        q = 

        """
        freq_map = defaultdict(int)
        for t in tasks:
            freq_map[t] += 1

        h = [-f for f in freq_map.values()]
        heapq.heapify(h)

        q = deque() # (val, expiration)
        time = 0
        
        while h or q:
            # pull from q
            while q and q[0][1] == time:
                heapq.heappush(h, q.popleft()[0])
            
            # idle time
            if not h:
                time += 1
            # pop from heap
            else:
                freq = heapq.heappop(h)
                time += 1
                if freq + 1 < 0:
                    q.append((freq+1, time+n))
        
        return time





