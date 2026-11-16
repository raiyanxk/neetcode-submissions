"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        points = []

        for interval in intervals:
            points.append((interval.start, 1))
            points.append((interval.end, -1))
        
        points.sort()

        res = 0
        curr = 0

        for t, ty in points:
            if ty == 1:
                curr += 1
            else:
                curr -= 1
            res = max(res, curr)

        return res
