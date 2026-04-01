class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        insert interval algo

        left
        - append interval
        - append rest

        right
        - append i

        else:
            merge interval (DONT ADD cus can merge w/ later ones too)

        edge case: if u only merge or only right, then add interval at the end
        
        """

        res = []

        for i in range(len(intervals)):
            # left
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # right
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # else (merge)
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
        res.append(newInterval)
        return res



