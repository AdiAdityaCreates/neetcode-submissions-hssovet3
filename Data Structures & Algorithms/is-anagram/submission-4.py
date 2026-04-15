class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts ,countt = {},{}

        for  strs in s:
            counts[strs] = 1 + counts.get(strs,0)
        for strs in  t:
            countt[strs] = 1 + countt.get(strs,0)

        return counts == countt