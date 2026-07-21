class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x:x[1])

        end = intervals[0][1]
        count = 0

        for s , e in intervals[1:]:

            if s < end:
                count += 1
            else:
                end = e
        return count
