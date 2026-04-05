class TimeMap:

    def __init__(self):
        # key --> [(t1, val), (t2, val), (t3, val)]
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """

        return the largest timestamp; <= timestamp

        if t <= timestamp --> True else False

        T T T T F F F 

        """
        # edge case - no valeus for inputted timestamp r there
        if key not in self.time_map or timestamp < self.time_map[key][0][0]:
            return ""

        # max binary search 
        L, R = 0, len(self.time_map[key])-1

        while L <= R:
            mid = (L+R) // 2

            # if works, go bigger
            if self.time_map[key][mid][0] <= timestamp:
                L = mid+1
            # if doesn't go smaller
            else:
                R = mid-1
        
        return self.time_map[key][R][1]

