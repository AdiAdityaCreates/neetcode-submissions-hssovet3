class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        ans = -1
        while l <=r:
            mid = l +(r-l)//2
            if nums[mid] <= target:
                ans = mid
                l = mid + 1
            else:
                r = mid-1
        return ans+1 if (nums[ans] != target) else ans