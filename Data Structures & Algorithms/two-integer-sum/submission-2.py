class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        l = 0
        r = len(nums)-1

        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                return [l,r]
            if s > target:
                r -= 1
            else:
                l += 1