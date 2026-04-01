class TimeMap:

    def __init__(self):
        self.map = {} # key --> [[t1,v1], [t2, v2]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        # no keys OR no values --> return ""
        if key not in self.map or timestamp < self.map[key][0][0]:
            return ""

        # max binary search
        L, R = 0, len(self.map[key])-1

        while L <= R:
            mid = (L+R) // 2

            # if works --> go right in hopes of finding larger
            if self.map[key][mid][0] <= timestamp:
                L = mid+1
            # doesn't work --> go left to find one that works
            else:
                R = mid-1
        
        # R will be on max
        return self.map[key][R][1]

        
