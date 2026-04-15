class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:


        if not strs:
            return " "
        
        first_word = strs[0]

        for i in range(len(first_word)):

            c = first_word[i]
            for  other in strs[1:]:

                if i == len(other) or other[i] != c:
                    return first_word[:i]
        return first_word
                
        