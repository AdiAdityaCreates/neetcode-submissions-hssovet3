import heapq

class Solution:
    def minMeetingRooms(self, intervals):

        if not intervals:
            return 0

        pq = []

    
        intervals.sort(key=lambda x: x.start)

        for interval in intervals:

            s = interval.start
            e = interval.end

            
            if pq and pq[0] <= s:
                heapq.heappop(pq)


            heapq.heappush(pq, e)

        return len(pq)