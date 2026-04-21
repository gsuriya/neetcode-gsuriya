class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """

        strictly right
        - append i

        strictly left
        - append newInterval
        - append rest, return

        else merge
        - merge, DONT append 

        append at end in case only merging / strictly right

        [2, 5]

           i
        [[1,3],[4,6]]

        res = []

        """
        res = []

        for i in range(len(intervals)):
            # strictly left
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                res += intervals[i:]
                return res
            
            # strictly right
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            # else merge
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        
        res.append(newInterval) # in case only merges / stricly right
        return res









