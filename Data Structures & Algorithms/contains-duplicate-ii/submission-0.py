class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
      
        
        freq =  {}
        l = 0
        for r in range(len(nums)):

            if nums[r] in freq and r - freq[nums[r]] <=k:
                return True 
            freq[nums[r]] = r

        

        return False
                
