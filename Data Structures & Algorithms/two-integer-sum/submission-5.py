class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        l = 0
        res = []
        r = len(nums) -1 
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                res.append(l)
                res.append(r)
                l += 1
                r -= 1
            elif s > target:
                r -= 1
            else:
                l += 1

        return res
