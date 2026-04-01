class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """

        sort

        if overlap (start < prev_end)
        - "delete" one w/ lower end (put prev_end at min of two ends)
    
        else
        - extend prev end

        """
        res = 0
        intervals.sort()

        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end: # overlapping
                prev_end = min(prev_end, intervals[i][1]) # delete one that extends farther
                res += 1
            
            else:
                prev_end = intervals[i][1]
        
        return res