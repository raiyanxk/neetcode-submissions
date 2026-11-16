"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        endpoints = []

        for interval in intervals:
            endpoints.append((interval.start, 1))
            endpoints.append((interval.end, -1))
        
        endpoints.sort()
        res = 0
        curr = 0

        for time, t in endpoints:
            if t == 1:
                curr += 1
                res = max(res, curr)
            else:
                curr -= 1

        
        return res 
        