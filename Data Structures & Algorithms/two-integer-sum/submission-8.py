class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        l = 0
        res = []
        r = len(nums) -1 
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                return [l,r]
                
            elif s > target:
                r -= 1
            else:
                l += 1

        return res
