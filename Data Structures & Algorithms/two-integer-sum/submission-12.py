class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        freq = defaultdict(int)
        for r in range(len(nums)):
            if target - nums[r] in freq:
                return [freq[nums[r]- target],r]
            freq[nums[r]] += r