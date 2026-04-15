class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        for i in range(len(nums)-1):

            min_index = i
            for j in range(i+1,len(nums)):
                if nums[i] > nums[j]:
                    min_index = j
            nums[min_index],nums[i] = nums[i],nums[min_index]
