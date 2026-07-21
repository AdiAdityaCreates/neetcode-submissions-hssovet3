"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if not intervals:
            return 0

        intervals.sort(key=lambda x:x.start)

        pq = []
        for interval in intervals:
            s = interval.start
            e = interval.end

            if pq and pq[0] <= s:
                heapq.heappop(pq)
            heapq.heappush(pq,e)
        return len(pq)