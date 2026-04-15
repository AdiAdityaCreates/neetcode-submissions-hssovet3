class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        for i in range(n-1):

            
            for i in range(n-1):
                if nums[i] > nums[i+1]:
                    nums[i],nums[i+1] = nums[i+1],nums[i]
            
        return nums
                