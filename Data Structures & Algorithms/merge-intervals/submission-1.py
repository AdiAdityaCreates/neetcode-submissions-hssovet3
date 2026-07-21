class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])

        ans = [intervals[0]]

        for  s,e in intervals[1:]:

            if ans and ans[-1][1]  >= s:
                ans[-1][1] = max(ans[-1][1],e)
            else:
                ans.append([s,e])
        return ans