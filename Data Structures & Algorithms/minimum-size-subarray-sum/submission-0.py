class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        sum_a = 0
        l = 0

        for r in range(len(nums)):
            sum_a += nums[r]

            while sum_a >= target:
                res = min(res, r - l + 1)
                sum_a -= nums[l]
                l += 1

        return 0 if res == float('inf') else res