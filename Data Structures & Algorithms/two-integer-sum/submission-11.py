class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for r in range(len(nums)):
            diff = target - nums[r]
            if diff in freq:
                return [freq[diff], r]
            freq[nums[r]] = r