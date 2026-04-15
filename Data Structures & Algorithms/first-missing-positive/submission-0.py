class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        
         s = set(nums)
         for i in range(len(nums)):
            if i+1 not in s:
                return i+1
         return n