class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for r in range(len(nums)):
            if target - nums[r] in freq:
                return [freq[target - nums[r]],r]
            freq[nums[r]] = r