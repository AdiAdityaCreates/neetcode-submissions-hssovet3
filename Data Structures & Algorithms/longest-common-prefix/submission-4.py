from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = ""
        word = strs[0]

        for i in range(len(word)):
            for other in strs[1:]:
                if i >= len(other) or other[i] != word[i]:
                    return prefix
            prefix += word[i]

        return prefix