class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        
        always use max freq letters first cus can use idle time to use OTHER letters

        1. freq_map
        2. put freqs in maxheap, time-based queue (expiration_time, val)
        3. while maxheap or q:
        - pull values from queue
        - pop largest if smth in heap
            - nothing in heap, idle time so increment global time
            - append (f-1, expiration time) to time-based queue
            - increment global time
        
        return global time (num of cpu cycles)


        """

        # freq_map
        freq_map = defaultdict(int)
        for c in tasks:
            freq_map[c] += 1

        # maxheap and time-based queue
        maxh = [-f for f in freq_map.values()]
        heapq.heapify(maxh)
        q = deque() # (expiration_time, val)
        
        """
        time = 4
        
        q = [(3, -2)]
        maxh = [-2]


        """

        time = 0
        while maxh or q:
            # pull from q and push into heap
            if q and q[0][0] == time:
                t, val = q.popleft()
                heapq.heappush(maxh, val)

            # idle time
            if not maxh:
                time += 1
            else:
                val = heapq.heappop(maxh)+1
                time += 1
                
                if val != 0: # only process again if not 0
                    q.append((time+n, val))
        
        return time



        
