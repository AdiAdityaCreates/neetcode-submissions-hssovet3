class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        freq = {}  

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in freq:
                return [freq[comp], i]
            freq[nums[i]] = i  
        return [-1]