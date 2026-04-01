"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """

        edge case: no intervals --> return True

        sort
        if overlap: --> return False
        else: --> extend prev_end

        """

        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)

        prev_end = intervals[0].end
        for i in range(1, len(intervals)):
            # overlap
            if intervals[i].start < prev_end:
                return False
            
            # no overlap
            else:
                prev_end = intervals[i].end

        return True


