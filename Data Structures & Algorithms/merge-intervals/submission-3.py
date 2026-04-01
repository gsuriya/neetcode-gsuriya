class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """

        append first int to res

        if i overlapping w/ res[-1] --> extend upper bound for res[-1] interval
        
        else not overlapping --> append interval i and extend max pointer to upper bound


        """
        intervals.sort(key=lambda x: x[0])
        
        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            # overlapping
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], intervals[i][1])

            # ~overlapping
            else:
                res.append(intervals[i])
            
        return res