class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        freq = defaultdict(int)
        freq[0] = 1
        count = 0
        pref = 0
        for i in range(len(nums)):
            pref +=  nums[i]
            if pref - k in freq:
                count += freq[pref -k]
            freq[pref] += 1
        return count
        