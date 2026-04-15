class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        


        freq = {}
        for  s  in strs:
            c =tuple(sorted(s))
            if c in freq:
                freq[c].append(s)
            else:
                freq[c] = [s]
        return list(freq.values())