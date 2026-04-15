class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq = {}

        for ch in strs:
            key = "".join(sorted(ch))

            if key in freq:
                freq[key].append(ch)
            else:
                freq[key] = [ch]

        return list(freq.values())