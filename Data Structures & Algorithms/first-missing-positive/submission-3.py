class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        freq = Counter(nums)
        for  i in range(len(nums)):
            if i+1 not in freq:
                return i+1
        return len(nums)+1