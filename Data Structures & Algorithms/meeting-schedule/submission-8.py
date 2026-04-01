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

        sort intervals by 1st val


        if curr_start <= prev_end --> overlap so return false

        once at the end, return True

        """
        if not intervals:
            return True


        intervals.sort(key=lambda x: x.start)
        
        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            if intervals[i].start < res[-1].end: # overlap
                return False
            else: # ~overlap
                res.append(intervals[i]) # append so res[-1][1] updates
        
        return True











