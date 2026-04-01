class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """

        prev_end = intervals[0][1]

        iterate thru rest of ints:
        - if start < prev_end: # overlapping --> delete one that extends longer

        - else: # ~overlapping --> extend prev_end

        """
        intervals.sort()
        res = 0

        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end: # overlapping
                res += 1
                prev_end = min(prev_end, intervals[i][1])
            
            else: # ~overlapping --> extend prev_end
                prev_end = intervals[i][1]

        
        return res



        