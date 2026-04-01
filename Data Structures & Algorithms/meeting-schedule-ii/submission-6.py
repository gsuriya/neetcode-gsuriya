"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """

        use two pointers NOT sweep line
        put start and end times into sorted lists

        go over merged (start & end) and increment/decrement count
        - return max_count

                         i
        starts = [0, 5, 10]
                 j
        ends =  [10, 20, 40]


        edge: u don't need an extra room for start and end same time
        - so decrement first and THEN increment

        """

        starts = []
        ends = []

        for i in range(len(intervals)):
            starts.append(intervals[i].start)
            ends.append(intervals[i].end)
        
        starts.sort()
        ends.sort()

        max_count = 0
        count = 0

        # go over merged chronological times
        i, j = 0, 0
        while i < len(starts) and j < len(ends):
            if starts[i] < ends[j]: # no <= to handle edge case
                count += 1
                max_count = max(max_count, count)
                i += 1
            else: 
                count -= 1
                j += 1
        while i < len(starts):
            count += 1
            max_count = max(max_count, count)
            i += 1
        while j < len(ends):
            count -= 1
            j += 1

        return max_count










