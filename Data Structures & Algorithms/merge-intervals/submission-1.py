class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """

        sort
        append first interval to res
        
        iterate thru rest:
        - if int can be merged w/ res[-1] int, then extend max in res[-1]
        - elif not, then append

        """

        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            # merge
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], intervals[i][1])

            # ~merge, append
            else:
                res.append(intervals[i])
        
        return res



        