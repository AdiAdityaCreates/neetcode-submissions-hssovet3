class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        mp = defaultdict(int)
        mp[0] =1

        count = 0
        prefix = 0
        for r in range(len(nums)):
            prefix += nums[r]
            if prefix - k in mp:
                count += mp[prefix-k]
            mp[prefix] += 1
        return count