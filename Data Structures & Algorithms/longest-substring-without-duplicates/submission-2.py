from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       
        l = 0
        strs = defaultdict(int)
        res = 0
        for r in range(len(s)):
            strs[s[r]] += 1

            while strs[s[r]] > 1:
                strs[s[l]] -= 1
                l += 1
            res = max(res,r-l+1)
        return res
