class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        counts = {}
        countt = {}

        for ch in s:
            counts[ch] = 1 + counts.get(ch, 0)

        for ch in t:
            countt[ch] = 1 + countt.get(ch, 0)

        return counts == countt