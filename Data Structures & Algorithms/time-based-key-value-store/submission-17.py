"""
multiple values for same key at time stamps
retrieve keys value at timestamp (t)

map = {
        k1: [(t1,v1), (t2,v2), (t3,v3)]
        k2: [(t1,v1), (t2,v2), (t3,v3)]
        k3: [(t1,v1), (t2,v2), (t3,v3)]
      }

"""


class TimeMap:
    
    def __init__(self):
        # create hashmap
        self.time_map = defaultdict(dict)
    def set(self, key: str, value: str, timestamp: int) -> None:
        # set values for key in map
        self.time_map[key][timestamp] = value
    def get(self, key: str, timestamp: int) -> str:
        sorted_times = list(self.time_map[key].keys())
        # sorted_times = [1 3 5 7 9 10]
        # timestamp = 6

        # max val that works binary search
        l, r = 0, len(sorted_times)-1

        return_time = -1
        while l <= r:
            mid = (l+r) // 2

            res = 1 if sorted_times[mid] <= timestamp else -1

            # if works go right
            if res == 1:
                return_time = max(return_time, sorted_times[mid])
                l = mid+1
            # if doesn't work go left
            elif res == -1:
                r = mid-1

        if return_time == -1:
            return ""
      
        
        return self.time_map[key][sorted_times[r]]
        

