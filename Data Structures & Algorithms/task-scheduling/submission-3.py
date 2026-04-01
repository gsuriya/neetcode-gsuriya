class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """

        1. add frequencies to max heap
        2. start popping frequencies w/ delayed re-entry
        - put delayed freqs in queue
        - add back to heap to be processed again

        """

        # step 1 - add freqs to heap
        freq_map = defaultdict(int)
        for c in tasks:
            freq_map[c] += 1
        h = []
        heapq.heapify(h)
        for f in freq_map.values():
            heapq.heappush(h, -f)
        

        # step 2
        time = 0 # a tick = heappop or idle time
        q = deque()

        while h or q:
            # pop from heap and add to queue
            if not h: # idle time
                time += 1
            else:           # (letterfreq, expiration time)
                time += 1

                # if letterfreq is 0, then don't append
                letterfreq = heapq.heappop(h)+1
                if letterfreq:
                    q.append((letterfreq, time+n))
            
            # add from q back to heap
            while q and q[0][1] == time:
                heapq.heappush(h, q.popleft()[0])
        
        return time
            
            









