class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """

        append first interval to res

        iterate thru rest of intervals:
        - if first number <= last number interval in res
            extend interval in res
        - else
            append intervals[i] to res

        """
        intervals.sort()

        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]: # extend last interv in res
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
        
        return res





