class TimeMap:
    """

    each key --> multiple vals

    {
                     L              R
        "alice": [(1, "happy"), (3, "sad")]
                    T                F
    }

    """
    def __init__(self):
        self.time_map = defaultdict(list) # key --> [(timestamp, val)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # edge cases: key not in map or timestamp lower than all timestamps in that list
        if key not in self.time_map or timestamp < self.time_map[key][0][0]:
            return ""
        
        # returns most recent val --> max binary search
        L, R = 0, len(self.time_map[key])-1

        while L <= R:
            mid = (L+R) // 2

            # works, move right to find more
            if self.time_map[key][mid][0] <= timestamp:
                L = mid+1
            # doesn't work, move left to find one that works
            else:
                R = mid-1
                
        return self.time_map[key][R][1]


        
