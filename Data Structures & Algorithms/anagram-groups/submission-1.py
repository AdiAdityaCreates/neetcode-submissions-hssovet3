class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq = {}

        for s in strs:
            key = tuple(sorted(s))   # convert to tuple (hashable)

            if key in freq:
                freq[key].append(s)  
            else:
                freq[key] = [s]

        return list(freq.values())