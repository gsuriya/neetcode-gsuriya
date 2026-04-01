import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        time = 1

        h = [-1, -1]
        q = [(-2, 2)]

        """
        
        q = deque()
        
        freq_map = defaultdict(int)
        for c in tasks:
            freq_map[c] += 1
        h = [-f for f in freq_map.values()]
        heapq.heapify(h)
        time = 0

        while h or q:
            # if nothing in heap but in q --> idle time
            if not h:
                time += 1
            else:
                freq = heapq.heappop(h)+1
                time += 1
                if freq:
                    q.append((freq, time+n))

            # pull from q into heap
            if q and q[0][1] == time:
                heapq.heappush(h, q.popleft()[0])
        
        return time





         