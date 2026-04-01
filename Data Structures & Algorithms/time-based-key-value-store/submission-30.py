class TimeMap:
        
    """

    for each key, multiple timestamps
                                       
    map = {                            
                             R
        key --> [(3, v1), (7, v2), (11, v3)]

    }

    set(key, time, value)
    - map[key].append(time, value)

    get(key, 9)

    L   R                                
    T T F  
    0   11

    - find max time <= 9            

    """
    def __init__(self):
        self.map = defaultdict(list) # key --> [(t1, val), (t2, val)]
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        # timestamps inserted in sorted order per problem description
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # if key not in data structure, return ""
        if key not in self.map:
            return ""

        # binary search key list
        L, R = 0, len(self.map[key])-1

        while L <= R:
            mid = (L+R) // 2

            # if it works, go right to find larger val that COULD work
            if self.map[key][mid][0] <= timestamp:
                L = mid+1

            # if it doesn't work, go left to find smaller val that works
            else:
                R = mid-1
        
        if R == -1:
            return ""
        
        return self.map[key][R][1]







