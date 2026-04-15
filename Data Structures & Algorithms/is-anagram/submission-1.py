class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq = {}
        for ch in s :
            if ch in freq:
                freq[ch] += 1
            else :
                freq[ch] = 1
        tfreq = {}
        for ch in t:
            if ch in tfreq:
                tfreq[ch] += 1
            else:
                tfreq[ch]= 1

        if freq == tfreq:
            return True 
        else:
            return False