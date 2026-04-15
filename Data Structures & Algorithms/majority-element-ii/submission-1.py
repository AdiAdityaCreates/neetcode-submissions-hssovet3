class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        freq = {}
        res = []
        freq =Counter(nums)
        
        for key in freq:
            if freq[key] >=3:
                res.append(key)
        return res