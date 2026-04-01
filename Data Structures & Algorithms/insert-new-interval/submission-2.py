class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """

        if interval to the left
        - append interval, append the rest
        - return

        elif interval to the right
        - append i

        else: (overlaps)
        - merge

        add interval at the end for edge cases: only rights or only merges
 
        """
        res = []

        for i in range(len(intervals)):
            # newInterval to the left
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            # newInterval to the right
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            # merge, DONT append here cus might need to merge w/ later intervals
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
        res.append(newInterval)

        return res



