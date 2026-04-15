class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        prefix = [1]*len(nums)
        prefix[0] = 1
        res = [1]*len(nums)
        
        sufix =[1]*len(nums)
        sufix[len(nums)-1] = 1
        for i in range(1,len(nums)):
            prefix[i] = nums[i-1]*prefix[i-1]
        for i in range(len(nums)-2,-1,-1):
            sufix[i] = nums[i+1]*sufix[i+1]
        for i in range(len(nums)):
            res[i] = prefix[i]*sufix[i]
        return res
