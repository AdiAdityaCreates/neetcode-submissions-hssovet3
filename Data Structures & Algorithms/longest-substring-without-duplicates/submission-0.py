class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strs= set()
        res = 0
        l = 0
        for r in range(len(s)):

            while s[r] in strs:
               
                strs.remove(s[l])
                l += 1
            strs.add(s[r])
            res = max(res,r-l+1)
        return res

       