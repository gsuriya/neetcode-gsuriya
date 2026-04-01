"""
multiple values for same key at time stamps
retrieve keys value at timestamp (t)

map = {
                l         m        r
        k1: [(t1,v1), (t2,v2), (t3,v3)]
        k2: [(t1,v1), (t2,v2), (t3,v3)]
        k3: [(t1,v1), (t2,v2), (t3,v3)]
      }

"""


class TimeMap:
    
    def __init__(self):
        # create hashmap
        self.time_map = defaultdict(list)
       
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # get most recent val for timestamp
        # max val that works binary search

        l, r = 0, len(self.time_map[key])-1
        recent_timestamp = [0, 0] # [timestamp, index]

        while l <= r: # eventually crosses if checks too far, so l <= r is good
            mid = (l+r) // 2

            # if it works, keep going right to find bigger val
            if timestamp >= self.time_map[key][mid][0]:
                recent_timestamp[0] = max(recent_timestamp[0], self.time_map[key][mid][0])
                recent_timestamp[1] = mid
                l = mid+1
            # if it doesn't work, go left to find smaller val
            else:
                r = mid-1

        if recent_timestamp[0] == 0:
            return ""

        return self.time_map[key][recent_timestamp[1]][1]

